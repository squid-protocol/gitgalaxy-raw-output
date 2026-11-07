# ARCHITECTURAL_BRIEF: arktype
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/arktypeio/arktype.git` |
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
- **Scope:** 408 analyzed artifact(s), 58832 LOC.
- **Load-bearing artifact:** `ark/type/index.ts` -- 92 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `ark/schema/index.ts` -- pulls in 47 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `ark/attest/bench/await1k.ts` at magnitude 1075.54 (structural weight, not risk).
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
| Total Artifacts | 569 |
| Analyzed Artifacts (Scanned) | 408 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 161 |
| Total LOC | 58832 |
| Volatility Index | 0.01 |
| % Scanned of codebase = | 71.7% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7041 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1944 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 35.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7459 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 20 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 355 | 57092 | 87.0% |
| MARKDOWN | 19 | 0 | 4.7% |
| PLAINTEXT | 12 | 0 | 2.9% |
| JSON | 12 | 1304 | 2.9% |
| YAML | 5 | 139 | 1.2% |
| JAVASCRIPT | 5 | 297 | 1.2% |

## 4.1 SOURCE ENCODINGS
All 408 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 37%, Data / Markup / Trivial 14%, Large Core Modules (3) 14%, Callbacks & Closures Files 8%, Large Core Modules (2) 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 377 | 92.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 31 | 7.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 161*

**Composition by Extension & Reason:**
- `.tsx`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 415 LOC)
- `.json`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3502 LOC)
- `.mdx`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 11x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (Machine-Generated Source Code Signature: 42 LOC)
- `.2025-10-05`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wasm`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 68.1 | 8.7 | 3.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 23.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 31.3 | 19.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 20.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 98.2 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.7 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 89.8 | 4.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 47.3 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 177 | 75 | 2 | `ark/schema/roots/union.ts` |
| cleanup | 1 | 1 | 0 | `ark/attest/cli/trace.ts` |
| guards | 1646 | 190 | 12 | `ark/type/__tests__/nary.test.ts` |
| danger | 356 | 113 | 3 | `ark/type/__tests__/realWorld.test.ts` |
| concurrency | 1027 | 9 | 0 | `ark/attest/bench/await1k.ts` |
| connectivity | 2613 | 236 | 19 | `ark/type/keywords/string.ts` |
| io | 416 | 79 | 2 | `ark/fs/fs.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 4 | 4 | 0 | `ark/attest/cli/stats.ts` |
| time | 64 | 21 | 0 | `ark/type/__tests__/range.test.ts` |
| serialization | 39 | 24 | 0 | `ark/type/__tests__/pipe.test.ts` |
| regex | 73 | 37 | 0 | `ark/type/__tests__/match.test.ts` |
| events | 107 | 45 | 1 | `eslint.config.js` |
| tests | 1867 | 133 | 13 | `ark/regex/__tests__/regex.test.ts` |
| docs | 361 | 76 | 2 | `ark/type/variants/base.ts` |
| debt | 141 | 73 | 1 | `ark/type/__tests__/match.test.ts` |
| mutation | 7448 | 332 | 42 | `ark/type/nary.ts` |
| dead_code | 64 | 35 | 0 | `ark/type/__tests__/generateBenchData.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 4 | 1 | 0 | `ark/regex/__tests__/regex.test.ts` |
| ml_ai | 20 | 7 | 0 | `ark/attest/cli/trace.ts` |
| ui | 17 | 8 | 0 | `ark/schema/structure/structure.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ark/fs/fs.ts` (Hits: 47)
- `ark/schema/roots/union.ts` (Hits: 27)
- `ark/type/__tests__/discrimination.test.ts` (Hits: 23)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.ts** (`ark/type/index.ts`) — 92 inbound connections
2. **implement.ts** (`ark/schema/shared/implement.ts`) — 39 inbound connections
3. **attributes.ts** (`ark/type/attributes.ts`) — 37 inbound connections
4. **registry.ts** (`ark/schema/shared/registry.ts`) — 33 inbound connections
5. **root.ts** (`ark/schema/roots/root.ts`) — 31 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`ark/schema/index.ts`) — 47 outbound dependencies
2. **root.ts** (`ark/schema/roots/root.ts`) — 26 outbound dependencies
3. **kinds.ts** (`ark/schema/kinds.ts`) — 24 outbound dependencies
4. **index.ts** (`ark/util/index.ts`) — 24 outbound dependencies
5. **structure.ts** (`ark/schema/structure/structure.ts`) — 23 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_intersectSequences` **(Compute Cores)** (@ `ark/schema/structure/sequence.ts`) -> Impact: **86.8** | LOC: 123
- `constructor` **(Many-Argument Workhorses)** (@ `ark/schema/node.ts`) -> Impact: **72.0** | LOC: 124
- `_traverse` **(Many-Argument Workhorses)** (@ `ark/schema/structure/structure.ts`) -> Impact: **70.0** | LOC: 79
- `structure` **(Many-Argument Workhorses)** (@ `ark/schema/structure/structure.ts`) -> Impact: **59.5** | LOC: 109
- `get` **(Defensive Guards)** (@ `ark/schema/structure/structure.ts`) -> Impact: **55.2** | LOC: 65
- `_transform` **(Many-Argument Workhorses)** (@ `ark/schema/node.ts`) -> Impact: **53.2** | LOC: 95
- `await1K` **(Compute Cores)** (@ `ark/attest/bench/await1k.ts`) -> Impact: **51.5** | LOC: 1002
- `reduceObjectJsonSchema` **(Many-Argument Workhorses)** (@ `ark/schema/structure/structure.ts`) -> Impact: **50.3** | LOC: 106
- `parseObjectLiteral` **(Many-Argument Workhorses)** (@ `ark/type/parser/objectLiteral.ts`) -> Impact: **49.3** | LOC: 119
- `intersectProps` **(Many-Argument Workhorses)** (@ `ark/schema/structure/prop.ts`) -> Impact: **46.2** | LOC: 45

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `ark/util` | 28 | 2022.96 | 17.49% | 1.68% |
| `ark/attest/bench` | 6 | 1409.14 | 16.23% | 0.0% |
| `ark/type/__tests__` | 54 | 1170.26 | 1.37% | 0.62% |
| `ark/type` | 14 | 770.38 | 7.28% | 4.45% |
| `ark/attest/cache` | 5 | 488.08 | 14.55% | 0.0% |
| `ark/type/parser` | 6 | 478.66 | 13.24% | 0.0% |
| `ark/type/keywords` | 9 | 462.24 | 4.82% | 1.46% |
| `ark/attest/cli` | 4 | 426.66 | 20.22% | 11.61% |
| `ark/fs` | 6 | 372.16 | 21.02% | 1.65% |
| `ark/json-schema` | 13 | 354.14 | 16.2% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `ark/type/__tests__/integration/testSimpleConfig.ts` -> **99.9925%** Exposure
- `ark/type/__tests__/integration/testEoptConfig.ts` -> **81.7574%** Exposure
- `ark/schema/roots/morph.ts` -> **77.4349%** Exposure
- `ark/util/__tests__/traits.scratch.ts` -> **74.4868%** Exposure
- `ark/extension/arktype.scratch.ts` -> **71.4798%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `ark/schema/shared/errors.ts` -> **100.0%** Exposure
- `ark/schema/shared/intersections.ts` -> **100.0%** Exposure
- `ark/schema/shared/registry.ts` -> **100.0%** Exposure
- `ark/schema/shared/traversal.ts` -> **100.0%** Exposure
- `ark/util/clone.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `ark/type/__tests__/match.test.ts` -> **5** Orphaned Functions | **17** Duplicates
- `ark/type/__tests__/integration/testSimpleConfig.ts` -> **6** Orphaned Functions | **0** Duplicates
- `ark/type/__tests__/select.test.ts` -> **0** Orphaned Functions | **5** Duplicates
- `ark/extension/arktype.scratch.ts` -> **4** Orphaned Functions | **0** Duplicates
- `ark/schema/__tests__/errors.test.ts` -> **0** Orphaned Functions | **4** Duplicates

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
- **Unknown Dependencies:** `752` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `ark/attest/bench/await1k.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.754)
- **Top Global Matches:** file_cluster_2: 7.754, file_cluster_15: 7.806, file_cluster_17: 8.54
- **Magnitude:** 1075.54 | **LOC:** 1003 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.856; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (11.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `await1K` **(Compute Cores)** (Impact: 51.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1005`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 1003`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.856
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.020156
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ark/util/flatMorph.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.039)
- **Top Global Matches:** file_cluster_5: 7.039, file_cluster_0: 9.915, file_cluster_12: 10.464
- **Magnitude:** 569.98 | **LOC:** 110 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 2.524; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.2%), Connectivity (formerly Api Exposure) (50.4%), Mutation Surface (formerly State Flux) (37.3%), Complexity Load (formerly Cognitive Load) (21.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 72`, `args: 4`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.524
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.046499
  * `Imports (Out-Degree: 5):` arrays.ts, generics.ts, keys.ts, records.ts, unionToTuple.ts
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ark/attest/cli/trace.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.179)
- **Top Global Matches:** file_cluster_15: 7.179, file_cluster_10: 7.281, file_cluster_12: 7.378
- **Magnitude:** 362.28 | **LOC:** 788 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.51; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.1%), Complexity Load (formerly Cognitive Load) (27.3%)
- **Documentation Coverage:** 91.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findNodeByPreference` **(Compute Cores)** (Impact: 19.8)
  * `analyzeTypeInstantiations` **(Defensive Guards)** (Impact: 16.7)
  * `findCallExpressionInRange` **(Compute Cores)** (Impact: 15.2)
  * `processDurationEntry` **(Many-Argument Workhorses)** (Impact: 14.9)
  * `collectFunctionStats` **(Compute Cores)** (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 34 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 136`, `args: 58`, `func_start: 34`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 44`, `unreferenced_by_name: 1`
* *Architecture:* `io: 17`, `api: 3`, `concurrency: 3`, `import: 9`
* *Defense:* `safety: 12`, `doc: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.51
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ts.ts, config.ts, shared.ts, fs, node:child_process, node:fs, node:path, typescript
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ark/type/keywords/string.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.746)
- **Top Global Matches:** file_cluster_15: 5.746, file_cluster_10: 7.452, file_cluster_0: 8.05
- **Magnitude:** 224.3 | **LOC:** 968 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 2.82; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (50.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.0%), Mutation Surface (formerly State Flux) (21.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tryParseDatePattern` **(Compute Cores)** (Impact: 26.2)
  * `isLuhnValid` **(Compute Cores)** (Impact: 9.4)
    * *Intent:* // https://github.com/validatorjs/validator.js/blob/master/src/lib/isLuhnNumber.js
  * `regexStringNode` **(Compute Cores)** (Impact: 6.9)
    * *Intent:* // non-trivial expressions should have an explanation or attribution
  * `isParsableDate` **(Compute Cores)** (Impact: 4.6)
  * `parseJson` **(Defensive Guards)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 341`, `args: 42`, `func_start: 21`
* *Risk/State:* `state_mutation: 8`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 100`, `import: 6`
* *Defense:* `safety: 9`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.82
  * `Choke Point (Betweenness):` 6e-05 | `Ripple Effect (Closeness):` 0.126795
  * `Imports (Out-Degree: 4):` attributes.ts, module.ts, scope.ts, number.ts, schema, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ark/type/nary.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.786)
- **Top Global Matches:** file_cluster_0: 5.786, file_cluster_2: 9.381, file_cluster_13: 9.806
- **Magnitude:** 204.82 | **LOC:** 2649 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 6.307; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.5%), Mutation Surface (formerly State Flux) (39.7%), Connectivity (formerly Api Exposure) (26.1%), Complexity Load (formerly Cognitive Load) (9.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 1565`
* *Risk/State:* `state_mutation: 67`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.307
  * `Choke Point (Betweenness):` 0.000485 | `Ripple Effect (Closeness):` 0.128564
  * `Imports (Out-Degree: 5):` attributes.ts, keywords.ts, type.ts, instantiate.ts, object.ts, schema, util
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ark/fs/fs.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.984)
- **Top Global Matches:** file_cluster_12: 7.984, file_cluster_5: 9.788, file_cluster_15: 9.868
- **Magnitude:** 189.76 | **LOC:** 242 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 0.952; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.3%), Guard Balance (formerly Safety Score) (54.7%)
- **Documentation Coverage:** 89.4737% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `walkPaths` **(Defensive Guards)** (Impact: 28.8)
  * `cpR` **(Compute Cores)** (Impact: 12.8)
  * `findPackageRoot` **(Defensive Guards)** (Impact: 8.0)
  * `findPackageAncestors` **(Defensive Guards)** (Impact: 7.8)
  * `filePath` **(Callbacks & Closures)** (Impact: 6.3)
    * *Intent:* /** Fetch the file and directory paths from a path, uri, or `import.meta.url` */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 110`, `args: 44`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 10`, `planned_debt: 1`
