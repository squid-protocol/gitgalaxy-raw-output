# ARCHITECTURAL_BRIEF: desktop
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/desktop/desktop.git` |
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
- **Scope:** 1264 analyzed artifact(s), 133466 LOC.
- **Load-bearing artifact:** `app/src/models/repository.ts` -- 213 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `app/src/ui/app.tsx` -- pulls in 153 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `app/.npmrc` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 2390 |
| Analyzed Artifacts (Scanned) | 1264 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1126 |
| Total LOC | 133466 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 52.9% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4523 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1708 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 20.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 6.2964 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 94 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 988 | 120446 | 78.2% |
| CSS | 176 | 10894 | 13.9% |
| MARKDOWN | 33 | 0 | 2.6% |
| XML | 24 | 25 | 1.9% |
| YAML | 12 | 620 | 0.9% |
| SHELL | 10 | 220 | 0.8% |
| JAVASCRIPT | 9 | 1005 | 0.7% |
| PLAINTEXT | 5 | 1 | 0.4% |
| JSON | 5 | 240 | 0.4% |
| HTML | 1 | 10 | 0.1% |
| BATCH | 1 | 5 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 1263 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 21%, Data / Markup / Trivial 17%, Callbacks & Closures Files 14%, Large Core Modules (3) 11%, Large Core Modules (2) 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1221 | 96.6% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 37 | 2.9% |
| Static: Minified & Vendor Opaque Mass | 5 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1126*

**Composition by Extension & Reason:**
- `no_extension`: 390x Unsupported Format (.undeterminable), 354x Excluded (Binary Format Detected), 195x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 62x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 82 exceeds 500 chars)
- `.json`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 4781 LOC)
- `.png`: 11x Excluded (Explicitly Denied Extension: '.png')
- `.h`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 27 exceeds 500 chars)
- `.lock`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.lock')
- `.gyp`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.plist`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cpp`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.car`: 2x Excluded (Unsupported Extension: '.car')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.0 | 4.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 25.6 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.9 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 21.6 | 20.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 19.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.9 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 77.9 | 2.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 37.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 799 | 443 | 2 | `app/test/unit/text-token-parser-test.ts` |
| cleanup | 137 | 74 | 0 | `app/src/ui/lib/tooltip.tsx` |
| guards | 9550 | 673 | 19 | `app/src/lib/stores/app-store.ts` |
| danger | 687 | 256 | 2 | `app/src/lib/api.ts` |
| concurrency | 6395 | 409 | 10 | `app/src/lib/stores/app-store.ts` |
| connectivity | 4834 | 884 | 7 | `app/styles/_variables.scss` |
| io | 3040 | 393 | 7 | `app/test/unit/git/commit-test.ts` |
| crypto | 7 | 6 | 0 | `eslint-rules/tests/insecure-random.test.js` |
| ipc | 24 | 21 | 0 | `app/src/lib/highlighter/worker.ts` |
| time | 205 | 83 | 0 | `app/src/lib/stores/helpers/repository-indicator-updater.ts` |
| serialization | 46 | 27 | 0 | `app/test/unit/accounts-store-test.ts` |
| regex | 209 | 93 | 0 | `app/src/lib/hooks/shell-escape.ts` |
| events | 781 | 196 | 1 | `app/src/main-process/main.ts` |
| tests | 1751 | 131 | 2 | `app/test/unit/git/diff-test.ts` |
| docs | 5103 | 688 | 10 | `app/src/ui/dispatcher/dispatcher.ts` |
| debt | 220 | 85 | 0 | `.github/skills/update-git/trigger-workflow.sh` |
| mutation | 23991 | 901 | 44 | `app/src/lib/stores/app-store.ts` |
| dead_code | 59 | 24 | 0 | `app/src/highlighter/globals.d.ts` |
| credential | 4 | 3 | 0 | `.github/skills/update-git/trigger-workflow.sh` |
| threat | 2 | 2 | 0 | `app/app-info.ts` |
| ml_ai | 126 | 51 | 0 | `app/src/lib/format-relative.ts` |
| ui | 9012 | 454 | 19 | `app/src/ui/app.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.9166**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `app/test/unit/git/commit-test.ts` (Hits: 93)
- `app/src/ui/add-repository/create-repository.tsx` (Hits: 89)
- `app/src/lib/shells/win32.ts` (Hits: 87)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **repository.ts** (`app/src/models/repository.ts`) — 213 inbound connections
2. **index.ts** (`app/src/ui/dialog/index.ts`) — 101 inbound connections
3. **index.ts** (`app/src/ui/dispatcher/index.ts`) — 100 inbound connections
4. **api.ts** (`app/src/lib/api.ts`) — 94 inbound connections
5. **index.ts** (`app/src/ui/octicons/index.ts`) — 94 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **app.tsx** (`app/src/ui/app.tsx`) — 153 outbound dependencies
2. **app-store.ts** (`app/src/lib/stores/app-store.ts`) — 115 outbound dependencies
3. **_ui.scss** (`app/styles/_ui.scss`) — 113 outbound dependencies
4. **index.ts** (`app/src/highlighter/index.ts`) — 60 outbound dependencies
5. **dispatcher.ts** (`app/src/ui/dispatcher/dispatcher.ts`) — 60 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parse` **(Many-Argument Workhorses)** (@ `app/src/lib/actions-log-parser/action-log-parser.ts`) -> Impact: **258.9** | LOC: 567
  * *Intent:* /** * Converts the content to HTML with appropriate styles, escapes content to prevent XSS * */
- `popupContent` **(Many-Argument Workhorses)** (@ `app/src/ui/app.tsx`) -> Impact: **236.4** | LOC: 1159
- `showTestUI` **(Many-Argument Workhorses)** (@ `app/src/ui/lib/test-ui-components/test-ui-components.ts`) -> Impact: **171.0** | LOC: 468
- `getStates` **(Compute Cores)** (@ `app/src/lib/actions-log-parser/action-log-parser.ts`) -> Impact: **136.9** | LOC: 192
  * *Intent:* /** * Parses the content into ANSII states * */
- `buildDefaultMenu` **(Many-Argument Workhorses)** (@ `app/src/main-process/menu/build-default-menu.ts`) -> Impact: **126.9** | LOC: 558
- `getDescriptionForError` **(Stateful Encapsulated Methods)** (@ `app/src/lib/git/core.ts`) -> Impact: **116.1** | LOC: 140
- `expandTextDiffHunk` **(Many-Argument Workhorses)** (@ `app/src/ui/diff/text-diff-expansion.ts`) -> Impact: **94.8** | LOC: 231
  * *Intent:* /** * Expands a hunk in a text diff. Returns the new diff with the expanded hunk, * or undefined if anything went wrong. * */
- `parseLines` **(Compute Cores)** (@ `app/src/lib/actions-log-parser/action-log-parser.ts`) -> Impact: **81.9** | LOC: 224
  * *Intent:* /** * Parses the content into lines with nodes * */
