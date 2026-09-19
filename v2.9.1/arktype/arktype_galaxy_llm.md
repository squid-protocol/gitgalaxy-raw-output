# ARCHITECTURAL_BRIEF: arktype
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/arktypeio/arktype.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 398 analyzed artifact(s), 58872 LOC.
- **Load-bearing artifact:** `ark/type/__tests__/integration/util.ts` -- 166 in-repo importer(s) depend on it. Changes here propagate furthest.
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
| Analyzed Artifacts (Scanned) | 398 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 171 |
| Total LOC | 58872 |
| Volatility Index | 0.013 |
| % Scanned of codebase = | 69.9% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5947 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3378 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 23.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6681 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 17 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 355 | 57265 | 89.2% |
| MARKDOWN | 13 | 0 | 3.3% |
| PLAINTEXT | 12 | 0 | 3.0% |
| JSON | 12 | 1304 | 3.0% |
| JAVASCRIPT | 5 | 297 | 1.3% |
| YAML | 1 | 6 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `3.093`
> **Composition Archetype:** `Hub-Coupled App` (z +3.09; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 38%, Data / Markup / Trivial 12%, Large Core Modules (3) 12%, Generic / Templated Code Files 11%, Callbacks & Closures Files 10%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 373 | 93.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 25 | 6.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 171*

**Composition by Extension & Reason:**
- `.tsx`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable), 1x Excluded (Saturation: Line 10 exceeds 500 chars)
- `.json`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3502 LOC)
- `.mdx`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 11x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.2025-10-05`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wasm`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 68.1 | 9.8 | 5.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.2 | 27.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 31.9 | 20.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 21.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.9 | 1.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.8 | 2.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 88.6 | 7.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 47.2 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 179 | 76 | 2 | `ark/schema/roots/union.ts` |
| cleanup | 1 | 1 | 0 | `ark/attest/cli/trace.ts` |
| guards | 1645 | 190 | 12 | `ark/type/__tests__/nary.test.ts` |
| danger | 360 | 114 | 3 | `ark/type/__tests__/realWorld.test.ts` |
| concurrency | 1026 | 8 | 0 | `ark/attest/bench/await1k.ts` |
| connectivity | 2627 | 234 | 19 | `ark/type/keywords/string.ts` |
| io | 432 | 80 | 3 | `ark/fs/fs.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 4 | 4 | 0 | `ark/attest/cli/stats.ts` |
| time | 64 | 21 | 0 | `ark/type/__tests__/range.test.ts` |
| serialization | 40 | 25 | 0 | `ark/type/__tests__/pipe.test.ts` |
| regex | 76 | 37 | 0 | `ark/type/__tests__/match.test.ts` |
| events | 108 | 46 | 1 | `eslint.config.js` |
| tests | 1867 | 133 | 13 | `ark/regex/__tests__/regex.test.ts` |
| docs | 359 | 74 | 2 | `ark/type/variants/base.ts` |
| debt | 106 | 67 | 1 | `ark/attest/bench/baseline.ts` |
| mutation | 7523 | 331 | 43 | `ark/type/nary.ts` |
| dead_code | 168 | 86 | 1 | `ark/schema/roots/union.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 95 | 40 | 0 | `ark/schema/scope.ts` |
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

1. **util.ts** (`ark/type/__tests__/integration/util.ts`) — 166 inbound connections
2. **attest.ts** (`ark/attest/assert/attest.ts`) — 144 inbound connections
3. **implement.ts** (`ark/schema/shared/implement.ts`) — 39 inbound connections
4. **attributes.ts** (`ark/type/attributes.ts`) — 37 inbound connections
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

