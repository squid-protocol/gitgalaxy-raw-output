# ARCHITECTURAL_BRIEF: zls
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/zigtools/zls.git` |
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
| Total Artifacts | 134 |
| Analyzed Artifacts (Scanned) | 117 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17 |
| Total LOC | 49370 |
| Volatility Index | 0.043 |
| % Scanned of codebase = | 87.3% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4396 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5606 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 9.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3403 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 103 | 48833 | 88.0% |
| JSON | 10 | 451 | 8.5% |
| MARKDOWN | 2 | 0 | 1.7% |
| YAML | 1 | 11 | 0.9% |
| NIX | 1 | 75 | 0.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 115 | 98.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 1.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 17*

**Composition by Extension & Reason:**
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zig`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zon`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.nix`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.in`: 1x Excluded (Saturation: Line 9 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 40.3 | 6.6 | 3.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 20.5 | 11.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 31.3 | 2.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 21.2 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 46.9 | 1.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 35.4 | 1.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 79.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 14.2 | 2.1 | 0.8 | 0.1 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 27.2 | 19.9 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 61.2 | 84.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2453 | 84 | 58 | `src/analysis.zig` |
| cleanup | 696 | 57 | 13 | `src/DocumentStore.zig` |
| guards | 8671 | 78 | 165 | `src/analysis.zig` |
| danger | 1236 | 75 | 28 | `src/analyser/InternPool.zig` |
| concurrency | 193 | 15 | 2 | `src/analyser/InternPool.zig` |
| connectivity | 983 | 72 | 22 | `src/analysis.zig` |
| io | 2 | 1 | 0 | `src/build_runner/shared.zig` |
| crypto | 0 | 0 | 0 | - |
| ipc | 4 | 3 | 0 | `src/build_runner/shared.zig` |
| time | 0 | 0 | 0 | - |
| serialization | 4 | 3 | 0 | `src/DocumentStore.zig` |
| regex | 0 | 0 | 0 | - |
| events | 35 | 14 | 1 | `tests/analysis_check.zig` |
| tests | 842 | 35 | 21 | `tests/lsp_features/completion.zig` |
| docs | 1198 | 59 | 32 | `src/analyser/InternPool.zig` |
| debt | 238 | 47 | 6 | `src/analyser/InternPool.zig` |
| mutation | 9431 | 104 | 171 | `src/analysis.zig` |
| dead_code | 119 | 39 | 3 | `tests/analysis/capture.zig` |
| credential | 0 | 0 | 0 | - |
| threat | 80 | 21 | 2 | `src/configuration.zig` |
| ml_ai | 258 | 29 | 3 | `src/analyser/InternPool.zig` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.6667**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/build_runner/shared.zig` (Hits: 2)
- `README.md` (Hits: 0)
- `src/analyser/README.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **zls.zig** (`src/zls.zig`) — 24 inbound connections
2. **offsets.zig** (`src/offsets.zig`) — 22 inbound connections
3. **tracy.zig** (`src/tracy.zig`) — 17 inbound connections
4. **DocumentStore.zig** (`src/DocumentStore.zig`) — 15 inbound connections
5. **context.zig** (`tests/context.zig`) — 14 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **zls.zig** (`src/zls.zig`) — 33 outbound dependencies
2. **Server.zig** (`src/Server.zig`) — 27 outbound dependencies
3. **tests.zig** (`tests/tests.zig`) — 19 outbound dependencies
4. **DocumentStore.zig** (`src/DocumentStore.zig`) — 13 outbound dependencies
5. **completions.zig** (`src/features/completions.zig`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `resolveTypeOfNodeUncached` (@ `src/analysis.zig`) -> Impact: **442.6** | LOC: 1092
- `main` (@ `src/build_runner/build_runner.zig`) -> Impact: **269.3** | LOC: 437
- `resolvePeerTypes` (@ `src/analyser/InternPool.zig`) -> Impact: **234.8** | LOC: 495
- `resolveExpressionTypeFromAncestors` (@ `src/analysis.zig`) -> Impact: **211.3** | LOC: 424
- `writeNodeTokens` (@ `src/features/semantic_tokens.zig`) -> Impact: **193.1** | LOC: 675
- `getFieldAccessType` (@ `src/analysis.zig`) -> Impact: **167.3** | LOC: 215
- `initializeHandler` (@ `src/Server.zig`) -> Impact: **160.2** | LOC: 244
- `getSignatureInfo` (@ `src/features/signature_help.zig`) -> Impact: **137.5** | LOC: 252
- `lastToken` (@ `src/ast.zig`) -> Impact: **126.2** | LOC: 410
  * *Intent:* /// Similar to `std.zig.Ast.lastToken` but also handles ASTs with syntax errors.
- `getSwitchOrStructInitContext` (@ `src/features/completions.zig`) -> Impact: **122.7** | LOC: 213
  * *Intent:* /// Looks for an identifier that can be passed to `collectContainerNodes()` /// Returns the token index of the identifier /// If the identifier is a `...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 20 | 7468.74 | 11.99% | 4.53% |
