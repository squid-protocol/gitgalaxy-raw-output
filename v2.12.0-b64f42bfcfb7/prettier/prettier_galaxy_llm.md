# ARCHITECTURAL_BRIEF: prettier
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/prettier/prettier.git` |
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
- **Scope:** 7062 analyzed artifact(s), 135333 LOC.
- **Load-bearing artifact:** `src/document/index.js` -- 113 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `website/data/users.yml` -- pulls in 81 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/language-js/parentheses/needs-parentheses.js` at magnitude 837.12 (structural weight, not risk).
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
| Total Artifacts | 9196 |
| Analyzed Artifacts (Scanned) | 7062 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2134 |
| Total LOC | 135333 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 76.8% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6517 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0119 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.7034 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 143 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 4821 | 108220 | 68.3% |
| TYPESCRIPT | 623 | 8840 | 8.8% |
| HTML | 417 | 6259 | 5.9% |
| MARKDOWN | 416 | 0 | 5.9% |
| CSS | 294 | 8389 | 4.2% |
| YAML | 291 | 2497 | 4.1% |
| JSON | 96 | 1069 | 1.4% |
| XML | 59 | 40 | 0.8% |
| PLAINTEXT | 44 | 0 | 0.6% |
| SHELL | 1 | 19 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 7048 |
| utf-8 | bom | 14 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 67%, Declarative / Non-Code 15%, Large Core Modules (2) 6%, State Mutators Files 3%, Parameter Forwarders Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 6562 | 92.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 460 | 6.5% |
| Static: Minified & Vendor Opaque Mass | 40 | 0.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2134*

