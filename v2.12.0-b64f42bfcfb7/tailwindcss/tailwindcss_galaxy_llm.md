# ARCHITECTURAL_BRIEF: tailwindcss
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/tailwindlabs/tailwindcss.git` |
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
- **Scope:** 481 analyzed artifact(s), 113718 LOC.
- **Load-bearing artifact:** `packages/tailwindcss/src/design-system.ts` -- 54 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `integrations/upgrade/index.test.ts` -- pulls in 50 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/tailwindcss/src/utilities.test.ts` at magnitude 18047.25 (structural weight, not risk).
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
| Total Artifacts | 538 |
| Analyzed Artifacts (Scanned) | 481 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 57 |
| Total LOC | 113718 |
| Volatility Index | 0.017 |
| % Scanned of codebase = | 89.4% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6112 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1469 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1504 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 61 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 309 | 102075 | 64.2% |
| RUST | 47 | 8793 | 9.8% |
| PLAINTEXT | 36 | 1 | 7.5% |
| MARKDOWN | 26 | 0 | 5.4% |
| CSS | 18 | 698 | 3.7% |
| JAVASCRIPT | 16 | 351 | 3.3% |
| JSON | 14 | 177 | 2.9% |
| YAML | 8 | 1055 | 1.7% |
| XML | 4 | 3 | 0.8% |
| HTML | 3 | 565 | 0.6% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 480 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 30%, Declarative / Non-Code 24%, Compute Cores Files 12%, Large Core Modules (3) 8%, Large Core Modules (2) 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 416 | 86.5% |
| Unknown | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 61 | 12.7% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 57*