- `getRepositoryMenuBuilder` **(Compute Cores)** (@ `app/src/lib/menu-update.ts`) -> Impact: **80.5** | LOC: 225
- `onMenuEvent` **(Compute Cores)** (@ `app/src/ui/app.tsx`) -> Impact: **79.4** | LOC: 117

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `app/src/lib/stores` | 24 | 7733.58 | 31.61% | 4.82% |
| `app` | 8 | 5109.66 | 5.02% | 0.0% |
| `app/src/lib/git` | 57 | 5107.34 | 39.28% | 1.79% |
| `app/src/lib` | 102 | 4436.69 | 14.23% | 4.62% |
| `app/src/ui/lib` | 79 | 4079.0 | 11.66% | 1.65% |
| `app/test/unit/git` | 35 | 3746.07 | 19.62% | 0.0% |
| `app/test/unit` | 70 | 2634.06 | 3.7% | 0.0% |
| `app/src/ui` | 22 | 2344.9 | 17.09% | 1.59% |
| `app/src/ui/diff` | 16 | 2040.94 | 8.8% | 0.0% |
| `app/src/ui/dispatcher` | 3 | 1997.48 | 11.7% | 2.74% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `app/src/lib/stores/base-store.ts` -> **100.0%** Exposure
- `app/src/lib/globals.d.ts` -> **99.993%** Exposure
- `app/src/highlighter/globals.d.ts` -> **99.9188%** Exposure
- `app/styles/ui/_scroll.scss` -> **99.821%** Exposure
- `.github/ISSUE_TEMPLATE/bug_report.yaml` -> **98.6851%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/skills/update-git/trigger-workflow.sh` -> **100.0%** Exposure
- `app/src/lib/actions-log-parser/action-log-parser.ts` -> **100.0%** Exposure
- `app/src/lib/create-terminal-stream.ts` -> **100.0%** Exposure
- `app/src/lib/fix-emoji-spacing.ts` -> **100.0%** Exposure
- `app/src/lib/git/git-delimiter-parser.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `app/src/highlighter/globals.d.ts` -> **20** Orphaned Functions | **0** Duplicates
- `app/src/lib/globals.d.ts` -> **7** Orphaned Functions | **0** Duplicates
- `.github/workflows/ci.yml` -> **0** Orphaned Functions | **4** Duplicates
- `app/src/lib/stores/base-store.ts` -> **0** Orphaned Functions | **4** Duplicates
- `app/src/ui/history/commit-list.tsx` -> **0** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `app/app-info.ts` -> **100.0%** Exposure
- `app/src/ui/diff/diff-helpers.tsx` -> **60.18%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1444` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `app/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/lib/stores/app-store.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.536)
- **Top Global Matches:** file_cluster_15: 7.536, file_cluster_16: 7.658, file_cluster_10: 8.577
- **Magnitude:** 4237.62 | **LOC:** 8730 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 37.5%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **115**; blast radius 0.629; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.9%), Complexity Load (formerly Cognitive Load) (69.6%)
- **Documentation Coverage:** 60.2763% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_recordCommitStats` **(Many-Argument Workhorses)** (Impact: 49.0)
  * `_undoMultiCommitOperation` **(Many-Argument Workhorses)** (Impact: 44.1)
    * *Intent:* /** This shouldn't be called directly. See `Dispatcher`. */
  * `_mergeBranch` **(Many-Argument Workhorses)** (Impact: 42.0)
  * `onGitStoreUpdated` **(Many-Argument Workhorses)** (Impact: 40.1)
  * `initializeMultiCommitOperationIfConflictsFound` **(Many-Argument Workhorses)** (Impact: 33.4)
    * *Intent:* /** * This method is to initialize a multi commit operation state on app load * if conflicts are fou...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 95 instances
* *Amplified Cascading Flux:* 134 instances
* *Concurrency (weighted view):* 1135
* *State Mutation (weighted view):* 496
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 767`, `structural_boundaries: 1270`, `args: 594`, `func_start: 356`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 228`, `planned_debt: 4`
* *Architecture:* `io: 61`, `api: 241`, `concurrency: 660`, `import: 115`
* *Defense:* `safety: 120`, `doc: 144`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.629
  * `Choke Point (Betweenness):` 0.033653 | `Ripple Effect (Closeness):` 0.089799
  * `Imports (Out-Degree: 134):` , remote-parsing, account, app-menu, author, banner, branch, branches-tab...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `app/src/ui/dispatcher/dispatcher.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.682)
