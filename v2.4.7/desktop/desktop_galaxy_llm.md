# ARCHITECTURAL_BRIEF: desktop
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/desktop` |
| **Timestamp** | `2026-08-07T04:15:00.782948+00:00` |
| **Scan Duration** | `4.1s` |
| **Git Branch** | `development` |
| **Git Commit** | `371bde25d10f8a90663dd26bedd443813a867e8d` |
| **Git Remote** | `https://github.com/desktop/desktop.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 859 malicious artifacts.

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
| Total Artifacts | 2390 |
| Analyzed Artifacts (Scanned) | 1069 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1321 |
| Total LOC | 89991 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 44.7% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4983 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.194 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 13.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.4475 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 95 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 851 | 79020 | 79.6% |
| CSS | 172 | 10341 | 16.1% |
| XML | 22 | 25 | 2.1% |
| JSON | 6 | 260 | 0.6% |
| JAVASCRIPT | 6 | 285 | 0.6% |
| MARKDOWN | 5 | 0 | 0.5% |
| PLAINTEXT | 4 | 1 | 0.4% |
| SHELL | 2 | 49 | 0.2% |
| HTML | 1 | 10 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.035`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 477 | 44.6% |
| file_cluster_8 | 428 | 40.0% |
| file_cluster_4 | 78 | 7.3% |
| file_cluster_2 | 46 | 4.3% |
| file_cluster_16 | 18 | 1.7% |
| file_cluster_17 | 6 | 0.6% |
| file_cluster_0 | 2 | 0.2% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 0.7% |
| Static: Minified & Vendor Opaque Mass | 5 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1321*

**Composition by Extension & Reason:**
- `no_extension`: 943x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 173x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable), 1x Excluded (Saturation: Line 82 exceeds 500 chars)
- `.md`: 90x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 4781 LOC)
- `.png`: 11x Excluded (Explicitly Denied Extension: '.png')
- `.js`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.scss`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 45 exceeds 500 chars)
- `.lock`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.lock')
- `.gyp`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 1954 commas in 624 LOC)
- `.cpp`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 22.8 | 11.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 42.6 | 53.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 14.3 | 2.4 | 80.0 |
| API Exposure | 0.0 | 19.8 | 5.1 | 5.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 24.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 39.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 36.3 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 85.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 6.5 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 78.6 | 3.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 32.4 | 25.9 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 98.0 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `app/src/ui/add-repository/create-repository.tsx` (Hits: 93)
- `app/src/lib/shells/win32.ts` (Hits: 87)
- `app/src/lib/shells/linux.ts` (Hits: 49)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **dialog.tsx** (`app/src/ui/dialog/dialog.tsx`) — 102 inbound connections
2. **dispatcher.ts** (`app/src/ui/dispatcher/dispatcher.ts`) — 99 inbound connections
3. **path.ts** (`app/src/lib/path.ts`) — 93 inbound connections
4. **fatal-error.ts** (`app/src/lib/fatal-error.ts`) — 86 inbound connections
5. **api.ts** (`app/src/lib/api.ts`) — 82 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **app.tsx** (`app/src/ui/app.tsx`) — 153 outbound dependencies
2. **app-store.ts** (`app/src/lib/stores/app-store.ts`) — 115 outbound dependencies
3. **_ui.scss** (`app/styles/_ui.scss`) — 113 outbound dependencies
4. **index.ts** (`app/src/highlighter/index.ts`) — 60 outbound dependencies
5. **dispatcher.ts** (`app/src/ui/dispatcher/dispatcher.ts`) — 60 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `sendNonFatalException` (@ `app/src/ui/app.tsx`) -> Impact: **343.6** | LOC: 1538
- `popupContent` (@ `app/src/ui/app.tsx`) -> Impact: **342.7** | LOC: 1520
- `onUpdateSelection` (@ `app/src/ui/diff/side-by-side-diff.tsx`) -> Impact: **306.0** | LOC: 680
- `setOnOpenBanner` (@ `app/src/ui/app.tsx`) -> Impact: **292.2** | LOC: 648
- `safeDirectoryName` (@ `app/src/ui/add-repository/create-repository.tsx`) -> Impact: **236.9** | LOC: 658
  * *Intent:* // We use this instead of sanitizedRepositoryName because it deals with // valid repository names on GitHub.com but here we only care about whether //...
