# ARCHITECTURAL_BRIEF: abapGit
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/abapGit/abapGit` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 1508 |
| Analyzed Artifacts (Scanned) | 1461 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 47 |
| Total LOC | 149703 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 96.9% |
| Dominant Lang | ABAP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ABAP | 727 | 144616 | 49.8% |
| XML | 704 | 4 | 48.2% |
| CSS | 7 | 2236 | 0.5% |
| MARKDOWN | 5 | 0 | 0.3% |
| SHELL | 4 | 77 | 0.3% |
| JAVASCRIPT | 4 | 1931 | 0.3% |
| PLAINTEXT | 4 | 1 | 0.3% |
| JSON | 3 | 803 | 0.2% |
| TYPESCRIPT | 2 | 29 | 0.1% |
| YAML | 1 | 6 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Mainframe / COBOL & Config` (z +1.59; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 50%, I/O & Config Routines Files 20%, Declarative / Non-Code 8%, Large Core Modules 7%, Interface Declarations Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1451 | 99.3% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 0.5% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 47*

**Composition by Extension & Reason:**
- `.abap`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 55 LOC)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2176 LOC)
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.woff`: 1x Excluded (Explicitly Denied Extension: '.woff')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 87.3 | 10.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 27.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 14.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 16.2 | 0.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 33.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 68.3 | 0.6 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 50.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.4 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 88.8 | 4.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 42.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 15794 | 611 | 34 | `src/json/zcl_abapgit_ajson.clas.testclasses.abap` |
| cleanup | 866 | 258 | 2 | `src/objects/tabl/zcl_abapgit_object_tabl.clas.abap` |
| guards | 5705 | 641 | 12 | `src/ui/zabapgit_js_common.w3mi.data.js` |
| danger | 1048 | 138 | 0 | `src/diff/diff3/zcl_abapgit_diff3.clas.testclasses.abap` |
| concurrency | 129 | 34 | 0 | `test/gitea/tests/gitea.spec.ts` |
| connectivity | 698 | 542 | 1 | `src/ui/zabapgit_css_theme_belize_blue.w3mi.data.css` |
| io | 1055 | 244 | 2 | `src/diff/diff3/zcl_abapgit_diff3.clas.abap` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `test/gitea/create.sh` |
| time | 4 | 1 | 0 | `src/ui/zabapgit_js_common.w3mi.data.js` |
| serialization | 5 | 1 | 0 | `src/ui/zabapgit_js_common.w3mi.data.js` |
| regex | 30 | 2 | 0 | `src/ui/zabapgit_js_common.w3mi.data.js` |
| events | 49 | 10 | 0 | `src/ui/zabapgit_js_common.w3mi.data.js` |
| tests | 3369 | 143 | 0 | `src/json/zcl_abapgit_ajson.clas.testclasses.abap` |
| docs | 107 | 11 | 0 | `src/cts/zcl_abapgit_cts_api.clas.abap` |
| debt | 411 | 112 | 0 | `src/objects/core/zcl_abapgit_folder_logic.clas.testclasses.abap` |
| mutation | 61188 | 669 | 126 | `src/json/zcl_abapgit_ajson.clas.testclasses.abap` |
| dead_code | 3036 | 342 | 12 | `src/ui/flow/zcl_abapgit_flow_logic.clas.testclasses.abap` |
| credential | 2 | 2 | 0 | `src/git/zcl_abapgit_git_commit.clas.testclasses.abap` |
| threat | 308 | 29 | 0 | `src/ui/zabapgit_js_common.w3mi.data.js` |
| ml_ai | 1481 | 134 | 0 | `src/json/zcl_abapgit_ajson.clas.testclasses.abap` |
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
2. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 0 inbound connections
3. **README.md** (`README.md`) — 0 inbound connections
4. **SECURITY.md** (`SECURITY.md`) — 0 inbound connections
5. **README.md** (`test/README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **zabapgit.prog.abap** (`src/zabapgit.prog.abap`) — 6 outbound dependencies
2. **README.md** (`README.md`) — 5 outbound dependencies
3. **express.mjs** (`test/express.mjs`) — 4 outbound dependencies
4. **zabapgit_parallel.fugr.saplzabapgit_parallel.abap** (`src/objects/core/zabapgit_parallel.fugr.saplzabapgit_parallel.abap`) — 2 outbound dependencies
5. **eslint.config.mjs** (`eslint.config.mjs`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `resolve` **(Many-Argument Workhorses)** (@ `src/objects/core/zcl_abapgit_dependencies.clas.abap`) -> Impact: **114.2** | LOC: 138
- `render_repo_top` **(Many-Argument Workhorses)** (@ `src/ui/lib/zcl_abapgit_gui_chunk_lib.clas.abap`) -> Impact: **79.6** | LOC: 137
- `any_to_abap` **(Many-Argument Workhorses)** (@ `src/json/zcl_abapgit_ajson.clas.locals_imp.abap`) -> Impact: **78.7** | LOC: 154
- `test` **(I/O & Config Routines)** (@ `src/diff/diff3/zcl_abapgit_diff3.clas.testclasses.abap`) -> Impact: **77.7** | LOC: 633
- `convert_value` **(Many-Argument Workhorses)** (@ `src/json/zcl_abapgit_ajson.clas.locals_imp.abap`) -> Impact: **66.9** | LOC: 78
- `serialize_type` **(Compute Cores)** (@ `src/objects/tabl/zcl_abapgit_object_tabl_ddl.clas.abap`) -> Impact: **62.8** | LOC: 78
- `render_field` **(Many-Argument Workhorses)** (@ `src/ui/lib/zcl_abapgit_html_form.clas.abap`) -> Impact: **62.8** | LOC: 130
- `prioritize_deser` **(Many-Argument Workhorses)** (@ `src/objects/core/zcl_abapgit_file_deserialize.clas.abap`) -> Impact: **58.2** | LOC: 125
- `find_up_to_date` **(Many-Argument Workhorses)** (@ `src/ui/flow/zcl_abapgit_flow_git.clas.abap`) -> Impact: **53.6** | LOC: 93
- `check_report_status` **(Many-Argument Workhorses)** (@ `src/git/zcl_abapgit_git_transport.clas.abap`) -> Impact: **51.9** | LOC: 77

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/objects` | 321 | 18574.78 | 12.82% | 37.57% |
| `__monolith__` | 8 | 5049.94 | 0.64% | 0.0% |
| `src/json` | 36 | 3927.74 | 12.6% | 9.35% |
| `src/ui/lib` | 49 | 3459.92 | 12.83% | 6.37% |
| `src/ui` | 36 | 3457.02 | 7.4% | 15.09% |
| `src/objects/core` | 42 | 3416.22 | 14.96% | 11.69% |
| `src/ui/pages` | 43 | 3160.19 | 14.13% | 12.93% |
| `src/git` | 47 | 2682.34 | 15.89% | 5.04% |
| `src/repo` | 37 | 2261.88 | 13.53% | 9.31% |
| `src/ui/flow` | 21 | 2138.38 | 16.54% | 20.47% |

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
- `src/git/zcl_abapgit_git_branch_utils.clas.abap` -> **100.0%** Exposure
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
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `34` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/ui/zabapgit_js_common.w3mi.data.js` (JAVASCRIPT) -> Cumulative Risk: **684.19**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +1.68)
- **Magnitude:** 2133.68 | **LOC:** 2590 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (89.852%), Documentation (86.7704%)
- **Heaviest Functions:** `submitSapeventForm` (Many-Argument Workhorses, Impact: 38.3), `mousedownEventListener` (Defensive Guards, Impact: 33.2), `enumerateUiActions` (Callbacks & Closures, Impact: 26.9)

