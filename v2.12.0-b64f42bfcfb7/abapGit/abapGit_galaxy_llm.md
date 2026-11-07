# ARCHITECTURAL_BRIEF: abapGit
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/abapGit/abapGit` |
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
- **Scope:** 1482 analyzed artifact(s), 150595 LOC.
- **Load-bearing artifact:** `CONTRIBUTING.md` -- 1 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/zabapgit.prog.abap` -- pulls in 6 dependencies, the widest assembly point in the scan.
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
| Total Artifacts | 1508 |
| Analyzed Artifacts (Scanned) | 1482 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 26 |
| Total LOC | 150595 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 98.3% |
| Dominant Lang | ABAP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ABAP | 735 | 145318 | 49.6% |
| XML | 712 | 4 | 48.0% |
| CSS | 7 | 2236 | 0.5% |
| YAML | 6 | 196 | 0.4% |
| MARKDOWN | 5 | 0 | 0.3% |
| SHELL | 4 | 77 | 0.3% |
| JAVASCRIPT | 4 | 1931 | 0.3% |
| PLAINTEXT | 4 | 1 | 0.3% |
| JSON | 3 | 803 | 0.2% |
| TYPESCRIPT | 2 | 29 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 784 |
| utf-8 | bom | 697 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 50%, Large Core Modules 15%, Interface Declarations Files 10%, Declarative / Non-Code 9%, Large Core Modules (3) 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1472 | 99.3% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 0.5% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 26*

