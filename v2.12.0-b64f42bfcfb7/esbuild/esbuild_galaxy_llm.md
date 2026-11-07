# ARCHITECTURAL_BRIEF: esbuild
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/evanw/esbuild.git` |
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
- **Scope:** 322 analyzed artifact(s), 160891 LOC.
- **Load-bearing artifact:** `internal/logger/logger.go` -- 67 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `scripts/end-to-end-tests.js` -- pulls in 125 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `internal/js_parser/js_parser.go` at magnitude 14724.0 (structural weight, not risk).
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
| Total Artifacts | 348 |
| Analyzed Artifacts (Scanned) | 322 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 26 |
| Total LOC | 160891 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 92.5% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4645 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1123 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 10.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8905 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 24 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 147 | 116683 | 45.7% |
| PLAINTEXT | 55 | 0 | 17.1% |
| MARKDOWN | 46 | 0 | 14.3% |
| JAVASCRIPT | 24 | 29197 | 7.5% |
| TYPESCRIPT | 20 | 9072 | 6.2% |
| JSON | 13 | 3242 | 4.0% |
| XML | 5 | 0 | 1.6% |
| HTML | 5 | 1456 | 1.6% |
| YAML | 4 | 347 | 1.2% |
| MAKEFILE | 1 | 804 | 0.3% |
| SHELL | 1 | 18 | 0.3% |
| CSS | 1 | 72 | 0.3% |

## 4.1 SOURCE ENCODINGS
All 322 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 43%, Large Core Modules (3) 14%, Callbacks & Closures Files 9%, Compute Cores Files 8%, Large Core Modules 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 221 | 68.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 101 | 31.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 26*

**Composition by Extension & Reason:**
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 5x Excluded (Explicitly Denied Extension: '.png')
- `.go`: 1x Excluded (Machine-Generated Source Code Signature: 423 LOC), 1x Excluded (Machine-Generated Source Code Signature: 938 LOC), 1x Excluded (Embedded Hex Payload: 4058 hex tokens in 2066 LOC)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (Massive Static Asset Blob: 5304 LOC), 1x Excluded (Static Asset Blob without Intent: 2344 LOC)
- `.mod`: 1x Unsupported Format (.mod)
- `.sum`: 1x Excluded (Unsupported Extension: '.sum')
- `.version`: 1x Excluded (Unsupported Extension: '.version')
- `.ts`: 1x Unsupported Format (.undeterminable)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.conf`: 1x Excluded (Unsupported Extension: '.conf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 28.9 | 23.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 90.4 | 45.7 | 55.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 35.0 | 21.7 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 26.3 | 2.3 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 87.9 | 8.5 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 61.1 | 97.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 14.2 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.3 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 64.9 | 5.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 76.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1814 | 107 | 13 | `internal/js_parser/js_parser.go` |
| cleanup | 214 | 23 | 0 | `Makefile` |
| guards | 5517 | 165 | 30 | `scripts/end-to-end-tests.js` |
| danger | 2741 | 80 | 8 | `scripts/end-to-end-tests.js` |
| concurrency | 3963 | 66 | 11 | `scripts/js-api-tests.js` |
| connectivity | 6142 | 147 | 33 | `internal/js_ast/js_ast.go` |
| io | 1891 | 47 | 3 | `scripts/js-api-tests.js` |
| crypto | 4 | 4 | 0 | `lib/npm/node-install.ts` |
| ipc | 202 | 32 | 0 | `lib/npm/node.ts` |
| time | 109 | 29 | 0 | `scripts/js-api-tests.js` |
| serialization | 237 | 26 | 0 | `scripts/js-api-tests.js` |
| regex | 178 | 35 | 1 | `scripts/js-api-tests.js` |
| events | 202 | 24 | 0 | `scripts/js-api-tests.js` |
| tests | 3600 | 55 | 5 | `scripts/js-api-tests.js` |
| docs | 6175 | 132 | 44 | `internal/js_parser/js_parser.go` |
| debt | 2105 | 75 | 5 | `scripts/decorator-tests.js` |
| mutation | 30427 | 179 | 185 | `scripts/end-to-end-tests.js` |
| dead_code | 2487 | 146 | 15 | `scripts/js-api-tests.js` |
| credential | 314 | 11 | 0 | `scripts/browser/package-lock.json` |
| threat | 37 | 13 | 0 | `internal/bundler_tests/bundler_default_test.go` |
| ml_ai | 96 | 15 | 0 | `internal/js_ast/js_ast_helpers.go` |
| ui | 40 | 10 | 0 | `scripts/try.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.1556**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/js-api-tests.js` (Hits: 783)
- `scripts/plugin-tests.js` (Hits: 180)
- `scripts/end-to-end-tests.js` (Hits: 171)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **logger.go** (`internal/logger/logger.go`) — 67 inbound connections
2. **bitset.go** (`internal/helpers/bitset.go`) — 42 inbound connections
3. **config.go** (`internal/config/config.go`) — 39 inbound connections
4. **compat.go** (`internal/compat/compat.go`) — 34 inbound connections
5. **ast.go** (`internal/ast/ast.go`) — 31 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **end-to-end-tests.js** (`scripts/end-to-end-tests.js`) — 125 outbound dependencies
2. **js-api-tests.js** (`scripts/js-api-tests.js`) — 56 outbound dependencies
3. **plugin-tests.js** (`scripts/plugin-tests.js`) — 40 outbound dependencies
4. **api_impl.go** (`pkg/api/api_impl.go`) — 32 outbound dependencies
5. **verify-source-map.js** (`scripts/verify-source-map.js`) — 32 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `visitExprInOut` **(Many-Argument Workhorses)** (@ `internal/js_parser/js_parser.go`) -> Impact: **1342.3** | LOC: 2424
  * *Intent:* // This function takes "exprIn" as input from the caller and produces "exprOut" // for the caller to pass along extra data. This is mostly for optiona...
- `printExpr` **(Many-Argument Workhorses)** (@ `internal/js_printer/js_printer.go`) -> Impact: **923.4** | LOC: 1348
- `parseOptionsImpl` **(Many-Argument Workhorses)** (@ `pkg/cli/cli_impl.go`) -> Impact: **795.4** | LOC: 926
- `visitAndAppendStmt` **(Many-Argument Workhorses)** (@ `internal/js_parser/js_parser.go`) -> Impact: **603.0** | LOC: 1218
- `parseStmt` **(Many-Argument Workhorses)** (@ `internal/js_parser/js_parser.go`) -> Impact: **486.0** | LOC: 1348
- `parseProperty` **(Many-Argument Workhorses)** (@ `internal/js_parser/js_parser.go`) -> Impact: **441.4** | LOC: 555
- `parseSuffix` **(Many-Argument Workhorses)** (@ `internal/js_parser/js_parser.go`) -> Impact: **416.0** | LOC: 718
- `printStmt` **(Many-Argument Workhorses)** (@ `internal/js_printer/js_printer.go`) -> Impact: **347.0** | LOC: 809
- `parsePrefix` **(Many-Argument Workhorses)** (@ `internal/js_parser/js_parser.go`) -> Impact: **298.5** | LOC: 610
- `mangleStmts` **(Many-Argument Workhorses)** (@ `internal/js_parser/js_parser.go`) -> Impact: **275.4** | LOC: 519

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `scripts` | 28 | 22578.2 | 64.0% | 22.87% |
| `internal/js_parser` | 11 | 22027.04 | 27.29% | 36.39% |
| `internal/css_parser` | 21 | 7909.94 | 37.81% | 22.37% |
| `internal/bundler_tests` | 15 | 5829.7 | 2.65% | 74.78% |
| `internal/linker` | 2 | 4584.92 | 43.95% | 12.3% |
| `internal/resolver` | 7 | 4252.26 | 27.69% | 32.13% |
| `internal/js_printer` | 2 | 4004.7 | 27.03% | 52.41% |
| `internal/js_ast` | 4 | 3315.34 | 12.43% | 35.28% |
| `pkg/api` | 8 | 3136.4 | 14.78% | 37.91% |
| `lib/shared` | 5 | 3082.53 | 71.94% | 10.52% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `internal/helpers/float.go` -> **100.0%** Exposure
- `scripts/decorator-tests.ts` -> **100.0%** Exposure
- `scripts/decorator-tests.js` -> **100.0%** Exposure
- `internal/fs/iswin_wasm.go` -> **99.9925%** Exposure
- `.github/workflows/ci.yml` -> **99.9885%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cmd/esbuild/stdio_protocol.go` -> **100.0%** Exposure
- `internal/bundler_tests/bundler_test.go` -> **100.0%** Exposure
- `internal/config/config.go` -> **100.0%** Exposure
- `internal/css_parser/css_decls.go` -> **100.0%** Exposure
- `internal/css_parser/css_decls_box_shadow.go` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scripts/decorator-tests.js` -> **0** Orphaned Functions | **535** Duplicates
- `scripts/js-api-tests.js` -> **323** Orphaned Functions | **22** Duplicates
- `scripts/decorator-tests.ts` -> **0** Orphaned Functions | **322** Duplicates
- `internal/bundler_tests/bundler_default_test.go` -> **301** Orphaned Functions | **0** Duplicates
- `internal/js_parser/js_parser_test.go` -> **130** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `980` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `internal/js_parser/js_parser.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.869)
- **Top Global Matches:** file_cluster_8: 7.869, file_cluster_6: 13.081, file_cluster_4: 21.279
- **Magnitude:** 14724.0 | **LOC:** 18789 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **16**; blast radius 5.064; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.4%), Complexity Load (formerly Cognitive Load) (47.4%)
- **Documentation Coverage:** 80.5825% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visitExprInOut` **(Many-Argument Workhorses)** (Impact: 1342.3)
    * *Intent:* // This function takes "exprIn" as input from the caller and produces "exprOut" // for the caller to...
  * `visitAndAppendStmt` **(Many-Argument Workhorses)** (Impact: 603.0)
  * `parseStmt` **(Many-Argument Workhorses)** (Impact: 486.0)
  * `parseProperty` **(Many-Argument Workhorses)** (Impact: 441.4)
  * `parseSuffix` **(Many-Argument Workhorses)** (Impact: 416.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 1848 instances
* *High Risk Execution (weighted view):* 32
* *State Mutation (weighted view):* 5721
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4265`, `structural_boundaries: 1491`, `args: 196`, `func_start: 196`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 34`, `state_mutation: 2025`, `dead_code: 62`, `planned_debt: 10`, `fragile_debt: 11`, `unreferenced_by_name: 9`
* *Architecture:* `api: 19`, `import: 1`
* *Defense:* `safety: 2`, `doc: 1236`, `test: 19`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.064
  * `Choke Point (Betweenness):` 0.002577 | `Ripple Effect (Closeness):` 0.067723
  * `Imports (Out-Degree: 13):` fmt, ast, compat, config, helpers, js_ast, js_lexer, logger...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `scripts/end-to-end-tests.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.955)
- **Top Global Matches:** file_cluster_8: 9.955, file_cluster_6: 11.484, file_cluster_4: 19.063
- **Magnitude:** 7222.86 | **LOC:** 9848 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 83.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **125**; blast radius 1.578; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test` **(Many-Argument Workhorses)** (Impact: 59.2)
  * `quote` **(Defensive Guards)** (Impact: 22.3)
    * *Intent:* // Use the shell to set the working directory instead of using node's // "child_process" module. For...
  * `patchString` **(Defensive Guards)** (Impact: 11.1)
  * `waitForCondition` **(Defensive Guards)** (Impact: 10.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 37 instances
* *Amplified Race Conditions:* 534 instances
* *Amplified Cascading Flux:* 103 instances
* *High Risk Execution (weighted view):* 28
* *Concurrency (weighted view):* 3536
* *State Mutation (weighted view):* 2769
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 3508`, `args: 1034`, `func_start: 675`, `class_start: 144`
* *Risk/State:* `safety_bypasses: 118`, `high_risk_execution: 65`, `state_mutation: 2563`, `dead_code: 12`, `planned_debt: 1`, `fragile_debt: 8`, `unreferenced_by_name: 1`
* *Architecture:* `io: 171`, `api: 635`, `concurrency: 866`, `import: 547`
* *Defense:* `safety: 1435`, `test: 819`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` #pkg, bar.js, , common, qux, , file.js, File1.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/linker/linker.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.67)
- **Top Global Matches:** file_cluster_8: 6.67, file_cluster_6: 17.248, file_cluster_3: 19.937
- **Magnitude:** 4496.92 | **LOC:** 7294 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **31**; blast radius 2.835; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.2%), Complexity Load (formerly Cognitive Load) (36.7%)
- **Documentation Coverage:** 61.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scanImportsAndExports` **(I/O & Config Routines)** (Impact: 188.8)
  * `generateCodeForFileInChunkJS` **(Many-Argument Workhorses)** (Impact: 181.7)
  * `generateChunkJS` **(Many-Argument Workhorses)** (Impact: 153.4)
  * `convertStmtsForChunk` **(Many-Argument Workhorses)** (Impact: 141.6)
  * `generateChunkCSS` **(Many-Argument Workhorses)** (Impact: 140.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 612 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 1937
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1185`, `structural_boundaries: 595`, `args: 75`, `func_start: 75`, `class_start: 27`
* *Risk/State:* `high_risk_execution: 11`, `state_mutation: 713`, `dead_code: 10`, `planned_debt: 5`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 15`, `concurrency: 9`, `import: 1`
* *Defense:* `safety: 1`, `doc: 631`, `sync_locks: 5`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.835
  * `Choke Point (Betweenness):` 0.00467 | `Ripple Effect (Closeness):` 0.03797
  * `Imports (Out-Degree: 21):` bytes, base64, binary, fmt, ast, bundler, compat, config...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scripts/js-api-tests.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.435)
- **Top Global Matches:** file_cluster_12: 8.435, file_cluster_10: 9.133, file_cluster_15: 9.441
- **Magnitude:** 3836.72 | **LOC:** 8070 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **56**; blast radius 1.578; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (99.7%), Complexity Load (formerly Cognitive Load) (93.3%), Guard Balance (formerly Safety Score) (42.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `makeEventStream` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `testWatchStdoutChildProcess` **(Defensive Guards)** (Impact: 16.3)
  * `testIncrementalChildProcessExit` **(Callbacks & Closures)** (Impact: 12.0)
    * *Intent:* // More info about this test case: https://github.com/evanw/esbuild/issues/2727
  * `rebuildCancel` **(Defensive Guards)** (Impact: 11.5)
  * `rapidRebuildCancel` **(Defensive Guards)** (Impact: 10.5)
    * *Intent:* // This test checks for races between manual "rebuild()" and "cancel()". // Ideally calling "cancel(...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 30 instances
* *Amplified Race Conditions:* 103 instances
* *Amplified Cascading Flux:* 52 instances
* *High Risk Execution (weighted view):* 27
* *Concurrency (weighted view):* 2059
* *State Mutation (weighted view):* 229
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 2243`, `args: 732`, `func_start: 531`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 77`, `high_risk_execution: 57`, `state_mutation: 125`, `fragile_debt: 3`, `duplicate_logic: 22`, `unreferenced_by_name: 323`
* *Architecture:* `io: 783`, `api: 176`, `concurrency: 1544`, `import: 231`
* *Defense:* `safety: 367`, `test: 964`, `immutability_locks: 3`, `cleanup: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $chunk, $path.basename(inputCommon), $chunk, , $chunk, $path.basename(imported), $path.basename(inputCommon), a.unknown...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/js_printer/js_printer.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.747)
- **Top Global Matches:** file_cluster_6: 8.747, file_cluster_8: 10.558, file_cluster_4: 16.054
- **Magnitude:** 3777.18 | **LOC:** 5026 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **15**; blast radius 2.145; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.2%), Complexity Load (formerly Cognitive Load) (48.3%)
- **Documentation Coverage:** 86.4865% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printExpr` **(Many-Argument Workhorses)** (Impact: 923.4)
  * `printStmt` **(Many-Argument Workhorses)** (Impact: 347.0)
  * `printUnquotedUTF16` **(Many-Argument Workhorses)** (Impact: 135.2)
  * `printRequireOrImportExpr` **(Many-Argument Workhorses)** (Impact: 125.6)
  * `printProperty` **(Compute Cores)** (Impact: 121.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 335 instances
* *State Mutation (weighted view):* 1013
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1315`, `structural_boundaries: 245`, `args: 71`, `func_start: 71`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 7`, `state_mutation: 343`, `planned_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 35`, `import: 1`
* *Defense:* `doc: 168`, `test: 5`, `immutability_locks: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.145
  * `Choke Point (Betweenness):` 8.6e-05 | `Ripple Effect (Closeness):` 0.034298
  * `Imports (Out-Degree: 8):` bytes, fmt, ast, compat, config, helpers, js_ast, logger...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scripts/decorator-tests.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 15.476)
