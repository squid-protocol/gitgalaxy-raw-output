# ARCHITECTURAL_BRIEF: desktop
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/desktop` |
| **Timestamp** | `2026-08-03T19:54:12.482962+00:00` |
| **Scan Duration** | `4.29s` |
| **Git Branch** | `development` |
| **Git Commit** | `371bde25d10f8a90663dd26bedd443813a867e8d` |
| **Git Remote** | `https://github.com/desktop/desktop.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 859 malicious artifacts.

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
| Modularity | 0.4984 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
> **Architectural Drift Z-Score:** `5.021`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 475 | 44.4% |
| file_cluster_8 | 428 | 40.0% |
| file_cluster_4 | 78 | 7.3% |
| file_cluster_2 | 48 | 4.5% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 22.6 | 11.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 40.4 | 50.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 17.8 | 2.4 | 80.0 |
| API Exposure | 0.0 | 19.8 | 5.0 | 5.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 26.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 39.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 36.3 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 85.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 6.5 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 78.6 | 3.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 46.7 | 40.0 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 35.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 15.2 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `safeDirectoryName` (@ `app/src/ui/add-repository/create-repository.tsx`) -> Impact: **1052.9** | LOC: 658
  * *Intent:* // We use this instead of sanitizedRepositoryName because it deals with // valid repository names on GitHub.com but here we only care about whether //...