- **Top Global Matches:** file_cluster_15: 6.682, file_cluster_16: 8.013, file_cluster_0: 8.112
- **Magnitude:** 1778.94 | **LOC:** 4083 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **88** in-repo importer(s); it depends on **60**; blast radius 5.696; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.6%)
- **Documentation Coverage:** 21.9512% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rebase` **(Many-Argument Workhorses)** (Impact: 37.4)
    * *Intent:* /** Starts a rebase for the given base and target branch */
  * `performRetry` **(Compute Cores)** (Impact: 24.9)
    * *Intent:* /** Perform the given retry action. */
  * `getMultiCommitOperationSuccessBanner` **(Stateful Encapsulated Methods)** (Impact: 24.3)
  * `processMultiCommitOperationRebaseResult` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* /** * Processes the multi commit operation result * 1. Completes the operation with banner if succes...
  * `squash` **(Many-Argument Workhorses)** (Impact: 23.4)
    * *Intent:* /** * Starts a squash * * squash or null if a commit to squash is root (first in history) of the * b...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 377
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 625`, `args: 293`, `func_start: 276`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 28`, `planned_debt: 5`
* *Architecture:* `io: 37`, `api: 259`, `concurrency: 297`, `import: 60`
* *Defense:* `safety: 29`, `doc: 207`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.696
  * `Choke Point (Betweenness):` 0.02783 | `Ripple Effect (Closeness):` 0.077036
  * `Imports (Out-Degree: 63):` api, app-shell, app-state, ci-checks, cli-action, custom-integration, drag-and-drop-manager, fatal-error...
  * `Imported By (In-Degree: 88):` (Excluded from Brief to save tokens)

### `app/src/ui/app.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 9.286)
- **Top Global Matches:** file_cluster_16: 9.286, file_cluster_0: 10.179, file_cluster_10: 10.21
- **Magnitude:** 1104.88 | **LOC:** 3761 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 41.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **153**; blast radius 0.376; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.8%), Guard Balance (formerly Safety Score) (50.5%), Concurrency Surface (formerly Concurrency) (27.7%)
- **Documentation Coverage:** 88.3871% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `popupContent` **(Many-Argument Workhorses)** (Impact: 236.4)
  * `onMenuEvent` **(Compute Cores)** (Impact: 79.4)
  * `onWindowKeyDown` **(Compute Cores)** (Impact: 35.9)
    * *Intent:* /** * On Windows pressing the Alt key and holding it down should * highlight the application menu. *...
  * `renderRepositoryToolbarButton` **(I/O & Config Routines)** (Impact: 17.9)
  * `renderRepository` **(I/O & Config Routines)** (Impact: 15.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 429`, `structural_boundaries: 638`, `args: 175`, `func_start: 148`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 27`, `planned_debt: 3`
* *Architecture:* `io: 24`, `api: 10`, `concurrency: 34`, `import: 153`
* *Defense:* `safety: 19`, `doc: 25`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.376
  * `Choke Point (Betweenness):` 0.000976 | `Ripple Effect (Closeness):` 0.002373
  * `Imports (Out-Degree: 155):` api, app-shell, app-state, branch, clamp, commit-url, custom-integration, drag-and-drop-manager...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/lib/stores/git-store.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.904)
- **Top Global Matches:** file_cluster_16: 7.904, file_cluster_15: 7.967, file_cluster_0: 8.223
- **Magnitude:** 1066.62 | **LOC:** 1775 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **34**; blast radius 0.782; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (84.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.3%)
- **Documentation Coverage:** 29.6875% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `discardChanges` **(Many-Argument Workhorses)** (Impact: 35.2)
  * `loadCommitAndCoAuthors` **(Compute Cores)** (Impact: 28.0)
    * *Intent:* /** * Attempt to restore both the commit message and any co-authors * in it after an undo operation....
  * `fetch` **(Compute Cores)** (Impact: 21.8)
    * *Intent:* /** * Fetch the default, current, and upstream remotes, using the given account for * authentication...
  * `emitUpdatesForChangedTags` **(Stateful Encapsulated Methods)** (Impact: 19.5)
    * *Intent:* /** * Calculates the commits that have changed based on the changes in existing tags * to emit the c...
  * `loadLocalCommits` **(Compute Cores)** (Impact: 16.3)
    * *Intent:* /** * Load local commits into memory for the current repository. * * this will reset the local commi...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 35 instances
* *Amplified Cascading Flux:* 80 instances
* *Concurrency (weighted view):* 319
* *State Mutation (weighted view):* 254
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 274`, `args: 121`, `func_start: 71`, `class_start: 1`
* *Risk/State:* `state_mutation: 94`, `planned_debt: 1`
* *Architecture:* `io: 18`, `api: 61`, `concurrency: 144`, `import: 34`
* *Defense:* `safety: 19`, `doc: 51`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.782
  * `Choke Point (Betweenness):` 0.003982 | `Ripple Effect (Closeness):` 0.083302
  * `Imports (Out-Degree: 52):` git, author, branch, commit, commit-message, diff, git-author, progress...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `app/src/ui/diff/side-by-side-diff.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.368)
- **Top Global Matches:** file_cluster_16: 7.368, file_cluster_15: 7.633, file_cluster_10: 8.623
- **Magnitude:** 970.1 | **LOC:** 2151 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **19**; blast radius 0.373; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.7%), Complexity Load (formerly Cognitive Load) (24.1%)
- **Documentation Coverage:** 87.9121% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getModifiedRows` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `getDiffRowsFromHunk` **(Many-Argument Workhorses)** (Impact: 28.4)
    * *Intent:* /** * Returns an array of rows with the needed data to render a side-by-side diff * with them. * * I...
  * `getDiscardLabel` **(Stateful Encapsulated Methods)** (Impact: 23.5)
  * `onDocumentSelectionChange` **(Compute Cores)** (Impact: 22.0)
  * `onUpdateSelection` **(Compute Cores)** (Impact: 22.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 86 instances
* *State Mutation (weighted view):* 279
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 293`, `structural_boundaries: 251`, `args: 96`, `func_start: 82`, `class_start: 5`
* *Risk/State:* `state_mutation: 107`
* *Architecture:* `api: 11`, `concurrency: 2`, `import: 22`
* *Defense:* `safety: 30`, `doc: 34`, `immutability_locks: 29`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.373
  * `Choke Point (Betweenness):` 0.00026 | `Ripple Effect (Closeness):` 0.003813
  * `Imports (Out-Degree: 14):` fatal-error, types, menu-item, diff, aria-live-container, diff-contents-warning, diff-explorer, diff-helpers...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `app/src/lib/actions-log-parser/action-log-parser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.19)
- **Top Global Matches:** file_cluster_6: 6.19, file_cluster_4: 10.274, file_cluster_8: 15.356
- **Magnitude:** 953.48 | **LOC:** 741 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.341; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.8%), Complexity Load (formerly Cognitive Load) (78.4%)
- **Documentation Coverage:** 39.1304% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 258.9)
    * *Intent:* /** * Converts the content to HTML with appropriate styles, escapes content to prevent XSS * */
  * `getStates` **(Compute Cores)** (Impact: 136.9)
    * *Intent:* /** * Parses the content into ANSII states * */
  * `parseLines` **(Compute Cores)** (Impact: 81.9)
    * *Intent:* /** * Parses the content into lines with nodes * */
  * `parseCommandEnd` **(I/O & Config Routines)** (Impact: 17.4)
  * `updateLineMetaData` **(Stateful Encapsulated Methods)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 129 instances
