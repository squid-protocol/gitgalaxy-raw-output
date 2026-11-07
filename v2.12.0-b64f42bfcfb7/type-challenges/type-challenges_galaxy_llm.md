# ARCHITECTURAL_BRIEF: type-challenges
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/type-challenges/type-challenges.git` |
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
- **Scope:** 1069 analyzed artifact(s), 6677 LOC.
- **Load-bearing artifact:** `scripts/locales.ts` -- 12 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `scripts/generate-play.ts` -- pulls in 11 dependencies, the widest assembly point in the scan.
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
| Total Artifacts | 1088 |
| Analyzed Artifacts (Scanned) | 1069 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 19 |
| Total LOC | 6677 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 98.3% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3109 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3519 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6143 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 415 | 187 | 38.8% |
| TYPESCRIPT | 397 | 4917 | 37.1% |
| YAML | 241 | 1378 | 22.5% |
| JSON | 9 | 166 | 0.8% |
| PLAINTEXT | 4 | 1 | 0.4% |
| JAVASCRIPT | 1 | 23 | 0.1% |
| XML | 1 | 0 | 0.1% |
| SHELL | 1 | 5 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 1068 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 84%, Declarative / Non-Code 14%, Compute Cores Files 0%, Parameter Forwarders Files 0%, Callbacks & Closures Files 0%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 650 | 60.8% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 416 | 38.9% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 19*

**Composition by Extension & Reason:**
- `.ts`: 2x Excluded (Saturation: Line 8 exceeds 500 chars), 1x Excluded (Saturation: Line 29 exceeds 500 chars), 1x Packed Payload Guard (Impossible Density: 3.95 hits/line)
- `.svg`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (Massive Static Asset Blob: 3209 LOC)
- `.toml`: 1x Unsupported Format (.toml)
- `.html`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.8 | 1.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 17.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 98.7 | 1.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.3 | 2.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 82.1 | 0.9 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.6 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 19 | 6 | 0 | `questions/00925-extreme-assert-array-index/test-cases.ts` |
| cleanup | 0 | 0 | 0 | - |
| guards | 133 | 36 | 0 | `questions/00472-hard-tuple-to-enum-object/test-cases.ts` |
| danger | 296 | 209 | 1 | `questions/21220-medium-permutations-of-tuple/test-cases.ts` |
| concurrency | 99 | 13 | 0 | `scripts/loader.ts` |
| connectivity | 76 | 23 | 0 | `scripts/toUrl.ts` |
| io | 65 | 7 | 0 | `scripts/generate-play.ts` |
| crypto | 1 | 1 | 0 | `scripts/generate-play.ts` |
| ipc | 0 | 0 | 0 | - |
| time | 2 | 1 | 0 | `scripts/actions/issue-pr.ts` |
| serialization | 10 | 3 | 0 | `scripts/actions/issue-pr.ts` |
| regex | 18 | 5 | 0 | `scripts/actions/issue-pr.ts` |
| events | 25 | 6 | 0 | `eslint.config.js` |
| tests | 17 | 5 | 0 | `questions/33345-extreme-dynamic-route/test-cases.ts` |
| docs | 406 | 396 | 1 | `questions/00697-extreme-tag/test-cases.ts` |
| debt | 34 | 9 | 0 | `questions/33345-extreme-dynamic-route/test-cases.ts` |
| mutation | 778 | 224 | 1 | `scripts/actions/issue-pr.ts` |
| dead_code | 17 | 13 | 0 | `questions/00006-hard-simple-vue/test-cases.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 7 | 4 | 0 | `questions/00006-hard-simple-vue/test-cases.ts` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/generate-play.ts` (Hits: 21)
- `scripts/loader.ts` (Hits: 14)
- `scripts/toUrl.ts` (Hits: 11)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **locales.ts** (`scripts/locales.ts`) — 12 inbound connections
2. **types.ts** (`scripts/types.ts`) — 11 inbound connections
3. **TODOs.md** (`TODOs.md`) — 5 inbound connections
4. **loader.ts** (`scripts/loader.ts`) — 5 inbound connections
5. **toUrl.ts** (`scripts/toUrl.ts`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **generate-play.ts** (`scripts/generate-play.ts`) — 11 outbound dependencies
2. **issue-pr.ts** (`scripts/actions/issue-pr.ts`) — 9 outbound dependencies
3. **formatToCode.ts** (`scripts/actions/utils/formatToCode.ts`) — 7 outbound dependencies
4. **translate.ts** (`scripts/translate.ts`) — 7 outbound dependencies
5. **build.ts** (`scripts/build.ts`) — 6 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `action` **(Many-Argument Workhorses)** (@ `scripts/actions/issue-pr.ts`) -> Impact: **46.1** | LOC: 122
- `action` **(Many-Argument Workhorses)** (@ `scripts/actions/toggle-pr-with-issue.ts`) -> Impact: **27.1** | LOC: 62
- `action` **(Many-Argument Workhorses)** (@ `scripts/actions/labeling.ts`) -> Impact: **25.0** | LOC: 60
- `generatePlayground` **(I/O & Config Routines)** (@ `scripts/generate-play.ts`) -> Impact: **22.3** | LOC: 86
- `resolveInfo` **(Defensive Guards)** (@ `scripts/loader.ts`) -> Impact: **17.9** | LOC: 11
- `toQuizREADME` **(Compute Cores)** (@ `scripts/toUrl.ts`) -> Impact: **12.3** | LOC: 6
- `translateMarkdown` **(Compute Cores)** (@ `scripts/translate.ts`) -> Impact: **11.4** | LOC: 29
- `loadInfo` **(Generic / Templated Code)** (@ `scripts/loader.ts`) -> Impact: **9.6** | LOC: 22
- `updateComment` **(Many-Argument Workhorses)** (@ `scripts/actions/issue-pr.ts`) -> Impact: **9.4** | LOC: 29
- `toRawREADME` **(Compute Cores)** (@ `scripts/toUrl.ts`) -> Impact: **9.0** | LOC: 7

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 13 | 5074.48 | 0.62% | 0.0% |
| `scripts` | 12 | 482.68 | 35.29% | 0.0% |
| `scripts/actions` | 4 | 259.24 | 34.5% | 3.37% |
| `questions/00925-extreme-assert-array-index` | 4 | 69.98 | 15.73% | 9.44% |
| `questions/00697-extreme-tag` | 4 | 66.68 | 0.0% | 0.0% |
| `questions/00002-medium-return-type` | 10 | 65.18 | 0.69% | 0.0% |
| `questions/00009-medium-deep-readonly` | 9 | 56.22 | 0.0% | 0.0% |
| `questions/00012-medium-chainable-options` | 8 | 55.9 | 0.0% | 0.0% |
| `questions/00003-medium-omit` | 9 | 55.72 | 0.0% | 6.92% |
| `questions/00008-medium-readonly-2` | 9 | 55.66 | 0.53% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `questions/33345-extreme-dynamic-route/test-cases.ts` -> **98.7249%** Exposure
- `questions/00006-hard-simple-vue/test-cases.ts` -> **97.0688%** Exposure
- `questions/00213-hard-vue-basic-props/test-cases.ts` -> **95.9316%** Exposure
- `questions/00004-easy-pick/test-cases.ts` -> **81.7574%** Exposure
- `questions/00003-medium-omit/test-cases.ts` -> **62.2459%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `questions/00925-extreme-assert-array-index/test-cases.ts` -> **100.0%** Exposure
- `scripts/build.ts` -> **100.0%** Exposure
- `scripts/loader.ts` -> **99.9958%** Exposure
- `questions/00697-extreme-tag/test-cases.ts` -> **99.4438%** Exposure
- `scripts/generate-play.ts` -> **99.3621%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `questions/00006-hard-simple-vue/test-cases.ts` -> **3** Orphaned Functions | **0** Duplicates
- `questions/00213-hard-vue-basic-props/test-cases.ts` -> **3** Orphaned Functions | **0** Duplicates
- `questions/00006-hard-simple-vue/template.ts` -> **1** Orphaned Functions | **0** Duplicates
- `questions/00017-hard-currying-1/template.ts` -> **1** Orphaned Functions | **0** Duplicates
- `questions/00020-medium-promise-all/template.ts` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `223` packages imported that bypass the Zero-Trust whitelist.

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/actions/issue-pr.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.604)
- **Top Global Matches:** file_cluster_4: 7.604, file_cluster_6: 8.249, file_cluster_12: 14.109
- **Magnitude:** 187.58 | **LOC:** 273 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 1.068; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (94.9%), Complexity Load (formerly Cognitive Load) (79.2%), Guard Balance (formerly Safety Score) (59.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `action` **(Many-Argument Workhorses)** (Impact: 46.1)
  * `updateComment` **(Many-Argument Workhorses)** (Impact: 9.4)
  * `createMessageBody` **(Compute Cores)** (Impact: 7.7)
  * `getCodeBlock` **(Compute Cores)** (Impact: 6.5)
  * `getCommentRange` **(Compute Cores)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 41`, `args: 11`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 19`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 4`, `concurrency: 13`, `import: 9`