- `setOnOpenBanner` (@ `app/src/ui/app.tsx`) -> Impact: **681.9** | LOC: 648
- `popupContent` (@ `app/src/ui/app.tsx`) -> Impact: **609.5** | LOC: 1520
- `onUpdateSelection` (@ `app/src/ui/diff/side-by-side-diff.tsx`) -> Impact: **578.0** | LOC: 680
- `performPull` (@ `app/src/lib/stores/app-store.ts`) -> Impact: **453.5** | LOC: 462
- `showTestUI` (@ `app/src/ui/lib/test-ui-components/test-ui-components.ts`) -> Impact: **419.6** | LOC: 456
- `findNextPageSelectableRow` (@ `app/src/ui/lib/list/list.tsx`) -> Impact: **388.0** | LOC: 416
  * *Intent:* /** * Callback to fire when the index path of the position to insert items via * keyboard changes.
- `getRepositoryMenuBuilder` (@ `app/src/lib/menu-update.ts`) -> Impact: **375.7** | LOC: 314
- `parse` (@ `app/src/lib/git/cherry-pick.ts`) -> Impact: **328.9** | LOC: 339
  * *Intent:* /** * The cherry pick was not attempted: * - it could not check the status of the repository. * - there was an invalid revision range provided.
- `getAvatarUrlCandidates` (@ `app/src/ui/lib/avatar.tsx`) -> Impact: **293.3** | LOC: 266

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `renderUpdateErrors` (@ `app/src/ui/about/about.tsx`) -> **O(2^N) [Recursive]**
- `safeDirectoryName` (@ `app/src/ui/add-repository/create-repository.tsx`) -> **O(2^N) [Recursive]**
  * *Intent:* // We use this instead of sanitizedRepositoryName because it deals with // valid repository names on GitHub.com but here we only care about whether //...
- `renderWarningPopover` (@ `app/src/ui/changes/commit-message-avatar.tsx`) -> **O(2^N) [Recursive]**
- `squash` (@ `app/src/lib/git/squash.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* * maintaining that A came before C and E came after C, placed in history at the * the squashOnto of C. * * Also means if the last 2 commits in history...
- `progressCallback` (@ `app/src/lib/progress/from-process.ts`) -> **O(2^N) [Recursive]**
- `getAheadBehind` (@ `app/src/lib/stores/ahead-behind-store.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Attempt to _synchronously_ retrieve an ahead behind status for a particular * range. If the range doesn't exist in the cache this function retur...
- `emitUpdate` (@ `app/src/lib/stores/app-store.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* // One is the default value, we only care about checking the locally stored
- `_upsertGitHubRepository` (@ `app/src/lib/stores/repositories-store.ts`) -> **O(2^N) [Recursive]**
- `getItemId` (@ `app/src/ui/account-picker.tsx`) -> **O(2^N) [Recursive]**
- `onKeyDown` (@ `app/src/ui/autocompletion/autocompleting-text-input.tsx`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `safeDirectoryName` (@ `app/src/ui/add-repository/create-repository.tsx`) -> DB Complexity: **397**
  * *Intent:* // We use this instead of sanitizedRepositoryName because it deals with // valid repository names on GitHub.com but here we only care about whether //...
- `popupContent` (@ `app/src/ui/app.tsx`) -> DB Complexity: **327**
- `findHyper` (@ `app/src/lib/shells/win32.ts`) -> DB Complexity: **192**
- `setOnOpenBanner` (@ `app/src/ui/app.tsx`) -> DB Complexity: **154**
- `findNextPageSelectableRow` (@ `app/src/ui/lib/list/list.tsx`) -> DB Complexity: **108**
  * *Intent:* /** * Callback to fire when the index path of the position to insert items via * keyboard changes.
- `onUpdateSelection` (@ `app/src/ui/diff/side-by-side-diff.tsx`) -> DB Complexity: **103**
- `emitUpdate` (@ `app/src/lib/stores/app-store.ts`) -> DB Complexity: **88**
  * *Intent:* // One is the default value, we only care about checking the locally stored
- `renderActiveTab` (@ `app/src/ui/preferences/preferences.tsx`) -> DB Complexity: **81**
- `constructor` (@ `app/src/main-process/app-window.ts`) -> DB Complexity: **75**
- `getAvailableShells` (@ `app/src/lib/shells/linux.ts`) -> DB Complexity: **72**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `app` | 8 | 5020.81 | 5.6% | 0.0% |
| `app/src/ui/lib` | 79 | 802.0 | 28.06% | 2.03% |
| `app/src/lib/stores` | 24 | 648.51 | 48.15% | 8.23% |
| `app/src/ui` | 22 | 548.97 | 43.62% | 4.91% |
| `app/src/lib` | 102 | 504.79 | 16.61% | 10.06% |
| `app/src/lib/git` | 57 | 471.05 | 27.3% | 2.55% |
| `app/src/ui/history` | 12 | 297.01 | 43.51% | 1.98% |
| `app/src/ui/diff` | 16 | 283.28 | 25.38% | 0.0% |
| `app/src/ui/preferences` | 11 | 257.22 | 59.9% | 0.82% |
| `app/src/ui/dispatcher` | 3 | 242.51 | 28.48% | 2.99% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `app/src/lib/is-git-on-path.ts` -> **100.0%** Exposure
- `app/src/lib/pick.ts` -> **100.0%** Exposure
- `app/src/lib/stores/base-store.ts` -> **100.0%** Exposure
- `app/src/ui/autocompletion/autocompletion-provider.ts` -> **100.0%** Exposure
- `script/setup-macos-keychain` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `app/src/lib/git/push.ts` -> **100.0%** Exposure
- `app/src/lib/mouse-scroller.ts` -> **100.0%** Exposure
- `app/src/lib/popup-manager.ts` -> **100.0%** Exposure
- `app/src/lib/set-state.ts` -> **100.0%** Exposure
- `app/src/lib/split-buffer.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `app/src/lib/stores/base-store.ts` -> **0** Orphaned Functions | **8** Duplicates
- `app/src/lib/stores/repository-state-cache.ts` -> **0** Orphaned Functions | **7** Duplicates
- `app/src/main-process/menu/build-default-menu.ts` -> **0** Orphaned Functions | **7** Duplicates
- `app/src/main-process/ordered-webrequest.ts` -> **0** Orphaned Functions | **7** Duplicates
- `app/src/lib/editors/win32.ts` -> **0** Orphaned Functions | **6** Duplicates

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

### Exploit Generation Surface
- `app/src/lib/actions-log-parser/action-log-parser.ts` -> **100.0%** Exposure
- `app/src/lib/api.ts` -> **100.0%** Exposure
- `app/src/lib/git/core.ts` -> **100.0%** Exposure
- `app/src/lib/stores/accounts-store.ts` -> **100.0%** Exposure
- `app/src/lib/stores/app-store.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `app/src/ui/banners/os-version-no-longer-supported-banner.tsx` -> **100.0%** Exposure
- `app/src/ui/main-process-proxy.ts` -> **100.0%** Exposure
- `script/build.ts` -> **100.0%** Exposure
- `script/draft-release/index.ts` -> **100.0%** Exposure
- `script/package.ts` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `app/src/ui/diff/diff-helpers.tsx` -> **98.0093%** Exposure
### Algorithmic DoS Exposure
- `app/src/lib/actions-log-parser/action-log-parser.ts` -> **100.0%** Exposure
- `app/src/lib/api.ts` -> **100.0%** Exposure
- `app/src/lib/diff-parser.ts` -> **100.0%** Exposure
- `app/src/lib/file-system.ts` -> **100.0%** Exposure
- `app/src/lib/git/cherry-pick.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1072` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `app/src/main-process/ordered-webrequest.ts` (TYPESCRIPT) -> Cumulative Risk: **962.24**
- **Archetype:** `file_cluster_4` (Distance: 12.852 IQR)
- **Magnitude:** 19.07 | **LOC:** 249 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 38.0), `addEventListener` (Impact: 5.7), `addEventListener` (Impact: 4.4)

### 2. `app/src/ui/rename-branch/rename-branch-dialog.tsx` (TYPESCRIPT) -> Cumulative Risk: **909.12**
- **Archetype:** `file_cluster_13` (Distance: 12.924 IQR)
- **Magnitude:** 18.24 | **LOC:** 151 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `render` (Impact: 19.3), `checkBranchRules` (Impact: 13.2), `onNameChange` (Impact: 9.8)

### 3. `app/src/ui/autocompletion/user-autocompletion-provider.tsx` (TYPESCRIPT) -> Cumulative Risk: **890.57**
- **Archetype:** `file_cluster_13` (Distance: 11.564 IQR)
- **Magnitude:** 14.67 | **LOC:** 219 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (99.9986%)
- **Heaviest Functions:** `renderItem` (Impact: 29.7), `exactMatch` (Impact: 18.1), `getRegExp` (Impact: 8.8)

### 4. `app/src/ui/open-with-external-editor/open-with-external-editor.tsx` (TYPESCRIPT) -> Cumulative Risk: **881.54**
- **Archetype:** `file_cluster_13` (Distance: 12.724 IQR)
- **Magnitude:** 21.06 | **LOC:** 178 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `renderEditorSelect` (Impact: 22.2), `render` (Impact: 18.7), `renderCustomEditor` (Impact: 13.8)

### 5. `app/src/ui/check-runs/ci-check-run-rerun-dialog.tsx` (TYPESCRIPT) -> Cumulative Risk: **863.64**
- **Archetype:** `file_cluster_13` (Distance: 12.671 IQR)
- **Magnitude:** 29.69 | **LOC:** 260 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `determineRerunnability` (Impact: 36.4), `renderRerunWarning` (Impact: 32.6), `getTitle` (Impact: 22.8)

### 6. `app/src/ui/lib/sandboxed-markdown.tsx` (TYPESCRIPT) -> Cumulative Risk: **862.76**
- **Archetype:** `file_cluster_13` (Distance: 12.942 IQR)
- **Magnitude:** 39.49 | **LOC:** 404 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `renderMarkdown` (Impact: 38.2), `applyFilters` (Impact: 35.6), `setupLinkInterceptor` (Impact: 28.7)

### 7. `app/src/ui/preferences/preferences.tsx` (TYPESCRIPT) -> Cumulative Risk: **861.43**
- **Archetype:** `file_cluster_2` (Distance: 13.451 IQR)
- **Magnitude:** 105.22 | **LOC:** 919 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `renderActiveTab` (Impact: 121.9), `onSave` (Impact: 94.1), `getTabId` (Impact: 58.6)

### 8. `app/src/ui/app.tsx` (TYPESCRIPT) -> Cumulative Risk: **860.59**
- **Archetype:** `file_cluster_13` (Distance: 13.94 IQR)
- **Magnitude:** 285.62 | **LOC:** 3761 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `setOnOpenBanner` (Impact: 681.9), `popupContent` (Impact: 609.5), `onWindowKeyUp` (Impact: 33.3)

### 9. `app/src/ui/missing-repository.tsx` (TYPESCRIPT) -> Cumulative Risk: **858.39**
- **Archetype:** `file_cluster_4` (Distance: 12.873 IQR)
- **Magnitude:** 27.3 | **LOC:** 190 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `render` (Impact: 42.5), `cloneAgain` (Impact: 27.0), `onTrustDirectory` (Impact: 8.6)

### 10. `app/src/ui/preferences/integrations.tsx` (TYPESCRIPT) -> Cumulative Risk: **854.51**
- **Archetype:** `file_cluster_13` (Distance: 12.579 IQR)
- **Magnitude:** 28.87 | **LOC:** 386 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `componentDidMount` (Impact: 34.0), `componentWillReceiveProps` (Impact: 25.5), `render` (Impact: 18.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `app/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.448
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/ui/app.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.94 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.785 IQR)
- **Top Global Matches:** file_cluster_13: 13.94, file_cluster_2: 14.036, file_cluster_17: 14.298
- **Magnitude:** 285.62 | **LOC:** 3761 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 327
- **Risk Profile:** Cognitive Load (89.802%), Tech Debt (8.0209%)
**Top Internal Functions/Classes:**
  * `setOnOpenBanner` (Impact: 681.9 | O(N^4) | DB: 154)
  * `popupContent` (Impact: 609.5 | O(N^3) | DB: 327)
  * `onWindowKeyUp` (Impact: 33.3 | O(N^3) | DB: 7)
  * `constructor` (Impact: 31.9 | O(N^3) | DB: 13)
  * `checkIfThankYouIsInOrder` (Impact: 20.6 | O(N^2) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 347`, `structural_boundaries: 493`, `args: 202`, `func_start: 119`, `class_start: 1`
* *Risk/State:* `state_mutation: 1168`, `dead_code: 3`, `planned_debt: 3`
* *Architecture:* `io: 19`, `api: 10`, `concurrency: 145`, `import: 154`
* *Defense:* `safety: 18`, `doc: 15`, `immutability_locks: 161`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.495
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002809
  * `Imports (Out-Degree: 97):` invalidated-token, features, preferences, warning-before-reset, unreachable-commits-dialog, react-transition-group, publish-repository, generate-commit-message-override-warning...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/ui/dispatcher/dispatcher.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.41 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.054 IQR)
- **Top Global Matches:** file_cluster_4: 13.41, file_cluster_13: 13.721, file_cluster_8: 14.033
- **Magnitude:** 206.48 | **LOC:** 4083 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (49.9949%), Tech Debt (8.9693%)
**Top Internal Functions/Classes:**
  * `processMultiCommitOperationRebaseResult` (Impact: 119.0 | O(2^N) | DB: 6)
  * `squash` (Impact: 60.5 | O(2^N) | DB: 13)
  * `onConflictsFoundBanner` (Impact: 54.7 | O(2^N) | DB: 20)
  * `getMultiCommitOperationSuccessBanner` (Impact: 47.3 | O(N^2) | DB: 2)
  * `reorderCommits` (Impact: 30.5 | O(N^2) | DB: 13)
    * *Intent:* /** * Ask the dispatcher to apply a transformation function to the current * state of the applicatio...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 240`, `args: 145`, `func_start: 141`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 385`, `dead_code: 2`, `planned_debt: 5`
* *Architecture:* `io: 20`, `api: 223`, `concurrency: 679`, `import: 60`
* *Defense:* `safety: 64`, `doc: 125`, `immutability_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.851
  * `Choke Point (Betweenness):` 0.05552 | `Ripple Effect (Closeness):` 0.068399
  * `Imports (Out-Degree: 38):` drag-and-drop-manager, drag-drop, repository-state-cache, pull-request, manual-conflict-resolution, tip, fetch, commit-status-store...
  * `Imported By (In-Degree: 99):` (Excluded from Brief to save tokens)

### `app/src/lib/stores/app-store.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.377 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.917 IQR)
- **Top Global Matches:** file_cluster_4: 13.377, file_cluster_13: 13.483, file_cluster_8: 13.839
- **Magnitude:** 194.71 | **LOC:** 8730 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 48.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 88
- **Risk Profile:** Cognitive Load (89.3238%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `performPull` (Impact: 453.5 | O(N^6) | DB: 67)
  * `emitUpdate` (Impact: 99.5 | O(2^N) | DB: 88)
    * *Intent:* // One is the default value, we only care about checking the locally stored
  * `_changeFileSelection` (Impact: 44.8 | O(N^3) | DB: 9)
  * `getShasInDiff` (Impact: 41.6 | O(N^3) | DB: 4)
  * `updateCompareToBranch` (Impact: 35.6 | O(N^3) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 303`, `args: 119`, `func_start: 75`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 468`, `dead_code: 2`
* *Architecture:* `io: 6`, `api: 64`, `concurrency: 528`, `import: 116`
* *Defense:* `safety: 39`, `doc: 33`, `immutability_locks: 152`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.727
  * `Choke Point (Betweenness):` 0.03579 | `Ripple Effect (Closeness):` 0.059862
  * `Imports (Out-Degree: 80):` equality, drag-drop, app-state, pull-request-matching, shared, remote-parsing, computed-action, changes-state...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/ui/add-repository/create-repository.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.897 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.869 IQR)
- **Top Global Matches:** file_cluster_4: 13.897, file_cluster_13: 13.951, file_cluster_17: 13.99
- **Magnitude:** 161.59 | **LOC:** 783 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 397
- **Risk Profile:** Cognitive Load (73.3063%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `safeDirectoryName` (Impact: 1052.9 | O(2^N) | DB: 397)
    * *Intent:* // We use this instead of sanitizedRepositoryName because it deals with // valid repository names on...
  * `onWindowFocus` (Impact: 2.0 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 126`, `args: 52`, `func_start: 35`, `class_start: 3`
* *Risk/State:* `state_mutation: 386`, `dead_code: 1`
* *Architecture:* `io: 93`, `api: 6`, `concurrency: 156`, `import: 32`
* *Defense:* `safety: 35`, `doc: 16`, `immutability_locks: 66`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000936
  * `Imports (Out-Degree: 26):` row, link-button, checkbox, ok-cancel-button-group, path, default-dir, gitignores, is-top-most...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/src/ui/preferences/preferences.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.451 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.308 IQR)
- **Top Global Matches:** file_cluster_2: 13.451, file_cluster_13: 13.525, file_cluster_4: 13.603
- **Magnitude:** 105.22 | **LOC:** 919 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(N^4) | **DB Complexity:** 81
- **Risk Profile:** Cognitive Load (95.4773%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderActiveTab` (Impact: 121.9 | O(N^4) | DB: 81)
  * `onSave` (Impact: 94.1 | O(N^3) | DB: 51)
  * `getTabId` (Impact: 58.6 | O(N^2) | DB: 1)
  * `componentWillMount` (Impact: 57.4 | O(N^2) | DB: 24)
  * `constructor` (Impact: 14.3 | O(N^1) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 116`, `args: 61`, `func_start: 76`, `class_start: 3`
* *Risk/State:* `state_mutation: 444`
* *Architecture:* `io: 2`, `api: 9`, `concurrency: 125`, `import: 31`
* *Defense:* `safety: 15`, `doc: 3`, `sync_locks: 1`, `immutability_locks: 94`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.448
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` octicons, default-branch, accessibility, tab-bar, git, ok-cancel-button-group, octicons.generated, preferences...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/ui/history/commit-list.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.834 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.285 IQR)
- **Top Global Matches:** file_cluster_2: 13.834, file_cluster_13: 13.837, file_cluster_17: 13.858
- **Magnitude:** 99.09 | **LOC:** 1046 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (34.6556%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getContextMenuForSingleCommit` (Impact: 128.3 | O(N^3) | DB: 38)
  * `renderRowFocusTooltip` (Impact: 40.0 | O(N^4) | DB: 9)
  * `onDropDataInsertion` (Impact: 35.8 | O(N^2) | DB: 7)
  * `render` (Impact: 31.3 | O(N^3) | DB: 27)
  * `renderKeyboardInsertionElement` (Impact: 31.3 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 161`, `args: 100`, `func_start: 57`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 449`
* *Architecture:* `io: 1`, `api: 7`, `import: 27`
* *Defense:* `safety: 47`, `doc: 41`, `immutability_locks: 116`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.704
  * `Choke Point (Betweenness):` 0.014545 | `Ripple Effect (Closeness):` 0.063674
  * `Imports (Out-Degree: 16):` drag-drop, octicons, list-row-index-path, commit-list-item, electron, debounce, aria-live-container, memoize-one...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/ui/diff/side-by-side-diff.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.84 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.891 IQR)
- **Top Global Matches:** file_cluster_13: 12.84, file_cluster_2: 13.047, file_cluster_8: 13.15
- **Magnitude:** 98.78 | **LOC:** 2151 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 103
- **Risk Profile:** Cognitive Load (53.4641%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onUpdateSelection` (Impact: 578.0 | O(N^3) | DB: 103)
  * `onKeyDown` (Impact: 16.6 | O(N^1) | DB: 2)
  * `onMouseDown` (Impact: 13.0 | O(N^1) | DB: 5)
  * `onSelectAll` (Impact: 12.5 | O(N^1) | DB: 2)
    * *Intent:* /** * Indicates the hunk that the user is currently hovering via the gutter. * * In this context, a ...
  * `closestRow` (Impact: 10.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 129`, `args: 50`, `func_start: 55`, `class_start: 4`
* *Risk/State:* `state_mutation: 329`
* *Architecture:* `api: 9`, `import: 22`
* *Defense:* `safety: 18`, `doc: 29`, `immutability_locks: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.529
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001873
  * `Imports (Out-Degree: 11):` diff-explorer, aria-live-container, react-dom, memoize-one, text-diff-expansion, react-virtualized, diff-helpers, get-tokens...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `app/src/ui/lib/list/list.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.648 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.226 IQR)
- **Top Global Matches:** file_cluster_2: 13.648, file_cluster_13: 13.681, file_cluster_17: 13.886
- **Magnitude:** 97.95 | **LOC:** 1758 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 108
- **Risk Profile:** Cognitive Load (52.3811%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `findNextPageSelectableRow` (Impact: 388.0 | O(N^3) | DB: 108)
    * *Intent:* /** * Callback to fire when the index path of the position to insert items via * keyboard changes.
  * `onRef` (Impact: 38.0 | O(N^2) | DB: 7)
    * *Intent:* /** * A handler called whenever the user drops items on the list to be inserted. * * @param row - Th...
  * `constructor` (Impact: 29.4 | O(N^3) | DB: 9)
    * *Intent:* /** * This function will be called when the selection changes as a result of a * user keyboard or mo...
  * `onSelectAll` (Impact: 18.4 | O(N^1) | DB: 7)
    * *Intent:* /** * A handler called whenever a key down event is received on the * row container element. Due to ...
  * `addSelectionByPage` (Impact: 14.1 | O(N^2) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 69`, `args: 37`, `func_start: 27`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 434`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 10`, `concurrency: 6`, `import: 15`
* *Defense:* `safety: 12`, `doc: 34`, `immutability_locks: 75`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.152
  * `Choke Point (Betweenness):` 0.003652 | `Ripple Effect (Closeness):` 0.060385
  * `Imports (Out-Degree: 10):` list-row-index-path, react-virtualized, selection, focus-container, react, memoize-one, equality, range...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `app/src/ui/autocompletion/autocompleting-text-input.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.302 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.377 IQR)
- **Top Global Matches:** file_cluster_2: 13.302, file_cluster_13: 13.412, file_cluster_17: 13.586
- **Magnitude:** 85.31 | **LOC:** 794 | **CtrlFlow:** 56.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (42.8791%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onKeyDown` (Impact: 131.0 | O(2^N) | DB: 9)
  * `render` (Impact: 36.5 | O(N^3) | DB: 10)
  * `attemptAutocompletion` (Impact: 26.0 | O(N^3) | DB: 7)
  * `renderItem` (Impact: 24.5 | O(2^N) | DB: 1)
  * `renderAutocompletions` (Impact: 18.8 | O(N^2) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 87`, `args: 51`, `func_start: 43`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 332`
* *Architecture:* `api: 12`, `concurrency: 37`, `import: 10`
* *Defense:* `safety: 24`, `doc: 29`, `immutability_locks: 102`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.893
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001248
  * `Imports (Out-Degree: 6):` popover, list, react, fatal-error, menu-item, classnames, aria-live-container, textarea-caret...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/src/ui/lib/augmented-filter-list.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.467 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.478 IQR)
- **Top Global Matches:** file_cluster_17: 13.467, file_cluster_2: 13.504, file_cluster_13: 13.651
- **Magnitude:** 84.21 | **LOC:** 926 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (35.1078%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onKeyDown` (Impact: 71.8 | O(N^3) | DB: 13)
  * `createStateUpdate` (Impact: 42.1 | O(N^2) | DB: 7)
  * `onRowKeyDown` (Impact: 39.5 | O(N^2) | DB: 9)
  * `componentDidUpdate` (Impact: 26.5 | O(N^3) | DB: 14)
  * `selectNextItem` (Impact: 25.8 | O(N^2) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 134`, `args: 82`, `func_start: 37`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 406`
* *Architecture:* `io: 1`, `api: 19`, `import: 12`
* *Defense:* `safety: 16`, `doc: 37`, `immutability_locks: 100`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002341
  * `Imports (Out-Degree: 8):` react, row, section-list, xor, classnames, filter-list, aria-live-container, fuzzy-find...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/src/ui/lib/section-filter-list.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.359 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.243 IQR)
- **Top Global Matches:** file_cluster_2: 13.359, file_cluster_13: 13.503, file_cluster_17: 13.533
- **Magnitude:** 77.53 | **LOC:** 788 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (34.729%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onKeyDown` (Impact: 71.8 | O(N^3) | DB: 13)
  * `createStateUpdate` (Impact: 46.7 | O(N^2) | DB: 6)
  * `componentDidUpdate` (Impact: 33.3 | O(N^3) | DB: 12)
  * `onRowKeyDown` (Impact: 31.2 | O(N^2) | DB: 6)
  * `selectNextItem` (Impact: 22.8 | O(N^2) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 104`, `args: 63`, `func_start: 34`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 358`
* *Architecture:* `io: 1`, `api: 18`, `import: 11`
* *Defense:* `safety: 12`, `doc: 31`, `immutability_locks: 80`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.724
  * `Choke Point (Betweenness):` 7.8e-05 | `Ripple Effect (Closeness):` 0.009346
  * `Imports (Out-Degree: 8):` react, row, section-list, classnames, filter-list, aria-live-container, fuzzy-find, octicons.generated...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `app/src/lib/api.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.347 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.961 IQR)
- **Top Global Matches:** file_cluster_4: 12.347, file_cluster_13: 12.726, file_cluster_17: 12.889
- **Magnitude:** 75.3 | **LOC:** 2486 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 88.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 55
- **Risk Profile:** Cognitive Load (49.8461%), Tech Debt (9.3466%)
**Top Internal Functions/Classes:**
  * `fetchAllRepoRulesets` (Impact: 201.4 | O(N^2) | DB: 55)
  * `callback` (Impact: 55.3 | O(2^N) | DB: 8)
  * `fetchIssueComment` (Impact: 31.2 | O(2^N) | DB: 1)
  * `fetchUpdatedPullRequests` (Impact: 18.0 | O(N^2) | DB: 6)
  * `getNextPagePathWithIncreasingPageSize` (Impact: 17.3 | O(N^1))
    * *Intent:* /** * Information about a commit as returned by the GitHub API. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 152`, `args: 47`, `func_start: 42`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 82`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 20`, `api: 48`, `concurrency: 252`, `import: 11`
* *Defense:* `safety: 44`, `doc: 73`, `immutability_locks: 123`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.122
  * `Choke Point (Betweenness):` 0.023597 | `Ripple Effect (Closeness):` 0.142782
  * `Imports (Out-Degree: 9):` account, copilot-commit-message, http, copilot-error, endpoint-capabilities, url, http-status-code, remote-parsing...
  * `Imported By (In-Degree: 82):` (Excluded from Brief to save tokens)

### `app/src/lib/stores/repositories-store.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.809 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.125 IQR)
- **Top Global Matches:** file_cluster_4: 12.809, file_cluster_13: 13.34, file_cluster_11: 13.683
- **Magnitude:** 71.38 | **LOC:** 742 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (57.4997%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_upsertGitHubRepository` (Impact: 139.4 | O(2^N) | DB: 7)
  * `getLastStashCheckDate` (Impact: 56.7 | O(2^N) | DB: 5)
  * `putOwner` (Impact: 37.8 | O(N^2) | DB: 3)
  * `updateBranchProtections` (Impact: 21.3 | O(N^2) | DB: 13)
  * `upsertGitHubRepositoryFromMatch` (Impact: 9.6 | O(N^2) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 64`, `args: 21`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 118`, `dead_code: 1`
* *Architecture:* `io: 3`, `api: 21`, `concurrency: 274`, `import: 12`
* *Defense:* `safety: 15`, `doc: 19`, `immutability_locks: 28`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.728
  * `Choke Point (Betweenness):` 0.001923 | `Ripple Effect (Closeness):` 0.055182
  * `Imports (Out-Degree: 10):` api, equality, github-repository, fatal-error, repository, owner, workflow-preferences, repository-matching...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `app/src/ui/diff/side-by-side-diff-row.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.471 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.331 IQR)
- **Top Global Matches:** file_cluster_2: 12.471, file_cluster_13: 12.597, file_cluster_8: 12.668
- **Magnitude:** 70.53 | **LOC:** 1052 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (30.6958%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderLineNumbers` (Impact: 63.2 | O(N^4) | DB: 8)
  * `renderHunkHandle` (Impact: 61.0 | O(N^4) | DB: 13)
  * `render` (Impact: 55.5 | O(N^4) | DB: 39)
  * `getDiffColumn` (Impact: 24.8 | O(N^2) | DB: 1)
  * `getDiffData` (Impact: 24.6 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 115`, `args: 65`, `func_start: 35`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 278`
* *Architecture:* `api: 10`, `import: 13`
* *Defense:* `safety: 21`, `doc: 43`, `immutability_locks: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.488
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001685
  * `Imports (Out-Degree: 6):` diff-helpers, octicons, popover, react, whitespace-hint-popover, equality, types, diff...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/src/ui/history/compare.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.991 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.116 IQR)
- **Top Global Matches:** file_cluster_13: 12.991, file_cluster_2: 12.995, file_cluster_17: 13.139
- **Magnitude:** 68.96 | **LOC:** 753 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (88.8601%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onBranchFilterKeyDown` (Impact: 53.5 | O(N^2) | DB: 14)
  * `renderCommitList` (Impact: 27.9 | O(N^3) | DB: 35)
  * `componentWillReceiveProps` (Impact: 19.4 | O(N^2) | DB: 5)
  * `componentDidUpdate` (Impact: 18.8 | O(N^2) | DB: 4)
  * `onScroll` (Impact: 18.8 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 107`, `args: 68`, `func_start: 61`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 317`
* *Architecture:* `api: 15`, `concurrency: 37`, `import: 28`
* *Defense:* `safety: 17`, `doc: 3`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.448
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` drag-drop, commit-list, branches, squashed-commit-description, tab-bar, filter-list, fuzzy-find, octicons.generated...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/ui/lib/filter-list.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.274 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.266 IQR)
- **Top Global Matches:** file_cluster_2: 13.274, file_cluster_13: 13.484, file_cluster_17: 13.594
- **Magnitude:** 66.81 | **LOC:** 678 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (34.5906%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onKeyDown` (Impact: 71.5 | O(N^3) | DB: 13)
  * `createStateUpdate` (Impact: 46.2 | O(N^2) | DB: 3)
  * `componentDidUpdate` (Impact: 33.3 | O(N^3) | DB: 12)
  * `onRowKeyDown` (Impact: 25.2 | O(N^2) | DB: 6)
  * `selectNextItem` (Impact: 22.8 | O(N^2) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 88`, `args: 49`, `func_start: 25`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 316`
* *Architecture:* `api: 21`, `import: 7`
* *Defense:* `safety: 7`, `doc: 35`, `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 6.7e-05 | `Ripple Effect (Closeness):` 0.016854
  * `Imports (Out-Degree: 5):` list, react, row, classnames, aria-live-container, fuzzy-find, text-box
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `app/src/lib/stores/git-store.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.094 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.158 IQR)
- **Top Global Matches:** file_cluster_4: 13.094, file_cluster_13: 13.271, file_cluster_8: 13.749
- **Magnitude:** 65.69 | **LOC:** 1775 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (57.4993%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mergeRemoteAndLocalBranches` (Impact: 42.3 | O(N^2) | DB: 5)
  * `undoFirstCommit` (Impact: 39.9 | O(N^2) | DB: 11)
  * `emitUpdatesForChangedTags` (Impact: 35.7 | O(N^2) | DB: 9)
    * *Intent:* /** The store for a repository's git data. */
  * `loadLocalCommits` (Impact: 23.2 | O(N^2) | DB: 13)
  * `createBranch` (Impact: 18.9 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 94`, `args: 37`, `func_start: 26`
* *Risk/State:* `state_mutation: 201`
* *Architecture:* `io: 3`, `api: 25`, `concurrency: 213`, `import: 34`
* *Defense:* `doc: 19`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.795
  * `Choke Point (Betweenness):` 0.003891 | `Ripple Effect (Closeness):` 0.047953
  * `Imports (Out-Degree: 21):` remote, upstream-already-exists-error, progress, pull-request, tip, app-state, tags-to-push-storage, path...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/ui/test-notifications/test-notifications.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.283 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.815 IQR)
- **Top Global Matches:** file_cluster_2: 12.283, file_cluster_13: 12.323, file_cluster_8: 12.393
- **Magnitude:** 64.72 | **LOC:** 801 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (69.4561%), Tech Debt (14.2854%)
**Top Internal Functions/Classes:**
  * `prepareForNextStep` (Impact: 56.3 | O(N^3) | DB: 26)
  * `doFinalAction` (Impact: 41.9 | O(N^2) | DB: 13)
  * `renderCurrentStep` (Impact: 29.6 | O(N^3) | DB: 9)
  * `getTypeFriendlyName` (Impact: 27.8 | O(N^2) | DB: 1)
  * `renderNotificationHint` (Impact: 23.4 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 123`, `args: 62`, `func_start: 35`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 268`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 7`, `concurrency: 24`, `import: 20`
* *Defense:* `safety: 9`, `immutability_locks: 69`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.452
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00214
  * `Imports (Out-Degree: 12):` pull-request-review-helpers, octicons, list-row-index-path, pull-request, link-button, notifications-debug-store, octicons.generated, repository...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/src/ui/changes/commit-message-avatar.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.098 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.342 IQR)