* *Architecture:* `io: 47`, `api: 35`, `import: 9`
* *Defense:* `safety: 10`, `doc: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.952
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.006143
  * `Imports (Out-Degree: 2):` caller.ts, shell.ts, node:fs, node:os, node:path, node:process, node:url
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ark/util/arrays.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.193)
- **Top Global Matches:** file_cluster_0: 8.193, file_cluster_5: 10.031, file_cluster_12: 11.132
- **Magnitude:** 183.9 | **LOC:** 510 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **4**; blast radius 9.52; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (90.3%), Guard Balance (formerly Safety Score) (54.0%), Mutation Surface (formerly State Flux) (46.9%), Complexity Load (formerly Cognitive Load) (19.8%)
- **Documentation Coverage:** 61.5385% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getDuplicatesOf` **(Defensive Guards)** (Impact: 17.8)
    * *Intent:* /** * Extracts duplicated elements and their indices from an array, returning them. * * Note that gi...
  * `appendUnique` **(Defensive Guards)** (Impact: 16.7)
    * *Intent:* /** * Appends a value or concatenates an array to an array if it is not already included, returning ...
  * `conflatenate` **(Defensive Guards)** (Impact: 10.9)
    * *Intent:* /** * Concatenates an element or list with a readonly list */
  * `arrayEquals` **(Defensive Guards)** (Impact: 10.7)
  * `getPath` **(Callbacks & Closures)** (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 316`, `args: 22`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 14`
* *Architecture:* `io: 2`, `api: 44`, `import: 4`
* *Defense:* `safety: 8`, `doc: 7`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.52
  * `Choke Point (Betweenness):` 0.00048 | `Ripple Effect (Closeness):` 0.055904
  * `Imports (Out-Degree: 4):` functions.ts, generics.ts, intersections.ts, numbers.ts
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `ark/attest/assert/chainableAssertions.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.4)
- **Top Global Matches:** file_cluster_12: 6.4, file_cluster_5: 6.869, file_cluster_0: 9.402
- **Magnitude:** 182.96 | **LOC:** 393 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 0.999; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (80.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.8%), Connectivity (formerly Api Exposure) (43.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `snap` **(Defensive Guards)** (Impact: 17.7)
  * `toFile` **(Defensive Guards)** (Impact: 14.8)
  * `inline` **(Defensive Guards)** (Impact: 12.7)
    * *Intent:* // Use variadic args to distinguish undefined being passed explicitly from no args
  * `immediateAssertion` **(Compute Cores)** (Impact: 10.7)
  * `unwrap` **(Defensive Guards)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 158`, `args: 40`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 16`
* *Architecture:* `io: 4`, `api: 19`, `import: 12`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.999
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.019009
  * `Imports (Out-Degree: 6):` snapshots.ts, writeAssertionCache.ts, config.ts, utils.ts, assertions.ts, attest.ts, fs, util...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ark/attest/bench/bench.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.487)
- **Top Global Matches:** file_cluster_0: 7.487, file_cluster_12: 8.63, file_cluster_10: 8.871
- **Magnitude:** 179.56 | **LOC:** 362 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **9**; blast radius 2.846; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.2%), Mutation Surface (formerly State Flux) (97.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `benchFn` **(Many-Argument Workhorses)** (Impact: 15.6)
  * `createAssertion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `createStatMethod` **(Stateful Encapsulated Methods)** (Impact: 6.5)
  * `markAssertion` **(Stateful Encapsulated Methods)** (Impact: 4.8)
  * `loopCalls` **(Callbacks & Closures)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 29
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 115`, `args: 38`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 21`
* *Architecture:* `io: 1`, `api: 14`, `concurrency: 9`, `import: 9`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.846
  * `Choke Point (Betweenness):` 0.000511 | `Ripple Effect (Closeness):` 0.029285
  * `Imports (Out-Degree: 7):` config.ts, utils.ts, await1k.ts, baseline.ts, call1k.ts, measure.ts, type.ts, fs...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `ark/util/serialize.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.325)
- **Top Global Matches:** file_cluster_3: 11.325, file_cluster_8: 15.969, file_cluster_6: 28.232
- **Magnitude:** 178.2 | **LOC:** 241 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 0.941; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (76.3%), Connectivity (formerly Api Exposure) (57.0%), Guard Balance (formerly Safety Score) (47.4%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_serialize` **(Defensive Guards)** (Impact: 44.2)
  * `stringifyUnquoted` **(Many-Argument Workhorses)** (Impact: 36.2)
  * `printable` **(Defensive Guards)** (Impact: 30.3)
  * `describeCollapsibleDate` **(Compute Cores)** (Impact: 26.0)
    * *Intent:* /** * Converts a Date instance to a human-readable description relative to its precision */
  * `print` **(Parameter Forwarders)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 99`, `args: 20`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`
* *Architecture:* `api: 12`, `import: 5`
* *Defense:* `safety: 16`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.941
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.027654
  * `Imports (Out-Degree: 5):` arrays.ts, domain.ts, primitive.ts, records.ts, registry.ts
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ark/attest/cache/ts.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.184)
- **Top Global Matches:** file_cluster_12: 6.184, file_cluster_10: 8.92, file_cluster_15: 9.051
- **Magnitude:** 156.58 | **LOC:** 339 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **7**; blast radius 1.997; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (77.7%), Connectivity (formerly Api Exposure) (68.5%), Guard Balance (formerly Safety Score) (54.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nearestBoundingCallExpression` **(Defensive Guards)** (Impact: 11.0)
  * `constructor` **(Compute Cores)** (Impact: 10.3)
  * `getSourceFileOrThrow` **(Compute Cores)** (Impact: 8.6)
  * `instantiateTsconfigFromPath` **(Defensive Guards)** (Impact: 7.2)
  * `getStringifiableType` **(Compute Cores)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 81`, `args: 34`, `func_start: 24`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 12`
* *Architecture:* `io: 18`, `api: 22`, `import: 7`
* *Defense:* `safety: 11`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.030387
  * `Imports (Out-Degree: 1):` config.ts, fs, util, vfs, node:fs, node:path, typescript
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `ark/util/numbers.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.653)
- **Top Global Matches:** file_cluster_0: 6.653, file_cluster_15: 9.503, file_cluster_16: 10.951
- **Magnitude:** 147.74 | **LOC:** 269 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 4.491; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (77.8%), Guard Balance (formerly Safety Score) (52.8%), Complexity Load (formerly Cognitive Load) (33.5%)
- **Documentation Coverage:** 91.3043% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseNumeric` **(Defensive Guards)** (Impact: 27.2)
  * `nearestFloat` **(Compute Cores)** (Impact: 19.9)
    * *Intent:* * * console.log(nearestFloat(0)); // Smallest positive number * console.log(nearestFloat(2)); // 2.0...
  * `createNumberMatcher` **(Compute Cores)** (Impact: 8.0)
  * `tryParseWellFormedBigint` **(Defensive Guards)** (Impact: 6.6)
  * `isNumberLike` **(Compute Cores)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 106`, `args: 13`, `func_start: 12`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 26`, `import: 3`
* *Defense:* `safety: 6`, `doc: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.491
  * `Choke Point (Betweenness):` 0.000165 | `Ripple Effect (Closeness):` 0.047385
  * `Imports (Out-Degree: 2):` $token, errors.ts, strings.ts
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `ark/fast-check/arktypeFastCheck.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.887)
- **Top Global Matches:** file_cluster_8: 9.887, file_cluster_6: 11.177, file_cluster_4: 18.583
- **Magnitude:** 147.6 | **LOC:** 209 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 2.397; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (53.5%), Complexity Load (formerly Cognitive Load) (49.8%), Connectivity (formerly Api Exposure) (33.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildArbitrary` **(Defensive Guards)** (Impact: 45.2)
  * `buildStructureArbitrary` **(Defensive Guards)** (Impact: 29.6)
  * `buildObjectArbitrary` **(Generic / Templated Code)** (Impact: 7.7)
  * `buildIndexSignatureArbitrary` **(Callbacks & Closures)** (Impact: 7.7)
  * `getSpreadVariadicElementsTuple` **(Compute Cores)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 74`, `args: 12`, `func_start: 8`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `api: 3`, `import: 9`
* *Defense:* `safety: 10`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.397
  * `Choke Point (Betweenness):` 0.000182 | `Ripple Effect (Closeness):` 0.012039
  * `Imports (Out-Degree: 5):` array.ts, domain.ts, object.ts, proto.ts, fastCheckContext.ts, schema, util, arktype...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `ark/type/parser/reduce/dynamic.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.561)