- **Top Global Matches:** file_cluster_10: 15.476, file_cluster_12: 15.496, file_cluster_15: 16.274
- **Magnitude:** 3474.28 | **LOC:** 5384 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 2.919; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (92.8%), Complexity Load (formerly Cognitive Load) (89.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__decorateElement` **(Defensive Guards)** (Impact: 130.8)
  * `__runInitializers` **(Compute Cores)** (Impact: 9.1)
  * `prettyPrint` **(Defensive Guards)** (Impact: 7.5)
  * `__decoratorContext` **(Compute Cores)** (Impact: 7.4)
  * `__privateAdd` **(Defensive Guards)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 50 instances
* *Amplified Cascading Flux:* 222 instances
* *Concurrency (weighted view):* 308
* *State Mutation (weighted view):* 1674
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 2531`, `args: 1870`, `func_start: 639`, `class_start: 131`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 1230`, `duplicate_logic: 535`
* *Architecture:* `concurrency: 58`
* *Defense:* `safety: 158`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.919
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003115
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `internal/bundler/bundler.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.763)
- **Top Global Matches:** file_cluster_3: 9.763, file_cluster_8: 14.725, file_cluster_6: 27.49
- **Magnitude:** 2657.26 | **LOC:** 3532 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **30**; blast radius 3.477; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.0%)
- **Documentation Coverage:** 80.4878% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseFile` **(Many-Argument Workhorses)** (Impact: 220.8)
  * `processScannedFiles` **(Many-Argument Workhorses)** (Impact: 153.4)
  * `runOnLoadPlugins` **(Many-Argument Workhorses)** (Impact: 112.6)
  * `addEntryPoints` **(Compute Cores)** (Impact: 108.6)
  * `RunOnResolvePlugins` **(Many-Argument Workhorses)** (Impact: 91.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 353 instances
* *Concurrency (weighted view):* 60
* *State Mutation (weighted view):* 1096
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 628`, `structural_boundaries: 303`, `args: 34`, `func_start: 34`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 390`, `planned_debt: 3`, `fragile_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 16`, `concurrency: 15`, `import: 1`
* *Defense:* `safety: 7`, `doc: 243`, `sync_locks: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.477
  * `Choke Point (Betweenness):` 0.004997 | `Ripple Effect (Closeness):` 0.041231
  * `Imports (Out-Degree: 16):` bytes, base32, base64, fmt, ast, cache, compat, config...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `scripts/decorator-tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.704)
- **Top Global Matches:** file_cluster_5: 9.704, file_cluster_12: 10.291, file_cluster_7: 10.36
- **Magnitude:** 2475.88 | **LOC:** 3913 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.5%), Complexity Load (formerly Cognitive Load) (93.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prettyPrint` **(Defensive Guards)** (Impact: 7.5)
  * `run` **(Defensive Guards)** (Impact: 4.8)
  * `assertEq` **(Defensive Guards)** (Impact: 4.2)
  * `assertThrows` **(Defensive Guards)** (Impact: 4.2)
  * `fieldDec1` **(Callbacks & Closures)** (Impact: 4.0)
    * *Intent:* // Field decorators
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 56 instances
* *Amplified Cascading Flux:* 207 instances
* *Concurrency (weighted view):* 339
* *State Mutation (weighted view):* 1152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 2525`, `args: 1686`, `func_start: 386`, `class_start: 130`
* *Risk/State:* `safety_bypasses: 223`, `state_mutation: 738`, `planned_debt: 1`, `duplicate_logic: 322`
* *Architecture:* `api: 2`, `concurrency: 59`
* *Defense:* `safety: 10`, `test: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/shared/common.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.316)
- **Top Global Matches:** file_cluster_4: 9.316, file_cluster_12: 10.948, file_cluster_5: 12.241
- **Magnitude:** 2276.82 | **LOC:** 1879 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **3**; blast radius 4.759; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (89.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildOrContextImpl` **(Many-Argument Workhorses)** (Impact: 196.2)
  * `flagsForBuildOptions` **(Many-Argument Workhorses)** (Impact: 150.4)
  * `buildOrContextContinue` **(Many-Argument Workhorses)** (Impact: 100.5)
    * *Intent:* // "buildOrContext" cannot be written using async/await due to "buildSync" // and must be written in...
  * `createChannel` **(Defensive Guards)** (Impact: 98.8)
    * *Intent:* // This can't use any promises in the main execution flow because it must work // for both sync and ...
  * `pushCommonFlags` **(Many-Argument Workhorses)** (Impact: 90.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 284 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 82
* *State Mutation (weighted view):* 864
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 390`, `structural_boundaries: 356`, `args: 160`, `func_start: 108`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 69`, `high_risk_execution: 1`, `state_mutation: 296`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 28`, `api: 16`, `concurrency: 32`, `import: 3`
* *Defense:* `safety: 52`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.759
  * `Choke Point (Betweenness):` 0.000122 | `Ripple Effect (Closeness):` 0.016021
  * `Imports (Out-Degree: 3):` stdio_protocol, types, uint8array_json_parser
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `internal/js_lexer/js_lexer.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.321)
- **Top Global Matches:** file_cluster_6: 6.321, file_cluster_4: 11.471, file_cluster_8: 14.254
- **Magnitude:** 2252.62 | **LOC:** 2666 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **9**; blast radius 4.955; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.9%), Complexity Load (formerly Cognitive Load) (47.5%)
- **Documentation Coverage:** 86.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Next` **(I/O & Config Routines)** (Impact: 241.6)
  * `tryToDecodeEscapeSequences` **(Many-Argument Workhorses)** (Impact: 152.1)
    * *Intent:* // If this fails, this returns "nil, false, end" where "end" is the value to // store to "lexer.end"...
  * `parseNumericLiteralOrDot` **(I/O & Config Routines)** (Impact: 120.3)
  * `NextInsideJSXElement` **(I/O & Config Routines)** (Impact: 56.0)
  * `scanCommentText` **(I/O & Config Routines)** (Impact: 46.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 354 instances
* *State Mutation (weighted view):* 1070
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 651`, `structural_boundaries: 133`, `args: 45`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 11`, `state_mutation: 362`, `dead_code: 1`, `unreferenced_by_name: 18`
* *Architecture:* `api: 181`, `import: 1`
* *Defense:* `doc: 137`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.955
  * `Choke Point (Betweenness):` 0.000186 | `Ripple Effect (Closeness):` 0.069803
  * `Imports (Out-Degree: 5):` fmt, ast, config, helpers, js_ast, logger, strconv, strings...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `internal/js_ast/js_ast_helpers.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.694)
- **Top Global Matches:** file_cluster_8: 6.694, file_cluster_6: 17.706, file_cluster_3: 19.296
- **Magnitude:** 2238.22 | **LOC:** 3017 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.578; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.3%), Complexity Load (formerly Cognitive Load) (26.6%)
- **Documentation Coverage:** 61.3861% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SimplifyUnusedExpr` **(Many-Argument Workhorses)** (Impact: 192.7)
    * *Intent:* // This will return a nil expression if the expression can be totally removed. // // This function i...
  * `MangleIfExpr` **(Many-Argument Workhorses)** (Impact: 146.1)
    * *Intent:* // This function intentionally avoids mutating the input AST so it can be // called after the AST ha...
  * `CheckEqualityIfNoSideEffects` **(Many-Argument Workhorses)** (Impact: 115.5)
    * *Intent:* // Returns "equal, ok". If "ok" is false, then nothing is known about the two // values. If "ok" is ...
  * `FoldBinaryOperator` **(Many-Argument Workhorses)** (Impact: 111.1)
    * *Intent:* // This function intentionally avoids mutating the input AST so it can be // called after the AST ha...
  * `ExprCanBeRemovedIfUnused` **(Compute Cores)** (Impact: 109.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 119 instances
* *State Mutation (weighted view):* 361
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 929`, `structural_boundaries: 519`, `args: 56`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 123`, `dead_code: 1`, `unreferenced_by_name: 19`
* *Architecture:* `api: 67`, `import: 1`
* *Defense:* `doc: 146`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ast, compat, helpers, logger, math, strconv, strings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/resolver/resolver.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.368)
- **Top Global Matches:** file_cluster_8: 6.368, file_cluster_6: 17.874, file_cluster_3: 18.778
- **Magnitude:** 2140.62 | **LOC:** 2973 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **16**; blast radius 3.968; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.5%), Complexity Load (formerly Cognitive Load) (31.0%)
- **Documentation Coverage:** 80.4348% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `finalizeImportsExportsResult` **(Many-Argument Workhorses)** (Impact: 270.7)
  * `parseTSConfigFromSource` **(Many-Argument Workhorses)** (Impact: 164.0)
  * `loadNodeModules` **(Many-Argument Workhorses)** (Impact: 113.0)
  * `Resolve` **(Many-Argument Workhorses)** (Impact: 112.4)
  * `ResolveGlob` **(Many-Argument Workhorses)** (Impact: 104.5)
    * *Intent:* // This returns nil on failure and non-nil on success. Note that this may // return an empty array t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 193 instances
* *State Mutation (weighted view):* 596
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 618`, `structural_boundaries: 303`, `args: 38`, `func_start: 38`, `class_start: 9`
* *Risk/State:* `state_mutation: 210`, `fragile_debt: 4`, `unreferenced_by_name: 8`
* *Architecture:* `api: 30`, `import: 1`
* *Defense:* `safety: 7`, `doc: 238`, `sync_locks: 7`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.968
  * `Choke Point (Betweenness):` 0.001981 | `Ripple Effect (Closeness):` 0.05095
  * `Imports (Out-Degree: 12):` errors, fmt, ast, cache, compat, config, fs, helpers...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `internal/js_parser/js_parser_lower_class.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.947)