| `tests/utility` | 3 | 5731.91 | 3.28% | 0.0% |
| `src/features` | 13 | 3153.72 | 17.04% | 7.51% |
| `src/analyser` | 8 | 2228.5 | 8.21% | 4.22% |
| `src/build_runner` | 3 | 1071.28 | 18.32% | 2.78% |
| `tests/lsp_features` | 13 | 866.06 | 2.97% | 0.0% |
| `tests` | 9 | 528.88 | 4.16% | 0.0% |
| `tests/analysis` | 25 | 429.12 | 2.67% | 0.0% |
| `tests/build_runner_cases` | 16 | 148.76 | 0.0% | 0.0% |
| `__monolith__` | 4 | 50.58 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/features/workspace_symbols.zig` -> **31.2669%** Exposure
- `src/features/diagnostics.zig` -> **19.5206%** Exposure
- `src/DocumentStore.zig` -> **19.0318%** Exposure
- `src/DocumentScope.zig` -> **16.8973%** Exposure
- `src/analyser/segmented_list.zig` -> **13.2708%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/analyser/segmented_list.zig` -> **99.9892%** Exposure
- `src/tools/config_gen.zig` -> **98.5157%** Exposure
- `src/ast.zig` -> **98.3683%** Exposure
- `src/build_runner/build_runner.zig` -> **98.2542%** Exposure
- `src/features/signature_help.zig` -> **95.5794%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/analysis/capture.zig` -> **12** Orphaned Functions | **0** Duplicates
- `tests/analysis/assign_destructure.zig` -> **7** Orphaned Functions | **0** Duplicates
- `tests/analysis/optional.zig` -> **7** Orphaned Functions | **0** Duplicates
- `tests/analysis/either.zig` -> **3** Orphaned Functions | **2** Duplicates
- `tests/analysis/generics.zig` -> **5** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `296` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/ast.zig` (ZIG) -> Cumulative Risk: **611.75**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 856.42 | **LOC:** 1847 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 77.8%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.3683%), Documentation (84.9057%), Api Exposure (83.2961%)
- **Heaviest Functions:** `lastToken` (Impact: 126.2), `indexOfBreakTarget` (Impact: 45.8), `fullPtrTypeComponents` (Impact: 37.1)

### 2. `src/analyser/segmented_list.zig` (ZIG) -> Cumulative Risk: **562.81**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 343.32 | **LOC:** 444 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9892%), Safety Score (88.826%), Verification (80.0%)
- **Heaviest Functions:** `SegmentedList` (Impact: 82.4), `BaseIterator` (Impact: 24.1), `shrinkCapacity` (Impact: 11.6)

### 3. `src/TrigramStore.zig` (ZIG) -> Cumulative Risk: **508.14**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 195.04 | **LOC:** 695 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (89.1892%), State Flux (87.5209%), Verification (80.0%)
- **Heaviest Functions:** `isVarDeclAlias` (Impact: 15.0), `mergeIntersection` (Impact: 13.5), `next` (Impact: 11.1)

### 4. `src/analysis.zig` (ZIG) -> Cumulative Risk: **503.68**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2970.68 | **LOC:** 7016 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 45.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Api Exposure (88.4986%), Documentation (84.1317%)
- **Heaviest Functions:** `resolveTypeOfNodeUncached` (Impact: 442.6), `resolveExpressionTypeFromAncestors` (Impact: 211.3), `getFieldAccessType` (Impact: 167.3)

### 5. `src/configuration.zig` (ZIG) -> Cumulative Risk: **500.82**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 159.7 | **LOC:** 778 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 73.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (76.5323%), Churn (67.45%)
- **Heaviest Functions:** `eql` (Impact: 21.0), `free` (Impact: 20.9), `deinit` (Impact: 6.2)

