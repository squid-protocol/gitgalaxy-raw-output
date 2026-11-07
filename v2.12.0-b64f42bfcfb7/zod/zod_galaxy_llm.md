# ARCHITECTURAL_BRIEF: zod
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/colinhacks/zod.git` |
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
- **Scope:** 420 analyzed artifact(s), 55954 LOC.
- **Load-bearing artifact:** `packages/zod/src/v4/index.ts` -- 72 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/zod/src/v4/locales/index.ts` -- pulls in 50 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `.npmrc` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 567 |
| Analyzed Artifacts (Scanned) | 420 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 147 |
| Total LOC | 55954 |
| Volatility Index | 0.012 |
| % Scanned of codebase = | 74.1% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7022 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4218 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 17.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.4844 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 23 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 357 | 54773 | 85.0% |
| MARKDOWN | 18 | 0 | 4.3% |
| JSON | 18 | 291 | 4.3% |
| PLAINTEXT | 9 | 1 | 2.1% |
| YAML | 8 | 255 | 1.9% |
| XML | 6 | 48 | 1.4% |
| HTML | 2 | 537 | 0.5% |
| JAVASCRIPT | 2 | 49 | 0.5% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 419 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 37%, Data / Markup / Trivial 24%, Large Core Modules (2) 14%, Callbacks & Closures Files 6%, Large Core Modules 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 391 | 93.1% |
| Unknown | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 26 | 6.2% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 147*

