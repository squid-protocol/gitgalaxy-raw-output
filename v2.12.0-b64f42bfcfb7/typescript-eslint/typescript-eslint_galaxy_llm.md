# ARCHITECTURAL_BRIEF: typescript-eslint
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/typescript-eslint/typescript-eslint.git` |
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
- **Scope:** 2922 analyzed artifact(s), 263179 LOC.
- **Load-bearing artifact:** `packages/ast-spec/src/ast-node-types.ts` -- 171 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/ast-spec/src/unions/Node.ts` -- pulls in 168 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/eslint-plugin/tests/rules/member-ordering.test.ts` at magnitude 32083.7 (structural weight, not risk).
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
| Total Artifacts | 8445 |
| Analyzed Artifacts (Scanned) | 2922 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5523 |
| Total LOC | 263179 |
| Volatility Index | 0.008 |
| % Scanned of codebase = | 34.6% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8086 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2393 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.9035 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 211 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2604 | 256210 | 89.1% |
| JSON | 96 | 1823 | 3.3% |
| MARKDOWN | 57 | 0 | 2.0% |
| JAVASCRIPT | 44 | 1626 | 1.5% |
| CSS | 36 | 1668 | 1.2% |
| PLAINTEXT | 32 | 1 | 1.1% |
| YAML | 28 | 1736 | 1.0% |
| XML | 18 | 0 | 0.6% |
| HTML | 7 | 115 | 0.2% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 2921 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 59%, Declarative / Non-Code 21%, Compute Cores Files 5%, Large Core Modules (3) 3%, Large Core Modules (2) 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2833 | 97.0% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 88 | 3.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5523*

**Composition by Extension & Reason:**
- `.shot`: 4641x Unsupported Format (.shot), 556x Excluded (Unsupported Extension: '.shot')
- `.mdx`: 191x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 6140 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2227 LOC)
- `no_extension`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.ts`: 19x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1814 LOC)
- `.snap`: 15x Excluded (Unsupported Extension: '.snap')
- `.png`: 11x Excluded (Explicitly Denied Extension: '.png')
- `.jpg`: 8x Excluded (Explicitly Denied Extension: '.jpg')
- `.json`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mts`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.unknown`: 1x Excluded (Unsupported Extension: '.unknown')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 81.8 | 12.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 7.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.9 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 5.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.6 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.4 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 68.2 | 2.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 26.8 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 76.9 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 800 | 219 | 0 | `packages/eslint-plugin/tests/rules/consistent-type-assertions.test.ts` |
| cleanup | 40 | 11 | 0 | `packages/scope-manager/src/referencer/Referencer.ts` |
| guards | 8853 | 729 | 4 | `packages/eslint-plugin/tests/rules/member-ordering.test.ts` |
| danger | 2663 | 406 | 1 | `packages/eslint-plugin/tests/rules/no-explicit-any.test.ts` |
| concurrency | 4585 | 204 | 0 | `packages/eslint-plugin/tests/rules/no-floating-promises.test.ts` |
| connectivity | 5678 | 1334 | 4 | `packages/eslint-plugin/tests/rules/member-ordering.test.ts` |
| io | 947 | 154 | 0 | `packages/eslint-plugin/tests/rules/no-floating-promises.test.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 15 | 4 | 0 | `packages/eslint-plugin/tests/rules/naming-convention/naming-convention.test.ts` |
| time | 140 | 21 | 0 | `packages/eslint-plugin/tests/rules/no-implied-eval.test.ts` |
| serialization | 65 | 38 | 0 | `packages/website/src/components/hooks/useHashState.ts` |
| regex | 230 | 76 | 0 | `packages/eslint-plugin/tests/rules/prefer-regexp-exec.test.ts` |
| events | 296 | 83 | 0 | `eslint.config.mjs` |
| tests | 4309 | 173 | 0 | `packages/scope-manager/tests/eslint-scope/es6-destructuring-assignments.test.ts` |
| docs | 4224 | 767 | 3 | `packages/eslint-plugin/tests/rules/no-deprecated.test.ts` |
| debt | 1320 | 532 | 1 | `packages/eslint-plugin/tests/rules/no-confusing-void-expression.test.ts` |
| mutation | 21199 | 1520 | 16 | `packages/eslint-plugin/tests/rules/member-ordering.test.ts` |
| dead_code | 499 | 340 | 1 | `packages/eslint-plugin/src/rules/strict-boolean-expressions.ts` |
| credential | 1 | 1 | 0 | `packages/website/docusaurus.config.mts` |
| threat | 57 | 2 | 0 | `packages/eslint-plugin/tests/rules/ban-ts-comment.test.ts` |
| ml_ai | 312 | 38 | 0 | `packages/eslint-plugin/tests/rules/strict-boolean-expressions.test.ts` |
| ui | 903 | 128 | 0 | `packages/eslint-plugin/tests/rules/consistent-type-assertions.test.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/eslint-plugin/tests/rules/no-floating-promises.test.ts` (Hits: 49)
- `packages/integration-tests/tools/pack-packages.ts` (Hits: 39)
- `packages/typescript-estree/tests/lib/semanticInfo.test.ts` (Hits: 37)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ast-node-types.ts** (`packages/ast-spec/src/ast-node-types.ts`) — 171 inbound connections
2. **BaseNode.ts** (`packages/ast-spec/src/base/BaseNode.ts`) — 155 inbound connections
3. **index.ts** (`packages/eslint-plugin/src/util/index.ts`) — 147 inbound connections
4. **index.ts** (`packages/scope-manager/src/variable/index.ts`) — 127 inbound connections
5. **base-config.ts** (`packages/scope-manager/src/lib/base-config.ts`) — 87 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Node.ts** (`packages/ast-spec/src/unions/Node.ts`) — 168 outbound dependencies
2. **index.ts** (`packages/eslint-plugin/src/rules/index.ts`) — 135 outbound dependencies
3. **index.ts** (`packages/scope-manager/src/lib/index.ts`) — 120 outbound dependencies
4. **index.ts** (`packages/ast-spec/src/index.ts`) — 49 outbound dependencies
5. **spec.ts** (`packages/ast-spec/src/type/spec.ts`) — 45 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `isValidEscape` **(Many-Argument Workhorses)** (@ `packages/typescript-estree/src/convert.ts`) -> Impact: **752.1** | LOC: 2964
- `convertNode` **(Many-Argument Workhorses)** (@ `packages/typescript-estree/src/convert.ts`) -> Impact: **665.2** | LOC: 2185
  * *Intent:* /** * Converts a TypeScript node into an ESTree node. * The core of the conversion logic: * Identify and convert each relevant TypeScript SyntaxKind *...
- `create` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin/src/rules/no-unused-vars.ts`) -> Impact: **350.5** | LOC: 1052
- `checkSyntaxError` **(Many-Argument Workhorses)** (@ `packages/typescript-estree/src/check-syntax-errors.ts`) -> Impact: **340.9** | LOC: 618
- `create` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin/src/rules/no-misused-promises.ts`) -> Impact: **254.8** | LOC: 523
- `create` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin/src/rules/no-unnecessary-condition.ts`) -> Impact: **242.8** | LOC: 699
- `create` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin/src/rules/consistent-type-imports.ts`) -> Impact: **238.5** | LOC: 855
- `create` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin/src/rules/prefer-string-starts-ends-with.ts`) -> Impact: **230.2** | LOC: 654
- `create` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin/src/rules/no-shadow.ts`) -> Impact: **222.6** | LOC: 606
- `create` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin/src/rules/strict-boolean-expressions.ts`) -> Impact: **216.8** | LOC: 872

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/eslint-plugin/tests/rules` | 130 | 80835.11 | 0.5% | 0.0% |
| `packages/eslint-plugin/src/rules` | 135 | 21109.69 | 10.89% | 3.9% |
| `packages/eslint-plugin/tests/rules/member-ordering` | 5 | 8576.09 | 5.46% | 0.0% |
| `__monolith__` | 19 | 5240.18 | 0.7% | 0.49% |
| `packages/typescript-estree/src` | 20 | 3507.84 | 8.91% | 6.75% |
| `packages/scope-manager/tests/eslint-scope` | 32 | 3418.63 | 1.03% | 0.0% |
| `packages/type-utils/tests` | 12 | 2762.69 | 3.0% | 0.0% |
| `packages/eslint-plugin/src/util` | 46 | 1958.58 | 6.8% | 0.61% |
| `packages/scope-manager/src/lib` | 120 | 1878.12 | 0.0% | 0.0% |
| `packages/typescript-estree/tests/lib` | 18 | 1713.52 | 4.27% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/ast-spec/src/legacy-fixtures/types/fixtures/this-type-expanded/fixture.ts` -> **100.0%** Exposure
- `packages/ast-spec/src/legacy-fixtures/basics/fixtures/class-with-optional-computed-method/fixture.ts` -> **99.9999%** Exposure
- `.github/ISSUE_TEMPLATE/08-bug-report-complex.yaml` -> **99.9995%** Exposure
- `packages/ast-spec/src/legacy-fixtures/basics/fixtures/interface-with-all-property-types/fixture.ts` -> **99.9983%** Exposure
- `packages/eslint-plugin/typings/typescript.d.ts` -> **99.9983%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/website-eslint/src/index.js` -> **100.0%** Exposure
- `packages/website-eslint/src/mock/assert.js` -> **100.0%** Exposure
- `packages/website-eslint/src/mock/path.js` -> **100.0%** Exposure
- `packages/ast-spec/tests/util/serializers/Node.ts` -> **100.0%** Exposure
- `packages/eslint-plugin/src/util/baseTypeUtils.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/eslint-plugin/typings/eslint-rules.d.ts` -> **9** Orphaned Functions | **19** Duplicates
- `packages/scope-manager/tests/types/reference-type.test.ts` -> **2** Orphaned Functions | **11** Duplicates
- `packages/scope-manager/tests/test-utils/custom-matchers/vitest-custom-matchers.d.ts` -> **10** Orphaned Functions | **0** Duplicates
- `packages/type-utils/tests/test-utils/custom-matchers/vitest-custom-matchers.d.ts` -> **9** Orphaned Functions | **0** Duplicates
- `packages/eslint-plugin/tests/rules/prefer-optional-chain/prefer-optional-chain.test.ts` -> **0** Orphaned Functions | **8** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `packages/website/docusaurus.config.mts` -> **76.8824%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1868` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/eslint-plugin/tests/rules/member-ordering.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.947)
- **Top Global Matches:** file_cluster_12: 5.947, file_cluster_2: 6.932, file_cluster_17: 7.281
- **Magnitude:** 32083.7 | **LOC:** 5352 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.8%), Connectivity (formerly Api Exposure) (3.8%), Complexity Load (formerly Cognitive Load) (2.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 257`, `args: 574`, `func_start: 569`, `class_start: 133`
* *Risk/State:* `safety_bypasses: 88`, `state_mutation: 14`
* *Architecture:* `api: 279`, `import: 4`
* *Defense:* `doc: 2`, `immutability_locks: 165`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` member-ordering, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/member-ordering/member-ordering-alphabetically-order.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.667)
- **Top Global Matches:** file_cluster_2: 3.667, file_cluster_17: 4.961, file_cluster_13: 4.971
- **Magnitude:** 6473.52 | **LOC:** 2735 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (6.1%), Complexity Load (formerly Cognitive Load) (5.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 272`, `args: 114`, `func_start: 114`, `class_start: 69`
* *Risk/State:* None
* *Architecture:* `api: 132`, `import: 4`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` member-ordering, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/no-floating-promises.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.029)
- **Top Global Matches:** file_cluster_10: 6.029, file_cluster_0: 8.168, file_cluster_2: 8.231
- **Magnitude:** 5549.62 | **LOC:** 5619 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (37.4%), Complexity Load (formerly Cognitive Load) (22.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (5.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Concurrency (weighted view):* 1274
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 1755`, `args: 845`, `func_start: 249`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 3`, `planned_debt: 1`
* *Architecture:* `io: 49`, `api: 2`, `concurrency: 1239`, `import: 4`
* *Defense:* `safety: 649`, `doc: 1`, `test: 139`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` no-floating-promises, RuleTester, node:path, node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/type-utils/tests/isTypeReadonly.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.949)
- **Top Global Matches:** file_cluster_10: 6.949, file_cluster_0: 8.097, file_cluster_13: 8.761
- **Magnitude:** 2510.7 | **LOC:** 441 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.2%), Complexity Load (formerly Cognitive Load) (3.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 158`, `args: 67`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `import: 3`
* *Defense:* `safety: 19`, `doc: 1`, `test: 65`, `immutability_locks: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` index.js, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/no-misused-promises.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.743)
- **Top Global Matches:** file_cluster_10: 5.743, file_cluster_0: 6.987, file_cluster_2: 7.427
- **Magnitude:** 1998.68 | **LOC:** 2664 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (50.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (5.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 28 instances
* *Concurrency (weighted view):* 461
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 973`, `args: 399`, `func_start: 225`, `class_start: 141`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 13`
* *Architecture:* `api: 7`, `concurrency: 321`, `import: 2`
* *Defense:* `safety: 13`, `doc: 2`, `test: 17`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` no-misused-promises, RuleTester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/typescript-estree/src/convert.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.766)
- **Top Global Matches:** file_cluster_4: 6.766, file_cluster_6: 10.727, file_cluster_16: 12.398
- **Magnitude:** 1953.14 | **LOC:** 3059 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 64.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 0.451; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (70.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.6%), Guard Balance (formerly Safety Score) (53.5%), Complexity Load (formerly Cognitive Load) (23.3%)
- **Documentation Coverage:** 53.1915% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isValidEscape` **(Many-Argument Workhorses)** (Impact: 752.1)
  * `convertNode` **(Many-Argument Workhorses)** (Impact: 665.2)
    * *Intent:* /** * Converts a TypeScript node into an ESTree node. * The core of the conversion logic: * Identify...
  * `deeplyCopy` **(Compute Cores)** (Impact: 35.4)
    * *Intent:* /** * For nodes that are copied directly from the TypeScript AST into * ESTree mostly as-is. The onl...
  * `fixExports` **(Many-Argument Workhorses)** (Impact: 24.7)
    * *Intent:* /** * Fixes the exports of the given ts.Node */
  * `convertChainExpression` **(Stateful Encapsulated Methods)** (Impact: 21.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 212
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 434`, `structural_boundaries: 563`, `args: 58`, `func_start: 33`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 78`, `planned_debt: 3`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 6`, `import: 9`
* *Defense:* `safety: 44`, `doc: 39`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.451
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.002919
  * `Imports (Out-Degree: 6):` check-syntax-errors, getModifiers, node-utils, parser-options, semantic-or-syntactic-errors, ts-estree, typescript
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin/tests/rules/strict-boolean-expressions.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.39)
- **Top Global Matches:** file_cluster_2: 5.39, file_cluster_12: 6.204, file_cluster_10: 6.243
- **Magnitude:** 1858.48 | **LOC:** 4769 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (47.4%), Concurrency Surface (formerly Concurrency) (12.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (5.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (5.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 643`, `args: 315`, `func_start: 133`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 5`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `concurrency: 3`, `import: 4`
* *Defense:* `safety: 119`, `doc: 1`, `test: 135`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` strict-boolean-expressions, RuleTester, rule-tester, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/strict-void-return.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.346)
- **Top Global Matches:** file_cluster_10: 5.346, file_cluster_2: 7.29, file_cluster_0: 7.426
- **Magnitude:** 1811.03 | **LOC:** 2795 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (62.4%), Guard Balance (formerly Safety Score) (51.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Concurrency (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1188`, `args: 507`, `func_start: 255`, `class_start: 96`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 51`, `fragile_debt: 3`
* *Architecture:* `concurrency: 68`, `import: 3`
* *Defense:* `safety: 20`, `doc: 1`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` strict-void-return, RuleTester, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/member-ordering/member-ordering-alphabetically-case-insensitive-order.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.855)
- **Top Global Matches:** file_cluster_2: 2.855, file_cluster_17: 4.483, file_cluster_13: 4.596
- **Magnitude:** 1566.63 | **LOC:** 733 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (5.9%), Complexity Load (formerly Cognitive Load) (5.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 59`, `args: 25`, `func_start: 25`, `class_start: 14`
* *Risk/State:* None
* *Architecture:* `api: 29`, `import: 4`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` member-ordering, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/prefer-readonly.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.907)
- **Top Global Matches:** file_cluster_2: 4.907, file_cluster_17: 5.331, file_cluster_13: 5.926
- **Magnitude:** 1546.04 | **LOC:** 3493 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.2%), Concurrency Surface (formerly Concurrency) (12.4%), Connectivity (formerly Api Exposure) (4.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 401`, `args: 220`, `func_start: 200`, `class_start: 255`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 93`
* *Architecture:* `api: 132`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 24`, `test: 60`, `immutability_locks: 97`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` prefer-readonly, RuleTester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/explicit-module-boundary-types.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.376)
- **Top Global Matches:** file_cluster_10: 4.376, file_cluster_2: 5.26, file_cluster_17: 5.987
- **Magnitude:** 1495.97 | **LOC:** 2199 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.2%), Connectivity (formerly Api Exposure) (12.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (4.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 574`, `args: 306`, `func_start: 203`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 18`
* *Architecture:* `api: 178`, `import: 2`
* *Defense:* `safety: 7`, `doc: 1`, `test: 29`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` explicit-module-boundary-types, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/return-await.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.426)
- **Top Global Matches:** file_cluster_10: 6.426, file_cluster_2: 7.121, file_cluster_12: 7.142
- **Magnitude:** 1399.21 | **LOC:** 1676 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (39.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (5.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (5.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 371`, `args: 217`, `func_start: 205`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 15`
* *Architecture:* `io: 2`, `concurrency: 392`, `import: 4`
* *Defense:* `safety: 180`, `doc: 2`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` return-await, RuleTester, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/explicit-member-accessibility.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 4.43)
- **Top Global Matches:** file_cluster_13: 4.43, file_cluster_2: 5.108, file_cluster_17: 5.634
- **Magnitude:** 1286.6 | **LOC:** 2520 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (4.8%), Connectivity (formerly Api Exposure) (4.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 370`, `args: 185`, `func_start: 192`, `class_start: 163`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 62`
* *Architecture:* `api: 108`, `import: 2`
* *Defense:* `doc: 1`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` explicit-member-accessibility, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/explicit-function-return-type.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.084)
- **Top Global Matches:** file_cluster_10: 4.084, file_cluster_2: 5.406, file_cluster_17: 6.261
- **Magnitude:** 1266.75 | **LOC:** 2108 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.9%), Concurrency Surface (formerly Concurrency) (12.3%), Connectivity (formerly Api Exposure) (3.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 400`, `args: 282`, `func_start: 146`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 9`
* *Architecture:* `api: 9`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 13`, `doc: 1`, `test: 5`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` explicit-function-return-type, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/typescript-estree/tests/lib/getProjectConfigFiles.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.179)
- **Top Global Matches:** file_cluster_10: 5.179, file_cluster_12: 6.904, file_cluster_2: 7.418
- **Magnitude:** 1162.84 | **LOC:** 248 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (84.4%), Guard Balance (formerly Safety Score) (43.9%), Complexity Load (formerly Cognitive Load) (6.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 46`, `args: 24`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`
* *Architecture:* `io: 6`, `concurrency: 10`, `import: 11`
* *Defense:* `safety: 4`, `test: 27`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` parseSettings, ExpiringCache, getProjectConfigFiles, getProjectConfigFiles.js, node:fs, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/no-unnecessary-type-parameters.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.283)
- **Top Global Matches:** file_cluster_0: 6.283, file_cluster_5: 7.69, file_cluster_12: 8.279
- **Magnitude:** 1159.41 | **LOC:** 1907 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.5%), Concurrency Surface (formerly Concurrency) (18.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (5.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (5.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 638`, `args: 281`, `func_start: 203`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 4`
* *Architecture:* `api: 1`, `concurrency: 12`, `import: 7`
* *Defense:* `safety: 10`, `doc: 4`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` no-unnecessary-type-parameters, RuleTester, rule-tester, types, typescript
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/scope-manager/tests/eslint-scope/es6-default-parameters.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.113)
- **Top Global Matches:** file_cluster_10: 4.113, file_cluster_2: 6.094, file_cluster_13: 6.765
- **Magnitude:** 1042.08 | **LOC:** 396 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (2.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 30`, `args: 33`, `func_start: 24`
* *Risk/State:* None
* *Architecture:* `import: 2`
* *Defense:* `safety: 2`, `doc: 1`, `test: 72`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` index.js, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/promise-function-async.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.763)
- **Top Global Matches:** file_cluster_10: 5.763, file_cluster_2: 6.248, file_cluster_13: 6.507
- **Magnitude:** 840.9 | **LOC:** 1015 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (50.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.6%), Connectivity (formerly Api Exposure) (8.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 251`, `args: 142`, `func_start: 143`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 6`
* *Architecture:* `api: 30`, `concurrency: 189`, `import: 3`
* *Defense:* `safety: 5`, `doc: 1`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` promise-function-async, RuleTester, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/require-await.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.007)
- **Top Global Matches:** file_cluster_12: 6.007, file_cluster_10: 6.57, file_cluster_2: 6.638
- **Magnitude:** 803.6 | **LOC:** 1224 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (51.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (5.8%), Dead Code Surface (formerly Dead Code) (5.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 129`, `args: 100`, `func_start: 123`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 2`, `dead_code: 2`
* *Architecture:* `api: 2`, `concurrency: 166`, `import: 3`
* *Defense:* `safety: 2`, `doc: 1`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` require-await, RuleTester, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/unified-signatures.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.68)
- **Top Global Matches:** file_cluster_2: 4.68, file_cluster_13: 5.08, file_cluster_17: 5.572
- **Magnitude:** 799.91 | **LOC:** 1261 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.6%), Concurrency Surface (formerly Concurrency) (21.6%), Connectivity (formerly Api Exposure) (6.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 274`, `args: 197`, `func_start: 198`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 7`
* *Architecture:* `api: 19`, `concurrency: 11`, `import: 2`
* *Defense:* `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unified-signatures, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/await-thenable.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.107)
- **Top Global Matches:** file_cluster_12: 7.107, file_cluster_5: 7.342, file_cluster_0: 7.864
- **Magnitude:** 796.67 | **LOC:** 1445 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (50.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (5.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (5.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Concurrency (weighted view):* 318
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 306`, `args: 71`, `func_start: 67`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 2`
* *Architecture:* `io: 10`, `api: 4`, `concurrency: 298`, `import: 3`
* *Defense:* `safety: 25`, `doc: 1`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` await-thenable, RuleTester, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/src/rules/no-unused-vars.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.343)
- **Top Global Matches:** file_cluster_4: 6.343, file_cluster_6: 7.912, file_cluster_15: 13.29
- **Magnitude:** 783.52 | **LOC:** 1470 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **4**; blast radius 0.595; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (62.4%), Guard Balance (formerly Safety Score) (51.7%), Debt Markers (formerly Tech Debt) (50.8%), Connectivity (formerly Api Exposure) (29.2%)
- **Documentation Coverage:** 77.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create` **(Many-Argument Workhorses)** (Impact: 350.5)
  * `collectUnusedVariables` **(I/O & Config Routines)** (Impact: 62.4)
  * `report` **(Many-Argument Workhorses)** (Impact: 48.8)
  * `getImportFixer` **(Compute Cores)** (Impact: 31.1)
  * `markDeclarationChildAsUsed` **(Compute Cores)** (Impact: 29.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 202`, `structural_boundaries: 255`, `args: 50`, `func_start: 32`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 26`, `dead_code: 3`, `planned_debt: 18`, `fragile_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 21`, `doc: 12`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.595
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.002853
  * `Imports (Out-Degree: 5):` util, referenceContainsTypeQuery, scope-manager, utils
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin/tests/rules/no-explicit-any.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 4.742)
- **Top Global Matches:** file_cluster_7: 4.742, file_cluster_5: 6.445, file_cluster_12: 7.132
- **Magnitude:** 778.4 | **LOC:** 2087 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (63.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 443`, `args: 124`, `func_start: 103`, `class_start: 64`
* *Risk/State:* `safety_bypasses: 140`
* *Architecture:* `import: 2`
* *Defense:* `doc: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` no-explicit-any, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/prefer-readonly-parameter-types.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.694)
- **Top Global Matches:** file_cluster_0: 5.694, file_cluster_2: 5.828, file_cluster_17: 5.946
- **Magnitude:** 763.24 | **LOC:** 1325 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.7%), Connectivity (formerly Api Exposure) (1.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 184`, `args: 146`, `func_start: 133`, `class_start: 59`
* *Risk/State:* `safety_bypasses: 2`, `fragile_debt: 2`
* *Architecture:* `io: 7`, `api: 5`, `import: 5`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 81`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` prefer-readonly-parameter-types, util, RuleTester, rule-tester, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/website/src/components/config/ConfigEslint.tsx` (TYPESCRIPT) | Magnitude: 9.86 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 28, args: 10, ui_framework: 10
- `packages/eslint-plugin/src/util/index.ts` (TYPESCRIPT) | Magnitude: 51.92 | Delta: **0.218** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 40, api: 36, import: 34, indent_spaces: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `packages/scope-manager/tests/types/variable-definition.test.ts` (TYPESCRIPT) | Magnitude: 13.66 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 152, structural_boundaries: 20, args: 9, test: 9
- `packages/scope-manager/tests/fixtures/functions/function-expression/default-params/readable-ref-nested.ts` (TYPESCRIPT) | Magnitude: 0.0 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 3, func_start: 2, core_var_decl: 2, design_snake_case: 2
- `packages/typescript-eslint/tests/configs.test.ts` (TYPESCRIPT) | Magnitude: 48.48 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 301, structural_boundaries: 89, args: 61, closures: 43
- `packages/eslint-plugin/tests/util/isNodeEqual.test.ts` (TYPESCRIPT) | Magnitude: 10.64 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 9, args: 3, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/eslint-plugin/src/rules/no-unsafe-type-assertion.ts` (TYPESCRIPT) | Magnitude: 58.1 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 143, structural_boundaries: 52, branch: 13, core_var_decl: 10
- `packages/rule-tester/src/utils/validationHelpers.ts` (TYPESCRIPT) | Magnitude: 45.1 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 90, structural_boundaries: 29, args: 14, api: 10
- `packages/eslint-plugin/tests/rules/prefer-includes.test.ts` (TYPESCRIPT) | Magnitude: 347.88 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 492, structural_boundaries: 80, args: 79, func_start: 79
- `packages/eslint-plugin/tests/rules/no-confusing-void-expression.test.ts` (TYPESCRIPT) | Magnitude: 754.48 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 1014, structural_boundaries: 299, args: 182, debug_prints: 174
- `packages/type-utils/tests/discriminateAnyType.test.ts` (TYPESCRIPT) | Magnitude: 9.28 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 41, core_var_decl: 21, design_snake_case: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/scope-manager/vitest.config.mts` (TYPESCRIPT) | Magnitude: 16.4 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 9, import: 4, io: 3
- `packages/ast-spec/src/element/MethodDefinition/fixtures/_error_/duplicated-accessibility-modifiers/fixture.ts` (TYPESCRIPT) | Magnitude: 0.0 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, class_start: 1
- `packages/website/webpack.plugin.js` (JAVASCRIPT) | Magnitude: 7.24 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 33, import: 5, doc: 4, globals: 4
- `packages/integration-tests/fixtures/eslint-v9/eslint.config.mjs` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, import: 2, branch: 1
- `packages/eslint-plugin/src/util/getParentFunctionNode.ts` (TYPESCRIPT) | Magnitude: 12.74 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 9, branch: 4, doc: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/eslint-plugin/src/util/getForStatementHeadLoc.ts` (TYPESCRIPT) | Magnitude: 3.86 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 6, doc: 3, args: 2
- `packages/type-utils/src/discriminateAnyType.ts` (TYPESCRIPT) | Magnitude: 30.06 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 21, branch: 7, import: 3
- `packages/eslint-plugin/tests/fixtures/deprecated.ts` (TYPESCRIPT) | Magnitude: 0.03 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 20, doc: 13, indent_spaces: 11, args: 10
- `packages/eslint-plugin/src/util/rangeToLoc.ts` (TYPESCRIPT) | Magnitude: 3.4 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, args: 1, func_start: 1
- `packages/scope-manager/src/referencer/ExportVisitor.ts` (TYPESCRIPT) | Magnitude: 31.54 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 21, branch: 10, dead_code: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/ast-spec/src/legacy-fixtures/types/fixtures/mapped-readonly-minus/fixture.ts` (TYPESCRIPT) | Magnitude: 0.01 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 1, planned_debt: 1, immutability_locks: 1
- `packages/ast-spec/src/legacy-fixtures/types/fixtures/mapped-readonly-plus/fixture.ts` (TYPESCRIPT) | Magnitude: 0.01 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 1, planned_debt: 1, immutability_locks: 1
- `packages/ast-spec/src/legacy-fixtures/types/fixtures/mapped-readonly/fixture.ts` (TYPESCRIPT) | Magnitude: 0.01 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 1, planned_debt: 1, immutability_locks: 1
- `packages/scope-manager/src/lib/es2020.ts` (TYPESCRIPT) | Magnitude: 16.48 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 12, import: 10, api: 1
- `packages/ast-spec/src/index.ts` (TYPESCRIPT) | Magnitude: 64.98 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 50, api: 49, import: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/eslint-plugin/tests/rules/no-meaningless-void-operator.test.ts` (TYPESCRIPT) | Magnitude: 73.73 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 17, args: 10, func_start: 7
- `packages/website/plugins/blog-footer.ts` (TYPESCRIPT) | Magnitude: 10.28 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 17, import: 3, branch: 2
- `packages/ast-spec/src/unions/ClassElement.ts` (TYPESCRIPT) | Magnitude: 16.34 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 18, import: 8, indent_spaces: 8, api: 1
- `packages/scope-manager/src/lib/es2017.ts` (TYPESCRIPT) | Magnitude: 16.44 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 11, import: 9, api: 1
- `packages/scope-manager/src/lib/es2024.ts` (TYPESCRIPT) | Magnitude: 16.44 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 11, import: 9, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/eslint-plugin-internal/src/rules/prefer-tsutils-methods.ts` (TYPESCRIPT) | Magnitude: 116.86 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 33, branch: 30, core_var_decl: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/type-utils/tests/test-utils/custom-matchers/vitest-custom-matchers.d.ts` (TYPESCRIPT) | Magnitude: 1.68 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 19, branch: 12, args: 9
- `packages/type-utils/tests/builtinSymbolLikes.test.ts` (TYPESCRIPT) | Magnitude: 16.18 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 113, structural_boundaries: 94, test: 28, args: 21
- `packages/ast-spec/src/legacy-fixtures/basics/fixtures/class-with-mixin/fixture.ts` (TYPESCRIPT) | Magnitude: 0.0 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 11, generics: 4, class_start: 3, args: 2
- `packages/website/src/components/lib/parseConfig.ts` (TYPESCRIPT) | Magnitude: 39.98 | Delta: **0.157** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 28, branch: 12, generics: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/eslint-plugin/src/configs/flat/recommended.ts` (TYPESCRIPT) | Magnitude: 16.76 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 32, doc: 22, decorators: 21, structural_boundaries: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/eslint-plugin/src/rules/prefer-nullish-coalescing.ts` (TYPESCRIPT) | Magnitude: 552.62 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 771, branch: 167, structural_boundaries: 157, core_var_decl: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/rule-tester/src/utils/SourceCodeFixer.ts` (TYPESCRIPT) | Magnitude: 77.22 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 15, branch: 14, core_var_decl: 14
- `packages/eslint-plugin/src/rules/no-useless-empty-export.ts` (TYPESCRIPT) | Magnitude: 46.14 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 17, branch: 11, api: 5
- `packages/eslint-plugin/src/rules/no-array-constructor.ts` (TYPESCRIPT) | Magnitude: 46.32 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 14, branch: 11, core_var_decl: 5

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/eslint-plugin/tests/rules/no-floating-promises.test.ts` -> **Maria Solano** (100.0% isolated ownership) | Magnitude: 5549.62
- `packages/type-utils/tests/isTypeReadonly.test.ts` -> **Tamashoo** (100.0% isolated ownership) | Magnitude: 2510.7
- `packages/eslint-plugin/tests/rules/strict-boolean-expressions.test.ts` -> **Maria Solano** (100.0% isolated ownership) | Magnitude: 1858.48
- `packages/eslint-plugin/tests/rules/explicit-module-boundary-types.test.ts` -> **Dima Barabash** (100.0% isolated ownership) | Magnitude: 1495.97
- `packages/eslint-plugin/tests/rules/return-await.test.ts` -> **Maria Solano** (100.0% isolated ownership) | Magnitude: 1399.21

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/scope-manager/src/variable/ImplicitLibVariable.ts` -> **Severity: 0.034** (Bridge: 0.0004 * Flux: 97.3403%)
- `packages/scope-manager/src/analyze.ts` -> **Severity: 0.032** (Bridge: 0.0007 * Flux: 48.8237%)
- `packages/eslint-plugin/src/util/collectUnusedVariables.ts` -> **Severity: 0.019** (Bridge: 0.0002 * Flux: 100.0%)
- `packages/scope-manager/src/referencer/Referencer.ts` -> **Severity: 0.016** (Bridge: 0.0007 * Flux: 21.0998%)
- `packages/ast-spec/tests/util/serializers/Node.ts` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/eslint-plugin/src/util/getFunctionHeadLoc.ts` -> **Severity: 2.733** (Embedded: 0.0438 * Error Risk: 62.3363%)
- `packages/eslint-plugin/src/util/collectUnusedVariables.ts` -> **Severity: 2.693** (Embedded: 0.0478 * Error Risk: 56.3504%)
- `packages/eslint-plugin/src/util/misc.ts` -> **Severity: 2.447** (Embedded: 0.0486 * Error Risk: 50.3813%)
- `packages/eslint-plugin/src/util/getThisExpression.ts` -> **Severity: 2.445** (Embedded: 0.0436 * Error Risk: 56.1121%)
- `packages/eslint-plugin/src/util/needsPrecedingSemiColon.ts` -> **Severity: 2.302** (Embedded: 0.0432 * Error Risk: 53.3284%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/scope-manager/src/ID.ts` -> **Severity: 426.9** (Blast Radius: 4.269 * Doc Risk: 100.0%)
- `packages/eslint-plugin/src/util/astUtils.ts` -> **Severity: 382.444** (Blast Radius: 8.605 * Doc Risk: 44.4444%)
- `packages/scope-manager/src/ScopeManager.ts` -> **Severity: 322.583** (Blast Radius: 3.95 * Doc Risk: 81.6667%)
- `packages/website/plugins/utils/nodes.ts` -> **Severity: 310.7** (Blast Radius: 3.107 * Doc Risk: 100.0%)
- `packages/eslint-plugin/tests/rules/naming-convention/cases/createTestCases.ts` -> **Severity: 282.2** (Blast Radius: 2.822 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 537 literal sites + 4 sites through wrappers = 541

- `throwMissingLegacyESLintError` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `packages/utils/src/ts-eslint/eslint/LegacyESLint.ts`
- `diagnosticReporter` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/typescript-estree/src/create-program/getWatchProgramsForProjects.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 7823 call pairs -- scoped 32.4%, unique 0.0%, ambiguous 12.5%, external 55.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 7730 | 32.5% | 0.0% | 12.6% | 54.9% |
| javascript | 78 | 30.8% | 0.0% | 6.4% | 62.8% |
| html | 15 | 0.0% | 0.0% | 0.0% | 100.0% |

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