**Composition by Extension & Reason:**
- `.abap`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2176 LOC)
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.woff`: 1x Excluded (Explicitly Denied Extension: '.woff')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 87.3 | 10.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.1 | 22.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 14.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 20.1 | 0.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 33.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.0 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 42.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2262 | 460 | 5 | `src/json/zcl_abapgit_ajson.clas.testclasses.abap` |
| cleanup | 865 | 259 | 1 | `src/objects/tabl/zcl_abapgit_object_tabl.clas.abap` |
| guards | 5741 | 649 | 12 | `src/ui/zabapgit_js_common.w3mi.data.js` |
| danger | 1051 | 140 | 0 | `src/diff/diff3/zcl_abapgit_diff3.clas.testclasses.abap` |
| concurrency | 129 | 34 | 0 | `test/gitea/tests/gitea.spec.ts` |
| connectivity | 710 | 553 | 1 | `src/ui/zabapgit_css_theme_belize_blue.w3mi.data.css` |
| io | 1066 | 249 | 2 | `src/diff/diff3/zcl_abapgit_diff3.clas.abap` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `test/gitea/create.sh` |
| time | 4 | 1 | 0 | `src/ui/zabapgit_js_common.w3mi.data.js` |
| serialization | 5 | 1 | 0 | `src/ui/zabapgit_js_common.w3mi.data.js` |
| regex | 30 | 2 | 0 | `src/ui/zabapgit_js_common.w3mi.data.js` |
| events | 51 | 11 | 0 | `src/ui/zabapgit_js_common.w3mi.data.js` |
| tests | 3387 | 145 | 0 | `src/json/zcl_abapgit_ajson.clas.testclasses.abap` |
| docs | 111 | 14 | 0 | `src/cts/zcl_abapgit_cts_api.clas.abap` |
| debt | 411 | 112 | 0 | `src/objects/core/zcl_abapgit_folder_logic.clas.testclasses.abap` |
| mutation | 61357 | 674 | 126 | `src/json/zcl_abapgit_ajson.clas.testclasses.abap` |
| dead_code | 2956 | 321 | 12 | `src/ui/flow/zcl_abapgit_flow_logic.clas.testclasses.abap` |
| credential | 2 | 2 | 0 | `src/git/zcl_abapgit_git_commit.clas.testclasses.abap` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 1486 | 134 | 0 | `src/json/zcl_abapgit_ajson.clas.testclasses.abap` |
| ui | 167 | 24 | 0 | `src/ui/zabapgit_js_common.w3mi.data.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/diff/diff3/zcl_abapgit_diff3.clas.abap` (Hits: 47)
- `ci/deploy-release-tag.sh` (Hits: 33)
- `src/objects/zcl_abapgit_object_nspc.clas.abap` (Hits: 24)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 1 inbound connections
2. **zabapgit_password_dialog.prog.abap** (`src/zabapgit_password_dialog.prog.abap`) — 1 inbound connections
3. **FUNDING.yml** (`.github/FUNDING.yml`) — 0 inbound connections
4. **ajson_mirror.yaml** (`.github/workflows/ajson_mirror.yaml`) — 0 inbound connections
5. **main-build.yml** (`.github/workflows/main-build.yml`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **zabapgit.prog.abap** (`src/zabapgit.prog.abap`) — 6 outbound dependencies
2. **README.md** (`README.md`) — 5 outbound dependencies
3. **main-build.yml** (`.github/workflows/main-build.yml`) — 4 outbound dependencies
4. **express.mjs** (`test/express.mjs`) — 4 outbound dependencies
5. **ajson_mirror.yaml** (`.github/workflows/ajson_mirror.yaml`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `resolve` **(Many-Argument Workhorses)** (@ `src/objects/core/zcl_abapgit_dependencies.clas.abap`) -> Impact: **114.2** | LOC: 138
- `render_repo_top` **(Many-Argument Workhorses)** (@ `src/ui/lib/zcl_abapgit_gui_chunk_lib.clas.abap`) -> Impact: **79.6** | LOC: 137
- `any_to_abap` **(Many-Argument Workhorses)** (@ `src/json/zcl_abapgit_ajson.clas.locals_imp.abap`) -> Impact: **78.7** | LOC: 154
- `test` **(I/O & Config Routines)** (@ `src/diff/diff3/zcl_abapgit_diff3.clas.testclasses.abap`) -> Impact: **77.7** | LOC: 633
- `convert_value` **(Many-Argument Workhorses)** (@ `src/json/zcl_abapgit_ajson.clas.locals_imp.abap`) -> Impact: **66.9** | LOC: 78
- `serialize_type` **(Many-Argument Workhorses)** (@ `src/objects/tabl/zcl_abapgit_object_tabl_ddl.clas.abap`) -> Impact: **62.8** | LOC: 78
- `render_field` **(Many-Argument Workhorses)** (@ `src/ui/lib/zcl_abapgit_html_form.clas.abap`) -> Impact: **62.8** | LOC: 130
- `prioritize_deser` **(Many-Argument Workhorses)** (@ `src/objects/core/zcl_abapgit_file_deserialize.clas.abap`) -> Impact: **58.2** | LOC: 125
- `find_up_to_date` **(Many-Argument Workhorses)** (@ `src/ui/flow/zcl_abapgit_flow_git.clas.abap`) -> Impact: **53.6** | LOC: 93
- `check_report_status` **(Many-Argument Workhorses)** (@ `src/git/zcl_abapgit_git_transport.clas.abap`) -> Impact: **51.9** | LOC: 77

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/objects` | 321 | 18574.78 | 12.82% | 37.36% |
| `__monolith__` | 8 | 5049.94 | 0.64% | 0.0% |
| `src/json` | 36 | 3927.74 | 12.6% | 8.25% |
| `src/ui/lib` | 49 | 3459.92 | 12.83% | 6.01% |
| `src/ui` | 36 | 3434.02 | 7.41% | 14.91% |
| `src/objects/core` | 42 | 3416.22 | 14.96% | 10.8% |
| `src/ui/pages` | 43 | 3160.19 | 14.13% | 11.57% |
| `src/git` | 47 | 2682.34 | 15.89% | 4.76% |
| `src/repo` | 37 | 2261.88 | 13.53% | 8.96% |
| `src/ui/flow` | 21 | 2138.38 | 16.54% | 19.63% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `deps/cl_package_factory.clas.abap` -> **100.0%** Exposure
- `src/objects/core/zcl_abapgit_folder_logic.clas.testclasses.abap` -> **100.0%** Exposure
- `src/objects/zcl_abapgit_object_asfc.clas.abap` -> **100.0%** Exposure
- `src/objects/zcl_abapgit_object_auth.clas.abap` -> **100.0%** Exposure
- `src/objects/zcl_abapgit_object_sppf.clas.abap` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/diff/diff3/zcl_abapgit_diff3.clas.abap` -> **100.0%** Exposure
- `src/diff/zcl_abapgit_diff.clas.abap` -> **100.0%** Exposure
- `src/diff/zcl_abapgit_diff_diff3.clas.abap` -> **100.0%** Exposure
- `src/diff/zcl_abapgit_diff_std.clas.abap` -> **100.0%** Exposure
- `src/env/zcl_abapgit_abap_language_vers.clas.abap` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/ui/flow/zcl_abapgit_flow_logic.clas.testclasses.abap` -> **103** Orphaned Functions | **4** Duplicates
- `src/objects/core/zcl_abapgit_folder_logic.clas.testclasses.abap` -> **0** Orphaned Functions | **63** Duplicates
- `src/ui/pages/sett/zcl_abapgit_gui_page_sett_remo.clas.testclasses.abap` -> **47** Orphaned Functions | **0** Duplicates
- `src/objects/core/zcl_abapgit_serialize.clas.testclasses.abap` -> **44** Orphaned Functions | **2** Duplicates
- `src/repo/zcl_abapgit_repo_checksums.clas.testclasses.abap` -> **45** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `46` packages imported that bypass the Zero-Trust whitelist.

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/zabapgit_js_common.w3mi.data.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.831)
- **Top Global Matches:** file_cluster_4: 8.831, file_cluster_10: 9.091, file_cluster_15: 9.796
- **Magnitude:** 2110.68 | **LOC:** 2590 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 85.9206% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `submitSapeventForm` **(Many-Argument Workhorses)** (Impact: 38.3)
    * *Intent:* // Use a supplied form, a pre-created form or create a hidden form // and submit with sapevent
  * `mousedownEventListener` **(Defensive Guards)** (Impact: 33.2)
  * `enumerateUiActions` **(Callbacks & Closures)** (Impact: 25.9)
  * `hintActivate` **(Defensive Guards)** (Impact: 25.2)
  * `handleKey` **(Compute Cores)** (Impact: 24.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 288 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 1007
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 502`, `structural_boundaries: 394`, `args: 238`, `func_start: 179`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 6`, `state_mutation: 431`, `dead_code: 1`, `planned_debt: 3`, `unreferenced_by_name: 24`
* *Architecture:* `io: 15`, `concurrency: 3`
* *Defense:* `safety: 187`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/json/zcl_abapgit_ajson.clas.locals_imp.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.456)
- **Top Global Matches:** file_cluster_4: 6.456, file_cluster_6: 8.224, file_cluster_12: 12.924
- **Magnitude:** 1359.72 | **LOC:** 2339 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.0%), Guard Balance (formerly Safety Score) (64.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `any_to_abap` **(Many-Argument Workhorses)** (Impact: 78.7)
  * `convert_value` **(Many-Argument Workhorses)** (Impact: 66.9)
  * `value_to_abap` **(Many-Argument Workhorses)** (Impact: 44.6)
  * `get_node_type` **(Many-Argument Workhorses)** (Impact: 44.0)
  * `stringify_node` **(Many-Argument Workhorses)** (Impact: 43.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 11 instances
* *Amplified Cascading Flux:* 179 instances
* *Memory Alloc (weighted view):* 7
* *State Mutation (weighted view):* 583
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 226`, `args: 86`, `func_start: 53`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 225`, `planned_debt: 6`
* *Architecture:* `io: 4`, `api: 8`
* *Defense:* `safety: 59`, `immutability_locks: 10`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/diff/diff3/zcl_abapgit_diff3.clas.testclasses.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.008)
- **Top Global Matches:** file_cluster_8: 9.008, file_cluster_6: 14.266, file_cluster_4: 22.13
- **Magnitude:** 1131.62 | **LOC:** 3382 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (58.3%), Complexity Load (formerly Cognitive Load) (39.6%), Debt Markers (formerly Tech Debt) (12.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test` **(I/O & Config Routines)** (Impact: 77.7)
  * `diff_comm` **(I/O & Config Routines)** (Impact: 34.0)
  * `test_invert_patch` **(I/O & Config Routines)** (Impact: 33.3)
  * `test` **(I/O & Config Routines)** (Impact: 32.6)
  * `test_diff_patch` **(I/O & Config Routines)** (Impact: 31.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 213 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 685
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 492`, `args: 4`, `func_start: 28`, `class_start: 22`
* *Risk/State:* `state_mutation: 259`, `duplicate_logic: 5`
* *Architecture:* `api: 1`
* *Defense:* `test: 272`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/json/zcl_abapgit_ajson.clas.testclasses.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.624)
- **Top Global Matches:** file_cluster_15: 8.624, file_cluster_11: 8.708, file_cluster_2: 8.74
- **Magnitude:** 1021.86 | **LOC:** 5748 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.674; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (87.9%), Guard Balance (formerly Safety Score) (47.9%), Debt Markers (formerly Tech Debt) (18.0%), Complexity Load (formerly Cognitive Load) (15.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_with_type_slice` **(Many-Argument Workhorses)** (Impact: 16.0)
  * `array_to_string_table` **(I/O & Config Routines)** (Impact: 6.5)
  * `to_abap_compressed_hash` **(I/O & Config Routines)** (Impact: 5.8)
  * `to_abap_negative` **(I/O & Config Routines)** (Impact: 5.5)
  * `set_array` **(I/O & Config Routines)** (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 19 instances
* *Amplified Cascading Flux:* 14 instances
* *Memory Alloc (weighted view):* 161
* *State Mutation (weighted view):* 484
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 673`, `args: 7`, `func_start: 165`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 456`, `planned_debt: 2`, `fragile_debt: 12`, `duplicate_logic: 4`
* *Architecture:* `io: 9`, `api: 6`
* *Defense:* `safety: 99`, `test: 503`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TYPE
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/lib/zcl_abapgit_gui_chunk_lib.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.917)
- **Top Global Matches:** file_cluster_15: 6.917, file_cluster_4: 7.249, file_cluster_9: 8.216
- **Magnitude:** 798.74 | **LOC:** 1410 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 75.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render_repo_top` **(Many-Argument Workhorses)** (Impact: 79.6)
  * `render_branch_name` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `render_table_header` **(Many-Argument Workhorses)** (Impact: 32.3)
  * `render_label_list` **(Many-Argument Workhorses)** (Impact: 30.0)
  * `render_item_state` **(Many-Argument Workhorses)** (Impact: 28.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 98 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 313
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 87`, `args: 57`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `state_mutation: 117`, `dead_code: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 35`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/tabl/zcl_abapgit_object_tabl_ddl.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.473)
- **Top Global Matches:** file_cluster_8: 7.473, file_cluster_3: 17.813, file_cluster_6: 19.118
- **Magnitude:** 793.94 | **LOC:** 901 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.4%), Guard Balance (formerly Safety Score) (69.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `serialize_type` **(Many-Argument Workhorses)** (Impact: 62.8)
  * `serialize_extend` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `serialize_field_foreign_key` **(Many-Argument Workhorses)** (Impact: 38.8)
  * `serialize_top` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `serialize` **(Many-Argument Workhorses)** (Impact: 36.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 128 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 401
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 75`, `args: 33`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `state_mutation: 145`, `planned_debt: 15`
* *Architecture:* `api: 1`
* *Defense:* `safety: 41`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/routing/zcl_abapgit_gui_router.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.406)
- **Top Global Matches:** file_cluster_6: 6.406, file_cluster_4: 6.756, file_cluster_15: 14.143
- **Magnitude:** 787.82 | **LOC:** 956 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.4%), Complexity Load (formerly Cognitive Load) (64.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `repository_services` **(Many-Argument Workhorses)** (Impact: 45.8)
  * `general_page_routing` **(Many-Argument Workhorses)** (Impact: 41.9)
  * `zip_services` **(Many-Argument Workhorses)** (Impact: 34.4)
  * `git_services` **(Many-Argument Workhorses)** (Impact: 21.1)
  * `jump_object` **(Many-Argument Workhorses)** (Impact: 18.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 486
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 51`, `args: 36`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `state_mutation: 184`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 1`
* *Defense:* `safety: 19`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/diff/diff3/zcl_abapgit_diff3.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.285)
- **Top Global Matches:** file_cluster_6: 7.285, file_cluster_4: 8.325, file_cluster_15: 15.441
- **Magnitude:** 781.7 | **LOC:** 1330 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.5%), Complexity Load (formerly Cognitive Load) (61.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `zif_abapgit_diff3~lcs` **(I/O & Config Routines)** (Impact: 45.4)
  * `zif_abapgit_diff3~diff3_merge_regions` **(I/O & Config Routines)** (Impact: 29.6)
  * `zif_abapgit_diff3~diff_comm` **(I/O & Config Routines)** (Impact: 23.1)
  * `zif_abapgit_diff3~diff_indices` **(I/O & Config Routines)** (Impact: 10.9)
  * `zif_abapgit_diff3~patch` **(I/O & Config Routines)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 25 instances
* *Amplified Cascading Flux:* 159 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 547
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 175`, `args: 16`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `state_mutation: 229`, `dead_code: 1`, `unreferenced_by_name: 7`
* *Architecture:* `io: 47`, `api: 1`
* *Defense:* `safety: 16`, `immutability_locks: 1`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_objects.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.655)
- **Top Global Matches:** file_cluster_15: 6.655, file_cluster_4: 7.176, file_cluster_16: 8.229
- **Magnitude:** 670.98 | **LOC:** 1428 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 36.4%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize` **(Many-Argument Workhorses)** (Impact: 46.3)
  * `delete` **(Many-Argument Workhorses)** (Impact: 36.8)
  * `create_object` **(Many-Argument Workhorses)** (Impact: 30.1)
  * `deserialize_step` **(Many-Argument Workhorses)** (Impact: 26.8)
  * `update_original_system` **(Many-Argument Workhorses)** (Impact: 26.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 80 instances
* *Memory Alloc (weighted view):* 7
* *State Mutation (weighted view):* 306
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 99`, `args: 49`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `state_mutation: 146`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 1`
* *Defense:* `safety: 46`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/pages/diff/zcl_abapgit_gui_page_diff_base.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.125)
- **Top Global Matches:** file_cluster_15: 6.125, file_cluster_4: 7.84, file_cluster_16: 8.023
- **Magnitude:** 663.68 | **LOC:** 1494 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `append_diff` **(Many-Argument Workhorses)** (Impact: 44.0)
  * `render_lines` **(Many-Argument Workhorses)** (Impact: 26.4)
  * `render_diff_head` **(Many-Argument Workhorses)** (Impact: 25.0)
  * `calculate_diff` **(Many-Argument Workhorses)** (Impact: 22.8)
  * `render_line_split` **(Many-Argument Workhorses)** (Impact: 22.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 83 instances
* *Memory Alloc (weighted view):* 11
* *State Mutation (weighted view):* 276
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 84`, `args: 51`, `func_start: 41`, `class_start: 2`
* *Risk/State:* `state_mutation: 110`, `dead_code: 5`, `unreferenced_by_name: 4`
* *Architecture:* `io: 6`, `api: 1`
* *Defense:* `safety: 34`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/flow/zcl_abapgit_flow_logic.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.326)
- **Top Global Matches:** file_cluster_9: 6.326, file_cluster_15: 7.539, file_cluster_16: 8.583
- **Magnitude:** 639.24 | **LOC:** 1065 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (76.5%), Guard Balance (formerly Safety Score) (67.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_objects_and_files_from_tr` **(Many-Argument Workhorses)** (Impact: 35.3)
  * `try_matching_transports` **(Many-Argument Workhorses)** (Impact: 35.2)
  * `check_files` **(Many-Argument Workhorses)** (Impact: 26.2)
  * `consolidate_files` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `update_all_branches` **(Many-Argument Workhorses)** (Impact: 18.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 15 instances
* *Amplified Cascading Flux:* 94 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 334
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 139`, `args: 36`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `state_mutation: 146`, `planned_debt: 6`
* *Architecture:* `io: 22`, `api: 1`
* *Defense:* `safety: 13`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/pages/zcl_abapgit_gui_page_repo_view.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.571)
- **Top Global Matches:** file_cluster_15: 6.571, file_cluster_4: 7.628, file_cluster_16: 8.125
- **Magnitude:** 629.7 | **LOC:** 1423 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.5%), Complexity Load (formerly Cognitive Load) (52.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `zif_abapgit_gui_renderable~render` **(I/O & Config Routines)** (Impact: 28.4)
  * `apply_order_by` **(Many-Argument Workhorses)** (Impact: 24.0)
  * `zif_abapgit_gui_event_handler~on_event` **(I/O & Config Routines)** (Impact: 17.4)
  * `render_item` **(Many-Argument Workhorses)** (Impact: 16.4)
  * `build_main_toolbar` **(I/O & Config Routines)** (Impact: 15.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 83 instances
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 354
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 84`, `args: 40`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `state_mutation: 188`, `unreferenced_by_name: 4`
* *Architecture:* `io: 21`, `api: 1`
* *Defense:* `safety: 17`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_object_fugr.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.929)
- **Top Global Matches:** file_cluster_15: 6.929, file_cluster_4: 7.916, file_cluster_11: 7.965
- **Magnitude:** 564.02 | **LOC:** 1498 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.2%), Debt Markers (formerly Tech Debt) (32.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize_functions` **(Many-Argument Workhorses)** (Impact: 35.8)
  * `includes` **(Compute Cores)** (Impact: 34.6)
  * `deserialize_xml` **(Many-Argument Workhorses)** (Impact: 19.5)
  * `get_abap_version` **(Compute Cores)** (Impact: 15.6)
  * `serialize_functions` **(I/O & Config Routines)** (Impact: 15.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 75 instances
* *Concurrency (weighted view):* 19
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 107`, `args: 22`, `func_start: 35`, `class_start: 2`
* *Risk/State:* `state_mutation: 92`, `planned_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `io: 14`, `api: 1`, `concurrency: 4`
* *Defense:* `safety: 13`, `sync_locks: 4`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/pages/sett/zcl_abapgit_gui_page_sett_remo.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.078)
- **Top Global Matches:** file_cluster_4: 7.078, file_cluster_9: 8.057, file_cluster_15: 8.238
- **Magnitude:** 553.48 | **LOC:** 1102 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.4%), Complexity Load (formerly Cognitive Load) (56.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validate_form` **(Many-Argument Workhorses)** (Impact: 32.6)
  * `zif_abapgit_gui_event_handler~on_event` **(I/O & Config Routines)** (Impact: 25.6)
  * `get_form_schema` **(Many-Argument Workhorses)** (Impact: 25.0)
  * `choose_tag` **(Many-Argument Workhorses)** (Impact: 15.8)
  * `zif_abapgit_gui_hotkeys~get_hotkey_actions` **(I/O & Config Routines)** (Impact: 14.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 90 instances
* *Memory Alloc (weighted view):* 7
* *State Mutation (weighted view):* 291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 62`, `args: 23`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 111`, `planned_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `io: 7`, `api: 1`
* *Defense:* `safety: 17`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/lib/zcl_abapgit_html_form.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.116)
- **Top Global Matches:** file_cluster_4: 5.116, file_cluster_15: 8.879, file_cluster_16: 10.053
- **Magnitude:** 528.0 | **LOC:** 1102 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.4%), Guard Balance (formerly Safety Score) (59.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render_field` **(Many-Argument Workhorses)** (Impact: 62.8)
  * `render` **(Many-Argument Workhorses)** (Impact: 40.8)
  * `render_field_table` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `render_field_text` **(Many-Argument Workhorses)** (Impact: 20.2)
  * `render_field_radio` **(Many-Argument Workhorses)** (Impact: 18.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 45 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 236
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 82`, `args: 42`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `state_mutation: 146`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* `safety: 34`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/git/zcl_abapgit_git_pack.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.706)
- **Top Global Matches:** file_cluster_9: 6.706, file_cluster_15: 6.747, file_cluster_16: 7.43
- **Magnitude:** 505.5 | **LOC:** 797 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 75.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.0%), Complexity Load (formerly Cognitive Load) (62.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decode` **(Many-Argument Workhorses)** (Impact: 32.7)
  * `decode_commit` **(Many-Argument Workhorses)** (Impact: 25.7)
  * `decode_tag` **(Many-Argument Workhorses)** (Impact: 25.5)
  * `type_and_length` **(Many-Argument Workhorses)** (Impact: 24.4)
  * `get_type` **(Compute Cores)** (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 91 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 298
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 38`, `args: 25`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `state_mutation: 116`, `planned_debt: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 5`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_object_tran.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.298)
- **Top Global Matches:** file_cluster_4: 7.298, file_cluster_12: 7.887, file_cluster_15: 7.935
- **Magnitude:** 489.66 | **LOC:** 1008 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 40.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.5%), Complexity Load (formerly Cognitive Load) (74.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize_oo_transaction` **(Many-Argument Workhorses)** (Impact: 38.9)
  * `split_parameters` **(Many-Argument Workhorses)** (Impact: 35.1)
  * `zif_abapgit_object~deserialize` **(I/O & Config Routines)** (Impact: 27.6)
  * `shift_param` **(Many-Argument Workhorses)** (Impact: 25.0)
  * `set_oo_parameters` **(Compute Cores)** (Impact: 18.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Cascading Flux:* 66 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 247
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 70`, `args: 15`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 115`, `unreferenced_by_name: 12`
* *Architecture:* `io: 12`, `api: 1`
* *Defense:* `safety: 22`, `immutability_locks: 3`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_objects_program.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.117)
- **Top Global Matches:** file_cluster_4: 6.117, file_cluster_15: 8.245, file_cluster_9: 9.299
- **Magnitude:** 476.18 | **LOC:** 1168 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.8%), Complexity Load (formerly Cognitive Load) (26.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize_dynpros` **(Many-Argument Workhorses)** (Impact: 39.9)
  * `serialize_program` **(Many-Argument Workhorses)** (Impact: 36.4)
  * `serialize_dynpros` **(Many-Argument Workhorses)** (Impact: 32.7)
  * `deserialize_textpool` **(Many-Argument Workhorses)** (Impact: 31.6)
  * `update_program` **(Many-Argument Workhorses)** (Impact: 17.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 53 instances
* *Concurrency (weighted view):* 6
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 63`, `args: 31`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 67`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 1`
* *Defense:* `safety: 16`, `sync_locks: 1`, `immutability_locks: 5`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/json/zcl_abapgit_ajson.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.25)
- **Top Global Matches:** file_cluster_15: 6.25, file_cluster_11: 6.635, file_cluster_12: 7.666
- **Magnitude:** 454.12 | **LOC:** 1023 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.6%), Guard Balance (formerly Safety Score) (63.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `zif_abapgit_ajson~set` **(I/O & Config Routines)** (Impact: 15.5)
  * `zif_abapgit_ajson~setx` **(I/O & Config Routines)** (Impact: 15.5)
  * `create_from` **(Many-Argument Workhorses)** (Impact: 15.1)
  * `delete_subtree` **(Many-Argument Workhorses)** (Impact: 15.0)
  * `prove_path_exists` **(Many-Argument Workhorses)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 65 instances
* *Memory Alloc (weighted view):* 11
* *State Mutation (weighted view):* 251
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 128`, `args: 17`, `func_start: 47`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 121`, `planned_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `io: 7`, `api: 1`
* *Defense:* `safety: 26`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/routing/zcl_abapgit_services_repo.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.432)
- **Top Global Matches:** file_cluster_15: 5.432, file_cluster_16: 6.966, file_cluster_2: 7.509
- **Magnitude:** 437.98 | **LOC:** 977 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `popup_decisions` **(Many-Argument Workhorses)** (Impact: 25.7)
  * `popup_data_loss_overwrite` **(Many-Argument Workhorses)** (Impact: 18.7)
  * `popup_delete_tabl_data` **(Many-Argument Workhorses)** (Impact: 18.7)
  * `purge` **(Many-Argument Workhorses)** (Impact: 17.6)
  * `popup_objects_overwrite` **(Many-Argument Workhorses)** (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 228
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 59`, `args: 27`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `state_mutation: 120`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 1`
* *Defense:* `safety: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/git/zcl_abapgit_git_porcelain.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.792)
- **Top Global Matches:** file_cluster_15: 5.792, file_cluster_16: 7.208, file_cluster_9: 7.772
- **Magnitude:** 421.54 | **LOC:** 837 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.6%), Complexity Load (formerly Cognitive Load) (49.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `receive_pack_push` **(Many-Argument Workhorses)** (Impact: 37.2)
  * `push` **(Many-Argument Workhorses)** (Impact: 29.8)
  * `walk` **(Many-Argument Workhorses)** (Impact: 18.4)
  * `walk_tree` **(Many-Argument Workhorses)** (Impact: 17.8)
  * `create_tag` **(Many-Argument Workhorses)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 57 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 215
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 45`, `args: 29`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `state_mutation: 101`, `planned_debt: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 8`, `immutability_locks: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/zcl_abapgit_popups.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.005)
- **Top Global Matches:** file_cluster_4: 7.005, file_cluster_15: 8.95, file_cluster_16: 9.157
- **Magnitude:** 407.3 | **LOC:** 937 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.2%), Complexity Load (formerly Cognitive Load) (49.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `zif_abapgit_popups~branch_list_popup` **(I/O & Config Routines)** (Impact: 38.9)
  * `_popup_3_get_values` **(Many-Argument Workhorses)** (Impact: 20.4)
  * `zif_abapgit_popups~popup_to_select_labels` **(I/O & Config Routines)** (Impact: 11.9)
  * `zif_abapgit_popups~tag_list_popup` **(I/O & Config Routines)** (Impact: 11.6)
  * `center` **(Many-Argument Workhorses)** (Impact: 11.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 59 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 233
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 62`, `args: 9`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `state_mutation: 115`, `unreferenced_by_name: 13`
* *Architecture:* `io: 6`, `api: 1`
* *Defense:* `safety: 24`, `immutability_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_object_intf.clas.locals_imp.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.744)
- **Top Global Matches:** file_cluster_15: 6.744, file_cluster_11: 7.127, file_cluster_2: 7.13
- **Magnitude:** 403.14 | **LOC:** 746 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.0%), Complexity Load (formerly Cognitive Load) (52.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_abapgit_descriptions` **(Many-Argument Workhorses)** (Impact: 23.5)
  * `get_methods` **(I/O & Config Routines)** (Impact: 8.7)
  * `deserialize_translation` **(Many-Argument Workhorses)** (Impact: 7.5)
  * `serialize_translations` **(Many-Argument Workhorses)** (Impact: 6.2)
  * `set_methods` **(I/O & Config Routines)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 65 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 290
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 64`, `args: 31`, `func_start: 21`, `class_start: 6`
* *Risk/State:* `state_mutation: 160`, `unreferenced_by_name: 2`
* *Architecture:* `io: 20`, `api: 3`
* *Defense:* `safety: 13`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/core/zcl_abapgit_serialize.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.1)
- **Top Global Matches:** file_cluster_15: 6.1, file_cluster_16: 7.45, file_cluster_9: 8.115
- **Magnitude:** 396.1 | **LOC:** 779 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 75.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.0%), Complexity Load (formerly Cognitive Load) (56.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filter_ignored_objects` **(Many-Argument Workhorses)** (Impact: 32.9)
  * `determine_max_processes` **(Many-Argument Workhorses)** (Impact: 20.9)
  * `run_parallel` **(Many-Argument Workhorses)** (Impact: 20.6)
  * `filter_unsupported_objects` **(Compute Cores)** (Impact: 18.0)
  * `serialize` **(Many-Argument Workhorses)** (Impact: 13.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 59 instances
* *Concurrency (weighted view):* 6
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 62`, `args: 25`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `state_mutation: 81`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 1`, `concurrency: 1`
* *Defense:* `safety: 19`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/objects/zcl_abapgit_object_ueno.clas.abap` (ABAP) | Magnitude: 220.04 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 488, core_var_decl: 149, design_snake_case: 149, state_mutation: 76
- `src/objects/aff/zcl_abapgit_json_path.clas.locals_imp.abap` (ABAP) | Magnitude: 147.02 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 292, core_var_decl: 83, design_snake_case: 83, state_mutation: 39
- `src/repo/zcl_abapgit_repo_online.clas.abap` (ABAP) | Magnitude: 188.44 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 308, core_var_decl: 103, design_snake_case: 103, state_mutation: 49
- `src/objects/zcl_abapgit_object_suso.clas.abap` (ABAP) | Magnitude: 113.86 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 324, core_var_decl: 113, design_snake_case: 111, structural_boundaries: 40
- `src/objects/oo/zcl_abapgit_oo_interface.clas.abap` (ABAP) | Magnitude: 111.7 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 301, core_var_decl: 120, design_snake_case: 111, structural_boundaries: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/utils/zcl_abapgit_string_map.clas.abap` (ABAP) | Magnitude: 115.06 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 179, core_var_decl: 37, design_snake_case: 37, structural_boundaries: 31
- `src/objects/rules/zcl_abapgit_field_rules.clas.abap` (ABAP) | Magnitude: 65.46 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 94, core_var_decl: 23, design_snake_case: 23, structural_boundaries: 19
- `src/objects/zcl_abapgit_object_bdef.clas.abap` (ABAP) | Magnitude: 136.76 | Delta: **0.136** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 464, core_var_decl: 126, design_snake_case: 126, pointers: 122

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `test/setup.mjs` (JAVASCRIPT) | Magnitude: 23.44 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 5, concurrency: 4, indent_spaces: 4, sec_db_hooks: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/ui/pages/codi/zcl_abapgit_gui_page_syntax.clas.abap` (ABAP) | Magnitude: 39.98 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 90, core_var_decl: 19, design_snake_case: 19, state_mutation: 16
- `src/objects/core/zcl_abapgit_objects_files.clas.testclasses.abap` (ABAP) | Magnitude: 69.98 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 170, core_var_decl: 55, design_snake_case: 55, state_mutation: 38
- `src/persist/zcl_abapgit_persistence_repo.clas.abap` (ABAP) | Magnitude: 137.96 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 254, core_var_decl: 81, design_snake_case: 81, structural_boundaries: 48
- `src/git/zcl_abapgit_git_time.clas.abap` (ABAP) | Magnitude: 45.16 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 64, core_var_decl: 17, design_snake_case: 17, state_mutation: 11
- `src/ui/pages/zcl_abapgit_gui_page_cpackage.clas.abap` (ABAP) | Magnitude: 50.1 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 146, core_var_decl: 48, design_snake_case: 48, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/json/zcl_abapgit_ajson_filter_lib.clas.locals_imp.abap` (ABAP) | Magnitude: 69.08 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 92, structural_boundaries: 22, core_var_decl: 22, design_snake_case: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/ui/lib/zcl_abapgit_html_table.clas.testclasses.abap` (ABAP) | Magnitude: 77.32 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 252, core_var_decl: 85, design_snake_case: 85, pointers: 57
- `src/ui/core/zif_abapgit_gui_hotkeys.intf.abap` (ABAP) | Magnitude: 15.38 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 3, args: 1, class_start: 1
- `deps/seop.type.abap` (ABAP) | Magnitude: 12.6 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: immutability_locks: 4
- `src/ui/core/zcl_abapgit_gui_css_processor.clas.testclasses.abap` (ABAP) | Magnitude: 33.0 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 248, core_var_decl: 57, design_snake_case: 57, test: 27
- `src/objects/aff/zcl_abapgit_object_cdbo.clas.abap` (ABAP) | Magnitude: 10.7 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 36, core_var_decl: 9, design_snake_case: 9, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `src/objects/aff/zcl_abapgit_object_bgqc.clas.abap` (ABAP) | Magnitude: 12.8 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 9, pointers: 8, core_var_decl: 6
- `src/data/zcl_abapgit_data_serializer.clas.abap` (ABAP) | Magnitude: 53.98 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 100, core_var_decl: 24, design_snake_case: 24, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/objects/aff/zcl_abapgit_object_chkc.clas.abap` (ABAP) | Magnitude: 11.96 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 39, pointers: 13, core_var_decl: 9, design_snake_case: 9
- `src/objects/aff/zcl_abapgit_object_chko.clas.abap` (ABAP) | Magnitude: 12.08 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 40, pointers: 13, core_var_decl: 9, design_snake_case: 9
- `src/objects/aff/zcl_abapgit_object_chkv.clas.abap` (ABAP) | Magnitude: 12.08 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 40, pointers: 13, core_var_decl: 9, design_snake_case: 9
- `deps/if_package.intf.abap` (ABAP) | Magnitude: 17.14 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 105, args: 20, structural_boundaries: 9, safety: 8
- `src/objects/aff/zcl_abapgit_object_eeec.clas.abap` (ABAP) | Magnitude: 8.94 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 43, pointers: 12, core_var_decl: 10, design_snake_case: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/git/zcl_abapgit_git_pack.clas.abap` (ABAP) | Magnitude: 505.5 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 586, core_var_decl: 166, design_snake_case: 166, state_mutation: 116

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/repo/zcl_abapgit_repo.clas.abap` -> Churn: **85.25%** | Cog Load: 67.2981% | Debt: 9.4893%
- `src/ui/zabapgit_js_common.w3mi.data.js` -> Churn: **84.19%** | Cog Load: 86.2391% | Debt: 38.9846%
- `src/ui/flow/zcl_abapgit_flow_logic.clas.testclasses.abap` -> Churn: **80.33%** | Cog Load: 19.7312% | Debt: 100.0%
- `src/objects/zcl_abapgit_object_tran.clas.abap` -> Churn: **77.52%** | Cog Load: 74.7232% | Debt: 28.1406%
- `src/ui/flow/zcl_abapgit_flow_logic.clas.abap` -> Churn: **76.54%** | Cog Load: 61.5862% | Debt: 10.5738%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/json/zcl_abapgit_ajson.clas.locals_imp.abap` -> **Marc Bernard** (100.0% isolated ownership) | Magnitude: 1359.72
- `src/json/zcl_abapgit_ajson.clas.testclasses.abap` -> **github-actions[bot]** (100.0% isolated ownership) | Magnitude: 1021.86
- `src/objects/tabl/zcl_abapgit_object_tabl_ddl.clas.abap` -> **Marc Bernard** (100.0% isolated ownership) | Magnitude: 793.94
- `src/ui/flow/zcl_abapgit_flow_logic.clas.abap` -> **Lars Hvam** (100.0% isolated ownership) | Magnitude: 639.24
- `src/objects/zcl_abapgit_object_fugr.clas.abap` -> **Marc Bernard** (100.0% isolated ownership) | Magnitude: 564.02

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/zabapgit_password_dialog.prog.abap` -> **Severity: 0.04** (Embedded: 0.0007 * Error Risk: 59.5681%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/zabapgit_password_dialog.prog.abap` -> **Severity: 124.7** (Blast Radius: 1.247 * Doc Risk: 100.0%)
- `deps/cl_package_factory.clas.abap` -> **Severity: 67.4** (Blast Radius: 0.674 * Doc Risk: 100.0%)
- `deps/cl_package_helper.clas.abap` -> **Severity: 67.4** (Blast Radius: 0.674 * Doc Risk: 100.0%)
- `src/apack/zcl_abapgit_apack_helper.clas.abap` -> **Severity: 67.4** (Blast Radius: 0.674 * Doc Risk: 100.0%)
- `src/apack/zcl_abapgit_apack_migration.clas.abap` -> **Severity: 67.4** (Blast Radius: 0.674 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 770 call pairs -- scoped 4.0%, unique 0.1%, ambiguous 0.0%, external 95.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 507 | 5.9% | 0.0% | 0.0% | 94.1% |
| abap | 253 | 0.4% | 0.4% | 0.0% | 99.2% |
| shell | 10 | 0.0% | 0.0% | 0.0% | 100.0% |

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