**Composition by Extension & Reason:**
- `.tsx`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 27x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.mdx`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ai`: 8x Excluded (Explicitly Denied Extension: '.ai')
- `.jpg`: 8x Excluded (Explicitly Denied Extension: '.jpg')
- `.pdf`: 8x Excluded (Explicitly Denied Extension: '.pdf')
- `.ts`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.css`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 12474 LOC)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 10.1 | 5.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 83.4 | 18.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 19.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 10.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.1 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 41.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 134 | 34 | 0 | `packages/zod/src/v3/types.ts` |
| cleanup | 0 | 0 | 0 | - |
| guards | 5083 | 271 | 28 | `packages/zod/src/v4/mini/tests/index.test.ts` |
| danger | 1702 | 143 | 8 | `packages/zod/src/v3/types.ts` |
| concurrency | 1133 | 119 | 6 | `packages/zod/src/v3/tests/async-parsing.test.ts` |
| connectivity | 2285 | 146 | 4 | `packages/zod/src/v4/core/schemas.ts` |
| io | 991 | 90 | 5 | `packages/zod/src/v4/classic/tests/to-json-schema.test.ts` |
| crypto | 2 | 2 | 0 | `packages/zod/src/v4/classic/tests/hash.test.ts` |
| ipc | 0 | 0 | 0 | - |
| time | 129 | 35 | 0 | `packages/zod/src/v4/classic/tests/codec.test.ts` |
| serialization | 57 | 25 | 0 | `packages/zod/src/v4/core/to-json-schema.ts` |
| regex | 69 | 19 | 0 | `packages/zod/src/v4/core/util.ts` |
| events | 169 | 39 | 0 | `packages/docs-v3/blog/index.html` |
| tests | 6841 | 168 | 47 | `packages/zod/src/v4/classic/tests/string.test.ts` |
| docs | 312 | 38 | 0 | `packages/zod/src/v4/classic/schemas.ts` |
| debt | 429 | 78 | 2 | `packages/zod/src/v4/classic/schemas.ts` |
| mutation | 7786 | 313 | 45 | `packages/zod/src/v3/types.ts` |
| dead_code | 986 | 103 | 4 | `packages/zod/src/v4/core/api.ts` |
| credential | 9 | 2 | 0 | `packages/zod/src/v4/classic/tests/string.test.ts` |
| threat | 17 | 6 | 0 | `packages/zod/src/v4/locales/fa.ts` |
| ml_ai | 114 | 27 | 0 | `packages/tsc/generate.ts` |
| ui | 23 | 4 | 0 | `packages/zod/src/v3/types.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/zod/src/v4/classic/tests/to-json-schema.test.ts` (Hits: 159)
- `packages/zod/src/v4/classic/tests/string.test.ts` (Hits: 111)
- `packages/zod/src/v3/types.ts` (Hits: 82)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.ts** (`packages/zod/src/v4/index.ts`) — 72 inbound connections
2. **index.ts** (`packages/zod/src/v3/index.ts`) — 64 inbound connections
3. **util.ts** (`packages/zod/src/v4/core/util.ts`) — 62 inbound connections
4. **errors.ts** (`packages/zod/src/v4/core/errors.ts`) — 59 inbound connections
5. **checks.ts** (`packages/zod/src/v4/core/checks.ts`) — 54 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`packages/zod/src/v4/locales/index.ts`) — 50 outbound dependencies
2. **index.ts** (`packages/zod/src/v4/core/index.ts`) — 16 outbound dependencies
3. **external.ts** (`packages/zod/src/v4/classic/external.ts`) — 12 outbound dependencies
4. **schemas.ts** (`packages/zod/src/v4/core/schemas.ts`) — 12 outbound dependencies
5. **index.html** (`packages/docs-v3/blog/index.html`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `convertBaseSchema` **(Many-Argument Workhorses)** (@ `packages/zod/src/v4/classic/from-json-schema.ts`) -> Impact: **279.5** | LOC: 394
- `_parse` **(Compute Cores)** (@ `packages/zod/src/v3/types.ts`) -> Impact: **137.1** | LOC: 309
- `finalize` **(Many-Argument Workhorses)** (@ `packages/zod/src/v4/core/to-json-schema.ts`) -> Impact: **108.4** | LOC: 158
- `errorMap` **(Compute Cores)** (@ `packages/zod/src/v3/locales/en.ts`) -> Impact: **96.0** | LOC: 119
- `extractDefs` **(Many-Argument Workhorses)** (@ `packages/zod/src/v4/core/to-json-schema.ts`) -> Impact: **65.9** | LOC: 141
- `parse` **(Many-Argument Workhorses)** (@ `packages/zod/src/v4/core/schemas.ts`) -> Impact: **65.1** | LOC: 124
- `isTransforming` **(Compute Cores)** (@ `packages/zod/src/v4/core/to-json-schema.ts`) -> Impact: **60.3** | LOC: 63
- `convertSchema` **(Compute Cores)** (@ `packages/zod/src/v4/classic/from-json-schema.ts`) -> Impact: **54.2** | LOC: 80
- `numberProcessor` **(Many-Argument Workhorses)** (@ `packages/zod/src/v4/core/json-schema-processors.ts`) -> Impact: **53.4** | LOC: 40
- `literalProcessor` **(Many-Argument Workhorses)** (@ `packages/zod/src/v4/core/json-schema-processors.ts`) -> Impact: **51.1** | LOC: 38

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/zod/src/v3/tests` | 61 | 8341.46 | 7.75% | 0.0% |
| `packages/zod/src/v4/classic/tests` | 74 | 7470.81 | 7.08% | 0.0% |
| `packages/zod/src/v4/core` | 19 | 6102.57 | 37.9% | 15.59% |
| `__monolith__` | 16 | 5127.16 | 0.64% | 0.0% |
| `packages/zod/src/v4/classic` | 10 | 2051.73 | 16.9% | 21.24% |
| `packages/zod/src/v4/mini` | 7 | 907.72 | 3.32% | 1.49% |
| `packages/zod/src/v4/mini/tests` | 15 | 728.58 | 3.06% | 0.0% |
| `packages/bench` | 36 | 666.16 | 17.49% | 16.56% |
| `packages/tsc` | 7 | 384.34 | 19.91% | 0.0% |
| `packages/resolution` | 7 | 317.28 | 4.37% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/bench/safe.ts` -> **100.0%** Exposure
- `packages/zod/src/v4/classic/schemas.ts` -> **99.976%** Exposure
- `packages/bench/key-iteration.ts` -> **99.593%** Exposure
- `packages/zod/src/v4/core/api.ts` -> **99.4229%** Exposure
- `packages/zod/src/v4/classic/compat.ts` -> **99.3307%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/bench/instanceof.ts` -> **100.0%** Exposure
- `packages/tsc/generate.ts` -> **100.0%** Exposure
- `packages/zod/src/v3/benchmarks/index.ts` -> **100.0%** Exposure
- `packages/zod/src/v3/helpers/parseUtil.ts` -> **100.0%** Exposure
- `packages/zod/src/v3/locales/en.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/zod/src/v4/core/api.ts` -> **104** Orphaned Functions | **2** Duplicates
- `packages/zod/src/v4/classic/schemas.ts` -> **0** Orphaned Functions | **82** Duplicates
- `packages/zod/src/v3/types.ts` -> **32** Orphaned Functions | **22** Duplicates
- `packages/zod/src/v4/core/util.ts` -> **47** Orphaned Functions | **2** Duplicates
- `packages/zod/src/v4/classic/tests/codec.test.ts` -> **0** Orphaned Functions | **28** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `packages/zod/src/v4/mini/tests/string.test.ts` -> **99.9972%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `506` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/schemas.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.503)
- **Top Global Matches:** file_cluster_5: 9.503, file_cluster_12: 10.626, file_cluster_0: 11.112
- **Magnitude:** 2289.46 | **LOC:** 4557 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 41.2%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **12**; blast radius 54.067; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (99.1%)
- **Documentation Coverage:** 96.2617% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 65.1)
  * `runChecks` **(Defensive Guards)** (Impact: 42.1)
  * `handleIntersectionResults` **(Many-Argument Workhorses)** (Impact: 40.2)
  * `parse` **(Compute Cores)** (Impact: 33.3)
  * `mergeValues` **(Compute Cores)** (Impact: 27.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 40 instances
* *Amplified Cascading Flux:* 249 instances
* *Concurrency (weighted view):* 280
* *State Mutation (weighted view):* 778
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 524`, `structural_boundaries: 1750`, `args: 298`, `func_start: 96`, `class_start: 225`
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 280`, `dead_code: 30`, `planned_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `io: 15`, `api: 337`, `concurrency: 80`, `import: 13`
* *Defense:* `safety: 94`, `doc: 50`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 54.067
  * `Choke Point (Betweenness):` 0.022088 | `Ripple Effect (Closeness):` 0.145177
  * `Imports (Out-Degree: 12):` api.js, checks.js, core.js, doc.js, errors.js, json-schema.js, parse.js, regexes.js...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `packages/zod/src/v4/classic/schemas.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.351)
