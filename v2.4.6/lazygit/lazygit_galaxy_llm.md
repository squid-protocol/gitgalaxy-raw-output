# ARCHITECTURAL_BRIEF: lazygit
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/lazygit` |
| **Timestamp** | `2026-08-03T19:54:38.304659+00:00` |
| **Scan Duration** | `2.33s` |
| **Git Branch** | `master` |
| **Git Commit** | `4c2c0ce32dd3136503ceef2e1bd6649794047cf0` |
| **Git Remote** | `https://github.com/jesseduffield/lazygit.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 876 malicious artifacts.

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
| Total Artifacts | 2113 |
| Analyzed Artifacts (Scanned) | 891 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1222 |
| Total LOC | 70157 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 42.2% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4339 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3158 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.9509 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 21 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 859 | 65597 | 96.4% |
| SHELL | 12 | 156 | 1.3% |
| MARKDOWN | 7 | 0 | 0.8% |
| JSON | 7 | 4165 | 0.8% |
| NIX | 3 | 124 | 0.3% |
| DOCKERFILE | 1 | 13 | 0.1% |
| MAKEFILE | 1 | 52 | 0.1% |
| YAML | 1 | 50 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `8.386`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 841 | 94.4% |
| file_cluster_13 | 23 | 2.6% |
| file_cluster_4 | 7 | 0.8% |
| file_cluster_11 | 5 | 0.6% |
| file_cluster_6 | 4 | 0.4% |
| file_cluster_9 | 1 | 0.1% |
| file_cluster_15 | 1 | 0.1% |
| file_cluster_0 | 1 | 0.1% |
| file_cluster_17 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 7 | 0.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1222*