- `findNextPageSelectableRow` (@ `app/src/ui/lib/list/list.tsx`) -> Impact: **204.4** | LOC: 416
  * *Intent:* /** * Callback to fire when the index path of the position to insert items via * keyboard changes.
- `showTestUI` (@ `app/src/ui/lib/test-ui-components/test-ui-components.ts`) -> Impact: **203.9** | LOC: 456
- `buildMenuItemInfoMap` (@ `app/src/ui/changes/no-changes.tsx`) -> Impact: **163.7** | LOC: 593
  * *Intent:* /** * Whether or not the menu item is currently * enabled.
- `render` (@ `app/src/ui/lib/list/list.tsx`) -> Impact: **154.3** | LOC: 280
- `getAvatarUrlCandidates` (@ `app/src/ui/lib/avatar.tsx`) -> Impact: **153.3** | LOC: 266

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `app` | 8 | 5017.59 | 5.6% | 12.27% |
| `app/src/ui/lib` | 79 | 697.55 | 28.11% | 6.61% |
| `app/src/lib/stores` | 24 | 596.77 | 48.06% | 15.64% |
| `app/src/ui` | 22 | 533.7 | 45.35% | 13.06% |
| `app/src/lib` | 102 | 468.85 | 16.74% | 14.83% |
| `app/src/lib/git` | 57 | 349.99 | 27.41% | 15.98% |
| `app/src/ui/history` | 12 | 266.52 | 43.62% | 13.12% |
| `app/src/ui/diff` | 16 | 252.89 | 25.87% | 3.73% |
| `app/src/ui/dispatcher` | 3 | 220.64 | 28.37% | 2.99% |
| `app/src/ui/preferences` | 11 | 215.91 | 59.98% | 7.24% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `app/src/cli/main.ts` -> **100.0%** Exposure
- `app/src/lib/error-with-metadata.ts` -> **100.0%** Exposure
- `app/src/lib/is-git-on-path.ts` -> **100.0%** Exposure
- `app/src/lib/pick.ts` -> **100.0%** Exposure
- `app/src/lib/stores/base-store.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `app/src/lib/git/push.ts` -> **100.0%** Exposure
- `app/src/lib/mouse-scroller.ts` -> **100.0%** Exposure
- `app/src/lib/popup-manager.ts` -> **100.0%** Exposure
- `app/src/lib/split-buffer.ts` -> **100.0%** Exposure
- `app/src/lib/tailer.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `app/src/lib/editors/win32.ts` -> **0** Orphaned Functions | **14** Duplicates
- `app/src/ui/history/commit-list.tsx` -> **0** Orphaned Functions | **14** Duplicates
- `app/src/lib/actions-log-parser/action-log-parser.ts` -> **8** Orphaned Functions | **4** Duplicates
- `app/src/main-process/ordered-webrequest.ts` -> **0** Orphaned Functions | **9** Duplicates
- `app/src/lib/error-with-metadata.ts` -> **0** Orphaned Functions | **8** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`app/src/highlighter/index.ts`** -> AI Confidence: **99.48%**
2. **`app/src/main-process/menu/build-default-menu.ts`** -> AI Confidence: **99.39%**
3. **`app/src/ui/lib/list/list.tsx`** -> AI Confidence: **99.35%**
4. **`app/src/cli/main.ts`** -> AI Confidence: **99.32%**
5. **`app/src/lib/git/commit.ts`** -> AI Confidence: **99.31%**
6. **`app/src/lib/git/core.ts`** -> AI Confidence: **99.31%**
7. **`app/src/lib/git/log.ts`** -> AI Confidence: **99.31%**
8. **`app/src/lib/git/pull.ts`** -> AI Confidence: **99.31%**
9. **`app/src/lib/git/push.ts`** -> AI Confidence: **99.31%**
10. **`app/src/lib/git/reorder.ts`** -> AI Confidence: **99.31%**
11. **`app/src/lib/git/squash.ts`** -> AI Confidence: **99.31%**
12. **`app/src/lib/helpers/repo-rules.ts`** -> AI Confidence: **99.31%**
13. **`app/src/lib/menu-update.ts`** -> AI Confidence: **99.31%**
14. **`app/src/lib/shells/shared.ts`** -> AI Confidence: **99.31%**
15. **`app/src/lib/shells/win32.ts`** -> AI Confidence: **99.31%**
16. **`app/src/lib/stores/updates/changes-state.ts`** -> AI Confidence: **99.31%**
17. **`app/src/ui/about/about.tsx`** -> AI Confidence: **99.31%**
18. **`app/src/ui/add-repository/create-repository.tsx`** -> AI Confidence: **99.31%**
19. **`app/src/ui/app-menu/menu-list-item.tsx`** -> AI Confidence: **99.31%**
20. **`app/src/ui/autocompletion/autocompleting-text-input.tsx`** -> AI Confidence: **99.31%**
21. **`app/src/ui/changes/commit-message-avatar.tsx`** -> AI Confidence: **99.31%**
22. **`app/src/ui/check-runs/ci-check-run-popover.tsx`** -> AI Confidence: **99.31%**
23. **`app/src/ui/diff/seamless-diff-switcher.tsx`** -> AI Confidence: **99.31%**
24. **`app/src/ui/diff/side-by-side-diff.tsx`** -> AI Confidence: **99.31%**
25. **`app/src/ui/dispatcher/error-handlers.ts`** -> AI Confidence: **99.31%**
26. **`app/src/ui/drag-elements/commit-drag-element.tsx`** -> AI Confidence: **99.31%**
27. **`app/src/ui/dropdown-select-button.tsx`** -> AI Confidence: **99.31%**
28. **`app/src/ui/history/commit-list.tsx`** -> AI Confidence: **99.31%**
29. **`app/src/ui/history/compare-branch-list-item.tsx`** -> AI Confidence: **99.31%**
30. **`app/src/ui/lib/augmented-filter-list.tsx`** -> AI Confidence: **99.31%**
31. **`app/src/ui/lib/avatar.tsx`** -> AI Confidence: **99.31%**
32. **`app/src/ui/lib/configure-git-user.tsx`** -> AI Confidence: **99.31%**
33. **`app/src/ui/lib/filter-list.tsx`** -> AI Confidence: **99.31%**
34. **`app/src/ui/lib/path-text.tsx`** -> AI Confidence: **99.31%**
35. **`app/src/ui/lib/popover.tsx`** -> AI Confidence: **99.31%**
36. **`app/src/ui/lib/rich-text.tsx`** -> AI Confidence: **99.31%**
37. **`app/src/ui/lib/sandboxed-markdown.tsx`** -> AI Confidence: **99.31%**
38. **`app/src/ui/lib/section-filter-list.tsx`** -> AI Confidence: **99.31%**
39. **`app/src/ui/lib/text-box.tsx`** -> AI Confidence: **99.31%**
40. **`app/src/ui/lib/tooltip.tsx`** -> AI Confidence: **99.31%**
41. **`app/src/ui/preferences/integrations.tsx`** -> AI Confidence: **99.31%**
42. **`app/src/ui/publish-repository/publish.tsx`** -> AI Confidence: **99.31%**
43. **`app/src/ui/repositories-list/group-repositories.ts`** -> AI Confidence: **99.31%**
44. **`app/src/ui/repositories-list/repository-list-item.tsx`** -> AI Confidence: **99.31%**
45. **`app/src/ui/sign-in/sign-in.tsx`** -> AI Confidence: **99.31%**
46. **`app/src/ui/toolbar/button.tsx`** -> AI Confidence: **99.31%**
47. **`app/src/ui/toolbar/dropdown.tsx`** -> AI Confidence: **99.31%**
48. **`app/src/ui/window/title-bar.tsx`** -> AI Confidence: **99.31%**
49. **`script/build.ts`** -> AI Confidence: **99.31%**
50. **`script/draft-release/run.ts`** -> AI Confidence: **99.31%**
51. **`app/src/lib/actions-log-parser/actions-logs-ansii.ts`** -> AI Confidence: **99.29%**
52. **`app/src/lib/create-terminal-stream.ts`** -> AI Confidence: **99.29%**
53. **`app/src/ui/lib/parse-files-to-be-overwritten.ts`** -> AI Confidence: **99.29%**
54. **`eslint-rules/insecure-random.js`** -> AI Confidence: **99.29%**
55. **`script/draft-release/release-pr-content.sh`** -> AI Confidence: **99.29%**
56. **`app/src/lib/api.ts`** -> AI Confidence: **99.24%**
57. **`app/src/lib/git/cherry-pick.ts`** -> AI Confidence: **99.24%**
58. **`app/src/lib/git/rebase.ts`** -> AI Confidence: **99.24%**
59. **`app/src/lib/git/status.ts`** -> AI Confidence: **99.24%**
60. **`app/src/lib/hooks/with-hooks-env.ts`** -> AI Confidence: **99.24%**
61. **`app/src/lib/stores/notifications-debug-store.ts`** -> AI Confidence: **99.24%**
62. **`app/src/lib/stores/repositories-store.ts`** -> AI Confidence: **99.24%**
63. **`app/src/ui/add-repository/add-existing-repository.tsx`** -> AI Confidence: **99.24%**
64. **`app/src/ui/app-error.tsx`** -> AI Confidence: **99.24%**
65. **`app/src/ui/app.tsx`** -> AI Confidence: **99.24%**
66. **`app/src/ui/branches/branch-list.tsx`** -> AI Confidence: **99.24%**
67. **`app/src/ui/branches/push-branch-commits.tsx`** -> AI Confidence: **99.24%**
68. **`app/src/ui/changes/no-changes.tsx`** -> AI Confidence: **99.24%**
69. **`app/src/ui/check-runs/ci-check-run-rerun-dialog.tsx`** -> AI Confidence: **99.24%**
70. **`app/src/ui/create-branch/create-branch-dialog.tsx`** -> AI Confidence: **99.24%**
71. **`app/src/ui/diff/side-by-side-diff-row.tsx`** -> AI Confidence: **99.24%**
72. **`app/src/ui/diff/submodule-diff.tsx`** -> AI Confidence: **99.24%**
73. **`app/src/ui/history/merge-call-to-action-with-conflicts.tsx`** -> AI Confidence: **99.24%**
74. **`app/src/ui/lib/conflicts/unmerged-file.tsx`** -> AI Confidence: **99.24%**
75. **`app/src/ui/lib/git-email-not-found-warning.tsx`** -> AI Confidence: **99.24%**
76. **`app/src/ui/lib/popover-dropdown.tsx`** -> AI Confidence: **99.24%**
77. **`app/src/ui/lib/test-ui-components/test-ui-components.ts`** -> AI Confidence: **99.24%**
78. **`app/src/ui/multi-commit-operation/choose-branch/base-choose-branch-dialog.tsx`** -> AI Confidence: **99.24%**
79. **`app/src/ui/multi-commit-operation/choose-branch/choose-target-branch.tsx`** -> AI Confidence: **99.24%**
80. **`app/src/ui/open-pull-request/open-pull-request-dialog.tsx`** -> AI Confidence: **99.24%**
81. **`app/src/ui/preferences/git.tsx`** -> AI Confidence: **99.24%**
82. **`app/src/ui/preferences/preferences.tsx`** -> AI Confidence: **99.24%**
83. **`app/src/ui/repositories-list/repositories-list.tsx`** -> AI Confidence: **99.24%**
84. **`app/src/ui/repository-settings/repository-settings.tsx`** -> AI Confidence: **99.24%**
85. **`app/src/ui/toolbar/push-pull-button.tsx`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `app/src/ui/diff/diff-helpers.tsx` -> **98.0093%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1072` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `app/src/main-process/ordered-webrequest.ts` (TYPESCRIPT) -> Cumulative Risk: **732.64**
- **Archetype:** `file_cluster_4` (Distance: 12.832 IQR)
- **Magnitude:** 18.75 | **LOC:** 249 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `constructor` (Impact: 20.1), `async` (Impact: 9.5), `async` (Impact: 9.4)

### 2. `app/src/lib/trampoline/trampoline-ui-helper.ts` (TYPESCRIPT) -> Cumulative Risk: **678.98**
- **Archetype:** `file_cluster_4` (Distance: 11.123 IQR)
- **Magnitude:** 14.09 | **LOC:** 108 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (99.9979%), Tech Debt (99.9673%)
- **Heaviest Functions:** `promptForGitHubSignIn` (Impact: 13.2), `resolve` (Impact: 5.9), `promptForGenericGitAuthentication` (Impact: 4.2)

### 3. `app/src/main-process/app-window.ts` (TYPESCRIPT) -> Cumulative Risk: **677.92**
- **Archetype:** `file_cluster_13` (Distance: 12.537 IQR)
- **Magnitude:** 34.62 | **LOC:** 515 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Concurrency (99.8887%)
- **Heaviest Functions:** `constructor` (Impact: 50.2), `show` (Impact: 21.9), `trySetUpdaterGuid` (Impact: 8.7)

### 4. `app/src/ui/app.tsx` (TYPESCRIPT) -> Cumulative Risk: **675.95**
- **Archetype:** `file_cluster_13` (Distance: 13.833 IQR)
- **Magnitude:** 299.2 | **LOC:** 3761 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (93.3838%)
- **Heaviest Functions:** `sendNonFatalException` (Impact: 343.6), `popupContent` (Impact: 342.7), `setOnOpenBanner` (Impact: 292.2)

### 5. `app/src/ui/preferences/appearance.tsx` (TYPESCRIPT) -> Cumulative Risk: **657.2**
- **Archetype:** `file_cluster_13` (Distance: 11.453 IQR)
- **Magnitude:** 13.72 | **LOC:** 178 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.8713%), Verification (80.0%)
- **Heaviest Functions:** `renderThemeSwatch` (Impact: 11.7), `componentDidUpdate` (Impact: 9.8), `constructor` (Impact: 8.8)

### 6. `app/src/lib/stores/app-store.ts` (TYPESCRIPT) -> Cumulative Risk: **653.22**
- **Archetype:** `file_cluster_4` (Distance: 13.356 IQR)
- **Magnitude:** 180.97 | **LOC:** 8730 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 48.5%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (89.2993%), State Flux (84.97%)
- **Heaviest Functions:** `performPull` (Impact: 146.1), `_finishConflictedMerge` (Impact: 94.0), `emitUpdate` (Impact: 32.0)

### 7. `app/src/lib/git/push.ts` (TYPESCRIPT) -> Cumulative Risk: **651.22**
- **Archetype:** `file_cluster_4` (Distance: 12.898 IQR)
- **Magnitude:** 14.38 | **LOC:** 120 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (89.7789%)
- **Heaviest Functions:** `push` (Impact: 48.9), `progressCallback` (Impact: 1.4), `progressCallback` (Impact: 1.4)

### 8. `app/src/ui/open-with-external-editor/open-with-external-editor.tsx` (TYPESCRIPT) -> Cumulative Risk: **649.5**
- **Archetype:** `file_cluster_13` (Distance: 12.7 IQR)
- **Magnitude:** 18.66 | **LOC:** 178 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (93.0572%)
- **Heaviest Functions:** `renderEditorSelect` (Impact: 11.8), `render` (Impact: 10.0), `renderCustomEditor` (Impact: 9.5)

### 9. `app/src/ui/preferences/preferences.tsx` (TYPESCRIPT) -> Cumulative Risk: **638.05**
- **Archetype:** `file_cluster_2` (Distance: 13.441 IQR)
- **Magnitude:** 93.71 | **LOC:** 919 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (95.4244%)
- **Heaviest Functions:** `renderActiveTab` (Impact: 54.3), `onSave` (Impact: 50.8), `getTabId` (Impact: 39.6)

### 10. `app/src/ui/rename-branch/rename-branch-dialog.tsx` (TYPESCRIPT) -> Cumulative Risk: **631.38**
- **Archetype:** `file_cluster_13` (Distance: 12.908 IQR)
- **Magnitude:** 17.15 | **LOC:** 151 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (99.2899%)
- **Heaviest Functions:** `checkBranchRules` (Impact: 13.2), `render` (Impact: 10.6), `onNameChange` (Impact: 6.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `app/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.448
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/ui/app.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.833 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.747 IQR)
- **Top Global Matches:** file_cluster_13: 13.833, file_cluster_2: 13.94, file_cluster_17: 14.2
- **Magnitude:** 299.2 | **LOC:** 3761 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (89.7372%), Tech Debt (23.1547%)
**Top Internal Functions/Classes:**
  * `sendNonFatalException` (Impact: 343.6)
  * `popupContent` (Impact: 342.7)
  * `setOnOpenBanner` (Impact: 292.2)
  * `onMacOSWindowKeyDown` (Impact: 38.7)
  * `renderRepositoryToolbarButton` (Impact: 30.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 347`, `structural_boundaries: 493`, `args: 123`, `func_start: 119`, `class_start: 1`
* *Risk/State:* `state_mutation: 1142`, `dead_code: 3`, `planned_debt: 3`, `duplicate_logic: 8`
* *Architecture:* `io: 19`, `api: 18`, `concurrency: 145`, `import: 154`
* *Defense:* `safety: 18`, `doc: 15`, `immutability_locks: 161`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.495
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002809
  * `Imports (Out-Degree: 97):` drag-and-drop-manager, menu-item, saml-reauth-required, cloning-repository, tutorial, confirm-discard-stash, create-fork-dialog, drag-drop...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/ui/dispatcher/dispatcher.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.404 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.053 IQR)
- **Top Global Matches:** file_cluster_4: 13.404, file_cluster_13: 13.713, file_cluster_8: 14.028
- **Magnitude:** 186.82 | **LOC:** 4083 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (49.9946%), Tech Debt (8.9693%)
**Top Internal Functions/Classes:**
  * `getMultiCommitOperationSuccessBanner` (Impact: 32.3)
  * `processMultiCommitOperationRebaseResult` (Impact: 31.7)
  * `squash` (Impact: 23.4)
  * `reorderCommits` (Impact: 21.9)
    * *Intent:* /** * Ask the dispatcher to apply a transformation function to the current * state of the applicatio...
  * `onConflictsFoundBanner` (Impact: 18.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 240`, `args: 146`, `func_start: 141`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 381`, `dead_code: 2`, `planned_debt: 5`
* *Architecture:* `io: 20`, `api: 242`, `concurrency: 674`, `import: 60`
* *Defense:* `safety: 64`, `doc: 125`, `immutability_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.851
  * `Choke Point (Betweenness):` 0.05552 | `Ripple Effect (Closeness):` 0.068399
  * `Imports (Out-Degree: 38):` main-process-proxy, account, commit-message, app-menu, repository-state-cache, generic-git-auth, shells, unreachable-commits-dialog...
  * `Imported By (In-Degree: 99):` (Excluded from Brief to save tokens)

### `app/src/lib/stores/app-store.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.356 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.898 IQR)
- **Top Global Matches:** file_cluster_4: 13.356, file_cluster_13: 13.449, file_cluster_8: 13.82
- **Magnitude:** 180.97 | **LOC:** 8730 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 48.5%
- **Risk Profile:** Cognitive Load (89.2993%), Tech Debt (10.3116%)
**Top Internal Functions/Classes:**
  * `performPull` (Impact: 146.1)
  * `_finishConflictedMerge` (Impact: 94.0)
    * *Intent:* /** This shouldn't be called directly. See `Dispatcher`. */
  * `emitUpdate` (Impact: 32.0)
    * *Intent:* // One is the default value, we only care about checking the locally stored
  * `_addAccount` (Impact: 26.4)
  * `_executeCompare` (Impact: 24.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 303`, `args: 118`, `func_start: 75`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 460`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 6`, `api: 92`, `concurrency: 498`, `import: 116`
* *Defense:* `safety: 39`, `doc: 33`, `immutability_locks: 152`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.727
  * `Choke Point (Betweenness):` 0.03579 | `Ripple Effect (Closeness):` 0.059862
  * `Imports (Out-Degree: 80):` account, git-error-context, local-storage, stash, tip, menu-update, default-dir, workflow-preferences...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/ui/lib/list/list.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.627 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.22 IQR)
- **Top Global Matches:** file_cluster_2: 13.627, file_cluster_13: 13.657, file_cluster_17: 13.865
- **Magnitude:** 106.37 | **LOC:** 1758 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (52.2625%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `findNextPageSelectableRow` (Impact: 204.4)
    * *Intent:* /** * Callback to fire when the index path of the position to insert items via * keyboard changes.
  * `render` (Impact: 154.3)
  * `onRowMouseDown` (Impact: 61.8)
  * `onRowMouseUp` (Impact: 28.0)
    * *Intent:* // There is no -1 here because you can insert _after_ the last row
  * `onRef` (Impact: 25.7)
    * *Intent:* /** * A handler called whenever the user drops items on the list to be inserted. * * @param row - Th...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 69`, `args: 36`, `func_start: 27`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 432`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 12`, `concurrency: 6`, `import: 15`
* *Defense:* `safety: 12`, `doc: 34`, `immutability_locks: 75`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.152
  * `Choke Point (Betweenness):` 0.003652 | `Ripple Effect (Closeness):` 0.060385
  * `Imports (Out-Degree: 10):` range, memoize-one, react-dom, react-virtualized, id-pool, equality, list-row-index-path, react...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `app/src/ui/diff/side-by-side-diff.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.756 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.86 IQR)
- **Top Global Matches:** file_cluster_13: 12.756, file_cluster_2: 12.982, file_cluster_8: 13.086
- **Magnitude:** 100.67 | **LOC:** 2151 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (53.653%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onUpdateSelection` (Impact: 306.0)
  * `getDiffRowsFromHunk` (Impact: 39.4)
  * `getModifiedRows` (Impact: 31.2)
  * `getDiscardLabel` (Impact: 23.5)
    * *Intent:* // Check to see if there's at least a partial selection within the // diff container. If there isn't...
  * `calcSearchTokens` (Impact: 19.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 129`, `args: 49`, `func_start: 55`, `class_start: 4`
* *Risk/State:* `state_mutation: 315`
* *Architecture:* `api: 19`, `import: 22`
* *Defense:* `safety: 18`, `doc: 29`, `immutability_locks: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.529
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001873
  * `Imports (Out-Degree: 11):` diff-contents-warning, escapeRegExp, aria-live-container, types, diff-helpers, classnames, fatal-error, side-by-side-diff-row...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `app/src/ui/preferences/preferences.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.441 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.305 IQR)
- **Top Global Matches:** file_cluster_2: 13.441, file_cluster_13: 13.513, file_cluster_4: 13.591
- **Magnitude:** 93.71 | **LOC:** 919 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (95.4244%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderActiveTab` (Impact: 54.3)
  * `onSave` (Impact: 50.8)
  * `getTabId` (Impact: 39.6)
  * `componentWillMount` (Impact: 39.4)
  * `getAvailableShells` (Impact: 14.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 116`, `args: 58`, `func_start: 76`, `class_start: 3`
* *Risk/State:* `state_mutation: 444`
* *Architecture:* `io: 2`, `api: 10`, `concurrency: 125`, `import: 31`
* *Defense:* `safety: 15`, `doc: 3`, `sync_locks: 1`, `immutability_locks: 94`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.448
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` account, accounts, shells, identifier-rules, config-lock-file-exists, preferences, integrations, accessibility...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/ui/history/commit-list.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.797 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.275 IQR)
- **Top Global Matches:** file_cluster_13: 13.797, file_cluster_2: 13.803, file_cluster_17: 13.814
- **Magnitude:** 87.09 | **LOC:** 1046 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (34.6556%), Tech Debt (85.0995%)
**Top Internal Functions/Classes:**
  * `getContextMenuForSingleCommit` (Impact: 67.7)
  * `onDropDataInsertion` (Impact: 24.6)
  * `renderRowFocusTooltip` (Impact: 17.9)
  * `render` (Impact: 17.4)
  * `renderKeyboardInsertionElement` (Impact: 16.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 161`, `args: 90`, `func_start: 57`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 449`, `duplicate_logic: 14`
* *Architecture:* `io: 1`, `api: 8`, `import: 27`
* *Defense:* `safety: 47`, `doc: 41`, `immutability_locks: 116`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.704
  * `Choke Point (Betweenness):` 0.014545 | `Ripple Effect (Closeness):` 0.063674
  * `Imports (Out-Degree: 16):` account, aria-live-container, popover, drag-drop, menu-item, commit, commit-list-item, classnames...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/lib/api.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.325 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.945 IQR)
- **Top Global Matches:** file_cluster_4: 12.325, file_cluster_13: 12.7, file_cluster_17: 12.861
- **Magnitude:** 81.35 | **LOC:** 2486 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 88.9%
- **Risk Profile:** Cognitive Load (47.839%), Tech Debt (86.1917%)
**Top Internal Functions/Classes:**
  * `fetchAllRepoRulesets` (Impact: 141.7)
  * `isGitHubHost` (Impact: 28.9)
  * `callback` (Impact: 19.3)
  * `fetchMentionables` (Impact: 17.9)
  * `getNextPagePathWithIncreasingPageSize` (Impact: 17.3)
    * *Intent:* /** * Information about a commit as returned by the GitHub API. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 152`, `args: 47`, `func_start: 42`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 82`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `io: 20`, `api: 51`, `concurrency: 242`, `import: 11`
* *Defense:* `safety: 44`, `doc: 73`, `immutability_locks: 123`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.122
  * `Choke Point (Betweenness):` 0.023597 | `Ripple Effect (Closeness):` 0.142782
  * `Imports (Out-Degree: 9):` http-status-code, copilot-commit-message, endpoint-capabilities, url, http, account, suppress-certificate-error, copilot-error...
  * `Imported By (In-Degree: 82):` (Excluded from Brief to save tokens)

### `app/src/ui/add-repository/create-repository.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.877 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.872 IQR)
- **Top Global Matches:** file_cluster_4: 13.877, file_cluster_13: 13.931, file_cluster_17: 13.97
- **Magnitude:** 79.99 | **LOC:** 783 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (73.3063%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `safeDirectoryName` (Impact: 236.9)
    * *Intent:* // We use this instead of sanitizedRepositoryName because it deals with // valid repository names on...
  * `onWindowFocus` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 126`, `args: 45`, `func_start: 35`, `class_start: 3`
* *Risk/State:* `state_mutation: 386`, `dead_code: 1`
* *Architecture:* `io: 93`, `api: 6`, `concurrency: 156`, `import: 32`
* *Defense:* `safety: 35`, `doc: 16`, `immutability_locks: 66`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000936
  * `Imports (Out-Degree: 26):` main-process-proxy, input-warning, row, description, gitignores, promises, feature-flag, ref...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/src/ui/lib/augmented-filter-list.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.447 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.456 IQR)
- **Top Global Matches:** file_cluster_17: 13.447, file_cluster_2: 13.49, file_cluster_13: 13.633
- **Magnitude:** 73.99 | **LOC:** 926 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.1078%), Tech Debt (20.9774%)
**Top Internal Functions/Classes:**
  * `onKeyDown` (Impact: 37.9)
  * `createStateUpdate` (Impact: 29.1)
  * `onRowKeyDown` (Impact: 27.4)
  * `selectNextItem` (Impact: 18.0)
  * `componentDidUpdate` (Impact: 14.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 134`, `args: 78`, `func_start: 37`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 406`, `duplicate_logic: 3`
* *Architecture:* `io: 1`, `api: 20`, `import: 12`
* *Defense:* `safety: 16`, `doc: 37`, `immutability_locks: 100`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002341
  * `Imports (Out-Degree: 8):` text-box, list-row-index-path, xor, aria-live-container, react, classnames, section-list-selection, section-list...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/src/ui/autocompletion/autocompleting-text-input.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.286 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.373 IQR)
- **Top Global Matches:** file_cluster_2: 13.286, file_cluster_13: 13.394, file_cluster_17: 13.57
- **Magnitude:** 66.06 | **LOC:** 794 | **CtrlFlow:** 56.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.8791%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onKeyDown` (Impact: 35.0)
  * `render` (Impact: 19.2)
  * `attemptAutocompletion` (Impact: 13.9)
  * `renderAutocompletions` (Impact: 13.6)
  * `insertCompletion` (Impact: 12.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 87`, `args: 47`, `func_start: 43`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 332`
* *Architecture:* `api: 13`, `concurrency: 37`, `import: 10`
* *Defense:* `safety: 24`, `doc: 29`, `immutability_locks: 102`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.893
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001248
  * `Imports (Out-Degree: 6):` list, id-pool, index, textarea-caret, react, aria-live-container, classnames, popover...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/src/ui/lib/section-filter-list.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.333 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.229 IQR)
- **Top Global Matches:** file_cluster_2: 13.333, file_cluster_13: 13.473, file_cluster_17: 13.501
- **Magnitude:** 65.18 | **LOC:** 788 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (34.729%), Tech Debt (24.0736%)
**Top Internal Functions/Classes:**
  * `onKeyDown` (Impact: 37.9)
  * `createStateUpdate` (Impact: 23.4)
  * `onRowKeyDown` (Impact: 21.7)
  * `selectNextItem` (Impact: 15.9)
  * `componentDidUpdate` (Impact: 14.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 104`, `args: 59`, `func_start: 34`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 358`, `duplicate_logic: 3`
* *Architecture:* `io: 1`, `api: 19`, `import: 11`
* *Defense:* `safety: 12`, `doc: 31`, `immutability_locks: 80`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.724
  * `Choke Point (Betweenness):` 7.8e-05 | `Ripple Effect (Closeness):` 0.009346
  * `Imports (Out-Degree: 8):` text-box, list-row-index-path, aria-live-container, react, classnames, section-list-selection, section-list, filter-list...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `app/src/ui/history/compare.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.979 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.102 IQR)
- **Top Global Matches:** file_cluster_13: 12.979, file_cluster_2: 12.989, file_cluster_17: 13.13
- **Magnitude:** 63.55 | **LOC:** 753 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.8358%), Tech Debt (15.0038%)
**Top Internal Functions/Classes:**
  * `onBranchFilterKeyDown` (Impact: 36.3)
  * `renderCommitList` (Impact: 15.8)
  * `getPlaceholderText` (Impact: 14.7)
  * `componentWillReceiveProps` (Impact: 13.4)
  * `componentDidUpdate` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 107`, `args: 61`, `func_start: 61`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 317`, `duplicate_logic: 2`
* *Architecture:* `api: 17`, `concurrency: 37`, `import: 28`
* *Defense:* `safety: 17`, `doc: 3`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.448
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` fancy-text-box, unique-coauthors-as-authors, account, merge-call-to-action-with-conflicts, filter-list, throttled-scheduler, drag-drop, ref...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/lib/stores/git-store.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.077 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.144 IQR)
- **Top Global Matches:** file_cluster_4: 13.077, file_cluster_13: 13.253, file_cluster_8: 13.743
- **Magnitude:** 62.89 | **LOC:** 1775 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (57.4649%), Tech Debt (39.5934%)
**Top Internal Functions/Classes:**
  * `mergeRemoteAndLocalBranches` (Impact: 28.8)
  * `undoFirstCommit` (Impact: 28.0)
  * `emitUpdatesForChangedTags` (Impact: 19.5)
    * *Intent:* /** The store for a repository's git data. */
  * `loadLocalCommits` (Impact: 16.3)
  * `getCompareCommits` (Impact: 12.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 94`, `args: 37`, `func_start: 26`
* *Risk/State:* `state_mutation: 201`, `duplicate_logic: 3`
* *Architecture:* `io: 3`, `api: 28`, `concurrency: 208`, `import: 34`
* *Defense:* `doc: 19`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.795
  * `Choke Point (Betweenness):` 0.003891 | `Ripple Effect (Closeness):` 0.047953
  * `Imports (Out-Degree: 21):` commit-message, remote, base-store, fatal-error, find-default-remote, stats, stash, tip...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/ui/changes/no-changes.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.607 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.699 IQR)
- **Top Global Matches:** file_cluster_13: 11.607, file_cluster_2: 11.749, file_cluster_8: 11.794
- **Magnitude:** 58.03 | **LOC:** 783 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (57.498%), Tech Debt (16.1745%)
**Top Internal Functions/Classes:**
  * `buildMenuItemInfoMap` (Impact: 163.7)
    * *Intent:* /** * Whether or not the menu item is currently * enabled.
  * `renderRemoteAction` (Impact: 28.5)
  * `renderPushBranchAction` (Impact: 23.4)
  * `renderPullBranchAction` (Impact: 18.6)
  * `renderViewStashAction` (Impact: 16.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 99`, `args: 40`, `func_start: 37`, `class_start: 3`
* *Risk/State:* `state_mutation: 160`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 7`, `concurrency: 6`, `import: 24`
* *Defense:* `safety: 6`, `doc: 11`, `immutability_locks: 64`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001248
  * `Imports (Out-Degree: 12):` app-menu, remote, dropdown-suggested-action, preferences, tip, path, stash-entry, ref...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/src/lib/stores/repositories-store.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.766 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.11 IQR)
- **Top Global Matches:** file_cluster_4: 12.766, file_cluster_13: 13.303, file_cluster_11: 13.652
- **Magnitude:** 55.97 | **LOC:** 742 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.4997%), Tech Debt (32.7252%)
**Top Internal Functions/Classes:**
  * `_upsertGitHubRepository` (Impact: 37.4)
  * `putOwner` (Impact: 25.8)
  * `getLastStashCheckDate` (Impact: 19.7)
  * `updateBranchProtections` (Impact: 15.2)
  * `upsertGitHubRepositoryFromMatch` (Impact: 7.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 64`, `args: 21`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 116`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 22`, `concurrency: 274`, `import: 12`
* *Defense:* `safety: 15`, `doc: 19`, `immutability_locks: 28`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.728
  * `Choke Point (Betweenness):` 0.001923 | `Ripple Effect (Closeness):` 0.055182
  * `Imports (Out-Degree: 10):` owner, repositories-database, base-store, fatal-error, api, tags-to-push-storage, repository, equality...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `eslint-rules/react-proper-lifecycle-methods.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.787 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.267 IQR)
- **Top Global Matches:** file_cluster_8: 11.787, file_cluster_7: 11.949, file_cluster_6: 12.038
- **Magnitude:** 55.84 | **LOC:** 368 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1128%), Tech Debt (99.7808%)
**Top Internal Functions/Classes:**
  * `getPropsType` (Impact: 24.4)
    * *Intent:* // @ts-check /** * react-proper-lifecycle-methods * * This custom eslint rule is attempts to prevent...
  * `create` (Impact: 9.8)
    * *Intent:* /**
  * `verifyParameter` (Impact: 7.8)
  * `getParameterName` (Impact: 3.9)
  * `verifyParameters` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 8`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 1`
* *Defense:* `safety: 7`, `doc: 27`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.448
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` experimental-utils, typescript-estree
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/ui/lib/filter-list.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.247 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.262 IQR)
- **Top Global Matches:** file_cluster_2: 13.247, file_cluster_13: 13.457, file_cluster_17: 13.568
- **Magnitude:** 55.58 | **LOC:** 678 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.5906%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onKeyDown` (Impact: 37.5)
  * `createStateUpdate` (Impact: 22.9)
  * `onRowKeyDown` (Impact: 17.4)
  * `selectNextItem` (Impact: 15.9)
  * `componentDidUpdate` (Impact: 14.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 88`, `args: 44`, `func_start: 25`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 316`
* *Architecture:* `api: 22`, `import: 7`
* *Defense:* `safety: 7`, `doc: 35`, `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 6.7e-05 | `Ripple Effect (Closeness):` 0.016854
  * `Imports (Out-Degree: 5):` text-box, list, aria-live-container, react, classnames, row, fuzzy-find
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `app/src/ui/diff/side-by-side-diff-row.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.419 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.321 IQR)
- **Top Global Matches:** file_cluster_2: 12.419, file_cluster_13: 12.543, file_cluster_8: 12.617
- **Magnitude:** 55.18 | **LOC:** 1052 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (30.6958%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderHunkHandle` (Impact: 27.2)
  * `renderLineNumbers` (Impact: 27.2)
  * `render` (Impact: 26.9)
  * `getDiffColumn` (Impact: 16.8)
  * `getDiffData` (Impact: 16.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 115`, `args: 46`, `func_start: 35`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 278`
* *Architecture:* `api: 11`, `import: 13`
* *Defense:* `safety: 21`, `doc: 43`, `immutability_locks: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.488
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001685
  * `Imports (Out-Degree: 6):` diff, diff-helpers, react, classnames, diff, octicons, octicons.generated, popover...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/src/ui/test-notifications/test-notifications.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.237 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.805 IQR)
- **Top Global Matches:** file_cluster_2: 12.237, file_cluster_13: 12.274, file_cluster_8: 12.348
- **Magnitude:** 53.44 | **LOC:** 801 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (89.6778%), Tech Debt (14.2854%)
**Top Internal Functions/Classes:**
  * `prepareForNextStep` (Impact: 30.3)
  * `doFinalAction` (Impact: 28.9)
  * `getTypeFriendlyName` (Impact: 18.8)
  * `renderCurrentStep` (Impact: 15.7)
  * `renderNotificationHint` (Impact: 13.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 123`, `args: 46`, `func_start: 35`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 268`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 8`, `concurrency: 24`, `import: 20`
* *Defense:* `safety: 9`, `immutability_locks: 69`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.452
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00214
  * `Imports (Out-Degree: 12):` section-list, loading, classnames, repository, fatal-error, pull-request-review-helpers, list-row-index-path, valid-notification-pull-request-review...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/src/ui/repository.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.803 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.111 IQR)
- **Top Global Matches:** file_cluster_2: 12.803, file_cluster_13: 12.851, file_cluster_8: 13.205
- **Magnitude:** 53.32 | **LOC:** 754 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (67.6958%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderChangesSidebar` (Impact: 19.7)
  * `renderContentForChanges` (Impact: 18.8)
  * `onGlobalKeyDown` (Impact: 12.8)
  * `renderCompareSidebar` (Impact: 9.6)
  * `renderSidebarContents` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 89`, `args: 41`, `func_start: 42`, `class_start: 3`
* *Risk/State:* `state_mutation: 315`
* *Architecture:* `api: 18`, `import: 32`
* *Defense:* `safety: 8`, `doc: 11`, `immutability_locks: 69`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.453
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000936
  * `Imports (Out-Degree: 23):` drag-and-drop-manager, multiple-selection, tip, files-changed-badge, tutorial, stores, drag-drop, app-menu...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/src/ui/lib/avatar.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.093 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.413 IQR)
- **Top Global Matches:** file_cluster_13: 13.093, file_cluster_17: 13.137, file_cluster_2: 13.335
- **Magnitude:** 47.18 | **LOC:** 547 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (86.1785%), Tech Debt (28.5422%)
**Top Internal Functions/Classes:**
  * `getAvatarUrlCandidates` (Impact: 153.3)
  * `onImageRef` (Impact: 33.7)
  * `resolveBotAvatar` (Impact: 20.2)
  * `renderAvatar` (Impact: 19.0)
  * `getTitle` (Impact: 15.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 61`, `args: 34`, `func_start: 20`
* *Risk/State:* `state_mutation: 138`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 13`, `concurrency: 4`, `import: 14`
* *Defense:* `safety: 26`, `doc: 3`, `immutability_locks: 41`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.448
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` tooltip, account, fatal-error, api, expiring-operation-cache, react, noop, octicons...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/lib/stats/stats-store.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.149 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.265 IQR)
- **Top Global Matches:** file_cluster_13: 11.149, file_cluster_4: 11.222, file_cluster_8: 11.27
- **Magnitude:** 45.75 | **LOC:** 1248 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.8953%), Tech Debt (10.4356%)
**Top Internal Functions/Classes:**
  * `getDailyMeasures` (Impact: 95.4)
  * `recordOperationSuccessful` (Impact: 22.3)
  * `recordOperationConflictsEncounteredCount` (Impact: 22.2)
  * `recordOperationSuccessfulWithConflicts` (Impact: 22.2)
  * `recordOperationUndone` (Impact: 22.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 89`, `args: 32`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 53`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 28`, `concurrency: 97`, `import: 25`
* *Defense:* `safety: 13`, `doc: 44`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.292
  * `Choke Point (Betweenness):` 0.014681 | `Ripple Effect (Closeness):` 0.064619
  * `Imports (Out-Degree: 17):` account, diff-mode, valid-notification-pull-request-review, fatal-error, config, get-architecture, notifications-store, http...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/ui/repository-settings/repository-settings.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.211 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.275 IQR)
- **Top Global Matches:** file_cluster_13: 13.211, file_cluster_2: 13.283, file_cluster_4: 13.328
- **Magnitude:** 44.64 | **LOC:** 439 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.4871%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `componentWillMount` (Impact: 28.6)
  * `onSubmit` (Impact: 25.9)
  * `renderActiveTab` (Impact: 20.4)
  * `render` (Impact: 13.0)
  * `onCommitterNameChanged` (Impact: 6.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 63`, `args: 18`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `state_mutation: 246`
* *Architecture:* `io: 4`, `api: 9`, `concurrency: 55`, `import: 21`
* *Defense:* `safety: 9`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.074
  * `Choke Point (Betweenness):` 0.033534 | `Ripple Effect (Closeness):` 0.071024
  * `Imports (Out-Degree: 13):` account, remote, identifier-rules, no-remote, workflow-preferences, remote, popup, repository...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `app/src/lib/git/update-ref.ts` (TYPESCRIPT) | Magnitude: 2.57 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 18, doc: 10, concurrency: 10, decorators: 8
- `app/src/lib/actions-log-parser/actions-logs-ansii.ts` (TYPESCRIPT) | Magnitude: 2.13 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: branch: 24, structural_boundaries: 6, api: 6, immutability_locks: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `app/src/ui/repositories-list/repository-list-item-context-menu.ts` (TYPESCRIPT) | Magnitude: 6.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 30, args: 18, func_start: 18
- `app/src/ui/dialog/header.tsx` (TYPESCRIPT) | Magnitude: 4.29 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 36, state_mutation: 30, ui_framework: 13, structural_boundaries: 7
- `app/src/ui/lib/radio-group.tsx` (TYPESCRIPT) | Magnitude: 3.36 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 45, state_mutation: 17, structural_boundaries: 16, ui_framework: 9
- `app/src/ui/changes/changes.tsx` (TYPESCRIPT) | Magnitude: 9.38 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 95, state_mutation: 64, ui_framework: 34, structural_boundaries: 26
- `app/src/ui/history/commit-list.tsx` (TYPESCRIPT) | Magnitude: 87.09 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 781, state_mutation: 449, branch: 164, structural_boundaries: 161

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `app/src/lib/editors/found-editor.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, immutability_locks: 2, indent_spaces: 2, class_start: 1
- `app/src/lib/progress/checkout.ts` (TYPESCRIPT) | Magnitude: 0.5 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, api: 3, indent_spaces: 3, args: 2
- `app/src/lib/progress/revert.ts` (TYPESCRIPT) | Magnitude: 0.5 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, api: 3, indent_spaces: 3, args: 2
- `app/src/lib/fuzzy-find.ts` (TYPESCRIPT) | Magnitude: 1.85 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 17, generics: 8, args: 7
- `app/src/lib/set-state.ts` (TYPESCRIPT) | Magnitude: 2.1 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 11, structural_boundaries: 7, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `app/src/ui/check-runs/ci-check-run-list.tsx` (TYPESCRIPT) | Magnitude: 11.85 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 126, state_mutation: 64, structural_boundaries: 30, branch: 26
- `app/src/ui/dropdown-select-button.tsx` (TYPESCRIPT) | Magnitude: 35.99 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 316, state_mutation: 174, branch: 66, structural_boundaries: 53
- `app/src/ui/lib/observable-ref.ts` (TYPESCRIPT) | Magnitude: 2.12 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 12, generics: 10, state_mutation: 9
- `app/src/ui/lib/augmented-filter-list.tsx` (TYPESCRIPT) | Magnitude: 73.99 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 599, state_mutation: 406, branch: 137, structural_boundaries: 134
- `app/src/ui/branches/group-branches.ts` (TYPESCRIPT) | Magnitude: 3.53 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 12, immutability_locks: 11, state_mutation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `app/src/ui/preferences/custom-integration-form.tsx` (TYPESCRIPT) | Magnitude: 14.56 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 155, state_mutation: 69, ui_framework: 29, structural_boundaries: 25
- `app/src/ui/relative-time.tsx` (TYPESCRIPT) | Magnitude: 11.63 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 86, state_mutation: 58, immutability_locks: 18, ui_framework: 15
- `app/src/ui/accessibility/aria-live-container.tsx` (TYPESCRIPT) | Magnitude: 7.39 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, state_mutation: 39, structural_boundaries: 12, api: 10
- `app/src/ui/editor/editor-error.tsx` (TYPESCRIPT) | Magnitude: 4.11 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 17, ui_framework: 14, state_mutation: 13
- `app/src/ui/lib/ref-name-text-box.tsx` (TYPESCRIPT) | Magnitude: 14.88 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 130, state_mutation: 78, ui_framework: 31, branch: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `app/src/lib/hooks/get-shell.ts` (TYPESCRIPT) | Magnitude: 9.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 38, branch: 30, concurrency: 25
- `app/src/ui/lib/config-lock-file-exists.tsx` (TYPESCRIPT) | Magnitude: 2.66 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 12, structural_boundaries: 11, indent_spaces: 10, branch: 4
- `app/src/lib/git/diff-index.ts` (TYPESCRIPT) | Magnitude: 6.96 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 20, branch: 16, concurrency: 14
- `app/src/lib/stores/commit-status-store.ts` (TYPESCRIPT) | Magnitude: 26.76 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 178, state_mutation: 71, structural_boundaries: 42, concurrency: 42
- `app/src/ui/stashing/stash-diff-header.tsx` (TYPESCRIPT) | Magnitude: 9.83 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 80, state_mutation: 38, concurrency: 24, structural_boundaries: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `app/styles/_ui.scss` (CSS) | Magnitude: 0.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 113
- `app/src/main-process/shell.ts` (TYPESCRIPT) | Magnitude: 0.67 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 3, args: 2, io: 2
- `app/src/models/repository.ts` (TYPESCRIPT) | Magnitude: 2.91 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 19, api: 9, args: 6
- `app/test/e2e/playwright.config.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, io: 4, structural_boundaries: 3, import: 2
- `app/src/lib/databases/issues-database.ts` (TYPESCRIPT) | Magnitude: 2.5 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 11, args: 8, api: 8

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `app/src/lib/stores/app-store.ts` -> Churn: **78.58%** | Cog Load: 89.2993% | Debt: 10.3116%
- `app/src/lib/hooks/hooks-proxy.ts` -> Churn: **74.41%** | Cog Load: 57.5505% | Debt: 0.0%
- `script/build.ts` -> Churn: **66.3%** | Cog Load: 9.0041% | Debt: 73.7952%
- `app/src/ui/app.tsx` -> Churn: **65.73%** | Cog Load: 89.7372% | Debt: 23.1547%
- `app/src/lib/stores/copilot-store.ts` -> Churn: **64.97%** | Cog Load: 57.4774% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `app/src/ui/lib/list/list.tsx` -> **tidy-dev** (100.0% isolated ownership) | Magnitude: 106.37
- `app/src/ui/diff/side-by-side-diff.tsx` -> **tidy-dev** (100.0% isolated ownership) | Magnitude: 100.67
- `app/src/lib/api.ts` -> **Sergio Padrino** (88.9% isolated ownership) | Magnitude: 81.35
- `app/src/ui/lib/section-filter-list.tsx` -> **tidy-dev** (100.0% isolated ownership) | Magnitude: 65.18
- `app/src/ui/changes/no-changes.tsx` -> **Jack Freeman** (100.0% isolated ownership) | Magnitude: 58.03

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `app/src/ui/dispatcher/dispatcher.ts` -> **Severity: 5.55** (Bridge: 0.0555 * Flux: 99.9601%)
- `app/src/lib/menu-update.ts` -> **Severity: 3.744** (Bridge: 0.05 * Flux: 74.877%)
- `app/src/ui/repository-settings/repository-settings.tsx` -> **Severity: 3.353** (Bridge: 0.0335 * Flux: 100.0%)
- `app/src/lib/stores/app-store.ts` -> **Severity: 3.041** (Bridge: 0.0358 * Flux: 84.97%)
- `app/src/ui/dialog/dialog.tsx` -> **Severity: 1.739** (Bridge: 0.0238 * Flux: 73.0316%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `app/src/ui/dialog/ok-cancel-button-group.tsx` -> **Severity: 10.058** (Embedded: 0.1051 * Error Risk: 95.6528%)
- `app/src/ui/lib/link-button.tsx` -> **Severity: 8.942** (Embedded: 0.0964 * Error Risk: 92.7965%)
- `app/src/models/github-repository.ts` -> **Severity: 8.909** (Embedded: 0.1054 * Error Risk: 84.5365%)
- `app/src/lib/ipc-renderer.ts` -> **Severity: 8.835** (Embedded: 0.1104 * Error Risk: 80.0%)
- `app/src/ui/secret-scanning/bypass-push-protection-dialog.tsx` -> **Severity: 8.812** (Embedded: 0.1159 * Error Risk: 76.0371%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `app/src/ui/main-process-proxy.ts` -> **Severity: 1718.694** (Blast Radius: 17.297 * Doc Risk: 99.3637%)
- `app/src/lib/fatal-error.ts` -> **Severity: 1299.379** (Blast Radius: 16.35 * Doc Risk: 79.4727%)
- `app/src/models/github-repository.ts` -> **Severity: 1152.677** (Blast Radius: 11.644 * Doc Risk: 98.9932%)
- `app/src/lib/api.ts` -> **Severity: 518.668** (Blast Radius: 30.122 * Doc Risk: 17.2189%)
- `app/src/ui/lib/app-proxy.ts` -> **Severity: 468.499** (Blast Radius: 5.309 * Doc Risk: 88.2461%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