- **Top Global Matches:** file_cluster_8: 5.947, file_cluster_6: 17.06, file_cluster_3: 19.638
- **Magnitude:** 2097.08 | **LOC:** 2601 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 2.111; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.8%), Complexity Load (formerly Cognitive Load) (37.4%)
- **Documentation Coverage:** 75.7576% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processProperties` **(Many-Argument Workhorses)** (Impact: 180.7)
  * `finishAndGenerateCode` **(Many-Argument Workhorses)** (Impact: 129.4)
  * `lowerField` **(Many-Argument Workhorses)** (Impact: 100.6)
    * *Intent:* // Handle lowering of instance and static fields. Move their initializers // from the class body to ...
  * `analyzeProperty` **(Many-Argument Workhorses)** (Impact: 80.0)
  * `computeClassLoweringInfo` **(Compute Cores)** (Impact: 73.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 309 instances
* *State Mutation (weighted view):* 960
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 480`, `structural_boundaries: 118`, `args: 33`, `func_start: 33`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 342`, `dead_code: 16`, `unreferenced_by_name: 9`
* *Architecture:* `import: 1`
* *Defense:* `doc: 213`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.04778
  * `Imports (Out-Degree: 7):` fmt, ast, compat, config, helpers, js_ast, logger
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scripts/plugin-tests.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.155)
- **Top Global Matches:** file_cluster_12: 7.155, file_cluster_10: 8.006, file_cluster_15: 9.366
- **Magnitude:** 1793.5 | **LOC:** 3513 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **40**; blast radius 1.578; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (82.0%), Debt Markers (formerly Tech Debt) (77.6%), Guard Balance (formerly Safety Score) (46.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `importAttributesOnResolve` **(Defensive Guards)** (Impact: 10.4)
  * `invalidRegExp` **(Defensive Guards)** (Impact: 10.3)
  * `onEndCallback` **(Defensive Guards)** (Impact: 10.0)
  * `setup` **(Defensive Guards)** (Impact: 9.3)
  * `fetch` **(Callbacks & Closures)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 12 instances
* *Amplified Race Conditions:* 77 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 806
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 855`, `args: 401`, `func_start: 216`
* *Risk/State:* `safety_bypasses: 59`, `high_risk_execution: 14`, `state_mutation: 85`, `duplicate_logic: 10`, `unreferenced_by_name: 98`
* *Architecture:* `io: 180`, `api: 97`, `concurrency: 421`, `import: 75`
* *Defense:* `safety: 147`, `test: 268`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` base.js, esbuild, example.custom, example.js, name, index, loadme, name...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/logger/logger.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.09)
- **Top Global Matches:** file_cluster_6: 6.09, file_cluster_4: 10.515, file_cluster_8: 15.072
- **Magnitude:** 1757.56 | **LOC:** 2074 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **67** in-repo importer(s); it depends on **9**; blast radius 78.022; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.0%), Debt Markers (formerly Tech Debt) (57.6%)
- **Documentation Coverage:** 79.0476% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `detailStruct` **(Many-Argument Workhorses)** (Impact: 74.3)
  * `msgString` **(Many-Argument Workhorses)** (Impact: 64.9)
  * `GenerateStringInJSTable` **(Many-Argument Workhorses)** (Impact: 64.6)
    * *Intent:* // For Yarn PnP we sometimes parse JSON embedded in a JS string. This generates // a table that rema...
  * `PrintSummary` **(Many-Argument Workhorses)** (Impact: 63.2)
  * `NewStderrLog` **(Compute Cores)** (Impact: 51.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 226 instances
* *State Mutation (weighted view):* 685
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 217`, `args: 60`, `func_start: 60`, `class_start: 19`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 233`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 28`
* *Architecture:* `api: 187`, `import: 1`
* *Defense:* `doc: 116`, `sync_locks: 21`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 78.022
  * `Choke Point (Betweenness):` 0.001012 | `Ripple Effect (Closeness):` 0.235245
  * `Imports (Out-Degree: 1):` binary, fmt, os, runtime, sort, strings, sync, time...
  * `Imported By (In-Degree: 67):` (Excluded from Brief to save tokens)