- **Top Global Matches:** file_cluster_12: 5.561, file_cluster_5: 6.962, file_cluster_15: 8.8
- **Magnitude:** 131.1 | **LOC:** 237 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **8**; blast radius 7.452; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (69.1%), Complexity Load (formerly Cognitive Load) (61.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushRootToBranch` **(Defensive Guards)** (Impact: 13.9)
  * `previousOperator` **(Defensive Guards)** (Impact: 7.7)
  * `reduceLeftBound` **(Compute Cores)** (Impact: 6.2)
  * `finalizeBranches` **(I/O & Config Routines)** (Impact: 5.2)
  * `applyPrefixes` **(Generic / Templated Code)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 54`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 23`
* *Architecture:* `api: 14`, `import: 8`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.452
  * `Choke Point (Betweenness):` 0.002029 | `Ripple Effect (Closeness):` 0.133533
  * `Imports (Out-Degree: 6):` attributes.ts, operand.ts, operator.ts, tokens.ts, string.ts, shared.ts, schema, util
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `ark/type/parser/objectLiteral.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 13.016)
- **Top Global Matches:** file_cluster_8: 13.016, file_cluster_3: 15.267, file_cluster_6: 24.457
- **Magnitude:** 128.44 | **LOC:** 356 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **5**; blast radius 4.17; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (61.1%), Guard Balance (formerly Safety Score) (51.1%), Mutation Surface (formerly State Flux) (31.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseObjectLiteral` **(Many-Argument Workhorses)** (Impact: 49.3)
  * `preparseKey` **(Generic / Templated Code)** (Impact: 34.1)
  * `writeInvalidUndeclaredBehaviorMessage` **(Generic / Templated Code)** (Impact: 3.6)
  * `appendNamedProp` **(Generic / Templated Code)** (Impact: 2.8)
  * `writeInvalidSpreadTypeMessage` **(Generic / Templated Code)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 124`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 18`, `import: 7`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.17
  * `Choke Point (Betweenness):` 0.000236 | `Ripple Effect (Closeness):` 0.122307
  * `Imports (Out-Degree: 3):` validate.ts, definition.ts, property.ts, schema, util
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `ark/type/parser/tupleLiteral.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.466)
- **Top Global Matches:** file_cluster_0: 7.466, file_cluster_9: 9.369, file_cluster_15: 10.18
- **Magnitude:** 128.18 | **LOC:** 397 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **4**; blast radius 3.83; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (77.4%), Connectivity (formerly Api Exposure) (60.0%), Guard Balance (formerly Safety Score) (54.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseTupleLiteral` **(Compute Cores)** (Impact: 22.0)
  * `appendSpreadBranch` **(Compute Cores)** (Impact: 16.6)
  * `appendRequiredElement` **(Compute Cores)** (Impact: 11.5)
  * `appendVariadicElement` **(Compute Cores)** (Impact: 9.6)
  * `appendDefaultableElement` **(Compute Cores)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 147`, `args: 11`, `func_start: 7`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 18`, `import: 6`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.83
  * `Choke Point (Betweenness):` 0.00018 | `Ripple Effect (Closeness):` 0.123399
  * `Imports (Out-Degree: 2):` definition.ts, property.ts, schema, util
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `ark/type/scope.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.734)
- **Top Global Matches:** file_cluster_0: 6.734, file_cluster_5: 8.576, file_cluster_12: 9.293
- **Magnitude:** 118.88 | **LOC:** 481 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **16**; blast radius 26.618; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (93.1%), Guard Balance (formerly Safety Score) (50.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (24.6%), Mutation Surface (formerly State Flux) (15.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `preparseOwnAliasEntry` **(Stateful Encapsulated Methods)** (Impact: 17.6)
  * `parseOwnDefinitionFormat` **(Compute Cores)** (Impact: 13.1)
  * `normalizeRootScopeValue` **(Encapsulated Accessors)** (Impact: 4.5)
  * `preparseOwnDefinitionFormat` **(Stateful Encapsulated Methods)** (Impact: 4.0)
  * `ambientAttachments` **(Type Conversions)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 268`, `args: 33`, `func_start: 22`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`
* *Architecture:* `api: 35`, `import: 17`
* *Defense:* `safety: 4`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.618
  * `Choke Point (Betweenness):` 0.008945 | `Ripple Effect (Closeness):` 0.183663
  * `Imports (Out-Degree: 14):` declare.ts, fn.ts, generic.ts, keywords.ts, match.ts, module.ts, nary.ts, infer.ts...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `ark/type/match.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.75)
- **Top Global Matches:** file_cluster_0: 7.75, file_cluster_15: 9.554, file_cluster_12: 10.105
- **Magnitude:** 114.84 | **LOC:** 462 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 6.728; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.7%), Mutation Surface (formerly State Flux) (53.0%), Connectivity (formerly Api Exposure) (43.8%), Complexity Load (formerly Cognitive Load) (15.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `default` **(Compute Cores)** (Impact: 14.2)
  * `caseEntries` **(Stateful Encapsulated Methods)** (Impact: 9.7)
  * `at` **(Compute Cores)** (Impact: 9.0)
  * `constructor` **(Type Conversions)** (Impact: 5.7)
  * `case` **(Compute Cores)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 249`, `args: 38`, `func_start: 14`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`
* *Architecture:* `api: 14`, `import: 11`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.728
  * `Choke Point (Betweenness):` 0.000351 | `Ripple Effect (Closeness):` 0.131312
  * `Imports (Out-Degree: 5):` attributes.ts, keywords.ts, string.ts, scope.ts, base.ts, schema, util
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `ark/util/scanner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.737)
- **Top Global Matches:** file_cluster_0: 6.737, file_cluster_5: 9.635, file_cluster_12: 9.96
- **Magnitude:** 112.18 | **LOC:** 190 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.804; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.0%), Guard Balance (formerly Safety Score) (57.4%)
- **Documentation Coverage:** 93.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `shiftUntilEscapable` **(Compute Cores)** (Impact: 14.8)
  * `shiftUntil` **(Compute Cores)** (Impact: 6.1)
  * `sliceChars` **(Parameter Forwarders)** (Impact: 3.6)
  * `shiftUntilLookahead` **(Parameter Forwarders)** (Impact: 3.1)
  * `jumpToIndex` **(Parameter Forwarders)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 90`, `args: 23`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 14`
