# ARCHITECTURAL_BRIEF: abapGit
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/abapGit` |
| **Timestamp** | `2026-08-07T03:46:32.336205+00:00` |
| **Scan Duration** | `2.96s` |
| **Git Branch** | `main` |
| **Git Commit** | `951e2243efbf0dbbfb4978a4ffa182b77e2ee939` |
| **Git Remote** | `https://github.com/abapGit/abapGit` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 728 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
| Cognitive Load Exposure | 0.0 | 98.3 | 7.2 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 16.8 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 1.4 | 1.7 | 0.2 |
| API Exposure | 0.0 | 17.6 | 0.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 9.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 68.3 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 55.3 | 93.3 | 100.0 |
| Instability Exposure | 0.0 | 5.4 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 82.2 | 4.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 20.4 | 14.4 | 5.2 |
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

- `parse_boolean` (@ `src/json/zcl_abapgit_ajson.clas.testclasses.abap`) -> Impact: **92.9** | LOC: 1491
- `parse_number` (@ `src/json/zcl_abapgit_ajson.clas.testclasses.abap`) -> Impact: **92.5** | LOC: 1482
- `parse_null` (@ `src/json/zcl_abapgit_ajson.clas.testclasses.abap`) -> Impact: **92.5** | LOC: 1482
- `build_json` (@ `src/objects/aff/zcl_abapgit_json_path.clas.locals_imp.abap`) -> Impact: **67.1** | LOC: 295
- `enumerateUiActions` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> Impact: **44.7** | LOC: 97
- `submitSapeventForm` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> Impact: **38.3** | LOC: 51
- `deployHintContainers` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> Impact: **34.3** | LOC: 64
- `mousedownEventListener` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> Impact: **33.2** | LOC: 71
- `hintActivate` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> Impact: **25.2** | LOC: 23
- `handleKey` (@ `src/ui/zabapgit_js_common.w3mi.data.js`) -> Impact: **24.9** | LOC: 45
  * *Intent:* // does not work if inside the input node

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/objects` | 321 | 42899.64 | 6.94% | 4.58% |
| `src/ui/flow` | 21 | 6794.3 | 7.82% | 4.84% |
| `src/objects/ecatt` | 33 | 5927.12 | 6.65% | 0.0% |
| `src/diff/diff3` | 6 | 5831.94 | 6.65% | 0.0% |
| `src/objects/texts` | 29 | 5606.63 | 7.68% | 2.06% |
| `src/utils` | 24 | 5454.74 | 6.46% | 2.32% |
| `src/git/zlib` | 10 | 5266.9 | 12.63% | 0.0% |
| `__monolith__` | 8 | 5049.94 | 0.78% | 0.0% |
| `src` | 24 | 4888.84 | 6.33% | 0.0% |
| `src/repo` | 37 | 4615.53 | 6.64% | 2.83% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `ci/deploy-release-tag.sh` -> **100.0%** Exposure
- `ci/push-tag.sh` -> **100.0%** Exposure
- `src/objects/core/zabapgit_parallel.fugr.saplzabapgit_parallel.abap` -> **100.0%** Exposure
- `src/xml/zif_abapgit_xml_input.intf.abap` -> **99.9955%** Exposure
- `src/ui/zabapgit_js_common.w3mi.data.js` -> **99.9519%** Exposure
### Highest State Flux (Mutation/Volatility)
- `ci/deploy-release-tag.sh` -> **100.0%** Exposure
- `src/ui/zabapgit_js_common.w3mi.data.js` -> **100.0%** Exposure
- `src/ui/pages/sett/zcl_abapgit_gui_page_sett_pers.clas.abap` -> **100.0%** Exposure
- `src/objects/zcl_abapgit_objects_program.clas.testclasses.abap` -> **99.9963%** Exposure
- `src/git/zlib/zcl_abapgit_zlib_huffman.clas.testclasses.abap` -> **99.9737%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/ui/zabapgit_js_common.w3mi.data.js` -> **24** Orphaned Functions | **40** Duplicates
- `ci/deploy-release-tag.sh` -> **1** Orphaned Functions | **5** Duplicates
- `src/git/v2/zcl_abapgit_gitv2_porcelain.clas.abap` -> **4** Orphaned Functions | **0** Duplicates
- `ci/push-tag.sh` -> **1** Orphaned Functions | **2** Duplicates
- `src/diff/zcl_abapgit_diff.clas.abap` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/diff/zcl_abapgit_diff_diff3.clas.abap`** -> AI Confidence: **99.29%**
2. **`src/git/zlib/zcl_abapgit_zlib.clas.abap`** -> AI Confidence: **99.29%**
3. **`src/objects/core/zcl_abapgit_dependencies.clas.abap`** -> AI Confidence: **99.29%**
4. **`src/repo/utils/zcl_abapgit_version.clas.abap`** -> AI Confidence: **99.29%**
5. **`src/syntax/zcl_abapgit_syntax_factory.clas.abap`** -> AI Confidence: **99.29%**
6. **`src/syntax/zcl_abapgit_syntax_xml.clas.abap`** -> AI Confidence: **99.29%**
7. **`src/test/zcl_abapgit_objects_ci_tests.clas.abap`** -> AI Confidence: **99.29%**
8. **`src/ui/zcl_abapgit_password_dialog.clas.abap`** -> AI Confidence: **99.29%**
9. **`src/zabapgit.prog.abap`** -> AI Confidence: **99.22%**
10. **`ci/push-tag.sh`** -> AI Confidence: **99.17%**
11. **`src/cts/zcl_abapgit_transport_objects.clas.abap`** -> AI Confidence: **99.17%**
12. **`src/diff/zcl_abapgit_diff_std.clas.abap`** -> AI Confidence: **99.17%**
13. **`src/exits/zcl_abapgit_exit.clas.abap`** -> AI Confidence: **99.17%**
14. **`src/git/zlib/zcl_abapgit_zlib_huffman.clas.abap`** -> AI Confidence: **99.17%**
15. **`src/objects/core/zcl_abapgit_folder_logic.clas.abap`** -> AI Confidence: **99.17%**
16. **`src/objects/ecatt/zcl_abapgit_ecatt_script_downl.clas.abap`** -> AI Confidence: **99.17%**
17. **`src/objects/enh/zcl_abapgit_object_enho_clif.clas.abap`** -> AI Confidence: **99.17%**
18. **`src/objects/tabl/zcl_abapgit_object_tabl_ddl.clas.abap`** -> AI Confidence: **99.17%**
19. **`src/ui/flow/zcl_abapgit_flow_exit.clas.abap`** -> AI Confidence: **99.17%**
20. **`src/ui/lib/zcl_abapgit_html_form_utils.clas.abap`** -> AI Confidence: **99.17%**
21. **`src/ui/lib/zcl_abapgit_log_viewer.clas.abap`** -> AI Confidence: **99.17%**
22. **`src/ui/routing/zcl_abapgit_gui_router.clas.abap`** -> AI Confidence: **99.17%**
23. **`src/xml/zcl_abapgit_xml_pretty.clas.abap`** -> AI Confidence: **99.17%**
24. **`src/syntax/zcl_abapgit_syntax_json.clas.abap`** -> AI Confidence: **99.11%**
25. **`ci/deploy-release-tag.sh`** -> AI Confidence: **99.06%**
26. **`src/ui/zabapgit_js_common.w3mi.data.js`** -> AI Confidence: **99.06%**
27. **`src/apack/zcl_abapgit_apack_helper.clas.abap`** -> AI Confidence: **99.06%**
28. **`src/background/zcl_abapgit_background.clas.abap`** -> AI Confidence: **99.06%**
29. **`src/background/zcl_abapgit_background_push_au.clas.abap`** -> AI Confidence: **99.06%**
30. **`src/cts/zcl_abapgit_cts_api.clas.abap`** -> AI Confidence: **99.06%**
31. **`src/cts/zcl_abapgit_default_transport.clas.abap`** -> AI Confidence: **99.06%**
32. **`src/cts/zcl_abapgit_transport.clas.abap`** -> AI Confidence: **99.06%**
33. **`src/cts/zcl_abapgit_transport_mass.clas.abap`** -> AI Confidence: **99.06%**
34. **`src/data/zcl_abapgit_data_supporter.clas.abap`** -> AI Confidence: **99.06%**
35. **`src/diff/zcl_abapgit_diff.clas.abap`** -> AI Confidence: **99.06%**
36. **`src/git/zcl_abapgit_git_add_patch.clas.abap`** -> AI Confidence: **99.06%**
37. **`src/git/zcl_abapgit_git_branch_list.clas.abap`** -> AI Confidence: **99.06%**
38. **`src/git/zcl_abapgit_git_branch_utils.clas.abap`** -> AI Confidence: **99.06%**
39. **`src/git/zcl_abapgit_git_delta.clas.abap`** -> AI Confidence: **99.06%**
40. **`src/git/zcl_abapgit_git_delta.clas.locals_imp.abap`** -> AI Confidence: **99.06%**
41. **`src/git/zcl_abapgit_git_factory.clas.abap`** -> AI Confidence: **99.06%**
42. **`src/git/zcl_abapgit_git_pack.clas.abap`** -> AI Confidence: **99.06%**
43. **`src/git/zcl_abapgit_git_porcelain.clas.abap`** -> AI Confidence: **99.06%**
44. **`src/git/zcl_abapgit_git_transport.clas.abap`** -> AI Confidence: **99.06%**
45. **`src/git_platform/zcl_abapgit_git_url.clas.abap`** -> AI Confidence: **99.06%**
46. **`src/git_platform/zcl_abapgit_pr_enumerator.clas.abap`** -> AI Confidence: **99.06%**
47. **`src/http/zcl_abapgit_http.clas.abap`** -> AI Confidence: **99.06%**
48. **`src/http/zcl_abapgit_http_agent.clas.abap`** -> AI Confidence: **99.06%**
49. **`src/http/zcl_abapgit_http_client.clas.abap`** -> AI Confidence: **99.06%**
50. **`src/http/zcl_abapgit_proxy_auth.clas.abap`** -> AI Confidence: **99.06%**
51. **`src/http/zcl_abapgit_url.clas.abap`** -> AI Confidence: **99.06%**
52. **`src/inspect/zcl_abapgit_code_inspector.clas.abap`** -> AI Confidence: **99.06%**
53. **`src/json/zcl_abapgit_ajson.clas.locals_imp.abap`** -> AI Confidence: **99.06%**
54. **`src/json/zcl_abapgit_ajson_filter_lib.clas.locals_imp.abap`** -> AI Confidence: **99.06%**
55. **`src/json/zcl_abapgit_ajson_utilities.clas.abap`** -> AI Confidence: **99.06%**
56. **`src/json/zcl_abapgit_ajson_utilities.clas.locals_imp.abap`** -> AI Confidence: **99.06%**
57. **`src/json/zcx_abapgit_ajson_error.clas.testclasses.abap`** -> AI Confidence: **99.06%**
58. **`src/objects/aff/zcl_abapgit_aff_factory.clas.abap`** -> AI Confidence: **99.06%**
59. **`src/objects/aff/zcl_abapgit_json_handler.clas.locals_imp.abap`** -> AI Confidence: **99.06%**
60. **`src/objects/aff/zcl_abapgit_json_path.clas.abap`** -> AI Confidence: **99.06%**
61. **`src/objects/aff/zcl_abapgit_json_path.clas.locals_imp.abap`** -> AI Confidence: **99.06%**
62. **`src/objects/aff/zcl_abapgit_object_common_aff.clas.abap`** -> AI Confidence: **99.06%**
63. **`src/objects/aff/zcl_abapgit_object_eeec.clas.abap`** -> AI Confidence: **99.06%**
64. **`src/objects/aff/zcl_abapgit_object_evtb.clas.abap`** -> AI Confidence: **99.06%**
65. **`src/objects/aff/zcl_abapgit_object_nont.clas.abap`** -> AI Confidence: **99.06%**
66. **`src/objects/aff/zcl_abapgit_object_ront.clas.abap`** -> AI Confidence: **99.06%**
67. **`src/objects/aff/zcl_abapgit_object_swcr.clas.abap`** -> AI Confidence: **99.06%**
68. **`src/objects/core/zabapgit_parallel.fugr.z_abapgit_serialize_package.abap`** -> AI Confidence: **99.06%**
69. **`src/objects/core/zcl_abapgit_file_deserialize.clas.abap`** -> AI Confidence: **99.06%**
70. **`src/objects/core/zcl_abapgit_file_deserialize.clas.testclasses.abap`** -> AI Confidence: **99.06%**
71. **`src/objects/core/zcl_abapgit_objects_activation.clas.abap`** -> AI Confidence: **99.06%**
72. **`src/objects/core/zcl_abapgit_objects_check.clas.abap`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `24` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/ui/zabapgit_js_common.w3mi.data.js` (JAVASCRIPT) -> Cumulative Risk: **673.09**
- **Archetype:** `file_cluster_17` (Distance: 15.123 IQR)
- **Magnitude:** 2970.28 | **LOC:** 2590 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9519%), Safety Score (95.5746%)
- **Heaviest Functions:** `enumerateUiActions` (Impact: 44.7), `submitSapeventForm` (Impact: 38.3), `deployHintContainers` (Impact: 34.3)