**Composition by Extension & Reason:**
- `.snap`: 1430x Excluded (Unsupported Extension: '.snap'), 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.snap)
- `.js`: 165x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 31 LOC)
- `.yml`: 94x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.png`: 75x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 13x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.uppercase-rocks')
- `.graphql`: 68x Excluded (Unsupported Extension: '.graphql')
- `.ts`: 51x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2200 LOC), 1x Packed Payload Guard (Impossible Density: 3.43 hits/line)
- `.md`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 895 LOC)
- `.json`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.foo`: 9x Excluded (Unsupported Extension: '.foo'), 5x Unsupported Format (.foo)
- `.css`: 1x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Saturation: Line 85 exceeds 500 chars), 1x Zero-Density Threshold (LOC: 52, Signals: 0)
- `.mjs`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjml`: 9x Excluded (Unsupported Extension: '.mjml')
- `.scss`: 1x Zero-Density Threshold (LOC: 168, Signals: 0), 1x Zero-Density Threshold (LOC: 117, Signals: 0), 1x Zero-Density Threshold (LOC: 97, Signals: 0)
- `.lock`: 3x Excluded (Unsupported Extension: '.lock'), 2x Unsupported Format (.lock), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 89.5 | 12.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 0.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.0 | 0.9 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 51.6 | 2.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 23.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 96.7 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 259 | 116 | 0 | `tests/format/flow/flow-repo/core_tests/boolean.js` |
| cleanup | 16 | 12 | 0 | `scripts/benchmark/compare.sh` |
| guards | 7495 | 935 | 1 | `src/language-js/parentheses/needs-parentheses.js` |
| danger | 2609 | 702 | 0 | `tests/format/flow/flow-repo/type-printer/types.js` |
| concurrency | 2321 | 439 | 0 | `tests/integration/__tests__/cache.js` |
| connectivity | 3777 | 1537 | 1 | `tests/format/flow/flow-repo/type-printer/types.js` |
| io | 1106 | 236 | 0 | `tests/format/angular/angular/real-world.component.html` |
| crypto | 3 | 3 | 0 | `tests/config/install-prettier.js` |
| ipc | 41 | 17 | 0 | `tests/format/js/module-blocks/quote-props/worker.js` |
| time | 54 | 25 | 0 | `tests/format/flow/flow-repo/date/date.js` |
| serialization | 93 | 53 | 0 | `tests/unit/whitespace-utilities.js` |
| regex | 289 | 134 | 0 | `tests/integration/__tests__/cache.js` |
| events | 707 | 163 | 0 | `tests/format/vue/event-binding/assignment.vue` |
| tests | 1332 | 210 | 0 | `tests/integration/__tests__/public-utilities.js` |
| docs | 1741 | 672 | 0 | `tests/format/flow/flow-repo/logical/logical.js` |
| debt | 1071 | 401 | 0 | `tests/format/js/function/dangling-comments.js` |
| mutation | 17933 | 2755 | 6 | `website/playground/Playground.jsx` |
| dead_code | 1804 | 744 | 1 | `tests/format/flow/flow-repo/logical/logical.js` |
| credential | 7 | 7 | 0 | `tests/format/json/json/pass1.json` |
| threat | 16 | 5 | 0 | `tests/integration/__tests__/public-utilities.js` |
| ml_ai | 179 | 20 | 0 | `tests/format/css/parens/parens.css` |
| ui | 2502 | 338 | 0 | `tests/format/flow/flow-repo/type-printer/types.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/format/angular/angular/real-world.component.html` (Hits: 130)
- `tests/integration/__tests__/cache.js` (Hits: 55)
- `tests/integration/__tests__/patterns-dirs.js` (Hits: 40)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.js** (`src/document/index.js`) — 113 inbound connections
2. **group.js** (`src/document/builders/group.js`) — 70 inbound connections
3. **indent.js** (`src/document/builders/indent.js`) — 62 inbound connections
4. **node-types.js** (`src/language-js/utilities/node-types.js`) — 55 inbound connections
5. **comments.js** (`src/language-js/utilities/comments.js`) — 39 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **users.yml** (`website/data/users.yml`) — 81 outbound dependencies
2. **estree.js** (`src/language-js/print/estree.js`) — 39 outbound dependencies
3. **flow.js** (`src/language-js/print/flow.js`) — 38 outbound dependencies
4. **typescript.js** (`src/language-js/print/typescript.js`) — 34 outbound dependencies
5. **production-plugins.js** (`src/main/plugins/builtin-plugins/production-plugins.js`) — 28 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `needsParentheses` **(Defensive Guards)** (@ `src/language-js/parentheses/needs-parentheses.js`) -> Impact: **768.1** | LOC: 848
  * *Intent:* /** */ /** */
- `genericPrint` **(Many-Argument Workhorses)** (@ `src/language-css/printer-postcss.js`) -> Impact: **410.4** | LOC: 529
- `printCommaSeparatedValueGroup` **(Many-Argument Workhorses)** (@ `src/language-css/print/comma-separated-value-group.js`) -> Impact: **406.6** | LOC: 493
  * *Intent:* /** */ /** */
- `printFlow` **(Many-Argument Workhorses)** (@ `src/language-js/print/flow.js`) -> Impact: **317.6** | LOC: 315
- `printEstree` **(Many-Argument Workhorses)** (@ `src/language-js/print/estree.js`) -> Impact: **274.5** | LOC: 258
  * *Intent:* /** */ /** */
- `print` **(Many-Argument Workhorses)** (@ `src/language-handlebars/printer-glimmer.js`) -> Impact: **231.2** | LOC: 385
  * *Intent:* // https://github.com/glimmerjs/glimmer-vm/blob/master/packages/%40glimmer/syntax/lib/generation/print.ts
- `printMdast` **(Many-Argument Workhorses)** (@ `src/language-markdown/print/mdast.js`) -> Impact: **224.8** | LOC: 336
- `printTernary` **(Many-Argument Workhorses)** (@ `src/language-js/print/ternary.js`) -> Impact: **210.6** | LOC: 276
  * *Intent:* /** * The following is the shared logic for * ternary operators, namely ConditionalExpression, * ConditionalTypeAnnotation and TSConditionalType */
- `tokenizeHtmlText` **(Many-Argument Workhorses)** (@ `src/language-markdown/parse/micromark/micromark-extension-html-text.js`) -> Impact: **204.1** | LOC: 762
  * *Intent:* /** * Context. */
- `genericPrint` **(Many-Argument Workhorses)** (@ `src/language-graphql/printer-graphql.js`) -> Impact: **194.7** | LOC: 413

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/language-js/print` | 73 | 6767.96 | 20.51% | 1.17% |
| `tests/integration/__tests__` | 75 | 3553.18 | 6.29% | 0.0% |
| `src/language-markdown/print` | 12 | 1489.14 | 16.8% | 5.93% |
| `src/main` | 17 | 1476.48 | 44.38% | 2.18% |
| `tests/format/yaml/spec` | 99 | 1265.98 | 0.05% | 0.0% |
| `src/language-css` | 10 | 1106.32 | 19.89% | 2.48% |
| `src/language-js/parentheses` | 4 | 1079.58 | 26.62% | 4.53% |
| `src/language-js/utilities` | 61 | 1078.62 | 8.49% | 4.7% |
| `website/playground` | 17 | 1005.82 | 15.9% | 3.09% |
| `src/cli` | 17 | 1005.44 | 27.21% | 0.5% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `website/playground/sidebar/options.jsx` -> **99.9955%** Exposure
- `src/document/public.d.ts` -> **99.9818%** Exposure
- `website/playground/sidebar/inputs.jsx` -> **99.9768%** Exposure
- `src/standalone.d.ts` -> **99.593%** Exposure
- `src/index.d.ts` -> **99.5461%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `benchmarks/string-buffer-compress.js` -> **100.0%** Exposure
- `src/cli/index.js` -> **100.0%** Exposure
- `src/common/ast-path.js` -> **100.0%** Exposure
- `src/common/get-file-info.js` -> **100.0%** Exposure
- `src/config/editorconfig/editorconfig-to-prettier.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/format/flow/flow-repo/logical/logical.js` -> **65** Orphaned Functions | **0** Duplicates
- `src/index.d.ts` -> **44** Orphaned Functions | **2** Duplicates
- `tests/format/js/function/dangling-comments.js` -> **1** Orphaned Functions | **39** Duplicates
- `tests/format/flow/flow-repo/binding/rebinding.js` -> **33** Orphaned Functions | **4** Duplicates
- `tests/format/flow/flow-repo/dictionary/dictionary.js` -> **31** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `website/docusaurus.config.js` -> **96.6735%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1185` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/language-js/parentheses/needs-parentheses.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.902)
- **Top Global Matches:** file_cluster_3: 7.902, file_cluster_8: 20.947, file_cluster_6: 33.656
- **Magnitude:** 837.12 | **LOC:** 1000 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 85.7%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **13**; blast radius 0.241; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (46.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.6%), Guard Balance (formerly Safety Score) (24.4%), Mutation Surface (formerly State Flux) (17.8%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `needsParentheses` **(Defensive Guards)** (Impact: 768.1)
    * *Intent:* /** */ /** */
  * `isFollowedByRightBracket` **(Defensive Guards)** (Impact: 24.2)
    * *Intent:* /** */
  * `isPathInForStatementInitializer` **(Defensive Guards)** (Impact: 7.7)
    * *Intent:* /** */
  * `endsWithRightBracket` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 438`, `structural_boundaries: 166`, `args: 22`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `safety: 249`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.002546
  * `Imports (Out-Degree: 14):` comments.js, create-type-check-function.js, function-parameters.js, get-precedence.js, is-bitwise-operator.js, is-nullish-coalescing.js, is-object-property.js, node-types.js...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `tests/integration/__tests__/cache.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.117)
- **Top Global Matches:** file_cluster_10: 6.117, file_cluster_15: 8.005, file_cluster_2: 8.48
- **Magnitude:** 674.8 | **LOC:** 708 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.119; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (84.3%), Guard Balance (formerly Safety Score) (52.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runCliWithoutGitignore` **(Parameter Forwarders)** (Impact: 2.1)
  * `resolveDir` **(Parameter Forwarders)** (Impact: 1.6)
  * `clean` **(Callbacks & Closures)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 86 instances
