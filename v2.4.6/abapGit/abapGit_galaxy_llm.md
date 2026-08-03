# ARCHITECTURAL_BRIEF: abapGit
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/abapGit` |
| **Timestamp** | `2026-08-03T19:23:57.124863+00:00` |
| **Scan Duration** | `3.19s` |
| **Git Branch** | `main` |
| **Git Commit** | `951e2243efbf0dbbfb4978a4ffa182b77e2ee939` |
| **Git Remote** | `https://github.com/abapGit/abapGit` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 728 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 1508 |
| Analyzed Artifacts (Scanned) | 1380 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 128 |
| Total LOC | 142141 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 91.5% |
| Dominant Lang | ABAP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ABAP | 723 | 137272 | 52.4% |
| XML | 636 | 4 | 46.1% |
| CSS | 7 | 2236 | 0.5% |
| MARKDOWN | 4 | 0 | 0.3% |
| JAVASCRIPT | 3 | 1924 | 0.2% |
| PLAINTEXT | 3 | 1 | 0.2% |
| JSON | 2 | 647 | 0.1% |
| SHELL | 2 | 57 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `8.886`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1368 | 99.1% |
| file_cluster_17 | 2 | 0.1% |
| file_cluster_13 | 2 | 0.1% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 0.4% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 128*