* *State Mutation (weighted view):* 401
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 36`, `args: 20`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 143`, `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 1`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` action-log-pipeline-commands, actions-log-parser-objects, actions-logs-ansii
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/ui/lib/list/list.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.167)
- **Top Global Matches:** file_cluster_4: 7.167, file_cluster_12: 9.887, file_cluster_16: 10.539
- **Magnitude:** 743.36 | **LOC:** 1758 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **15**; blast radius 1.208; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (79.3%), Guard Balance (formerly Safety Score) (55.0%), Concurrency Surface (formerly Concurrency) (19.5%)
- **Documentation Coverage:** 87.0968% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onKeyDown` **(Compute Cores)** (Impact: 73.6)
  * `onRowMouseDown` **(Many-Argument Workhorses)** (Impact: 62.2)
  * `getRowRenderer` **(Compute Cores)** (Impact: 28.6)
  * `onRowMouseUp` **(Compute Cores)** (Impact: 28.0)
  * `componentDidUpdate` **(Many-Argument Workhorses)** (Impact: 27.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 42 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 318`, `structural_boundaries: 156`, `args: 84`, `func_start: 54`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 48`
* *Architecture:* `io: 1`, `api: 12`, `concurrency: 1`, `import: 15`
* *Defense:* `safety: 25`, `doc: 56`, `immutability_locks: 51`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.208
  * `Choke Point (Betweenness):` 0.0048 | `Ripple Effect (Closeness):` 0.060306
  * `Imports (Out-Degree: 10):` equality, non-fatal-exception, range, drag-drop, focus-container, id-pool, list-item-insertion-overlay, list-row...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `app/src/ui/lib/list/section-list.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.246)
- **Top Global Matches:** file_cluster_4: 8.246, file_cluster_12: 8.339, file_cluster_16: 9.024
- **Magnitude:** 733.62 | **LOC:** 1783 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **14**; blast radius 0.451; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (79.9%), Guard Balance (formerly Safety Score) (54.8%), Concurrency Surface (formerly Concurrency) (19.2%)
- **Documentation Coverage:** 89.0411% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onRowMouseDown` **(Many-Argument Workhorses)** (Impact: 60.6)
  * `onKeyDown` **(Compute Cores)** (Impact: 46.9)
  * `componentDidUpdate` **(Many-Argument Workhorses)** (Impact: 27.3)
  * `getRowRenderer` **(Many-Argument Workhorses)** (Impact: 26.9)
  * `onRowMouseUp` **(Compute Cores)** (Impact: 26.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 159`, `args: 97`, `func_start: 63`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 48`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 13`, `concurrency: 1`, `import: 14`
* *Defense:* `safety: 26`, `doc: 46`, `immutability_locks: 43`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.451
  * `Choke Point (Betweenness):` 0.000675 | `Ripple Effect (Closeness):` 0.010227
  * `Imports (Out-Degree: 10):` equality, non-fatal-exception, range, drag-drop, focus-container, id-pool, list-item-insertion-overlay, list-row...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/lib/api.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.125)
- **Top Global Matches:** file_cluster_0: 8.125, file_cluster_15: 8.821, file_cluster_12: 9.23
- **Magnitude:** 724.78 | **LOC:** 2486 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 88.9%
- **Blast Radius:** changing it is visible to **94** in-repo importer(s); it depends on **10**; blast radius 23.767; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Connectivity (formerly Api Exposure) (96.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.0%), Guard Balance (formerly Safety Score) (44.7%)
- **Documentation Coverage:** 17.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copilotRequest` **(Many-Argument Workhorses)** (Impact: 47.1)
    * *Intent:* /** * Make an authenticated request to the client's Copilot endpoint with its * token. Used for Copi...
  * `getNextPagePathFromLink` **(Stateful Encapsulated Methods)** (Impact: 25.5)
    * *Intent:* /** * Parses the Link header from GitHub and returns the 'next' path * if one is present. * * If no ...
  * `fetchAll` **(Stateful Encapsulated Methods)** (Impact: 20.4)
    * *Intent:* /** * Authenticated requests to a paginating resource such as issues. * * Follows the GitHub API hyp...
  * `isGitHubHost` **(Defensive Guards)** (Impact: 15.6)
    * *Intent:* /** * Attempts to determine whether or not the url belongs to a GitHub host. * * This is a best-effo...
  * `ghRequest` **(Stateful Encapsulated Methods)** (Impact: 15.4)
    * *Intent:* /** * Make an authenticated request to the client's endpoint with its token. * Used for GitHub API r...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 197
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 372`, `args: 90`, `func_start: 71`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 15`, `fragile_debt: 1`
* *Architecture:* `io: 79`, `api: 99`, `concurrency: 177`, `import: 12`
* *Defense:* `safety: 106`, `doc: 123`, `immutability_locks: 161`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.767
  * `Choke Point (Betweenness):` 0.028325 | `Ripple Effect (Closeness):` 0.161542
  * `Imports (Out-Degree: 9):` account, bypass-push-protection-dialog, copilot-commit-message, copilot-error, endpoint-capabilities, http, http-status-code, remote-parsing...
  * `Imported By (In-Degree: 94):` (Excluded from Brief to save tokens)

### `app/src/ui/changes/commit-message.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.496)
- **Top Global Matches:** file_cluster_4: 7.496, file_cluster_16: 10.157, file_cluster_0: 10.785
- **Magnitude:** 676.18 | **LOC:** 1820 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **44**; blast radius 0.422; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.6%), Guard Balance (formerly Safety Score) (51.7%), Mutation Surface (formerly State Flux) (46.5%)
- **Documentation Coverage:** 95.122% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateRepoRulesCommitMessageFailures` **(Defensive Guards)** (Impact: 41.9)
  * `componentDidUpdate` **(Many-Argument Workhorses)** (Impact: 32.1)
  * `createCommit` **(Defensive Guards)** (Impact: 25.5)
  * `updateRepoRulesCommitAuthorFailures` **(Stateful Encapsulated Methods)** (Impact: 23.8)
  * `renderBranchProtectionsRepoRulesCommitWarning` **(I/O & Config Routines)** (Impact: 22.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 35 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 211`, `args: 101`, `func_start: 76`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 47`
* *Architecture:* `io: 1`, `api: 7`, `concurrency: 16`, `import: 45`
* *Defense:* `safety: 39`, `doc: 23`, `immutability_locks: 68`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.422
  * `Choke Point (Betweenness):` 0.000304 | `Ripple Effect (Closeness):` 0.00461
  * `Imports (Out-Degree: 41):` app-state, email, endpoint-capabilities, fatal-error, feature-flag, format-commit-message, git, config...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/test/unit/git/multi-operation-terminal-output-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.446)
- **Top Global Matches:** file_cluster_10: 4.446, file_cluster_2: 6.946, file_cluster_13: 7.511
- **Magnitude:** 497.73 | **LOC:** 156 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.341; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (54.9%), Complexity Load (formerly Cognitive Load) (49.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (8.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 52
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 32`, `args: 19`, `func_start: 6`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `concurrency: 17`, `import: 4`
* *Defense:* `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` git, multi-operation-terminal-output, node:assert, node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/lib/git/diff.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.004)
- **Top Global Matches:** file_cluster_15: 7.004, file_cluster_0: 7.875, file_cluster_16: 8.597
- **Magnitude:** 486.76 | **LOC:** 853 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **20**; blast radius 0.727; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (58.5%)
- **Documentation Coverage:** 23.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getImageDiff` **(Many-Argument Workhorses)** (Impact: 32.9)
  * `getCommitRangeDiff` **(Many-Argument Workhorses)** (Impact: 27.2)
    * *Intent:* /** * Render the difference between two commits for a file * */
  * `getWorkingDirectoryDiff` **(Many-Argument Workhorses)** (Impact: 19.0)
    * *Intent:* /** * Render the diff for a file within the repository working directory. The file will be * compare...
  * `getMediaType` **(Compute Cores)** (Impact: 15.6)
    * *Intent:* /** * Map a given file extension to the related data URL media type */
  * `convertDiff` **(Many-Argument Workhorses)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 34 instances
* *Concurrency (weighted view):* 165
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 106`, `args: 30`, `func_start: 24`
* *Risk/State:* `state_mutation: 41`, `planned_debt: 1`
* *Architecture:* `io: 41`, `api: 11`, `concurrency: 55`, `import: 23`
* *Defense:* `safety: 7`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.727
  * `Choke Point (Betweenness):` 0.004337 | `Ripple Effect (Closeness):` 0.094667
  * `Imports (Out-Degree: 18):` diff, repository, status, diff-parser, fatal-error, feature-flag, get-old-path, status-parser...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `app/src/lib/stores/repositories-store.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 8.355)
- **Top Global Matches:** file_cluster_16: 8.355, file_cluster_15: 8.394, file_cluster_4: 8.464
- **Magnitude:** 440.64 | **LOC:** 742 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **11**; blast radius 0.804; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (69.0%), Complexity Load (formerly Cognitive Load) (61.5%)
- **Documentation Coverage:** 20.4082% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_upsertGitHubRepository` **(Stateful Encapsulated Methods)** (Impact: 38.2)
  * `putOwner` **(Stateful Encapsulated Methods)** (Impact: 23.8)
  * `getPermissionsString` **(Compute Cores)** (Impact: 15.0)
  * `toGitHubRepository` **(Stateful Encapsulated Methods)** (Impact: 14.2)
  * `updateBranchProtections` **(Compute Cores)** (Impact: 11.0)
    * *Intent:* /** Add or update the branch protections associated with a GitHub repository. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 172
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 117`, `args: 42`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `dead_code: 1`
* *Architecture:* `io: 13`, `api: 21`, `concurrency: 92`, `import: 11`
* *Defense:* `safety: 19`, `doc: 23`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.804
  * `Choke Point (Betweenness):` 0.001097 | `Ripple Effect (Closeness):` 0.083921
  * `Imports (Out-Degree: 11):` github-repository, owner, repository, workflow-preferences, api, repositories-database, equality, fatal-error...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `app/test/unit/git/cherry-pick-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.122)
- **Top Global Matches:** file_cluster_10: 6.122, file_cluster_15: 7.967, file_cluster_2: 8.454
- **Magnitude:** 422.72 | **LOC:** 726 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.341; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.8%), Guard Balance (formerly Safety Score) (48.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addThreeMoreCommitsOntoFeatureBranch` **(I/O & Config Routines)** (Impact: 3.2)
  * `setup` **(Callbacks & Closures)** (Impact: 2.3)
  * `makeConflictCommit` **(Callbacks & Closures)** (Impact: 2.2)
  * `getCommitOneLine` **(Parameter Forwarders)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 37 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 371
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 211`, `args: 33`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23`
* *Architecture:* `io: 29`, `concurrency: 186`, `import: 16`
* *Defense:* `safety: 5`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` git, cherry-pick, status, manual-conflict-resolution, progress, repository, status, git...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/ui/changes/filter-changes-list.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.626)
- **Top Global Matches:** file_cluster_10: 8.626, file_cluster_16: 8.725, file_cluster_0: 8.757
- **Magnitude:** 405.98 | **LOC:** 1544 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **47**; blast radius 0.631; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.6%), Mutation Surface (formerly State Flux) (16.0%)
- **Documentation Coverage:** 98.8636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getDefaultContextMenu` **(Callbacks & Closures)** (Impact: 32.8)
  * `renderChangedFile` **(Many-Argument Workhorses)** (Impact: 32.5)
  * `onContextMenu` **(Compute Cores)** (Impact: 15.9)
  * `renderCommitMessageForm` **(I/O & Config Routines)** (Impact: 13.5)
  * `getPlaceholderMessage` **(Stateful Encapsulated Methods)** (Impact: 13.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 242`, `args: 122`, `func_start: 84`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 22`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 35`, `api: 6`, `concurrency: 1`, `import: 50`
* *Defense:* `safety: 4`, `doc: 22`, `immutability_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.631
  * `Choke Point (Betweenness):` 0.000699 | `Ripple Effect (Closeness):` 0.00293
  * `Imports (Out-Degree: 42):` app-shell, app-state, equality, fuzzy-find, git, menu-item, path, status...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `app/src/lib/stats/stats-store.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.984)
- **Top Global Matches:** file_cluster_15: 6.984, file_cluster_16: 7.072, file_cluster_0: 7.928
- **Magnitude:** 397.06 | **LOC:** 1248 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **24**; blast radius 2.754; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.4%), Connectivity (formerly Api Exposure) (45.7%)
- **Documentation Coverage:** 52.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getDailyStats` **(Many-Argument Workhorses)** (Impact: 17.3)
    * *Intent:* /** Get the daily stats. */
  * `reportStats` **(Defensive Guards)** (Impact: 14.2)
    * *Intent:* /** Report any stats which are eligible for reporting. */
  * `recordOperationConflictsEncounteredCount` **(Compute Cores)** (Impact: 12.4)
  * `recordOperationSuccessful` **(Compute Cores)** (Impact: 12.4)
  * `recordOperationSuccessfulWithConflicts` **(Compute Cores)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 95
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 167`, `args: 78`, `func_start: 63`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 10`, `api: 43`, `concurrency: 60`, `import: 25`
* *Defense:* `safety: 8`, `doc: 61`, `immutability_locks: 32`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.754
  * `Choke Point (Betweenness):` 0.029001 | `Ripple Effect (Closeness):` 0.103177
  * `Imports (Out-Degree: 24):` merge, account, multi-commit-operation, repository, app-proxy, application-theme, diff-mode, ui-activity-monitor...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `app/src/ui/history/commit-list.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.882)
- **Top Global Matches:** file_cluster_4: 8.882, file_cluster_16: 9.0, file_cluster_15: 9.646
- **Magnitude:** 374.48 | **LOC:** 1046 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **26**; blast radius 0.509; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.0%), Mutation Surface (formerly State Flux) (30.5%), Debt Markers (formerly Tech Debt) (22.3%)
- **Documentation Coverage:** 94.8276% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getContextMenuForSingleCommit` **(Many-Argument Workhorses)** (Impact: 67.7)
  * `onDropDataInsertion` **(Compute Cores)** (Impact: 36.6)
  * `onRowContextMenu` **(Compute Cores)** (Impact: 11.9)
  * `renderRowFocusTooltip` **(Compute Cores)** (Impact: 11.7)
  * `renderCommit` **(Compute Cores)** (Impact: 10.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 181`, `args: 92`, `func_start: 54`, `class_start: 3`
* *Risk/State:* `state_mutation: 20`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 5`, `import: 27`
* *Defense:* `safety: 22`, `doc: 39`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.509
  * `Choke Point (Betweenness):` 0.009573 | `Ripple Effect (Closeness):` 0.072509
  * `Imports (Out-Degree: 20):` api, emoji, equality, fatal-error, format-date, menu-item, account, avatar...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/test/unit/git/commit-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.208)
- **Top Global Matches:** file_cluster_10: 6.208, file_cluster_2: 8.677, file_cluster_13: 9.083
- **Magnitude:** 360.38 | **LOC:** 915 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.341; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (47.5%), Guard Balance (formerly Safety Score) (46.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setup` **(Callbacks & Closures)** (Impact: 2.6)
  * `getTextDiff` **(Generic / Templated Code)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 26 instances
* *Concurrency (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 237`, `args: 52`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 14`, `fragile_debt: 1`
* *Architecture:* `io: 93`, `concurrency: 198`, `import: 14`
* *Defense:* `safety: 9`, `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` git, status, diff, manual-conflict-resolution, repository, status, path-exists, repositories...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/ui/lib/tooltip.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.487)
- **Top Global Matches:** file_cluster_16: 7.487, file_cluster_15: 8.115, file_cluster_10: 8.471
- **Magnitude:** 358.36 | **LOC:** 842 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **7**; blast radius 7.362; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (74.2%), Guard Balance (formerly Safety Score) (52.8%), Concurrency Surface (formerly Concurrency) (46.3%)
- **Documentation Coverage:** 93.8776% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getTooltipRectRelativeTo` **(Compute Cores)** (Impact: 23.6)
  * `getDirection` **(Many-Argument Workhorses)** (Impact: 23.3)
  * `componentDidUpdate` **(Compute Cores)** (Impact: 18.8)
  * `fits` **(Compute Cores)** (Impact: 15.6)
  * `onTooltipRef` **(Defensive Guards)** (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 69`, `args: 43`, `func_start: 41`, `class_start: 4`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `api: 12`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 12`, `doc: 29`, `immutability_locks: 27`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.362
  * `Choke Point (Betweenness):` 0.000583 | `Ripple Effect (Closeness):` 0.113149
  * `Imports (Out-Degree: 4):` fatal-error, id-pool, observable-ref, rect, classnames, react, react-dom
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `app/src/lib/ci-checks/ci-checks.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.713)
- **Top Global Matches:** file_cluster_15: 7.713, file_cluster_0: 8.018, file_cluster_9: 8.277
- **Magnitude:** 351.74 | **LOC:** 723 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **5**; blast radius 1.364; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.1%), Concurrency Surface (formerly Concurrency) (73.1%)
- **Documentation Coverage:** 9.7561% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getCheckRunsGroupedByActionWorkflowNameAndEvent` **(Defensive Guards)** (Impact: 20.6)
    * *Intent:* /** * Groups check runs by their actions workflow name and actions workflow event type. * Event type...
  * `getCheckRunShortDescription` **(Many-Argument Workhorses)** (Impact: 17.6)
    * *Intent:* /** * Method to generate a user friendly short check run description such as * "Successful in xs", "...
  * `getCheckRunConclusionAdjective` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* /** * Returns the user-facing adjective for a given check run conclusion. */
  * `getCheckRunActionsWorkflowRunsByCheckSuiteId` **(Many-Argument Workhorses)** (Impact: 15.6)
    * *Intent:* /** * Retrieves the action workflow runs by using the check suite id. * * If the check run is run us...
  * `getLatestPRWorkflowRunsLogsForCheckRun` **(Many-Argument Workhorses)** (Impact: 15.2)
    * *Intent:* /** * Retrieve GitHub Actions job and logs for the check runs. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 27 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 101`, `args: 34`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `api: 22`, `concurrency: 14`, `import: 5`
* *Defense:* `safety: 7`, `doc: 24`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.364
  * `Choke Point (Betweenness):` 0.000484 | `Ripple Effect (Closeness):` 0.088938
  * `Imports (Out-Degree: 5):` account, github-repository, api, endpoint-capabilities, format-duration
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `app/src/lib/git/core.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.648)
- **Top Global Matches:** file_cluster_6: 7.648, file_cluster_4: 9.074, file_cluster_12: 16.294
- **Magnitude:** 351.3 | **LOC:** 609 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **50** in-repo importer(s); it depends on **10**; blast radius 8.665; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.6%), Mutation Surface (formerly State Flux) (74.5%), Guard Balance (formerly Safety Score) (47.3%)
- **Documentation Coverage:** 44.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getDescriptionForError` **(Stateful Encapsulated Methods)** (Impact: 116.1)
  * `git` **(Many-Argument Workhorses)** (Impact: 75.2)
  * `constructor` **(Many-Argument Workhorses)** (Impact: 19.4)
  * `isAuthFailureError` **(Compute Cores)** (Impact: 7.8)
    * *Intent:* /** * Determine whether the provided `error` is an authentication failure * as per our definition. N...
  * `processCallback` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* // Keep at most 256kb of combined stderr and stdout output. This is used // to provide more context ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 141`, `args: 26`, `func_start: 14`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 18`
* *Architecture:* `io: 14`, `api: 27`, `concurrency: 9`, `import: 10`
* *Defense:* `safety: 38`, `doc: 24`, `sync_locks: 3`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.665
  * `Choke Point (Betweenness):` 0.033001 | `Ripple Effect (Closeness):` 0.116248
  * `Imports (Out-Degree: 7):` git-perf, errno-exception, fatal-error, with-hooks-env, trampoline-environment, coerce-to-string, push-terminal-chunk, buffer...
  * `Imported By (In-Degree: 50):` (Excluded from Brief to save tokens)

### `app/src/lib/git/rebase.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.426)
- **Top Global Matches:** file_cluster_4: 6.426, file_cluster_15: 11.016, file_cluster_12: 11.242
- **Magnitude:** 350.62 | **LOC:** 628 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **20**; blast radius 0.775; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (95.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (50.9%)
- **Documentation Coverage:** 13.6364% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `continueRebase` **(Many-Argument Workhorses)** (Impact: 49.8)
    * *Intent:* /** * Proceed with the current rebase operation and report back on whether it completed * * It is ex...
  * `rebaseInteractive` **(Many-Argument Workhorses)** (Impact: 36.4)
    * *Intent:* /** * Method for initiating interactive rebase in the app. * * In order to modify the interactive to...
  * `getRebaseSnapshot` **(Compute Cores)** (Impact: 23.8)
    * *Intent:* /** * Inspect the `.git/rebase-merge` folder and convert the current rebase state * into data that c...
  * `parse` **(Defensive Guards)** (Impact: 11.3)
  * `rebase` **(Many-Argument Workhorses)** (Impact: 11.1)
    * *Intent:* /** * A stub function to use for initiating rebase in the app. * * If the rebase fails, the reposito...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 100
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 96`, `args: 19`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 26`, `planned_debt: 6`
* *Architecture:* `io: 25`, `api: 11`, `concurrency: 35`, `import: 20`
* *Defense:* `safety: 27`, `doc: 19`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.775
  * `Choke Point (Betweenness):` 0.006007 | `Ripple Effect (Closeness):` 0.097553
  * `Imports (Out-Degree: 15):` branch, commit, manual-conflict-resolution, progress, rebase, repository, status, path-exists...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `app/src/ui/preferences/preferences.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.222)
- **Top Global Matches:** file_cluster_10: 8.222, file_cluster_16: 9.011, file_cluster_0: 9.064
- **Magnitude:** 343.88 | **LOC:** 919 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **31**; blast radius 0.633; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (75.6%), Guard Balance (formerly Safety Score) (55.1%)
- **Documentation Coverage:** 96.0784% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onSave` **(I/O & Config Routines)** (Impact: 29.4)
  * `renderActiveTab` **(I/O & Config Routines)** (Impact: 24.3)
  * `getTabId` **(Compute Cores)** (Impact: 17.2)
  * `componentWillMount` **(I/O & Config Routines)** (Impact: 16.4)
  * `constructor` **(I/O & Config Routines)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 25 instances
* *Concurrency (weighted view):* 45
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 134`, `args: 52`, `func_start: 48`, `class_start: 3`
* *Risk/State:* `state_mutation: 58`
* *Architecture:* `io: 1`, `api: 4`, `concurrency: 25`, `import: 31`
* *Defense:* `safety: 12`, `doc: 3`, `sync_locks: 1`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.633
  * `Choke Point (Betweenness):` 0.000278 | `Ripple Effect (Closeness):` 0.001648
  * `Imports (Out-Degree: 32):` custom-integration, lookup, email, fatal-error, git, config, default-branch, config...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/src/ui/lib/augmented-filter-list.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.925)
- **Top Global Matches:** file_cluster_0: 8.925, file_cluster_12: 9.578, file_cluster_4: 9.701
- **Magnitude:** 336.44 | **LOC:** 926 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.354; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.6%), Mutation Surface (formerly State Flux) (51.2%), Connectivity (formerly Api Exposure) (16.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onKeyDown` **(Compute Cores)** (Impact: 27.9)
  * `createStateUpdate` **(Many-Argument Workhorses)** (Impact: 27.7)
  * `onRowKeyDown` **(Compute Cores)** (Impact: 27.4)
  * `selectNextItem` **(Compute Cores)** (Impact: 18.0)
  * `componentDidUpdate` **(Compute Cores)** (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 151`, `args: 79`, `func_start: 33`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 23`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 12`, `import: 12`
* *Defense:* `safety: 4`, `doc: 35`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.354
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.002519
  * `Imports (Out-Degree: 8):` fuzzy-find, aria-live-container, section-list, section-list-selection, row, text-box, octicons.generated, filter-list...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `app/src/lib/actions-log-parser/actions-log-parser-objects.ts` (TYPESCRIPT) | Magnitude: 33.68 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 31, core_var_decl: 18, api: 17
- `app/src/ui/add-repository/add-existing-repository.tsx` (TYPESCRIPT) | Magnitude: 136.86 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 224, structural_boundaries: 61, io: 43, core_var_decl: 42
- `app/src/ui/history/merge-call-to-action.tsx` (TYPESCRIPT) | Magnitude: 15.9 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 18, ui_framework: 16, core_var_decl: 11
- `app/src/ui/dropdown-select-button.tsx` (TYPESCRIPT) | Magnitude: 154.2 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 298, core_var_decl: 71, structural_boundaries: 60, branch: 52
- `app/src/ui/create-branch/create-branch-dialog.tsx` (TYPESCRIPT) | Magnitude: 180.84 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 437, structural_boundaries: 74, ui_framework: 74, branch: 60

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `app/src/main-process/authenticated-image-filter.ts` (TYPESCRIPT) | Magnitude: 23.56 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 12, branch: 7, bitwise_ops: 7
- `app/src/lib/file-system.ts` (TYPESCRIPT) | Magnitude: 19.7 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 24, args: 10, io: 8
- `app/src/ui/check-runs/ci-check-run-list-item.tsx` (TYPESCRIPT) | Magnitude: 40.54 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 164, structural_boundaries: 43, core_var_decl: 40, design_camel_case: 28
- `app/styles/ui/_button.scss` (CSS) | Magnitude: 0.85 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 82, class_start: 17, closures: 13, branch: 2
- `app/src/lib/format-duration.ts` (TYPESCRIPT) | Magnitude: 36.3 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 27, core_var_decl: 9, branch: 8, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `app/src/ui/lib/test-ui-components/test-ui-components.ts` (TYPESCRIPT) | Magnitude: 265.46 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 432, structural_boundaries: 109, branch: 65, args: 29
- `app/src/ui/lib/application-theme.ts` (TYPESCRIPT) | Magnitude: 39.66 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 29, branch: 13, core_var_decl: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `app/src/ui/lib/text-area.tsx` (TYPESCRIPT) | Magnitude: 14.16 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 51, branch: 18, structural_boundaries: 18, ui_framework: 18
- `app/styles/ui/onboarding-tutorial/_done.scss` (CSS) | Magnitude: 0.29 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 51, class_start: 8, ui_framework: 3, branch: 2
- `app/styles/ui/dialogs/_repository-settings.scss` (CSS) | Magnitude: 0.79 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 37, class_start: 9, ui_framework: 2, safety_bypasses: 1
- `app/test/unit/identifier-rules-test.ts` (TYPESCRIPT) | Magnitude: 18.84 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 37, test: 25, structural_boundaries: 12, args: 9
- `app/styles/ui/_missing-repository-view.scss` (CSS) | Magnitude: 0.79 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 37, class_start: 7, ui_framework: 4, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `app/test/unit/email-test.ts` (TYPESCRIPT) | Magnitude: 21.32 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 307, decorators: 36, structural_boundaries: 19, test: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `app/src/ui/branches/ci-status.tsx` (TYPESCRIPT) | Magnitude: 88.92 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 41, branch: 32, ui_framework: 19
- `app/src/lib/editors/launch.ts` (TYPESCRIPT) | Magnitude: 34.96 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 15, core_var_decl: 10, branch: 9
- `app/src/ui/lib/sandboxed-markdown.tsx` (TYPESCRIPT) | Magnitude: 167.7 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 260, branch: 51, structural_boundaries: 50, core_var_decl: 43
- `app/src/ui/diff/image-diffs/two-up.tsx` (TYPESCRIPT) | Magnitude: 14.84 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 65, core_var_decl: 26, ui_framework: 25, design_camel_case: 24
- `app/src/models/commit-identity.ts` (TYPESCRIPT) | Magnitude: 25.58 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 27, core_var_decl: 10, api: 8, branch: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `app/src/lib/stores/base-store.ts` (TYPESCRIPT) | Magnitude: 18.92 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 17, args: 8, func_start: 8
- `app/src/lib/stores/repositories-store.ts` (TYPESCRIPT) | Magnitude: 440.64 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 475, structural_boundaries: 117, concurrency: 92, branch: 66
- `app/src/ui/multi-commit-operation/choose-branch/choose-target-branch.tsx` (TYPESCRIPT) | Magnitude: 69.56 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 166, structural_boundaries: 38, core_var_decl: 37, ui_framework: 31
- `app/src/lib/stores/git-store.ts` (TYPESCRIPT) | Magnitude: 1066.62 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1120, structural_boundaries: 274, branch: 175, core_var_decl: 149
- `app/src/ui/lib/draggable.tsx` (TYPESCRIPT) | Magnitude: 82.16 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 36, branch: 18, args: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `app/src/ui/branches/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `app/src/lib/app-state.ts` (TYPESCRIPT) | Magnitude: 51.66 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 260, immutability_locks: 198, doc: 176, structural_boundaries: 125
- `app/src/lib/git/index.ts` (TYPESCRIPT) | Magnitude: 50.7 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 36, api: 35, import: 35, io: 1
- `app/src/models/stash-entry.ts` (TYPESCRIPT) | Magnitude: 20.5 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 11, immutability_locks: 9, doc: 6
- `app/styles/_ui.scss` (CSS) | Magnitude: 0.86 | Delta: **0.237** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: import: 113

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `app/styles/ui/_progress.scss` (CSS) | Magnitude: 0.08 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 17, closures: 3, func_start: 1, safety: 1
- `app/styles/ui/_text-box.scss` (CSS) | Magnitude: 0.8 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 50, ui_framework: 7, class_start: 6, closures: 6
- `app/src/lib/valid-notification-pull-request-review.ts` (TYPESCRIPT) | Magnitude: 8.04 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 7, api: 3, branch: 2
- `app/src/lib/progress/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7, io: 1
- `app/test/helpers/repository-builder-cherry-pick-test.ts` (TYPESCRIPT) | Magnitude: 14.52 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 13, concurrency: 9, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `app/src/ui/app-menu/app-menu-bar.tsx` (TYPESCRIPT) | Magnitude: 211.1 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 299, branch: 70, core_var_decl: 53, structural_boundaries: 45
- `app/src/ui/lib/list/section-list.tsx` (TYPESCRIPT) | Magnitude: 733.62 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1159, branch: 285, core_var_decl: 227, ui_framework: 166
- `app/src/ui/history/commit-list.tsx` (TYPESCRIPT) | Magnitude: 374.48 | Delta: **0.118** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 759, structural_boundaries: 181, branch: 157, core_var_decl: 156

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `app/src/highlighter/globals.d.ts` (TYPESCRIPT) | Magnitude: 5.03 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 270, indent_spaces: 82, doc: 38, args: 33
- `app/src/lib/logging/renderer/install.ts` (TYPESCRIPT) | Magnitude: 25.52 | Delta: **0.12** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 17, branch: 5, args: 5, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `app/src/lib/shells/win32.ts` (TYPESCRIPT) | Magnitude: 206.66 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 443, structural_boundaries: 109, io: 87, core_var_decl: 75
- `app/src/lib/trampoline/trampoline-askpass-handler.ts` (TYPESCRIPT) | Magnitude: 62.74 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 107, structural_boundaries: 35, branch: 26, core_var_decl: 14
- `app/src/ui/lib/popover.tsx` (TYPESCRIPT) | Magnitude: 154.44 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 327, branch: 72, core_var_decl: 56, structural_boundaries: 49
- `app/src/ui/open-pull-request/pull-request-merge-status.tsx` (TYPESCRIPT) | Magnitude: 14.82 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 18, core_var_decl: 8, branch: 7
- `app/src/lib/hooks/get-repo-hooks.ts` (TYPESCRIPT) | Magnitude: 41.9 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 15, branch: 11, io: 8

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `app/src/lib/stores/app-store.ts` -> Churn: **77.88%** | Cog Load: 69.569% | Debt: 7.8013%
- `app/src/lib/stores/copilot-store.ts` -> Churn: **71.6%** | Cog Load: 52.7605% | Debt: 0.0%
- `app/src/lib/hooks/hooks-proxy.ts` -> Churn: **70.0%** | Cog Load: 74.3436% | Debt: 0.0%
- `.github/workflows/ci.yml` -> Churn: **66.48%** | Cog Load: 8.1987% | Debt: 78.8648%
- `app/src/lib/git/commit.ts` -> Churn: **52.01%** | Cog Load: 75.3533% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `app/src/lib/api.ts` -> **Sergio Padrino** (88.9% isolated ownership) | Magnitude: 724.78
- `app/test/unit/git/multi-operation-terminal-output-test.ts` -> **Markus Olsson** (100.0% isolated ownership) | Magnitude: 497.73
- `app/test/unit/git/cherry-pick-test.ts` -> **Markus Olsson** (100.0% isolated ownership) | Magnitude: 422.72
- `app/src/lib/stats/stats-store.ts` -> **Markus Olsson** (100.0% isolated ownership) | Magnitude: 397.06
- `app/src/ui/history/commit-list.tsx` -> **Markus Olsson** (100.0% isolated ownership) | Magnitude: 374.48

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `app/src/lib/git/core.ts` -> **Severity: 2.457** (Bridge: 0.033 * Flux: 74.4574%)
- `app/src/lib/trampoline/trampoline-environment.ts` -> **Severity: 2.235** (Bridge: 0.0234 * Flux: 95.7191%)
- `app/src/lib/stores/app-store.ts` -> **Severity: 1.82** (Bridge: 0.0337 * Flux: 54.0705%)
- `app/src/lib/git/interpret-trailers.ts` -> **Severity: 1.606** (Bridge: 0.0161 * Flux: 99.9903%)
- `app/src/lib/menu-update.ts` -> **Severity: 1.515** (Bridge: 0.016 * Flux: 94.9147%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `app/src/models/repository.ts` -> **Severity: 8.902** (Embedded: 0.1865 * Error Risk: 47.7429%)
- `app/src/lib/ipc-renderer.ts` -> **Severity: 8.877** (Embedded: 0.111 * Error Risk: 80.0%)
- `app/src/models/github-repository.ts` -> **Severity: 8.057** (Embedded: 0.1675 * Error Risk: 48.0912%)
- `app/src/models/commit.ts` -> **Severity: 7.918** (Embedded: 0.1411 * Error Risk: 56.1138%)
- `app/src/lib/http.ts` -> **Severity: 7.393** (Embedded: 0.1289 * Error Risk: 57.3563%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `app/src/ui/lib/tooltip.tsx` -> **Severity: 691.127** (Blast Radius: 7.362 * Doc Risk: 93.8776%)
- `app/src/ui/dialog/ok-cancel-button-group.tsx` -> **Severity: 568.8** (Blast Radius: 6.636 * Doc Risk: 85.7143%)
- `app/src/ui/lib/observable-ref.ts` -> **Severity: 426.1** (Blast Radius: 8.522 * Doc Risk: 50.0%)
- `app/src/lib/api.ts` -> **Severity: 407.435** (Blast Radius: 23.767 * Doc Risk: 17.1429%)
- `app/src/lib/git/core.ts` -> **Severity: 381.26** (Blast Radius: 8.665 * Doc Risk: 44.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 111 literal sites + 2 sites through wrappers = 113
- **`panics_and_aborts`:** 313 literal sites + 125 sites through wrappers = 438

- `assertNever` (function, panics_and_aborts, primitive): 104 call sites in 65 files -- `app/src/lib/fatal-error.ts`
- `fatalError` (function, panics_and_aborts, primitive): 19 call sites in 13 files -- `app/src/lib/fatal-error.ts`
- `boomtown` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `app/src/ui/lib/test-ui-components/test-ui-components.ts`
- `realpath` (function, debug_prints, primitive): 2 call sites in 1 files -- `app/static/darwin/github.sh`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 13151 call pairs -- scoped 49.1%, unique 0.0%, ambiguous 16.2%, external 34.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 13092 | 49.3% | 0.0% | 16.2% | 34.5% |
| javascript | 40 | 30.0% | 0.0% | 0.0% | 70.0% |
| shell | 19 | 0.0% | 0.0% | 0.0% | 100.0% |

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