* *Concurrency (weighted view):* 542
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 123`, `args: 40`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 115`
* *Architecture:* `io: 55`, `concurrency: 112`, `import: 3`
* *Defense:* `test: 83`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises, node:path, node:url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/format/flow/flow-repo/type_param_variance2/libs/Promise.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 7.405)
- **Top Global Matches:** file_cluster_14: 7.405, file_cluster_7: 8.547, file_cluster_5: 12.219
- **Magnitude:** 663.6 | **LOC:** 48 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (5.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 10`, `args: 8`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 7`
* *Architecture:* `concurrency: 18`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-js/print/jsx.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.11)
- **Top Global Matches:** file_cluster_8: 7.11, file_cluster_6: 10.537, file_cluster_4: 18.918
- **Magnitude:** 644.46 | **LOC:** 856 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.126; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Guard Balance (formerly Safety Score) (43.8%), Complexity Load (formerly Cognitive Load) (37.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.2%)
- **Documentation Coverage:** 88.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printJsxElementInternal` **(Many-Argument Workhorses)** (Impact: 161.7)
    * *Intent:* // This is both to break children before attributes, // and to ensure that when children break, thei...
  * `printJsxChildren` **(Many-Argument Workhorses)** (Impact: 65.1)
    * *Intent:* // JSX Children are strange, mostly for two reasons: // 1. JSX reads newlines into string values, in...
  * `printJsx` **(Compute Cores)** (Impact: 40.1)
  * `printJsxExpressionContainer` **(Defensive Guards)** (Impact: 35.6)
  * `printJsxOpeningElement` **(Many-Argument Workhorses)** (Impact: 35.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 91`, `args: 36`, `func_start: 23`
* *Risk/State:* `state_mutation: 39`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `import: 12`
* *Defense:* `safety: 97`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.126
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.001073
  * `Imports (Out-Degree: 19):` index.js, print.js, get-preferred-quote.js, unexpected-node-error.js, needs-parentheses.js, comments.js, create-type-check-function.js, get-raw.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/format/typescript/_errors_/modifiers/format.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.683)
- **Top Global Matches:** file_cluster_2: 4.683, file_cluster_17: 5.451, file_cluster_13: 6.113
- **Magnitude:** 578.2 | **LOC:** 157 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.119; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (27.4%), Complexity Load (formerly Cognitive Load) (8.3%), Connectivity (formerly Api Exposure) (6.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (5.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 38`, `args: 20`, `func_start: 1`, `class_start: 4`
* *Risk/State:* None
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` outdent
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-handlebars/printer-glimmer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.523)
- **Top Global Matches:** file_cluster_15: 6.523, file_cluster_4: 8.375, file_cluster_16: 8.675
- **Magnitude:** 535.96 | **LOC:** 858 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.195; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (58.2%), Guard Balance (formerly Safety Score) (46.6%)
- **Documentation Coverage:** 94.8718% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `print` **(Many-Argument Workhorses)** (Impact: 231.2)
    * *Intent:* // https://github.com/glimmerjs/glimmer-vm/blob/master/packages/%40glimmer/syntax/lib/generation/pri...
  * `isElseIfBlock` **(Defensive Guards)** (Impact: 13.1)
  * `isPathExpressionPartNeedBrackets` **(Defensive Guards)** (Impact: 12.8)
  * `printParams` **(Defensive Guards)** (Impact: 9.6)
  * `printInverse` **(Defensive Guards)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 120`, `args: 51`, `func_start: 36`
* *Risk/State:* `state_mutation: 39`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 79`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.195
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.001255
  * `Imports (Out-Degree: 17):` index.js, get-preferred-quote.js, html-whitespace.js, is-non-empty-array.js, unexpected-node-error.js, embed.js, get-visitor-keys.js, loc.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/language-css/print/comma-separated-value-group.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.999)