**Composition by Extension & Reason:**
- `.xml`: 81x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.abap`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2176 LOC)
- `.json`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.woff`: 1x Excluded (Explicitly Denied Extension: '.woff')
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 97.0 | 7.2 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 2.3 | 1.7 | 0.2 |
| API Exposure | 0.0 | 17.6 | 0.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 9.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 68.3 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 55.3 | 93.3 | 100.0 |
| Instability Exposure | 0.0 | 5.4 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 82.2 | 4.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 27.4 | 14.9 | 6.7 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/diff/diff3/zcl_abapgit_diff3.clas.abap` (Hits: 47)
- `ci/deploy-release-tag.sh` (Hits: 33)
- `src/objects/zcl_abapgit_object_nspc.clas.abap` (Hits: 24)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 0 inbound connections
2. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
3. **README.md** (`README.md`) — 0 inbound connections
4. **SECURITY.md** (`SECURITY.md`) — 0 inbound connections
5. **abaplint.json** (`abaplint.json`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **zabapgit.prog.abap** (`src/zabapgit.prog.abap`) — 6 outbound dependencies
2. **express.mjs** (`test/express.mjs`) — 4 outbound dependencies
3. **eslint.config.mjs** (`eslint.config.mjs`) — 2 outbound dependencies
4. **zabapgit_parallel.fugr.saplzabapgit_parallel.abap** (`src/objects/core/zabapgit_parallel.fugr.saplzabapgit_parallel.abap`) — 2 outbound dependencies
5. **zcl_abapgit_apack_helper.clas.abap** (`src/apack/zcl_abapgit_apack_helper.clas.abap`) — 1 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `build_json` (@ `src/objects/aff/zcl_abapgit_json_path.clas.locals_imp.abap`) -> Impact: **381.0** | LOC: 295
- `parse_number` (@ `src/json/zcl_abapgit_ajson.clas.testclasses.abap`) -> Impact: **138.4** | LOC: 1482
- `enumerateUiActions` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> Impact: **84.5** | LOC: 97
- `deployHintContainers` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> Impact: **49.9** | LOC: 64
- `mousedownEventListener` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> Impact: **48.1** | LOC: 71
- `get_r3tr_obj_for_limu_obj` (@ `src/cts/zcl_abapgit_cts_api.clas.abap`) -> Impact: **41.2** | LOC: 32
- `package_to_path` (@ `src/objects/core/zcl_abapgit_folder_logic.clas.abap`) -> Impact: **40.6** | LOC: 42
- `filter_unsupported_objects` (@ `src/objects/core/zcl_abapgit_serialize.clas.abap`) -> Impact: **40.4** | LOC: 37
- `resolve_var_recursively` (@ `src/ui/core/zcl_abapgit_gui_css_processor.clas.abap`) -> Impact: **40.4** | LOC: 17
- `submitSapeventForm` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> Impact: **38.3** | LOC: 51

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `build_json` (@ `src/objects/aff/zcl_abapgit_json_path.clas.locals_imp.abap`) -> **O(2^N) [Recursive]**
- `resolve_var_recursively` (@ `src/ui/core/zcl_abapgit_gui_css_processor.clas.abap`) -> **O(2^N) [Recursive]**
- `delete_branch` (@ `src/ui/routing/zcl_abapgit_services_git.clas.abap`) -> **O(2^N) [Recursive]**
- `text` (@ `src/ui/lib/zcl_abapgit_html_form.clas.abap`) -> **O(2^N) [Recursive]**
- `run` (@ `src/background/zcl_abapgit_background.clas.abap`) -> **O(2^N) [Recursive]**
- `walk_tree` (@ `src/git/zcl_abapgit_git_porcelain.clas.abap`) -> **O(2^N) [Recursive]**
- `to_json` (@ `src/json/zcl_abapgit_ajson_mapping.clas.testclasses.abap`) -> **O(2^N) [Recursive]**
- `walk_tree` (@ `src/ui/flow/zcl_abapgit_flow_git.clas.locals_imp.abap`) -> **O(2^N) [Recursive]**
- `push` (@ `src/repo/zcl_abapgit_repo_online.clas.abap`) -> **O(2^N) [Recursive]**
- `bind` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /* exported preparePatch */ /* exported registerStagePatch */ /* exported toggleRepoListDetail */ /* exported onTagTypeChange */ /* exported getIndocS...

### Highest Data Gravity (Database Complexity)
- `handleKey` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> DB Complexity: **25**
  * *Intent:* // does not work if inside the input node
- `mousedownEventListener` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> DB Complexity: **20**
- `StageHelper` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> DB Complexity: **20**
- `onPageLoad` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> DB Complexity: **19**
- `DiffHelper` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> DB Complexity: **18**
- `setHooks` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> DB Complexity: **16**
- `onStage` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> DB Complexity: **15**
- `CommandPalette` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> DB Complexity: **14**
- `deserialize_nested_arrays` (@ `src/objects/aff/zcl_abapgit_json_path.clas.testclasses.abap`) -> DB Complexity: **14**
- `enumerateUiActions` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> DB Complexity: **13**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/objects` | 321 | 43529.24 | 7.06% | 4.58% |
| `src/ui/flow` | 21 | 6851.7 | 7.82% | 4.84% |
| `src/objects/ecatt` | 33 | 5927.12 | 6.65% | 0.0% |
| `src/diff/diff3` | 6 | 5831.94 | 6.65% | 0.0% |
| `src/objects/texts` | 29 | 5617.83 | 7.68% | 2.06% |
| `src/utils` | 24 | 5469.04 | 6.46% | 2.32% |
| `src/git/zlib` | 10 | 5266.9 | 12.63% | 0.0% |
| `__monolith__` | 8 | 5049.94 | 0.78% | 0.0% |
| `src` | 24 | 4888.84 | 6.33% | 0.0% |
| `src/repo` | 37 | 4662.93 | 6.64% | 2.83% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `ci/deploy-release-tag.sh` -> **100.0%** Exposure
- `ci/push-tag.sh` -> **100.0%** Exposure
- `src/objects/core/zabapgit_parallel.fugr.saplzabapgit_parallel.abap` -> **100.0%** Exposure
- `src/xml/zif_abapgit_xml_input.intf.abap` -> **99.9955%** Exposure
- `src/ui/pages/zcl_abapgit_gui_page_repo_over.clas.locals_imp.abap` -> **98.9013%** Exposure
### Highest State Flux (Mutation/Volatility)
- `ci/deploy-release-tag.sh` -> **100.0%** Exposure
- `src/ui/zabapgit_js_common.w3mi.data.js` -> **100.0%** Exposure
- `src/ui/pages/sett/zcl_abapgit_gui_page_sett_pers.clas.abap` -> **100.0%** Exposure
- `src/objects/zcl_abapgit_objects_program.clas.testclasses.abap` -> **99.9963%** Exposure
- `src/git/zlib/zcl_abapgit_zlib_huffman.clas.testclasses.abap` -> **99.9737%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/ui/zabapgit_js_common.w3mi.data.js` -> **23** Orphaned Functions | **22** Duplicates
- `ci/deploy-release-tag.sh` -> **1** Orphaned Functions | **5** Duplicates
- `src/git/v2/zcl_abapgit_gitv2_porcelain.clas.abap` -> **4** Orphaned Functions | **0** Duplicates
- `ci/push-tag.sh` -> **1** Orphaned Functions | **2** Duplicates
- `src/diff/zcl_abapgit_diff.clas.abap` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/diff/zcl_abapgit_diff_diff3.clas.abap`** -> AI Confidence: **99.29%**
2. **`src/git/zlib/zcl_abapgit_zlib.clas.abap`** -> AI Confidence: **99.29%**
3. **`src/objects/core/zcl_abapgit_dependencies.clas.abap`** -> AI Confidence: **99.29%**
4. **`src/syntax/zcl_abapgit_syntax_factory.clas.abap`** -> AI Confidence: **99.29%**
5. **`src/syntax/zcl_abapgit_syntax_xml.clas.abap`** -> AI Confidence: **99.29%**
6. **`src/test/zcl_abapgit_objects_ci_tests.clas.abap`** -> AI Confidence: **99.29%**
7. **`src/ui/zcl_abapgit_password_dialog.clas.abap`** -> AI Confidence: **99.29%**
8. **`src/zabapgit.prog.abap`** -> AI Confidence: **99.22%**
9. **`src/cts/zcl_abapgit_transport_objects.clas.abap`** -> AI Confidence: **99.17%**
10. **`src/exits/zcl_abapgit_exit.clas.abap`** -> AI Confidence: **99.17%**
11. **`src/git/zlib/zcl_abapgit_zlib_huffman.clas.abap`** -> AI Confidence: **99.17%**
12. **`src/objects/core/zcl_abapgit_folder_logic.clas.abap`** -> AI Confidence: **99.17%**
13. **`src/objects/ecatt/zcl_abapgit_ecatt_script_downl.clas.abap`** -> AI Confidence: **99.17%**
14. **`src/objects/tabl/zcl_abapgit_object_tabl_ddl.clas.abap`** -> AI Confidence: **99.17%**
15. **`src/repo/utils/zcl_abapgit_version.clas.abap`** -> AI Confidence: **99.17%**
16. **`src/ui/routing/zcl_abapgit_gui_router.clas.abap`** -> AI Confidence: **99.17%**
17. **`src/syntax/zcl_abapgit_syntax_json.clas.abap`** -> AI Confidence: **99.11%**
18. **`ci/push-tag.sh`** -> AI Confidence: **99.06%**
19. **`src/ui/zabapgit_js_common.w3mi.data.js`** -> AI Confidence: **99.06%**
20. **`src/apack/zcl_abapgit_apack_helper.clas.abap`** -> AI Confidence: **99.06%**
21. **`src/background/zcl_abapgit_background.clas.abap`** -> AI Confidence: **99.06%**
22. **`src/background/zcl_abapgit_background_push_au.clas.abap`** -> AI Confidence: **99.06%**
23. **`src/cts/zcl_abapgit_cts_api.clas.abap`** -> AI Confidence: **99.06%**
24. **`src/cts/zcl_abapgit_default_transport.clas.abap`** -> AI Confidence: **99.06%**
25. **`src/cts/zcl_abapgit_transport.clas.abap`** -> AI Confidence: **99.06%**
26. **`src/cts/zcl_abapgit_transport_mass.clas.abap`** -> AI Confidence: **99.06%**
27. **`src/data/zcl_abapgit_data_supporter.clas.abap`** -> AI Confidence: **99.06%**
28. **`src/diff/zcl_abapgit_diff.clas.abap`** -> AI Confidence: **99.06%**
29. **`src/diff/zcl_abapgit_diff_std.clas.abap`** -> AI Confidence: **99.06%**
30. **`src/git/zcl_abapgit_git_add_patch.clas.abap`** -> AI Confidence: **99.06%**
31. **`src/git/zcl_abapgit_git_branch_list.clas.abap`** -> AI Confidence: **99.06%**
32. **`src/git/zcl_abapgit_git_branch_utils.clas.abap`** -> AI Confidence: **99.06%**
33. **`src/git/zcl_abapgit_git_delta.clas.abap`** -> AI Confidence: **99.06%**
34. **`src/git/zcl_abapgit_git_delta.clas.locals_imp.abap`** -> AI Confidence: **99.06%**
35. **`src/git/zcl_abapgit_git_pack.clas.abap`** -> AI Confidence: **99.06%**
36. **`src/git/zcl_abapgit_git_transport.clas.abap`** -> AI Confidence: **99.06%**
37. **`src/git_platform/zcl_abapgit_git_url.clas.abap`** -> AI Confidence: **99.06%**
38. **`src/http/zcl_abapgit_http.clas.abap`** -> AI Confidence: **99.06%**
39. **`src/http/zcl_abapgit_http_client.clas.abap`** -> AI Confidence: **99.06%**
40. **`src/inspect/zcl_abapgit_code_inspector.clas.abap`** -> AI Confidence: **99.06%**
41. **`src/json/zcl_abapgit_ajson.clas.locals_imp.abap`** -> AI Confidence: **99.06%**
42. **`src/json/zcl_abapgit_ajson_filter_lib.clas.locals_imp.abap`** -> AI Confidence: **99.06%**
43. **`src/json/zcl_abapgit_ajson_utilities.clas.abap`** -> AI Confidence: **99.06%**
44. **`src/json/zcl_abapgit_ajson_utilities.clas.locals_imp.abap`** -> AI Confidence: **99.06%**
45. **`src/json/zcx_abapgit_ajson_error.clas.testclasses.abap`** -> AI Confidence: **99.06%**
46. **`src/objects/aff/zcl_abapgit_json_handler.clas.locals_imp.abap`** -> AI Confidence: **99.06%**
47. **`src/objects/aff/zcl_abapgit_json_path.clas.abap`** -> AI Confidence: **99.06%**
48. **`src/objects/aff/zcl_abapgit_json_path.clas.locals_imp.abap`** -> AI Confidence: **99.06%**
49. **`src/objects/aff/zcl_abapgit_object_eeec.clas.abap`** -> AI Confidence: **99.06%**
50. **`src/objects/aff/zcl_abapgit_object_evtb.clas.abap`** -> AI Confidence: **99.06%**
51. **`src/objects/aff/zcl_abapgit_object_nont.clas.abap`** -> AI Confidence: **99.06%**
52. **`src/objects/aff/zcl_abapgit_object_ront.clas.abap`** -> AI Confidence: **99.06%**
53. **`src/objects/aff/zcl_abapgit_object_swcr.clas.abap`** -> AI Confidence: **99.06%**
54. **`src/objects/core/zabapgit_parallel.fugr.z_abapgit_serialize_package.abap`** -> AI Confidence: **99.06%**
55. **`src/objects/core/zcl_abapgit_file_deserialize.clas.abap`** -> AI Confidence: **99.06%**
56. **`src/objects/core/zcl_abapgit_file_deserialize.clas.testclasses.abap`** -> AI Confidence: **99.06%**
57. **`src/objects/core/zcl_abapgit_objects_activation.clas.abap`** -> AI Confidence: **99.06%**
58. **`src/objects/core/zcl_abapgit_objects_compare.clas.abap`** -> AI Confidence: **99.06%**
59. **`src/objects/core/zcl_abapgit_serialize.clas.abap`** -> AI Confidence: **99.06%**
60. **`src/objects/core/zcl_abapgit_tadir.clas.abap`** -> AI Confidence: **99.06%**
61. **`src/objects/ecatt/zcl_abapgit_ecatt_data_upload.clas.abap`** -> AI Confidence: **99.06%**
62. **`src/objects/ecatt/zcl_abapgit_ecatt_sp_upload.clas.abap`** -> AI Confidence: **99.06%**
63. **`src/objects/ecatt/zcl_abapgit_ecatt_val_obj_upl.clas.abap`** -> AI Confidence: **99.06%**
64. **`src/objects/enh/zcl_abapgit_object_enho_badi.clas.abap`** -> AI Confidence: **99.06%**
65. **`src/objects/enh/zcl_abapgit_object_enho_class.clas.abap`** -> AI Confidence: **99.06%**
66. **`src/objects/enh/zcl_abapgit_object_enho_clif.clas.abap`** -> AI Confidence: **99.06%**
67. **`src/objects/enh/zcl_abapgit_object_enho_fugr.clas.abap`** -> AI Confidence: **99.06%**
68. **`src/objects/enh/zcl_abapgit_object_enho_wdyn.clas.abap`** -> AI Confidence: **99.06%**
69. **`src/objects/jump/zcl_abapgit_gui_jumper.clas.abap`** -> AI Confidence: **99.06%**
70. **`src/objects/oo/zcl_abapgit_oo_class.clas.abap`** -> AI Confidence: **99.06%**
71. **`src/objects/oo/zcl_abapgit_oo_factory.clas.abap`** -> AI Confidence: **99.06%**
72. **`src/objects/rules/zcl_abapgit_field_rules.clas.abap`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/ui/zabapgit_js_common.w3mi.data.js` -> **100.0%** Exposure
- `src/cts/zcl_abapgit_cts_api.clas.abap` -> **100.0%** Exposure
- `src/cts/zcl_abapgit_transport.clas.abap` -> **100.0%** Exposure
- `src/diff/zcl_abapgit_diff.clas.abap` -> **100.0%** Exposure
- `src/git/v2/zcl_abapgit_gitv2_porcelain.clas.abap` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `src/objects/oo/zcl_abapgit_oo_base.clas.abap` -> **100.0%** Exposure
- `src/objects/zcl_abapgit_object_avas.clas.abap` -> **100.0%** Exposure
- `src/objects/zcl_abapgit_object_shi5.clas.abap` -> **100.0%** Exposure
- `src/objects/zcl_abapgit_object_splo.clas.abap` -> **100.0%** Exposure
- `src/objects/zcl_abapgit_object_suso.clas.abap` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `src/objects/aff/zcl_abapgit_json_path.clas.locals_imp.abap` -> **100.0%** Exposure
- `src/objects/aff/zcl_abapgit_json_path.clas.testclasses.abap` -> **100.0%** Exposure
- `src/objects/enh/zcl_abapgit_object_enho_hook.clas.abap` -> **100.0%** Exposure
- `src/objects/zcl_abapgit_object_shi8.clas.abap` -> **100.0%** Exposure
- `src/objects/zcl_abapgit_object_susc.clas.abap` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `24` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/ui/zabapgit_js_common.w3mi.data.js` (JAVASCRIPT) -> Cumulative Risk: **820.72**
- **Archetype:** `file_cluster_17` (Distance: 15.137 IQR)
- **Magnitude:** 3087.28 | **LOC:** 2590 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Tech Debt (98.0881%)
- **Heaviest Functions:** `enumerateUiActions` (Impact: 84.5), `deployHintContainers` (Impact: 49.9), `mousedownEventListener` (Impact: 48.1)