### `pkg/api/api_impl.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.813)
- **Top Global Matches:** file_cluster_4: 6.813, file_cluster_6: 7.15, file_cluster_9: 14.208
- **Magnitude:** 1745.36 | **LOC:** 2566 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **32**; blast radius 5.802; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.4%), Complexity Load (formerly Cognitive Load) (30.6%)
- **Documentation Coverage:** 86.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateBuildOptions` **(Many-Argument Workhorses)** (Impact: 110.5)
  * `analyzeMetafileImpl` **(Many-Argument Workhorses)** (Impact: 80.8)
  * `rebuildImpl` **(Many-Argument Workhorses)** (Impact: 76.6)
  * `validateDefines` **(Many-Argument Workhorses)** (Impact: 75.6)
  * `validateFeatures` **(Many-Argument Workhorses)** (Impact: 53.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 204 instances
* *High Risk Execution (weighted view):* 14
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 638
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 461`, `structural_boundaries: 303`, `args: 65`, `func_start: 65`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 15`, `state_mutation: 230`, `unreferenced_by_name: 13`
* *Architecture:* `api: 7`, `concurrency: 5`, `import: 1`
* *Defense:* `safety: 8`, `doc: 131`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.802
  * `Choke Point (Betweenness):` 0.006051 | `Ripple Effect (Closeness):` 0.020249
  * `Imports (Out-Degree: 18):` bytes, base64, binary, errors, fmt, api_helpers, ast, bundler...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `internal/css_parser/css_parser.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.543)