- **Top Global Matches:** file_cluster_3: 6.999, file_cluster_8: 21.152, file_cluster_6: 34.027
- **Magnitude:** 523.92 | **LOC:** 568 | **CtrlFlow:** 48.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.126; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.1%), Guard Balance (formerly Safety Score) (41.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printCommaSeparatedValueGroup` **(Many-Argument Workhorses)** (Impact: 406.6)
    * *Intent:* /** */ /** */
  * `isPossibleFontSize` **(Defensive Guards)** (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 59`, `args: 5`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 84`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.126
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001084
  * `Imports (Out-Degree: 8):` index.js, loc.js, index.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/language-js/comments/handle-comments.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.833)
- **Top Global Matches:** file_cluster_4: 6.833, file_cluster_9: 10.882, file_cluster_6: 11.062
- **Magnitude:** 500.6 | **LOC:** 1088 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 89.5%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **22**; blast radius 0.136; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.6%), Guard Balance (formerly Safety Score) (35.4%), Mutation Surface (formerly State Flux) (26.3%), Complexity Load (formerly Cognitive Load) (15.8%)
- **Documentation Coverage:** 78.3784% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleLastFunctionParameterComments` **(Defensive Guards)** (Impact: 67.5)
  * `handleClassComments` **(Defensive Guards)** (Impact: 32.4)
  * `handleMethodNameComments` **(Defensive Guards)** (Impact: 29.7)
  * `handleCommentInEmptyParens` **(Defensive Guards)** (Impact: 23.2)
  * `handleModuleSpecifiersComments` **(Defensive Guards)** (Impact: 21.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 252`, `structural_boundaries: 118`, `args: 39`, `func_start: 36`
* *Risk/State:* `state_mutation: 10`, `dead_code: 2`
* *Architecture:* `api: 1`, `import: 22`
* *Defense:* `safety: 149`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.136
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.001223
  * `Imports (Out-Degree: 24):` utilities.js, get-next-non-space-non-comment-character-index.js, get-next-non-space-non-comment-character.js, has-newline-in-range.js, has-newline.js, is-non-empty-array.js, index.js, call-arguments.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/language-html/utilities/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.65)
- **Top Global Matches:** file_cluster_4: 6.65, file_cluster_6: 10.357, file_cluster_15: 11.239
- **Magnitude:** 461.48 | **LOC:** 655 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **6**; blast radius 0.895; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (35.4%), Connectivity (formerly Api Exposure) (18.9%), Complexity Load (formerly Cognitive Load) (18.6%), Mutation Surface (formerly State Flux) (18.2%)
- **Documentation Coverage:** 92.3077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isLeadingSpaceSensitiveNode` **(Defensive Guards)** (Impact: 46.1)
  * `isTrailingSpaceSensitiveNode` **(Defensive Guards)** (Impact: 36.7)
  * `getNodeCssStyleDisplay` **(Defensive Guards)** (Impact: 34.9)
  * `shouldPreserveContent` **(Defensive Guards)** (Impact: 24.4)
  * `inferParserByTypeAttribute` **(Compute Cores)** (Impact: 24.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 110`, `args: 56`, `func_start: 52`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `safety: 89`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.895
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.002134
  * `Imports (Out-Degree: 9):` index.js, index.js, html-whitespace.js, infer-parser.js, constants.evaluate.js, is-unknown-namespace.js
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/language-css/printer-postcss.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 4.654)
- **Top Global Matches:** file_cluster_1: 4.654, file_cluster_3: 48.158, file_cluster_8: 70.029
- **Magnitude:** 434.02 | **LOC:** 603 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 0.176; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (41.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.9%), Complexity Load (formerly Cognitive Load) (20.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `genericPrint` **(Many-Argument Workhorses)** (Impact: 410.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 76`, `args: 6`, `func_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 1`, `import: 14`
* *Defense:* `safety: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.001255
  * `Imports (Out-Degree: 21):` index.js, is-non-empty-array.js, print-string.js, unexpected-node-error.js, embed.js, get-visitor-keys.js, loc.js, index.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/language-markdown/parse/micromark/micromark-extension-html-text.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.692)
- **Top Global Matches:** file_cluster_15: 6.692, file_cluster_4: 7.887, file_cluster_16: 8.378
- **Magnitude:** 432.08 | **LOC:** 813 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.16; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (84.8%), Guard Balance (formerly Safety Score) (39.6%), Connectivity (formerly Api Exposure) (11.8%), Complexity Load (formerly Cognitive Load) (10.6%)
- **Documentation Coverage:** 6.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tokenizeHtmlText` **(Many-Argument Workhorses)** (Impact: 204.1)
    * *Intent:* /** * Context. */
  * `tagOpenAttributeValueBefore` **(Defensive Guards)** (Impact: 15.6)
    * *Intent:* /** * Before unquoted, double quoted, or single quoted attribute value, allowing * whitespace. * * `...
  * `tagOpenAttributeValueUnquoted` **(Defensive Guards)** (Impact: 15.3)
    * *Intent:* /** * In unquoted attribute value. * * ```markdown * > | a <b c=d> e * ^ * ``` * */
  * `tagOpenBetween` **(Defensive Guards)** (Impact: 11.1)
    * *Intent:* /** * In opening tag, after tag name. * * ```markdown * > | a <b> c * ^ * ``` * */
  * `tagOpen` **(Defensive Guards)** (Impact: 9.3)
    * *Intent:* /** * After `<x`, in opening tag name. * * ```markdown * > | a <b> c * ^ * ``` * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 90`, `args: 32`, `func_start: 32`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 58`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.16
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000848
  * `Imports (Out-Degree: 0):` micromark-factory-space, micromark-util-character, micromark-util-symbol
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/document/printer/printer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 15.652)
- **Top Global Matches:** file_cluster_3: 15.652, file_cluster_1: 33.374, file_cluster_8: 37.022
- **Magnitude:** 422.6 | **LOC:** 578 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 85.7%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **8**; blast radius 1.195; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.8%), Complexity Load (formerly Cognitive Load) (41.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printDocToString` **(Many-Argument Workhorses)** (Impact: 139.4)
    * *Intent:* */
  * `fits` **(Many-Argument Workhorses)** (Impact: 103.7)
    * *Intent:* /** */
  * `printGroup` **(I/O & Config Routines)** (Impact: 13.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 156
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 65`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 52`, `fragile_debt: 2`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 20`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.195
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.012211
  * `Imports (Out-Degree: 9):` end-of-line.js, get-string-width.js, index.js, index.js, invalid-doc-error.js, indent.js, print-result.js, trim-indentation.js
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/language-markdown/print/preprocess.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.291)
- **Top Global Matches:** file_cluster_4: 7.291, file_cluster_6: 10.281, file_cluster_9: 11.62
- **Magnitude:** 411.62 | **LOC:** 603 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.14; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (49.1%), Guard Balance (formerly Safety Score) (49.0%), Complexity Load (formerly Cognitive Load) (39.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `splitTextIntoSentences` **(Defensive Guards)** (Impact: 39.0)
  * `markAlignedList` **(Defensive Guards)** (Impact: 35.2)
  * `markAlignedListLegacy` **(Defensive Guards)** (Impact: 27.9)
  * `getBracketContent` **(Defensive Guards)** (Impact: 19.6)
  * `preprocess` **(Defensive Guards)** (Impact: 18.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 90`, `args: 37`, `func_start: 21`
* *Risk/State:* `state_mutation: 40`, `duplicate_logic: 4`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 63`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001052
  * `Imports (Out-Degree: 2):` html-whitespace.js, utilities.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cli/format.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.805)
- **Top Global Matches:** file_cluster_8: 6.805, file_cluster_6: 17.197, file_cluster_3: 20.112
- **Magnitude:** 395.4 | **LOC:** 507 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.128; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.6%), Complexity Load (formerly Cognitive Load) (89.0%), Guard Balance (formerly Safety Score) (51.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formatFiles` **(Compute Cores)** (Impact: 100.7)
  * `handleError` **(Many-Argument Workhorses)** (Impact: 44.0)
  * `format` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `formatStdin` **(Defensive Guards)** (Impact: 12.2)
  * `listDifferent` **(Defensive Guards)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 83
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 76`, `args: 10`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 3`, `state_mutation: 29`, `planned_debt: 1`
* *Architecture:* `io: 5`, `api: 1`, `concurrency: 33`, `import: 12`
* *Defense:* `safety: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000141
  * `Imports (Out-Degree: 10):` index.js, expand-patterns.js, find-cache-file.js, format-results-cache.js, mockable.js, get-options-for-file.js, prettier-internal.js, utilities.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/language-markdown/print/mdast.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.662)
- **Top Global Matches:** file_cluster_4: 6.662, file_cluster_6: 10.173, file_cluster_9: 11.439
- **Magnitude:** 387.82 | **LOC:** 560 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **17**; blast radius 0.179; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (84.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (42.8%), Complexity Load (formerly Cognitive Load) (37.5%)
- **Documentation Coverage:** 81.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printMdast` **(Many-Argument Workhorses)** (Impact: 224.8)
  * `printRoot` **(Many-Argument Workhorses)** (Impact: 29.1)
  * `prevOrNextWord` **(Defensive Guards)** (Impact: 14.7)
    * *Intent:* /** */
  * `printTitle` **(Defensive Guards)** (Impact: 12.3)
  * `processor` **(Defensive Guards)** (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 103`, `args: 21`, `func_start: 14`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 2`, `import: 17`
* *Defense:* `safety: 61`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.000936
  * `Imports (Out-Degree: 21):` index.js, get-max-continuous-count.js, get-min-not-present-continuous-count.js, get-preferred-quote.js, unexpected-node-error.js, loc.js, utilities.js, children.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/core.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.93)
- **Top Global Matches:** file_cluster_6: 6.93, file_cluster_4: 8.454, file_cluster_15: 15.188
- **Magnitude:** 382.64 | **LOC:** 432 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 0.293; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `coreFormat` **(Many-Argument Workhorses)** (Impact: 59.8)
  * `formatWithCursor` **(Compute Cores)** (Impact: 29.9)
  * `formatRange` **(Many-Argument Workhorses)** (Impact: 20.5)
  * `ensureIndexInText` **(Defensive Guards)** (Impact: 10.6)
  * `normalizeInputAndOptions` **(Many-Argument Workhorses)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 37 instances
* *Concurrency (weighted view):* 96
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 66`, `args: 14`, `func_start: 14`
* *Risk/State:* `state_mutation: 45`, `planned_debt: 1`
* *Architecture:* `api: 1`, `concurrency: 31`, `import: 12`
* *Defense:* `safety: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.293
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.002301
  * `Imports (Out-Degree: 13):` end-of-line.js, constants.js, index.js, get-alignment-size.js, ast-to-doc.js, get-cursor-node.js, massage-ast.js, normalize-format-options.js...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/language-js/print/flow.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.286)
- **Top Global Matches:** file_cluster_1: 6.286, file_cluster_3: 48.346, file_cluster_8: 70.158
- **Magnitude:** 332.38 | **LOC:** 378 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **38**; blast radius 0.126; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (47.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.4%), Connectivity (formerly Api Exposure) (22.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printFlow` **(Many-Argument Workhorses)** (Impact: 317.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 108`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 2`
* *Architecture:* `api: 2`, `import: 38`
* *Defense:* `safety: 11`, `doc: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.126
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.001073
  * `Imports (Out-Degree: 39):` assert, index.js, print-number.js, print-string.js, get-raw.js, is-flow-keyword-type.js, is-method.js, array-type.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `website/static/worker.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.977)
- **Top Global Matches:** file_cluster_4: 7.977, file_cluster_11: 9.803, file_cluster_10: 9.887
- **Magnitude:** 329.76 | **LOC:** 337 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.5%), Guard Balance (formerly Safety Score) (53.6%)
- **Documentation Coverage:** 84.2105% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleFormatMessage` **(Defensive Guards)** (Impact: 29.0)
    * *Intent:* /** */
  * `formatCode` **(Defensive Guards)** (Impact: 9.4)
    * *Intent:* /** */
  * `stringifyError` **(Defensive Guards)** (Impact: 8.1)
  * `createPlugin` **(Callbacks & Closures)** (Impact: 6.8)
    * *Intent:* // Similar to `createParsersAndPrinters` in `src/plugins/builtin-plugins-proxy.js`
  * `serializeAst` **(Defensive Guards)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 25 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 163
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 66`, `args: 19`, `func_start: 15`
* *Risk/State:* `state_mutation: 27`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 38`, `import: 4`
* *Defense:* `safety: 26`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` prettier-plugin-doc-explorer.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-js/print/assignment.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.179)
- **Top Global Matches:** file_cluster_4: 7.179, file_cluster_6: 9.329, file_cluster_9: 12.847
- **Magnitude:** 329.44 | **LOC:** 469 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **11**; blast radius 0.241; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (44.3%), Guard Balance (formerly Safety Score) (42.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.8%)
- **Documentation Coverage:** 79.1667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `chooseLayout` **(Many-Argument Workhorses)** (Impact: 77.9)
  * `shouldBreakAfterOperator` **(Many-Argument Workhorses)** (Impact: 61.5)
  * `printAssignment` **(Many-Argument Workhorses)** (Impact: 31.8)
    * *Intent:* /** */
  * `isPoorlyBreakableMemberOrCallChain` **(Defensive Guards)** (Impact: 28.9)
    * *Intent:* /** * A chain with no calls at all or whose calls are all without arguments or with lone short argum...
  * `isCallExpressionWithComplexTypeArguments` **(Defensive Guards)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 91`, `args: 25`, `func_start: 19`
* *Risk/State:* `state_mutation: 7`, `planned_debt: 2`
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 42`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.001335
  * `Imports (Out-Degree: 16):` index.js, get-string-width.js, is-non-empty-array.js, call-arguments.js, has-leading-own-line-comment.js, is-lone-short-argument.js, is-object-property.js, node-types.js...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/language-css/parser-postcss.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 4.221)
- **Top Global Matches:** file_cluster_1: 4.221, file_cluster_3: 48.101, file_cluster_8: 69.976
- **Magnitude:** 328.9 | **LOC:** 453 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 0.176; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (70.2%), Guard Balance (formerly Safety Score) (59.3%), Connectivity (formerly Api Exposure) (30.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseNestedCSS` **(Many-Argument Workhorses)** (Impact: 166.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 62`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 55`, `planned_debt: 2`
* *Architecture:* `api: 4`, `import: 15`
* *Defense:* `safety: 45`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.001255
  * `Imports (Out-Degree: 13):` parser-create-error.js, index.js, is-object.js, replace-non-line-breaks-with-space.js, loc.js, parse-media-query.js, parse-selector.js, parse-value.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/language-html/print-preprocess.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.811)
- **Top Global Matches:** file_cluster_6: 7.811, file_cluster_4: 10.092, file_cluster_9: 15.492
- **Magnitude:** 321.1 | **LOC:** 411 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.126; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (56.4%), Guard Balance (formerly Safety Score) (54.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.9%)
- **Documentation Coverage:** 78.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extractWhitespaces` **(Many-Argument Workhorses)** (Impact: 36.6)
    * *Intent:* /** * - add `hasLeadingSpaces` field * - add `hasTrailingSpaces` field * - add `hasDanglingSpaces` f...
  * `mergeSimpleElementIntoText` **(Defensive Guards)** (Impact: 27.7)
  * `isSimpleElement` **(Defensive Guards)** (Impact: 21.9)
  * `extractInterpolation` **(Defensive Guards)** (Impact: 20.4)
  * `mergeNodeIntoText` **(Defensive Guards)** (Impact: 17.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 42`, `args: 26`, `func_start: 14`
* *Risk/State:* `state_mutation: 44`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 39`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.126
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001052
  * `Imports (Out-Degree: 2):` html-whitespace.js, index.js, angular-html-parser
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/document/utilities/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.372)
- **Top Global Matches:** file_cluster_6: 6.372, file_cluster_4: 11.068, file_cluster_8: 14.644
- **Magnitude:** 315.08 | **LOC:** 426 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **35** in-repo importer(s); it depends on **6**; blast radius 2.355; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.7%), Complexity Load (formerly Cognitive Load) (33.9%)
- **Documentation Coverage:** 86.9565% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cleanDocFn` **(Defensive Guards)** (Impact: 57.7)
  * `mapDoc` **(Compute Cores)** (Impact: 41.7)
    * *Intent:* /** */
  * `process` **(Compute Cores)** (Impact: 30.6)
  * `stripTrailingHardlineFromDoc` **(Compute Cores)** (Impact: 27.6)
  * `isEmptyDoc` **(Defensive Guards)** (Impact: 12.3)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 76`, `args: 27`, `func_start: 23`
* *Risk/State:* `state_mutation: 17`, `fragile_debt: 1`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `safety: 30`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.355
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.014614
  * `Imports (Out-Degree: 6):` index.js, assert-doc.js, get-doc-type.js, invalid-doc-error.js, traverse-doc.js, trim-newlines
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `src/language-js/print/member-chain.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.756)
- **Top Global Matches:** file_cluster_6: 8.756, file_cluster_8: 11.022, file_cluster_4: 15.733
- **Magnitude:** 308.12 | **LOC:** 420 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.127; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.8%), Guard Balance (formerly Safety Score) (56.7%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printMemberChain` **(Many-Argument Workhorses)** (Impact: 176.2)
    * *Intent:* */
  * `rec` **(I/O & Config Routines)** (Impact: 19.9)
  * `shouldNotWrap` **(Defensive Guards)** (Impact: 16.6)
  * `shouldInsertEmptyLineAfter` **(Defensive Guards)** (Impact: 5.2)
    * *Intent:* // Here we try to retain one typed empty line after each call expression or // the first group wheth...
  * `lastGroupWillBreakAndOtherCallsHaveFunctionArguments` **(Interface Declarations)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 45`, `args: 17`, `func_start: 9`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `api: 1`, `import: 16`
* *Defense:* `safety: 15`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.001199
  * `Imports (Out-Degree: 23):` index.js, print.js, get-next-non-space-non-comment-character-index.js, is-next-line-empty.js, index.js, needs-parentheses.js, comments.js, is-long-curried-call-expression.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/language-js/print/binaryish.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.384)
- **Top Global Matches:** file_cluster_8: 11.384, file_cluster_3: 13.594, file_cluster_6: 23.773
- **Magnitude:** 294.54 | **LOC:** 397 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 92.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.4%), Complexity Load (formerly Cognitive Load) (39.4%), Guard Balance (formerly Safety Score) (36.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (32.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printBinaryishExpression` **(Defensive Guards)** (Impact: 117.2)
    * *Intent:* */
  * `printBinaryishExpressions` **(Many-Argument Workhorses)** (Impact: 108.7)
    * *Intent:* // For binary expressions to be consistent, we need to group // subsequent operators with the same p...
  * `shouldInlineLogicalExpression` **(Defensive Guards)** (Impact: 10.8)
  * `isVueFilterSequenceExpression` **(Defensive Guards)** (Impact: 9.2)
  * `isBitwiseOrExpression` **(Defensive Guards)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 39`, `args: 10`, `func_start: 5`
* *Risk/State:* `state_mutation: 13`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 61`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.001382
  * `Imports (Out-Degree: 16):` index.js, print.js, comments.js, has-leading-own-line-comment.js, is-boolean-type-coercion.js, is-object-property.js, is-type-cast-comment.js, node-types.js...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/language-js/print/estree.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.854)
- **Top Global Matches:** file_cluster_1: 6.854, file_cluster_3: 48.419, file_cluster_8: 70.205
- **Magnitude:** 293.52 | **LOC:** 345 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **39**; blast radius 0.126; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.6%), Complexity Load (formerly Cognitive Load) (23.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printEstree` **(Many-Argument Workhorses)** (Impact: 274.5)
    * *Intent:* /** */ /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 120`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 1`, `concurrency: 3`, `import: 39`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.126
  * `Choke Point (Betweenness):` 3.7e-05 | `Ripple Effect (Closeness):` 0.001073
  * `Imports (Out-Degree: 42):` index.js, print.js, unexpected-node-error.js, comments.js, is-meaningful-empty-statement.js, is-method.js, node-types.js, array.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/format/typescript/union/comments/18106.ts` (TYPESCRIPT) | Magnitude: 17.72 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 9, core_var_decl: 3, design_upper_case: 3
- `tests/format/typescript/optional-variance/basic.ts` (TYPESCRIPT) | Magnitude: 16.0 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 31, indent_spaces: 18, generics: 13, args: 5
- `tests/format/typescript/optional-variance/with-jsx.tsx` (TYPESCRIPT) | Magnitude: 16.0 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 31, indent_spaces: 18, generics: 13, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/format/js/arrows/curried.js` (JAVASCRIPT) | Magnitude: 34.46 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 203, args: 196, indent_spaces: 148, core_var_decl: 23
- `website/playground/version-link.vue` (HTML) | Magnitude: 3.1 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 31, core_var_decl: 9, design_snake_case: 8, args: 6
- `tests/format/flow/flow-repo/arith/Arith.js` (JAVASCRIPT) | Magnitude: 30.88 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 35, args: 12, func_start: 9, branch: 8
- `tests/format/js/method-chain/comment.js` (JAVASCRIPT) | Magnitude: 13.02 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 6, args: 5, closures: 4
- `tests/integration/__tests__/plugin-default-options.js` (JAVASCRIPT) | Magnitude: 21.8 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 36, state_mutation: 6, structural_boundaries: 2, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/format/js/preserve-line/argument-list.js` (JAVASCRIPT) | Magnitude: 10.5 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 7, args: 7, func_start: 4
- `tests/config/prettier-plugins/prettier-plugin-async-printer/index.cjs` (JAVASCRIPT) | Magnitude: 31.8 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 36, api: 7, args: 6, func_start: 6
- `tests/format/flow/flow-repo/async/async_base_class.js` (JAVASCRIPT) | Magnitude: 5.36 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 6, concurrency: 4, indent_spaces: 3, args: 2
- `scripts/draft-blog-post.js` (JAVASCRIPT) | Magnitude: 28.36 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 58, core_var_decl: 16, structural_boundaries: 13, io: 13
- `tests/format/jsx/fragment/fragment.js` (JAVASCRIPT) | Magnitude: 8.96 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 26, ui_framework: 6, core_var_decl: 5, design_snake_case: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/format/js/method-chain/break-last-call.js` (JAVASCRIPT) | Magnitude: 17.68 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 6, args: 4, core_var_decl: 3
- `tests/format/css/attribute/spaces.css` (CSS) | Magnitude: 0.87 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: core_var_decl: 10, design_snake_case: 10, branch: 8, reflection_metaprogramming: 8
- `tests/integration/__tests__/plugin-options-string.js` (JAVASCRIPT) | Magnitude: 52.36 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 57, state_mutation: 18, structural_boundaries: 8, test: 6
- `tests/format/flow/interface-types/break/break.js` (JAVASCRIPT) | Magnitude: 8.64 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 31, class_start: 6, api: 5
- `src/document/public.d.ts` (TYPESCRIPT) | Magnitude: 3.53 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 156, structural_boundaries: 56, doc: 28, args: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/format/html/multiparser/css/html-with-css-style.html` (HTML) | Magnitude: 0.02 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 3, func_start: 1, decorators: 1
- `tests/format/html/multiparser/js/html-with-js-script.html` (HTML) | Magnitude: 0.02 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 3, core_var_decl: 2, design_snake_case: 2
- `tests/format/typescript/as/export_default_as.ts` (TYPESCRIPT) | Magnitude: 2.12 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 1, structural_boundaries: 1, args: 1, func_start: 1
- `tests/format/typescript/export-default/function_as.ts` (TYPESCRIPT) | Magnitude: 2.12 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 1, structural_boundaries: 1, args: 1, func_start: 1
- `tests/format/typescript/conformance/types/ambient/ambientDeclarations.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 18, class_start: 3, core_var_decl: 2, design_snake_case: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tests/format/flow/flow-repo/union_new/test9.js` (JAVASCRIPT) | Magnitude: 7.4 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 4, args: 4, branch: 3, func_start: 2
- `tests/format/flow-repo/ambient_declarations/component_namespace.js` (JAVASCRIPT) | Magnitude: 13.6 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 2, indent_spaces: 2, args: 1, safety_bypasses: 1
- `tests/format/flow/flow-repo/react_modules/es6class-types-callsite.js` (JAVASCRIPT) | Magnitude: 4.9 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, safety_bypasses: 4, ui_framework: 3
- `tests/integration/__tests__/debug-print-doc.js` (JAVASCRIPT) | Magnitude: 18.2 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 8, state_mutation: 3, safety_bypasses: 2, structural_boundaries: 1
- `tests/format/flow/assignments/issue-10850.js` (JAVASCRIPT) | Magnitude: 12.6 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: ui_framework: 3, bitwise_ops: 2, indent_spaces: 2, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/format/flow/flow-repo/try/init.js` (JAVASCRIPT) | Magnitude: 30.38 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 90, safety: 33, structural_boundaries: 30, args: 15
- `tests/format/typescript/class/parameter-properties.ts` (TYPESCRIPT) | Magnitude: 7.46 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 5, encapsulation: 4, args: 3
- `tests/format/flow/flow-repo/predicates-abstract/sanity-refine.js` (JAVASCRIPT) | Magnitude: 10.88 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: safety: 12, structural_boundaries: 11, args: 4, func_start: 4
- `scripts/generate-flow-estree-type-definition.js` (JAVASCRIPT) | Magnitude: 66.36 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 43, core_var_decl: 18, structural_boundaries: 15, design_snake_case: 14
- `src/utilities/create-get-visitor-keys.js` (JAVASCRIPT) | Magnitude: 16.42 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 17, branch: 4, structural_boundaries: 4, safety: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/format/js/comments/trailing-jsdocs.js` (JAVASCRIPT) | Magnitude: 13.6 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 4, immutability_locks: 4, indent_spaces: 4, api: 1
- `tests/format/typescript/mapped-type/issue-11098.ts` (TYPESCRIPT) | Magnitude: 15.64 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 10, core_var_decl: 10, design_pascal_case: 10
- `.github/workflows/mark-issue-duplicate.yml` (YAML) | Magnitude: 15.36 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, args: 4, branch: 2, structural_boundaries: 2
- `tests/format/flow/flow-repo/import_typeof/import_typeof.js` (JAVASCRIPT) | Magnitude: 15.68 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 32, core_var_decl: 18, import: 14, safety: 10
- `src/language-js/parse/index.js` (JAVASCRIPT) | Magnitude: 23.68 | Delta: **0.157** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, api: 9, import: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/format/handlebars/style-tag/with-lang-attribute-3.hbs` (HTML) | Magnitude: 12.08 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 4, func_start: 1, class_start: 1, decorators: 1
- `.github/workflows/cleanup-cspell.yml` (YAML) | Magnitude: 13.64 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 28, args: 5, func_start: 4, globals: 4
- `.github/workflows/lock.yml` (YAML) | Magnitude: 16.38 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 15, args: 5, branch: 2, structural_boundaries: 2
- `tests/format/typescript/no-semi/no-semi.ts` (TYPESCRIPT) | Magnitude: 13.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 1, class_start: 1, immutability_locks: 1
- `src/cli/file-info.js` (JAVASCRIPT) | Magnitude: 8.24 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 7, import: 4, concurrency: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/main/comments/attach.js` (JAVASCRIPT) | Magnitude: 257.5 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 266, branch: 77, core_var_decl: 45, structural_boundaries: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tests/format/typescript/compiler/anyIsAssignableToObject.ts` (TYPESCRIPT) | Magnitude: 13.12 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 3, class_start: 2, indent_spaces: 2, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/language-js/embed/css.js` (JAVASCRIPT) | Magnitude: 102.22 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 104, branch: 42, structural_boundaries: 32, safety: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/format/flow/flow-repo/generators/return.js` (JAVASCRIPT) | Magnitude: 2.62 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 7, safety_bypasses: 3, core_var_decl: 3
- `tests/format/flow/flow-repo/refinements/void.js` (JAVASCRIPT) | Magnitude: 85.2 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 52, branch: 43, safety: 22, structural_boundaries: 16
- `scripts/clean-cspell.js` (JAVASCRIPT) | Magnitude: 31.3 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 18, core_var_decl: 10, args: 8
- `tests/integration/__tests__/infer-parser.js` (JAVASCRIPT) | Magnitude: 74.74 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 280, structural_boundaries: 58, test: 47, state_mutation: 46
- `tests/integration/__tests__/with-shebang.js` (JAVASCRIPT) | Magnitude: 13.6 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 3, structural_boundaries: 1, args: 1, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/main/get-cursor-node.js` (JAVASCRIPT) | Magnitude: 56.38 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 50, core_var_decl: 15, design_camel_case: 15, branch: 14
- `src/language-js/location/overrides.js` (JAVASCRIPT) | Magnitude: 48.5 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 63, branch: 26, safety: 23, structural_boundaries: 21

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/language-js/parentheses/needs-parentheses.js` -> **fisker Cheung** (85.7% isolated ownership) | Magnitude: 837.12
- `tests/format/flow/flow-repo/type_param_variance2/libs/Promise.js` -> **fisker Cheung** (100.0% isolated ownership) | Magnitude: 663.6
- `src/language-js/print/jsx.js` -> **fisker Cheung** (100.0% isolated ownership) | Magnitude: 644.46
- `tests/format/typescript/_errors_/modifiers/format.test.js` -> **fisker Cheung** (100.0% isolated ownership) | Magnitude: 578.2
- `src/language-handlebars/printer-glimmer.js` -> **fisker Cheung** (100.0% isolated ownership) | Magnitude: 535.96

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/index.js` -> **Severity: 0.014** (Bridge: 0.0003 * Flux: 43.1409%)
- `src/document/printer/printer.js` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.9997%)
- `src/language-js/print/index.js` -> **Severity: 0.003** (Bridge: 0.0001 * Flux: 27.4596%)
- `scripts/utilities/generate-schema.js` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 95.3635%)
- `src/cli/options/get-context-options.js` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 76.5323%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/document/printer/printer.js` -> **Severity: 0.767** (Embedded: 0.0122 * Error Risk: 62.78%)
- `src/document/utilities/index.js` -> **Severity: 0.711** (Embedded: 0.0146 * Error Risk: 48.6633%)
- `src/document/builders/align.js` -> **Severity: 0.679** (Embedded: 0.0121 * Error Risk: 56.2528%)
- `src/document/builders/join.js` -> **Severity: 0.664** (Embedded: 0.0121 * Error Risk: 54.7004%)
- `src/document/utilities/traverse-doc.js` -> **Severity: 0.648** (Embedded: 0.0107 * Error Risk: 60.7392%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/config/get-prettier.js` -> **Severity: 273.1** (Blast Radius: 2.731 * Doc Risk: 100.0%)
- `tests/config/format-test/utilities.js` -> **Severity: 251.0** (Blast Radius: 2.51 * Doc Risk: 100.0%)
- `src/document/utilities/index.js` -> **Severity: 204.783** (Blast Radius: 2.355 * Doc Risk: 86.9565%)
- `src/index.js` -> **Severity: 191.2** (Blast Radius: 2.39 * Doc Risk: 80.0%)
- `src/language-js/location/is-index.js` -> **Severity: 184.3** (Blast Radius: 1.843 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 326 literal sites + 5 sites through wrappers = 331
- **`panics_and_aborts`:** 319 literal sites + 1 sites through wrappers = 320

- `bar` (function, debug_prints, primitive): 1 call sites in 1 files -- `tests/format/typescript/arrow/arrow_regression.ts`
- `print` (function, debug_prints, primitive): 1 call sites in 1 files -- `tests/format/flow/flow-repo/union_new/issue-1462-i.js`
- `print` (function, debug_prints, primitive): 1 call sites in 1 files -- `tests/format/flow/flow-repo/union_new/issue-1462-ii.js`
- `qux` (function, debug_prints, primitive): 1 call sites in 1 files -- `tests/format/flow/flow-repo/try/return.js`
- `qux` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `tests/format/flow/flow-repo/try/return.js`
- `showErrorMessage` (function, debug_prints, primitive): 1 call sites in 1 files -- `scripts/lint-changelog.js`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 7895 call pairs -- scoped 40.5%, unique 0.0%, ambiguous 15.2%, external 44.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 7707 | 41.0% | 0.0% | 15.2% | 43.8% |
| typescript | 146 | 25.3% | 0.0% | 19.2% | 55.5% |
| html | 35 | 2.9% | 0.0% | 0.0% | 97.1% |
| shell | 7 | 14.3% | 0.0% | 0.0% | 85.7% |

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
