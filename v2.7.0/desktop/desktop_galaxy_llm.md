# ARCHITECTURAL_BRIEF: desktop
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/desktop/desktop.git` |
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
| Total Artifacts | 2390 |
| Analyzed Artifacts (Scanned) | 1273 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1117 |
| Total LOC | 134467 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 53.3% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4702 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1652 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 13.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.4098 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 132 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 1010 | 122105 | 79.3% |
| CSS | 176 | 10894 | 13.8% |
| MARKDOWN | 30 | 0 | 2.4% |
| XML | 27 | 25 | 2.1% |
| JAVASCRIPT | 10 | 1053 | 0.8% |
| SHELL | 7 | 114 | 0.5% |
| JSON | 6 | 260 | 0.5% |
| PLAINTEXT | 5 | 1 | 0.4% |
| HTML | 1 | 10 | 0.1% |
| BATCH | 1 | 5 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1233 | 96.9% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 34 | 2.7% |
| Static: Minified & Vendor Opaque Mass | 5 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1117*

**Composition by Extension & Reason:**
- `no_extension`: 492x Excluded (Binary Format Detected), 332x Unsupported Format (.undeterminable), 115x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 65x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable), 1x Excluded (Saturation: Line 82 exceeds 500 chars)
- `.yml`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 4781 LOC)
- `.png`: 11x Excluded (Explicitly Denied Extension: '.png')
- `.sh`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.lock')
- `.gyp`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cpp`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.car`: 2x Excluded (Unsupported Extension: '.car')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.8 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.4 | 29.4 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 11.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 21.8 | 20.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 26.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 20.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 36.3 | 0.6 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 82.9 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.8 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 79.6 | 3.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 38.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 60.2 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 802 | 446 | 2 | `app/test/unit/text-token-parser-test.ts` |
| cleanup | 138 | 74 | 0 | `app/src/ui/lib/tooltip.tsx` |
| guards | 9607 | 679 | 18 | `app/src/lib/stores/app-store.ts` |
| danger | 765 | 269 | 2 | `app/src/lib/api.ts` |
| concurrency | 6433 | 416 | 10 | `app/src/lib/stores/app-store.ts` |
| connectivity | 4889 | 896 | 7 | `app/styles/_variables.scss` |
| io | 3089 | 404 | 6 | `app/test/unit/git/commit-test.ts` |
| crypto | 2 | 1 | 0 | `eslint-rules/tests/insecure-random.test.js` |
| ipc | 33 | 30 | 0 | `app/src/lib/highlighter/worker.ts` |
| time | 206 | 84 | 0 | `app/src/lib/stores/helpers/repository-indicator-updater.ts` |
| serialization | 45 | 28 | 0 | `app/test/unit/accounts-store-test.ts` |
| regex | 221 | 101 | 0 | `app/src/lib/hooks/shell-escape.ts` |
| events | 796 | 200 | 1 | `app/src/main-process/main.ts` |
| tests | 1762 | 131 | 2 | `app/test/unit/git/diff-test.ts` |
| docs | 5081 | 681 | 10 | `app/src/ui/dispatcher/dispatcher.ts` |
| debt | 211 | 88 | 0 | `script/build.ts` |
| mutation | 24241 | 919 | 44 | `app/src/lib/stores/app-store.ts` |
| dead_code | 162 | 85 | 0 | `app/src/highlighter/globals.d.ts` |
| credential | 1 | 1 | 0 | `app/src/ui/diff/diff-helpers.tsx` |
| threat | 36 | 16 | 0 | `app/src/main-process/ordered-webrequest.ts` |
| ml_ai | 117 | 47 | 0 | `app/src/lib/format-relative.ts` |
| ui | 8998 | 453 | 18 | `app/src/ui/app.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.8333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `app/test/unit/git/commit-test.ts` (Hits: 93)
- `app/src/ui/add-repository/create-repository.tsx` (Hits: 89)
- `app/src/lib/shells/win32.ts` (Hits: 87)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **repository.ts** (`app/src/models/repository.ts`) — 211 inbound connections
2. **path.ts** (`app/src/lib/path.ts`) — 132 inbound connections
3. **dialog.tsx** (`app/src/ui/dialog/dialog.tsx`) — 102 inbound connections
4. **dispatcher.ts** (`app/src/ui/dispatcher/dispatcher.ts`) — 100 inbound connections
5. **api.ts** (`app/src/lib/api.ts`) — 94 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **app.tsx** (`app/src/ui/app.tsx`) — 153 outbound dependencies
2. **app-store.ts** (`app/src/lib/stores/app-store.ts`) — 115 outbound dependencies
3. **_ui.scss** (`app/styles/_ui.scss`) — 113 outbound dependencies
4. **index.ts** (`app/src/highlighter/index.ts`) — 60 outbound dependencies
5. **dispatcher.ts** (`app/src/ui/dispatcher/dispatcher.ts`) — 60 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parse` (@ `app/src/lib/actions-log-parser/action-log-parser.ts`) -> Impact: **260.3** | LOC: 567
  * *Intent:* /** * Converts the content to HTML with appropriate styles, escapes content to prevent XSS * * @param content * @param lineNumber */
- `popupContent` (@ `app/src/ui/app.tsx`) -> Impact: **238.1** | LOC: 1159
- `showTestUI` (@ `app/src/ui/lib/test-ui-components/test-ui-components.ts`) -> Impact: **188.9** | LOC: 468
- `safeDirectoryName` (@ `app/src/ui/add-repository/create-repository.tsx`) -> Impact: **149.0** | LOC: 660
  * *Intent:* // We use this instead of sanitizedRepositoryName because it deals with // valid repository names on GitHub.com but here we only care about whether //...
- `buildDefaultMenu` (@ `app/src/main-process/menu/build-default-menu.ts`) -> Impact: **142.5** | LOC: 558
- `getStates` (@ `app/src/lib/actions-log-parser/action-log-parser.ts`) -> Impact: **136.9** | LOC: 192
  * *Intent:* /** * Parses the content into ANSII states * * @param content content to parse */
- `getDescriptionForError` (@ `app/src/lib/git/core.ts`) -> Impact: **133.4** | LOC: 140
- `onDismiss` (@ `app/src/ui/app.tsx`) -> Impact: **114.5** | LOC: 829
- `getNextPagePathFromLink` (@ `app/src/lib/api.ts`) -> Impact: **100.5** | LOC: 369
  * *Intent:* /** * Parses the Link header from GitHub and returns the 'next' path * if one is present. * * If no link rel next header is found this method returns ...
- `expandTextDiffHunk` (@ `app/src/ui/diff/text-diff-expansion.ts`) -> Impact: **94.8** | LOC: 231
  * *Intent:* /** * Expands a hunk in a text diff. Returns the new diff with the expanded hunk, * or undefined if anything went wrong. * * @param diff Original text...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `app/src/lib/stores` | 24 | 7927.48 | 29.92% | 4.83% |
| `app/src/lib/git` | 57 | 5252.14 | 39.77% | 2.12% |
| `app` | 8 | 5122.86 | 5.21% | 0.0% |
| `app/src/lib` | 102 | 4650.19 | 14.55% | 5.64% |
| `app/test/unit/git` | 35 | 4343.22 | 30.61% | 0.0% |
| `app/src/ui/lib` | 79 | 4180.6 | 11.94% | 1.93% |
| `app/test/unit` | 70 | 2996.7 | 5.72% | 0.0% |
| `app/src/ui` | 22 | 2536.4 | 17.35% | 2.01% |
| `app/src/ui/diff` | 16 | 2109.44 | 8.93% | 0.0% |
| `app/src/ui/dispatcher` | 3 | 2045.98 | 13.33% | 2.77% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `app/src/lib/stores/base-store.ts` -> **100.0%** Exposure
- `app/src/lib/globals.d.ts` -> **99.9955%** Exposure
- `app/src/highlighter/globals.d.ts` -> **99.928%** Exposure
- `app/styles/ui/_scroll.scss` -> **99.821%** Exposure
- `eslint-rules/no-loosely-typed-webcontents-ipc.js` -> **99.3307%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `app/src/lib/actions-log-parser/action-log-parser.ts` -> **100.0%** Exposure
- `app/src/lib/create-terminal-stream.ts` -> **100.0%** Exposure
- `app/src/lib/fix-emoji-spacing.ts` -> **100.0%** Exposure
- `app/src/lib/git/git-delimiter-parser.ts` -> **100.0%** Exposure
- `app/src/lib/git/update-index.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `app/src/highlighter/globals.d.ts` -> **20** Orphaned Functions | **0** Duplicates
- `app/src/lib/globals.d.ts` -> **7** Orphaned Functions | **0** Duplicates
- `app/src/lib/actions-log-parser/action-log-parser.ts` -> **4** Orphaned Functions | **0** Duplicates
- `app/src/lib/stores/base-store.ts` -> **0** Orphaned Functions | **4** Duplicates
- `script/build.ts` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `app/src/ui/diff/diff-helpers.tsx` -> **60.18%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1475` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `app/src/lib/hooks/hooks-proxy.ts` (TYPESCRIPT) -> Cumulative Risk: **703.31**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 93.94 | **LOC:** 207 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.7287%), State Flux (87.5854%)
- **Heaviest Functions:** `abort` (Impact: 31.2), `createHooksProxy` (Impact: 8.8), `tryExit` (Impact: 4.0)

### 2. `app/src/lib/shells/linux.ts` (TYPESCRIPT) -> Cumulative Risk: **645.98**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 198.3 | **LOC:** 258 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9976%), Safety Score (86.0085%)
- **Heaviest Functions:** `launch` (Impact: 38.5), `getShellPath` (Impact: 31.8), `getAvailableShells` (Impact: 24.9)

### 3. `app/src/lib/hooks/get-shell-env.ts` (TYPESCRIPT) -> Cumulative Risk: **638.61**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 68.24 | **LOC:** 92 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9969%), State Flux (99.8482%)
- **Heaviest Functions:** `getShellEnv` (Impact: 33.8)

### 4. `app/src/lib/git/submodule.ts` (TYPESCRIPT) -> Cumulative Risk: **638.09**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 108.84 | **LOC:** 198 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9997%), State Flux (95.4978%), Verification (80.0%)
- **Heaviest Functions:** `updateSubmodulesAfterOperation` (Impact: 33.1), `listSubmodules` (Impact: 11.3), `parse` (Impact: 6.6)

### 5. `app/src/lib/stores/app-store.ts` (TYPESCRIPT) -> Cumulative Risk: **637.97**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 4336.82 | **LOC:** 8730 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 48.5%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Verification (80.0%), Churn (79.56%)
- **Heaviest Functions:** `_recordCommitStats` (Impact: 49.0), `_undoMultiCommitOperation` (Impact: 44.1), `_mergeBranch` (Impact: 42.0)

### 6. `app/src/ui/repository-settings/repository-settings.tsx` (TYPESCRIPT) -> Cumulative Risk: **635.0**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 209.14 | **LOC:** 439 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (92.4809%)
- **Heaviest Functions:** `onSubmit` (Impact: 21.0), `componentWillMount` (Impact: 13.6), `renderActiveTab` (Impact: 13.1)

### 7. `app/src/lib/shells/win32.ts` (TYPESCRIPT) -> Cumulative Risk: **629.62**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 280.16 | **LOC:** 559 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9999%), Verification (80.0%)
- **Heaviest Functions:** `findHyper` (Impact: 89.0), `getAvailableShells` (Impact: 19.9), `findPowerShell` (Impact: 8.9)

### 8. `app/src/lib/trampoline/trampoline-environment.ts` (TYPESCRIPT) -> Cumulative Risk: **627.62**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 144.26 | **LOC:** 222 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9908%), State Flux (95.7191%), Verification (80.0%)
- **Heaviest Functions:** `withTrampolineEnv` (Impact: 39.0), `getCredentialUrl` (Impact: 22.2), `getHasRejectedCredentialsForEndpoint` (Impact: 7.6)

### 9. `app/src/main-process/ordered-webrequest.ts` (TYPESCRIPT) -> Cumulative Risk: **626.33**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 154.86 | **LOC:** 249 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.7653%)
- **Heaviest Functions:** `constructor` (Impact: 20.5), `addEventListener` (Impact: 3.3), `addEventListener` (Impact: 3.2)

### 10. `app/src/lib/git/commit.ts` (TYPESCRIPT) -> Cumulative Risk: **621.18**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 122.84 | **LOC:** 137 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 86.7%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9966%), Verification (80.0%)
- **Heaviest Functions:** `createCommit` (Impact: 45.4), `createMergeCommit` (Impact: 12.8)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/lib/stores/app-store.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4336.82 | **LOC:** 8730 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 48.5%
- **Risk Profile:** Cognitive Load (48.5127%), Tech Debt (7.8286%)
**Top Internal Functions/Classes:**
  * `_recordCommitStats` (Impact: 49.0)
  * `_undoMultiCommitOperation` (Impact: 44.1)
    * *Intent:* /** This shouldn't be called directly. See `Dispatcher`. */
  * `_mergeBranch` (Impact: 42.0)
  * `onGitStoreUpdated` (Impact: 40.1)
  * `_findPullRequestBranch` (Impact: 36.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 95 instances
* *Amplified Cascading Flux:* 134 instances
* *Concurrency (weighted view):* 1135
* *State Mutation (weighted view):* 496
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 809`, `structural_boundaries: 1270`, `args: 594`, `func_start: 356`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 228`, `dead_code: 12`, `planned_debt: 4`
* *Architecture:* `io: 61`, `api: 241`, `concurrency: 660`, `import: 115`
* *Defense:* `safety: 120`, `doc: 144`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.027183 | `Ripple Effect (Closeness):` 0.058454
  * `Imports (Out-Degree: 100):` , remote-parsing, account, app-menu, author, banner, branch, branches-tab...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/ui/dispatcher/dispatcher.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1821.44 | **LOC:** 4083 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (26.321%), Tech Debt (8.2978%)
**Top Internal Functions/Classes:**
  * `rebase` (Impact: 45.4)
    * *Intent:* /** Starts a rebase for the given base and target branch */
  * `performRetry` (Impact: 24.9)
    * *Intent:* /** Perform the given retry action. */
  * `getMultiCommitOperationSuccessBanner` (Impact: 24.3)
  * `processMultiCommitOperationRebaseResult` (Impact: 23.8)
    * *Intent:* /** * Processes the multi commit operation result * 1. Completes the operation with banner if succes...
  * `squash` (Impact: 23.4)
    * *Intent:* /** * Starts a squash * * @param toSquash - commits to squash onto another commit * @param squashOnt...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 377
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 625`, `args: 293`, `func_start: 276`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 28`, `dead_code: 3`, `planned_debt: 5`
* *Architecture:* `io: 37`, `api: 259`, `concurrency: 297`, `import: 60`
* *Defense:* `safety: 29`, `doc: 207`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.055
  * `Choke Point (Betweenness):` 0.054666 | `Ripple Effect (Closeness):` 0.066308
  * `Imports (Out-Degree: 54):` api, app-shell, app-state, ci-checks, cli-action, custom-integration, drag-and-drop-manager, fatal-error...
  * `Imported By (In-Degree: 100):` (Excluded from Brief to save tokens)

### `app/src/ui/app.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1239.98 | **LOC:** 3761 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (13.1108%), Tech Debt (7.9815%)
**Top Internal Functions/Classes:**
  * `popupContent` (Impact: 238.1)
  * `onDismiss` (Impact: 114.5)
  * `onMenuEvent` (Impact: 79.4)
  * `onWindowKeyDown` (Impact: 36.2)
    * *Intent:* /** * On Windows pressing the Alt key and holding it down should * highlight the application menu. *...
  * `renderRepositoryToolbarButton` (Impact: 18.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 438`, `structural_boundaries: 638`, `args: 175`, `func_start: 148`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 27`, `dead_code: 3`, `planned_debt: 3`
* *Architecture:* `io: 24`, `api: 12`, `concurrency: 34`, `import: 153`
* *Defense:* `safety: 19`, `doc: 25`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.405
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002357
  * `Imports (Out-Degree: 113):` api, app-shell, app-state, branch, clamp, commit-url, custom-integration, drag-and-drop-manager...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/lib/stores/git-store.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1072.02 | **LOC:** 1775 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (60.4444%), Tech Debt (8.0492%)
**Top Internal Functions/Classes:**
  * `discardChanges` (Impact: 35.2)
  * `loadCommitAndCoAuthors` (Impact: 29.4)
    * *Intent:* /** * Attempt to restore both the commit message and any co-authors * in it after an undo operation....
  * `fetch` (Impact: 21.8)
    * *Intent:* /** * Fetch the default, current, and upstream remotes, using the given account for * authentication...
  * `emitUpdatesForChangedTags` (Impact: 19.5)
    * *Intent:* /** * Calculates the commits that have changed based on the changes in existing tags * to emit the c...
  * `loadLocalCommits` (Impact: 16.3)
    * *Intent:* /** * Load local commits into memory for the current repository. * * @param branch The branch to que...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 35 instances
* *Amplified Cascading Flux:* 80 instances
* *Concurrency (weighted view):* 319
* *State Mutation (weighted view):* 254
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 274`, `args: 121`, `func_start: 71`, `class_start: 1`
* *Risk/State:* `state_mutation: 94`, `planned_debt: 1`
* *Architecture:* `io: 18`, `api: 61`, `concurrency: 144`, `import: 34`
* *Defense:* `safety: 19`, `doc: 51`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.628
  * `Choke Point (Betweenness):` 0.004238 | `Ripple Effect (Closeness):` 0.047445
  * `Imports (Out-Degree: 28):` git, author, branch, commit, commit-message, diff, git-author, progress...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/ui/diff/side-by-side-diff.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1028.1 | **LOC:** 2151 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.317%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `closestRow` (Impact: 34.3)
  * `getDiffRowsFromHunk` (Impact: 32.9)
    * *Intent:* /** * Returns an array of rows with the needed data to render a side-by-side diff * with them. * * I...
  * `getModifiedRows` (Impact: 31.2)
  * `onUpdateSelection` (Impact: 23.5)
  * `getDiscardLabel` (Impact: 23.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 287
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 305`, `structural_boundaries: 251`, `args: 96`, `func_start: 82`, `class_start: 5`
* *Risk/State:* `state_mutation: 107`
* *Architecture:* `api: 11`, `concurrency: 2`, `import: 22`
* *Defense:* `safety: 30`, `doc: 34`, `immutability_locks: 29`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.41
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001571
  * `Imports (Out-Degree: 11):` fatal-error, types, menu-item, diff, aria-live-container, diff-contents-warning, diff-explorer, diff-helpers...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `app/src/lib/actions-log-parser/action-log-parser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 997.28 | **LOC:** 741 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.3195%), Tech Debt (14.9349%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 260.3)
    * *Intent:* /** * Converts the content to HTML with appropriate styles, escapes content to prevent XSS * * @para...
  * `getStates` (Impact: 136.9)
    * *Intent:* /** * Parses the content into ANSII states * * @param content content to parse */
  * `parseLines` (Impact: 81.9)
    * *Intent:* /** * Parses the content into lines with nodes * * @param content content to parse */
  * `parseCommandEnd` (Impact: 59.5)
  * `updateLineMetaData` (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 129 instances
* *State Mutation (weighted view):* 401
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 36`, `args: 20`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 143`, `dead_code: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 1`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` action-log-pipeline-commands, actions-log-parser-objects, actions-logs-ansii
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/lib/api.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 868.38 | **LOC:** 2486 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 88.9%
- **Risk Profile:** Cognitive Load (13.5144%), Tech Debt (8.3155%)
**Top Internal Functions/Classes:**
  * `getNextPagePathFromLink` (Impact: 100.5)
    * *Intent:* /** * Parses the Link header from GitHub and returns the 'next' path * if one is present. * * If no ...
  * `copilotRequest` (Impact: 47.1)
    * *Intent:* /** * Make an authenticated request to the client's Copilot endpoint with its * token. Used for Copi...
  * `fetchAll` (Impact: 20.4)
    * *Intent:* /** * Authenticated requests to a paginating resource such as issues. * * Follows the GitHub API hyp...
  * `isGitHubHost` (Impact: 17.0)
    * *Intent:* /** * Attempts to determine whether or not the url belongs to a GitHub host. * * This is a best-effo...
  * `ghRequest` (Impact: 15.4)
    * *Intent:* /** * Make an authenticated request to the client's endpoint with its token. * Used for GitHub API r...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 197
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 372`, `args: 90`, `func_start: 71`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 15`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 79`, `api: 99`, `concurrency: 177`, `import: 12`
* *Defense:* `safety: 106`, `doc: 123`, `immutability_locks: 161`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.5
  * `Choke Point (Betweenness):` 0.032393 | `Ripple Effect (Closeness):` 0.151956
  * `Imports (Out-Degree: 9):` account, bypass-push-protection-dialog, copilot-commit-message, copilot-error, endpoint-capabilities, http, http-status-code, remote-parsing...
  * `Imported By (In-Degree: 94):` (Excluded from Brief to save tokens)

### `app/src/ui/lib/list/list.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 764.16 | **LOC:** 1758 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.7427%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onKeyDown` (Impact: 73.6)
  * `onRowMouseDown` (Impact: 62.3)
  * `getRowRenderer` (Impact: 28.6)
  * `onRowMouseUp` (Impact: 28.0)
  * `componentDidUpdate` (Impact: 27.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 42 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 156`, `args: 84`, `func_start: 54`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 48`, `dead_code: 2`
* *Architecture:* `io: 1`, `api: 12`, `concurrency: 1`, `import: 15`
* *Defense:* `safety: 25`, `doc: 56`, `immutability_locks: 51`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.748
  * `Choke Point (Betweenness):` 0.004308 | `Ripple Effect (Closeness):` 0.058626
  * `Imports (Out-Degree: 10):` equality, non-fatal-exception, range, drag-drop, focus-container, id-pool, list-item-insertion-overlay, list-row...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `app/src/ui/lib/list/section-list.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 755.42 | **LOC:** 1783 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.6494%), Tech Debt (8.0392%)
**Top Internal Functions/Classes:**
  * `onRowMouseDown` (Impact: 60.7)
  * `onKeyDown` (Impact: 46.9)
  * `getRowRenderer` (Impact: 28.6)
  * `componentDidUpdate` (Impact: 27.3)
  * `onRowMouseUp` (Impact: 26.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 159`, `args: 97`, `func_start: 63`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 48`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 13`, `concurrency: 1`, `import: 14`
* *Defense:* `safety: 26`, `doc: 46`, `immutability_locks: 43`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.488
  * `Choke Point (Betweenness):` 2e-05 | `Ripple Effect (Closeness):` 0.008557
  * `Imports (Out-Degree: 10):` equality, non-fatal-exception, range, drag-drop, focus-container, id-pool, list-item-insertion-overlay, list-row...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/ui/changes/commit-message.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 698.18 | **LOC:** 1820 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 55.6%
- **Risk Profile:** Cognitive Load (18.1282%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateRepoRulesCommitMessageFailures` (Impact: 43.9)
  * `componentDidUpdate` (Impact: 32.1)
  * `createCommit` (Impact: 26.9)
  * `renderBranchProtectionsRepoRulesCommitWarning` (Impact: 26.6)
  * `updateRepoRulesCommitAuthorFailures` (Impact: 23.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 35 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 211`, `args: 101`, `func_start: 76`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 47`, `dead_code: 2`
* *Architecture:* `io: 1`, `api: 8`, `concurrency: 16`, `import: 45`
* *Defense:* `safety: 39`, `doc: 23`, `immutability_locks: 68`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.443
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002175
  * `Imports (Out-Degree: 38):` app-state, email, endpoint-capabilities, fatal-error, feature-flag, format-commit-message, git, config...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `app/src/lib/markdown-filters/mention-filter.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 540.52 | **LOC:** 143 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.8197%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 13`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 1`, `doc: 5`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005616
  * `Imports (Out-Degree: 3):` github-repository, api, node-filter
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/test/unit/git/remote-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 507.29 | **LOC:** 197 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.1374%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Concurrency (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 73`, `args: 19`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 19`, `concurrency: 55`, `import: 8`
* *Defense:* `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` git, remote, find-default-remote, repository, repositories, dugite, node:assert, node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/test/unit/git/multi-operation-terminal-output-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 497.73 | **LOC:** 156 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.9701%), Tech Debt (0.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` git, multi-operation-terminal-output, node:assert, node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/lib/git/diff.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 497.16 | **LOC:** 853 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.6507%), Tech Debt (8.4971%)
**Top Internal Functions/Classes:**
  * `getImageDiff` (Impact: 32.9)
  * `getCommitRangeDiff` (Impact: 29.6)
    * *Intent:* /** * Render the difference between two commits for a file * */
  * `getWorkingDirectoryDiff` (Impact: 19.0)
    * *Intent:* /** * Render the diff for a file within the repository working directory. The file will be * compare...
  * `getCommitRangeChangedFiles` (Impact: 16.1)
  * `getMediaType` (Impact: 15.6)
    * *Intent:* /** * Map a given file extension to the related data URL media type */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 37 instances
* *Concurrency (weighted view):* 165
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 106`, `args: 30`, `func_start: 24`
* *Risk/State:* `state_mutation: 41`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 41`, `api: 11`, `concurrency: 55`, `import: 23`
* *Defense:* `safety: 7`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` diff, repository, status, diff-parser, fatal-error, feature-flag, get-old-path, status-parser...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/test/unit/git/cherry-pick-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 466.02 | **LOC:** 726 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.8149%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `makeConflictCommit` (Impact: 29.1)
  * `setup` (Impact: 18.7)
  * `addThreeMoreCommitsOntoFeatureBranch` (Impact: 3.2)
  * `getCommitOneLine` (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 37 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 371
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 211`, `args: 33`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23`, `unreferenced_by_name: 1`
* *Architecture:* `io: 29`, `concurrency: 186`, `import: 16`
* *Defense:* `safety: 5`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` git, cherry-pick, status, manual-conflict-resolution, progress, repository, status, git...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/test/unit/path-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 464.41 | **LOC:** 104 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.0404%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 33`, `args: 12`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `io: 7`, `concurrency: 21`, `import: 6`
* *Defense:* `safety: 4`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` path, fs, node:assert, node:test, os, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/lib/stores/repositories-store.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 455.74 | **LOC:** 742 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.6204%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_upsertGitHubRepository` (Impact: 48.2)
  * `putOwner` (Impact: 25.8)
  * `getPermissionsString` (Impact: 15.0)
  * `toGitHubRepository` (Impact: 14.2)
  * `addRepository` (Impact: 12.0)
    * *Intent:* /** * Add a new local repository. * * If a repository already exists with that path, it will be retu...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 172
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 117`, `args: 42`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `dead_code: 1`
* *Architecture:* `io: 13`, `api: 21`, `concurrency: 92`, `import: 11`
* *Defense:* `safety: 19`, `doc: 23`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.659
  * `Choke Point (Betweenness):` 0.001622 | `Ripple Effect (Closeness):` 0.053507
  * `Imports (Out-Degree: 11):` github-repository, owner, repository, workflow-preferences, api, repositories-database, equality, fatal-error...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `app/src/ui/changes/filter-changes-list.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 437.28 | **LOC:** 1544 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 63.6%
- **Risk Profile:** Cognitive Load (10.064%), Tech Debt (8.0194%)
**Top Internal Functions/Classes:**
  * `getDefaultContextMenu` (Impact: 32.8)
  * `renderChangedFile` (Impact: 32.6)
  * `onContextMenu` (Impact: 16.0)
  * `renderCommitMessageForm` (Impact: 13.5)
  * `getPlaceholderMessage` (Impact: 13.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 242`, `args: 122`, `func_start: 84`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 22`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 35`, `api: 7`, `concurrency: 1`, `import: 50`
* *Defense:* `safety: 4`, `doc: 22`, `immutability_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.731
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003273
  * `Imports (Out-Degree: 34):` app-shell, app-state, equality, fuzzy-find, git, menu-item, path, status...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `app/src/lib/git/core.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 415.3 | **LOC:** 609 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (29.8207%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getDescriptionForError` (Impact: 133.4)
  * `git` (Impact: 81.9)
  * `push` (Impact: 40.4)
  * `constructor` (Impact: 19.4)
  * `isGitError` (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 141`, `args: 26`, `func_start: 14`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 18`
* *Architecture:* `io: 14`, `api: 27`, `concurrency: 9`, `import: 10`
* *Defense:* `safety: 38`, `doc: 24`, `sync_locks: 3`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.323
  * `Choke Point (Betweenness):` 0.015358 | `Ripple Effect (Closeness):` 0.078081
  * `Imports (Out-Degree: 8):` git-perf, errno-exception, fatal-error, with-hooks-env, trampoline-environment, coerce-to-string, push-terminal-chunk, buffer...
  * `Imported By (In-Degree: 47):` (Excluded from Brief to save tokens)

### `app/src/ui/history/commit-list.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 407.98 | **LOC:** 1046 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.3283%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getContextMenuForSingleCommit` (Impact: 67.7)
  * `onDropDataInsertion` (Impact: 38.3)
  * `onRowContextMenu` (Impact: 11.9)
  * `renderRowFocusTooltip` (Impact: 11.7)
  * `render` (Impact: 11.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 181`, `args: 92`, `func_start: 54`, `class_start: 3`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `io: 1`, `api: 5`, `import: 27`
* *Defense:* `safety: 22`, `doc: 39`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.554
  * `Choke Point (Betweenness):` 0.01109 | `Ripple Effect (Closeness):` 0.062628
  * `Imports (Out-Degree: 19):` api, emoji, equality, fatal-error, format-date, menu-item, account, avatar...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/src/lib/stats/stats-store.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 400.16 | **LOC:** 1248 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.1883%), Tech Debt (9.5765%)
**Top Internal Functions/Classes:**
  * `getDailyStats` (Impact: 19.0)
    * *Intent:* /** Get the daily stats. */
  * `reportStats` (Impact: 14.2)
    * *Intent:* /** Report any stats which are eligible for reporting. */
  * `recordOperationConflictsEncounteredCount` (Impact: 12.4)
  * `recordOperationSuccessful` (Impact: 12.4)
  * `recordOperationSuccessfulWithConflicts` (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 95
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 167`, `args: 78`, `func_start: 63`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 10`, `api: 43`, `concurrency: 60`, `import: 25`
* *Defense:* `safety: 8`, `doc: 61`, `immutability_locks: 32`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.366
  * `Choke Point (Betweenness):` 0.016285 | `Ripple Effect (Closeness):` 0.062891
  * `Imports (Out-Degree: 21):` merge, account, multi-commit-operation, repository, app-proxy, application-theme, diff-mode, ui-activity-monitor...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `app/test/unit/git/commit-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 375.88 | **LOC:** 915 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (47.5208%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setup` (Impact: 18.1)
  * `getTextDiff` (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 26 instances
* *Concurrency (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 237`, `args: 52`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 14`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 93`, `concurrency: 198`, `import: 14`
* *Defense:* `safety: 9`, `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` git, status, diff, manual-conflict-resolution, repository, status, path-exists, repositories...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/src/lib/git/rebase.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 372.92 | **LOC:** 628 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.7343%), Tech Debt (15.2032%)
**Top Internal Functions/Classes:**
  * `continueRebase` (Impact: 56.5)
    * *Intent:* /** * Proceed with the current rebase operation and report back on whether it completed * * It is ex...
  * `rebaseInteractive` (Impact: 45.4)
    * *Intent:* /** * Method for initiating interactive rebase in the app. * * In order to modify the interactive to...
  * `getRebaseSnapshot` (Impact: 23.8)
    * *Intent:* /** * Inspect the `.git/rebase-merge` folder and convert the current rebase state * into data that c...
  * `rebase` (Impact: 13.4)
    * *Intent:* /** * A stub function to use for initiating rebase in the app. * * If the rebase fails, the reposito...
  * `parse` (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 100
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 96`, `args: 19`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 26`, `dead_code: 1`, `planned_debt: 6`
* *Architecture:* `io: 25`, `api: 11`, `concurrency: 35`, `import: 20`
* *Defense:* `safety: 27`, `doc: 19`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.419
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000786
  * `Imports (Out-Degree: 13):` branch, commit, manual-conflict-resolution, progress, rebase, repository, status, path-exists...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/src/ui/lib/tooltip.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 368.86 | **LOC:** 842 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.2507%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getTooltipRectRelativeTo` (Impact: 23.6)
  * `getDirection` (Impact: 23.3)
  * `componentDidUpdate` (Impact: 18.8)
  * `onTooltipRef` (Impact: 17.3)
  * `fits` (Impact: 15.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 69`, `args: 43`, `func_start: 41`, `class_start: 4`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `api: 12`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 12`, `doc: 29`, `immutability_locks: 27`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.288
  * `Choke Point (Betweenness):` 0.000541 | `Ripple Effect (Closeness):` 0.100021
  * `Imports (Out-Degree: 4):` fatal-error, id-pool, observable-ref, rect, classnames, react, react-dom
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `app/src/lib/hooks/hooks-proxy.ts` -> Churn: **75.33%** | Cog Load: 77.1519% | Debt: 0.0%
- `app/src/lib/git/commit.ts` -> Churn: **59.59%** | Cog Load: 75.3655% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `app/src/ui/diff/side-by-side-diff.tsx` -> **tidy-dev** (100.0% isolated ownership) | Magnitude: 1028.1
- `app/src/lib/api.ts` -> **Sergio Padrino** (88.9% isolated ownership) | Magnitude: 868.38
- `app/src/lib/markdown-filters/mention-filter.ts` -> **Markus Olsson** (100.0% isolated ownership) | Magnitude: 540.52
- `app/test/unit/git/multi-operation-terminal-output-test.ts` -> **Markus Olsson** (100.0% isolated ownership) | Magnitude: 497.73
- `app/test/unit/git/cherry-pick-test.ts` -> **Markus Olsson** (100.0% isolated ownership) | Magnitude: 466.02

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `app/src/lib/menu-update.ts` -> **Severity: 3.695** (Bridge: 0.0389 * Flux: 94.9147%)
- `app/src/ui/repository-settings/repository-settings.tsx` -> **Severity: 2.939** (Bridge: 0.0318 * Flux: 92.4809%)
- `app/src/ui/dialog/dialog.tsx` -> **Severity: 1.894** (Bridge: 0.0238 * Flux: 79.7283%)
- `app/src/lib/stores/app-store.ts` -> **Severity: 1.47** (Bridge: 0.0272 * Flux: 54.0705%)
- `app/src/ui/main-process-proxy.ts` -> **Severity: 1.188** (Bridge: 0.0474 * Flux: 25.0555%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `app/src/lib/http.ts` -> **Severity: 9.181** (Embedded: 0.1227 * Error Risk: 74.8501%)
- `app/src/lib/ipc-renderer.ts` -> **Severity: 8.608** (Embedded: 0.1033 * Error Risk: 83.361%)
- `app/src/ui/lib/app-proxy.ts` -> **Severity: 7.816** (Embedded: 0.1191 * Error Risk: 65.6041%)
- `app/src/models/repository.ts` -> **Severity: 7.808** (Embedded: 0.1612 * Error Risk: 48.4312%)
- `app/src/ui/lib/id-pool.ts` -> **Severity: 7.748** (Embedded: 0.1146 * Error Risk: 67.6371%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `app/src/ui/dialog/dialog.tsx` -> **Severity: 734.184** (Blast Radius: 9.114 * Doc Risk: 80.5556%)
- `app/src/ui/lib/tooltip.tsx` -> **Severity: 684.18** (Blast Radius: 7.288 * Doc Risk: 93.8776%)
- `app/src/ui/dialog/ok-cancel-button-group.tsx` -> **Severity: 491.572** (Blast Radius: 5.735 * Doc Risk: 85.7143%)
- `app/src/lib/api.ts` -> **Severity: 454.287** (Blast Radius: 26.5 * Doc Risk: 17.1429%)
- `app/src/ui/lib/observable-ref.ts` -> **Severity: 416.85** (Blast Radius: 8.337 * Doc Risk: 50.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