* *Defense:* `safety: 5`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.068
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000935
  * `Imports (Out-Degree: 5):` locales, readme, toUrl, types, resolve, formatToCode, octokit-create-pull-request, js-yaml...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scripts/generate-play.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.933)
- **Top Global Matches:** file_cluster_6: 8.933, file_cluster_4: 12.237, file_cluster_8: 16.654
- **Magnitude:** 126.0 | **LOC:** 181 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.913; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.4%), Complexity Load (formerly Cognitive Load) (96.2%), Guard Balance (formerly Safety Score) (59.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generatePlayground` **(I/O & Config Routines)** (Impact: 22.3)
  * `takeSnapshot` **(Compute Cores)** (Impact: 6.8)
  * `isQuizWritable` **(Compute Cores)** (Impact: 6.3)
  * `calculateOverridableFiles` **(Compute Cores)** (Impact: 5.7)
  * `readPlaygroundCache` **(Defensive Guards)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 49
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 40`, `args: 12`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 9`
* *Architecture:* `io: 21`, `concurrency: 14`, `import: 11`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` issue-pr, formatToCode, loader, locales, types, ansis, fs-extra, node:crypto...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/loader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.935)
- **Top Global Matches:** file_cluster_5: 7.935, file_cluster_12: 8.659, file_cluster_7: 10.609
- **Magnitude:** 114.56 | **LOC:** 118 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **6**; blast radius 2.387; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.8%), Connectivity (formerly Api Exposure) (65.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveInfo` **(Defensive Guards)** (Impact: 17.9)
  * `loadInfo` **(Generic / Templated Code)** (Impact: 9.6)
  * `loadQuiz` **(Generic / Templated Code)** (Impact: 4.8)
  * `loadQuizByNo` **(Parameter Forwarders)** (Impact: 3.4)
  * `loadFile` **(Parameter Forwarders)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 43`, `args: 11`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 15`
* *Architecture:* `io: 14`, `api: 9`, `concurrency: 20`, `import: 6`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.387
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006236
  * `Imports (Out-Degree: 2):` locales, types, fast-glob, fs-extra, js-yaml, node:path
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `scripts/toUrl.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.43)
- **Top Global Matches:** file_cluster_15: 5.43, file_cluster_16: 7.963, file_cluster_11: 8.051
- **Magnitude:** 84.26 | **LOC:** 86 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 1.905; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (82.1%), Complexity Load (formerly Cognitive Load) (18.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `toQuizREADME` **(Compute Cores)** (Impact: 12.3)
  * `toRawREADME` **(Compute Cores)** (Impact: 9.0)
  * `toNearborREADME` **(Compute Cores)** (Impact: 8.9)
  * `toQuestionsRawREADME` **(Compute Cores)** (Impact: 5.9)
  * `toShareAnswerFull` **(Parameter Forwarders)** (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 44`, `args: 13`, `func_start: 12`
* *Risk/State:* None
* *Architecture:* `io: 11`, `api: 15`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.905
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.00421
  * `Imports (Out-Degree: 3):` loader, locales, types, lz-string
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `scripts/translate.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.228)
- **Top Global Matches:** file_cluster_15: 7.228, file_cluster_10: 8.309, file_cluster_13: 8.906
- **Magnitude:** 61.12 | **LOC:** 74 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 1.3; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (95.9%), Mutation Surface (formerly State Flux) (93.1%), Guard Balance (formerly Safety Score) (54.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `translateMarkdown` **(Compute Cores)** (Impact: 11.4)
  * `translateAllQuizzes` **(Compute Cores)** (Impact: 7.6)
  * `translateQuiz` **(Compute Cores)** (Impact: 4.7)
  * `translateQuizByNo` **(Parameter Forwarders)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 30`, `args: 7`, `func_start: 4`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 7`, `api: 4`, `concurrency: 11`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.3
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000935
  * `Imports (Out-Degree: 4):` loader, locales, types, resolve, google-translate-api, fs-extra, node:path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `questions/00925-extreme-assert-array-index/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.335)
- **Top Global Matches:** file_cluster_2: 4.335, file_cluster_17: 5.628, file_cluster_15: 6.722
- **Magnitude:** 52.06 | **LOC:** 101 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (72.8%), Complexity Load (formerly Cognitive Load) (62.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* None
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/build.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.169)
- **Top Global Matches:** file_cluster_9: 8.169, file_cluster_10: 13.301, file_cluster_15: 13.323
- **Magnitude:** 50.02 | **LOC:** 55 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.913; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (98.2%), Guard Balance (formerly Safety Score) (67.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build` **(I/O & Config Routines)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 15`, `args: 5`, `func_start: 1`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `io: 9`, `api: 1`, `concurrency: 5`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` formatToCode, loader, locales, toUrl, fs-extra, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00697-extreme-tag/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.633)
- **Top Global Matches:** file_cluster_5: 7.633, file_cluster_7: 10.666, file_cluster_12: 11.488
- **Magnitude:** 39.32 | **LOC:** 162 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.913; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Guard Balance (formerly Safety Score) (64.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 22`
* *Architecture:* `import: 1`
* *Defense:* `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/actions/toggle-pr-with-issue.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.882)
- **Top Global Matches:** file_cluster_9: 7.882, file_cluster_12: 12.123, file_cluster_16: 13.619
- **Magnitude:** 33.02 | **LOC:** 67 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.913; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (90.6%), Guard Balance (formerly Safety Score) (50.7%), Complexity Load (formerly Cognitive Load) (25.4%), Connectivity (formerly Api Exposure) (3.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `action` **(Many-Argument Workhorses)** (Impact: 27.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 12`, `args: 3`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 1`, `concurrency: 4`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/actions/labeling.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.297)
- **Top Global Matches:** file_cluster_9: 7.297, file_cluster_12: 11.983, file_cluster_16: 13.248
- **Magnitude:** 32.08 | **LOC:** 65 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.913; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (95.5%), Guard Balance (formerly Safety Score) (49.3%), Complexity Load (formerly Cognitive Load) (25.5%), Connectivity (formerly Api Exposure) (3.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `action` **(Many-Argument Workhorses)** (Impact: 25.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 12`, `args: 2`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 1`, `concurrency: 5`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00020-medium-promise-all/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.417)
- **Top Global Matches:** file_cluster_0: 8.417, file_cluster_13: 11.371, file_cluster_2: 12.102
- **Magnitude:** 25.26 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.913; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `concurrency: 10`, `import: 1`
* *Defense:* `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00189-easy-awaited/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.556)
- **Top Global Matches:** file_cluster_5: 9.556, file_cluster_7: 11.432, file_cluster_14: 11.777
- **Magnitude:** 22.26 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.913; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.6%), Guard Balance (formerly Safety Score) (54.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 1`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `concurrency: 7`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `eslint.config.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.788)
- **Top Global Matches:** file_cluster_2: 4.788, file_cluster_13: 5.905, file_cluster_17: 6.331
- **Magnitude:** 19.46 | **LOC:** 25 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.913; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.1%), Mutation Surface (formerly State Flux) (50.0%), Complexity Load (formerly Cognitive Load) (8.0%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` eslint-config
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/03326-medium-bem-style-string/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.533)
- **Top Global Matches:** file_cluster_0: 6.533, file_cluster_13: 9.829, file_cluster_2: 10.822
- **Magnitude:** 18.12 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.913; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.2%), Guard Balance (formerly Safety Score) (53.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/locales.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.025)
- **Top Global Matches:** file_cluster_15: 7.025, file_cluster_0: 8.16, file_cluster_11: 9.174
- **Magnitude:** 17.82 | **LOC:** 27 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **5**; blast radius 5.927; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (74.9%), Complexity Load (formerly Cognitive Load) (6.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `t` **(Compute Cores)** (Impact: 7.2)
  * `f` **(Parameter Forwarders)** (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 10`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.927
  * `Choke Point (Betweenness):` 5.3e-05 | `Ripple Effect (Closeness):` 0.011225
  * `Imports (Out-Degree: 5):` en.json, ja.json, ko.json, pt-BR.json, zh-CN.json
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `questions/26401-medium-json-schema-to-typescript/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 4.751)
- **Top Global Matches:** file_cluster_0: 4.751, file_cluster_2: 6.86, file_cluster_13: 7.362
- **Magnitude:** 17.68 | **LOC:** 161 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.913; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (5.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 78`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/14080-hard-fizzbuzz/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.735)
- **Top Global Matches:** file_cluster_2: 3.735, file_cluster_17: 5.616, file_cluster_13: 5.816
- **Magnitude:** 17.58 | **LOC:** 131 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.913; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00553-hard-deep-object-to-unique/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.419)
- **Top Global Matches:** file_cluster_0: 6.419, file_cluster_13: 10.281, file_cluster_2: 10.715
- **Magnitude:** 17.44 | **LOC:** 29 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.913; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.3%), Mutation Surface (formerly State Flux) (31.0%), Complexity Load (formerly Cognitive Load) (5.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 12`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/31997-extreme-parameter-intersection/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 4.718)
- **Top Global Matches:** file_cluster_0: 4.718, file_cluster_2: 6.623, file_cluster_13: 7.259
- **Magnitude:** 17.24 | **LOC:** 127 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.913; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (6.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 31`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/31797-hard-sudoku/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 4.893)
- **Top Global Matches:** file_cluster_0: 4.893, file_cluster_2: 5.653, file_cluster_13: 6.629
- **Magnitude:** 16.98 | **LOC:** 109 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.913; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00869-extreme-distributeunions/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 4.753)
- **Top Global Matches:** file_cluster_0: 4.753, file_cluster_2: 7.175, file_cluster_13: 7.626
- **Magnitude:** 16.54 | **LOC:** 83 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.913; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 18`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/33345-extreme-dynamic-route/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.292)
- **Top Global Matches:** file_cluster_0: 6.292, file_cluster_2: 8.941, file_cluster_13: 9.345
- **Magnitude:** 16.46 | **LOC:** 75 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.913; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.7%), Complexity Load (formerly Cognitive Load) (5.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 7`
* *Risk/State:* `planned_debt: 10`
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/09160-hard-assign/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 4.987)
- **Top Global Matches:** file_cluster_0: 4.987, file_cluster_2: 5.187, file_cluster_13: 5.973
- **Magnitude:** 16.42 | **LOC:** 93 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.913; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 19`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/17973-medium-deepmutable/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 6.52)
- **Top Global Matches:** file_cluster_17: 6.52, file_cluster_2: 6.661, file_cluster_13: 6.788
- **Magnitude:** 16.38 | **LOC:** 76 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.913; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 2`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `questions/04518-medium-fill/template.ts` (TYPESCRIPT) | Magnitude: 13.12 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, core_var_decl: 2, design_snake_case: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `questions/16259-medium-to-primitive/test-cases.ts` (TYPESCRIPT) | Magnitude: 15.56 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 7, core_var_decl: 3, immutability_locks: 2
- `questions/03376-medium-inordertraversal/template.ts` (TYPESCRIPT) | Magnitude: 13.12 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 3, class_start: 1, safety_bypasses: 1
- `questions/00274-extreme-integers-comparator/template.ts` (TYPESCRIPT) | Magnitude: 13.12 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, class_start: 1, safety_bypasses: 1
- `questions/00006-hard-simple-vue/test-cases.ts` (TYPESCRIPT) | Magnitude: 6.94 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 6, args: 5, func_start: 5

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `questions/00003-medium-omit/test-cases.ts` -> Churn: **100.0%** | Cog Load: 0.0% | Debt: 62.2459%

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `scripts/types.ts` -> **Severity: 0.55** (Embedded: 0.0105 * Error Risk: 52.1415%)
- `scripts/loader.ts` -> **Severity: 0.393** (Embedded: 0.0062 * Error Risk: 62.971%)
- `scripts/actions/issue-pr.ts` -> **Severity: 0.056** (Embedded: 0.0009 * Error Risk: 59.4898%)
- `scripts/translate.ts` -> **Severity: 0.051** (Embedded: 0.0009 * Error Risk: 54.5923%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scripts/locales.ts` -> **Severity: 592.7** (Blast Radius: 5.927 * Doc Risk: 100.0%)
- `scripts/loader.ts` -> **Severity: 238.7** (Blast Radius: 2.387 * Doc Risk: 100.0%)
- `scripts/toUrl.ts` -> **Severity: 190.5** (Blast Radius: 1.905 * Doc Risk: 100.0%)
- `scripts/actions/utils/formatToCode.ts` -> **Severity: 144.3** (Blast Radius: 1.443 * Doc Risk: 100.0%)
- `scripts/utils/resolve.ts` -> **Severity: 137.1** (Blast Radius: 1.371 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 189 call pairs -- scoped 20.1%, unique 0.0%, ambiguous 0.5%, external 79.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 186 | 20.4% | 0.0% | 0.5% | 79.0% |
| shell | 3 | 0.0% | 0.0% | 0.0% | 100.0% |

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