- **Top Global Matches:** file_cluster_8: 6.543, file_cluster_6: 11.851, file_cluster_4: 20.337
- **Magnitude:** 1724.32 | **LOC:** 2487 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **8**; blast radius 5.498; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.4%), Complexity Load (formerly Cognitive Load) (46.7%)
- **Documentation Coverage:** 91.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseAtRule` **(Compute Cores)** (Impact: 238.9)
  * `convertTokensHelper` **(Many-Argument Workhorses)** (Impact: 149.8)
  * `parseListOfRules` **(Compute Cores)** (Impact: 64.8)
  * `mangleRules` **(Many-Argument Workhorses)** (Impact: 63.5)
  * `parseSelectorRule` **(Many-Argument Workhorses)** (Impact: 48.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 234 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 714
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 533`, `structural_boundaries: 222`, `args: 40`, `func_start: 40`, `class_start: 12`
* *Risk/State:* `state_mutation: 246`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 7`, `concurrency: 1`, `import: 1`
* *Defense:* `doc: 139`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.498
  * `Choke Point (Betweenness):` 0.007979 | `Ripple Effect (Closeness):` 0.052735
  * `Imports (Out-Degree: 12):` fmt, ast, compat, config, css_ast, css_lexer, logger, strings
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `pkg/cli/cli_impl.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.179)
- **Top Global Matches:** file_cluster_6: 6.179, file_cluster_8: 11.738, file_cluster_4: 13.271
- **Magnitude:** 1693.24 | **LOC:** 1565 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 2.645; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.5%), Complexity Load (formerly Cognitive Load) (63.2%)
- **Documentation Coverage:** 73.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseOptionsImpl` **(Many-Argument Workhorses)** (Impact: 795.4)
  * `runImpl` **(Many-Argument Workhorses)** (Impact: 99.7)
  * `parseServeOptionsImpl` **(Compute Cores)** (Impact: 36.0)
  * `serveImpl` **(Defensive Guards)** (Impact: 21.4)
  * `parseOptionsForRun` **(Compute Cores)** (Impact: 18.0)
    * *Intent:* // This returns either BuildOptions, TransformOptions, or an error
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 205 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 620
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 458`, `structural_boundaries: 156`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 210`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 2`, `import: 1`
* *Defense:* `safety: 43`, `doc: 46`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.645
  * `Choke Point (Betweenness):` 0.000284 | `Ripple Effect (Closeness):` 0.008011
  * `Imports (Out-Degree: 5):` fmt, cli_helpers, fs, logger, api, ioutil, net, os...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `internal/bundler_tests/bundler_default_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.719)
- **Top Global Matches:** file_cluster_15: 5.719, file_cluster_2: 6.573, file_cluster_11: 7.245
- **Magnitude:** 1490.58 | **LOC:** 9410 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.578; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (93.4%), Guard Balance (formerly Safety Score) (49.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.4%), Mutation Surface (formerly State Flux) (13.6%)
- **Documentation Coverage:** 92.691% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestCommentPreservation` **(I/O & Config Routines)** (Impact: 9.7)
  * `TestThisWithES6Syntax` **(Compute Cores)** (Impact: 7.5)
    * *Intent:* // The value of "this" is "exports" in CommonJS modules and undefined in ES6 // modules. This is det...
  * `TestWarningsInsideNodeModules` **(Compute Cores)** (Impact: 6.5)
  * `TestLegalCommentsManyEndOfFile` **(I/O & Config Routines)** (Impact: 6.4)
  * `TestAssignToImport` **(Compute Cores)** (Impact: 6.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1379`, `args: 301`, `func_start: 301`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 165`, `dead_code: 3`, `fragile_debt: 2`, `unreferenced_by_name: 301`
* *Architecture:* `api: 301`, `import: 117`
* *Defense:* `doc: 79`, `test: 326`, `immutability_locks: 86`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.578
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` entry1.css, entry2.css, bundler, compat, config, helpers, js_ast, logger...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/js_parser/js_parser_lower.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.957)
- **Top Global Matches:** file_cluster_6: 5.957, file_cluster_8: 12.254, file_cluster_4: 12.729
- **Magnitude:** 1434.88 | **LOC:** 2133 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 1.909; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.0%), Complexity Load (formerly Cognitive Load) (35.1%)
- **Documentation Coverage:** 94.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lowerOptionalChain` **(Many-Argument Workhorses)** (Impact: 133.3)
  * `lowerFunction` **(Many-Argument Workhorses)** (Impact: 124.9)
  * `lowerObjectRestHelper` **(Many-Argument Workhorses)** (Impact: 104.0)
  * `markSyntaxFeature` **(Many-Argument Workhorses)** (Impact: 59.3)
  * `lowerTemplateLiteral` **(Many-Argument Workhorses)** (Impact: 41.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 184 instances
* *State Mutation (weighted view):* 585
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 328`, `structural_boundaries: 156`, `args: 36`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 217`, `dead_code: 7`, `planned_debt: 1`, `unreferenced_by_name: 18`
* *Architecture:* `import: 1`
* *Defense:* `doc: 111`, `test: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.909
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.047489
  * `Imports (Out-Degree: 8):` fmt, ast, compat, config, helpers, js_ast, logger
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `internal/css_ast/css_ast.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.367)
- **Top Global Matches:** file_cluster_15: 7.367, file_cluster_10: 7.428, file_cluster_16: 8.581
- **Magnitude:** 1227.66 | **LOC:** 1581 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **6**; blast radius 14.313; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.2%), Debt Markers (formerly Tech Debt) (26.1%)
- **Documentation Coverage:** 93.8865% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Equal` **(Compute Cores)** (Impact: 35.6)
  * `Equal` **(Compute Cores)** (Impact: 24.0)
  * `NumberOrFractionForPercentage` **(Compute Cores)** (Impact: 18.4)
  * `Equal` **(Compute Cores)** (Impact: 18.3)
  * `Equal` **(Compute Cores)** (Impact: 16.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 72 instances
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 336`, `args: 115`, `func_start: 115`, `class_start: 43`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 118`, `unreferenced_by_name: 18`
* *Architecture:* `api: 310`, `import: 1`
* *Defense:* `doc: 51`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.313
  * `Choke Point (Betweenness):` 0.000806 | `Ripple Effect (Closeness):` 0.130919
  * `Imports (Out-Degree: 4):` ast, css_lexer, helpers, logger, strconv, strings
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `internal/css_printer/css_printer.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.182)
- **Top Global Matches:** file_cluster_8: 6.182, file_cluster_6: 14.717, file_cluster_3: 22.734
- **Magnitude:** 1191.56 | **LOC:** 1324 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 2.139; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.8%), Complexity Load (formerly Cognitive Load) (44.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printRule` **(Many-Argument Workhorses)** (Impact: 235.4)
  * `printTokens` **(Many-Argument Workhorses)** (Impact: 99.9)
  * `printCompoundSelector` **(Many-Argument Workhorses)** (Impact: 84.1)
  * `printIdent` **(Many-Argument Workhorses)** (Impact: 83.6)
    * *Intent:* // Note: This function is hot in profiles
  * `printMediaQuery` **(Many-Argument Workhorses)** (Impact: 73.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 405`, `structural_boundaries: 70`, `args: 23`, `func_start: 23`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 96`, `unreferenced_by_name: 1`
* *Architecture:* `api: 20`, `import: 1`
* *Defense:* `doc: 32`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.139
  * `Choke Point (Betweenness):` 5.5e-05 | `Ripple Effect (Closeness):` 0.031584
  * `Imports (Out-Degree: 8):` fmt, ast, compat, config, css_ast, css_lexer, helpers, logger...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `internal/js_parser/js_parser_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.183)