### 6. `src/testing.zig` (ZIG) -> Cumulative Risk: **495.9**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 92.92 | **LOC:** 281 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (90.0%), State Flux (84.1282%), Verification (80.0%)
- **Heaviest Functions:** `renderLineDiff` (Impact: 9.8), `printDocumentScope` (Impact: 8.7), `printLine` (Impact: 6.0)

### 7. `src/features/completions.zig` (ZIG) -> Cumulative Risk: **494.11**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1099.88 | **LOC:** 1872 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 69.2%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (94.8423%), Documentation (91.3043%), Churn (89.73%)
- **Heaviest Functions:** `getSwitchOrStructInitContext` (Impact: 122.7), `completeFileSystemStringLiteral` (Impact: 119.8), `declToCompletion` (Impact: 103.1)

### 8. `src/features/code_actions.zig` (ZIG) -> Cumulative Risk: **473.7**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 319.5 | **LOC:** 1230 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Documentation (80.0%), Api Exposure (60.4435%)
- **Heaviest Functions:** `getDiscardLoc` (Impact: 29.7), `parse` (Impact: 22.4), `getParamRemovalRange` (Impact: 17.4)

### 9. `src/tracy.zig` (ZIG) -> Cumulative Risk: **464.79**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 245.54 | **LOC:** 344 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Api Exposure (91.8508%), Verification (80.0%)
- **Heaviest Functions:** `TracyAllocator` (Impact: 20.9), `resizeFn` (Impact: 10.4), `remapFn` (Impact: 10.4)