### 2. `ci/push-tag.sh` (SHELL) -> Cumulative Risk: **563.81**
- **Archetype:** `file_cluster_17` (Distance: 15.68 IQR)
- **Magnitude:** 2.2 | **LOC:** 29 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (98.9714%), Safety Score (97.5182%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 8.2), `Anonymous_Block` (Impact: 5.2), `__global_context__` (Impact: 5.2)

### 3. `ci/deploy-release-tag.sh` (SHELL) -> Cumulative Risk: **541.04**
- **Archetype:** `file_cluster_8` (Distance: 12.539 IQR)
- **Magnitude:** 5.93 | **LOC:** 54 | **CtrlFlow:** 62.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9819%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 8.2), `Anonymous_Block` (Impact: 8.2), `Anonymous_Block` (Impact: 5.2)

### 4. `src/ui/pages/zcl_abapgit_gui_page_repo_over.clas.locals_imp.abap` (ABAP) -> Cumulative Risk: **392.06**
- **Archetype:** `file_cluster_8` (Distance: 8.66 IQR)
- **Magnitude:** 32.32 | **LOC:** 37 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (98.9013%), Safety Score (77.5564%), Documentation (72.6932%)

### 5. `src/git/v2/zcl_abapgit_gitv2_porcelain.clas.abap` (ABAP) -> Cumulative Risk: **388.57**
- **Archetype:** `file_cluster_8` (Distance: 9.7 IQR)
- **Magnitude:** 57.56 | **LOC:** 322 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.5454%), Safety Score (64.7867%), Tech Debt (45.0817%)
- **Heaviest Functions:** `fetch_blobs` (Impact: 2.6), `list_no_blobs_multi` (Impact: 2.6), `list_branches` (Impact: 2.4)