### 2. `src/objects/zcl_abapgit_object_sobj.clas.abap` (ABAP) -> Cumulative Risk: **681.0**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +2.38)
- **Magnitude:** 107.18 | **LOC:** 256 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.714%), Tech Debt (99.3566%)
- **Heaviest Functions:** `is_program_locked` (Defensive Guards, Impact: 7.0), `is_objtype_locked` (I/O & Config Routines, Impact: 5.4), `get_field_rules` (I/O & Config Routines, Impact: 2.9)

### 3. `src/json/zcl_abapgit_ajson_mapping.clas.locals_imp.abap` (ABAP) -> Cumulative Risk: **660.17**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +2.07)
- **Magnitude:** 147.9 | **LOC:** 342 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9992%), Tech Debt (99.921%)
- **Heaviest Functions:** `zif_abapgit_ajson_mapping~rename_node` (I/O & Config Routines, Impact: 11.8), `zif_abapgit_ajson_mapping~to_json` (I/O & Config Routines, Impact: 6.8), `zif_abapgit_ajson_mapping~rename_node` (I/O & Config Routines, Impact: 5.3)

### 4. `src/diff/zcl_abapgit_diff.clas.abap` (ABAP) -> Cumulative Risk: **645.0**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +1.46)
- **Magnitude:** 148.88 | **LOC:** 284 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (91.7659%)
- **Heaviest Functions:** `shortlist` (I/O & Config Routines, Impact: 13.8), `map_beacons` (I/O & Config Routines, Impact: 12.8), `calculate_stats` (I/O & Config Routines, Impact: 6.8)

