# ARCHITECTURAL_BRIEF: @ledgerhq_hw-transport-node-hid
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 7 analyzed artifact(s), 172 LOC.
- **Load-bearing artifact:** `package/src/listenDevices.ts` -- 1 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/src/TransportNodeHid.ts` -- pulls in 7 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/src/TransportNodeHid.ts` at magnitude 38.98 (structural weight, not risk).
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
| Total Artifacts | 10 |
| Analyzed Artifacts (Scanned) | 7 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3 |
| Total LOC | 172 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 70.0% |
| Dominant Lang | TYPESCRIPT |

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
| TYPESCRIPT | 3 | 165 | 42.9% |
| PLAINTEXT | 2 | 0 | 28.6% |
| MARKDOWN | 1 | 0 | 14.3% |
| JSON | 1 | 7 | 14.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 57%, Callbacks & Closures Files 29%, Declarative / Non-Code 14%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4 | 57.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 42.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3*

**Composition by Extension & Reason:**
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 80 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 50.7 | 15.9 | 6.4 | 5.1 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 75.0 | 31.7 | 26.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 97.7 | 24.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.5 | 2.4 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 27.8 | 12.7 | 11.5 | 20.1 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 71.8 | 18.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 99.7 | 31.8 | 13.7 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 36.1 | 22.2 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 0 | 0 | 0 | - |
| cleanup | 0 | 0 | 0 | - |
| guards | 1 | 1 | 0 | `package/src/TransportNodeHid.ts` |
| danger | 1 | 1 | 0 | `package/src/TransportNodeHid.ts` |
| concurrency | 8 | 2 | 2 | `package/src/TransportNodeHid.ts` |
| connectivity | 4 | 3 | 1 | `package/src/listenDevices.ts` |
| io | 9 | 3 | 1 | `package/src/TransportNodeHid.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 13 | 2 | 4 | `package/src/listenDevices.ts` |
| tests | 0 | 0 | 0 | - |
| docs | 8 | 1 | 0 | `package/src/TransportNodeHid.ts` |
| debt | 1 | 1 | 0 | `package/src/TransportNodeHid.ts` |
| mutation | 48 | 3 | 23 | `package/src/listenDevices.ts` |
| dead_code | 5 | 1 | 0 | `package/src/TransportNodeHid.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/TransportNodeHid.ts` (Hits: 7)
- `package/jest.config.ts` (Hits: 1)
- `package/src/listenDevices.ts` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **listenDevices.ts** (`package/src/listenDevices.ts`) — 1 inbound connections
2. **CHANGELOG.md** (`package/CHANGELOG.md`) — 0 inbound connections
3. **LICENSE.txt** (`package/LICENSE.txt`) — 0 inbound connections
4. **package.json** (`package/package.json`) — 0 inbound connections
5. **jest.config.ts** (`package/jest.config.ts`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **TransportNodeHid.ts** (`package/src/TransportNodeHid.ts`) — 7 outbound dependencies
2. **listenDevices.ts** (`package/src/listenDevices.ts`) — 5 outbound dependencies
3. **jest.config.ts** (`package/jest.config.ts`) — 3 outbound dependencies
4. **CHANGELOG.md** (`package/CHANGELOG.md`) — 0 outbound dependencies
5. **LICENSE.txt** (`package/LICENSE.txt`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `poll` **(I/O & Config Routines)** (@ `package/src/listenDevices.ts`) -> Impact: **10.9** | LOC: 39
- `listen` **(Callbacks & Closures)** (@ `package/src/TransportNodeHid.ts`) -> Impact: **5.3** | LOC: 22
  * *Intent:* /** */
- `onRemove` **(Callbacks & Closures)** (@ `package/src/TransportNodeHid.ts`) -> Impact: **4.9** | LOC: 13
- `onAdd` **(Callbacks & Closures)** (@ `package/src/TransportNodeHid.ts`) -> Impact: **4.8** | LOC: 12
- `open` **(Callbacks & Closures)** (@ `package/src/TransportNodeHid.ts`) -> Impact: **4.8** | LOC: 11
  * *Intent:* /** * if path="" is not provided, the library will take the first device */
- `listenDevicesPollingSkip` **(I/O & Config Routines)** (@ `package/src/TransportNodeHid.ts`) -> Impact: **3.2** | LOC: 24
- `attachDetected` **(Callbacks & Closures)** (@ `package/src/listenDevices.ts`) -> Impact: **1.9** | LOC: 9
- `setListenDevicesDebounce` **(Callbacks & Closures)** (@ `package/src/TransportNodeHid.ts`) -> Impact: **1.8** | LOC: 8
  * *Intent:* /** * */
- `setListenDevicesPollingSkip` **(Callbacks & Closures)** (@ `package/src/TransportNodeHid.ts`) -> Impact: **1.8** | LOC: 8
  * *Intent:* /** * */
- `detachDetected` **(Callbacks & Closures)** (@ `package/src/listenDevices.ts`) -> Impact: **1.8** | LOC: 8

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/src` | 2 | 76.84 | 29.16% | 48.85% |
| `package` | 5 | 52.4 | 1.02% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/src/TransportNodeHid.ts` -> **97.7023%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/src/listenDevices.ts` -> **99.7039%** Exposure
- `package/src/TransportNodeHid.ts` -> **27.4596%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/TransportNodeHid.ts` -> **5** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `13` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/src/TransportNodeHid.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 38.98 | **LOC:** 127 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 127.389; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.7%), Concurrency Surface (formerly Concurrency) (71.8%), Guard Balance (formerly Safety Score) (52.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 44.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `listen` **(Callbacks & Closures)** (Impact: 5.3)
    * *Intent:* /** */
  * `onRemove` **(Callbacks & Closures)** (Impact: 4.9)
  * `onAdd` **(Callbacks & Closures)** (Impact: 4.8)
  * `open` **(Callbacks & Closures)** (Impact: 4.8)
    * *Intent:* /** * if path="" is not provided, the library will take the first device */
  * `listenDevicesPollingSkip` **(I/O & Config Routines)** (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 29`, `args: 11`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 5`
* *Architecture:* `io: 7`, `api: 1`, `concurrency: 4`, `import: 6`
* *Defense:* `safety: 1`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 127.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` listenDevices, devices, errors, hw-transport, hw-transport-node-hid, hw-transport-node-hid-noevents, node-hid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/listenDevices.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 37.86 | **LOC:** 89 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 235.668; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (75.0%), Complexity Load (formerly Cognitive Load) (50.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll` **(I/O & Config Routines)** (Impact: 10.9)
  * `attachDetected` **(Callbacks & Closures)** (Impact: 1.9)
  * `detachDetected` **(Callbacks & Closures)** (Impact: 1.8)
  * `flatDevice` **(Callbacks & Closures)** (Impact: 1.7)
  * `getDeviceByPaths` **(Parameter Forwarders)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 23`, `args: 14`, `func_start: 6`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `io: 1`, `api: 2`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 235.668
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.166667
  * `Imports (Out-Degree: 0):` hw-transport-node-hid-noevents, logs, events, debounce, usb
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 20.98 | **LOC:** 1049 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 127.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/jest.config.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 15.16 | **LOC:** 11 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 127.389; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (20.1%), Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 127.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jest.config.ts, node:path, node:url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 13.64 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 127.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.62 | **LOC:** 81 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 127.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/LICENSE.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 22 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 127.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/listenDevices.ts` -> **Severity: 12.494** (Embedded: 0.1667 * Error Risk: 74.9655%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/listenDevices.ts` -> **Severity: 23566.8** (Blast Radius: 235.668 * Doc Risk: 100.0%)
- `package/src/TransportNodeHid.ts` -> **Severity: 5661.728** (Blast Radius: 127.389 * Doc Risk: 44.4444%)

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