**Composition by Extension & Reason:**
- `.go`: 871x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 242 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2264 LOC)
- `.md`: 127x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 20 LOC), 1x Excluded (Machine-Generated Source Code Signature: 105 LOC)
- `no_extension`: 101x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.s`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1054 LOC), 1x Excluded (Static Asset Blob without Intent: 2049 LOC)
- `.txt`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bash`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tmpl`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mod`: 1x Unsupported Format (.mod)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 16.5 | 4.1 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.7 | 58.1 | 53.6 | 50.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 29.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 10.5 | 0.0 | 0.0 |
| API Exposure | 0.0 | 18.8 | 5.9 | 5.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 36.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 1.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 97.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 8.9 | 1.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 90.4 | 6.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 32.7 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `demo/record_demo.sh` (Hits: 13)
- `scripts/bisect.sh` (Hits: 8)
- `scripts/update_language_files.sh` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **utils.go** (`pkg/utils/utils.go`) — 104 inbound connections
2. **gocui.go** (`pkg/theme/gocui.go`) — 93 inbound connections
3. **models.go** (`pkg/gui/services/custom_commands/models.go`) — 92 inbound connections
4. **os.go** (`pkg/commands/oscommands/os.go`) — 49 inbound connections
5. **style.go** (`pkg/theme/style.go`) — 47 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **file_icons.go** (`pkg/gui/presentation/icons/file_icons.go`) — 723 outbound dependencies
2. **gui.go** (`pkg/gui/gui.go`) — 61 outbound dependencies
3. **random.go** (`pkg/integration/components/random.go`) — 52 outbound dependencies
4. **lines_test.go** (`pkg/utils/lines_test.go`) — 32 outbound dependencies
5. **app.go** (`pkg/app/app.go`) — 26 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Refresh` (@ `pkg/gui/controllers/helpers/refresh_helper.go`) -> Impact: **445.5** | LOC: 581
- `getBranchDisplayStrings` (@ `pkg/gui/presentation/branches.go`) -> Impact: **208.3** | LOC: 216
  * *Intent:* // getBranchDisplayStrings returns the display string of branch
- `NewCmdTask` (@ `pkg/tasks/tasks.go`) -> Impact: **183.1** | LOC: 282
- `getBoxDrawingChars` (@ `pkg/gui/presentation/graph/cell.go`) -> Impact: **180.7** | LOC: 37
- `startInteractiveRebaseWithEdit` (@ `pkg/gui/controllers/local_commits_controller.go`) -> Impact: **171.3** | LOC: 464
  * *Intent:* // we've selected the top commit so no rebase is required
- `Clear` (@ `pkg/integration/components/view_driver.go`) -> Impact: **169.5** | LOC: 438
- `wrappedPromptConfirmationFunction` (@ `pkg/gui/controllers/helpers/confirmation_helper.go`) -> Impact: **103.0** | LOC: 259
- `GetCommitListDisplayStrings` (@ `pkg/gui/presentation/commits.go`) -> Impact: **96.4** | LOC: 140
- `GetWorktrees` (@ `pkg/commands/git_commands/worktree_loader.go`) -> Impact: **82.6** | LOC: 176
- `getPreset` (@ `pkg/config/editor_presets.go`) -> Impact: **82.3** | LOC: 126
  * *Intent:* // IF YOU ADD A PRESET TO THIS FUNCTION YOU MUST UPDATE THE `Supported presets` SECTION OF docs/Config.md

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `Close` (@ `pkg/app/app.go`) -> **O(2^N) [Recursive]**
- `New` (@ `pkg/commands/git_cmd_obj_builder.go`) -> **O(2^N) [Recursive]**
- `Quote` (@ `pkg/commands/git_cmd_obj_builder.go`) -> **O(2^N) [Recursive]**
- `NewShell` (@ `pkg/commands/git_cmd_obj_builder.go`) -> **O(2^N) [Recursive]**
- `RunAndProcessLines` (@ `pkg/commands/git_cmd_obj_runner.go`) -> **O(2^N) [Recursive]**
  * *Intent:* // here we're wrapping the default command runner in some git-specific stuff e.g. retry logic if we get an error due to the presence of .git/index.loc...
- `New` (@ `pkg/commands/git_commands/branch.go`) -> **O(2^N) [Recursive]**
  * *Intent:* // New creates a new branch
- `RunWithOutput` (@ `pkg/commands/git_commands/custom.go`) -> **O(2^N) [Recursive]**
  * *Intent:* // Only to be used for the sake of running custom commands specified by the user. // If you want to run a new command, try finding a place for it in o...
- `GetCommitURL` (@ `pkg/commands/git_commands/hosting_service.go`) -> **O(2^N) [Recursive]**
- `GetPullRequestURL` (@ `pkg/commands/git_commands/hosting_service.go`) -> **O(2^N) [Recursive]**
- `EditRebase` (@ `pkg/commands/git_commands/rebase.go`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `Refresh` (@ `pkg/gui/controllers/helpers/refresh_helper.go`) -> DB Complexity: **107**
- `resetHelpersAndControllers` (@ `pkg/gui/controllers.go`) -> DB Complexity: **81**
  * *Intent:* // Note, the order of controllers determines the order in which keybindings appear // in the keybinding menu: the earlier that the controller is attac...
- `wrappedPromptConfirmationFunction` (@ `pkg/gui/controllers/helpers/confirmation_helper.go`) -> DB Complexity: **80**
- `NewCmdTask` (@ `pkg/tasks/tasks.go`) -> DB Complexity: **68**
- `getBranchDisplayStrings` (@ `pkg/gui/presentation/branches.go`) -> DB Complexity: **60**
  * *Intent:* // getBranchDisplayStrings returns the display string of branch
- `Clear` (@ `pkg/integration/components/view_driver.go`) -> DB Complexity: **50**
- `onNewRepo` (@ `pkg/gui/gui.go`) -> DB Complexity: **48**
- `GetWorktrees` (@ `pkg/commands/git_commands/worktree_loader.go`) -> DB Complexity: **44**
- `createAllViews` (@ `pkg/gui/views.go`) -> DB Complexity: **42**
- `Anonymous_Block_[Truncated]` (@ `demo/record_demo.sh`) -> DB Complexity: **41**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pkg/gui/controllers` | 60 | 8063.58 | 27.92% | 62.93% |
| `pkg/gui/controllers/helpers` | 39 | 4692.52 | 41.62% | 71.09% |
| `pkg/commands/git_commands` | 36 | 4045.3 | 40.81% | 67.26% |
| `pkg/integration/components` | 23 | 3434.58 | 16.43% | 66.64% |
| `pkg/gui` | 24 | 2822.94 | 46.71% | 71.91% |
| `pkg/gui/context` | 35 | 2522.24 | 29.23% | 82.59% |
| `pkg/utils` | 32 | 1728.06 | 33.6% | 61.52% |
| `pkg/gui/filetree` | 11 | 1636.54 | 33.2% | 67.08% |
| `pkg/integration/tests/interactive_rebase` | 60 | 1487.66 | 2.17% | 0.0% |
| `pkg/integration/tests/commit` | 59 | 1436.94 | 3.08% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `pkg/app/daemon/daemon.go` -> **100.0%** Exposure
- `pkg/commands/git_commands/bisect_info.go` -> **100.0%** Exposure
- `pkg/commands/models/commit_file.go` -> **100.0%** Exposure
- `pkg/gui/context/dynamic_title_builder.go` -> **100.0%** Exposure
- `pkg/gui/context/filtered_list.go` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `cmd/i18n/main.go` -> **100.0%** Exposure
- `pkg/app/entry_point.go` -> **100.0%** Exposure
- `pkg/commands/git_commands/bisect.go` -> **100.0%** Exposure
- `pkg/commands/git_commands/branch_loader.go` -> **100.0%** Exposure
- `pkg/commands/git_commands/commit.go` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pkg/app/daemon/daemon.go` -> **11** Orphaned Functions | **27** Duplicates
- `pkg/integration/components/views.go` -> **30** Orphaned Functions | **0** Duplicates
- `pkg/gui/context/base_context.go` -> **28** Orphaned Functions | **0** Duplicates
- `pkg/gui/gui.go` -> **27** Orphaned Functions | **0** Duplicates
- `pkg/commands/git_commands/branch.go` -> **25** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`pkg/theme/style.go`** -> AI Confidence: **99.48%**
2. **`pkg/app/entry_point.go`** -> AI Confidence: **99.39%**
3. **`pkg/config/editor_presets.go`** -> AI Confidence: **99.39%**
4. **`pkg/gui/controllers/helpers/search_helper.go`** -> AI Confidence: **99.34%**
5. **`pkg/commands/git_commands/branch_loader.go`** -> AI Confidence: **99.31%**
6. **`pkg/commands/git_commands/commit_loader.go`** -> AI Confidence: **99.31%**
7. **`pkg/commands/git_commands/remote_loader.go`** -> AI Confidence: **99.31%**
8. **`pkg/commands/git_commands/working_tree.go`** -> AI Confidence: **99.31%**
9. **`pkg/commands/git_commands/worktree_loader.go`** -> AI Confidence: **99.31%**
10. **`pkg/config/app_config.go`** -> AI Confidence: **99.31%**
11. **`pkg/gui/command_log_panel.go`** -> AI Confidence: **99.31%**
12. **`pkg/gui/context/local_commits_context.go`** -> AI Confidence: **99.31%**
13. **`pkg/gui/controllers.go`** -> AI Confidence: **99.31%**
14. **`pkg/gui/controllers/files_controller.go`** -> AI Confidence: **99.31%**
15. **`pkg/gui/controllers/helpers/confirmation_helper.go`** -> AI Confidence: **99.31%**
16. **`pkg/gui/controllers/helpers/diff_helper.go`** -> AI Confidence: **99.31%**
17. **`pkg/gui/controllers/helpers/fixup_helper.go`** -> AI Confidence: **99.31%**
18. **`pkg/gui/controllers/helpers/refresh_helper.go`** -> AI Confidence: **99.31%**
19. **`pkg/gui/controllers/helpers/window_arrangement_helper.go`** -> AI Confidence: **99.31%**
20. **`pkg/gui/controllers/workspace_reset_controller.go`** -> AI Confidence: **99.31%**
21. **`pkg/gui/filetree/file_tree_view_model.go`** -> AI Confidence: **99.31%**
22. **`pkg/gui/filetree/node.go`** -> AI Confidence: **99.31%**
23. **`pkg/gui/keybindings/keybindings.go`** -> AI Confidence: **99.31%**
24. **`pkg/gui/options_map.go`** -> AI Confidence: **99.31%**
25. **`pkg/gui/presentation/commits.go`** -> AI Confidence: **99.31%**
26. **`pkg/gui/presentation/graph/graph.go`** -> AI Confidence: **99.31%**
27. **`pkg/gui/presentation/status.go`** -> AI Confidence: **99.31%**
28. **`pkg/gui/presentation/worktrees.go`** -> AI Confidence: **99.31%**
29. **`pkg/gui/services/custom_commands/client.go`** -> AI Confidence: **99.31%**
30. **`pkg/gui/view_helpers.go`** -> AI Confidence: **99.31%**
31. **`pkg/gui/views.go`** -> AI Confidence: **99.31%**
32. **`pkg/integration/clients/cli.go`** -> AI Confidence: **99.31%**
33. **`pkg/integration/clients/tui.go`** -> AI Confidence: **99.31%**
34. **`pkg/integration/components/runner.go`** -> AI Confidence: **99.31%**
35. **`pkg/jsonschema/generate.go`** -> AI Confidence: **99.31%**
36. **`pkg/tasks/tasks.go`** -> AI Confidence: **99.31%**
37. **`pkg/utils/lines_test.go`** -> AI Confidence: **99.31%**
38. **`pkg/utils/rebase_todo.go`** -> AI Confidence: **99.31%**
39. **`Makefile`** -> AI Confidence: **99.29%**
40. **`pkg/gui/presentation/branches.go`** -> AI Confidence: **99.29%**
41. **`pkg/integration/tests/commit/search.go`** -> AI Confidence: **99.29%**
42. **`pkg/integration/tests/conflicts/resolve_non_textual_conflicts.go`** -> AI Confidence: **99.29%**
43. **`pkg/integration/tests/file/discard_all_dir_changes.go`** -> AI Confidence: **99.29%**
44. **`pkg/integration/tests/file/shared.go`** -> AI Confidence: **99.29%**
45. **`pkg/utils/thread_safe_map_test.go`** -> AI Confidence: **99.29%**
46. **`scripts/bump_gocui.sh`** -> AI Confidence: **99.29%**
47. **`scripts/bump_lazycore.sh`** -> AI Confidence: **99.29%**
48. **`pkg/integration/clients/injector/main.go`** -> AI Confidence: **99.25%**
49. **`pkg/app/app.go`** -> AI Confidence: **99.24%**
50. **`pkg/app/daemon/rebase.go`** -> AI Confidence: **99.24%**
51. **`pkg/commands/git_commands/file_loader.go`** -> AI Confidence: **99.24%**
52. **`pkg/commands/git_commands/patch.go`** -> AI Confidence: **99.24%**
53. **`pkg/commands/git_commands/submodule.go`** -> AI Confidence: **99.24%**
54. **`pkg/commands/oscommands/cmd_obj_runner.go`** -> AI Confidence: **99.24%**
55. **`pkg/gui/controllers/helpers/branches_helper.go`** -> AI Confidence: **99.24%**
56. **`pkg/gui/controllers/helpers/cherry_pick_helper.go`** -> AI Confidence: **99.24%**
57. **`pkg/gui/controllers/helpers/merge_and_rebase_helper.go`** -> AI Confidence: **99.24%**
58. **`pkg/gui/controllers/helpers/repos_helper.go`** -> AI Confidence: **99.24%**
59. **`pkg/gui/controllers/local_commits_controller.go`** -> AI Confidence: **99.24%**
60. **`pkg/gui/controllers/remotes_controller.go`** -> AI Confidence: **99.24%**
61. **`pkg/gui/controllers/status_controller.go`** -> AI Confidence: **99.24%**
62. **`pkg/gui/gui.go`** -> AI Confidence: **99.24%**
63. **`pkg/gui/presentation/icons/git_icons.go`** -> AI Confidence: **99.24%**
64. **`pkg/gui/services/custom_commands/handler_creator.go`** -> AI Confidence: **99.24%**
65. **`pkg/i18n/i18n.go`** -> AI Confidence: **99.24%**
66. **`pkg/integration/tests/tests.go`** -> AI Confidence: **99.24%**
67. **`pkg/theme/gocui.go`** -> AI Confidence: **99.24%**
68. **`pkg/updates/updates.go`** -> AI Confidence: **99.24%**
69. **`pkg/commands/git_commands/stash_loader.go`** -> AI Confidence: **99.23%**
70. **`pkg/gui/controllers/bisect_controller.go`** -> AI Confidence: **99.23%**
71. **`pkg/gui/keybindings.go`** -> AI Confidence: **99.23%**
72. **`pkg/gui/pty.go`** -> AI Confidence: **99.23%**
73. **`pkg/gui/services/custom_commands/menu_generator.go`** -> AI Confidence: **99.23%**
74. **`pkg/utils/rebase_todo_test.go`** -> AI Confidence: **99.23%**
75. **`pkg/commands/git_commands/branch.go`** -> AI Confidence: **99.18%**
76. **`pkg/commands/git_commands/file.go`** -> AI Confidence: **99.18%**
77. **`pkg/commands/git_commands/repo_paths.go`** -> AI Confidence: **99.18%**
78. **`pkg/gui/controllers/basic_commits_controller.go`** -> AI Confidence: **99.18%**
79. **`pkg/gui/controllers/helpers/suggestions_helper.go`** -> AI Confidence: **99.18%**
80. **`pkg/gui/controllers/helpers/tags_helper.go`** -> AI Confidence: **99.18%**
81. **`pkg/gui/controllers/helpers/update_helper.go`** -> AI Confidence: **99.18%**
82. **`pkg/gui/controllers/submodules_controller.go`** -> AI Confidence: **99.18%**
83. **`pkg/gui/controllers/sync_controller.go`** -> AI Confidence: **99.18%**
84. **`pkg/gui/filetree/commit_file_tree_view_model.go`** -> AI Confidence: **99.18%**
85. **`pkg/gui/popup/popup_handler.go`** -> AI Confidence: **99.18%**
86. **`pkg/integration/components/shell.go`** -> AI Confidence: **99.18%**
87. **`pkg/utils/utils.go`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `pkg/gui/presentation/icons/file_icons.go` -> **0.0005%** Exposure
### Exploit Generation Surface
- `pkg/gui/controllers/status_controller.go` -> **100.0%** Exposure
- `pkg/utils/lines_test.go` -> **5.6721%** Exposure
- `pkg/gui/controllers/local_commits_controller.go` -> **0.0003%** Exposure
- `pkg/gui/controllers/branches_controller.go` -> **0.0001%** Exposure
- `pkg/gui/controllers/files_controller.go` -> **0.0001%** Exposure
### Weaponizable Injection Vectors
- `pkg/gui/filetree/commit_file_node.go` -> **100.0%** Exposure
- `pkg/gui/filetree/file_node.go` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `pkg/gui/controllers/custom_patch_options_menu_action.go` -> **100.0%** Exposure
- `pkg/gui/controllers/helpers/refs_helper.go` -> **100.0%** Exposure
- `pkg/gui/controllers/local_commits_controller.go` -> **100.0%** Exposure
- `pkg/gui/controllers/workspace_reset_controller.go` -> **100.0%** Exposure
- `pkg/tasks/tasks.go` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3257` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pkg/gui/gui_driver.go` (GO) -> Cumulative Risk: **756.66**
- **Archetype:** `file_cluster_8` (Distance: 12.604 IQR)
- **Magnitude:** 179.5 | **LOC:** 174 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Concurrency (99.9089%), Tech Debt (99.2663%)
- **Heaviest Functions:** `PressKey` (Impact: 10.9), `ContextForView` (Impact: 10.2), `View` (Impact: 10.1)

### 2. `pkg/gui/controllers/local_commits_controller.go` (GO) -> Cumulative Risk: **754.88**
- **Archetype:** `file_cluster_8` (Distance: 11.911 IQR)
- **Magnitude:** 643.96 | **LOC:** 1560 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.5136%)
- **Heaviest Functions:** `startInteractiveRebaseWithEdit` (Impact: 171.3), `GetOnRenderToMain` (Impact: 17.4), `drop` (Impact: 16.8)

### 3. `pkg/gui/controllers/status_controller.go` (GO) -> Cumulative Risk: **743.37**
- **Archetype:** `file_cluster_8` (Distance: 11.923 IQR)
- **Magnitude:** 189.66 | **LOC:** 260 | **CtrlFlow:** 40.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Logic Bomb (100.0%), State Flux (99.8111%)
- **Heaviest Functions:** `onClick` (Impact: 18.5), `askForConfigFile` (Impact: 14.4), `GetOnRenderToMain` (Impact: 11.8)

### 4. `pkg/tasks/tasks.go` (GO) -> Cumulative Risk: **720.34**
- **Archetype:** `file_cluster_4` (Distance: 13.214 IQR)
- **Magnitude:** 535.3 | **LOC:** 432 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (96.6831%)
- **Heaviest Functions:** `NewCmdTask` (Impact: 183.1), `ReadToEnd` (Impact: 10.2), `ReadLines` (Impact: 5.2)

### 5. `pkg/gui/context/menu_context.go` (GO) -> Cumulative Risk: **685.69**
- **Archetype:** `file_cluster_8` (Distance: 11.959 IQR)
- **Magnitude:** 175.94 | **LOC:** 272 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9463%), State Flux (84.999%)
- **Heaviest Functions:** `OnMenuPress` (Impact: 18.4), `GetDisplayStrings` (Impact: 17.2), `FilterPrefix` (Impact: 10.1)

### 6. `pkg/gui/context/sub_commits_context.go` (GO) -> Cumulative Risk: **684.45**
- **Archetype:** `file_cluster_8` (Distance: 11.971 IQR)
- **Magnitude:** 203.74 | **LOC:** 245 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (97.7691%), Cognitive Load (91.9537%)
- **Heaviest Functions:** `NewSubCommitsContext` (Impact: 19.3), `IndexForGotoBottom` (Impact: 12.0), `GetSelectedRefRangeForDiffFiles` (Impact: 9.5)

### 7. `pkg/gui/context/base_context.go` (GO) -> Cumulative Risk: **681.48**
- **Archetype:** `file_cluster_8` (Distance: 12.328 IQR)
- **Magnitude:** 229.36 | **LOC:** 248 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9991%), Safety Score (85.6804%)
- **Heaviest Functions:** `AddOnClickFn` (Impact: 8.3), `GetKeybindings` (Impact: 7.8), `GetMouseKeybindings` (Impact: 7.8)

### 8. `pkg/gui/controllers/helpers/fixup_helper.go` (GO) -> Cumulative Risk: **672.86**
- **Archetype:** `file_cluster_4` (Distance: 13.995 IQR)
- **Magnitude:** 366.18 | **LOC:** 413 | **CtrlFlow:** 68.1% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9678%), Safety Score (99.0918%)
- **Heaviest Functions:** `blameAddedLines` (Impact: 43.6), `parseDiff` (Impact: 40.4), `blameDeletedLines` (Impact: 21.2)

### 9. `pkg/commands/git_commands/branch.go` (GO) -> Cumulative Risk: **668.27**
- **Archetype:** `file_cluster_8` (Distance: 12.581 IQR)
- **Magnitude:** 271.0 | **LOC:** 363 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 87.5%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9995%), Tech Debt (99.9986%)
- **Heaviest Functions:** `CurrentBranchInfo` (Impact: 19.9), `Merge` (Impact: 11.6), `IsBranchMerged` (Impact: 6.3)

### 10. `pkg/gui/gui.go` (GO) -> Cumulative Risk: **667.15**
- **Archetype:** `file_cluster_8` (Distance: 13.702 IQR)
- **Magnitude:** 370.88 | **LOC:** 1194 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 69.2%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.4101%), Safety Score (90.206%)
- **Heaviest Functions:** `onNewRepo` (Impact: 70.5), `onSwitchToNewRepo` (Impact: 9.1), `GetItemOperation` (Impact: 2.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pkg/integration/components/random.go` (GO | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.837 IQR)
- **Top Global Matches:** file_cluster_8: 9.837, file_cluster_13: 10.237, file_cluster_7: 10.408
- **Magnitude:** 1543.04 | **LOC:** 498 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.9461%), Tech Debt (37.5463%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 212`, `args: 8`, `func_start: 8`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 55`, `planned_debt: 12`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `api: 22`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 7`, `doc: 9`, `test: 4`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` lo, peace-time, io, quash-rebellion, cleanup-code, utils, clipboard, utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/controllers/helpers/refresh_helper.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.587 IQR)
- **Top Global Matches:** file_cluster_8: 13.587, file_cluster_15: 13.682, file_cluster_13: 13.745
- **Magnitude:** 782.82 | **LOC:** 953 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 107
- **Risk Profile:** Cognitive Load (55.6183%), Tech Debt (9.0927%)
**Top Internal Functions/Classes:**
  * `Refresh` (Impact: 445.5 | O(2^N) | DB: 107)
  * `NewRefreshHelper` (Impact: 4.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 64`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 287`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 36`, `import: 1`
* *Defense:* `safety: 19`, `doc: 10`, `sync_locks: 14`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` lo, sync, HEAD, block-ui, utils, time, strings, presentation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/controllers/branches_controller.go` (GO | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.229 IQR)
- **Top Global Matches:** file_cluster_8: 12.229, file_cluster_7: 12.665, file_cluster_15: 12.665
- **Magnitude:** 746.96 | **LOC:** 987 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (38.2533%), Tech Debt (10.4684%)
**Top Internal Functions/Classes:**
  * `rename` (Impact: 45.6 | O(N^1) | DB: 19)
  * `viewUpstreamOptions` (Impact: 37.9 | O(N^1) | DB: 30)
  * `delete` (Impact: 25.3 | O(N^1) | DB: 12)
  * `fastForward` (Impact: 17.1 | O(N^1) | DB: 8)
  * `stateText` (Impact: 16.9 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 131`, `args: 42`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `state_mutation: 235`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 200`, `import: 1`
* *Defense:* `safety: 22`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` lo, CLOSED, utils, strings, icons, color, MERGED, helpers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/controllers/local_commits_controller.go` (GO | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.911 IQR)
- **Top Global Matches:** file_cluster_8: 11.911, file_cluster_11: 12.166, file_cluster_15: 12.242
- **Magnitude:** 643.96 | **LOC:** 1560 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^2) | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (37.825%), Tech Debt (87.9021%)
**Top Internal Functions/Classes:**
  * `startInteractiveRebaseWithEdit` (Impact: 171.3 | O(N^2) | DB: 32)
    * *Intent:* // we've selected the top commit so no rebase is required
  * `GetOnRenderToMain` (Impact: 17.4 | O(N^1) | DB: 6)
  * `drop` (Impact: 16.8 | O(N^1) | DB: 8)
  * `reword` (Impact: 13.5 | O(N^1) | DB: 3)
  * `doRewordEditor` (Impact: 9.9 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 136`, `args: 41`, `func_start: 41`
* *Risk/State:* `state_mutation: 155`, `planned_debt: 30`, `orphaned_logic: 9`
* *Architecture:* `api: 182`, `import: 1`
* *Defense:* `safety: 15`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` lo, todo, gocui, helpers, strings, squashAbove, selectedCommit, git_commands...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/filetree/node.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.0 IQR)
- **Top Global Matches:** file_cluster_8: 13.0, file_cluster_15: 13.09, file_cluster_11: 13.252
- **Magnitude:** 584.86 | **LOC:** 385 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (49.1021%), Tech Debt (9.0308%)
**Top Internal Functions/Classes:**
  * `compressAux` (Impact: 36.9 | O(2^N) | DB: 9)
  * `SomeFile` (Impact: 35.0 | O(2^N) | DB: 1)
  * `EveryFile` (Impact: 35.0 | O(2^N) | DB: 1)
  * `FindFirstFileBy` (Impact: 35.0 | O(2^N) | DB: 2)
  * `ForEachFile` (Impact: 30.1 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 58`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 150`, `planned_debt: 1`
* *Architecture:* `api: 33`, `import: 1`
* *Defense:* `safety: 2`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.715
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001124
  * `Imports (Out-Degree: 1):` lo, slices, foldersFirst, strings, filesFirst, path, types, models
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pkg/gui/controllers/files_controller.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.986 IQR)
- **Top Global Matches:** file_cluster_8: 12.986, file_cluster_0: 13.139, file_cluster_13: 13.174
- **Magnitude:** 577.68 | **LOC:** 1590 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 61.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (63.4124%), Tech Debt (29.1114%)
**Top Internal Functions/Classes:**
  * `GetOnRenderToMain` (Impact: 51.9 | O(N^1) | DB: 25)
  * `toggleStagedAllWithLock` (Impact: 34.1 | O(N^1) | DB: 11)
  * `pressWithLock` (Impact: 31.9 | O(N^1) | DB: 10)
  * `ResetSubmodule` (Impact: 25.6 | O(2^N) | DB: 4)
  * `GetOnClick` (Impact: 12.3 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 72`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 198`, `dead_code: 3`, `orphaned_logic: 9`
* *Architecture:* `api: 150`, `import: 1`
* *Defense:* `safety: 18`, `doc: 13`, `sync_locks: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` lo, path, utils, DU, strings, AM, DD, AU...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/tasks/tasks.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.214 IQR)
- **Top Global Matches:** file_cluster_4: 13.214, file_cluster_15: 13.878, file_cluster_13: 13.953
- **Magnitude:** 535.3 | **LOC:** 432 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 68
- **Risk Profile:** Cognitive Load (49.9988%), Tech Debt (26.5316%)
**Top Internal Functions/Classes:**
  * `NewCmdTask` (Impact: 183.1 | O(N^2) | DB: 68)
  * `ReadToEnd` (Impact: 10.2 | O(N^1) | DB: 1)
  * `ReadLines` (Impact: 5.2 | O(N^1) | DB: 1)
  * `NewViewBufferManager` (Impact: 3.0 | O(N^1) | DB: 3)
  * `GetTaskKey` (Impact: 2.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 46`, `args: 7`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 171`, `dead_code: 2`, `orphaned_logic: 4`
* *Architecture:* `io: 5`, `api: 16`, `concurrency: 139`, `import: 1`
* *Defense:* `safety: 7`, `doc: 15`, `sync_locks: 15`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007156
  * `Imports (Out-Degree: 4):` time, io, gocui, go-deadlock, exec, sync, oscommands, bufio...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pkg/gui/controllers/commits_files_controller.go` (GO | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.219 IQR)
- **Top Global Matches:** file_cluster_8: 12.219, file_cluster_15: 12.611, file_cluster_7: 12.637
- **Magnitude:** 529.62 | **LOC:** 641 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 71.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (47.6097%), Tech Debt (17.0195%)
**Top Internal Functions/Classes:**
  * `toggleForPatch` (Impact: 32.5 | O(N^1) | DB: 11)
  * `openCopyMenu` (Impact: 17.9 | O(N^1) | DB: 11)
  * `discard` (Impact: 16.7 | O(N^1) | DB: 8)
  * `enterCommitFile` (Impact: 13.8 | O(N^1) | DB: 3)
  * `canDiscardFileChanges` (Impact: 13.5 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 87`, `args: 30`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 183`, `orphaned_logic: 5`
* *Architecture:* `api: 124`, `import: 1`
* *Defense:* `safety: 13`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` lo, gocui, patch, helpers, strings, filepath, git_commands, fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/config/user_config.go` (GO | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.638 IQR)
- **Top Global Matches:** file_cluster_0: 11.638, file_cluster_8: 11.924, file_cluster_7: 12.034
- **Magnitude:** 499.92 | **LOC:** 1081 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 61.1%
- **Algorithmic:** O(N) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (6.8525%), Tech Debt (21.4861%)
**Top Internal Functions/Classes:**
  * `GetDefaultConfig` (Impact: 9.2 | O(N^1) | DB: 7)
    * *Intent:* // Array of pagers. Each entry has the following format: // [dev] The following documentation is dup...
  * `JSONSchemaExtend` (Impact: 2.6 | O(N^1) | DB: 3)
    * *Intent:* // If true, when using the panel jump keys (default 1 through 5) and target panel is already active,...
  * `UseFuzzySearch` (Impact: 2.4 | O(N^1))
    * *Intent:* // Format used when displaying time if the time is less than 24 hours ago.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 22`, `args: 3`, `func_start: 3`, `class_start: 6`
* *Risk/State:* `state_mutation: 85`, `planned_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 392`, `import: 1`
* *Defense:* `doc: 109`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jsonschema, diff-so-fancy, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/integration/components/shell.go` (GO | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.268 IQR)
- **Top Global Matches:** file_cluster_8: 13.268, file_cluster_15: 13.367, file_cluster_7: 13.526
- **Magnitude:** 456.5 | **LOC:** 526 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (49.2469%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `CreateRepoHistory` (Impact: 18.8 | O(N^1) | DB: 20)
    * *Intent:* // Only to be used in demos, because the list might change and we don't want
  * `CopyFile` (Impact: 12.0 | O(N^1) | DB: 16)
  * `RunShellCommand` (Impact: 8.3 | O(N^1) | DB: 8)
  * `CreateNCommitsWithRandomMessages` (Impact: 7.9 | O(N^1) | DB: 2)
    * *Intent:* // creates commits 01, 02, 03, ..., n with a new file in each // The reason for padding with zeroes ...
  * `CreateFile` (Impact: 6.0 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 66`, `args: 59`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 156`
* *Architecture:* `io: 3`, `api: 99`, `import: 1`
* *Defense:* `safety: 13`, `doc: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.715
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001124
  * `Imports (Out-Degree: 2):` time, io, rand, exec, git, filepath, fmt, os...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pkg/gui/patch_exploring/state.go` (GO | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.251 IQR)
- **Top Global Matches:** file_cluster_8: 13.251, file_cluster_15: 13.269, file_cluster_7: 13.486
- **Magnitude:** 435.64 | **LOC:** 439 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (52.6879%), Tech Debt (98.8342%)
**Top Internal Functions/Classes:**
  * `SelectPreviousHunk` (Impact: 18.8 | O(N^1) | DB: 5)
  * `selectionRangeForCurrentBlockOfChanges` (Impact: 16.8 | O(N^1) | DB: 5)
  * `SelectedViewRange` (Impact: 16.5 | O(N^1))
  * `SelectNextHunk` (Impact: 14.2 | O(N^1) | DB: 5)
  * `CycleSelection` (Impact: 12.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 30`, `args: 38`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 186`, `dead_code: 1`, `orphaned_logic: 22`
* *Architecture:* `api: 36`, `import: 1`
* *Defense:* `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` lo, gocui, patch, set, strings, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/integration/clients/tui.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.629 IQR)
- **Top Global Matches:** file_cluster_8: 13.629, file_cluster_11: 13.937, file_cluster_13: 13.937
- **Magnitude:** 419.1 | **LOC:** 409 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (85.9286%), Tech Debt (9.9617%)
**Top Internal Functions/Classes:**
  * `RunTUI` (Impact: 73.8 | O(N^1) | DB: 40)
  * `layout` (Impact: 40.7 | O(N^1) | DB: 31)
  * `suspendAndRunTest` (Impact: 8.0 | O(N^1) | DB: 3)
  * `filterWithString` (Impact: 7.9 | O(N^1) | DB: 2)
  * `renderTests` (Impact: 7.0 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 47`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 233`, `orphaned_logic: 1`
* *Architecture:* `api: 14`, `import: 1`
* *Defense:* `safety: 36`, `doc: 1`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` lo, gui, tests, gocui, components, exec, strings, utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/presentation/branches.go` (GO | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.95 IQR)
- **Top Global Matches:** file_cluster_8: 12.95, file_cluster_13: 13.222, file_cluster_7: 13.235
- **Magnitude:** 401.3 | **LOC:** 288 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N) | **DB Complexity:** 60
- **Risk Profile:** Cognitive Load (60.0373%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getBranchDisplayStrings` (Impact: 208.3 | O(N^1) | DB: 60)
    * *Intent:* // getBranchDisplayStrings returns the display string of branch
  * `GetBranchListDisplayStrings` (Impact: 2.5 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 24`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 181`, `dead_code: 1`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.765
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00367
  * `Imports (Out-Degree: 7):` lo, MERGED, time, theme, CLOSED, strings, OPEN, icons...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pkg/gui/gui.go` (GO | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.702 IQR)
- **Top Global Matches:** file_cluster_8: 13.702, file_cluster_15: 13.788, file_cluster_13: 13.832
- **Magnitude:** 370.88 | **LOC:** 1194 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 69.2%
- **Algorithmic:** O(N) | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (71.7308%), Tech Debt (99.4101%)
**Top Internal Functions/Classes:**
  * `onNewRepo` (Impact: 70.5 | O(N^1) | DB: 48)
  * `onSwitchToNewRepo` (Impact: 9.1 | O(N^1) | DB: 1)
  * `GetItemOperation` (Impact: 2.7 | O(N^1))
  * `ClearItemOperation` (Impact: 2.7 | O(N^1))
  * `SetUpdating` (Impact: 2.6 | O(N^1) | DB: 1)
    * *Intent:* // this is the initial dir we are in upon opening lazygit. We hold onto this
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 53`, `args: 30`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `state_mutation: 156`, `dead_code: 2`, `orphaned_logic: 27`
* *Architecture:* `api: 58`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 8`, `doc: 8`, `sync_locks: 7`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.908
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003511
  * `Imports (Out-Degree: 23):` git_config, lo, reflect, io, graph, sync, Refresher.RefreshInterval, configs...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pkg/gui/controllers/helpers/fixup_helper.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.995 IQR)
- **Top Global Matches:** file_cluster_4: 13.995, file_cluster_11: 14.313, file_cluster_13: 14.383
- **Magnitude:** 366.18 | **LOC:** 413 | **CtrlFlow:** 68.1% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(N) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (49.7056%), Tech Debt (79.4969%)
**Top Internal Functions/Classes:**
  * `blameAddedLines` (Impact: 43.6 | O(N^1) | DB: 16)
  * `parseDiff` (Impact: 40.4 | O(N^1) | DB: 21)
  * `blameDeletedLines` (Impact: 21.2 | O(N^1) | DB: 10)
  * `IsFixupCommit` (Impact: 17.1 | O(N^1) | DB: 6)
    * *Intent:* // returns the list of commit hashes that introduced the lines which have now been deleted
  * `getDiff` (Impact: 7.5 | O(N^1) | DB: 7)
    * *Intent:* // If a commit can't be found, and the last known commit is already merged,
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 30`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 192`, `dead_code: 2`, `planned_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 6`, `concurrency: 30`, `import: 1`
* *Defense:* `safety: 6`, `doc: 15`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` lo, set, strings, errgroup, regexp, fmt, errors, types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/commands/git_commands/working_tree.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.984 IQR)
- **Top Global Matches:** file_cluster_8: 13.984, file_cluster_15: 14.001, file_cluster_11: 14.09
- **Magnitude:** 360.18 | **LOC:** 610 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 69.2%
- **Algorithmic:** O(N) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (45.9497%), Tech Debt (95.3105%)
**Top Internal Functions/Classes:**
  * `DiscardAllDirChanges` (Impact: 52.0 | O(N^1) | DB: 18)
  * `removeEmptyDirs` (Impact: 25.9 | O(N^1) | DB: 9)
  * `BeforeAndAfterFileForRename` (Impact: 20.8 | O(N^1) | DB: 1)
  * `DiscardUnstagedDirChanges` (Impact: 18.5 | O(N^1) | DB: 7)
  * `RemoveUntrackedDirFiles` (Impact: 12.9 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 58`, `args: 23`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 144`, `dead_code: 1`, `orphaned_logic: 14`
* *Architecture:* `api: 21`, `import: 1`
* *Defense:* `safety: 12`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` lo, set, strings, oscommands, path, filepath, regexp, fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/keybindings.go` (GO | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.98 IQR)
- **Top Global Matches:** file_cluster_8: 9.98, file_cluster_7: 10.554, file_cluster_13: 10.699
- **Magnitude:** 355.02 | **LOC:** 526 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (12.9949%), Tech Debt (36.2766%)
**Top Internal Functions/Classes:**
  * `GetInitialKeybindings` (Impact: 16.2 | O(N^1) | DB: 13)
  * `callKeybindingHandler` (Impact: 15.7 | O(N^1) | DB: 1)
  * `GetInitialKeybindingsWithCustomCommands` (Impact: 7.2 | O(N^1))
  * `noPopupPanel` (Impact: 5.3 | O(N^1))
  * `outsideFilterMode` (Impact: 5.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 21`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 51`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 230`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` gocui, helpers, log, errors, types, context, keybindings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/commands/git_commands/commit_loader.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.245 IQR)
- **Top Global Matches:** file_cluster_8: 13.245, file_cluster_11: 13.318, file_cluster_6: 13.399
- **Magnitude:** 349.92 | **LOC:** 609 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N) | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (42.2417%), Tech Debt (98.4359%)
**Top Internal Functions/Classes:**
  * `getHydratedSequencerCommits` (Impact: 27.2 | O(N^1) | DB: 21)
  * `setCommitStatuses` (Impact: 22.9 | O(N^1) | DB: 4)
  * `extractCommitFromLine` (Impact: 21.1 | O(N^1) | DB: 22)
  * `getConflictedSequencerCommit` (Impact: 13.5 | O(N^1) | DB: 6)
    * *Intent:* // If we have any commits in .git/sequencer/todo, then the last one of // those is the conflicting o...
  * `getLogCmd` (Impact: 8.6 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 32`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 229`, `planned_debt: 13`, `fragile_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 16`, `import: 1`
* *Defense:* `safety: 7`, `doc: 11`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` lo, todo, sort, set, strings, sync, oscommands, bytes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/integration/components/view_driver.go` (GO | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.487 IQR)
- **Top Global Matches:** file_cluster_8: 12.487, file_cluster_15: 12.55, file_cluster_7: 12.8
- **Magnitude:** 345.66 | **LOC:** 654 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (71.1946%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Clear` (Impact: 169.5 | O(2^N) | DB: 50)
  * `Title` (Impact: 5.3 | O(2^N) | DB: 1)
    * *Intent:* // asserts that the view has the expected title
  * `getSelectedLines` (Impact: 2.4 | O(N^1) | DB: 1)
  * `getSelectedRange` (Impact: 2.4 | O(N^1) | DB: 1)
  * `getSelectedLineIdx` (Impact: 2.4 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 68`, `args: 41`, `func_start: 41`, `class_start: 2`
* *Risk/State:* `state_mutation: 122`, `dead_code: 2`
* *Architecture:* `api: 35`, `import: 1`
* *Defense:* `doc: 5`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` lo, strings, fmt, gocui
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/commands/oscommands/os.go` (GO | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.328 IQR)
- **Top Global Matches:** file_cluster_8: 13.328, file_cluster_13: 13.478, file_cluster_4: 13.485
- **Magnitude:** 335.16 | **LOC:** 364 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (41.4117%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `PipeCommands` (Impact: 32.5 | O(N^1) | DB: 14)
    * *Intent:* // PipeCommands runs a heap of commands and pipes their inputs/outputs together like A | B | C
  * `AppendLineToFile` (Impact: 16.0 | O(N^1) | DB: 7)
    * *Intent:* // AppendLineToFile adds a new line in file
  * `CreateFileWithContent` (Impact: 11.4 | O(2^N) | DB: 3)
    * *Intent:* // CreateFileWithContent creates a file with the given content
  * `CopyToClipboard` (Impact: 10.8 | O(2^N) | DB: 4)
  * `OpenLink` (Impact: 10.4 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 55`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 131`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 40`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 18`, `doc: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 60.192
  * `Choke Point (Betweenness):` 0.000692 | `Ripple Effect (Closeness):` 0.11393
  * `Imports (Out-Degree: 3):` lo, io, directory, sync, clipboard, path, utils, str...
  * `Imported By (In-Degree: 49):` (Excluded from Brief to save tokens)

### `pkg/gui/presentation/graph/cell.go` (GO | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.064 IQR)
- **Top Global Matches:** file_cluster_8: 12.064, file_cluster_13: 12.426, file_cluster_7: 12.489
- **Magnitude:** 330.3 | **LOC:** 184 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (98.3428%), Tech Debt (93.4703%)
**Top Internal Functions/Classes:**
  * `getBoxDrawingChars` (Impact: 180.7 | O(N^1))
  * `render` (Impact: 23.7 | O(N^1) | DB: 11)
  * `cachedSprint` (Impact: 11.5 | O(N^1) | DB: 6)
  * `setLeft` (Impact: 7.7 | O(N^1) | DB: 2)
  * `setRight` (Impact: 5.5 | O(N^1) | DB: 2)
    * *Intent:* //nolint:unparam
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 36`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 79`, `orphaned_logic: 8`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `sync_locks: 5`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` sync, color, style, io
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/controllers/helpers/working_tree_helper.go` (GO | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.495 IQR)
- **Top Global Matches:** file_cluster_8: 12.495, file_cluster_15: 12.779, file_cluster_13: 12.793
- **Magnitude:** 325.2 | **LOC:** 419 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (44.2157%), Tech Debt (99.9245%)
**Top Internal Functions/Classes:**
  * `HandleCommitPress` (Impact: 21.5 | O(N^1) | DB: 9)
  * `CreateMergeConflictMenu` (Impact: 15.4 | O(N^1) | DB: 6)
  * `mergeFileWithTempFiles` (Impact: 14.1 | O(N^1) | DB: 7)
  * `WithEnsureCommittableFiles` (Impact: 10.5 | O(N^1) | DB: 1)
  * `FileForSubmodule` (Impact: 10.2 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 72`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 96`, `dead_code: 1`, `duplicate_logic: 10`, `orphaned_logic: 6`
* *Architecture:* `api: 46`, `import: 1`
* *Defense:* `safety: 16`, `doc: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` lo, strings, config, git_commands, regexp, fmt, errors, types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/controllers/helpers/branches_helper.go` (GO | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.211 IQR)
- **Top Global Matches:** file_cluster_8: 12.211, file_cluster_15: 12.613, file_cluster_13: 12.627
- **Magnitude:** 323.66 | **LOC:** 308 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (63.9848%), Tech Debt (34.653%)
**Top Internal Functions/Classes:**
  * `AutoForwardBranches` (Impact: 55.5 | O(2^N) | DB: 7)
  * `allBranchesMerged` (Impact: 30.1 | O(2^N) | DB: 4)
  * `ConfirmLocalAndRemoteDelete` (Impact: 27.8 | O(N^1) | DB: 9)
  * `ConfirmLocalDelete` (Impact: 27.2 | O(N^1) | DB: 7)
  * `ConfirmDeleteRemote` (Impact: 14.3 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 54`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 110`, `orphaned_logic: 5`
* *Architecture:* `api: 25`, `import: 1`
* *Defense:* `safety: 10`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` lo, gocui, selectedBranchName, remoteBranchName, strings, upstream, git_commands, fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/gui/context.go` (GO | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.654 IQR)
- **Top Global Matches:** file_cluster_13: 13.654, file_cluster_8: 13.655, file_cluster_15: 13.662
- **Magnitude:** 294.24 | **LOC:** 376 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (64.7467%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `currentStaticContextWithoutLock` (Impact: 14.3 | O(N^1) | DB: 3)
    * *Intent:* // if top one is a temporary popup, we remove it. Ideally you'd be able to
  * `NextInStack` (Impact: 13.0 | O(N^1) | DB: 1)
  * `Replace` (Impact: 10.7 | O(N^1) | DB: 3)
    * *Intent:* // use when you don't want to return to the original context upon
  * `ContextForKey` (Impact: 10.4 | O(N^1) | DB: 1)
  * `CurrentSide` (Impact: 9.8 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 32`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 123`, `dead_code: 2`
* *Architecture:* `api: 34`, `import: 1`
* *Defense:* `doc: 2`, `sync_locks: 17`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` lo, sync, utils, types, context
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/config/user_config_validation.go` (GO | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.042 IQR)
- **Top Global Matches:** file_cluster_8: 13.042, file_cluster_11: 13.338, file_cluster_13: 13.338
- **Magnitude:** 291.64 | **LOC:** 168 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (63.4046%), Tech Debt (13.6802%)
**Top Internal Functions/Classes:**
  * `validateCustomCommands` (Impact: 78.0 | O(2^N) | DB: 8)
  * `validateKeybindingsRecurse` (Impact: 64.0 | O(2^N) | DB: 8)
  * `Validate` (Impact: 28.9 | O(N^1) | DB: 10)
  * `validateCustomCommandPrompt` (Impact: 10.5 | O(N^1) | DB: 1)
  * `validateKeybindings` (Impact: 6.6 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 33`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 87`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.674
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` reflect, slices, strings, log, fmt, constants
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `pkg/config/user_config.go` (GO) | Magnitude: 499.92 | Delta: **0.286 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 414, api: 392, doc: 109, decorators: 92

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `pkg/gui/modes/diffing/diffing.go` (GO) | Magnitude: 15.58 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 9, indent_tabs: 6, encapsulation: 3, structural_boundaries: 2
- `pkg/gui/controllers/helpers/cherry_pick_helper.go` (GO) | Magnitude: 86.52 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 66, state_mutation: 38, encapsulation: 25, structural_boundaries: 15
- `pkg/gui/controllers/undo_controller.go` (GO) | Magnitude: 110.52 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 64, indent_tabs: 62, branch: 21, encapsulation: 20
- `pkg/fakes/log.go` (GO) | Magnitude: 56.52 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 21, indent_tabs: 19, api: 6, encapsulation: 6
- `pkg/gui/controllers/helpers/window_helper.go` (GO) | Magnitude: 123.94 | Delta: **0.202 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 60, state_mutation: 45, encapsulation: 18, branch: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pkg/gui/context.go` (GO) | Magnitude: 294.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 139, state_mutation: 123, branch: 44, encapsulation: 37
- `pkg/gui/context/parent_context_mgr.go` (GO) | Magnitude: 11.24 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, api: 4, pointers: 3, indent_tabs: 3
- `pkg/integration/components/test_driver.go` (GO) | Magnitude: 20.2 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 21, pointers: 12, encapsulation: 11, structural_boundaries: 7
- `pkg/commands/git_commands/bisect.go` (GO) | Magnitude: 104.8 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 74, state_mutation: 71, encapsulation: 29, structural_boundaries: 18
- `pkg/integration/components/matcher.go` (GO) | Magnitude: 41.16 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 28, structural_boundaries: 14, encapsulation: 13, state_mutation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `pkg/commands/patch/patch.go` (GO) | Magnitude: 226.1 | Delta: **0.16 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 92, indent_tabs: 87, api: 31, structural_boundaries: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scripts/run_integration_tests.sh` (SHELL) | Magnitude: 1.74 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 10, branch: 7, structural_boundaries: 7, state_mutation: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `pkg/gui/controllers/helpers/repos_helper.go` (GO) | Magnitude: 153.56 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 124, state_mutation: 82, encapsulation: 38, structural_boundaries: 29
- `pkg/commands/oscommands/cmd_obj_runner.go` (GO) | Magnitude: 278.74 | Delta: **0.199 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 189, state_mutation: 128, encapsulation: 64, structural_boundaries: 48
- `pkg/gui/controllers/helpers/fixup_helper.go` (GO) | Magnitude: 366.18 | Delta: **0.318 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 193, state_mutation: 192, branch: 64, encapsulation: 62
- `pkg/gui/test_mode.go` (GO) | Magnitude: 48.98 | Delta: **0.353 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 40, concurrency: 19, state_mutation: 14, encapsulation: 13
- `pkg/gui/background.go` (GO) | Magnitude: 177.0 | Delta: **0.486 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 111, state_mutation: 74, concurrency: 49, encapsulation: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `pkg/gui/menu_panel.go` (GO) | Magnitude: 25.84 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 27, state_mutation: 20, encapsulation: 16, structural_boundaries: 4
- `pkg/app/daemon/rebase.go` (GO) | Magnitude: 28.86 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 29, structural_boundaries: 9, state_mutation: 9, encapsulation: 8
- `pkg/utils/rebase_todo.go` (GO) | Magnitude: 151.44 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 90, state_mutation: 78, planned_debt: 44, structural_boundaries: 29
- `pkg/utils/rebase_todo_test.go` (GO) | Magnitude: 146.4 | Delta: **0.172 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 542, planned_debt: 323, encapsulation: 219, state_mutation: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pkg/utils/slice.go` (GO) | Magnitude: 157.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 80, state_mutation: 64, branch: 28, structural_boundaries: 24
- `pkg/utils/history_buffer.go` (GO) | Magnitude: 36.66 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 22, structural_boundaries: 9, state_mutation: 9, branch: 6
- `pkg/gui/controllers/bisect_controller.go` (GO) | Magnitude: 117.62 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 96, state_mutation: 38, encapsulation: 27, structural_boundaries: 19
- `pkg/commands/git_commands/working_tree.go` (GO) | Magnitude: 360.18 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 200, state_mutation: 144, structural_boundaries: 58, branch: 57
- `pkg/gui/patch_exploring/state.go` (GO) | Magnitude: 435.64 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 235, state_mutation: 186, encapsulation: 82, branch: 60

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `pkg/commands/models/worktree.go` (GO) | Magnitude: 16.54 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: api: 9, indent_tabs: 8, structural_boundaries: 6, args: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pkg/gui/controllers/files_controller.go` -> Churn: **81.0%** | Cog Load: 63.4124% | Debt: 29.1114%
- `pkg/gui/gui.go` -> Churn: **81.0%** | Cog Load: 71.7308% | Debt: 99.4101%
- `pkg/commands/git_commands/working_tree.go` -> Churn: **76.67%** | Cog Load: 45.9497% | Debt: 95.3105%
- `pkg/gui/controllers/local_commits_controller.go` -> Churn: **70.67%** | Cog Load: 37.825% | Debt: 87.9021%
- `pkg/gui/menu_panel.go` -> Churn: **66.13%** | Cog Load: 56.2177% | Debt: 98.9347%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `pkg/gui/controllers/branches_controller.go` -> **Stefan Haller** (100.0% isolated ownership) | Magnitude: 746.96
- `pkg/tasks/tasks.go` -> **Stefan Haller** (100.0% isolated ownership) | Magnitude: 535.3
- `pkg/gui/patch_exploring/state.go` -> **Stefan Haller** (100.0% isolated ownership) | Magnitude: 435.64
- `pkg/integration/clients/tui.go` -> **Stefan Haller** (100.0% isolated ownership) | Magnitude: 419.1
- `pkg/gui/keybindings.go` -> **Stefan Haller** (100.0% isolated ownership) | Magnitude: 355.02

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pkg/utils/utils.go` -> **Severity: 0.123** (Bridge: 0.0012 * Flux: 100.0%)
- `pkg/theme/gocui.go` -> **Severity: 0.082** (Bridge: 0.0008 * Flux: 99.9998%)
- `pkg/commands/oscommands/os.go` -> **Severity: 0.069** (Bridge: 0.0007 * Flux: 100.0%)
- `pkg/theme/style.go` -> **Severity: 0.024** (Bridge: 0.0002 * Flux: 100.0%)
- `pkg/gui/pty.go` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pkg/utils/utils.go` -> **Severity: 13.204** (Embedded: 0.1549 * Error Risk: 85.2652%)
- `pkg/theme/gocui.go` -> **Severity: 11.435** (Embedded: 0.1396 * Error Risk: 81.9112%)
- `pkg/commands/oscommands/os.go` -> **Severity: 10.084** (Embedded: 0.1139 * Error Risk: 88.5092%)
- `pkg/utils/regexp.go` -> **Severity: 9.761** (Embedded: 0.104 * Error Risk: 93.8617%)
- `pkg/utils/io.go` -> **Severity: 6.521** (Embedded: 0.0824 * Error Risk: 79.1391%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pkg/commands/oscommands/os.go` -> **Severity: 6019.2** (Blast Radius: 60.192 * Doc Risk: 100.0%)
- `pkg/gui/services/custom_commands/models.go` -> **Severity: 2786.8** (Blast Radius: 27.868 * Doc Risk: 100.0%)
- `pkg/theme/gocui.go` -> **Severity: 2782.349** (Blast Radius: 78.255 * Doc Risk: 35.5549%)
- `pkg/utils/regexp.go` -> **Severity: 2619.871** (Blast Radius: 30.704 * Doc Risk: 85.3267%)
- `pkg/commands/git_commands/sync.go` -> **Severity: 2277.2** (Blast Radius: 22.772 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