### 5. `src/utils/zcl_abapgit_log.clas.abap` (ABAP) -> Cumulative Risk: **642.01**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +1.46)
- **Magnitude:** 222.76 | **LOC:** 328 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (95.552%)
- **Heaviest Functions:** `get_messages_status` (Compute Cores, Impact: 21.9), `zif_abapgit_log~get_status` (I/O & Config Routines, Impact: 12.2), `zif_abapgit_log~add` (I/O & Config Routines, Impact: 7.2)

### 6. `src/ui/core/zcl_abapgit_html.clas.abap` (ABAP) -> Cumulative Risk: **640.89**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +2.54)
- **Magnitude:** 367.68 | **LOC:** 668 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9994%), Cognitive Load (87.3449%)
- **Heaviest Functions:** `study_line` (Many-Argument Workhorses, Impact: 42.0), `indent_line` (Compute Cores, Impact: 38.5), `zif_abapgit_html~a` (I/O & Config Routines, Impact: 20.6)

### 7. `src/objects/zcl_abapgit_object_tran.clas.abap` (ABAP) -> Cumulative Risk: **633.34**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.41)
- **Magnitude:** 489.66 | **LOC:** 1008 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9969%), Safety Score (84.5269%)
- **Heaviest Functions:** `deserialize_oo_transaction` (Many-Argument Workhorses, Impact: 38.9), `split_parameters` (Many-Argument Workhorses, Impact: 35.1), `zif_abapgit_object~deserialize` (I/O & Config Routines, Impact: 27.6)

### 8. `src/objects/zcl_abapgit_object_prog.clas.abap` (ABAP) -> Cumulative Risk: **632.98**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.47)
- **Magnitude:** 102.36 | **LOC:** 357 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (97.6671%), Tech Debt (97.0327%)
- **Heaviest Functions:** `serialize_texts` (Many-Argument Workhorses, Impact: 10.0), `zif_abapgit_object~deserialize` (I/O & Config Routines, Impact: 7.0), `zif_abapgit_object~delete` (I/O & Config Routines, Impact: 5.5)

### 9. `src/objects/zcl_abapgit_object_nrob.clas.abap` (ABAP) -> Cumulative Risk: **631.59**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +2.61)
- **Magnitude:** 156.44 | **LOC:** 412 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.953%), Tech Debt (87.2747%)
- **Heaviest Functions:** `zif_abapgit_object~deserialize` (I/O & Config Routines, Impact: 19.8), `zif_abapgit_object~serialize` (I/O & Config Routines, Impact: 19.2), `delete_intervals` (I/O & Config Routines, Impact: 9.3)