- **Top Global Matches:** file_cluster_15: 7.183, file_cluster_11: 8.953, file_cluster_2: 8.975
- **Magnitude:** 1171.28 | **LOC:** 6956 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 2.695; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (73.2%), Mutation Surface (formerly State Flux) (56.2%), Guard Balance (formerly Safety Score) (52.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (33.2%)
- **Documentation Coverage:** 93.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestUnicodeWhitespace` **(Compute Cores)** (Impact: 16.5)
  * `TestStrictMode` **(I/O & Config Routines)** (Impact: 15.8)
  * `TestMangleIf` **(I/O & Config Routines)** (Impact: 14.3)
  * `TestMangleInlineLocals` **(Compute Cores)** (Impact: 13.7)
  * `TestMangleBooleanWithSideEffects` **(I/O & Config Routines)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 434
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 1510`, `args: 150`, `func_start: 150`, `class_start: 1`
* *Risk/State:* `state_mutation: 432`, `fragile_debt: 5`, `unreferenced_by_name: 130`
* *Architecture:* `api: 135`, `import: 1`
* *Defense:* `doc: 154`, `test: 137`, `immutability_locks: 88`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.695
  * `Choke Point (Betweenness):` 0.000315 | `Ripple Effect (Closeness):` 0.006231
  * `Imports (Out-Degree: 10):` +value+, fmt, ast, compat, config, helpers, js_ast, js_printer...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `internal/js_parser/ts_parser.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.923)
- **Top Global Matches:** file_cluster_6: 7.923, file_cluster_8: 10.437, file_cluster_4: 15.458
- **Magnitude:** 1090.5 | **LOC:** 2087 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 1.909; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.9%), Debt Markers (formerly Tech Debt) (35.9%)
- **Documentation Coverage:** 59.375% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `skipTypeScriptTypeWithFlags` **(Many-Argument Workhorses)** (Impact: 193.7)
  * `parseTypeScriptNamespaceStmt` **(Many-Argument Workhorses)** (Impact: 68.8)
  * `generateClosureForTypeScriptNamespaceOrEnum` **(Many-Argument Workhorses)** (Impact: 65.9)
  * `parseTypeScriptEnumStmt` **(Many-Argument Workhorses)** (Impact: 52.2)
  * `skipTypeScriptTypeParameters` **(Compute Cores)** (Impact: 45.4)
    * *Intent:* // This is the type parameter declarations that go with other symbol // declarations (class, functio...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Cascading Flux:* 110 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 339
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 105`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 7`, `state_mutation: 119`, `dead_code: 8`, `planned_debt: 6`, `fragile_debt: 2`, `unreferenced_by_name: 12`
* *Architecture:* `import: 1`
* *Defense:* `safety: 6`, `doc: 111`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.909
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.047489
  * `Imports (Out-Degree: 7):` fmt, ast, compat, helpers, js_ast, js_lexer, logger, strings
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `internal/resolver/package_json.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.854)
- **Top Global Matches:** file_cluster_3: 8.854, file_cluster_8: 15.499, file_cluster_6: 28.373
- **Magnitude:** 1054.34 | **LOC:** 1463 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 1.859; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.4%), Debt Markers (formerly Tech Debt) (29.9%)
- **Documentation Coverage:** 65.2174% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `esmPackageTargetResolve` **(Many-Argument Workhorses)** (Impact: 154.0)
  * `parseImportsExportsMap` **(Many-Argument Workhorses)** (Impact: 92.2)
  * `parsePackageJSON` **(Compute Cores)** (Impact: 90.6)
  * `checkBrowserMap` **(Many-Argument Workhorses)** (Impact: 83.8)
  * `esmPackageTargetReverseResolve` **(Many-Argument Workhorses)** (Impact: 57.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 283
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 316`, `structural_boundaries: 173`, `args: 20`, `func_start: 20`, `class_start: 7`
* *Risk/State:* `state_mutation: 95`, `fragile_debt: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 2`, `doc: 104`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.859
  * `Choke Point (Betweenness):` 9.9e-05 | `Ripple Effect (Closeness):` 0.03617
  * `Imports (Out-Degree: 7):` fmt, config, helpers, js_ast, js_lexer, js_parser, logger, url...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `internal/cache/cache.go` (GO) | Magnitude: 39.18 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 59, structural_boundaries: 26, api: 14, sync_locks: 7
- `scripts/decorator-tests.js` (JAVASCRIPT) | Magnitude: 3474.28 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 5328, structural_boundaries: 2531, args: 1870, closures: 1563
- `internal/ast/ast.go` (GO) | Magnitude: 363.22 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 294, api: 170, doc: 92, structural_boundaries: 89

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `internal/fs/modkey_other.go` (GO) | Magnitude: 8.68 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 18, structural_boundaries: 6, branch: 4, encapsulation: 2
- `internal/css_ast/css_ast.go` (GO) | Magnitude: 1227.66 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 894, structural_boundaries: 336, api: 310, branch: 289
- `Makefile` (MAKEFILE) | Magnitude: 639.38 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 548, branch: 316, func_start: 162, io: 125
- `internal/resolver/dataurl.go` (GO) | Magnitude: 45.46 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 49, structural_boundaries: 14, branch: 12, api: 9
- `internal/bundler_tests/bundler_packagejson_test.go` (GO) | Magnitude: 502.6 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 2704, structural_boundaries: 564, args: 96, func_start: 96

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `scripts/wasm-tests.js` (JAVASCRIPT) | Magnitude: 125.82 | Delta: **0.127** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 307, core_var_decl: 54, io: 51, state_mutation: 41

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Makefile` -> Churn: **64.9%** | Cog Load: 53.603% | Debt: 80.5011%
- `scripts/esbuild.js` -> Churn: **54.31%** | Cog Load: 96.8429% | Debt: 18.0471%
- `scripts/end-to-end-tests.js` -> Churn: **50.83%** | Cog Load: 98.6615% | Debt: 9.3198%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `internal/js_parser/js_parser.go` -> **Evan Wallace** (100.0% isolated ownership) | Magnitude: 14724.0
- `scripts/end-to-end-tests.js` -> **Evan Wallace** (83.3% isolated ownership) | Magnitude: 7222.86
- `internal/linker/linker.go` -> **Evan Wallace** (100.0% isolated ownership) | Magnitude: 4496.92
- `scripts/js-api-tests.js` -> **Evan Wallace** (100.0% isolated ownership) | Magnitude: 3836.72
- `internal/js_printer/js_printer.go` -> **Evan Wallace** (100.0% isolated ownership) | Magnitude: 3777.18

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `internal/css_parser/css_parser.go` -> **Severity: 0.798** (Bridge: 0.008 * Flux: 99.9997%)
- `internal/css_parser/css_decls.go` -> **Severity: 0.609** (Bridge: 0.0061 * Flux: 100.0%)
- `pkg/api/api_impl.go` -> **Severity: 0.605** (Bridge: 0.0061 * Flux: 99.9953%)
- `internal/bundler_tests/bundler_test.go` -> **Severity: 0.591** (Bridge: 0.0059 * Flux: 100.0%)
- `internal/bundler/bundler.go` -> **Severity: 0.5** (Bridge: 0.005 * Flux: 99.9999%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `internal/logger/logger.go` -> **Severity: 16.456** (Embedded: 0.2352 * Error Risk: 69.9539%)
- `internal/logger/msg_ids.go` -> **Severity: 10.19** (Embedded: 0.1395 * Error Risk: 73.0715%)
- `internal/ast/ast.go` -> **Severity: 9.062** (Embedded: 0.1643 * Error Risk: 55.1556%)
- `internal/helpers/bitset.go` -> **Severity: 8.994** (Embedded: 0.1773 * Error Risk: 50.7142%)
- `internal/compat/compat.go` -> **Severity: 8.482** (Embedded: 0.1486 * Error Risk: 57.0947%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `internal/logger/logger.go` -> **Severity: 6167.452** (Blast Radius: 78.022 * Doc Risk: 79.0476%)
- `internal/helpers/bitset.go` -> **Severity: 4350.5** (Blast Radius: 43.505 * Doc Risk: 100.0%)
- `compat-table/src/index.ts` -> **Severity: 2962.4** (Blast Radius: 29.624 * Doc Risk: 100.0%)
- `internal/ast/ast.go` -> **Severity: 2477.135** (Blast Radius: 37.157 * Doc Risk: 66.6667%)
- `scripts/esbuild.js` -> **Severity: 1786.1** (Blast Radius: 17.861 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1028 literal sites + 10 sites through wrappers = 1038
- **`panics_and_aborts`:** 1581 literal sites + 22 sites through wrappers = 1603

- `run` (function, debug_prints, primitive): 10 call sites in 1 files -- `scripts/test-yarnpnp.js`
- `__typeError` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `scripts/decorator-tests.js`
- `croak` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `scripts/terser-tests.js`
- `croak` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `scripts/uglify-tests.js`
- `log` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `scripts/terser-tests.js`
- `log` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `scripts/uglify-tests.js`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 16230 call pairs -- scoped 42.1%, unique 1.4%, ambiguous 11.1%, external 45.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| go | 10334 | 55.2% | 2.2% | 16.8% | 25.8% |
| javascript | 4206 | 14.5% | 0.0% | 1.4% | 84.2% |
| typescript | 1493 | 31.6% | 0.0% | 1.0% | 67.4% |
| html | 191 | 19.9% | 0.0% | 0.0% | 80.1% |
| shell | 6 | 0.0% | 0.0% | 0.0% | 100.0% |

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