### 2. `src/ui/core/zcl_abapgit_gui_css_processor.clas.abap` (ABAP) -> Cumulative Risk: **619.19**
- **Archetype:** `file_cluster_8` (Distance: 9.512 IQR)
- **Magnitude:** 96.5 | **LOC:** 165 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `resolve_var_recursively` (Impact: 40.4), `process` (Impact: 36.5)

### 3. `ci/push-tag.sh` (SHELL) -> Cumulative Risk: **580.56**
- **Archetype:** `file_cluster_17` (Distance: 15.621 IQR)
- **Magnitude:** 1.6 | **LOC:** 29 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (98.9714%), Documentation (95.753%)
- **Heaviest Functions:** `__global_context__` (Impact: 5.2), `Anonymous_Block` (Impact: 4.2), `Anonymous_Block` (Impact: 3.2)

### 4. `src/diff/zcl_abapgit_diff.clas.abap` (ABAP) -> Cumulative Risk: **576.54**
- **Archetype:** `file_cluster_8` (Distance: 8.958 IQR)
- **Magnitude:** 45.38 | **LOC:** 284 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9812%)
- **Heaviest Functions:** `is_line_patched` (Impact: 9.5), `set_patch_new` (Impact: 6.5), `set_patch_old` (Impact: 6.5)