- **Top Global Matches:** file_cluster_5: 9.351, file_cluster_12: 11.947, file_cluster_7: 12.865
- **Magnitude:** 1825.04 | **LOC:** 2410 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 70.6%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **7**; blast radius 9.77; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.4%)
- **Documentation Coverage:** 87.0855% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_function` **(Defensive Guards)** (Impact: 16.1)
  * `hash` **(Defensive Guards)** (Impact: 11.0)
  * `tuple` **(Compute Cores)** (Impact: 10.8)
  * `addIssue` **(Defensive Guards)** (Impact: 10.6)
  * `extract` **(Generic / Templated Code)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 59 instances
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 362
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 1079`, `args: 551`, `func_start: 475`, `class_start: 81`
* *Risk/State:* `safety_bypasses: 116`, `state_mutation: 244`, `dead_code: 28`, `duplicate_logic: 82`
* *Architecture:* `io: 3`, `api: 262`, `concurrency: 18`, `import: 8`
* *Defense:* `safety: 37`, `doc: 65`, `test: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.77
  * `Choke Point (Betweenness):` 0.01249 | `Ripple Effect (Closeness):` 0.076812
  * `Imports (Out-Degree: 10):` index.js, json-schema-processors.js, standard-schema.js, to-json-schema.js, checks.js, iso.js, parse.js
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `packages/zod/src/v3/tests/refine.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.901)
- **Top Global Matches:** file_cluster_10: 4.901, file_cluster_2: 7.289, file_cluster_13: 7.335
- **Magnitude:** 1464.85 | **LOC:** 314 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.653; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (82.1%), Guard Balance (formerly Safety Score) (36.2%), Complexity Load (formerly Cognitive Load) (11.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 68`, `args: 38`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 10`, `concurrency: 13`, `import: 4`
* *Defense:* `safety: 25`, `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ZodError.js, util.js, vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/object.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.48)
- **Top Global Matches:** file_cluster_0: 8.48, file_cluster_5: 8.536, file_cluster_10: 8.6
- **Magnitude:** 1251.71 | **LOC:** 435 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.653; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (90.5%), Guard Balance (formerly Safety Score) (25.3%), Complexity Load (formerly Cognitive Load) (11.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 99`, `args: 42`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 6`, `planned_debt: 1`
* *Architecture:* `concurrency: 20`, `import: 3`
* *Defense:* `safety: 75`, `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` util.js, vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/partial.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.461)
- **Top Global Matches:** file_cluster_10: 4.461, file_cluster_2: 5.95, file_cluster_13: 6.947
- **Magnitude:** 1187.75 | **LOC:** 428 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.653; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (73.0%), Guard Balance (formerly Safety Score) (23.2%), Complexity Load (formerly Cognitive Load) (11.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 33`, `args: 26`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 4`, `concurrency: 4`, `import: 2`
* *Defense:* `safety: 83`, `test: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/transformer.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.105)
- **Top Global Matches:** file_cluster_10: 4.105, file_cluster_2: 6.822, file_cluster_13: 7.285
- **Magnitude:** 1063.53 | **LOC:** 234 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.653; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (95.4%), Complexity Load (formerly Cognitive Load) (15.0%), Dead Code Surface (formerly Dead Code) (9.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 49`, `args: 34`, `func_start: 4`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `io: 2`, `concurrency: 14`, `import: 3`
* *Defense:* `safety: 13`, `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` util.js, vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/discriminated-unions.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.851)
- **Top Global Matches:** file_cluster_10: 4.851, file_cluster_2: 6.232, file_cluster_13: 6.949
- **Magnitude:** 1041.88 | **LOC:** 662 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.653; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (38.9%), Guard Balance (formerly Safety Score) (28.2%), Dead Code Surface (formerly Dead Code) (8.8%), Complexity Load (formerly Cognitive Load) (7.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 152`, `args: 35`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `dead_code: 2`
* *Architecture:* `io: 9`, `concurrency: 11`, `import: 2`
* *Defense:* `safety: 95`, `test: 82`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/transform.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.448)
- **Top Global Matches:** file_cluster_10: 5.448, file_cluster_12: 6.721, file_cluster_2: 7.312
- **Magnitude:** 1028.98 | **LOC:** 362 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.653; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (77.0%), Guard Balance (formerly Safety Score) (41.5%), Complexity Load (formerly Cognitive Load) (10.6%), Dead Code Surface (formerly Dead Code) (8.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 61`, `args: 41`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 4`, `dead_code: 1`
* *Architecture:* `io: 11`, `concurrency: 14`, `import: 2`
* *Defense:* `safety: 15`, `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/partials.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.773)
- **Top Global Matches:** file_cluster_10: 4.773, file_cluster_2: 6.533, file_cluster_13: 7.128
- **Magnitude:** 1003.56 | **LOC:** 244 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.653; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (94.8%), Guard Balance (formerly Safety Score) (24.9%), Complexity Load (formerly Cognitive Load) (18.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 29`, `args: 15`, `func_start: 2`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `concurrency: 4`, `import: 4`
* *Defense:* `safety: 41`, `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` util.js, vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/api.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.619)
- **Top Global Matches:** file_cluster_5: 7.619, file_cluster_12: 9.442, file_cluster_0: 10.018
- **Magnitude:** 868.0 | **LOC:** 1799 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **6**; blast radius 10.538; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.2%)
- **Documentation Coverage:** 97.5309% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_stringbool` **(Defensive Guards)** (Impact: 44.7)
  * `_superRefine` **(Defensive Guards)** (Impact: 12.4)
  * `_tuple` **(Many-Argument Workhorses)** (Impact: 12.0)
    * *Intent:* // export function _tuple( // Class: util.SchemaClass<schemas.$ZodTuple>, // items: [], // params?: ...
  * `addIssue` **(Defensive Guards)** (Impact: 12.0)
  * `_stringFormat` **(Generic / Templated Code)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 769`, `args: 139`, `func_start: 124`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 20`, `dead_code: 9`, `duplicate_logic: 2`, `unreferenced_by_name: 104`
* *Architecture:* `io: 1`, `api: 250`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 13`, `doc: 7`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.538
  * `Choke Point (Betweenness):` 0.000339 | `Ripple Effect (Closeness):` 0.134971
  * `Imports (Out-Degree: 6):` checks.js, core.js, errors.js, registries.js, schemas.js, util.js
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `packages/zod/src/v4/mini/schemas.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.765)
- **Top Global Matches:** file_cluster_5: 7.765, file_cluster_12: 11.379, file_cluster_7: 11.814
- **Magnitude:** 789.18 | **LOC:** 1917 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 68.8%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 2.668; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (98.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.0%)
- **Documentation Coverage:** 97.6378% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_function` **(Defensive Guards)** (Impact: 16.1)
  * `hash` **(Defensive Guards)** (Impact: 11.0)
  * `tuple` **(Compute Cores)** (Impact: 10.8)
  * `object` **(Generic / Templated Code)** (Impact: 7.5)
  * `register` **(Generic / Templated Code)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 843`, `args: 221`, `func_start: 147`, `class_start: 74`
* *Risk/State:* `safety_bypasses: 104`, `state_mutation: 19`, `dead_code: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 262`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 14`, `doc: 5`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.668
  * `Choke Point (Betweenness):` 0.000312 | `Ripple Effect (Closeness):` 0.02024
  * `Imports (Out-Degree: 4):` index.js, util.js, parse.js
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/zod/src/v4/core/json-schema-processors.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 12.645)
- **Top Global Matches:** file_cluster_4: 12.645, file_cluster_5: 12.722, file_cluster_7: 12.769
- **Magnitude:** 742.38 | **LOC:** 668 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **6**; blast radius 7.193; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `numberProcessor` **(Many-Argument Workhorses)** (Impact: 53.4)
  * `literalProcessor` **(Many-Argument Workhorses)** (Impact: 51.1)
  * `tupleProcessor` **(Many-Argument Workhorses)** (Impact: 42.9)
  * `stringProcessor` **(Many-Argument Workhorses)** (Impact: 37.5)
    * *Intent:* // ==================== SIMPLE TYPE PROCESSORS ====================
  * `recordProcessor` **(Many-Argument Workhorses)** (Impact: 29.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 149`, `args: 55`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 92`
* *Architecture:* `io: 22`, `api: 43`, `import: 6`
* *Defense:* `safety: 9`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.193
  * `Choke Point (Betweenness):` 0.001508 | `Ripple Effect (Closeness):` 0.131932
  * `Imports (Out-Degree: 6):` checks.js, json-schema.js, registries.js, schemas.js, to-json-schema.js, util.js
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/zod/src/v4/core/util.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.47)
- **Top Global Matches:** file_cluster_5: 8.47, file_cluster_12: 11.251, file_cluster_7: 11.664
- **Magnitude:** 709.3 | **LOC:** 979 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **62** in-repo importer(s); it depends on **4**; blast radius 66.484; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.7%), Mutation Surface (formerly State Flux) (88.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getParsedType` **(Compute Cores)** (Impact: 39.5)
  * `finalizeIssue` **(Defensive Guards)** (Impact: 33.4)
  * `partial` **(Many-Argument Workhorses)** (Impact: 24.6)
  * `floatSafeRemainder` **(Defensive Guards)** (Impact: 18.1)
  * `parsedType` **(Compute Cores)** (Impact: 16.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 31 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 462`, `args: 102`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 76`, `state_mutation: 31`, `dead_code: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 47`
* *Architecture:* `io: 9`, `api: 131`, `concurrency: 4`, `import: 5`
* *Defense:* `safety: 40`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 66.484
  * `Choke Point (Betweenness):` 0.007016 | `Ripple Effect (Closeness):` 0.158846
  * `Imports (Out-Degree: 4):` checks.js, core.js, errors.js, schemas.js
  * `Imported By (In-Degree: 62):` (Excluded from Brief to save tokens)

### `packages/zod/src/v3/tests/discriminated-unions.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.429)
- **Top Global Matches:** file_cluster_12: 6.429, file_cluster_7: 7.437, file_cluster_10: 7.793
- **Magnitude:** 539.27 | **LOC:** 316 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.653; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (65.1%), Guard Balance (formerly Safety Score) (26.5%), Complexity Load (formerly Cognitive Load) (8.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 103`, `args: 22`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`
* *Architecture:* `io: 4`, `concurrency: 10`, `import: 2`
* *Defense:* `safety: 69`, `test: 36`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/checks.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.349)
- **Top Global Matches:** file_cluster_5: 8.349, file_cluster_0: 8.447, file_cluster_12: 9.018
- **Magnitude:** 505.76 | **LOC:** 1294 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **54** in-repo importer(s); it depends on **5**; blast radius 44.325; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (93.8%), Guard Balance (formerly Safety Score) (65.4%), Complexity Load (formerly Cognitive Load) (55.9%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check` **(Compute Cores)** (Impact: 15.8)
  * `check` **(Compute Cores)** (Impact: 6.6)
  * `check` **(Callbacks & Closures)** (Impact: 6.4)
  * `check` **(Callbacks & Closures)** (Impact: 6.4)
  * `check` **(Compute Cores)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 97 instances
* *State Mutation (weighted view):* 299
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 388`, `args: 70`, `func_start: 21`, `class_start: 66`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 105`, `dead_code: 19`
* *Architecture:* `api: 93`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 26`, `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 44.325
  * `Choke Point (Betweenness):` 0.006446 | `Ripple Effect (Closeness):` 0.155085
  * `Imports (Out-Degree: 5):` core.js, errors.js, regexes.js, schemas.js, util.js
  * `Imported By (In-Degree: 54):` (Excluded from Brief to save tokens)

### `packages/zod/src/v4/classic/tests/tuple.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.496)
- **Top Global Matches:** file_cluster_7: 6.496, file_cluster_12: 7.031, file_cluster_10: 9.03
- **Magnitude:** 488.56 | **LOC:** 184 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.653; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (88.5%), Guard Balance (formerly Safety Score) (40.3%), Complexity Load (formerly Cognitive Load) (12.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 22`, `args: 15`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 6`
* *Architecture:* `io: 6`, `concurrency: 9`, `import: 2`
* *Defense:* `safety: 9`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/standard-schema.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.429)
- **Top Global Matches:** file_cluster_10: 5.429, file_cluster_2: 7.705, file_cluster_13: 8.005
- **Magnitude:** 463.58 | **LOC:** 84 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.653; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (52.8%), Dead Code Surface (formerly Dead Code) (17.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 20`, `args: 9`, `func_start: 2`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `io: 2`, `concurrency: 14`, `import: 4`
* *Defense:* `safety: 9`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` util.js, standard-schema.js, vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/set.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.553)
- **Top Global Matches:** file_cluster_10: 6.553, file_cluster_12: 6.891, file_cluster_2: 8.542
- **Magnitude:** 446.05 | **LOC:** 143 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.653; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (55.5%), Guard Balance (formerly Safety Score) (30.3%), Complexity Load (formerly Cognitive Load) (14.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 21`, `args: 13`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`
* *Architecture:* `io: 3`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 10`, `test: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` util.js, vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/record.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.727)
- **Top Global Matches:** file_cluster_10: 5.727, file_cluster_0: 6.458, file_cluster_2: 6.947
- **Magnitude:** 348.1 | **LOC:** 633 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 80.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.653; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (46.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (45.4%), Guard Balance (formerly Safety Score) (36.6%), Complexity Load (formerly Cognitive Load) (7.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 58`, `args: 29`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 21`, `concurrency: 13`, `import: 2`
* *Defense:* `safety: 38`, `test: 84`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/mini/tests/string.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.551)
- **Top Global Matches:** file_cluster_10: 8.551, file_cluster_12: 9.224, file_cluster_7: 10.385
- **Magnitude:** 336.43 | **LOC:** 348 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.653; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (100.0%), Dead Code Surface (formerly Dead Code) (73.3%), Concurrency Surface (formerly Concurrency) (44.1%), Guard Balance (formerly Safety Score) (9.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 106`, `args: 101`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `dead_code: 14`
* *Architecture:* `io: 53`, `concurrency: 6`, `import: 2`
* *Defense:* `safety: 85`, `test: 148`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, mini
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/map.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.095)
- **Top Global Matches:** file_cluster_7: 6.095, file_cluster_12: 6.281, file_cluster_5: 8.06
- **Magnitude:** 325.28 | **LOC:** 331 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.653; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (48.3%), Guard Balance (formerly Safety Score) (44.7%), Dead Code Surface (formerly Dead Code) (11.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 24`, `args: 16`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `dead_code: 2`
* *Architecture:* `io: 11`, `concurrency: 8`, `import: 2`
* *Defense:* `safety: 11`, `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tsc/generate.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.24)
- **Top Global Matches:** file_cluster_3: 7.24, file_cluster_8: 20.677, file_cluster_6: 33.443
- **Magnitude:** 303.42 | **LOC:** 356 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **6**; blast radius 3.981; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Dead Code Surface (formerly Dead Code) (85.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.6%)
- **Documentation Coverage:** 94.135% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate` **(Compute Cores)** (Impact: 42.1)
    * *Intent:* // Step 4: Write the generated schemas to a file
  * `generateExtendChain` **(Compute Cores)** (Impact: 36.9)
  * `generateFields` **(Generic / Templated Code)** (Impact: 4.3)
    * *Intent:* // Step 3: Generate a random Zod schema
  * `randomStr` **(Compute Cores)** (Impact: 3.3)
    * *Intent:* // Step 2: Generate a random string for keys and variable names
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 188
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 50`, `args: 10`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 66`, `dead_code: 19`
* *Architecture:* `io: 8`, `api: 24`, `import: 6`
* *Defense:* `safety: 8`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.981
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01432
  * `Imports (Out-Degree: 0):` arktype, node:fs, node:path, valibot, v4, zod3
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/zod/src/v4/core/errors.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 14.369)
- **Top Global Matches:** file_cluster_8: 14.369, file_cluster_6: 16.596, file_cluster_4: 23.169
- **Magnitude:** 297.94 | **LOC:** 449 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **59** in-repo importer(s); it depends on **5**; blast radius 57.498; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.4%), Connectivity (formerly Api Exposure) (94.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.5%)
- **Documentation Coverage:** 93.1034% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `treeifyError` **(Defensive Guards)** (Impact: 33.5)
  * `processError` **(Defensive Guards)** (Impact: 33.2)
  * `formatError` **(Compute Cores)** (Impact: 29.5)
  * `processError` **(Compute Cores)** (Impact: 24.1)
  * `toDotPath` **(Compute Cores)** (Impact: 14.9)
    * *Intent:* * } * ]; * } * ``` * * to * * ``` * username * ✖ Expected number, received string at "username * fav...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 161`, `args: 19`, `func_start: 15`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 27`
* *Architecture:* `io: 22`, `api: 42`, `import: 5`
* *Defense:* `safety: 7`, `doc: 6`, `immutability_locks: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 57.498
  * `Choke Point (Betweenness):` 0.007615 | `Ripple Effect (Closeness):` 0.156172
  * `Imports (Out-Degree: 5):` checks.js, core.js, schemas.js, standard-schema.js, util.js
  * `Imported By (In-Degree: 59):` (Excluded from Brief to save tokens)