- `writeIncompleteReferenceError` **(Generic / Templated Code)** (@ `ark/regex/state.ts`) -> Impact: **95.2** | LOC: 434
- `_intersectSequences` **(Compute Cores)** (@ `ark/schema/structure/sequence.ts`) -> Impact: **86.9** | LOC: 125
- `constructor` **(Many-Argument Workhorses)** (@ `ark/schema/node.ts`) -> Impact: **73.7** | LOC: 124
- `_traverse` **(Many-Argument Workhorses)** (@ `ark/schema/structure/structure.ts`) -> Impact: **72.0** | LOC: 79
- `maybeParseTupleExpression` **(Generic / Templated Code)** (@ `ark/type/parser/tupleExpressions.ts`) -> Impact: **66.7** | LOC: 87
- `fn` **(Callbacks & Closures)** (@ `ark/type/__tests__/objects/defaults.test.ts`) -> Impact: **66.6** | LOC: 432
- `getCompletions` **(Compute Cores)** (@ `ark/attest/cache/writeAssertionCache.ts`) -> Impact: **64.4** | LOC: 156
- `structure` **(Many-Argument Workhorses)** (@ `ark/schema/structure/structure.ts`) -> Impact: **63.5** | LOC: 110
- `appendSpreadBranch` **(Generic / Templated Code)** (@ `ark/type/parser/tupleLiteral.ts`) -> Impact: **63.2** | LOC: 190
- `get` **(Defensive Guards)** (@ `ark/schema/structure/structure.ts`) -> Impact: **62.1** | LOC: 65

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `ark/util` | 28 | 2307.06 | 18.08% | 2.15% |
| `ark/type/__tests__` | 53 | 1559.06 | 2.2% | 0.73% |
| `ark/attest/bench` | 6 | 1418.94 | 16.46% | 0.0% |
| `ark/type` | 14 | 893.08 | 7.63% | 5.22% |
| `ark/type/parser` | 6 | 758.46 | 15.27% | 0.0% |
| `ark/type/keywords` | 9 | 612.04 | 4.96% | 0.0% |
| `ark/attest/cache` | 5 | 606.18 | 19.19% | 0.0% |
| `ark/repo` | 19 | 476.98 | 12.17% | 5.26% |
| `ark/attest/cli` | 4 | 465.66 | 22.53% | 15.07% |
| `ark/json-schema` | 13 | 440.54 | 17.35% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `ark/type/__tests__/integration/testSimpleConfig.ts` -> **99.9955%** Exposure
- `ark/type/__tests__/integration/testEoptConfig.ts` -> **88.0797%** Exposure
- `ark/util/__tests__/traits.scratch.ts` -> **82.0223%** Exposure
- `ark/extension/arktype.scratch.ts` -> **75.6296%** Exposure
- `ark/type/config.ts` -> **73.1059%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `ark/schema/shared/errors.ts` -> **100.0%** Exposure
- `ark/schema/shared/intersections.ts` -> **100.0%** Exposure
- `ark/schema/shared/registry.ts` -> **100.0%** Exposure
- `ark/schema/shared/traversal.ts` -> **100.0%** Exposure
- `ark/util/clone.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `ark/type/__tests__/match.test.ts` -> **5** Orphaned Functions | **6** Duplicates
- `ark/type/__tests__/integration/testSimpleConfig.ts` -> **6** Orphaned Functions | **0** Duplicates
- `ark/extension/arktype.scratch.ts` -> **4** Orphaned Functions | **0** Duplicates
- `ark/type/__tests__/generic.test.ts` -> **4** Orphaned Functions | **0** Duplicates
- `ark/type/__tests__/narrow.test.ts` -> **3** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `750` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `ark/attest/bench/await1k.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1075.54 | **LOC:** 1003 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 4.846; role: Pure Producer (Foundation)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.846
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.127095
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ark/util/flatMorph.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 569.98 | **LOC:** 110 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 4.107; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (72.7%), Connectivity (formerly Api Exposure) (50.4%), Mutation Surface (formerly State Flux) (37.3%), Complexity Load (formerly Cognitive Load) (21.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 72`, `args: 4`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2`, `dead_code: 1`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.02303
  * `Imports (Out-Degree: 5):` arrays.ts, generics.ts, keys.ts, records.ts, unionToTuple.ts
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ark/attest/cli/trace.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 393.68 | **LOC:** 788 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.2%), Complexity Load (formerly Cognitive Load) (29.9%)
- **Documentation Coverage:** 91.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `analyzeTypeInstantiations` **(Defensive Guards)** (Impact: 25.3)
  * `findNodeByPreference` **(Compute Cores)** (Impact: 19.9)
  * `processDurationEntry` **(Many-Argument Workhorses)** (Impact: 18.5)
  * `findCallExpressionInRange` **(Compute Cores)** (Impact: 15.3)
  * `collectFunctionStats` **(Compute Cores)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 36 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 136`, `args: 58`, `func_start: 34`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 44`, `unreferenced_by_name: 2`