### 6. `src/objects/zcl_abapgit_object_w3ht.clas.abap` (ABAP) -> Cumulative Risk: **384.11**
- **Archetype:** `file_cluster_8` (Distance: 7.82 IQR)
- **Magnitude:** 17.3 | **LOC:** 28 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (96.207%), Safety Score (82.388%), Documentation (67.787%)

### 7. `src/objects/zcl_abapgit_object_w3mi.clas.abap` (ABAP) -> Cumulative Risk: **384.11**
- **Archetype:** `file_cluster_8` (Distance: 7.82 IQR)
- **Magnitude:** 17.3 | **LOC:** 28 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (96.207%), Safety Score (82.388%), Documentation (67.787%)

### 8. `src/git/zlib/zcl_abapgit_zlib_huffman.clas.testclasses.abap` (ABAP) -> Cumulative Risk: **376.51**
- **Archetype:** `file_cluster_8` (Distance: 10.016 IQR)
- **Magnitude:** 149.08 | **LOC:** 85 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9737%), Safety Score (72.7261%), Documentation (47.5135%)

### 9. `src/objects/aff/zcl_abapgit_json_path.clas.locals_imp.abap` (ABAP) -> Cumulative Risk: **370.21**
- **Archetype:** `file_cluster_8` (Distance: 9.415 IQR)
- **Magnitude:** 104.56 | **LOC:** 405 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (69.3528%), Safety Score (57.1821%)
- **Heaviest Functions:** `build_json` (Impact: 67.1), `serialize_rec_array` (Impact: 4.9), `serialize_rec` (Impact: 4.8)