### 10. `src/Uri.zig` (ZIG) -> Cumulative Risk: **464.02**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 146.7 | **LOC:** 579 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (86.1131%), Verification (80.0%), Api Exposure (63.7102%)
- **Heaviest Functions:** `normalizePercentEncoded` (Impact: 15.8), `isFileScheme` (Impact: 6.0), `isSchemeChar` (Impact: 4.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/utility/position_context.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5711.57 | **LOC:** 768 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (4.3038%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 91`, `args: 30`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 7`, `state_mutation: 5`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `import: 9`
* *Defense:* `safety: 200`, `doc: 6`, `test: 35`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.591
  * `Choke Point (Betweenness):` 0.000116 | `Ripple Effect (Closeness):` 0.008621
  * `Imports (Out-Degree: 3):` ErrorBuilder.zig, helper.zig, std, zls
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/analysis.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2970.68 | **LOC:** 7016 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 45.0%
- **Risk Profile:** Cognitive Load (24.431%), Tech Debt (8.7198%)
**Top Internal Functions/Classes:**
  * `resolveTypeOfNodeUncached` (Impact: 442.6)
  * `resolveExpressionTypeFromAncestors` (Impact: 211.3)
  * `getFieldAccessType` (Impact: 167.3)
  * `eql` (Impact: 75.5)
  * `resolveType` (Impact: 74.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 150 instances
* *Memory Alloc (weighted view):* 20
* *State Mutation (weighted view):* 463
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1357`, `structural_boundaries: 1369`, `args: 197`, `func_start: 197`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 163`, `dead_code: 9`, `planned_debt: 15`, `fragile_debt: 1`
* *Architecture:* `api: 168`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 1439`, `doc: 111`, `test: 1`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.472
  * `Choke Point (Betweenness):` 0.009267 | `Ripple Effect (Closeness):` 0.211207
  * `Imports (Out-Degree: 7):` DocumentScope.zig, DocumentStore.zig, Uri.zig, InternPool.zig, error_msg.zig, ast.zig, builtin, references.zig...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/analyser/InternPool.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1667.6 | **LOC:** 5361 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 58.8%
- **Risk Profile:** Cognitive Load (7.6095%), Tech Debt (10.627%)
**Top Internal Functions/Classes:**
  * `resolvePeerTypes` (Impact: 234.8)
  * `printInternal` (Impact: 107.7)
  * `coerce` (Impact: 102.3)
    * *Intent:* // --------------------------------------------- // UTILITY // -------------------------------------...
  * `eqlCustom` (Impact: 94.4)
  * `coerceInMemoryAllowed` (Impact: 64.8)
    * *Intent:* /// If types have the same representation in runtime memory /// * int/float: same number of bits ///...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 47 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 455`, `structural_boundaries: 573`, `args: 134`, `func_start: 113`, `class_start: 68`
* *Risk/State:* `safety_bypasses: 114`, `high_risk_execution: 2`, `state_mutation: 59`, `dead_code: 5`, `planned_debt: 32`
* *Architecture:* `api: 130`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 1050`, `doc: 166`, `test: 48`, `sync_locks: 80`, `cleanup: 63`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.644
  * `Choke Point (Betweenness):` 0.00481 | `Ripple Effect (Closeness):` 0.157253
  * `Imports (Out-Degree: 3):` builtin, error_msg.zig, segmented_list.zig, std, string_pool.zig
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/features/completions.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1099.88 | **LOC:** 1872 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 69.2%
- **Risk Profile:** Cognitive Load (40.2536%), Tech Debt (9.396%)
**Top Internal Functions/Classes:**
  * `getSwitchOrStructInitContext` (Impact: 122.7)
    * *Intent:* /// Looks for an identifier that can be passed to `collectContainerNodes()` /// Returns the token in...
  * `completeFileSystemStringLiteral` (Impact: 119.8)
    * *Intent:* /// Asserts that `pos_context` is one of the following: /// - `.import_string_literal` /// - `.cincl...
  * `declToCompletion` (Impact: 103.1)
  * `collectContainerFields` (Impact: 94.4)
    * *Intent:* /// Given a Type that is a container, adds it's `.container_field*`s to completions
  * `getEnumLiteralContext` (Impact: 47.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 419`, `structural_boundaries: 263`, `args: 40`, `func_start: 40`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 79`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 8`, `import: 13`
* *Defense:* `safety: 309`, `doc: 22`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.86
  * `Choke Point (Betweenness):` 0.004307 | `Ripple Effect (Closeness):` 0.14238
  * `Imports (Out-Degree: 9):` DocumentScope.zig, DocumentStore.zig, Server.zig, Uri.zig, completions.zig, analysis.zig, ast.zig, offsets.zig...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/build_runner/build_runner.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 980.36 | **LOC:** 1503 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 74.1%
- **Risk Profile:** Cognitive Load (38.5185%), Tech Debt (8.3406%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 269.3)
  * `extractBuildInformation` (Impact: 115.4)
  * `runPkgConfig` (Impact: 70.5)
    * *Intent:* /// Run pkg-config for the given library name and parse the output, returning the arguments /// that...
  * `makeStep` (Impact: 44.6)
    * *Intent:* /// Runs the "make" function of the single step `s`, updates its state, and then spawns newly-ready ...
  * `processPkgConfig` (Impact: 28.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 63 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 195
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 162`, `args: 31`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 9`, `state_mutation: 69`, `dead_code: 7`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `concurrency: 5`, `import: 5`
* *Defense:* `safety: 252`, `doc: 49`, `sync_locks: 5`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.394
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` @build, @dependencies, builtin, shared.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Server.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 919.0 | **LOC:** 2030 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 79.3%
- **Risk Profile:** Cognitive Load (13.9226%), Tech Debt (10.3801%)
**Top Internal Functions/Classes:**
  * `initializeHandler` (Impact: 160.2)
  * `handleResponse` (Impact: 35.1)
  * `validateMessage` (Impact: 26.4)
  * `codeActionHandler` (Impact: 22.1)
  * `processMessageReportError` (Impact: 22.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 33 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 39 instances
* *Concurrency (weighted view):* 6
* *Memory Alloc (weighted view):* 33
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 294`, `args: 71`, `func_start: 71`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 49`, `planned_debt: 11`
* *Architecture:* `api: 17`, `concurrency: 1`, `import: 28`
* *Defense:* `safety: 330`, `doc: 56`, `cleanup: 47`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.907
  * `Choke Point (Betweenness):` 0.005082 | `Ripple Effect (Closeness):` 0.14962
  * `Imports (Out-Degree: 12):` Config.zig, DiagnosticsCollection.zig, DocumentStore.zig, Uri.zig, analyser.zig, analysis.zig, build_options, shared.zig...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/ast.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 856.42 | **LOC:** 1847 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 77.8%
- **Risk Profile:** Cognitive Load (33.2982%), Tech Debt (8.1409%)
**Top Internal Functions/Classes:**
  * `lastToken` (Impact: 126.2)
    * *Intent:* /// Similar to `std.zig.Ast.lastToken` but also handles ASTs with syntax errors.
  * `indexOfBreakTarget` (Impact: 45.8)
  * `fullPtrTypeComponents` (Impact: 37.1)
  * `next` (Impact: 32.1)
  * `next` (Impact: 28.7)
    * *Intent:* /// Iterates over FnProto Params w/ added bounds check to support incomplete ast nodes
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 83 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 219`, `args: 56`, `func_start: 56`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 99`, `dead_code: 4`, `planned_debt: 2`
* *Architecture:* `api: 52`, `concurrency: 4`, `import: 2`
* *Defense:* `safety: 120`, `doc: 34`, `test: 9`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.394
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` offsets.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/DocumentStore.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 539.28 | **LOC:** 2059 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 90.5%
- **Risk Profile:** Cognitive Load (11.5634%), Tech Debt (19.0318%)
**Top Internal Functions/Classes:**
  * `createAndStoreDocument` (Impact: 38.9)
    * *Intent:* /// **Thread safe** takes an exclusive lock
  * `invalidateBuildFileWorker` (Impact: 32.4)
  * `loadBuildConfiguration` (Impact: 16.4)
    * *Intent:* /// Runs the build.zig and extracts include directories and packages
  * `loadDirectoryRecursive` (Impact: 15.1)
  * `publishCimportDiagnostics` (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 47 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 19
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 372`, `args: 59`, `func_start: 59`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 49`, `dead_code: 1`, `planned_debt: 12`, `duplicate_logic: 2`
* *Architecture:* `api: 45`, `concurrency: 14`, `import: 16`
* *Defense:* `safety: 323`, `doc: 101`, `sync_locks: 33`, `cleanup: 100`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.285
  * `Choke Point (Betweenness):` 0.008293 | `Ripple Effect (Closeness):` 0.217241
  * `Imports (Out-Degree: 10):` BuildAssociatedConfig.zig, DiagnosticsCollection.zig, DocumentScope.zig, TrigramStore.zig, Uri.zig, analysis.zig, shared.zig, builtin...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/features/semantic_tokens.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 394.82 | **LOC:** 1200 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (15.238%), Tech Debt (8.0916%)
**Top Internal Functions/Classes:**
  * `writeNodeTokens` (Impact: 193.1)
  * `writeIdentifier` (Impact: 23.2)
  * `writeFieldAccess` (Impact: 22.1)
  * `writeVarDecl` (Impact: 21.2)
  * `writeContainerField` (Impact: 17.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 55`, `args: 15`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 15`, `planned_debt: 1`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 323`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.394
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` DocumentStore.zig, analysis.zig, ast.zig, offsets.zig, lsp, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/analyser/segmented_list.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 343.32 | **LOC:** 444 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.4937%), Tech Debt (13.2708%)
**Top Internal Functions/Classes:**
  * `SegmentedList` (Impact: 82.4)
    * *Intent:* /// This is a stack data structure where pointers to indexes have the same lifetime as the data stru...
  * `BaseIterator` (Impact: 24.1)
  * `shrinkCapacity` (Impact: 11.6)
    * *Intent:* /// Only shrinks capacity or retains current capacity. /// It may fail to reduce the capacity in whi...
  * `writeToSlice` (Impact: 11.2)
  * `growCapacity` (Impact: 11.1)
    * *Intent:* /// Only grows capacity, or retains current capacity.
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 11 instances
* *Amplified Cascading Flux:* 23 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 50`, `args: 31`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 35`, `planned_debt: 3`
* *Architecture:* `api: 26`, `import: 1`
* *Defense:* `safety: 11`, `doc: 25`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.363
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.116829
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/features/code_actions.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 319.5 | **LOC:** 1230 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.5846%), Tech Debt (8.5722%)
**Top Internal Functions/Classes:**
  * `getDiscardLoc` (Impact: 29.7)
    * *Intent:* /// takes the location of an identifier which is part of a discard `_ = location_here;` /// and retu...
  * `parse` (Impact: 22.4)
  * `getParamRemovalRange` (Impact: 17.4)
  * `lessThan` (Impact: 15.1)
  * `detectIndentation` (Impact: 13.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 211`, `structural_boundaries: 209`, `args: 38`, `func_start: 38`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 19`, `dead_code: 7`, `planned_debt: 2`
* *Architecture:* `api: 28`, `import: 10`
* *Defense:* `safety: 143`, `doc: 21`, `test: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.394
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` DocumentScope.zig, DocumentStore.zig, analysis.zig, ast.zig, offsets.zig, lsp, std, tracy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/offsets.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 314.44 | **LOC:** 806 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (6.5888%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sourceIndexToTokenIndex` (Impact: 28.8)
  * `identifierIndexToLoc` (Impact: 25.2)
    * *Intent:* /// The source index must be at the start of the valid identifier. /// /// Supported formats: /// - ...
  * `tokenToLoc` (Impact: 15.8)
  * `multilineLocAtIndex` (Impact: 15.3)
    * *Intent:* /// return the source location /// that starts `n` lines before the line at which `index` is located...
  * `pickTokenTag` (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 10 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 104`, `args: 42`, `func_start: 42`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 11`
* *Architecture:* `api: 70`, `import: 3`
* *Defense:* `safety: 141`, `doc: 42`, `test: 68`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 58.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.273444
  * `Imports (Out-Degree: 0):` ast.zig, lsp, std
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `tests/lsp_features/completion.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 308.04 | **LOC:** 5074 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 57.7%
- **Risk Profile:** Cognitive Load (3.1581%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testCompletionWithOptions` (Impact: 103.5)
  * `searchCompletionItemWithLabel` (Impact: 7.9)
  * `testCompletionTextEdit` (Impact: 6.6)
    * *Intent:* /// TODO this function should allow asserting where the cursor is placed after the text edit
  * `sort` (Impact: 2.1)
  * `printLabels` (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Memory Alloc (weighted view):* 1
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 165`, `args: 292`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 117`, `state_mutation: 15`, `dead_code: 2`, `planned_debt: 15`, `fragile_debt: 1`
* *Architecture:* `api: 54`, `concurrency: 15`, `import: 37`
* *Defense:* `safety: 507`, `doc: 9`, `test: 172`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.591
  * `Choke Point (Betweenness):` 0.000121 | `Ripple Effect (Closeness):` 0.008621
  * `Imports (Out-Degree: 3):` ErrorBuilder.zig, context.zig, std, zls
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/features/references.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 288.64 | **LOC:** 794 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 86.7%
- **Risk Profile:** Cognitive Load (10.3084%), Tech Debt (8.4127%)
**Top Internal Functions/Classes:**
  * `referenceNode` (Impact: 83.2)
  * `referencesHandler` (Impact: 47.5)
  * `gatherWorkspaceReferenceCandidates` (Impact: 32.3)
  * `symbolReferences` (Impact: 30.4)
  * `referenceNode` (Impact: 26.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 5 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 131`, `args: 14`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 5`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 148`, `doc: 10`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.394
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` DocumentStore.zig, Server.zig, Uri.zig, analysis.zig, ast.zig, offsets.zig, lsp, std...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 255.02 | **LOC:** 605 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 93.3%
- **Risk Profile:** Cognitive Load (11.3034%), Tech Debt (8.7162%)
**Top Internal Functions/Classes:**
  * `parseArgs` (Impact: 59.5)
  * `main` (Impact: 42.6)
  * `logFn` (Impact: 41.6)
  * `@"zls env"` (Impact: 30.9)
  * `deinit` (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Mitigated Memory Allocs:* 33 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 113`, `args: 12`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 8`, `state_mutation: 16`, `planned_debt: 1`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 121`, `doc: 21`, `sync_locks: 2`, `cleanup: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.394
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` builtin, exe_options, known-folders, std, tracy, zls
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tracy.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 245.54 | **LOC:** 344 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.5782%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `TracyAllocator` (Impact: 20.9)
  * `resizeFn` (Impact: 10.4)
  * `remapFn` (Impact: 10.4)
  * `allocFn` (Impact: 9.6)
  * `allocNamed` (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Memory Alloc (weighted view):* 2
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 30`, `args: 57`, `func_start: 57`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`
* *Architecture:* `api: 29`, `import: 3`
* *Defense:* `safety: 10`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 40.514
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.193442
  * `Imports (Out-Degree: 0):` builtin, options, std
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `src/DocumentScope.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 223.9 | **LOC:** 1346 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (6.973%), Tech Debt (16.8973%)
**Top Internal Functions/Classes:**
  * `nameToken` (Impact: 12.9)
    * *Intent:* /// Returns a `.identifier` or `.builtin` token.
  * `getScopeDeclarationsConst` (Impact: 9.7)
  * `getScopeChildScopesConst` (Impact: 9.7)
  * `get` (Impact: 5.7)
  * `getScopeDeclaration` (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 8 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 81`, `args: 45`, `func_start: 45`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 11`, `duplicate_logic: 4`
* *Architecture:* `api: 41`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 165`, `doc: 38`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.887
  * `Choke Point (Betweenness):` 0.000534 | `Ripple Effect (Closeness):` 0.205375
  * `Imports (Out-Degree: 2):` ast.zig, offsets.zig, std, tracy
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/print_ast.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 215.04 | **LOC:** 950 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (7.9091%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderNode` (Impact: 45.5)
  * `moveSourceCursor` (Impact: 15.1)
  * `renderToFile` (Impact: 14.2)
  * `renderOptField` (Impact: 9.9)
  * `renderOptTokenField` (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 11 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 53`, `args: 21`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 13`
* *Architecture:* `api: 11`, `concurrency: 4`, `import: 3`
* *Defense:* `safety: 193`, `doc: 1`, `test: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.178
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.118575
  * `Imports (Out-Degree: 1):` std, testing.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/features/diagnostics.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 202.46 | **LOC:** 750 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 92.9%
- **Risk Profile:** Cognitive Load (13.5242%), Tech Debt (19.5206%)
**Top Internal Functions/Classes:**
  * `loop` (Impact: 58.9)
  * `getErrorBundleFromStderr` (Impact: 43.9)
  * `generateDiagnostics` (Impact: 17.5)
  * `getErrorBundleFromAstCheck` (Impact: 15.7)
  * `sendManualWatchUpdate` (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 10 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 6
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 130`, `args: 16`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 9`, `planned_debt: 13`
* *Architecture:* `api: 8`, `concurrency: 1`, `import: 14`
* *Defense:* `safety: 129`, `doc: 3`, `sync_locks: 3`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.394
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` DiagnosticsCollection.zig, DocumentStore.zig, Server.zig, Uri.zig, analysis.zig, ast.zig, shared.zig, offsets.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/TrigramStore.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 195.04 | **LOC:** 695 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.0427%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isVarDeclAlias` (Impact: 15.0)
    * *Intent:* /// Check if the init expression is a sequence of field accesses /// where the last field name match...
  * `mergeIntersection` (Impact: 13.5)
    * *Intent:* /// Asserts `@min(a.len, b.len) <= out.len`.
  * `next` (Impact: 11.1)
  * `appendToBucket` (Impact: 6.7)
  * `containsInBucket` (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 19 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 85`, `args: 23`, `func_start: 23`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 22`, `dead_code: 4`
* *Architecture:* `api: 22`, `import: 4`
* *Defense:* `safety: 76`, `doc: 17`, `test: 4`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.584
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.185345
  * `Imports (Out-Degree: 1):` ast.zig, offsets.zig, std
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/features/signature_help.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 191.0 | **LOC:** 323 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.5124%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getSignatureInfo` (Impact: 137.5)
  * `from` (Impact: 4.8)
  * `fnProtoToSignatureInfo` (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 36`, `args: 5`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `safety: 40`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.394
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` DocumentStore.zig, analysis.zig, ast.zig, offsets.zig, lsp, std, version_data
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/features/inlay_hints.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 188.54 | **LOC:** 576 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 77.8%
- **Risk Profile:** Cognitive Load (14.2048%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `writeNodeInlayHint` (Impact: 68.7)
  * `writeCallHint` (Impact: 30.5)
    * *Intent:* /// writes parameter hints into `builder.hints`
  * `writeRangeInlayHint` (Impact: 10.2)
    * *Intent:* /// creates a list of `InlayHint`'s from the given document /// only parameter hints are created ///...
  * `writeCallNodeHint` (Impact: 9.5)
    * *Intent:* /// takes a Ast.full.Call (a function call), analysis its function expression, finds its declaration...
  * `writeForCaptureHint` (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 58`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 9`
* *Architecture:* `api: 3`, `import: 9`
* *Defense:* `safety: 79`, `doc: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.394
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Config.zig, DocumentStore.zig, analysis.zig, ast.zig, offsets.zig, lsp, std, tracy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/features/goto.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 180.56 | **LOC:** 379 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (9.3679%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `gotoHandler` (Impact: 39.5)
  * `gotoDefinitionString` (Impact: 30.3)
  * `gotoDefinitionSymbol` (Impact: 24.2)
  * `gotoDefinitionStructInit` (Impact: 18.4)
  * `gotoDefinitionFieldAccess` (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 77`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 70`, `doc: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.517
  * `Choke Point (Betweenness):` 0.000234 | `Ripple Effect (Closeness):` 0.137931
  * `Imports (Out-Degree: 6):` DocumentStore.zig, Server.zig, Uri.zig, analysis.zig, offsets.zig, lsp, std, tracy
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/ErrorBuilder.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 166.64 | **LOC:** 685 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.4488%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 49.6)
  * `lessThan` (Impact: 8.6)
  * `assertFmt` (Impact: 8.3)
    * *Intent:* // // //
  * `next` (Impact: 7.9)
  * `removeUnusedFiles` (Impact: 6.3)
    * *Intent:* /// remove all files that contain no messages
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 34`, `args: 19`, `func_start: 19`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 20`
* *Architecture:* `api: 15`, `import: 3`
* *Defense:* `safety: 78`, `doc: 9`, `test: 8`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.745
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.07837
  * `Imports (Out-Degree: 1):` builtin, std, zls
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/configuration.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 159.7 | **LOC:** 778 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 73.3%
- **Risk Profile:** Cognitive Load (33.2284%), Tech Debt (8.4088%)
**Top Internal Functions/Classes:**
  * `eql` (Impact: 21.0)
  * `free` (Impact: 20.9)
  * `deinit` (Impact: 6.2)
  * `deinit` (Impact: 3.7)
  * `validateConfiguration` (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 22 instances
* *Amplified Cascading Flux:* 18 instances
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 134`, `args: 12`, `func_start: 12`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 24`, `planned_debt: 1`
* *Architecture:* `api: 17`, `import: 4`
* *Defense:* `safety: 106`, `doc: 19`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.142241
  * `Imports (Out-Degree: 1):` Config.zig, builtin, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/DocumentStore.zig` -> **Techatrix** (90.5% isolated ownership) | Magnitude: 539.28
- `src/analyser/segmented_list.zig` -> **Techatrix** (100.0% isolated ownership) | Magnitude: 343.32
- `src/features/code_actions.zig` -> **Techatrix** (100.0% isolated ownership) | Magnitude: 319.5
- `src/offsets.zig` -> **Techatrix** (100.0% isolated ownership) | Magnitude: 314.44
- `src/features/references.zig` -> **Techatrix** (86.7% isolated ownership) | Magnitude: 288.64

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/analysis.zig` -> **Severity: 0.606** (Bridge: 0.0093 * Flux: 65.3976%)
- `src/DocumentStore.zig` -> **Severity: 0.419** (Bridge: 0.0083 * Flux: 50.4738%)
- `src/features/completions.zig` -> **Severity: 0.408** (Bridge: 0.0043 * Flux: 94.8423%)
- `src/Server.zig` -> **Severity: 0.333** (Bridge: 0.0051 * Flux: 65.5186%)
- `src/analyser/InternPool.zig` -> **Severity: 0.129** (Bridge: 0.0048 * Flux: 26.809%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/analyser/segmented_list.zig` -> **Severity: 10.377** (Embedded: 0.1168 * Error Risk: 88.826%)
- `src/tracy.zig` -> **Severity: 10.258** (Embedded: 0.1934 * Error Risk: 53.0277%)
- `src/TrigramStore.zig` -> **Severity: 7.897** (Embedded: 0.1853 * Error Risk: 42.607%)
- `src/testing.zig` -> **Severity: 6.428** (Embedded: 0.1186 * Error Risk: 54.2088%)
- `src/DocumentScope.zig` -> **Severity: 5.912** (Embedded: 0.2054 * Error Risk: 28.7873%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/offsets.zig` -> **Severity: 4207.059** (Blast Radius: 58.471 * Doc Risk: 71.9512%)
- `src/tracy.zig` -> **Severity: 4051.4** (Blast Radius: 40.514 * Doc Risk: 100.0%)
- `tests/context.zig` -> **Severity: 2520.7** (Blast Radius: 25.207 * Doc Risk: 100.0%)
- `src/analyser/InternPool.zig` -> **Severity: 2421.829** (Blast Radius: 31.644 * Doc Risk: 76.5336%)
- `src/testing.zig` -> **Severity: 2240.37** (Blast Radius: 24.893 * Doc Risk: 90.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