* *Architecture:* `io: 17`, `api: 3`, `concurrency: 3`, `import: 9`
* *Defense:* `safety: 12`, `doc: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ts.ts, config.ts, shared.ts, fs, node:child_process, node:fs, node:path, typescript
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ark/type/keywords/string.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 373.1 | **LOC:** 968 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (51.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.8%), Mutation Surface (formerly State Flux) (21.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isLuhnValid` **(Compute Cores)** (Impact: 55.3)
    * *Intent:* // https://github.com/validatorjs/validator.js/blob/master/src/lib/isLuhnNumber.js
  * `morphs` **(Compute Cores)** (Impact: 43.2)
  * `tryParseDatePattern` **(Compute Cores)** (Impact: 26.3)
  * `morphs` **(Compute Cores)** (Impact: 23.9)
  * `predicate` **(Defensive Guards)** (Impact: 19.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 341`, `args: 42`, `func_start: 21`
* *Risk/State:* `state_mutation: 8`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 101`, `import: 6`
* *Defense:* `safety: 9`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` attributes.ts, module.ts, scope.ts, number.ts, schema, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ark/util/arrays.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 306.0 | **LOC:** 510 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **4**; blast radius 13.876; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (90.3%), Guard Balance (formerly Safety Score) (62.5%), Mutation Surface (formerly State Flux) (46.9%), Complexity Load (formerly Cognitive Load) (20.3%)
- **Documentation Coverage:** 61.5385% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `arrayEquals` **(Generic / Templated Code)** (Impact: 53.4)
  * `intersectUniqueLists` **(Generic / Templated Code)** (Impact: 33.1)
  * `appendUnique` **(Generic / Templated Code)** (Impact: 31.6)
    * *Intent:* /** * Appends a value or concatenates an array to an array if it is not already included, returning ...
  * `range` **(Compute Cores)** (Impact: 28.4)
  * `getDuplicatesOf` **(Defensive Guards)** (Impact: 21.6)
    * *Intent:* /** * Extracts duplicated elements and their indices from an array, returning them. * * Note that gi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 316`, `args: 22`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 14`
* *Architecture:* `io: 2`, `api: 44`, `import: 4`
* *Defense:* `safety: 8`, `doc: 7`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.876
  * `Choke Point (Betweenness):` 0.000219 | `Ripple Effect (Closeness):` 0.032975
  * `Imports (Out-Degree: 3):` functions.ts, generics.ts, intersections.ts, numbers.ts
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `ark/attest/assert/chainableAssertions.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 209.56 | **LOC:** 393 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 9.299; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (80.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.8%), Connectivity (formerly Api Exposure) (44.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `snap` **(Defensive Guards)** (Impact: 18.7)
  * `toFile` **(Defensive Guards)** (Impact: 15.1)
  * `inline` **(Defensive Guards)** (Impact: 14.2)
    * *Intent:* // Use variadic args to distinguish undefined being passed explicitly from no args
  * `formatTypeString` **(Generic / Templated Code)** (Impact: 12.7)
  * `immediateAssertion` **(Compute Cores)** (Impact: 10.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 158`, `args: 40`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 16`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 20`, `import: 12`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.299
  * `Choke Point (Betweenness):` 0.00123 | `Ripple Effect (Closeness):` 0.182695
  * `Imports (Out-Degree: 6):` snapshots.ts, writeAssertionCache.ts, config.ts, utils.ts, assertions.ts, attest.ts, fs, util...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ark/util/serialize.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 205.4 | **LOC:** 241 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 1.11; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (76.3%), Connectivity (formerly Api Exposure) (57.0%), Guard Balance (formerly Safety Score) (43.6%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_serialize` **(Defensive Guards)** (Impact: 50.5)
  * `stringifyUnquoted` **(Many-Argument Workhorses)** (Impact: 38.5)
  * `printable` **(Defensive Guards)** (Impact: 35.6)
  * `describeCollapsibleDate` **(Compute Cores)** (Impact: 26.9)
    * *Intent:* /** * Converts a Date instance to a human-readable description relative to its precision */
  * `toJSON` **(Generic / Templated Code)** (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 99`, `args: 20`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`
* *Architecture:* `api: 12`, `import: 5`
* *Defense:* `safety: 16`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.11
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.005668
  * `Imports (Out-Degree: 3):` arrays.ts, domain.ts, primitive.ts, records.ts, registry.ts
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ark/type/nary.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 204.82 | **LOC:** 2649 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 1.947; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.6%), Mutation Surface (formerly State Flux) (39.7%), Connectivity (formerly Api Exposure) (26.1%), Complexity Load (formerly Cognitive Load) (9.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 1565`
* *Risk/State:* `state_mutation: 67`, `dead_code: 1`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.947
  * `Choke Point (Betweenness):` 0.000513 | `Ripple Effect (Closeness):` 0.051484
  * `Imports (Out-Degree: 5):` attributes.ts, keywords.ts, type.ts, instantiate.ts, object.ts, schema, util
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ark/fs/fs.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 195.36 | **LOC:** 242 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **7**; blast radius 34.695; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.3%), Guard Balance (formerly Safety Score) (65.2%)
- **Documentation Coverage:** 89.4737% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `walkPaths` **(Defensive Guards)** (Impact: 28.8)
  * `cpR` **(Compute Cores)** (Impact: 12.8)
  * `findPackageRoot` **(Defensive Guards)** (Impact: 9.5)
  * `findPackageAncestors` **(Defensive Guards)** (Impact: 9.3)
  * `assertPackageRoot` **(Defensive Guards)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 110`, `args: 44`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 10`, `planned_debt: 1`
* *Architecture:* `io: 47`, `api: 35`, `import: 9`
* *Defense:* `safety: 10`, `doc: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.695
  * `Choke Point (Betweenness):` 0.003177 | `Ripple Effect (Closeness):` 0.232071
  * `Imports (Out-Degree: 2):` caller.ts, shell.ts, node:fs, node:os, node:path, node:process, node:url
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `ark/type/parser/tupleLiteral.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 185.08 | **LOC:** 397 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **4**; blast radius 2.899; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (77.4%), Guard Balance (formerly Safety Score) (64.0%), Connectivity (formerly Api Exposure) (60.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `appendSpreadBranch` **(Generic / Templated Code)** (Impact: 63.2)
  * `parseTupleLiteral` **(Generic / Templated Code)** (Impact: 27.7)
  * `appendRequiredElement` **(Compute Cores)** (Impact: 11.6)
  * `appendVariadicElement` **(Compute Cores)** (Impact: 9.7)
  * `writeNonArraySpreadMessage` **(Compute Cores)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 147`, `args: 11`, `func_start: 7`
* *Risk/State:* `state_mutation: 10`, `dead_code: 3`
* *Architecture:* `api: 18`, `import: 6`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.899
  * `Choke Point (Betweenness):` 0.000763 | `Ripple Effect (Closeness):` 0.060096
  * `Imports (Out-Degree: 3):` definition.ts, property.ts, schema, util
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `ark/attest/bench/bench.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 182.56 | **LOC:** 362 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **9**; blast radius 23.662; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.2%), Mutation Surface (formerly State Flux) (97.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `benchFn` **(Many-Argument Workhorses)** (Impact: 15.7)
  * `createAssertion` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `createStatMethod` **(Stateful Encapsulated Methods)** (Impact: 6.5)
  * `loopAsyncCalls` **(Encapsulated Accessors)** (Impact: 6.2)
  * `markAssertion` **(Stateful Encapsulated Methods)** (Impact: 4.8)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.662
  * `Choke Point (Betweenness):` 0.002458 | `Ripple Effect (Closeness):` 0.189601
  * `Imports (Out-Degree: 5):` config.ts, utils.ts, await1k.ts, baseline.ts, call1k.ts, measure.ts, type.ts, fs...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `ark/type/__tests__/match.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 179.16 | **LOC:** 919 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (39.3%), Mutation Surface (formerly State Flux) (9.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (5.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `string` **(Callbacks & Closures)** (Impact: 9.1)
  * `strong` **(Callbacks & Closures)** (Impact: 8.7)
  * `three` **(Callbacks & Closures)** (Impact: 7.2)
  * `default` **(Defensive Guards)** (Impact: 6.6)
  * `value` **(Generic / Templated Code)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 265`, `args: 183`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`, `dead_code: 2`, `duplicate_logic: 6`, `unreferenced_by_name: 5`
* *Architecture:* `io: 3`, `import: 5`
* *Defense:* `safety: 11`, `test: 46`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` attest, schema, arktype, attributes.ts, match.ts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ark/type/parser/objectLiteral.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 176.34 | **LOC:** 356 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **5**; blast radius 2.859; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (61.1%), Guard Balance (formerly Safety Score) (54.2%), Mutation Surface (formerly State Flux) (31.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseObjectLiteral` **(Many-Argument Workhorses)** (Impact: 52.8)
  * `appendNamedProp` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `preparseKey` **(Generic / Templated Code)** (Impact: 39.7)
  * `writeInvalidUndeclaredBehaviorMessage` **(Generic / Templated Code)** (Impact: 4.9)
  * `writeInvalidSpreadTypeMessage` **(Generic / Templated Code)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 124`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 5`, `dead_code: 1`
* *Architecture:* `api: 18`, `import: 7`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.859
  * `Choke Point (Betweenness):` 0.000427 | `Ripple Effect (Closeness):` 0.059448
  * `Imports (Out-Degree: 4):` validate.ts, definition.ts, property.ts, schema, util
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `ark/repo/jsdocGen.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 172.86 | **LOC:** 415 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 1.055; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.1%), Connectivity (formerly Api Exposure) (48.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertBuildDirExists` **(Compute Cores)** (Impact: 30.7)
  * `parseJsDocLink` **(Defensive Guards)** (Impact: 11.7)
  * `findInheritedDocs` **(Defensive Guards)** (Impact: 10.1)
  * `parseBlock` **(Compute Cores)** (Impact: 9.3)
  * `parseJsDocText` **(Callbacks & Closures)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 92`, `args: 29`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 13`
* *Architecture:* `io: 16`, `api: 10`, `import: 6`
* *Defense:* `safety: 8`, `doc: 4`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002519
  * `Imports (Out-Degree: 0):` jsdocGen.ts, shared.ts, node:fs, node:path, ts-morph, typescript
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ark/attest/cache/ts.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 171.28 | **LOC:** 339 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 2.123; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (77.7%), Connectivity (formerly Api Exposure) (68.5%), Guard Balance (formerly Safety Score) (65.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nearestBoundingCallExpression` **(Defensive Guards)** (Impact: 14.5)
  * `constructor` **(Compute Cores)** (Impact: 11.7)
  * `instantiateTsconfigFromPath` **(Compute Cores)** (Impact: 8.7)
  * `getSourceFileOrThrow` **(Compute Cores)** (Impact: 8.6)
  * `getTsConfigInfoOrThrow` **(I/O & Config Routines)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 81`, `args: 34`, `func_start: 24`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 12`
* *Architecture:* `io: 18`, `api: 22`, `import: 7`
* *Defense:* `safety: 11`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.123
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.125665
  * `Imports (Out-Degree: 2):` config.ts, fs, util, vfs, node:fs, node:path, typescript
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ark/attest/cache/writeAssertionCache.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 171.06 | **LOC:** 352 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **7**; blast radius 10.735; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.4%), Guard Balance (formerly Safety Score) (63.5%), Mutation Surface (formerly State Flux) (61.0%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getCompletions` **(Compute Cores)** (Impact: 64.4)
  * `getJSDocFromSymbol` **(Compute Cores)** (Impact: 23.5)
    * *Intent:* /** * Extract JSDoc comments from a symbol's declarations */
  * `extractJSDocFromArgument` **(Compute Cores)** (Impact: 11.4)
    * *Intent:* /** * Extract JSDoc comments associated with the first argument of a call expression */
  * `checkDiagnosticMessages` **(Compute Cores)** (Impact: 9.6)
  * `analyzeProjectAssertions` **(I/O & Config Routines)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 91`, `args: 22`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 8`
* *Architecture:* `io: 3`, `api: 17`, `import: 7`
* *Defense:* `safety: 6`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.735
  * `Choke Point (Betweenness):` 3.8e-05 | `Ripple Effect (Closeness):` 0.134011
  * `Imports (Out-Degree: 2):` config.ts, utils.ts, ts.ts, utils.ts, fs, util, typescript
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `ark/regex/state.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 169.28 | **LOC:** 775 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **4**; blast radius 4.541; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (85.5%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.3%), Complexity Load (formerly Cognitive Load) (6.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeIncompleteReferenceError` **(Generic / Templated Code)** (Impact: 95.2)
  * `writeMidAnchorError` **(Generic / Templated Code)** (Impact: 1.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 394`, `args: 2`, `func_start: 1`, `class_start: 8`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `api: 59`, `import: 24`
* *Defense:* `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.541
  * `Choke Point (Betweenness):` 0.000159 | `Ripple Effect (Closeness):` 0.017992
  * `Imports (Out-Degree: 4):` escape.ts, quantify.ts, regex.ts, util
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `ark/util/numbers.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 168.94 | **LOC:** 269 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 7.831; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (77.8%), Guard Balance (formerly Safety Score) (59.9%), Complexity Load (formerly Cognitive Load) (35.3%)
- **Documentation Coverage:** 91.3043% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseNumeric` **(Defensive Guards)** (Impact: 20.9)
  * `tryParseInteger` **(Generic / Templated Code)** (Impact: 20.8)
  * `nearestFloat` **(Compute Cores)** (Impact: 19.9)
    * *Intent:* * * console.log(nearestFloat(0)); // Smallest positive number * console.log(nearestFloat(2)); // 2.0...
  * `createNumberMatcher` **(Compute Cores)** (Impact: 12.2)
  * `tryParseWellFormedNumber` **(Generic / Templated Code)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 106`, `args: 13`, `func_start: 13`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 26`, `import: 3`
* *Defense:* `safety: 6`, `doc: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.831
  * `Choke Point (Betweenness):` 0.000178 | `Ripple Effect (Closeness):` 0.025015
  * `Imports (Out-Degree: 1):` $token, errors.ts, strings.ts
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `ark/type/scope.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 168.48 | **LOC:** 481 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (93.1%), Guard Balance (formerly Safety Score) (53.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.5%), Mutation Surface (formerly State Flux) (15.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `define` **(Generic / Templated Code)** (Impact: 34.3)
  * `preparseOwnAliasEntry` **(Stateful Encapsulated Methods)** (Impact: 17.6)
  * `define` **(Generic / Templated Code)** (Impact: 14.9)
  * `parseOwnDefinitionFormat` **(Compute Cores)** (Impact: 14.8)
  * `preparseOwnDefinitionFormat` **(Stateful Encapsulated Methods)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 268`, `args: 33`, `func_start: 22`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`, `dead_code: 4`
* *Architecture:* `api: 35`, `import: 17`
* *Defense:* `safety: 4`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` declare.ts, fn.ts, generic.ts, keywords.ts, match.ts, module.ts, nary.ts, infer.ts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ark/type/__tests__/realWorld.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 168.4 | **LOC:** 1550 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (44.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.0%), Mutation Surface (formerly State Flux) (8.9%), Connectivity (formerly Api Exposure) (5.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validatePositiveBigint` **(Compute Cores)** (Impact: 43.2)
  * `constructor` **(Compute Cores)** (Impact: 34.1)
  * `trimString` **(Compute Cores)** (Impact: 26.7)
  * `never` **(Callbacks & Closures)** (Impact: 6.4)
  * `message` **(Callbacks & Closures)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 389`, `args: 139`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 2`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 13`, `import: 8`
* *Defense:* `safety: 13`, `test: 69`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` attest, schema, arktype, attributes.ts, node:assert
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ark/type/__tests__/objects/defaults.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 153.74 | **LOC:** 974 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (36.5%), Mutation Surface (formerly State Flux) (20.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (5.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fn` **(Callbacks & Closures)** (Impact: 66.6)
  * `toggle` **(Callbacks & Closures)** (Impact: 39.7)
  * `toggle` **(Callbacks & Closures)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 359`, `args: 166`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 8`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 21`, `test: 71`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` attest, schema, util, arktype, attributes.ts, validate.ts, property.ts, default.ts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ark/json-schema/object.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 153.32 | **LOC:** 275 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.822; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.0%), Guard Balance (formerly Safety Score) (70.4%), Connectivity (formerly Api Exposure) (37.9%), Complexity Load (formerly Cognitive Load) (28.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `jsonSchemaObjectAdditionalPropertiesValidator` **(Many-Argument Workhorses)** (Impact: 38.7)
  * `parseRequiredAndOptionalKeys` **(Compute Cores)** (Impact: 21.3)
  * `parseMinMaxProperties` **(Defensive Guards)** (Impact: 11.2)
  * `parseAdditionalProperties` **(Defensive Guards)** (Impact: 11.0)
  * `jsonSchemaObjectMaxPropertiesValidator` **(Compute Cores)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 59`, `args: 18`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 14`
* *Architecture:* `io: 2`, `api: 4`, `import: 6`
* *Defense:* `safety: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` errors.ts, json.ts, scope.ts, schema, util, arktype
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ark/type/parser/tupleExpressions.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 151.68 | **LOC:** 298 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **10**; blast radius 2.101; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (76.4%), Complexity Load (formerly Cognitive Load) (12.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `maybeParseTupleExpression` **(Generic / Templated Code)** (Impact: 66.7)
  * `parseBranchTuple` **(Generic / Templated Code)** (Impact: 9.5)
  * `instanceof` **(Compute Cores)** (Impact: 8.2)
  * `writeMalformedFunctionalExpressionMessage` **(Generic / Templated Code)** (Impact: 8.0)
  * `defineIndexOneParsers` **(Generic / Templated Code)** (Impact: 4.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 175`, `args: 22`, `func_start: 14`
* *Risk/State:* None
* *Architecture:* `api: 26`, `import: 10`
* *Defense:* `safety: 2`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.101
  * `Choke Point (Betweenness):` 0.001276 | `Ripple Effect (Closeness):` 0.059448
  * `Imports (Out-Degree: 8):` attributes.ts, keywords.ts, validate.ts, definition.ts, shared.ts, unenclosed.ts, tokens.ts, string.ts...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `ark/util/records.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 143.22 | **LOC:** 367 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **8**; blast radius 22.92; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (62.9%), Mutation Surface (formerly State Flux) (22.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.7%)
- **Documentation Coverage:** 59.2593% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hasDefinedKey` **(Generic / Templated Code)** (Impact: 19.9)
    * *Intent:* // must be defined this way to avoid https://github.com/microsoft/TypeScript/issues/55049
  * `invert` **(Generic / Templated Code)** (Impact: 11.9)
  * `splitByKeys` **(Generic / Templated Code)** (Impact: 8.0)
  * `isKeyOf` **(Generic / Templated Code)** (Impact: 5.9)
  * `withAlphabetizedKeys` **(Generic / Templated Code)** (Impact: 5.0)
    * *Intent:* /** Copies enumerable keys of o to a new object in alphabetical order */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 268`, `args: 23`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 4`
* *Architecture:* `api: 56`, `import: 8`
* *Defense:* `safety: 5`, `doc: 15`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.92
  * `Choke Point (Betweenness):` 0.000544 | `Ripple Effect (Closeness):` 0.034545
  * `Imports (Out-Degree: 6):` arrays.ts, domain.ts, errors.ts, flatMorph.ts, functions.ts, generics.ts, keys.ts, unionToTuple.ts
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `ark/fast-check/arktypeFastCheck.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 140.7 | **LOC:** 209 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 2.71; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (62.1%), Complexity Load (formerly Cognitive Load) (49.8%), Connectivity (formerly Api Exposure) (33.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildArbitrary` **(Defensive Guards)** (Impact: 45.3)
  * `buildStructureArbitrary` **(Defensive Guards)** (Impact: 22.1)
  * `buildObjectArbitrary` **(Generic / Templated Code)** (Impact: 7.8)
  * `buildIndexSignatureArbitrary` **(Callbacks & Closures)** (Impact: 7.8)
  * `getSpreadVariadicElementsTuple` **(Compute Cores)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 74`, `args: 12`, `func_start: 9`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `api: 3`, `import: 9`
* *Defense:* `safety: 10`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.71
  * `Choke Point (Betweenness):` 0.000111 | `Ripple Effect (Closeness):` 0.010076
  * `Imports (Out-Degree: 6):` array.ts, domain.ts, object.ts, proto.ts, fastCheckContext.ts, schema, util, arktype...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `ark/schema/structure/structure.ts` -> Churn: **63.09%** | Cog Load: 55.6153% | Debt: 8.1594%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `ark/attest/cli/trace.ts` -> **David Blass** (100.0% isolated ownership) | Magnitude: 393.68
- `ark/util/arrays.ts` -> **David Blass** (100.0% isolated ownership) | Magnitude: 306.0
- `ark/attest/assert/chainableAssertions.ts` -> **David Blass** (100.0% isolated ownership) | Magnitude: 209.56
- `ark/util/serialize.ts` -> **David Blass** (100.0% isolated ownership) | Magnitude: 205.4
- `ark/type/nary.ts` -> **David Blass** (100.0% isolated ownership) | Magnitude: 204.82

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `ark/attest/assert/attest.ts` -> **Severity: 1.116** (Bridge: 0.0159 * Flux: 70.1785%)
- `ark/fs/fs.ts` -> **Severity: 0.314** (Bridge: 0.0032 * Flux: 98.8118%)
- `ark/attest/bench/bench.ts` -> **Severity: 0.239** (Bridge: 0.0025 * Flux: 97.3568%)
- `ark/type/parser/reduce/dynamic.ts` -> **Severity: 0.188** (Bridge: 0.0019 * Flux: 99.959%)
- `ark/attest/bench/type.ts` -> **Severity: 0.164** (Bridge: 0.0023 * Flux: 69.9148%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `ark/type/__tests__/integration/util.ts` -> **Severity: 26.719** (Embedded: 0.5124 * Error Risk: 52.1415%)
- `ark/attest/assert/attest.ts` -> **Severity: 21.142** (Embedded: 0.3537 * Error Risk: 59.7781%)
- `ark/fs/fs.ts` -> **Severity: 15.132** (Embedded: 0.2321 * Error Risk: 65.2031%)
- `ark/fs/shell.ts` -> **Severity: 14.021** (Embedded: 0.1523 * Error Risk: 92.0666%)
- `ark/attest/bench/bench.ts` -> **Severity: 13.553** (Embedded: 0.1896 * Error Risk: 71.4822%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `ark/type/__tests__/integration/util.ts` -> **Severity: 10677.7** (Blast Radius: 106.777 * Doc Risk: 100.0%)
- `ark/attest/assert/attest.ts` -> **Severity: 7647.5** (Blast Radius: 76.475 * Doc Risk: 100.0%)
- `ark/fs/fs.ts` -> **Severity: 3104.29** (Blast Radius: 34.695 * Doc Risk: 89.4737%)
- `ark/attest/bench/bench.ts` -> **Severity: 2366.2** (Blast Radius: 23.662 * Doc Risk: 100.0%)
- `ark/util/generics.ts` -> **Severity: 1769.5** (Blast Radius: 17.695 * Doc Risk: 100.0%)

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