### 10. `src/ui/flow/zcl_abapgit_flow_logic.clas.testclasses.abap` (ABAP) -> Cumulative Risk: **366.5**
- **Archetype:** `file_cluster_8` (Distance: 9.063 IQR)
- **Magnitude:** 4143.98 | **LOC:** 746 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 77.8%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (69.19%), Tech Debt (63.8472%), Safety Score (52.7784%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/diff/diff3/zcl_abapgit_diff3.clas.testclasses.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.714 IQR)
- **Top Global Matches:** file_cluster_8: 8.714, file_cluster_7: 9.62, file_cluster_1: 9.823
- **Magnitude:** 5650.94 | **LOC:** 3382 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (6.5625%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 470`, `args: 4`, `func_start: 28`
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
- **Global Archetype:** `file_cluster_8` (Drift: 9.533 IQR)
- **Top Global Matches:** file_cluster_8: 9.533, file_cluster_7: 10.349, file_cluster_1: 10.6
- **Magnitude:** 4194.06 | **LOC:** 472 | **CtrlFlow:** 80.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.215%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 23`, `args: 16`, `func_start: 10`
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
- **Global Archetype:** `file_cluster_17` (Drift: 15.123 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.203 IQR)
- **Top Global Matches:** file_cluster_17: 15.123, file_cluster_11: 15.199, file_cluster_15: 15.546
- **Magnitude:** 2970.28 | **LOC:** 2590 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (87.495%), Tech Debt (99.9519%)
**Top Internal Functions/Classes:**
  * `enumerateUiActions` (Impact: 44.7)
  * `submitSapeventForm` (Impact: 38.3)
  * `deployHintContainers` (Impact: 34.3)
  * `mousedownEventListener` (Impact: 33.2)
  * `hintActivate` (Impact: 25.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 527`, `structural_boundaries: 383`, `args: 238`, `func_start: 199`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `state_mutation: 1661`, `dead_code: 9`, `planned_debt: 3`, `duplicate_logic: 40`, `orphaned_logic: 24`
* *Architecture:* `io: 15`, `concurrency: 8`
* *Defense:* `safety: 187`, `doc: 21`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/zcl_abapgit_convert.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.927 IQR)
- **Top Global Matches:** file_cluster_8: 8.927, file_cluster_7: 9.843, file_cluster_1: 10.076
- **Magnitude:** 2646.85 | **LOC:** 522 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (10.1792%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 45`, `args: 51`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 1`
* *Defense:* `safety: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/zcl_abapgit_object_intf.clas.locals_imp.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.773 IQR)
- **Top Global Matches:** file_cluster_8: 9.773, file_cluster_7: 10.539, file_cluster_2: 10.622
- **Magnitude:** 2579.99 | **LOC:** 746 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.9419%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 58`, `args: 44`, `func_start: 21`
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
- **Risk Profile:** Cognitive Load (8.2761%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_8` (Drift: 7.655 IQR)
- **Top Global Matches:** file_cluster_8: 7.655, file_cluster_7: 8.716, file_cluster_1: 8.927
- **Magnitude:** 1980.3 | **LOC:** 418 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.5557%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 26`, `args: 17`, `func_start: 11`
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
- **Global Archetype:** `file_cluster_8` (Drift: 8.923 IQR)
- **Top Global Matches:** file_cluster_8: 8.923, file_cluster_7: 9.532, file_cluster_1: 9.791
- **Magnitude:** 1755.58 | **LOC:** 442 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.3164%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 30`, `args: 20`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 11`, `doc: 18`, `immutability_locks: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TYPE
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/pages/zcl_abapgit_gui_page_merge_res.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.706 IQR)
- **Top Global Matches:** file_cluster_8: 9.706, file_cluster_7: 10.49, file_cluster_9: 10.626
- **Magnitude:** 1697.16 | **LOC:** 578 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.1068%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 38`, `args: 12`, `func_start: 15`
* *Risk/State:* `dead_code: 6`
* *Architecture:* `api: 1`
* *Defense:* `safety: 5`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/diff/zcl_abapgit_diff_std.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.733 IQR)
- **Top Global Matches:** file_cluster_8: 9.733, file_cluster_0: 10.49, file_cluster_7: 10.49
- **Magnitude:** 1688.01 | **LOC:** 304 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.8034%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 15`, `args: 11`, `func_start: 6`
* *Risk/State:* `state_mutation: 7`, `dead_code: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 7`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/texts/zcl_abapgit_sotr_handler.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.355 IQR)
- **Top Global Matches:** file_cluster_8: 8.355, file_cluster_7: 9.3, file_cluster_1: 9.561
- **Magnitude:** 1660.35 | **LOC:** 448 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.3106%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 25`, `args: 32`, `func_start: 8`
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
- **Global Archetype:** `file_cluster_8` (Drift: 7.932 IQR)
- **Top Global Matches:** file_cluster_8: 7.932, file_cluster_7: 9.001, file_cluster_1: 9.219
- **Magnitude:** 1466.21 | **LOC:** 595 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.8221%), Tech Debt (10.8358%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 31`, `args: 9`, `func_start: 14`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 16`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zabapgit_forms.prog.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.113 IQR)
- **Top Global Matches:** file_cluster_8: 9.113, file_cluster_7: 9.979, file_cluster_2: 10.182
- **Magnitude:** 1458.48 | **LOC:** 375 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.2186%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 22`, `args: 8`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 8`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* `safety: 14`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/texts/zcl_abapgit_i18n_params.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.593 IQR)
- **Top Global Matches:** file_cluster_8: 8.593, file_cluster_7: 9.505, file_cluster_1: 9.786
- **Magnitude:** 1419.64 | **LOC:** 278 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.1201%), Tech Debt (17.0262%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 24`, `args: 21`, `func_start: 9`
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
- **Global Archetype:** `file_cluster_8` (Drift: 8.224 IQR)
- **Top Global Matches:** file_cluster_8: 8.224, file_cluster_7: 9.154, file_cluster_1: 9.397
- **Magnitude:** 1356.28 | **LOC:** 371 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.5799%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 27`, `args: 44`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/objects/texts/zcl_abapgit_sots_handler.clas.abap` (ABAP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.225 IQR)
- **Top Global Matches:** file_cluster_8: 8.225, file_cluster_7: 9.199, file_cluster_1: 9.445
- **Magnitude:** 1296.16 | **LOC:** 328 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.0373%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 19`, `args: 23`, `func_start: 6`
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
- `ci/push-tag.sh` (SHELL) | Magnitude: 2.2 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 13, safety_bypasses: 6, io: 6, structural_boundaries: 4
- `src/ui/zabapgit_js_common.w3mi.data.js` (JAVASCRIPT) | Magnitude: 2970.28 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 1661, indent_spaces: 1526, branch: 527, structural_boundaries: 383

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/zabapgit_password_dialog.prog.abap` (ABAP) | Magnitude: 467.42 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 103, ui_framework: 22, branch: 14, structural_boundaries: 9
- `src/objects/zcl_abapgit_object_iobj.clas.abap` (ABAP) | Magnitude: 19.82 | Delta: **0.151 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 394, pointers: 179, generics: 65, args: 51
- `test/src/zcl_abapgit_object_zag1.clas.testclasses.abap` (ABAP) | Magnitude: 57.48 | Delta: **0.189 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 70, concurrency: 19, structural_boundaries: 16, pointers: 6
- `ci/deploy-release-tag.sh` (SHELL) | Magnitude: 5.93 | Delta: **0.21 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: io: 33, branch: 28, safety_bypasses: 27, state_mutation: 22
- `src/objects/zcl_abapgit_object_otgr.clas.abap` (ABAP) | Magnitude: 22.96 | Delta: **0.253 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 251, pointers: 62, branch: 36, structural_boundaries: 22

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/ui/flow/zcl_abapgit_flow_logic.clas.testclasses.abap` -> Churn: **69.19%** | Cog Load: 11.3319% | Debt: 63.8472%
- `src/ui/zabapgit_js_common.w3mi.data.js` -> Churn: **64.96%** | Cog Load: 87.495% | Debt: 99.9519%

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

- `src/data/zcl_abapgit_data_injector.clas.abap` -> **Severity: 72.5** (Blast Radius: 0.725 * Doc Risk: 100.0%)
- `src/git/zcl_abapgit_git_delta.clas.locals_def.abap` -> **Severity: 72.5** (Blast Radius: 0.725 * Doc Risk: 100.0%)
- `src/json/zcl_abapgit_ajson_ref_init_lib.clas.abap` -> **Severity: 72.5** (Blast Radius: 0.725 * Doc Risk: 100.0%)
- `src/json/zcl_abapgit_ajson_ref_init_lib.clas.locals_imp.abap` -> **Severity: 72.5** (Blast Radius: 0.725 * Doc Risk: 100.0%)
- `src/json/zif_abapgit_ajson_ref_init.intf.abap` -> **Severity: 72.5** (Blast Radius: 0.725 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