* *Architecture:* `api: 22`, `import: 2`
* *Defense:* `safety: 5`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.804
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025852
  * `Imports (Out-Degree: 2):` records.ts, strings.ts
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ark/util/records.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.891)
- **Top Global Matches:** file_cluster_5: 6.891, file_cluster_0: 9.449, file_cluster_12: 11.294
- **Magnitude:** 111.62 | **LOC:** 367 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **8**; blast radius 16.186; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (54.0%), Mutation Surface (formerly State Flux) (22.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.7%)
- **Documentation Coverage:** 59.2593% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hasDefinedKey` **(Generic / Templated Code)** (Impact: 9.5)
    * *Intent:* // must be defined this way to avoid https://github.com/microsoft/TypeScript/issues/55049
  * `splitByKeys` **(Generic / Templated Code)** (Impact: 4.8)
  * `isKeyOf` **(Generic / Templated Code)** (Impact: 3.9)
  * `withAlphabetizedKeys` **(Generic / Templated Code)** (Impact: 3.2)
    * *Intent:* /** Copies enumerable keys of o to a new object in alphabetical order */
  * `enumValues` **(Generic / Templated Code)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 268`, `args: 23`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 4`
* *Architecture:* `api: 56`, `import: 8`
* *Defense:* `safety: 5`, `doc: 15`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.186
  * `Choke Point (Betweenness):` 0.00074 | `Ripple Effect (Closeness):` 0.058534
  * `Imports (Out-Degree: 8):` arrays.ts, domain.ts, errors.ts, flatMorph.ts, functions.ts, generics.ts, keys.ts, unionToTuple.ts
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `ark/attest/cache/writeAssertionCache.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.863)
- **Top Global Matches:** file_cluster_12: 6.863, file_cluster_5: 8.684, file_cluster_10: 8.949
- **Magnitude:** 110.76 | **LOC:** 352 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **7**; blast radius 2.935; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.4%), Guard Balance (formerly Safety Score) (52.7%), Mutation Surface (formerly State Flux) (33.0%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getJSDocFromSymbol` **(Compute Cores)** (Impact: 23.4)
    * *Intent:* /** * Extract JSDoc comments from a symbol's declarations */
  * `getCompletions` **(Defensive Guards)** (Impact: 14.9)
  * `extractJSDocFromArgument` **(Compute Cores)** (Impact: 11.2)
    * *Intent:* /** * Extract JSDoc comments associated with the first argument of a call expression */
  * `checkDiagnosticMessages` **(Compute Cores)** (Impact: 9.6)
  * `analyzeProjectAssertions` **(I/O & Config Routines)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 91`, `args: 22`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 8`
* *Architecture:* `io: 3`, `api: 17`, `import: 7`
* *Defense:* `safety: 6`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.935
  * `Choke Point (Betweenness):` 0.000222 | `Ripple Effect (Closeness):` 0.035823
  * `Imports (Out-Degree: 4):` config.ts, utils.ts, ts.ts, utils.ts, fs, util, typescript
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `ark/attest/config.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.528)
- **Top Global Matches:** file_cluster_12: 8.528, file_cluster_0: 8.656, file_cluster_15: 8.741
- **Magnitude:** 109.74 | **LOC:** 213 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **7**; blast radius 5.651; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Connectivity (formerly Api Exposure) (67.6%), Guard Balance (formerly Safety Score) (57.0%), Debt Markers (formerly Tech Debt) (37.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getParamValue` **(Compute Cores)** (Impact: 21.2)
  * `addEnvConfig` **(Compute Cores)** (Impact: 13.6)
  * `parseTsVersions` **(Callbacks & Closures)** (Impact: 7.9)
  * `hasFlag` **(Defensive Guards)** (Impact: 4.5)
  * `isTsVersionAliases` **(Defensive Guards)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 57`, `args: 15`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`, `fragile_debt: 2`
* *Architecture:* `io: 5`, `api: 8`, `import: 7`
* *Defense:* `safety: 4`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.651
  * `Choke Point (Betweenness):` 7.9e-05 | `Ripple Effect (Closeness):` 0.046069
  * `Imports (Out-Degree: 1):` tsVersioning.ts, fs, util, node:fs, node:path, prettier, typescript
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `ark/json-schema/object.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.736)
- **Top Global Matches:** file_cluster_12: 6.736, file_cluster_10: 7.749, file_cluster_15: 8.383
- **Magnitude:** 107.12 | **LOC:** 275 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.787; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.0%), Guard Balance (formerly Safety Score) (56.8%), Complexity Load (formerly Cognitive Load) (26.2%), Connectivity (formerly Api Exposure) (16.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseRequiredAndOptionalKeys` **(Compute Cores)** (Impact: 21.2)
  * `parseAdditionalProperties` **(Defensive Guards)** (Impact: 9.6)
  * `parseMinMaxProperties` **(Defensive Guards)** (Impact: 9.5)
  * `jsonSchemaObjectAdditionalPropertiesValidator` **(Defensive Guards)** (Impact: 8.1)
  * `jsonSchemaObjectMaxPropertiesValidator` **(Callbacks & Closures)** (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 59`, `args: 18`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 14`
* *Architecture:* `io: 2`, `api: 1`, `import: 6`
* *Defense:* `safety: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.787
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.010238
  * `Imports (Out-Degree: 3):` errors.ts, json.ts, scope.ts, schema, util, arktype
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ark/type/__tests__/match.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.092)
- **Top Global Matches:** file_cluster_10: 6.092, file_cluster_15: 6.811, file_cluster_11: 7.857
- **Magnitude:** 105.06 | **LOC:** 919 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.51; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.1%), Mutation Surface (formerly State Flux) (8.9%), Complexity Load (formerly Cognitive Load) (3.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `default` **(Compute Cores)** (Impact: 2.9)
  * `default` **(Compute Cores)** (Impact: 2.9)
  * `three` **(Callbacks & Closures)** (Impact: 1.7)
  * `_matchOverlapping1` **(Parameter Forwarders)** (Impact: 1.6)
  * `_matchOverlapping2` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* // this will never be hit since it is a subtype of a previous case
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 265`, `args: 183`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`, `duplicate_logic: 17`, `unreferenced_by_name: 5`
* *Architecture:* `io: 3`, `import: 5`
* *Defense:* `safety: 11`, `test: 46`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.51
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` attest, schema, arktype, attributes.ts, match.ts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ark/regex/state.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.439)
- **Top Global Matches:** file_cluster_0: 7.439, file_cluster_9: 10.605, file_cluster_16: 11.945
- **Magnitude:** 98.28 | **LOC:** 775 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **4**; blast radius 12.139; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (85.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.7%), Complexity Load (formerly Cognitive Load) (6.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (3.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeIncompleteReferenceError` **(Generic / Templated Code)** (Impact: 24.2)
  * `writeMidAnchorError` **(Generic / Templated Code)** (Impact: 1.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 394`, `args: 2`, `func_start: 1`, `class_start: 8`
* *Risk/State:* None
* *Architecture:* `api: 59`, `import: 24`
* *Defense:* `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.139
  * `Choke Point (Betweenness):` 0.000182 | `Ripple Effect (Closeness):` 0.01755
  * `Imports (Out-Degree: 3):` escape.ts, quantify.ts, regex.ts, util
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `ark/util/__tests__/records.test.ts` (TYPESCRIPT) | Magnitude: 21.68 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 126, structural_boundaries: 30, branch: 20, core_var_decl: 18
- `ark/regex/__tests__/regex.test.ts` (TYPESCRIPT) | Magnitude: 37.66 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 1103, structural_boundaries: 381, args: 252, closures: 252
- `ark/json-schema/scope.ts` (TYPESCRIPT) | Magnitude: 19.62 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 65, structural_boundaries: 29, core_var_decl: 11, design_pascal_case: 11
- `ark/type/__tests__/integration/util.ts` (TYPESCRIPT) | Magnitude: 9.58 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 15, structural_boundaries: 6, core_var_decl: 3, design_snake_case: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `ark/type/__tests__/keywords/formData.test.ts` (TYPESCRIPT) | Magnitude: 17.86 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 35, structural_boundaries: 12, core_var_decl: 5, args: 4
- `ark/attest/cache/getCachedAssertions.ts` (TYPESCRIPT) | Magnitude: 38.74 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 76, structural_boundaries: 40, core_var_decl: 19, design_camel_case: 12
- `ark/type/__tests__/typeReference.test.ts` (TYPESCRIPT) | Magnitude: 16.64 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 27, indent_tabs: 27, args: 8, closures: 8
- `ark/type/__tests__/unenclosed.test.ts` (TYPESCRIPT) | Magnitude: 17.04 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 96, structural_boundaries: 61, args: 34, closures: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `ark/attest/__tests__/assertions.test.ts` (TYPESCRIPT) | Magnitude: 18.64 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 168, structural_boundaries: 86, args: 37, closures: 37
- `ark/attest/config.ts` (TYPESCRIPT) | Magnitude: 109.74 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 113, structural_boundaries: 57, branch: 37, core_var_decl: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `ark/repo/publish.ts` (TYPESCRIPT) | Magnitude: 31.4 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 14, branch: 8, structural_boundaries: 8, core_var_decl: 5
- `ark/schema/index.ts` (TYPESCRIPT) | Magnitude: 3.15 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 49, api: 47, import: 47, decorators: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `ark/attest/cli/trace.ts` (TYPESCRIPT) | Magnitude: 362.28 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 600, core_var_decl: 150, structural_boundaries: 136, branch: 106
- `ark/schema/roots/morph.ts` (TYPESCRIPT) | Magnitude: 5.6 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 192, structural_boundaries: 102, branch: 43, args: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `ark/util/index.ts` (TYPESCRIPT) | Magnitude: 39.48 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 24, api: 24, import: 24, io: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `ark/attest/bench/await1k.ts` (TYPESCRIPT) | Magnitude: 1075.54 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 1005, concurrency: 1003, indent_tabs: 1000, closures: 2
- `eslint.config.js` (JAVASCRIPT) | Magnitude: 21.2 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 202, doc: 44, decorators: 28, structural_boundaries: 22
- `ark/repo/nodeOptions.js` (JAVASCRIPT) | Magnitude: 14.72 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 7, state_mutation: 5, structural_boundaries: 4, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `ark/type/__tests__/badDefinitionType.test.ts` (TYPESCRIPT) | Magnitude: 15.92 | Delta: **0.157** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 41, structural_boundaries: 36, args: 17, closures: 17

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `ark/attest/cli/trace.ts` -> **David Blass** (100.0% isolated ownership) | Magnitude: 362.28
- `ark/fs/fs.ts` -> **David Blass** (100.0% isolated ownership) | Magnitude: 189.76
- `ark/util/serialize.ts` -> **David Blass** (100.0% isolated ownership) | Magnitude: 178.2
- `ark/attest/cache/ts.ts` -> **David Blass** (100.0% isolated ownership) | Magnitude: 156.58
- `ark/type/parser/reduce/dynamic.ts` -> **David Blass** (100.0% isolated ownership) | Magnitude: 131.1

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `ark/type/generic.ts` -> **Severity: 0.31** (Bridge: 0.006 * Flux: 51.3204%)
- `ark/type/variants/base.ts` -> **Severity: 0.249** (Bridge: 0.0029 * Flux: 85.6442%)
- `ark/type/parser/string.ts` -> **Severity: 0.205** (Bridge: 0.0037 * Flux: 55.9064%)
- `ark/type/parser/reduce/dynamic.ts` -> **Severity: 0.203** (Bridge: 0.002 * Flux: 99.959%)
- `ark/type/parser/shift/operator/operator.ts` -> **Severity: 0.173** (Bridge: 0.0026 * Flux: 66.3052%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `ark/type/attributes.ts` -> **Severity: 10.633** (Embedded: 0.2047 * Error Risk: 51.9316%)
- `ark/type/keywords/keywords.ts` -> **Severity: 9.944** (Embedded: 0.1906 * Error Risk: 52.1643%)
- `ark/type/scope.ts` -> **Severity: 9.342** (Embedded: 0.1837 * Error Risk: 50.8662%)
- `ark/type/type.ts` -> **Severity: 9.173** (Embedded: 0.1778 * Error Risk: 51.6032%)
- `ark/type/generic.ts` -> **Severity: 9.066** (Embedded: 0.1717 * Error Risk: 52.8077%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `ark/util/generics.ts` -> **Severity: 2149.2** (Blast Radius: 21.492 * Doc Risk: 100.0%)
- `ark/type/parser/definition.ts` -> **Severity: 1739.8** (Blast Radius: 17.398 * Doc Risk: 100.0%)
- `ark/type/parser/reduce/shared.ts` -> **Severity: 1533.8** (Blast Radius: 15.338 * Doc Risk: 100.0%)
- `ark/type/type.ts` -> **Severity: 1531.05** (Blast Radius: 30.621 * Doc Risk: 50.0%)
- `ark/type/scope.ts` -> **Severity: 1330.9** (Blast Radius: 26.618 * Doc Risk: 50.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 33 literal sites + 5 sites through wrappers = 38
- **`panics_and_aborts`:** 84 literal sites + 6 sites through wrappers = 90

- `throwAssertionError` (function, panics_and_aborts, primitive): 4 call sites in 3 files -- `ark/attest/assert/assertions.ts`
- `logTypePerfStats` (function, debug_prints, primitive): 2 call sites in 1 files -- `ark/attest/cli/stats.ts`
- `writeAssertionData` (function, debug_prints, primitive): 2 call sites in 2 files -- `ark/attest/fixtures.ts`
- `handleNegativeDelta` (function, debug_prints, primitive): 1 call sites in 1 files -- `ark/attest/bench/baseline.ts`
- `onFail` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `ark/type/__tests__/integration/onFailConfig.ts`
- `throwMissingAssertionDataError` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `ark/attest/cache/getCachedAssertions.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 3134 call pairs -- scoped 33.0%, unique 0.0%, ambiguous 23.3%, external 43.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 3125 | 33.1% | 0.0% | 23.3% | 43.6% |
| javascript | 9 | 11.1% | 0.0% | 11.1% | 77.8% |

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