### 5. `src/git/v2/zcl_abapgit_gitv2_porcelain.clas.abap` (ABAP) -> Cumulative Risk: **559.77**
- **Archetype:** `file_cluster_8` (Distance: 9.683 IQR)
- **Magnitude:** 60.16 | **LOC:** 322 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9997%), State Flux (98.5454%)
- **Heaviest Functions:** `send_command` (Impact: 4.8), `fetch_blobs` (Impact: 2.6), `list_no_blobs_multi` (Impact: 2.6)

### 6. `ci/deploy-release-tag.sh` (SHELL) -> Cumulative Risk: **559.75**
- **Archetype:** `file_cluster_8` (Distance: 12.441 IQR)
- **Magnitude:** 4.53 | **LOC:** 54 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9795%)
- **Heaviest Functions:** `__global_context__` (Impact: 4.5), `Anonymous_Block` (Impact: 4.2), `Anonymous_Block` (Impact: 4.2)

### 7. `src/ui/pages/zcl_abapgit_gui_page_repo_view.clas.abap` (ABAP) -> Cumulative Risk: **553.82**
- **Archetype:** `file_cluster_8` (Distance: 9.55 IQR)
- **Magnitude:** 179.9 | **LOC:** 1423 | **CtrlFlow:** 58.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Logic Bomb (100.0%), Spec Match (97.0588%), Algorithmic Dos (88.9656%), Verification (80.0%)
- **Heaviest Functions:** `build_dir_jump_link` (Impact: 15.3), `render_item_command` (Impact: 15.1), `build_branch_dropdown` (Impact: 11.0)

