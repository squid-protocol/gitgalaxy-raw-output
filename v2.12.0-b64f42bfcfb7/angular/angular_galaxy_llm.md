# ARCHITECTURAL_BRIEF: angular
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/angular/angular.git` |
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
- **Scope:** 3924 analyzed artifact(s), 211420 LOC.
- **Load-bearing artifact:** `devtools/projects/protocol/index.ts` -- 119 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `adev/src/content/reference/errors/overview.md` -- pulls in 48 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `.github/actions/deploy-docs-site/main.js` at magnitude 17997.68 (structural weight, not risk).
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
| Total Artifacts | 9855 |
| Analyzed Artifacts (Scanned) | 3924 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5931 |
| Total LOC | 211420 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 39.8% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.9011 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1079 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.8687 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 280 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 1688 | 101115 | 43.0% |
| MARKDOWN | 506 | 0 | 12.9% |
| CSS | 442 | 26656 | 11.3% |
| HTML | 422 | 21219 | 10.8% |
| JSON | 329 | 22293 | 8.4% |
| PLAINTEXT | 271 | 1 | 6.9% |
| XML | 87 | 167 | 2.2% |
| JAVASCRIPT | 80 | 36112 | 2.0% |
| YAML | 50 | 1403 | 1.3% |
| PYTHON | 32 | 1593 | 0.8% |
| SHELL | 10 | 679 | 0.3% |
| NIX | 7 | 182 | 0.2% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 3921 |
| utf-8 | bom | 2 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 52%, Declarative / Non-Code 25%, State Mutators Files 4%, Callbacks & Closures Files 4%, Large Core Modules (2) 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3117 | 79.4% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 776 | 19.8% |
| Static: Minified & Vendor Opaque Mass | 30 | 0.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5931*

**Composition by Extension & Reason:**
- `.ts`: 3790x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 13 exceeds 500 chars), 1x Unsupported Format (.undeterminable)
- `.js`: 815x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bazel`: 329x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 142x Excluded (Unsupported Extension: '.bazel')
- `.png`: 180x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 165x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Massive Static Asset Blob: 7696 LOC), 1x Excluded (Static Asset Blob without Intent: 1290 LOC)
- `.md`: 122x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Machine-Generated Source Code Signature: 28 LOC), 2x Excluded (Machine-Generated Source Code Signature: 50 LOC)
- `no_extension`: 57x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 19x Unsupported Format (.undeterminable)
- `.gif`: 36x Excluded (Explicitly Denied Extension: '.gif')
- `.ico`: 33x Excluded (Explicitly Denied Extension: '.ico')
- `.html`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 34 exceeds 500 chars), 1x Excluded (Saturation: Line 53 exceeds 500 chars)
- `.yaml`: 3x Zero-Density Threshold (LOC: 82, Signals: 0), 2x Excluded (Massive Static Asset Blob: 8745 LOC), 2x Excluded (Massive Static Asset Blob: 8722 LOC)
- `.jpg`: 16x Excluded (Explicitly Denied Extension: '.jpg')
- `.mjs`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.scss`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bzl`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 91.5 | 17.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.6 | 3.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 10.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 19.5 | 1.9 | 0.1 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 88.4 | 5.2 | 3.9 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 25.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 538 | 192 | 0 | `.github/actions/deploy-docs-site/main.js` |
| cleanup | 116 | 75 | 0 | `.github/actions/deploy-docs-site/main.js` |
| guards | 8587 | 987 | 4 | `.github/actions/deploy-docs-site/main.js` |
| danger | 2665 | 440 | 1 | `.github/actions/deploy-docs-site/main.js` |
| concurrency | 4118 | 429 | 1 | `.github/actions/deploy-docs-site/main.js` |
| connectivity | 5980 | 1796 | 4 | `.github/actions/deploy-docs-site/main.js` |
| io | 2737 | 519 | 1 | `adev/src/app/routing/navigation-entries/index.ts` |
| crypto | 1 | 1 | 0 | `modules/utilities/perf_util.ts` |
| ipc | 121 | 44 | 0 | `devtools/projects/ng-devtools/src/lib/shared/signal-graph/devtools-signal-graph.ts` |
| time | 225 | 104 | 0 | `.github/actions/deploy-docs-site/main.js` |
| serialization | 179 | 65 | 0 | `.github/actions/deploy-docs-site/main.js` |
| regex | 615 | 128 | 0 | `.github/actions/deploy-docs-site/main.js` |
| events | 1527 | 468 | 1 | `.github/actions/deploy-docs-site/main.js` |
| tests | 4356 | 275 | 0 | `vscode-ng-language-service/integration/lsp/ivy_spec.ts` |
| docs | 2540 | 1034 | 1 | `.github/actions/deploy-docs-site/main.js` |
| debt | 1069 | 302 | 0 | `.github/actions/deploy-docs-site/main.js` |
| mutation | 33085 | 1810 | 15 | `.github/actions/deploy-docs-site/main.js` |
| dead_code | 379 | 180 | 0 | `.github/actions/deploy-docs-site/main.js` |
| credential | 27 | 23 | 0 | `vscode-ng-language-service/server/src/tests/text_render_spec.ts` |
| threat | 9 | 3 | 0 | `.github/actions/deploy-docs-site/main.js` |
| ml_ai | 656 | 58 | 0 | `integration/cli-hello-world-lazy/src/app/app.component.html` |
| ui | 3491 | 1090 | 1 | `adev/src/app/features/home/home.component.scss` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `adev/src/app/routing/navigation-entries/index.ts` (Hits: 314)
- `.github/actions/deploy-docs-site/main.js` (Hits: 130)
- `devtools/projects/ng-devtools/src/lib/devtools-tabs/injector-tree/injector-tree-fns.spec.ts` (Hits: 95)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.ts** (`devtools/projects/protocol/index.ts`) — 119 inbound connections
2. **renderables.mts** (`adev/shared-docs/pipeline/api-gen/rendering/entities/renderables.mts`) — 42 inbound connections
3. **index.ts** (`adev/shared-docs/interfaces/index.ts`) — 35 inbound connections
4. **parse.mts** (`adev/shared-docs/pipeline/shared/marked/parse.mts`) — 24 inbound connections
5. **index.ts** (`modules/utilities/index.ts`) — 24 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **overview.md** (`adev/src/content/reference/errors/overview.md`) — 48 outbound dependencies
2. **SKILL.md** (`skills/dev-skills/angular-developer/SKILL.md`) — 35 outbound dependencies
3. **include-all.ts** (`integration/typings_test_ts59/include-all.ts`) — 29 outbound dependencies
4. **include-all.ts** (`integration/typings_test_ts60/include-all.ts`) — 29 outbound dependencies
5. **include-all.ts** (`integration/nodenext_resolution/include-all.ts`) — 27 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parse` **(Defensive Guards)** (@ `.github/actions/deploy-docs-site/main.js`) -> Impact: **656.0** | LOC: 787
- `shouldWrapKey` **(Defensive Guards)** (@ `.github/actions/deploy-docs-site/main.js`) -> Impact: **294.1** | LOC: 2347
- `usage` **(Many-Argument Workhorses)** (@ `.github/actions/deploy-docs-site/main.js`) -> Impact: **264.5** | LOC: 509
- `singleQuotedString` **(Many-Argument Workhorses)** (@ `.github/actions/deploy-docs-site/main.js`) -> Impact: **264.2** | LOC: 4625
- `encodeUnreserved` **(Many-Argument Workhorses)** (@ `.github/actions/deploy-docs-site/main.js`) -> Impact: **209.3** | LOC: 4158
- `validation` **(Many-Argument Workhorses)** (@ `.github/actions/deploy-docs-site/main.js`) -> Impact: **187.3** | LOC: 266
- `parse3` **(Many-Argument Workhorses)** (@ `.github/actions/deploy-docs-site/main.js`) -> Impact: **146.6** | LOC: 231
- `exports` **(Many-Argument Workhorses)** (@ `.github/actions/deploy-docs-site/main.js`) -> Impact: **121.9** | LOC: 63
- `foldFlowLines` **(Many-Argument Workhorses)** (@ `.github/actions/deploy-docs-site/main.js`) -> Impact: **114.8** | LOC: 104
- `option` **(Defensive Guards)** (@ `.github/actions/deploy-docs-site/main.js`) -> Impact: **93.7** | LOC: 108

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `.github/actions/deploy-docs-site` | 4 | 18044.54 | 17.63% | 3.33% |
| `__monolith__` | 20 | 5421.65 | 4.87% | 4.25% |
| `adev/src/app/editor` | 26 | 1723.39 | 22.51% | 7.53% |
| `vscode-ng-language-service/server/src` | 13 | 1100.56 | 24.82% | 3.04% |
| `devtools/projects/ng-devtools-backend/src/lib` | 16 | 987.82 | 14.26% | 20.35% |
| `vscode-ng-language-service/server/src/handlers` | 15 | 942.78 | 16.85% | 1.11% |
| `vscode-ng-language-service/client/src` | 7 | 842.54 | 28.95% | 8.15% |
| `devtools/projects/ng-devtools/src/lib/shared/split` | 9 | 738.36 | 15.8% | 13.77% |
| `adev/src/app/features/update` | 5 | 734.06 | 24.89% | 1.86% |
| `devtools/projects/shell-browser/src/app` | 20 | 691.57 | 15.9% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/ISSUE_TEMPLATE/4-devtools.yaml` -> **100.0%** Exposure
- `.github/ISSUE_TEMPLATE/5-vscode.yaml` -> **100.0%** Exposure
- `devtools/src/app/demo-app/todo/home/todos.service.ts` -> **100.0%** Exposure
- `modules/playground/src/todo/main.ts` -> **100.0%** Exposure
- `.github/workflows/pr.yml` -> **99.9999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.agent/skills/pr_review/scripts/submit_pr_review.sh` -> **100.0%** Exposure
- `scripts/ci/publish-snapshot-build-artifacts.sh` -> **100.0%** Exposure
- `adev/shared-docs/components/breadcrumb/breadcrumb.component.ts` -> **100.0%** Exposure
- `adev/shared-docs/components/cookie-popup/cookie-popup.component.ts` -> **100.0%** Exposure
- `adev/shared-docs/components/tab-group/tab-group.component.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `.github/actions/deploy-docs-site/main.js` -> **57** Orphaned Functions | **29** Duplicates
- `.github/workflows/ci.yml` -> **0** Orphaned Functions | **9** Duplicates
- `adev/src/content/tutorials/playground/3-minigame/src/main.ts` -> **9** Orphaned Functions | **0** Duplicates
- `adev/shared-docs/pipeline/api-gen/rendering/entities/categorization.mts` -> **8** Orphaned Functions | **0** Duplicates
- `modules/playground/src/todo/main.ts` -> **8** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `adev/src/app/environment.ts` -> **99.9997%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `71` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4455` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.github/actions/deploy-docs-site/main.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 12.68)
- **Top Global Matches:** file_cluster_4: 12.68, file_cluster_12: 14.368, file_cluster_15: 15.513
- **Magnitude:** 17997.68 | **LOC:** 33597 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 77.8%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **18**; blast radius 0.875; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.2%), Complexity Load (formerly Cognitive Load) (67.5%), Guard Balance (formerly Safety Score) (54.0%)
- **Documentation Coverage:** 93.6301% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Defensive Guards)** (Impact: 656.0)
  * `shouldWrapKey` **(Defensive Guards)** (Impact: 294.1)
  * `usage` **(Many-Argument Workhorses)** (Impact: 264.5)
  * `singleQuotedString` **(Many-Argument Workhorses)** (Impact: 264.2)
  * `encodeUnreserved` **(Many-Argument Workhorses)** (Impact: 209.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 116 instances
* *Amplified Cascading Flux:* 1505 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 820
* *State Mutation (weighted view):* 7371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3317`, `structural_boundaries: 7060`, `args: 2675`, `func_start: 1846`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 506`, `high_risk_execution: 5`, `state_mutation: 4361`, `planned_debt: 3`, `fragile_debt: 5`, `duplicate_logic: 29`, `unreferenced_by_name: 57`
* *Architecture:* `io: 130`, `api: 338`, `concurrency: 240`, `import: 56`
* *Defense:* `safety: 3086`, `doc: 228`, `test: 11`, `sync_locks: 13`, `immutability_locks: 16`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002158
  * `Imports (Out-Degree: 0):` assert, child_process, fs, promises, module, node:child_process, node:fs, promises...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vscode-ng-language-service/client/src/client.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.403)
- **Top Global Matches:** file_cluster_4: 7.403, file_cluster_16: 8.021, file_cluster_15: 8.368
- **Magnitude:** 550.36 | **LOC:** 812 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 45.5%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 0.273; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.6%)
- **Documentation Coverage:** 79.5918% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Compute Cores)** (Impact: 52.1)
  * `constructArgs` **(I/O & Config Routines)** (Impact: 20.1)
    * *Intent:* /** * Construct the arguments that's used to spawn the server process. */
  * `provideCompletionItem` **(Many-Argument Workhorses)** (Impact: 19.1)
  * `provideHover` **(Many-Argument Workhorses)** (Impact: 15.1)
  * `setAngularVersionAndShowMultipleVersionsWarning` **(Many-Argument Workhorses)** (Impact: 13.9)
    * *Intent:* // TODO(atscott): Now that language service resolves the version of Angular local to the project, do...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 44 instances
* *Concurrency (weighted view):* 100
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 125`, `args: 43`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 63`, `planned_debt: 1`
* *Architecture:* `io: 10`, `api: 20`, `concurrency: 60`, `import: 8`
* *Defense:* `safety: 12`, `doc: 8`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.273
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000509
  * `Imports (Out-Degree: 4):` notifications, requests, resolver, embedded_support, node:fs, node:path, vscode, node
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `integration/animations/e2e/src/animations.e2e-spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.089)
- **Top Global Matches:** file_cluster_12: 8.089, file_cluster_10: 8.429, file_cluster_7: 8.902
- **Magnitude:** 524.72 | **LOC:** 137 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.166; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.4%), Guard Balance (formerly Safety Score) (50.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 26 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 184
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 51`, `args: 15`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 8`
* *Architecture:* `io: 1`, `concurrency: 54`, `import: 1`
* *Defense:* `safety: 3`, `test: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` puppeteer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `adev/src/app/editor/embedded-tutorial-manager.service.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.312)
- **Top Global Matches:** file_cluster_10: 5.312, file_cluster_2: 6.532, file_cluster_13: 6.73
- **Magnitude:** 506.93 | **LOC:** 501 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.166; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (71.3%), Guard Balance (formerly Safety Score) (48.9%), Complexity Load (formerly Cognitive Load) (38.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Concurrency (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 55`, `args: 20`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 33`
* *Architecture:* `io: 10`, `concurrency: 36`, `import: 5`
* *Defense:* `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` constants, embedded-tutorial-manager.service, testing, docs, api
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vscode-ng-language-service/integration/lsp/ivy_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.161)
- **Top Global Matches:** file_cluster_7: 8.161, file_cluster_5: 9.362, file_cluster_12: 9.691
- **Magnitude:** 498.02 | **LOC:** 2757 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.166; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (73.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.6%), Complexity Load (formerly Cognitive Load) (26.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getDiagnosticsForFile` **(Callbacks & Closures)** (Impact: 4.2)
  * `initServer` **(Generic / Templated Code)** (Impact: 2.0)
  * `onSuggestStrictMode` **(Callbacks & Closures)** (Impact: 1.8)
  * `filter` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 33 instances
* *Concurrency (weighted view):* 371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 607`, `args: 274`, `func_start: 88`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 196`, `state_mutation: 43`
* *Architecture:* `io: 8`, `api: 29`, `concurrency: 206`, `import: 36`
* *Defense:* `safety: 55`, `test: 392`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` notifications, requests, test_constants, test_utils.js, common, core, node:fs, promises...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devtools/projects/ng-devtools/src/lib/shared/split/split.component.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.24)
- **Top Global Matches:** file_cluster_6: 10.24, file_cluster_4: 11.597, file_cluster_12: 16.119
- **Magnitude:** 434.2 | **LOC:** 740 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.166; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (75.4%), Guard Balance (formerly Safety Score) (69.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build` **(Many-Argument Workhorses)** (Impact: 40.7)
  * `dragEvent` **(Compute Cores)** (Impact: 35.7)
  * `startDragging` **(Many-Argument Workhorses)** (Impact: 32.5)
  * `refreshStyleSizes` **(Compute Cores)** (Impact: 31.2)
  * `notify` **(Compute Cores)** (Impact: 25.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 46 instances
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 94`, `args: 56`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 59`, `fragile_debt: 1`
* *Architecture:* `api: 15`, `concurrency: 8`, `import: 7`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 17`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` interface, splitArea.directive, utils, core, rxjs-interop, rxjs, operators
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devtools/projects/ng-devtools-backend/src/lib/component-tree/component-tree.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.747)
- **Top Global Matches:** file_cluster_12: 6.747, file_cluster_5: 8.908, file_cluster_4: 9.254
- **Magnitude:** 418.98 | **LOC:** 818 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **10**; blast radius 0.618; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Connectivity (formerly Api Exposure) (66.7%), Guard Balance (formerly Safety Score) (58.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.4%)
- **Documentation Coverage:** 94.3396% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `serializeProviderRecord` **(Many-Argument Workhorses)** (Impact: 34.5)
  * `getDependenciesForDirective` **(Many-Argument Workhorses)** (Impact: 30.5)
  * `getDirectiveCdStrategy` **(Compute Cores)** (Impact: 18.3)
  * `getDirectiveMetadata` **(Compute Cores)** (Impact: 14.9)
    * *Intent:* // Gets directive metadata. For newer versions of Angular (v12+) it uses // the global `getDirective...
  * `serializeInjector` **(Compute Cores)** (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 172`, `args: 48`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 40`
* *Architecture:* `api: 24`, `import: 10`
* *Defense:* `safety: 26`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.618
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.002545
  * `Imports (Out-Degree: 10):` protocol, index, interfaces, ng-debug-api, property-mutation, state-serializer, utils, core-enums...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `devtools/projects/ng-devtools/src/lib/shared/signals-visualizer/signals-visualizer.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.463)
- **Top Global Matches:** file_cluster_12: 7.463, file_cluster_16: 7.914, file_cluster_4: 8.185
- **Magnitude:** 410.38 | **LOC:** 798 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.201; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (59.8%), Guard Balance (formerly Safety Score) (59.4%)
- **Documentation Coverage:** 72.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateNodes` **(Compute Cores)** (Impact: 40.8)
  * `updateEdges` **(Stateful Encapsulated Methods)** (Impact: 20.7)
  * `getBodyText` **(Compute Cores)** (Impact: 20.5)
  * `highlightDependencies` **(Compute Cores)** (Impact: 17.8)
  * `updateClusters` **(Stateful Encapsulated Methods)** (Impact: 16.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 36 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 94`, `args: 67`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 53`
* *Architecture:* `io: 1`, `api: 12`, `concurrency: 4`, `import: 5`
* *Defense:* `safety: 9`, `doc: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.201
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000254
  * `Imports (Out-Degree: 4):` protocol, signal-graph, visualizer-types, d3, dagre-d3-es
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `adev/src/content/examples/form-validation/e2e/src/app.e2e-spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.13)
- **Top Global Matches:** file_cluster_10: 6.13, file_cluster_11: 8.276, file_cluster_13: 9.535
- **Magnitude:** 396.96 | **LOC:** 247 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.166; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (41.9%), Dead Code Surface (formerly Dead Code) (2.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tests` **(Callbacks & Closures)** (Impact: 5.5)
  * `crossValidationTests` **(Callbacks & Closures)** (Impact: 2.5)
  * `getPage` **(State Mutators)** (Impact: 2.4)
  * `asyncValidationTests` **(Callbacks & Closures)** (Impact: 2.2)
  * `bobTests` **(Callbacks & Closures)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 54 instances
* *Concurrency (weighted view):* 362
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 98`, `args: 35`, `func_start: 29`
* *Risk/State:* `state_mutation: 12`, `dead_code: 1`
* *Architecture:* `concurrency: 92`, `import: 1`
* *Defense:* `safety: 1`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` protractor
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `adev/src/app/editor/node-runtime-sandbox.service.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.396)
- **Top Global Matches:** file_cluster_12: 7.396, file_cluster_5: 7.826, file_cluster_7: 9.168
- **Magnitude:** 396.76 | **LOC:** 534 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **13**; blast radius 0.915; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (86.0%), Mutation Surface (formerly State Flux) (72.5%), Guard Balance (formerly Safety Score) (56.7%)
- **Documentation Coverage:** 45.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `startInteractiveTerminal` **(Stateful Encapsulated Methods)** (Impact: 13.1)
    * *Intent:* /** * Implemented based on: * https://webcontainers.io/tutorial/7-add-interactivity#_2-start-the-she...
  * `init` **(Defensive Guards)** (Impact: 8.9)
  * `initProject` **(Stateful Encapsulated Methods)** (Impact: 8.5)
    * *Intent:* /** * Initialize the WebContainer for an Angular project */
  * `write` **(Defensive Guards)** (Impact: 7.8)
  * `startDevServer` **(Callbacks & Closures)** (Impact: 7.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 213
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 122`, `args: 47`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 15`
* *Architecture:* `io: 15`, `api: 10`, `concurrency: 103`, `import: 13`
* *Defense:* `safety: 16`, `doc: 5`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.003664
  * `Imports (Out-Degree: 8):` alert-manager.service, embedded-tutorial-manager.service, loading-steps, error-filename-handler, node-runtime-errors, node-runtime-state.service, terminal-handler.service, typings-loader.service...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `adev/src/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.872)
- **Top Global Matches:** file_cluster_2: 5.872, file_cluster_13: 6.195, file_cluster_17: 6.51
- **Magnitude:** 385.6 | **LOC:** 109 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.166; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.4%), Guard Balance (formerly Safety Score) (52.5%), Complexity Load (formerly Cognitive Load) (13.9%), Connectivity (formerly Api Exposure) (12.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 3`, `args: 14`, `func_start: 2`, `class_start: 6`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 14`, `api: 16`, `concurrency: 2`
* *Defense:* `safety: 3`, `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` apple-touch-icon.png, favicon-16x16.png, favicon-32x32.png, favicon-48x48.png, favicon.ico, safari-pinned-tab.svg, site.webmanifest, 0...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `adev/shared-docs/pipeline/api-gen/rendering/transforms/code-transforms.mts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.78)
- **Top Global Matches:** file_cluster_4: 6.78, file_cluster_15: 7.803, file_cluster_12: 8.833
- **Magnitude:** 377.52 | **LOC:** 607 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **9**; blast radius 0.602; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.3%), Complexity Load (formerly Cognitive Load) (50.8%), Connectivity (formerly Api Exposure) (44.9%)
- **Documentation Coverage:** 53.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mapDocEntryToCode` **(Compute Cores)** (Impact: 42.9)
  * `appendPrefixAndSuffix` **(Compute Cores)** (Impact: 24.6)
  * `printInitializerFunctionSignatureLine` **(Many-Argument Workhorses)** (Impact: 24.1)
    * *Intent:* /** Prints an initializer function signature into a single line. */
  * `addRenderableCodeToc` **(Compute Cores)** (Impact: 18.9)
    * *Intent:* /** * Based on provided docEntry: * 1. Build metadata * 2. Run syntax highlighting * 3. Generate lis...
  * `groupCodeLines` **(Defensive Guards)** (Impact: 16.9)
    * *Intent:* /** Group overloaded methods */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 103`, `args: 37`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 45`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 6`, `concurrency: 3`, `import: 9`
* *Defense:* `safety: 6`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.602
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.003567
  * `Imports (Out-Degree: 9):` shiki.mjs, entities.mjs, categorization.mjs, renderables.mjs, traits.mjs, shiki.mjs, symbol-context.mjs, format-code.mjs...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `adev/shared-docs/pipeline/shared/marked/extensions/docs-card/docs-card.mts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.136)
- **Top Global Matches:** file_cluster_2: 4.136, file_cluster_17: 5.04, file_cluster_13: 5.659
- **Magnitude:** 334.66 | **LOC:** 152 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.249; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.6%), Mutation Surface (formerly State Flux) (14.5%), Complexity Load (formerly Cognitive Load) (7.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 25`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.249
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.004527
  * `Imports (Out-Degree: 2):` helpers.mjs, renderer.mjs, marked
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `adev/src/app/features/home/animation/animation.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.299)
- **Top Global Matches:** file_cluster_4: 7.299, file_cluster_12: 8.555, file_cluster_16: 8.702
- **Magnitude:** 318.1 | **LOC:** 508 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **6**; blast radius 1.12; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (67.8%), Guard Balance (formerly Safety Score) (67.5%), Complexity Load (formerly Cognitive Load) (43.1%)
- **Documentation Coverage:** 4.6875% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateFrame` **(Compute Cores)** (Impact: 26.8)
    * *Intent:* /** * Update the frame/animation by a given time. * */
  * `validateRules` **(Stateful Encapsulated Methods)** (Impact: 12.9)
    * *Intent:* /** Check whether the start and end styles match and the time frame is correct. */
  * `extractObjects` **(Stateful Encapsulated Methods)** (Impact: 12.4)
    * *Intent:* /** * Extracts all objects (layer elements and layer child elements) by their provided selectors. */
  * `setStyle` **(Stateful Encapsulated Methods)** (Impact: 10.8)
    * *Intent:* /** Set active style. */
  * `define` **(Compute Cores)** (Impact: 10.6)
    * *Intent:* /** * Define the animation. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 44 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 33`, `args: 32`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 51`, `dead_code: 1`
* *Architecture:* `api: 10`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 7`, `doc: 23`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.12
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.002313
  * `Imports (Out-Degree: 8):` animation-layer.directive, calculations, parser, types, types, core
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `vscode-ng-language-service/server/src/session.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.27)
- **Top Global Matches:** file_cluster_16: 6.27, file_cluster_15: 6.271, file_cluster_12: 7.306
- **Magnitude:** 295.4 | **LOC:** 809 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 58.3%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **25**; blast radius 1.22; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (80.1%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (59.9%), Guard Balance (formerly Safety Score) (53.5%)
- **Documentation Coverage:** 55.8824% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onDidOpenTextDocument` **(Defensive Guards)** (Impact: 24.5)
  * `handleProjectServiceEvent` **(Stateful Encapsulated Methods)** (Impact: 19.6)
    * *Intent:* /** * An event handler that gets invoked whenever the program changes and * TS ProjectService sends ...
  * `sendPendingDiagnostics` **(Stateful Encapsulated Methods)** (Impact: 17.8)
    * *Intent:* /** * Execute diagnostics request for each of the specified `files`. */
  * `createProjectService` **(I/O & Config Routines)** (Impact: 12.7)
  * `onDidChangeTextDocument` **(Stateful Encapsulated Methods)** (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 119`, `args: 64`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 28`, `planned_debt: 2`
* *Architecture:* `io: 12`, `api: 7`, `concurrency: 8`, `import: 25`
* *Defense:* `safety: 11`, `doc: 14`, `immutability_locks: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.003817
  * `Imports (Out-Degree: 21):` notifications, requests, config, diagnostic, code_actions, code_lens, completions, definitions...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `adev/src/app/features/update/update.component.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.597)
- **Top Global Matches:** file_cluster_10: 5.597, file_cluster_13: 7.296, file_cluster_0: 8.408
- **Magnitude:** 288.21 | **LOC:** 95 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.166; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (55.5%), Guard Balance (formerly Safety Score) (37.3%), Mutation Surface (formerly State Flux) (25.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 25`, `args: 11`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 2`, `concurrency: 7`, `import: 7`
* *Defense:* `safety: 2`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` recommendations, update.component, http, testing, testing, platform-browser, router
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `adev/src/app/features/update/recommendations.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.313)
- **Top Global Matches:** file_cluster_2: 6.313, file_cluster_12: 6.53, file_cluster_13: 6.646
- **Magnitude:** 284.88 | **LOC:** 2916 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 0.448; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.8%), Connectivity (formerly Api Exposure) (27.4%), Concurrency Surface (formerly Concurrency) (19.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 162`, `args: 3`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 11`, `planned_debt: 1`, `fragile_debt: 4`
* *Architecture:* `io: 84`, `api: 5`, `concurrency: 16`, `import: 15`
* *Defense:* `safety: 72`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.448
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000509
  * `Imports (Out-Degree: 0):` core, platform-browser
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `devtools/projects/ng-devtools-backend/src/lib/hooks/capture.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.308)
- **Top Global Matches:** file_cluster_5: 7.308, file_cluster_12: 7.694, file_cluster_7: 8.886
- **Magnitude:** 270.42 | **LOC:** 388 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.186; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.5%), Complexity Load (formerly Cognitive Load) (58.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `traverse` **(Compute Cores)** (Impact: 17.5)
  * `insertOrMerge` **(Defensive Guards)** (Impact: 17.0)
  * `insertElementProfile` **(Many-Argument Workhorses)** (Impact: 15.6)
  * `lexicographicOrder` **(Compute Cores)** (Impact: 11.2)
  * `onLifecycleHookEnd` **(Many-Argument Workhorses)** (Impact: 10.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 34 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 68`, `args: 28`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 41`, `planned_debt: 1`
* *Architecture:* `api: 10`, `concurrency: 1`, `import: 7`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000763
  * `Imports (Out-Degree: 7):` , protocol, highlighter, interfaces, utils, hooks, profiler
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `devtools/projects/ng-devtools/src/lib/devtools-tabs/injector-tree/injector-tree-fns.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.051)
- **Top Global Matches:** file_cluster_2: 4.051, file_cluster_17: 5.428, file_cluster_13: 6.093
- **Magnitude:** 252.44 | **LOC:** 11684 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.166; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.4%), Mutation Surface (formerly State Flux) (8.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (2.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6274`, `args: 28`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 5`
* *Architecture:* `io: 95`, `import: 2`
* *Defense:* `safety: 5`, `doc: 1`, `test: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` protocol, injector-tree-fns
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `adev/src/content/examples/v21-game-world/e2e/src/app.e2e-spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.987)
- **Top Global Matches:** file_cluster_10: 6.987, file_cluster_11: 7.11, file_cluster_2: 8.815
- **Magnitude:** 246.66 | **LOC:** 173 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.166; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (46.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (6.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getCharacterPosition` **(Interface Declarations)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 28 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 222
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 84`, `args: 9`, `func_start: 7`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `concurrency: 82`, `import: 1`
* *Defense:* `safety: 1`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` protractor
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vscode-ng-language-service/server/src/handlers/document_symbols.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.657)
- **Top Global Matches:** file_cluster_8: 8.657, file_cluster_3: 15.318, file_cluster_6: 21.136
- **Magnitude:** 238.92 | **LOC:** 441 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.215; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.5%), Concurrency Surface (formerly Concurrency) (21.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filterNavigationItem` **(Many-Argument Workhorses)** (Impact: 44.0)
    * *Intent:* /** * Filters a single NavigationTree item. * - If it's a class with a template, return the class no...
  * `scriptElementKindToSymbolKind` **(Compute Cores)** (Impact: 40.9)
    * *Intent:* /** * Maps TypeScript's ScriptElementKind to LSP SymbolKind. */
  * `onDocumentSymbol` **(Many-Argument Workhorses)** (Impact: 33.3)
    * *Intent:* /** * Handles textDocument/documentSymbol requests. * * Returns a hierarchical list of symbols in th...
  * `mergeTemplateSymbolsIntoClass` **(Many-Argument Workhorses)** (Impact: 28.4)
    * *Intent:* /** * Merges Angular template symbols into the component class in the TypeScript symbol tree. * This...
  * `filterNavigationTreeToTemplateClasses` **(Many-Argument Workhorses)** (Impact: 17.6)
    * *Intent:* /** * Filters the TypeScript NavigationTree to only include classes that have Angular templates. * T...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 54`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `api: 1`, `concurrency: 3`, `import: 6`
* *Defense:* `safety: 6`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001974
  * `Imports (Out-Degree: 3):` config, session, utils, api, tsserverlibrary, vscode-languageserver
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `devtools/projects/ng-devtools-backend/src/lib/highlighter.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.664)
- **Top Global Matches:** file_cluster_12: 7.664, file_cluster_9: 8.502, file_cluster_15: 8.687
- **Magnitude:** 238.44 | **LOC:** 285 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **3**; blast radius 0.578; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (77.3%), Guard Balance (formerly Safety Score) (66.5%), Connectivity (formerly Api Exposure) (52.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addHighlightForElement` **(Many-Argument Workhorses)** (Impact: 27.9)
  * `highlightHydrationElement` **(Defensive Guards)** (Impact: 23.2)
  * `positionOverlayContent` **(Many-Argument Workhorses)** (Impact: 22.1)
  * `createOverlaySvgElement` **(Generic / Templated Code)** (Impact: 10.7)
  * `findComponentAndHost` **(Type Conversions)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 94
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 47`, `args: 16`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 46`, `planned_debt: 1`
* *Architecture:* `io: 6`, `api: 7`, `import: 3`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.578
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.002714
  * `Imports (Out-Degree: 2):` protocol, ng-debug-api, core
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `devtools/projects/ng-devtools-backend/src/lib/client-event-subscribers.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.064)
- **Top Global Matches:** file_cluster_5: 8.064, file_cluster_12: 8.076, file_cluster_0: 10.075
- **Magnitude:** 237.58 | **LOC:** 689 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **17**; blast radius 0.397; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (81.7%), Guard Balance (formerly Safety Score) (56.7%), Connectivity (formerly Api Exposure) (46.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.9%)
- **Documentation Coverage:** 94.5946% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getTransferStateCallback` **(Defensive Guards)** (Impact: 17.4)
  * `getLatestComponentExplorerViewCallback` **(Compute Cores)** (Impact: 15.0)
  * `subscribeToClientEvents` **(Compute Cores)** (Impact: 13.4)
  * `getInjectorProvidersCallback` **(Compute Cores)** (Impact: 12.5)
  * `logProvider` **(Compute Cores)** (Impact: 10.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 130`, `args: 56`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 17`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 10`, `import: 17`
* *Defense:* `safety: 8`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.397
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.000905
  * `Imports (Out-Degree: 17):` protocol, shared-utils, component-inspector, component-tree, highlighter, hooks, capture, hooks...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `adev/src/content/examples/animations/e2e/src/app.e2e-spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.566)
- **Top Global Matches:** file_cluster_10: 6.566, file_cluster_15: 8.21, file_cluster_11: 9.141
- **Magnitude:** 228.3 | **LOC:** 308 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.166; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (39.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `newPageSleepFor` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Concurrency (weighted view):* 218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 146`, `args: 44`, `func_start: 17`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `concurrency: 118`, `import: 11`
* *Defense:* `safety: 3`, `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` auto.po, enter-leave.po, filter-stagger.po, hero-groups, open-close.po, querying.po, status-slider.po, toggle.po...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `modules/benchmarks/src/largeform/ng2/init.ts` (TYPESCRIPT) | Magnitude: 10.36 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 4, args: 4, func_start: 4
- `adev/src/app/features/not-found/not-found.ts` (TYPESCRIPT) | Magnitude: 10.58 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 7, decorators: 4, core_var_decl: 4
- `devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/property-pane/property-view/property-view-body/dependency-viewer/dependency-viewer.component.ts` (TYPESCRIPT) | Magnitude: 16.28 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, import: 5, indent_spaces: 5, decorators: 4
- `adev/shared-docs/pipeline/api-gen/rendering/transforms/jsdoc-transforms.mts` (TYPESCRIPT) | Magnitude: 79.14 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 49, core_var_decl: 32, branch: 22
- `devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/property-pane/property-pane-header/property-pane-header.component.ts` (TYPESCRIPT) | Magnitude: 3.5 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 9, import: 7, immutability_locks: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `adev/shared-docs/styles/_split.scss` (CSS) | Magnitude: 0.77 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 20, class_start: 10, closures: 3, immutability_locks: 3
- `devtools/projects/protocol/src/lib/messages.ts` (TYPESCRIPT) | Magnitude: 74.38 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 272, structural_boundaries: 227, api: 52, branch: 50
- `adev/shared-docs/pipeline/tutorials/tutorial_index.mts` (TYPESCRIPT) | Magnitude: 24.24 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 20, concurrency: 14, doc: 9
- `integration/trusted-types/e2e/protractor.conf.js` (JAVASCRIPT) | Magnitude: 11.42 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 38, state_mutation: 7, import: 3, args: 2
- `modules/benchmarks/src/defer/defer.perf-spec.ts` (TYPESCRIPT) | Magnitude: 19.26 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 15, args: 10, func_start: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `modules/playground/src/key_events/main.ts` (TYPESCRIPT) | Magnitude: 29.32 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 18, args: 10, core_var_decl: 10
- `adev/src/app/features/home/home.component.scss` (CSS) | Magnitude: 1.74 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 692, ui_framework: 91, class_start: 77, closures: 21
- `devtools/src/app/demo-app/todo/dialog.component.ts` (TYPESCRIPT) | Magnitude: 6.82 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 10, decorators: 6, api: 5
- `scripts/benchmarks/targets.mts` (TYPESCRIPT) | Magnitude: 65.08 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 16, concurrency: 12, args: 5
- `.github/workflows/ci.yml` (YAML) | Magnitude: 51.3 | Delta: **0.152** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 194, func_start: 37, import: 27, immutability_locks: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/signal-graph-manager/signal-graph-manager.spec.ts` (TYPESCRIPT) | Magnitude: 21.0 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 30, test: 14, args: 12
- `adev/src/app/editor/typings-loader.service.spec.ts` (TYPESCRIPT) | Magnitude: 30.84 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 30, io: 18, args: 13
- `vscode-ng-language-service/server/src/tests/config_spec.ts` (TYPESCRIPT) | Magnitude: 89.62 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 96, core_var_decl: 18, test: 17, design_snake_case: 16
- `adev/src/content/examples/aria/grid/src/table/basic/app/app.ts` (TYPESCRIPT) | Magnitude: 51.14 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 25, args: 17, branch: 8
- `adev/src/content/examples/aria/grid/src/table/retro/app/app.ts` (TYPESCRIPT) | Magnitude: 51.14 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 25, args: 17, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `adev/src/app/app.component.html` (HTML) | Magnitude: 19.56 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 20, core_var_decl: 7, design_snake_case: 7, class_start: 6
- `adev/src/content/tutorials/signals/steps/4-managing-async-data-with-signals/src/app/app.ts` (TYPESCRIPT) | Magnitude: 29.56 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 23, state_mutation: 13, planned_debt: 9, structural_boundaries: 4
- `modules/benchmarks/src/tree/baseline/index.html` (HTML) | Magnitude: 44.01 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 23, core_var_decl: 9, design_snake_case: 9, structural_boundaries: 7
- `adev/src/content/tutorials/first-app/steps/11-details-page/src/app/routes.ts` (TYPESCRIPT) | Magnitude: 16.32 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, import: 3, io: 2
- `adev/src/content/tutorials/first-app/steps/12-forms/src/app/routes.ts` (TYPESCRIPT) | Magnitude: 16.32 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, import: 3, io: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `adev/shared-docs/pipeline/api-gen/manifest/test/manifest.spec.mts` (TYPESCRIPT) | Magnitude: 14.26 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 438, structural_boundaries: 34, decorators: 25, test: 17
- `adev/shared-docs/index.bzl` (PYTHON) | Magnitude: 8.04 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 13, design_snake_case: 13, state_mutation: 5, indent_spaces: 5
- `adev/src/content/examples/animations/src/app/hero-list-enter-leave-page.ts` (TYPESCRIPT) | Magnitude: 5.04 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 6, import: 3, args: 2
- `adev/scripts/routes/generate-routes.mts` (TYPESCRIPT) | Magnitude: 26.7 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 12, args: 8, io: 7
- `devtools/projects/shell-browser/src/app/chrome-application-operations.ts` (TYPESCRIPT) | Magnitude: 53.24 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 25, args: 10, func_start: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `vscode-ng-language-service/server/src/session.ts` (TYPESCRIPT) | Magnitude: 295.4 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 527, structural_boundaries: 119, branch: 86, args: 64
- `devtools/projects/ng-devtools/src/lib/application-services/browser_styles_service.ts` (TYPESCRIPT) | Magnitude: 13.38 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 14, core_var_decl: 10, encapsulation: 8
- `devtools/projects/ng-devtools/src/lib/devtools-tabs/transfer-state/transfer-state.component.ts` (TYPESCRIPT) | Magnitude: 48.18 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 126, structural_boundaries: 43, core_var_decl: 22, args: 20
- `packages.bzl` (PYTHON) | Magnitude: 24.88 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 64, state_mutation: 7, structural_boundaries: 6, core_var_decl: 6
- `devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/directive-forest/tree-node/tree-node.component.ts` (TYPESCRIPT) | Magnitude: 43.14 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 105, core_var_decl: 34, structural_boundaries: 29, encapsulation: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `adev/shared-docs/providers/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `adev/shared-docs/utils/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `adev/shared-docs/index.ts` (TYPESCRIPT) | Magnitude: 22.16 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, api: 8, import: 8
- `adev/shared-docs/interfaces/index.ts` (TYPESCRIPT) | Magnitude: 23.68 | Delta: **0.157** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, api: 9, import: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `adev/shared-docs/pipeline/api-gen/extraction/test/dummy-entry-point/index.mts` (TYPESCRIPT) | Magnitude: 4.58 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, api: 3, core_var_decl: 2, args: 1
- `modules/benchmarks/src/change_detection/transplanted_views/index.html` (HTML) | Magnitude: 46.05 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, core_var_decl: 11, design_snake_case: 11, structural_boundaries: 7
- `modules/benchmarks/src/tree/ng2_switch/index.html` (HTML) | Magnitude: 44.53 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, core_var_decl: 10, design_snake_case: 10, structural_boundaries: 7
- `adev/src/content/examples/service-worker-getting-started/src/index.html` (HTML) | Magnitude: 15.22 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 3, core_var_decl: 3, design_snake_case: 3
- `modules/benchmarks/src/tree/ng2_static/index.html` (HTML) | Magnitude: 45.05 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, core_var_decl: 11, design_snake_case: 11, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `vscode-ng-language-service/server/src/handlers/inlay_hints.ts` (TYPESCRIPT) | Magnitude: 185.34 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 222, branch: 44, core_var_decl: 41, structural_boundaries: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `devtools/projects/ng-devtools-backend/src/lib/client-event-subscribers.ts` (TYPESCRIPT) | Magnitude: 237.58 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 449, structural_boundaries: 130, core_var_decl: 86, branch: 81

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `vscode-ng-language-service/server/src/handlers/completions.ts` (TYPESCRIPT) | Magnitude: 166.94 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 247, branch: 60, structural_boundaries: 55, core_var_decl: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `devtools/projects/ng-devtools-backend/src/lib/hooks/hooks.ts` (TYPESCRIPT) | Magnitude: 19.78 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 12, args: 6, func_start: 6
- `devtools/cypress/integration/track-state.e2e.js` (JAVASCRIPT) | Magnitude: 3.84 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 51, test: 31, args: 10, structural_boundaries: 8
- `vscode-ng-language-service/syntaxes/src/template-tag.ts` (TYPESCRIPT) | Magnitude: 18.94 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 144, safety_bypasses: 4, decorators: 4, bitwise_ops: 4
- `adev/shared-docs/pipeline/api-gen/rendering/shiki/shiki.mts` (TYPESCRIPT) | Magnitude: 15.96 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 8, safety_bypasses: 6, bitwise_ops: 6
- `devtools/tools/defaults.bzl` (PYTHON) | Magnitude: 0.05 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 69, core_var_decl: 47, design_snake_case: 47, state_mutation: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tools/bazel/npm_packages.bzl` (PYTHON) | Magnitude: 0.07 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 119, core_var_decl: 60, design_snake_case: 58, state_mutation: 24
- `adev/src/content/examples/v21-game-world/src/app/app.ts` (TYPESCRIPT) | Magnitude: 225.66 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 598, core_var_decl: 91, branch: 65, structural_boundaries: 63

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/pr.yml` -> Churn: **88.36%** | Cog Load: 7.1649% | Debt: 99.9999%
- `.github/workflows/ci.yml` -> Churn: **87.73%** | Cog Load: 5.7768% | Debt: 99.9842%
- `.github/workflows/perf.yml` -> Churn: **84.48%** | Cog Load: 0.0% | Debt: 99.9447%
- `.github/actions/deploy-docs-site/main.js` -> Churn: **70.23%** | Cog Load: 67.5265% | Debt: 13.3392%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `integration/animations/e2e/src/animations.e2e-spec.ts` -> **Jessica Janiuk** (100.0% isolated ownership) | Magnitude: 524.72
- `devtools/projects/ng-devtools/src/lib/shared/signals-visualizer/signals-visualizer.ts` -> **hawkgs** (100.0% isolated ownership) | Magnitude: 410.38
- `adev/src/app/features/home/animation/animation.ts` -> **khanhkhanhlele** (100.0% isolated ownership) | Magnitude: 318.1
- `devtools/projects/ng-devtools-backend/src/lib/hooks/capture.ts` -> **hawkgs** (100.0% isolated ownership) | Magnitude: 270.42
- `adev/src/content/examples/v21-game-world/e2e/src/app.e2e-spec.ts` -> **Devin Chasanoff** (100.0% isolated ownership) | Magnitude: 246.66

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `adev/shared-docs/pipeline/shared/marked/parse.mts` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 100.0%)
- `adev/shared-docs/pipeline/api-gen/rendering/transforms/jsdoc-transforms.mts` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 77.493%)
- `adev/shared-docs/pipeline/shared/marked/extensions/docs-code/format/index.mts` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `adev/shared-docs/pipeline/shared/marked/renderer.mts` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `adev/shared-docs/pipeline/shared/marked/extensions/docs-code/docs-code.mts` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `devtools/projects/protocol/src/lib/priority-aware-message-bus.ts` -> **Severity: 0.813** (Embedded: 0.0133 * Error Risk: 61.2467%)
- `devtools/projects/protocol/src/lib/message-bus.ts` -> **Severity: 0.694** (Embedded: 0.0133 * Error Risk: 51.9989%)
- `devtools/projects/protocol/src/lib/messages.ts` -> **Severity: 0.679** (Embedded: 0.0133 * Error Risk: 50.8996%)
- `modules/benchmarks/src/util.ts` -> **Severity: 0.535** (Embedded: 0.0068 * Error Risk: 78.6111%)
- `adev/shared-docs/pipeline/shared/shiki.mts` -> **Severity: 0.402** (Embedded: 0.0069 * Error Risk: 58.3381%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `devtools/projects/protocol/src/lib/message-bus.ts` -> **Severity: 433.575** (Blast Radius: 5.781 * Doc Risk: 75.0%)
- `devtools/projects/protocol/src/lib/priority-aware-message-bus.ts` -> **Severity: 409.0** (Blast Radius: 4.09 * Doc Risk: 100.0%)
- `modules/benchmarks/src/util.ts` -> **Severity: 349.558** (Blast Radius: 4.766 * Doc Risk: 73.344%)
- `modules/utilities/e2e_util.ts` -> **Severity: 179.6** (Blast Radius: 3.592 * Doc Risk: 50.0%)
- `adev/shared-docs/pipeline/shared/linking.mts` -> **Severity: 157.857** (Blast Radius: 2.21 * Doc Risk: 71.4286%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 567 literal sites + 8 sites through wrappers = 575
- **`panics_and_aborts`:** 550 literal sites + 2 sites through wrappers = 552

- `logToConsole` (function, debug_prints, primitive): 4 call sites in 1 files -- `devtools/projects/ng-devtools-backend/src/lib/component-tree/component-tree.ts`
- `argumentTypeError` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `.github/actions/deploy-docs-site/main.js`
- `execTimed` (function, debug_prints, primitive): 2 call sites in 1 files -- `modules/benchmarks/src/expanding_rows/benchmark.ts`
- `createReleaseBranch` (function, debug_prints, primitive): 1 call sites in 1 files -- `vscode-ng-language-service/tools/release.mts`
- `installDependencies` (function, debug_prints, primitive): 1 call sites in 1 files -- `vscode-ng-language-service/tools/release.mts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 12815 call pairs -- scoped 24.3%, unique 0.0%, ambiguous 13.7%, external 61.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 8818 | 27.8% | 0.0% | 15.6% | 56.6% |
| javascript | 3589 | 17.8% | 0.0% | 10.3% | 71.8% |
| python | 308 | 3.2% | 0.0% | 2.3% | 94.5% |
| shell | 100 | 20.0% | 1.0% | 0.0% | 79.0% |

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