### `packages/zod/src/v3/tests/preprocess.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.743)
- **Top Global Matches:** file_cluster_10: 6.743, file_cluster_12: 6.941, file_cluster_7: 8.648
- **Magnitude:** 294.84 | **LOC:** 187 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.653; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (92.7%), Guard Balance (formerly Safety Score) (35.4%), Complexity Load (formerly Cognitive Load) (11.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 38`, `args: 23`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `io: 5`, `concurrency: 11`, `import: 3`
* *Defense:* `safety: 21`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` util.js, vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/zod/src/v3/tests/object.test.ts` (TYPESCRIPT) | Magnitude: 1251.71 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 268, structural_boundaries: 99, core_var_decl: 77, safety: 75

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `packages/zod/src/v3/tests/nativeEnum.test.ts` (TYPESCRIPT) | Magnitude: 16.48 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 25, core_var_decl: 17, test: 12
- `packages/zod/src/v4/classic/tests/to-json-schema.test.ts` (TYPESCRIPT) | Magnitude: 104.22 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 2638, structural_boundaries: 441, test: 267, io: 159

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/zod/src/v4/classic/tests/prefault.test.ts` (TYPESCRIPT) | Magnitude: 16.2 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 50, test: 12, structural_boundaries: 11, core_var_decl: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/integration/fixtures/ai-sdk/index.ts` (TYPESCRIPT) | Magnitude: 0.02 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, safety: 3, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/zod/src/v4/locales/lt.ts` (TYPESCRIPT) | Magnitude: 0.03 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 215, branch: 41, structural_boundaries: 39, safety: 25
- `packages/zod/src/v4/locales/index.ts` (TYPESCRIPT) | Magnitude: 0.07 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: branch: 50, structural_boundaries: 50, api: 50, import: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/zod/src/v4/classic/external.ts` (TYPESCRIPT) | Magnitude: 30.82 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 20, import: 17, api: 15
- `packages/zod/src/v4/core/index.ts` (TYPESCRIPT) | Magnitude: 31.32 | Delta: **0.18** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 16, api: 16, import: 16, explicit_casts: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/bench/safeparse.ts` (TYPESCRIPT) | Magnitude: 6.4 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 20, safety: 5, core_var_decl: 5, structural_boundaries: 4
- `packages/zod/src/v4/mini/external.ts` (TYPESCRIPT) | Magnitude: 26.64 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 12, api: 11, import: 11
- `packages/zod/src/v4/core/versions.ts` (TYPESCRIPT) | Magnitude: 13.6 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 3, structural_boundaries: 1, api: 1, immutability_locks: 1
- `packages/zod/src/v3/external.ts` (TYPESCRIPT) | Magnitude: 19.12 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 6, api: 6, import: 6
- `packages/zod/src/v4/classic/tests/firstparty.test.ts` (TYPESCRIPT) | Magnitude: 18.52 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 169, structural_boundaries: 100, branch: 83, safety: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/zod/src/v4/core/json-schema-processors.ts` (TYPESCRIPT) | Magnitude: 742.38 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 468, structural_boundaries: 149, branch: 147, state_mutation: 92

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/zod/src/v4/classic/tests/lazy.test.ts` (TYPESCRIPT) | Magnitude: 11.4 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 164, structural_boundaries: 48, args: 38, closures: 33
- `packages/zod/src/v4/classic/tests/anyunknown.test.ts` (TYPESCRIPT) | Magnitude: 15.44 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 14, args: 6, test: 6
- `packages/zod/src/v4/core/checks.ts` (TYPESCRIPT) | Magnitude: 505.76 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 705, structural_boundaries: 388, generics: 141, state_mutation: 105
- `packages/zod/src/v4/core/core.ts` (TYPESCRIPT) | Magnitude: 102.34 | Delta: **0.196** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 60, branch: 27, generics: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/zod/src/v3/tests/Mocker.ts` (TYPESCRIPT) | Magnitude: 30.62 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 19, args: 16, func_start: 16
- `packages/zod/src/v4/classic/tests/error.test.ts` (TYPESCRIPT) | Magnitude: 29.62 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 503, test: 127, safety: 80, structural_boundaries: 68
- `packages/zod/src/v3/tests/function.test.ts` (TYPESCRIPT) | Magnitude: 69.46 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 171, structural_boundaries: 79, args: 51, core_var_decl: 48
- `scripts/fail-on-console.ts` (TYPESCRIPT) | Magnitude: 5.0 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 5, args: 4, closures: 3

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/zod/src/v4/classic/schemas.ts` -> Churn: **100.0%** | Cog Load: 23.4248% | Debt: 99.976%
- `packages/zod/src/v4/core/schemas.ts` -> Churn: **100.0%** | Cog Load: 59.9418% | Debt: 10.3456%
- `packages/zod/src/v4/core/util.ts` -> Churn: **82.96%** | Cog Load: 40.9394% | Debt: 97.7358%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/zod/src/v4/classic/tests/partial.test.ts` -> **kevinmitch14** (100.0% isolated ownership) | Magnitude: 1187.75
- `packages/zod/src/v4/core/json-schema-processors.ts` -> **Colin McDonnell** (83.3% isolated ownership) | Magnitude: 742.38
- `packages/zod/src/v4/classic/tests/tuple.test.ts` -> **Alexander “weej” Jones** (100.0% isolated ownership) | Magnitude: 488.56
- `packages/zod/src/v4/mini/tests/string.test.ts` -> **Nathaniel Gerlek** (100.0% isolated ownership) | Magnitude: 336.43
- `packages/zod/src/v4/classic/tests/map.test.ts` -> **Christopher Hiller** (100.0% isolated ownership) | Magnitude: 325.28

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/zod/src/v4/core/schemas.ts` -> **Severity: 2.206** (Bridge: 0.0221 * Flux: 99.8878%)
- `packages/zod/src/v4/core/to-json-schema.ts` -> **Severity: 2.026** (Bridge: 0.0204 * Flux: 99.4924%)
- `packages/bench/benchUtil.ts` -> **Severity: 1.325** (Bridge: 0.0161 * Flux: 82.2653%)
- `packages/zod/src/v4/classic/schemas.ts` -> **Severity: 1.241** (Bridge: 0.0125 * Flux: 99.3512%)
- `packages/zod/src/v4/core/errors.ts` -> **Severity: 0.734** (Bridge: 0.0076 * Flux: 96.4337%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/zod/src/v4/core/util.ts` -> **Severity: 12.038** (Embedded: 0.1588 * Error Risk: 75.7831%)
- `packages/zod/src/v4/core/core.ts` -> **Severity: 10.732** (Embedded: 0.1448 * Error Risk: 74.1176%)
- `packages/zod/src/v4/core/errors.ts` -> **Severity: 10.548** (Embedded: 0.1562 * Error Risk: 67.5414%)
- `packages/zod/src/v4/core/json-schema-processors.ts` -> **Severity: 10.49** (Embedded: 0.1319 * Error Risk: 79.5136%)
- `packages/zod/src/v4/core/checks.ts` -> **Severity: 10.148** (Embedded: 0.1551 * Error Risk: 65.4377%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/zod/src/v4/core/util.ts` -> **Severity: 6648.4** (Blast Radius: 66.484 * Doc Risk: 100.0%)
- `packages/zod/src/v4/core/errors.ts` -> **Severity: 5353.259** (Blast Radius: 57.498 * Doc Risk: 93.1034%)
- `packages/zod/src/v4/core/schemas.ts` -> **Severity: 5204.581** (Blast Radius: 54.067 * Doc Risk: 96.2617%)
- `packages/zod/src/v4/core/checks.ts` -> **Severity: 4221.429** (Blast Radius: 44.325 * Doc Risk: 95.2381%)
- `packages/zod/src/v4/core/core.ts` -> **Severity: 2504.688** (Blast Radius: 43.832 * Doc Risk: 57.1429%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2802 call pairs -- scoped 45.5%, unique 0.0%, ambiguous 11.1%, external 43.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 2790 | 45.7% | 0.0% | 11.1% | 43.2% |
| html | 12 | 0.0% | 0.0% | 0.0% | 100.0% |

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