- **Top Global Matches:** file_cluster_13: 13.098, file_cluster_2: 13.159, file_cluster_4: 13.38
- **Magnitude:** 63.35 | **LOC:** 479 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (58.5939%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderWarningPopover` (Impact: 233.3 | O(2^N) | DB: 31)
  * `renderGitConfigPopover` (Impact: 36.6 | O(N^3) | DB: 5)
  * `render` (Impact: 27.8 | O(N^2) | DB: 8)
  * `componentDidUpdate` (Impact: 18.8 | O(N^1) | DB: 8)
    * *Intent:* /** * Called when the user has requested to see the Git tab in the user settings
  * `renderWarningBadge` (Impact: 11.3 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 60`, `args: 33`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `state_mutation: 200`
* *Architecture:* `io: 1`, `api: 8`, `concurrency: 36`, `import: 18`
* *Defense:* `safety: 10`, `doc: 12`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.469
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002107
  * `Imports (Out-Degree: 7):` popover, octicons, avatar, repository, repo-rules, react, avatar, row...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `app/src/ui/repository.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.837 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.118 IQR)
- **Top Global Matches:** file_cluster_2: 12.837, file_cluster_13: 12.887, file_cluster_8: 13.238
- **Magnitude:** 59.27 | **LOC:** 754 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^3) | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (67.5475%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderChangesSidebar` (Impact: 35.3 | O(N^3) | DB: 43)
  * `renderContentForChanges` (Impact: 34.4 | O(N^3) | DB: 23)
  * `renderStashedChangesContent` (Impact: 15.5 | O(N^3) | DB: 12)
  * `renderCompareSidebar` (Impact: 13.1 | O(N^2) | DB: 14)
  * `onGlobalKeyDown` (Impact: 12.8 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 89`, `args: 52`, `func_start: 42`, `class_start: 3`
* *Risk/State:* `state_mutation: 315`
* *Architecture:* `api: 17`, `import: 32`
* *Defense:* `safety: 8`, `doc: 11`, `immutability_locks: 69`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.453
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000936
  * `Imports (Out-Degree: 23):` open-file, multiple-selection, resizable, diff, ui-view, pull-request, repository, files-changed-badge...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `eslint-rules/react-proper-lifecycle-methods.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.68 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.99 IQR)
- **Top Global Matches:** file_cluster_8: 11.68, file_cluster_7: 11.845, file_cluster_6: 11.937
- **Magnitude:** 58.74 | **LOC:** 368 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (5.1128%), Tech Debt (72.0768%)
**Top Internal Functions/Classes:**
  * `getPropsType` (Impact: 53.0 | O(N^4) | DB: 1)
    * *Intent:* // @ts-check /** * react-proper-lifecycle-methods * * This custom eslint rule is attempts to prevent...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 8`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 7`, `doc: 27`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.448
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` experimental-utils, typescript-estree
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/ui/repository-settings/repository-settings.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.243 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.281 IQR)
- **Top Global Matches:** file_cluster_13: 13.243, file_cluster_2: 13.311, file_cluster_4: 13.361
- **Magnitude:** 51.19 | **LOC:** 439 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (98.4826%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onSubmit` (Impact: 48.4 | O(N^3) | DB: 35)
  * `componentWillMount` (Impact: 41.6 | O(N^2) | DB: 15)
  * `renderActiveTab` (Impact: 37.7 | O(N^3) | DB: 21)
  * `render` (Impact: 28.6 | O(N^4) | DB: 9)
  * `constructor` (Impact: 7.2 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 63`, `args: 23`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `state_mutation: 246`
* *Architecture:* `io: 4`, `api: 8`, `concurrency: 55`, `import: 21`
* *Defense:* `safety: 9`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.074
  * `Choke Point (Betweenness):` 0.033534 | `Ripple Effect (Closeness):` 0.071024
  * `Imports (Out-Degree: 13):` git-ignore, remote, octicons, tab-bar, ok-cancel-button-group, octicons.generated, repository, react...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `app/src/ui/toolbar/push-pull-button.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.737 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.793 IQR)
- **Top Global Matches:** file_cluster_13: 12.737, file_cluster_2: 12.881, file_cluster_8: 13.038
- **Magnitude:** 50.98 | **LOC:** 688 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (42.4266%), Tech Debt (73.1059%)
**Top Internal Functions/Classes:**
  * `renderButton` (Impact: 35.0 | O(N^2) | DB: 27)
  * `componentDidUpdate` (Impact: 31.1 | O(N^2) | DB: 11)
  * `renderAheadBehind` (Impact: 19.5 | O(N^2) | DB: 2)
  * `onClick` (Impact: 17.0 | O(2^N) | DB: 5)
  * `setScreenReaderLoadingStateMessage` (Impact: 16.4 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 80`, `args: 46`, `func_start: 36`, `class_start: 4`
* *Risk/State:* `state_mutation: 248`, `fragile_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `io: 15`, `api: 11`, `import: 21`
* *Defense:* `safety: 24`, `doc: 31`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.989
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002809
  * `Imports (Out-Degree: 9):` octicons, progress, tip, fetch, relative-time, aria-live-container, dropdown, octicons.generated...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/ui/changes/no-changes.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.616 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.718 IQR)
- **Top Global Matches:** file_cluster_13: 11.616, file_cluster_2: 11.745, file_cluster_8: 11.763
- **Magnitude:** 49.62 | **LOC:** 783 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (37.585%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `buildMenuItemInfoMap` (Impact: 43.4 | O(2^N) | DB: 1)
  * `renderPushBranchAction` (Impact: 33.4 | O(N^2) | DB: 9)
  * `renderRemoteAction` (Impact: 28.5 | O(N^1) | DB: 7)
  * `renderPullBranchAction` (Impact: 26.6 | O(N^2) | DB: 3)
  * `renderViewStashAction` (Impact: 23.3 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 99`, `args: 51`, `func_start: 37`, `class_start: 3`
* *Risk/State:* `state_mutation: 160`
* *Architecture:* `io: 1`, `api: 6`, `concurrency: 6`, `import: 24`
* *Defense:* `safety: 6`, `doc: 11`, `immutability_locks: 64`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001248
  * `Imports (Out-Degree: 12):` remote, pull-request, tip, link-button, memoize-one, preferences, repository, react...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `app/src/lib/git/update-ref.ts` (TYPESCRIPT) | Magnitude: 3.41 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 18, doc: 10, concurrency: 10, decorators: 8
- `app/src/lib/actions-log-parser/actions-logs-ansii.ts` (TYPESCRIPT) | Magnitude: 2.13 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: branch: 24, structural_boundaries: 6, api: 6, immutability_locks: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `app/src/ui/dialog/header.tsx` (TYPESCRIPT) | Magnitude: 4.72 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 36, state_mutation: 30, ui_framework: 13, structural_boundaries: 7
- `app/src/ui/history/compare.tsx` (TYPESCRIPT) | Magnitude: 68.96 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 606, state_mutation: 317, ui_framework: 118, structural_boundaries: 107
- `app/src/ui/changes/changes.tsx` (TYPESCRIPT) | Magnitude: 10.11 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 95, state_mutation: 64, ui_framework: 34, structural_boundaries: 26
- `app/src/ui/lib/radio-group.tsx` (TYPESCRIPT) | Magnitude: 4.16 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 45, state_mutation: 17, structural_boundaries: 16, args: 10
- `app/src/lib/status.ts` (TYPESCRIPT) | Magnitude: 11.19 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 42, branch: 29, args: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `app/src/lib/editors/found-editor.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, immutability_locks: 2, indent_spaces: 2, class_start: 1
- `app/src/lib/progress/checkout.ts` (TYPESCRIPT) | Magnitude: 0.5 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, api: 3, indent_spaces: 3, args: 2
- `app/src/lib/progress/revert.ts` (TYPESCRIPT) | Magnitude: 0.5 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, api: 3, indent_spaces: 3, args: 2
- `app/src/lib/fuzzy-find.ts` (TYPESCRIPT) | Magnitude: 3.27 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 17, generics: 8, args: 7
- `app/src/lib/set-state.ts` (TYPESCRIPT) | Magnitude: 2.77 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 13, structural_boundaries: 7, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `app/src/ui/check-runs/ci-check-run-list.tsx` (TYPESCRIPT) | Magnitude: 13.48 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 126, state_mutation: 64, structural_boundaries: 30, branch: 26
- `app/src/ui/dropdown-select-button.tsx` (TYPESCRIPT) | Magnitude: 41.21 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 316, state_mutation: 174, branch: 66, structural_boundaries: 53
- `app/src/ui/lib/observable-ref.ts` (TYPESCRIPT) | Magnitude: 2.12 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 12, generics: 10, state_mutation: 9
- `app/src/ui/lib/augmented-filter-list.tsx` (TYPESCRIPT) | Magnitude: 84.21 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 599, state_mutation: 406, branch: 137, structural_boundaries: 134
- `app/src/ui/branches/group-branches.ts` (TYPESCRIPT) | Magnitude: 4.43 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 12, immutability_locks: 11, state_mutation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `app/src/ui/multi-commit-operation/choose-branch/choose-target-branch.tsx` (TYPESCRIPT) | Magnitude: 19.69 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 180, state_mutation: 95, structural_boundaries: 35, ui_framework: 33
- `app/src/ui/history/commit-list.tsx` (TYPESCRIPT) | Magnitude: 99.09 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 781, state_mutation: 449, branch: 164, structural_boundaries: 161
- `app/src/ui/editor/editor-error.tsx` (TYPESCRIPT) | Magnitude: 5.15 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 17, ui_framework: 14, state_mutation: 13
- `app/src/ui/lib/ref-name-text-box.tsx` (TYPESCRIPT) | Magnitude: 16.96 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 130, state_mutation: 78, ui_framework: 31, branch: 26
- `app/src/ui/preferences/custom-integration-form.tsx` (TYPESCRIPT) | Magnitude: 15.88 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 155, state_mutation: 69, ui_framework: 29, structural_boundaries: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `app/src/lib/hooks/get-shell.ts` (TYPESCRIPT) | Magnitude: 13.38 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 38, branch: 30, concurrency: 25
- `app/src/ui/lib/config-lock-file-exists.tsx` (TYPESCRIPT) | Magnitude: 3.09 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 12, structural_boundaries: 11, indent_spaces: 10, branch: 4
- `app/src/ui/stashing/stash-diff-header.tsx` (TYPESCRIPT) | Magnitude: 10.85 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 80, state_mutation: 38, concurrency: 24, structural_boundaries: 18
- `app/src/lib/git/diff-index.ts` (TYPESCRIPT) | Magnitude: 8.19 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 20, branch: 16, concurrency: 14
- `app/src/lib/directory-exists.ts` (TYPESCRIPT) | Magnitude: 1.06 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, io: 3, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `app/styles/_ui.scss` (CSS) | Magnitude: 0.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 113
- `app/src/main-process/shell.ts` (TYPESCRIPT) | Magnitude: 0.67 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 3, args: 2, io: 2
- `app/src/models/repository.ts` (TYPESCRIPT) | Magnitude: 2.91 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 19, api: 9, args: 6
- `app/test/e2e/playwright.config.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, io: 4, structural_boundaries: 3, import: 2
- `app/src/ui/multi-commit-operation/cherry-pick.tsx` (TYPESCRIPT) | Magnitude: 16.4 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 180, state_mutation: 54, concurrency: 31, structural_boundaries: 30

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `app/src/lib/stores/app-store.ts` -> Churn: **78.58%** | Cog Load: 89.3238% | Debt: 0.0%
- `app/src/lib/hooks/hooks-proxy.ts` -> Churn: **74.41%** | Cog Load: 57.5505% | Debt: 0.0%
- `script/build.ts` -> Churn: **66.3%** | Cog Load: 9.0041% | Debt: 73.7952%
- `app/src/ui/app.tsx` -> Churn: **65.73%** | Cog Load: 89.802% | Debt: 8.0209%
- `app/src/lib/stores/copilot-store.ts` -> Churn: **64.97%** | Cog Load: 57.4742% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `app/src/ui/diff/side-by-side-diff.tsx` -> **tidy-dev** (100.0% isolated ownership) | Magnitude: 98.78
- `app/src/ui/lib/list/list.tsx` -> **tidy-dev** (100.0% isolated ownership) | Magnitude: 97.95
- `app/src/ui/lib/section-filter-list.tsx` -> **tidy-dev** (100.0% isolated ownership) | Magnitude: 77.53
- `app/src/lib/api.ts` -> **Sergio Padrino** (88.9% isolated ownership) | Magnitude: 75.3
- `app/src/ui/diff/side-by-side-diff-row.tsx` -> **zeki** (100.0% isolated ownership) | Magnitude: 70.53

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `app/src/ui/dispatcher/dispatcher.ts` -> **Severity: 5.55** (Bridge: 0.0555 * Flux: 99.9645%)
- `app/src/lib/menu-update.ts` -> **Severity: 3.744** (Bridge: 0.05 * Flux: 74.877%)
- `app/src/ui/repository-settings/repository-settings.tsx` -> **Severity: 3.353** (Bridge: 0.0335 * Flux: 100.0%)
- `app/src/lib/stores/app-store.ts` -> **Severity: 3.041** (Bridge: 0.0358 * Flux: 84.9759%)
- `app/src/ui/dialog/dialog.tsx` -> **Severity: 1.739** (Bridge: 0.0238 * Flux: 73.0316%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `app/src/ui/dialog/ok-cancel-button-group.tsx` -> **Severity: 10.058** (Embedded: 0.1051 * Error Risk: 95.6528%)
- `app/src/ui/lib/link-button.tsx` -> **Severity: 8.942** (Embedded: 0.0964 * Error Risk: 92.7965%)
- `app/src/models/github-repository.ts` -> **Severity: 8.909** (Embedded: 0.1054 * Error Risk: 84.5365%)
- `app/src/ui/lib/tooltip.tsx` -> **Severity: 8.864** (Embedded: 0.0987 * Error Risk: 89.7735%)
- `app/src/lib/ipc-renderer.ts` -> **Severity: 8.835** (Embedded: 0.1104 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `app/src/ui/main-process-proxy.ts` -> **Severity: 1726.849** (Blast Radius: 17.297 * Doc Risk: 99.8352%)
- `app/src/lib/fatal-error.ts` -> **Severity: 1617.864** (Blast Radius: 16.35 * Doc Risk: 98.9519%)
- `app/src/models/github-repository.ts` -> **Severity: 1163.227** (Blast Radius: 11.644 * Doc Risk: 99.8993%)
- `app/src/ui/lib/observable-ref.ts` -> **Severity: 641.002** (Blast Radius: 7.322 * Doc Risk: 87.5447%)
- `app/src/lib/api.ts` -> **Severity: 518.668** (Blast Radius: 30.122 * Doc Risk: 17.2189%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