### 8. `src/objects/aff/zcl_abapgit_json_path.clas.locals_imp.abap` (ABAP) -> Cumulative Risk: **549.4**
- **Archetype:** `file_cluster_8` (Distance: 9.384 IQR)
- **Magnitude:** 408.76 | **LOC:** 405 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9992%), Verification (80.0%)
- **Heaviest Functions:** `build_json` (Impact: 381.0)

### 9. `src/objects/core/zcl_abapgit_serialize.clas.abap` (ABAP) -> Cumulative Risk: **537.68**
- **Archetype:** `file_cluster_8` (Distance: 9.418 IQR)
- **Magnitude:** 108.82 | **LOC:** 779 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Logic Bomb (100.0%), Algorithmic Dos (99.9932%), Spec Match (94.1176%), Verification (80.0%)
- **Heaviest Functions:** `filter_unsupported_objects` (Impact: 40.4), `serialize` (Impact: 16.8), `on_end_of_task` (Impact: 11.8)

### 10. `src/git/zcl_abapgit_git_porcelain.clas.abap` (ABAP) -> Cumulative Risk: **525.36**
- **Archetype:** `file_cluster_8` (Distance: 9.415 IQR)
- **Magnitude:** 107.7 | **LOC:** 837 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (94.971%), Verification (80.0%)
- **Heaviest Functions:** `walk_tree` (Impact: 31.9), `create_tag` (Impact: 10.1), `create_annotated_tag` (Impact: 3.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/diff/diff3/zcl_abapgit_diff3.clas.testclasses.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.713 IQR)
- **Top Global Matches:** file_cluster_8: 8.713, file_cluster_7: 9.618, file_cluster_1: 9.821
- **Magnitude:** 5650.94 | **LOC:** 3382 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.5625%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 472`, `args: 4`, `func_start: 28`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `test: 262`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/git/zlib/zcl_abapgit_zlib.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.524 IQR)
- **Top Global Matches:** file_cluster_8: 9.524, file_cluster_7: 10.341, file_cluster_1: 10.591
- **Magnitude:** 4194.06 | **LOC:** 472 | **CtrlFlow:** 78.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (27.215%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 26`, `args: 16`, `func_start: 10`
* *Risk/State:* `state_mutation: 43`
* *Architecture:* `api: 1`
* *Defense:* `safety: 6`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/flow/zcl_abapgit_flow_logic.clas.testclasses.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.063 IQR)
- **Top Global Matches:** file_cluster_8: 9.063, file_cluster_6: 9.857, file_cluster_7: 9.92
- **Magnitude:** 4143.98 | **LOC:** 746 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 77.8%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.3319%), Tech Debt (63.8472%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 170`, `args: 16`, `func_start: 123`
* *Risk/State:* `state_mutation: 24`, `planned_debt: 35`
* *Architecture:* `io: 14`, `api: 9`
* *Defense:* `safety: 5`, `test: 13`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_object_aifc.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.248 IQR)
- **Top Global Matches:** file_cluster_8: 9.248, file_cluster_16: 10.135, file_cluster_7: 10.136
- **Magnitude:** 3285.3 | **LOC:** 618 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.7203%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 77`, `args: 36`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 11`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* `safety: 21`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/zabapgit_js_common.w3mi.data.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.137 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.062 IQR)
- **Top Global Matches:** file_cluster_17: 15.137, file_cluster_11: 15.212, file_cluster_15: 15.556
- **Magnitude:** 3087.28 | **LOC:** 2590 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (87.7843%), Tech Debt (98.0881%)
**Top Internal Functions/Classes:**
  * `enumerateUiActions` (Impact: 84.5 | O(N^3) | DB: 13)
  * `deployHintContainers` (Impact: 49.9 | O(N^2) | DB: 6)
  * `mousedownEventListener` (Impact: 48.1 | O(N^2) | DB: 20)
  * `submitSapeventForm` (Impact: 38.3 | O(N^1) | DB: 5)
  * `CommandPalette` (Impact: 36.5 | O(2^N) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 527`, `structural_boundaries: 383`, `args: 238`, `func_start: 199`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `state_mutation: 1661`, `dead_code: 9`, `planned_debt: 3`, `duplicate_logic: 22`, `orphaned_logic: 23`
* *Architecture:* `io: 15`, `concurrency: 18`
* *Defense:* `safety: 187`, `doc: 21`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/zcl_abapgit_convert.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.831 IQR)
- **Top Global Matches:** file_cluster_8: 8.831, file_cluster_7: 9.761, file_cluster_1: 9.99
- **Magnitude:** 2646.85 | **LOC:** 522 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.1792%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 65`, `args: 51`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 1`
* *Defense:* `safety: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_object_intf.clas.locals_imp.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.738 IQR)
- **Top Global Matches:** file_cluster_8: 9.738, file_cluster_7: 10.507, file_cluster_2: 10.589
- **Magnitude:** 2579.99 | **LOC:** 746 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.9419%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 65`, `args: 44`, `func_start: 21`
* *Risk/State:* `state_mutation: 57`
* *Architecture:* `io: 20`, `api: 3`
* *Defense:* `safety: 11`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_object_smim.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.955 IQR)
- **Top Global Matches:** file_cluster_8: 7.955, file_cluster_7: 8.917, file_cluster_1: 9.184
- **Magnitude:** 2373.38 | **LOC:** 525 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.76%), Tech Debt (11.6927%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 41`, `args: 40`, `func_start: 22`
* *Risk/State:* `state_mutation: 5`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 8`, `api: 1`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_object_wdcc.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.528 IQR)
- **Top Global Matches:** file_cluster_8: 8.528, file_cluster_7: 9.453, file_cluster_1: 9.718
- **Magnitude:** 2350.75 | **LOC:** 495 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.6958%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 27`, `args: 39`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 4`
* *Architecture:* `io: 7`, `api: 1`, `concurrency: 3`
* *Defense:* `safety: 14`, `sync_locks: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_object_nrob.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.426 IQR)
- **Top Global Matches:** file_cluster_8: 8.426, file_cluster_7: 9.305, file_cluster_1: 9.568
- **Magnitude:** 2319.64 | **LOC:** 412 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.4042%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 28`, `args: 24`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`
* *Architecture:* `io: 1`, `api: 1`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_object_wdca.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.148 IQR)
- **Top Global Matches:** file_cluster_8: 9.148, file_cluster_7: 10.036, file_cluster_1: 10.281
- **Magnitude:** 2027.84 | **LOC:** 448 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.1578%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 28`, `args: 24`, `func_start: 18`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `io: 6`, `api: 1`
* *Defense:* `safety: 16`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/json/zcl_abapgit_ajson_utilities.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.632 IQR)
- **Top Global Matches:** file_cluster_8: 7.632, file_cluster_7: 8.697, file_cluster_1: 8.907
- **Magnitude:** 1980.3 | **LOC:** 418 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.5557%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 29`, `args: 17`, `func_start: 11`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/ecatt/zcl_abapgit_ecatt_script_downl.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.939 IQR)
- **Top Global Matches:** file_cluster_8: 7.939, file_cluster_7: 8.995, file_cluster_1: 9.196
- **Magnitude:** 1956.07 | **LOC:** 455 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.9625%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 16`, `args: 17`, `func_start: 8`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `safety: 8`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcx_abapgit_exception.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.891 IQR)
- **Top Global Matches:** file_cluster_8: 8.891, file_cluster_7: 9.504, file_cluster_1: 9.761
- **Magnitude:** 1755.58 | **LOC:** 442 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.3164%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 35`, `args: 20`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 11`, `doc: 18`, `immutability_locks: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TYPE
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/pages/zcl_abapgit_gui_page_merge_res.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.7 IQR)
- **Top Global Matches:** file_cluster_8: 9.7, file_cluster_7: 10.484, file_cluster_9: 10.62
- **Magnitude:** 1697.16 | **LOC:** 578 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.1068%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 39`, `args: 12`, `func_start: 15`
* *Risk/State:* `dead_code: 6`
* *Architecture:* `api: 1`
* *Defense:* `safety: 5`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/diff/zcl_abapgit_diff_std.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.678 IQR)
- **Top Global Matches:** file_cluster_8: 9.678, file_cluster_0: 10.425, file_cluster_7: 10.445
- **Magnitude:** 1688.01 | **LOC:** 304 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.8034%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 24`, `args: 11`, `func_start: 6`
* *Risk/State:* `state_mutation: 7`, `dead_code: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 7`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/texts/zcl_abapgit_sotr_handler.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.286 IQR)
- **Top Global Matches:** file_cluster_8: 8.286, file_cluster_7: 9.243, file_cluster_1: 9.501
- **Magnitude:** 1660.35 | **LOC:** 448 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.3106%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 33`, `args: 32`, `func_start: 8`
* *Risk/State:* `state_mutation: 3`, `dead_code: 1`
* *Architecture:* `io: 6`, `api: 1`
* *Defense:* `safety: 10`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/ecatt/zcl_abapgit_ecatt_val_obj_upl.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.291 IQR)
- **Top Global Matches:** file_cluster_8: 9.291, file_cluster_7: 10.204, file_cluster_16: 10.409
- **Magnitude:** 1645.0 | **LOC:** 357 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.1729%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 15`, `args: 23`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `api: 1`
* *Defense:* `safety: 22`, `immutability_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/pages/sett/zcl_abapgit_gui_page_sett_locl.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.922 IQR)
- **Top Global Matches:** file_cluster_8: 7.922, file_cluster_7: 8.993, file_cluster_1: 9.21
- **Magnitude:** 1466.21 | **LOC:** 595 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.8221%), Tech Debt (10.8358%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 32`, `args: 9`, `func_start: 14`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 16`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zabapgit_forms.prog.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.087 IQR)
- **Top Global Matches:** file_cluster_8: 9.087, file_cluster_7: 9.957, file_cluster_2: 10.158
- **Magnitude:** 1458.48 | **LOC:** 375 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.2186%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 26`, `args: 8`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 8`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* `safety: 14`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/texts/zcl_abapgit_i18n_params.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.567 IQR)
- **Top Global Matches:** file_cluster_8: 8.567, file_cluster_7: 9.483, file_cluster_1: 9.762
- **Magnitude:** 1419.64 | **LOC:** 278 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.1201%), Tech Debt (17.0262%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 28`, `args: 21`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `planned_debt: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 8`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_object_sfbf.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.088 IQR)
- **Top Global Matches:** file_cluster_8: 8.088, file_cluster_7: 9.042, file_cluster_1: 9.293
- **Magnitude:** 1383.19 | **LOC:** 375 | **CtrlFlow:** 45.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.8351%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 26`, `args: 28`, `func_start: 19`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `io: 2`, `api: 1`, `concurrency: 1`
* *Defense:* `safety: 3`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_object_idoc.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.208 IQR)
- **Top Global Matches:** file_cluster_8: 8.208, file_cluster_7: 9.14, file_cluster_1: 9.382
- **Magnitude:** 1356.28 | **LOC:** 371 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.5799%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 29`, `args: 44`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/texts/zcl_abapgit_sots_handler.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.161 IQR)
- **Top Global Matches:** file_cluster_8: 8.161, file_cluster_7: 9.147, file_cluster_1: 9.389
- **Magnitude:** 1296.16 | **LOC:** 328 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.0373%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 25`, `args: 23`, `func_start: 6`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* `safety: 6`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/objects/core/zabapgit_parallel.fugr.saplzabapgit_parallel.abap` (ABAP) | Magnitude: 11.04 | Delta: **0.145 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: import: 2, planned_debt: 1, sec_high_risk_execution: 1
- `src/zabapgit.prog.abap` (ABAP) | Magnitude: 15.54 | Delta: **0.215 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 12, import: 6, ui_framework: 5, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/ui/zabapgit_js_common.w3mi.data.js` (JAVASCRIPT) | Magnitude: 3087.28 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 1661, indent_spaces: 1526, branch: 527, structural_boundaries: 383
- `ci/push-tag.sh` (SHELL) | Magnitude: 1.6 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 7, structural_boundaries: 7, safety_bypasses: 6, io: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/zabapgit_password_dialog.prog.abap` (ABAP) | Magnitude: 467.42 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 103, ui_framework: 22, structural_boundaries: 15, branch: 14
- `src/objects/zcl_abapgit_object_iobj.clas.abap` (ABAP) | Magnitude: 22.62 | Delta: **0.151 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 394, pointers: 179, generics: 65, args: 51
- `test/src/zcl_abapgit_object_zag1.clas.testclasses.abap` (ABAP) | Magnitude: 57.48 | Delta: **0.189 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 70, concurrency: 19, structural_boundaries: 16, pointers: 6
- `src/objects/zcl_abapgit_object_otgr.clas.abap` (ABAP) | Magnitude: 35.06 | Delta: **0.253 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 251, pointers: 62, branch: 36, structural_boundaries: 22
- `test/express.mjs` (JAVASCRIPT) | Magnitude: 18.38 | Delta: **0.26 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, import: 4, concurrency: 3, args: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/ui/flow/zcl_abapgit_flow_logic.clas.testclasses.abap` -> Churn: **69.19%** | Cog Load: 11.3319% | Debt: 63.8472%
- `src/ui/zabapgit_js_common.w3mi.data.js` -> Churn: **64.96%** | Cog Load: 87.7843% | Debt: 98.0881%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/diff/diff3/zcl_abapgit_diff3.clas.testclasses.abap` -> **Lars Hvam** (100.0% isolated ownership) | Magnitude: 5650.94
- `src/objects/zcl_abapgit_object_aifc.clas.abap` -> **Marc Bernard** (100.0% isolated ownership) | Magnitude: 3285.3
- `src/objects/zcl_abapgit_object_smim.clas.abap` -> **Marc Bernard** (100.0% isolated ownership) | Magnitude: 2373.38
- `src/objects/zcl_abapgit_object_wdcc.clas.abap` -> **Marc Bernard** (100.0% isolated ownership) | Magnitude: 2350.75
- `src/objects/zcl_abapgit_object_nrob.clas.abap` -> **Marc Bernard** (100.0% isolated ownership) | Magnitude: 2319.64

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/apack/zcl_abapgit_apack_writer.clas.abap` -> **Severity: 72.5** (Blast Radius: 0.725 * Doc Risk: 100.0%)
- `src/background/zcl_abapgit_background.clas.abap` -> **Severity: 72.5** (Blast Radius: 0.725 * Doc Risk: 100.0%)
- `src/data/zcl_abapgit_data_injector.clas.abap` -> **Severity: 72.5** (Blast Radius: 0.725 * Doc Risk: 100.0%)
- `src/diff/zcl_abapgit_diff.clas.abap` -> **Severity: 72.5** (Blast Radius: 0.725 * Doc Risk: 100.0%)
- `src/git/zcl_abapgit_git_delta.clas.locals_def.abap` -> **Severity: 72.5** (Blast Radius: 0.725 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