**Composition by Extension & Reason:**
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 5x Unsupported Format (.toml), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.toml')
- `.haml`: 4x Unsupported Format (.haml)
- `.ts`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.snap`: 4x Unsupported Format (.snap)
- `.md`: 1x Excluded (Lexical Monotony: High structural repetition detected in 4288 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 2x Excluded (Unsupported Extension: '.lock')
- `.gitignore`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 2x Excluded (Unsupported Extension: '.patch')
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (Massive Static Asset Blob: 9485 LOC), 1x Zero-Density Threshold (LOC: 58, Signals: 0)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 23.3 | 6.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 91.0 | 37.2 | 50.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 98.3 | 3.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 16.5 | 6.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 29.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 45.4 | 26.5 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 91.5 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.3 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 6.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 53.6 | 84.6 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 136 | 65 | 1 | `packages/tailwindcss/src/candidate.ts` |
| cleanup | 6 | 3 | 0 | `packages/@tailwindcss-cli/src/utils/disposables.ts` |
| guards | 1034 | 173 | 6 | `packages/tailwindcss/src/canonicalize-candidates.ts` |
| danger | 621 | 135 | 4 | `integrations/upgrade/index.test.ts` |
| concurrency | 4938 | 153 | 17 | `packages/tailwindcss/src/utilities.test.ts` |
| connectivity | 1714 | 270 | 7 | `packages/tailwindcss/theme.css` |
| io | 2119 | 145 | 12 | `integrations/upgrade/index.test.ts` |
| crypto | 4 | 4 | 0 | `scripts/version-packages.mjs` |
| ipc | 13 | 11 | 0 | `integrations/oxide/workers.test.ts` |
| time | 22 | 13 | 0 | `integrations/utils.ts` |
| serialization | 54 | 23 | 0 | `integrations/upgrade/index.test.ts` |
| regex | 153 | 63 | 1 | `integrations/utils.ts` |
| events | 182 | 40 | 0 | `integrations/upgrade/index.test.ts` |
| tests | 5029 | 158 | 15 | `packages/tailwindcss/src/utilities.test.ts` |
| docs | 754 | 94 | 3 | `packages/tailwindcss/src/utilities.ts` |
| debt | 354 | 68 | 1 | `packages/tailwindcss/src/compat/plugin-api.test.ts` |
| mutation | 24398 | 340 | 58 | `packages/tailwindcss/src/utilities.test.ts` |
| dead_code | 80 | 34 | 0 | `crates/oxide/src/extractor/mod.rs` |
| credential | 16 | 7 | 0 | `integrations/cli/index.test.ts` |
| threat | 12 | 5 | 0 | `crates/oxide/tests/scanner.rs` |
| ml_ai | 43 | 13 | 0 | `packages/tailwindcss/src/index.test.ts` |
| ui | 179 | 33 | 0 | `crates/oxide/src/fixtures/example.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `integrations/upgrade/index.test.ts` (Hits: 146)
- `integrations/cli/index.test.ts` (Hits: 144)
- `crates/oxide/src/fixtures/example.html` (Hits: 140)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **design-system.ts** (`packages/tailwindcss/src/design-system.ts`) — 54 inbound connections
2. **utils.ts** (`integrations/utils.ts`) — 39 inbound connections
3. **ast.ts** (`packages/tailwindcss/src/ast.ts`) — 35 inbound connections
4. **utilities.css** (`packages/tailwindcss/utilities.css`) — 32 inbound connections
5. **plugin-api.ts** (`packages/tailwindcss/src/compat/plugin-api.ts`) — 30 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.test.ts** (`integrations/upgrade/index.test.ts`) — 50 outbound dependencies
2. **mod.rs** (`crates/oxide/src/scanner/mod.rs`) — 35 outbound dependencies
3. **mod.rs** (`crates/oxide/src/extractor/mod.rs`) — 27 outbound dependencies
4. **mod.rs** (`crates/oxide/src/extractor/pre_processors/mod.rs`) — 26 outbound dependencies
5. **migrate.ts** (`packages/@tailwindcss-upgrade/src/codemods/template/migrate.ts`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `createUtilities` **(Many-Argument Workhorses)** (@ `packages/tailwindcss/src/utilities.ts`) -> Impact: **1088.2** | LOC: 5641
- `optimizeAst` **(Many-Argument Workhorses)** (@ `packages/tailwindcss/src/ast.ts`) -> Impact: **299.1** | LOC: 461
  * *Intent:* // Optimize the AST for printing where all the special nodes that require custom // handling are handled such that the printing is a 1-to-1 transforma...
- `parse` **(Many-Argument Workhorses)** (@ `packages/tailwindcss/src/css-parser.ts`) -> Impact: **274.2** | LOC: 531
- `parseCss` **(Many-Argument Workhorses)** (@ `packages/tailwindcss/src/index.ts`) -> Impact: **236.2** | LOC: 567
- `buildPluginApi` **(Defensive Guards)** (@ `packages/tailwindcss/src/compat/plugin-api.ts`) -> Impact: **232.4** | LOC: 462
- `createVariants` **(Compute Cores)** (@ `packages/tailwindcss/src/variants.ts`) -> Impact: **223.2** | LOC: 816
- `modernizeArbitraryValuesVariant` **(Many-Argument Workhorses)** (@ `packages/tailwindcss/src/canonicalize-candidates.ts`) -> Impact: **223.0** | LOC: 372
- `transform` **(Many-Argument Workhorses)** (@ `packages/tailwindcss/src/ast.ts`) -> Impact: **180.3** | LOC: 208
- `test` **(Many-Argument Workhorses)** (@ `integrations/utils.ts`) -> Impact: **173.1** | LOC: 377
- `suggest` **(Many-Argument Workhorses)** (@ `packages/tailwindcss/src/utilities.ts`) -> Impact: **168.7** | LOC: 499

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/tailwindcss/src` | 58 | 37749.1 | 32.77% | 2.27% |
| `integrations/vite` | 19 | 5549.64 | 22.09% | 0.0% |
| `packages/tailwindcss/src/compat` | 24 | 5016.28 | 30.15% | 0.0% |
| `crates/node/npm/wasm32-wasi` | 3 | 5002.0 | 0.0% | 0.0% |
| `packages/@tailwindcss-upgrade/src/codemods/template` | 31 | 2282.28 | 26.88% | 0.53% |
| `integrations/upgrade` | 3 | 2222.76 | 22.3% | 0.0% |
| `integrations/postcss` | 8 | 2199.07 | 5.68% | 0.0% |
| `packages/@tailwindcss-upgrade/src/codemods/css` | 26 | 2022.42 | 40.76% | 1.7% |
| `integrations/cli` | 4 | 1812.75 | 19.72% | 0.0% |
| `packages/tailwindcss/src/utils` | 29 | 1266.06 | 28.12% | 2.82% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `crates/oxide/src/extractor/named_variant_machine.rs` -> **98.2626%** Exposure
- `crates/oxide/src/extractor/arbitrary_variable_machine.rs` -> **90.7281%** Exposure
- `crates/oxide/src/extractor/mod.rs` -> **86.4888%** Exposure
- `crates/node/src/lib.rs` -> **84.1131%** Exposure
- `crates/oxide/src/main.rs` -> **81.7574%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/@tailwindcss-cli/src/utils/args.test.ts` -> **100.0%** Exposure
- `packages/@tailwindcss-cli/src/utils/args.ts` -> **100.0%** Exposure
- `packages/@tailwindcss-cli/src/utils/disposables.ts` -> **100.0%** Exposure
- `packages/@tailwindcss-cli/src/utils/format-ns.ts` -> **100.0%** Exposure
- `packages/@tailwindcss-cli/src/utils/renderer.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/tailwindcss/src/compat/plugin-api.test.ts` -> **1** Orphaned Functions | **69** Duplicates
- `packages/tailwindcss/src/utilities.ts` -> **0** Orphaned Functions | **45** Duplicates
- `packages/tailwindcss/src/walk.test.ts` -> **0** Orphaned Functions | **42** Duplicates
- `packages/tailwindcss/src/index.test.ts` -> **0** Orphaned Functions | **27** Duplicates
- `crates/oxide/src/extractor/mod.rs` -> **25** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1063` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/tailwindcss/src/utilities.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.547)
- **Top Global Matches:** file_cluster_13: 5.547, file_cluster_2: 5.583, file_cluster_10: 5.966
- **Magnitude:** 18047.25 | **LOC:** 29983 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (86.0%), Guard Balance (formerly Safety Score) (67.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 759 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 4826
* *State Mutation (weighted view):* 10533
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 8436`, `args: 356`, `func_start: 342`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 10529`, `fragile_debt: 1`
* *Architecture:* `io: 6`, `concurrency: 1031`, `import: 4`
* *Defense:* `safety: 3`, `test: 1039`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` , run, utilities, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/node/npm/wasm32-wasi/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tailwindcss/src/utilities.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.886)
- **Top Global Matches:** file_cluster_4: 7.886, file_cluster_6: 10.06, file_cluster_15: 14.168
- **Magnitude:** 4854.84 | **LOC:** 6690 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **13**; blast radius 5.738; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (93.7%), Complexity Load (formerly Cognitive Load) (75.9%), Guard Balance (formerly Safety Score) (67.8%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createUtilities` **(Many-Argument Workhorses)** (Impact: 1088.2)
  * `suggest` **(Many-Argument Workhorses)** (Impact: 168.7)
  * `createCssUtility` **(Compute Cores)** (Impact: 139.9)
  * `functionalUtility` **(Many-Argument Workhorses)** (Impact: 113.5)
  * `resolveValueFunction` **(Many-Argument Workhorses)** (Impact: 107.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 439 instances
* *State Mutation (weighted view):* 2087
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 797`, `structural_boundaries: 1380`, `args: 463`, `func_start: 126`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1209`, `planned_debt: 1`, `duplicate_logic: 45`
* *Architecture:* `io: 2`, `api: 17`, `import: 14`
* *Defense:* `safety: 50`, `doc: 82`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.738
  * `Choke Point (Betweenness):` 0.002173 | `Ripple Effect (Closeness):` 0.097681
  * `Imports (Out-Degree: 13):` ast, candidate, design-system, feature-flags, theme, compare-breakpoints, default-map, escape...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `integrations/vite/index.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.923)