### 10. `src/objects/zcl_abapgit_object_scvi.clas.abap` (ABAP) -> Cumulative Risk: **628.78**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +3.33)
- **Magnitude:** 70.8 | **LOC:** 222 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9089%), State Flux (99.5195%)
- **Heaviest Functions:** `zif_abapgit_object~deserialize` (I/O & Config Routines, Impact: 4.0), `zif_abapgit_object~serialize` (I/O & Config Routines, Impact: 4.0), `zif_abapgit_object~delete` (I/O & Config Routines, Impact: 3.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/zabapgit_js_common.w3mi.data.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2133.68 | **LOC:** 2590 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (85.8479%), Tech Debt (40.4293%)
**Top Internal Functions/Classes:**
  * `submitSapeventForm` **(Many-Argument Workhorses)** (Impact: 38.3)
    * *Intent:* // Use a supplied form, a pre-created form or create a hidden form // and submit with sapevent
  * `mousedownEventListener` **(Defensive Guards)** (Impact: 33.2)
  * `enumerateUiActions` **(Callbacks & Closures)** (Impact: 26.9)
  * `hintActivate` **(Defensive Guards)** (Impact: 25.2)
  * `handleKey` **(Compute Cores)** (Impact: 24.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 292 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 1015
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 512`, `structural_boundaries: 394`, `args: 238`, `func_start: 179`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 6`, `state_mutation: 431`, `dead_code: 9`, `planned_debt: 3`, `unreferenced_by_name: 24`
* *Architecture:* `io: 15`, `concurrency: 3`
* *Defense:* `safety: 187`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/json/zcl_abapgit_ajson.clas.locals_imp.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1359.72 | **LOC:** 2339 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (65.0241%), Tech Debt (8.9436%)
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
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 225`, `dead_code: 1`, `planned_debt: 6`
* *Architecture:* `io: 4`, `api: 8`
* *Defense:* `safety: 59`, `immutability_locks: 10`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/diff/diff3/zcl_abapgit_diff3.clas.testclasses.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1131.62 | **LOC:** 3382 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.595%), Tech Debt (12.1567%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/json/zcl_abapgit_ajson.clas.testclasses.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1021.86 | **LOC:** 5748 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (15.7423%), Tech Debt (18.1398%)
**Top Internal Functions/Classes:**
  * `set_with_type_slice` **(Many-Argument Workhorses)** (Impact: 16.0)
  * `array_to_string_table` **(Tests & Verification)** (Impact: 6.5)
  * `to_abap_compressed_hash` **(Tests & Verification)** (Impact: 5.8)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TYPE
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/lib/zcl_abapgit_gui_chunk_lib.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 798.74 | **LOC:** 1410 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (44.6649%), Tech Debt (0.0%)
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
* *Risk/State:* `state_mutation: 117`, `dead_code: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 35`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/tabl/zcl_abapgit_object_tabl_ddl.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 793.94 | **LOC:** 901 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (71.4478%), Tech Debt (19.0242%)
**Top Internal Functions/Classes:**
  * `serialize_type` **(Compute Cores)** (Impact: 62.8)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/routing/zcl_abapgit_gui_router.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 787.82 | **LOC:** 956 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (64.7821%), Tech Debt (10.304%)
**Top Internal Functions/Classes:**
  * `repository_services` **(Many-Argument Workhorses)** (Impact: 45.8)
  * `general_page_routing` **(Compute Cores)** (Impact: 41.9)
  * `zip_services` **(Many-Argument Workhorses)** (Impact: 34.4)
  * `git_services` **(Compute Cores)** (Impact: 21.1)
  * `jump_object` **(Many-Argument Workhorses)** (Impact: 18.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 486
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 51`, `args: 36`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `state_mutation: 184`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 1`
* *Defense:* `safety: 19`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/diff/diff3/zcl_abapgit_diff3.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 781.7 | **LOC:** 1330 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (61.8953%), Tech Debt (15.0751%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_objects.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 670.98 | **LOC:** 1428 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 30.8%
- **Risk Profile:** Cognitive Load (43.3741%), Tech Debt (8.8542%)
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
* *Risk/State:* `state_mutation: 146`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 1`
* *Defense:* `safety: 46`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/pages/diff/zcl_abapgit_gui_page_diff_base.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 663.68 | **LOC:** 1494 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (36.7261%), Tech Debt (10.7312%)
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
* *Risk/State:* `state_mutation: 110`, `dead_code: 6`, `unreferenced_by_name: 4`
* *Architecture:* `io: 6`, `api: 1`
* *Defense:* `safety: 34`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/flow/zcl_abapgit_flow_logic.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 639.24 | **LOC:** 1065 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (61.5862%), Tech Debt (10.8648%)
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
* *Risk/State:* `state_mutation: 146`, `dead_code: 1`, `planned_debt: 6`
* *Architecture:* `io: 22`, `api: 1`
* *Defense:* `safety: 13`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/pages/zcl_abapgit_gui_page_repo_view.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 629.7 | **LOC:** 1423 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (52.3316%), Tech Debt (10.9561%)
**Top Internal Functions/Classes:**
  * `zif_abapgit_gui_renderable~render` **(I/O & Config Routines)** (Impact: 28.4)
  * `apply_order_by` **(Many-Argument Workhorses)** (Impact: 24.0)
  * `zif_abapgit_gui_event_handler~on_event` **(I/O & Config Routines)** (Impact: 17.4)
  * `render_item` **(Many-Argument Workhorses)** (Impact: 16.4)
  * `build_main_toolbar` **(Compute Cores)** (Impact: 15.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 83 instances
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 354
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 84`, `args: 40`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `state_mutation: 188`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 21`, `api: 1`
* *Defense:* `safety: 17`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_object_fugr.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 564.02 | **LOC:** 1498 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (32.1589%), Tech Debt (33.5276%)
**Top Internal Functions/Classes:**
  * `deserialize_functions` **(Many-Argument Workhorses)** (Impact: 35.8)
  * `includes` **(Compute Cores)** (Impact: 34.6)
  * `deserialize_xml` **(Many-Argument Workhorses)** (Impact: 19.5)
  * `get_abap_version` **(Compute Cores)** (Impact: 15.6)
  * `serialize_functions` **(Compute Cores)** (Impact: 15.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 75 instances
* *Concurrency (weighted view):* 19
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 107`, `args: 22`, `func_start: 35`, `class_start: 2`
* *Risk/State:* `state_mutation: 92`, `dead_code: 4`, `planned_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `io: 14`, `api: 1`, `concurrency: 4`
* *Defense:* `safety: 13`, `sync_locks: 4`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/pages/sett/zcl_abapgit_gui_page_sett_remo.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 553.48 | **LOC:** 1102 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.8183%), Tech Debt (14.8159%)
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
* *Risk/State:* `state_mutation: 111`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `io: 7`, `api: 1`
* *Defense:* `safety: 17`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/lib/zcl_abapgit_html_form.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 528.0 | **LOC:** 1102 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (67.3768%), Tech Debt (16.368%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/git/zcl_abapgit_git_pack.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 505.5 | **LOC:** 797 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (62.9206%), Tech Debt (8.5264%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_object_tran.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 489.66 | **LOC:** 1008 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (74.7232%), Tech Debt (28.8035%)
**Top Internal Functions/Classes:**
  * `deserialize_oo_transaction` **(Many-Argument Workhorses)** (Impact: 38.9)
  * `split_parameters` **(Many-Argument Workhorses)** (Impact: 35.1)
  * `zif_abapgit_object~deserialize` **(I/O & Config Routines)** (Impact: 27.6)
  * `shift_param` **(Compute Cores)** (Impact: 25.0)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_objects_program.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 476.18 | **LOC:** 1168 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.5108%), Tech Debt (10.9882%)
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
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 67`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 1`
* *Defense:* `safety: 16`, `sync_locks: 1`, `immutability_locks: 5`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/git/zlib/zcl_abapgit_zlib.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 457.5 | **LOC:** 472 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.1583%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `map_distance` **(Compute Cores)** (Impact: 36.4)
  * `map_length` **(Compute Cores)** (Impact: 35.3)
  * `decompress` **(Compute Cores)** (Impact: 19.4)
  * `dynamic` **(I/O & Config Routines)** (Impact: 14.6)
  * `fixed` **(I/O & Config Routines)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 96 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 318
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 27`, `args: 11`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `state_mutation: 126`
* *Architecture:* `api: 1`
* *Defense:* `safety: 6`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/json/zcl_abapgit_ajson.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 454.12 | **LOC:** 1023 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (78.6424%), Tech Debt (19.1972%)
**Top Internal Functions/Classes:**
  * `zif_abapgit_ajson~set` **(I/O & Config Routines)** (Impact: 15.5)
  * `zif_abapgit_ajson~setx` **(I/O & Config Routines)** (Impact: 15.5)
  * `create_from` **(Many-Argument Workhorses)** (Impact: 15.1)
  * `delete_subtree` **(Many-Argument Workhorses)** (Impact: 15.0)
  * `prove_path_exists` **(Compute Cores)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 65 instances
* *Memory Alloc (weighted view):* 11
* *State Mutation (weighted view):* 251
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 128`, `args: 17`, `func_start: 47`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 121`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `io: 7`, `api: 1`
* *Defense:* `safety: 26`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/routing/zcl_abapgit_services_repo.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 437.98 | **LOC:** 977 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (44.5046%), Tech Debt (8.3339%)
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
* *Risk/State:* `state_mutation: 120`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 1`
* *Defense:* `safety: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/git/zcl_abapgit_git_porcelain.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 421.54 | **LOC:** 837 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.4549%), Tech Debt (8.4465%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/zcl_abapgit_popups.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 407.3 | **LOC:** 937 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.6207%), Tech Debt (33.7957%)
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
* *Risk/State:* `state_mutation: 115`, `dead_code: 1`, `unreferenced_by_name: 13`
* *Architecture:* `io: 6`, `api: 1`
* *Defense:* `safety: 24`, `immutability_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_object_intf.clas.locals_imp.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 403.14 | **LOC:** 746 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.8226%), Tech Debt (10.6572%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/ui/flow/zcl_abapgit_flow_logic.clas.abap` -> Churn: **77.48%** | Cog Load: 61.5862% | Debt: 10.8648%
- `src/repo/zcl_abapgit_repo.clas.abap` -> Churn: **74.76%** | Cog Load: 67.2981% | Debt: 9.8454%
- `src/ui/flow/zcl_abapgit_flow_logic.clas.testclasses.abap` -> Churn: **71.07%** | Cog Load: 19.7312% | Debt: 100.0%
- `src/ui/zabapgit_js_common.w3mi.data.js` -> Churn: **70.18%** | Cog Load: 85.8479% | Debt: 40.4293%
- `src/objects/zcl_abapgit_object_tran.clas.abap` -> Churn: **64.62%** | Cog Load: 74.7232% | Debt: 28.8035%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/diff/diff3/zcl_abapgit_diff3.clas.testclasses.abap` -> **Lars Hvam** (100.0% isolated ownership) | Magnitude: 1131.62
- `src/json/zcl_abapgit_ajson.clas.testclasses.abap` -> **github-actions[bot]** (100.0% isolated ownership) | Magnitude: 1021.86
- `src/objects/tabl/zcl_abapgit_object_tabl_ddl.clas.abap` -> **Marc Bernard** (100.0% isolated ownership) | Magnitude: 793.94
- `src/diff/diff3/zcl_abapgit_diff3.clas.abap` -> **Lars Hvam** (100.0% isolated ownership) | Magnitude: 781.7
- `src/ui/flow/zcl_abapgit_flow_logic.clas.abap` -> **Lars Hvam** (100.0% isolated ownership) | Magnitude: 639.24

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `deps/cl_package_factory.clas.abap` -> **Severity: 68.4** (Blast Radius: 0.684 * Doc Risk: 100.0%)
- `deps/cl_package_helper.clas.abap` -> **Severity: 68.4** (Blast Radius: 0.684 * Doc Risk: 100.0%)
- `src/apack/zcl_abapgit_apack_helper.clas.abap` -> **Severity: 68.4** (Blast Radius: 0.684 * Doc Risk: 100.0%)
- `src/apack/zcl_abapgit_apack_migration.clas.abap` -> **Severity: 68.4** (Blast Radius: 0.684 * Doc Risk: 100.0%)
- `src/apack/zcl_abapgit_apack_reader.clas.abap` -> **Severity: 68.4** (Blast Radius: 0.684 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