- **Top Global Matches:** file_cluster_10: 4.923, file_cluster_13: 5.343, file_cluster_2: 5.773
- **Magnitude:** 2917.4 | **LOC:** 1278 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 1.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (46.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.3%), Complexity Load (formerly Cognitive Load) (31.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 46 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 353
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 305`, `args: 48`, `func_start: 15`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `io: 87`, `api: 30`, `concurrency: 123`, `import: 38`
* *Defense:* `safety: 6`, `doc: 13`, `test: 89`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` utils, app, custom-theme.css, imported.css, index.css?raw, index.css?url, index.css, vite...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tailwindcss/src/canonicalize-candidates.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.245)
- **Top Global Matches:** file_cluster_8: 7.245, file_cluster_6: 10.326, file_cluster_4: 18.779
- **Magnitude:** 2196.02 | **LOC:** 2909 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 76.9%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **20**; blast radius 2.253; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (91.3%), Guard Balance (formerly Safety Score) (60.4%), Complexity Load (formerly Cognitive Load) (59.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `modernizeArbitraryValuesVariant` **(Many-Argument Workhorses)** (Impact: 223.0)
  * `collapseCandidates` **(Many-Argument Workhorses)** (Impact: 122.5)
  * `arbitraryUtilities` **(Many-Argument Workhorses)** (Impact: 98.0)
  * `collapseGroup` **(Compute Cores)** (Impact: 86.0)
  * `tryReplacements` **(Many-Argument Workhorses)** (Impact: 82.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 172 instances
* *State Mutation (weighted view):* 520
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 628`, `structural_boundaries: 371`, `args: 123`, `func_start: 62`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 176`, `fragile_debt: 1`
* *Architecture:* `io: 21`, `api: 10`, `import: 22`
* *Defense:* `safety: 67`, `doc: 7`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.253
  * `Choke Point (Betweenness):` 0.006239 | `Ripple Effect (Closeness):` 0.070841
  * `Imports (Out-Degree: 20):` apply, ast, attribute-selector-parser, candidate, canonicalize-calc-expressions, apply-config-to-theme, constant-fold-declaration, design-system...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/tailwindcss/src/index.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.73)
- **Top Global Matches:** file_cluster_10: 7.73, file_cluster_13: 8.217, file_cluster_15: 9.244
- **Magnitude:** 2172.58 | **LOC:** 6301 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (94.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (76.0%), Guard Balance (formerly Safety Score) (52.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadStylesheet` **(Compute Cores)** (Impact: 11.1)
  * `loadStylesheet` **(Annotated & Test Methods)** (Impact: 4.8)
  * `loadStylesheet` **(Annotated & Test Methods)** (Impact: 4.5)
  * `loadStylesheet` **(Parameter Forwarders)** (Impact: 3.3)
  * `module` **(Annotated & Test Methods)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 170 instances
* *Concurrency (weighted view):* 1243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 861`, `args: 294`, `func_start: 229`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 719`, `planned_debt: 1`, `duplicate_logic: 27`
* *Architecture:* `io: 56`, `concurrency: 393`, `import: 7`
* *Defense:* `safety: 20`, `doc: 4`, `test: 422`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` , bar.css, plugin-api, bar.css, baz.css, plugin, run, three.css...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tailwindcss/src/compat/plugin-api.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.65)
- **Top Global Matches:** file_cluster_10: 7.65, file_cluster_13: 8.811, file_cluster_15: 8.898
- **Magnitude:** 1290.46 | **LOC:** 4640 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (50.6%), Mutation Surface (formerly State Flux) (43.4%), Complexity Load (formerly Cognitive Load) (23.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseValue` **(Defensive Guards)** (Impact: 6.0)
  * `sort` **(Compute Cores)** (Impact: 5.5)
  * `sort` **(Compute Cores)** (Impact: 5.5)
  * `run` **(Annotated & Test Methods)** (Impact: 5.0)
  * `run` **(Annotated & Test Methods)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 49 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 532
* *State Mutation (weighted view):* 227
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 700`, `args: 371`, `func_start: 290`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 221`, `duplicate_logic: 69`, `unreferenced_by_name: 1`
* *Architecture:* `io: 94`, `concurrency: 287`, `import: 6`
* *Defense:* `safety: 11`, `test: 197`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .., plugin, run, default-theme, inside.css, plugin-api, vitest, …
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integrations/upgrade/index.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.452)
- **Top Global Matches:** file_cluster_12: 7.452, file_cluster_13: 7.464, file_cluster_15: 7.751
- **Magnitude:** 1070.64 | **LOC:** 3450 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **50**; blast radius 1.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (85.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.0%), Guard Balance (formerly Safety Score) (54.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `withBOM` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 100 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 648
* *State Mutation (weighted view):* 319
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 582`, `args: 55`, `func_start: 44`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 313`
* *Architecture:* `io: 146`, `api: 41`, `concurrency: 148`, `import: 21`
* *Defense:* `safety: 20`, `doc: 47`, `test: 102`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` )
    expect(packageJson.dependencies).toMatchObject(, git, utils, a.1.css, a.1.utilities.1.css, a.1.utilities.css, a.1.utilities.utilities.css, b.1.components.css...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integrations/cli/index.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.536)
- **Top Global Matches:** file_cluster_15: 6.536, file_cluster_13: 6.671, file_cluster_10: 6.794
- **Magnitude:** 1058.84 | **LOC:** 2612 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (85.0%), Guard Balance (formerly Safety Score) (52.7%), Complexity Load (formerly Cognitive Load) (41.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `withBOM` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 119 instances
* *Concurrency (weighted view):* 749
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 360`, `args: 51`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 240`, `fragile_debt: 1`
* *Architecture:* `io: 144`, `api: 22`, `concurrency: 154`, `import: 6`
* *Defense:* `safety: 2`, `doc: 8`, `test: 112`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` utils, custom-theme.css, index.css, :, dedent, node:os, node:path, node:url...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tailwindcss/src/ast.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.34)
- **Top Global Matches:** file_cluster_6: 7.34, file_cluster_8: 11.49, file_cluster_4: 14.262
- **Magnitude:** 997.92 | **LOC:** 934 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **35** in-repo importer(s); it depends on **11**; blast radius 20.916; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.4%), Connectivity (formerly Api Exposure) (75.7%), Guard Balance (formerly Safety Score) (69.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `optimizeAst` **(Many-Argument Workhorses)** (Impact: 299.1)
    * *Intent:* // Optimize the AST for printing where all the special nodes that require custom // handling are han...
  * `transform` **(Many-Argument Workhorses)** (Impact: 180.3)
  * `toCss` **(Many-Argument Workhorses)** (Impact: 58.8)
  * `stringify` **(Many-Argument Workhorses)** (Impact: 54.4)
  * `isVariableUsed` **(Many-Argument Workhorses)** (Impact: 19.2)
    * *Intent:* // Find out if a variable is either used directly or if any of the variables that depend on it are /...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 99 instances
* *State Mutation (weighted view):* 302
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 131`, `args: 30`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 104`
* *Architecture:* `io: 12`, `api: 19`, `import: 10`
* *Defense:* `safety: 15`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 20.916
  * `Choke Point (Betweenness):` 0.006348 | `Ripple Effect (Closeness):` 0.132156
  * `Imports (Out-Degree: 8):` ) 
        parent.push(copy)
      
    

    
    else if (node.kind ===, ) return false
        

        return true
      )

      let layerPropertiesStatement = atRule(, , css-parser, design-system, source, theme, default-map...
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `packages/tailwindcss/src/css-functions.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.799)
- **Top Global Matches:** file_cluster_10: 5.799, file_cluster_11: 7.945, file_cluster_13: 8.023
- **Magnitude:** 961.3 | **LOC:** 1380 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (98.7%), Guard Balance (formerly Safety Score) (52.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadModule` **(I/O & Config Routines)** (Impact: 2.5)
  * `loadModule` **(Callbacks & Closures)** (Impact: 2.1)
  * `loadStylesheet` **(Interface Declarations)** (Impact: 1.6)
  * `loadModule` **(Callbacks & Closures)** (Impact: 1.2)
  * `loadModule` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 115 instances
* *Concurrency (weighted view):* 711
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 203`, `args: 97`, `func_start: 69`
* *Risk/State:* `state_mutation: 215`, `unreferenced_by_name: 1`
* *Architecture:* `io: 12`, `concurrency: 136`, `import: 6`
* *Defense:* `safety: 8`, `test: 145`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` , bar.css, plugin, run, promises, node:path, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integrations/postcss/next.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.343)
- **Top Global Matches:** file_cluster_10: 5.343, file_cluster_13: 5.869, file_cluster_2: 6.625
- **Magnitude:** 906.86 | **LOC:** 487 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (54.8%), Guard Balance (formerly Safety Score) (51.2%), Complexity Load (formerly Cognitive Load) (45.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 26 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 181
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 140`, `args: 40`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 18`
* *Architecture:* `io: 21`, `api: 25`, `concurrency: 51`, `import: 6`
* *Defense:* `doc: 1`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` utils, globals.css, page.module.css, next-pwa, theme, utilities, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integrations/upgrade/js-config.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.165)
- **Top Global Matches:** file_cluster_13: 6.165, file_cluster_12: 6.514, file_cluster_2: 6.588
- **Magnitude:** 871.35 | **LOC:** 2188 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 1.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (93.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (55.7%), Guard Balance (formerly Safety Score) (55.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 51 instances
* *Concurrency (weighted view):* 333
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 300`, `args: 31`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 250`
* *Architecture:* `io: 81`, `api: 32`, `concurrency: 78`, `import: 36`
* *Defense:* `safety: 25`, `doc: 26`, `test: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` utils, base.css, custom-plugin, my-base.css, tailwind.css, utilities.css, typography, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tailwindcss/src/compat/plugin-api.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 11.522)
- **Top Global Matches:** file_cluster_6: 11.522, file_cluster_8: 11.715, file_cluster_4: 18.371
- **Magnitude:** 860.98 | **LOC:** 637 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **19**; blast radius 14.298; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.6%), Connectivity (formerly Api Exposure) (62.6%), Guard Balance (formerly Safety Score) (61.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildPluginApi` **(Defensive Guards)** (Impact: 232.4)
  * `matchUtilities` **(Defensive Guards)** (Impact: 120.6)
  * `matchVariant` **(Defensive Guards)** (Impact: 97.2)
  * `compileFn` **(Defensive Guards)** (Impact: 74.8)
  * `addVariant` **(Compute Cores)** (Impact: 31.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 134`, `args: 54`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 54`
* *Architecture:* `io: 6`, `api: 10`, `import: 19`
* *Defense:* `safety: 39`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.298
  * `Choke Point (Betweenness):` 0.004826 | `Ripple Effect (Closeness):` 0.061794
  * `Imports (Out-Degree: 18):` .., apply, ast, candidate, css-functions, css-parser, design-system, selector-parser...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `integrations/utils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.431)
- **Top Global Matches:** file_cluster_4: 7.431, file_cluster_12: 11.291, file_cluster_15: 11.78
- **Magnitude:** 810.0 | **LOC:** 697 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **39** in-repo importer(s); it depends on **11**; blast radius 25.287; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (94.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.6744% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test` **(Many-Argument Workhorses)** (Impact: 173.1)
  * `spawn` **(Compute Cores)** (Impact: 48.1)
  * `exec` **(Many-Argument Workhorses)** (Impact: 34.2)
  * `parseSourceMap` **(Defensive Guards)** (Impact: 19.2)
  * `overwriteVersionsInPackageJson` **(Compute Cores)** (Impact: 15.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 27 instances
* *Amplified Cascading Flux:* 39 instances
* *Concurrency (weighted view):* 214
* *State Mutation (weighted view):* 130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 174`, `args: 76`, `func_start: 38`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 52`
* *Architecture:* `io: 49`, `api: 17`, `concurrency: 79`, `import: 13`
* *Defense:* `safety: 31`, `doc: 3`, `test: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.287
  * `Choke Point (Betweenness):` 0.000338 | `Ripple Effect (Closeness):` 0.081081
  * `Imports (Out-Degree: 2):` line-table, escape, dedent, fast-glob, node:child_process, promises, node:os, node:path...
  * `Imported By (In-Degree: 39):` (Excluded from Brief to save tokens)

### `packages/tailwindcss/src/variants.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.677)
- **Top Global Matches:** file_cluster_4: 6.677, file_cluster_6: 9.82, file_cluster_12: 12.345
- **Magnitude:** 808.74 | **LOC:** 1236 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **11**; blast radius 4.546; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (77.0%), Guard Balance (formerly Safety Score) (62.8%), Connectivity (formerly Api Exposure) (35.3%)
- **Documentation Coverage:** 95.122% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createVariants` **(Compute Cores)** (Impact: 223.2)
  * `staticVariant` **(Many-Argument Workhorses)** (Impact: 83.9)
  * `compare` **(Compute Cores)** (Impact: 60.6)
  * `fromAst` **(Compute Cores)** (Impact: 19.2)
  * `compoundsWith` **(Compute Cores)** (Impact: 17.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 71 instances
* *State Mutation (weighted view):* 220
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 259`, `args: 97`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 78`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 12`, `import: 11`
* *Defense:* `safety: 9`, `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.546
  * `Choke Point (Betweenness):` 0.000849 | `Ripple Effect (Closeness):` 0.096482
  * `Imports (Out-Degree: 10):` , ast, candidate, compile, design-system, theme, compare-breakpoints, default-map...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/tailwindcss/src/compat/config.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.812)
- **Top Global Matches:** file_cluster_10: 6.812, file_cluster_15: 8.207, file_cluster_13: 8.523
- **Magnitude:** 702.14 | **LOC:** 1774 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.087; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (95.4%), Complexity Load (formerly Cognitive Load) (66.0%), Guard Balance (formerly Safety Score) (52.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadModule` **(Callbacks & Closures)** (Impact: 6.2)
  * `loadModule` **(I/O & Config Routines)** (Impact: 4.2)
  * `loadModule` **(Callbacks & Closures)** (Impact: 2.2)
  * `loadModule` **(Parameter Forwarders)** (Impact: 2.2)
  * `loadModule` **(Parameter Forwarders)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 50 instances
* *Concurrency (weighted view):* 373
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 254`, `args: 95`, `func_start: 83`
* *Risk/State:* `state_mutation: 216`, `duplicate_logic: 10`
* *Architecture:* `io: 43`, `concurrency: 123`, `import: 4`
* *Defense:* `safety: 6`, `test: 113`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., plugin, flatten-color-palette, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/version-packages.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.42)
- **Top Global Matches:** file_cluster_2: 6.42, file_cluster_13: 6.648, file_cluster_10: 6.689
- **Magnitude:** 688.92 | **LOC:** 179 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.087; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (99.4%), Guard Balance (formerly Safety Score) (55.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 57
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 56`, `args: 8`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 11`
* *Architecture:* `io: 17`, `concurrency: 17`, `import: 7`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:child_process, node:crypto, promises, node:os, node:path, node:url, prettier
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tailwindcss/src/css-parser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.035)
- **Top Global Matches:** file_cluster_8: 11.035, file_cluster_3: 13.625, file_cluster_6: 23.444
- **Magnitude:** 631.22 | **LOC:** 718 | **CtrlFlow:** 39.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **3**; blast radius 8.222; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.9%), Guard Balance (formerly Safety Score) (78.1%), Connectivity (formerly Api Exposure) (41.2%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 274.2)
  * `parseString` **(Many-Argument Workhorses)** (Impact: 39.6)
  * `parseAtRule` **(Compute Cores)** (Impact: 10.3)
  * `constructor` **(State Mutators)** (Impact: 6.0)
  * `parseDeclaration` **(Compute Cores)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 282
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 33`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 94`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.222
  * `Choke Point (Betweenness):` 0.000852 | `Ripple Effect (Closeness):` 0.103806
  * `Imports (Out-Degree: 3):` ast, line-table, source
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `packages/tailwindcss/src/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.471)
- **Top Global Matches:** file_cluster_6: 7.471, file_cluster_4: 12.621, file_cluster_8: 14.017
- **Magnitude:** 613.54 | **LOC:** 867 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 2.012; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.2%), Concurrency Surface (formerly Concurrency) (81.2%), Guard Balance (formerly Safety Score) (64.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseCss` **(Many-Argument Workhorses)** (Impact: 236.2)
  * `build` **(Compute Cores)** (Impact: 36.1)
  * `build` **(Compute Cores)** (Impact: 30.1)
  * `parseThemeOptions` **(Compute Cores)** (Impact: 18.0)
  * `onCircularDependency` **(Defensive Guards)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 71 instances
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 115`, `args: 36`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `state_mutation: 76`
* *Architecture:* `io: 38`, `api: 10`, `concurrency: 13`, `import: 23`
* *Defense:* `safety: 12`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.012
  * `Choke Point (Betweenness):` 0.000256 | `Ripple Effect (Closeness):` 0.002079
  * `Imports (Out-Degree: 20):` package.json, apply, ast, at-import, apply-compat-hooks, types, plugin-api, compile...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/@tailwindcss-vite/src/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.369)
- **Top Global Matches:** file_cluster_4: 7.369, file_cluster_6: 8.844, file_cluster_12: 13.56
- **Magnitude:** 566.88 | **LOC:** 632 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 22.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.087; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.3%), Complexity Load (formerly Cognitive Load) (93.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.7%)
- **Documentation Coverage:** 91.1765% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tailwindcss` **(Compute Cores)** (Impact: 103.5)
  * `generate` **(Many-Argument Workhorses)** (Impact: 79.8)
    * *Intent:* // Generate the CSS for the root file. This can return false if the file is // not considered a Tail...
  * `createRoot` **(Defensive Guards)** (Impact: 30.2)
  * `hotUpdate` **(Compute Cores)** (Impact: 29.4)
  * `handler` **(Defensive Guards)** (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 26 instances
* *Concurrency (weighted view):* 87
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 110`, `args: 36`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 32`, `planned_debt: 2`
* *Architecture:* `io: 24`, `api: 7`, `concurrency: 27`, `import: 8`
* *Defense:* `safety: 23`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node, require-cache, oxide, node:fs, promises, node:path, vite
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/@tailwindcss-upgrade/src/codemods/template/migrate.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.202)
- **Top Global Matches:** file_cluster_10: 4.202, file_cluster_13: 5.256, file_cluster_2: 5.783
- **Magnitude:** 556.0 | **LOC:** 130 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 27`, `args: 6`, `func_start: 2`
* *Risk/State:* `state_mutation: 27`, `fragile_debt: 1`
* *Architecture:* `concurrency: 6`, `import: 5`
* *Defense:* `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` default-map, version, migrate, node, tailwindcss, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tailwindcss/src/candidate.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.575)
- **Top Global Matches:** file_cluster_8: 6.575, file_cluster_6: 11.125, file_cluster_4: 19.685
- **Magnitude:** 545.66 | **LOC:** 1179 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **7**; blast radius 10.288; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Connectivity (formerly Api Exposure) (63.4%), Guard Balance (formerly Safety Score) (59.4%), Complexity Load (formerly Cognitive Load) (44.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseCandidate` **(Compute Cores)** (Impact: 94.0)
  * `parseVariant` **(Many-Argument Workhorses)** (Impact: 92.6)
  * `printCandidate` **(Many-Argument Workhorses)** (Impact: 34.2)
  * `recursivelyEscapeUnderscores` **(Compute Cores)** (Impact: 24.8)
  * `printVariant` **(Compute Cores)** (Impact: 20.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 162`, `args: 21`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 54`, `planned_debt: 1`
* *Architecture:* `api: 15`, `import: 7`
* *Defense:* `safety: 15`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.288
  * `Choke Point (Betweenness):` 0.001792 | `Ripple Effect (Closeness):` 0.106261
  * `Imports (Out-Degree: 7):` design-system, decode-arbitrary-value, default-map, is-valid-arbitrary, segment, value-parser, walk
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `integrations/postcss/index.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 4.726)
- **Top Global Matches:** file_cluster_13: 4.726, file_cluster_10: 5.183, file_cluster_2: 5.281
- **Magnitude:** 545.47 | **LOC:** 894 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (59.1%), Guard Balance (formerly Safety Score) (51.9%), Connectivity (formerly Api Exposure) (10.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 43 instances
* *Concurrency (weighted view):* 265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 151`, `args: 23`, `func_start: 15`
* *Risk/State:* `state_mutation: 58`
* *Architecture:* `io: 53`, `api: 37`, `concurrency: 50`, `import: 6`
* *Defense:* `safety: 2`, `doc: 6`, `test: 20`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` utils, custom-theme.css, index.css, tailwind.css, :, postcss, node:path, utilities
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tailwindcss/src/variants.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.526)
- **Top Global Matches:** file_cluster_10: 6.526, file_cluster_13: 7.84, file_cluster_15: 7.952
- **Magnitude:** 520.78 | **LOC:** 2652 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (46.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.5%), Mutation Surface (formerly State Flux) (21.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `permute` **(Parameter Forwarders)** (Impact: 3.3)
  * `permute` **(Parameter Forwarders)** (Impact: 3.3)
  * `loadModule` **(Callbacks & Closures)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 28 instances
* *Concurrency (weighted view):* 398
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 356`, `args: 101`, `func_start: 94`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 67`, `duplicate_logic: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `concurrency: 258`, `import: 5`
* *Defense:* `test: 258`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` plugin, run, variants, dedent, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/oxide/tests/scanner.rs` (RUST) | Magnitude: 212.64 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 1469, generics: 184, structural_boundaries: 166, test: 161
- `packages/@tailwindcss-cli/src/utils/args.ts` (TYPESCRIPT) | Magnitude: 95.58 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 95, structural_boundaries: 41, branch: 40, generics: 13
- `packages/@tailwindcss-upgrade/src/utils/args.ts` (TYPESCRIPT) | Magnitude: 71.86 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 41, branch: 33, generics: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `packages/@tailwindcss-upgrade/src/codemods/template/candidates.test.ts` (TYPESCRIPT) | Magnitude: 54.84 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 18, core_var_decl: 14, design_snake_case: 11
- `packages/@tailwindcss-upgrade/src/codemods/css/migrate-at-layer-utilities.test.ts` (TYPESCRIPT) | Magnitude: 118.8 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 901, decorators: 138, structural_boundaries: 83, concurrency: 68
- `packages/@tailwindcss-node/src/urls.ts` (TYPESCRIPT) | Magnitude: 79.24 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 53, core_var_decl: 33, concurrency: 27
- `packages/tailwindcss/src/prefix.test.ts` (TYPESCRIPT) | Magnitude: 148.86 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 286, structural_boundaries: 42, decorators: 38, state_mutation: 33
- `packages/@tailwindcss-upgrade/src/codemods/template/migrate-modernize-arbitrary-values.test.ts` (TYPESCRIPT) | Magnitude: 18.08 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 22, import: 9, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `integrations/upgrade/index.test.ts` (TYPESCRIPT) | Magnitude: 1070.64 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 2967, structural_boundaries: 582, decorators: 520, state_mutation: 313
- `crates/oxide/src/scanner/init_tracing.rs` (RUST) | Magnitude: 28.24 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 18, args: 10, core_var_decl: 8
- `packages/@tailwindcss-upgrade/src/codemods/template/migrate.ts` (TYPESCRIPT) | Magnitude: 70.04 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 52, import: 21, concurrency: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `integrations/vite/multi-root.test.ts` (TYPESCRIPT) | Magnitude: 151.08 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 149, structural_boundaries: 41, core_var_decl: 17, design_snake_case: 17
- `packages/@tailwindcss-upgrade/src/codemods/template/migrate-automatic-var-injection.test.ts` (TYPESCRIPT) | Magnitude: 135.28 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: state_mutation: 90, indent_spaces: 42, structural_boundaries: 12, safety: 4
- `integrations/vite/html-style-blocks.test.ts` (TYPESCRIPT) | Magnitude: 41.24 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 11, io: 3, concurrency: 3
- `packages/tailwindcss/src/utilities.test.ts` (TYPESCRIPT) | Magnitude: 18047.25 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 25435, state_mutation: 10529, structural_boundaries: 8436, decorators: 1670
- `packages/@tailwindcss-upgrade/src/codemods/template/migrate-legacy-classes.test.ts` (TYPESCRIPT) | Magnitude: 36.0 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 9, import: 4, concurrency: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/@tailwindcss-upgrade/src/codemods/template/migrate-handle-empty-arbitrary-values.ts` (TYPESCRIPT) | Magnitude: 8.54 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, branch: 2, import: 2
- `packages/@tailwindcss-upgrade/src/utils/package-version.ts` (TYPESCRIPT) | Magnitude: 13.46 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 12, safety: 4, io: 4
- `packages/@tailwindcss-upgrade/src/utils/splice-changes-into-string.ts` (TYPESCRIPT) | Magnitude: 30.96 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 19, state_mutation: 8, structural_boundaries: 7, core_var_decl: 5
- `packages/tailwindcss/tests/ui.spec.ts` (TYPESCRIPT) | Magnitude: 423.08 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 1552, structural_boundaries: 376, concurrency: 262, test: 169

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `crates/oxide/src/lib.rs` (RUST) | Magnitude: 26.22 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 11, api: 11, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `integrations/postcss/source.test.ts` (TYPESCRIPT) | Magnitude: 308.88 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 683, structural_boundaries: 138, state_mutation: 76, concurrency: 60
- `packages/tailwindcss/src/compat/legacy-utilities.test.ts` (TYPESCRIPT) | Magnitude: 214.9 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 326, state_mutation: 57, structural_boundaries: 48, test: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/tailwindcss/src/compat/plugin-api.ts` (TYPESCRIPT) | Magnitude: 860.98 | Delta: **0.193** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 461, branch: 183, structural_boundaries: 134, core_var_decl: 75

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/tailwindcss/src/utilities.ts` -> Churn: **93.69%** | Cog Load: 75.9183% | Debt: 66.084%
- `packages/tailwindcss/src/canonicalize-candidates.ts` -> Churn: **91.31%** | Cog Load: 59.7141% | Debt: 8.1471%
- `packages/@tailwindcss-vite/src/index.ts` -> Churn: **79.66%** | Cog Load: 93.4248% | Debt: 9.2815%
- `integrations/utils.ts` -> Churn: **55.68%** | Cog Load: 94.6783% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/tailwindcss/src/compat/plugin-api.test.ts` -> **Adam Wathan** (100.0% isolated ownership) | Magnitude: 1290.46
- `integrations/postcss/next.test.ts` -> **xibeiyoumian** (100.0% isolated ownership) | Magnitude: 906.86
- `packages/tailwindcss/src/compat/plugin-api.ts` -> **Adam Wathan** (100.0% isolated ownership) | Magnitude: 860.98
- `packages/tailwindcss/src/variants.ts` -> **Robin Malfait** (100.0% isolated ownership) | Magnitude: 808.74
- `packages/tailwindcss/src/compat/config.test.ts` -> **Jordan Pittman** (100.0% isolated ownership) | Magnitude: 702.14

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/tailwindcss/src/design-system.ts` -> **Severity: 1.269** (Bridge: 0.0132 * Flux: 95.9359%)
- `packages/tailwindcss/src/intellisense.ts` -> **Severity: 0.638** (Bridge: 0.0064 * Flux: 100.0%)
- `packages/tailwindcss/src/ast.ts` -> **Severity: 0.635** (Bridge: 0.0063 * Flux: 100.0%)
- `packages/tailwindcss/src/canonicalize-candidates.ts` -> **Severity: 0.624** (Bridge: 0.0062 * Flux: 99.976%)
- `packages/tailwindcss/src/compat/plugin-api.ts` -> **Severity: 0.483** (Bridge: 0.0048 * Flux: 99.9926%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/tailwindcss/src/ast.ts` -> **Severity: 9.173** (Embedded: 0.1322 * Error Risk: 69.4075%)
- `packages/tailwindcss/src/utils/segment.ts` -> **Severity: 8.39** (Embedded: 0.1164 * Error Risk: 72.0636%)
- `packages/tailwindcss/src/utils/escape.ts` -> **Severity: 8.353** (Embedded: 0.1374 * Error Risk: 60.8027%)
- `packages/tailwindcss/src/utils/default-map.ts` -> **Severity: 8.338** (Embedded: 0.1482 * Error Risk: 56.2528%)
- `packages/tailwindcss/src/walk.ts` -> **Severity: 8.285** (Embedded: 0.1312 * Error Risk: 63.1656%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `integrations/utils.ts` -> **Severity: 2469.893** (Blast Radius: 25.287 * Doc Risk: 97.6744%)
- `packages/tailwindcss/src/design-system.ts` -> **Severity: 2370.9** (Blast Radius: 23.709 * Doc Risk: 100.0%)
- `packages/tailwindcss/src/ast.ts` -> **Severity: 2091.6** (Blast Radius: 20.916 * Doc Risk: 100.0%)
- `packages/tailwindcss/src/utils/escape.ts` -> **Severity: 1959.3** (Blast Radius: 19.593 * Doc Risk: 100.0%)
- `packages/tailwindcss/src/walk.ts` -> **Severity: 1636.3** (Blast Radius: 16.363 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 153 literal sites + 2 sites through wrappers = 155

- `never` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/tailwindcss/src/candidate.ts`
- `never` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/tailwindcss/src/utils/decode-arbitrary-value.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 5744 call pairs -- scoped 30.8%, unique 0.0%, ambiguous 8.8%, external 60.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 3952 | 32.3% | 0.0% | 12.6% | 55.1% |
| rust | 1782 | 27.7% | 0.0% | 0.4% | 71.9% |
| javascript | 10 | 10.0% | 0.0% | 30.0% | 60.0% |

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
