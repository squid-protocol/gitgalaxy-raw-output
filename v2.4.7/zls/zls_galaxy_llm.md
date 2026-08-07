# ARCHITECTURAL_BRIEF: zls
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_zig/zls` |
| **Timestamp** | `2026-08-07T04:30:17.670184+00:00` |
| **Scan Duration** | `1.27s` |
| **Git Branch** | `master` |
| **Git Commit** | `ef64fa01d9b513add8596eec09574df8feadbd5c` |
| **Git Remote** | `https://github.com/zigtools/zls.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 104 malicious artifacts.

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
| Total Artifacts | 134 |
| Analyzed Artifacts (Scanned) | 117 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17 |
| Total LOC | 52361 |
| Volatility Index | 0.017 |
| % Scanned of codebase = | 87.3% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.456 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5585 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 6.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4419 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 103 | 51824 | 88.0% |
| JSON | 10 | 451 | 8.5% |
| MARKDOWN | 2 | 0 | 1.7% |
| YAML | 1 | 11 | 0.9% |
| NIX | 1 | 75 | 0.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.429`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 99 | 84.6% |
| file_cluster_13 | 12 | 10.3% |
| file_cluster_16 | 4 | 3.4% |

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

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 68.3 | 17.5 | 10.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 95.4 | 36.0 | 35.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 99.9 | 6.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 20.5 | 0.0 | 0.0 |
| API Exposure | 0.0 | 17.8 | 1.2 | 0.2 | 0.0 |
| Concurrency Exposure | 0.0 | 34.7 | 1.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 96.5 | 9.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 35.4 | 1.5 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 95.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 14.2 | 0.8 | 0.1 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 15.6 | 4.5 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 18.7 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/build_runner/shared.zig` (Hits: 2)
- `README.md` (Hits: 0)
- `src/analyser/README.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **zls.zig** (`src/zls.zig`) — 24 inbound connections
2. **tracy.zig** (`src/tracy.zig`) — 17 inbound connections
3. **offsets.zig** (`src/offsets.zig`) — 9 inbound connections
4. **Uri.zig** (`src/Uri.zig`) — 6 inbound connections
5. **DocumentScope.zig** (`src/DocumentScope.zig`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **zls.zig** (`src/zls.zig`) — 33 outbound dependencies
2. **Server.zig** (`src/Server.zig`) — 27 outbound dependencies
3. **tests.zig** (`tests/tests.zig`) — 19 outbound dependencies
4. **DocumentStore.zig** (`src/DocumentStore.zig`) — 13 outbound dependencies
5. **completions.zig** (`src/features/completions.zig`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `resolveTypeOfNodeUncached` (@ `src/analysis.zig`) -> Impact: **1142.3** | LOC: 1092
- `loadBuildConfiguration` (@ `src/DocumentStore.zig`) -> Impact: **540.8** | LOC: 695
  * *Intent:* /// Runs the build.zig and extracts include directories and packages
- `resolveExpressionTypeFromAncestors` (@ `src/analysis.zig`) -> Impact: **511.1** | LOC: 424
- `writeNodeTokens` (@ `src/features/semantic_tokens.zig`) -> Impact: **484.1** | LOC: 675
- `resolvePeerTypes` (@ `src/analyser/InternPool.zig`) -> Impact: **410.8** | LOC: 495
- `main` (@ `src/build_runner/build_runner.zig`) -> Impact: **402.9** | LOC: 437
- `coerce` (@ `src/analyser/InternPool.zig`) -> Impact: **363.3** | LOC: 194
  * *Intent:* // --------------------------------------------- // UTILITY // --------------------------------------------- // pub const CoercionResult = union(enum)...
- `printInternal` (@ `src/analyser/InternPool.zig`) -> Impact: **358.1** | LOC: 275
- `getFieldAccessType` (@ `src/analysis.zig`) -> Impact: **329.2** | LOC: 215
- `getSignatureInfo` (@ `src/features/signature_help.zig`) -> Impact: **274.5** | LOC: 252

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tests/utility` | 3 | 17180.04 | 39.74% | 0.0% |
| `src` | 20 | 12336.04 | 29.23% | 20.5% |
| `src/features` | 13 | 5510.48 | 39.03% | 15.71% |
| `src/analyser` | 8 | 4204.42 | 15.35% | 8.94% |
| `tests/lsp_features` | 13 | 1601.6 | 9.45% | 0.0% |
| `src/build_runner` | 3 | 1541.0 | 26.76% | 2.95% |
| `tests` | 9 | 940.18 | 17.59% | 0.0% |
| `tests/analysis` | 25 | 577.04 | 7.37% | 0.0% |
| `tests/build_runner_cases` | 16 | 151.74 | 5.53% | 0.0% |
| `tests/language_features` | 1 | 59.22 | 18.72% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/tracy.zig` -> **99.9333%** Exposure
- `src/features/references.zig` -> **75.8887%** Exposure
- `src/features/workspace_symbols.zig` -> **63.1938%** Exposure
- `src/DocumentStore.zig` -> **57.0765%** Exposure
- `src/analysis.zig` -> **48.8264%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/features/selection_range.zig` -> **96.4996%** Exposure
- `src/TrigramStore.zig` -> **84.2404%** Exposure
- `src/diff.zig` -> **82.9205%** Exposure
- `src/DiagnosticsCollection.zig` -> **64.422%** Exposure
- `src/main.zig` -> **62.4892%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/analysis.zig` -> **0** Orphaned Functions | **37** Duplicates
- `src/analyser/InternPool.zig` -> **0** Orphaned Functions | **22** Duplicates
- `tests/analysis/capture.zig` -> **12** Orphaned Functions | **0** Duplicates
- `src/tracy.zig` -> **0** Orphaned Functions | **11** Duplicates
- `src/DocumentStore.zig` -> **0** Orphaned Functions | **10** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/features/completions.zig`** -> AI Confidence: **99.48%**
2. **`src/features/inlay_hints.zig`** -> AI Confidence: **99.48%**
3. **`src/features/signature_help.zig`** -> AI Confidence: **99.48%**
4. **`src/features/code_actions.zig`** -> AI Confidence: **99.39%**
5. **`src/features/hover.zig`** -> AI Confidence: **99.39%**
6. **`src/features/references.zig`** -> AI Confidence: **99.39%**
7. **`src/build_runner/build_runner.zig`** -> AI Confidence: **99.34%**
8. **`src/features/goto.zig`** -> AI Confidence: **99.34%**
9. **`src/features/semantic_tokens.zig`** -> AI Confidence: **99.34%**
10. **`tests/lsp_features/definition.zig`** -> AI Confidence: **99.34%**

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

### 1. `src/analysis.zig` (ZIG) -> Cumulative Risk: **519.57**
- **Archetype:** `file_cluster_8` (Distance: 14.849 IQR)
- **Magnitude:** 5640.26 | **LOC:** 7016 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 77.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Verification (80.0%), Cognitive Load (63.5325%)
- **Heaviest Functions:** `resolveTypeOfNodeUncached` (Impact: 1142.3), `resolveExpressionTypeFromAncestors` (Impact: 511.1), `getFieldAccessType` (Impact: 329.2)

### 2. `src/features/references.zig` (ZIG) -> Cumulative Risk: **487.53**
- **Archetype:** `file_cluster_8` (Distance: 13.267 IQR)
- **Magnitude:** 675.68 | **LOC:** 794 | **CtrlFlow:** 76.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Tech Debt (75.8887%), Documentation (57.9091%)
- **Heaviest Functions:** `referenceNode` (Impact: 199.6), `referencesHandler` (Impact: 105.5), `gatherWorkspaceReferenceCandidates` (Impact: 79.2)

### 3. `src/tracy.zig` (ZIG) -> Cumulative Risk: **475.41**
- **Archetype:** `file_cluster_8` (Distance: 9.941 IQR)
- **Magnitude:** 315.46 | **LOC:** 344 | **CtrlFlow:** 73.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9333%), Verification (80.0%)
- **Heaviest Functions:** `TracyAllocator` (Impact: 50.9), `resizeFn` (Impact: 15.3), `remapFn` (Impact: 15.3)

### 4. `src/TrigramStore.zig` (ZIG) -> Cumulative Risk: **473.48**
- **Archetype:** `file_cluster_8` (Distance: 13.322 IQR)
- **Magnitude:** 286.54 | **LOC:** 695 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (84.2404%), Verification (80.0%), Safety Score (58.742%)
- **Heaviest Functions:** `isVarDeclAlias` (Impact: 25.3), `next` (Impact: 22.0), `mergeIntersection` (Impact: 17.2)

### 5. `src/configuration.zig` (ZIG) -> Cumulative Risk: **449.04**
- **Archetype:** `file_cluster_8` (Distance: 12.817 IQR)
- **Magnitude:** 212.02 | **LOC:** 778 | **CtrlFlow:** 78.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Cognitive Load (68.3256%), State Flux (61.9212%)
- **Heaviest Functions:** `eql` (Impact: 37.0), `free` (Impact: 22.9), `deinit` (Impact: 7.4)

### 6. `src/main.zig` (ZIG) -> Cumulative Risk: **441.78**
- **Archetype:** `file_cluster_8` (Distance: 13.454 IQR)
- **Magnitude:** 317.72 | **LOC:** 605 | **CtrlFlow:** 67.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (62.4892%), Cognitive Load (53.5801%)
- **Heaviest Functions:** `parseArgs` (Impact: 86.8), `main` (Impact: 66.8), `logFn` (Impact: 48.8)

### 7. `src/features/diagnostics.zig` (ZIG) -> Cumulative Risk: **437.08**
- **Archetype:** `file_cluster_8` (Distance: 13.229 IQR)
- **Magnitude:** 338.56 | **LOC:** 750 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Cognitive Load (62.3841%), Safety Score (47.0952%)
- **Heaviest Functions:** `loop` (Impact: 108.2), `getErrorBundleFromAstCheck` (Impact: 43.9), `generateDiagnostics` (Impact: 43.6)

### 8. `src/build_runner/build_runner.zig` (ZIG) -> Cumulative Risk: **434.34**
- **Archetype:** `file_cluster_8` (Distance: 13.665 IQR)
- **Magnitude:** 1381.48 | **LOC:** 1503 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Churn (57.14%), Cognitive Load (52.252%)
- **Heaviest Functions:** `main` (Impact: 402.9), `extractBuildInformation` (Impact: 245.0), `runPkgConfig` (Impact: 119.0)

### 9. `src/DocumentStore.zig` (ZIG) -> Cumulative Risk: **431.1**
- **Archetype:** `file_cluster_8` (Distance: 13.812 IQR)
- **Magnitude:** 1224.74 | **LOC:** 2059 | **CtrlFlow:** 66.9% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Tech Debt (57.0765%), Churn (51.33%)
- **Heaviest Functions:** `loadBuildConfiguration` (Impact: 540.8), `invalidateBuildFileWorker` (Impact: 49.7), `loadDirectoryRecursive` (Impact: 37.6)

### 10. `src/features/workspace_symbols.zig` (ZIG) -> Cumulative Risk: **397.92**
- **Archetype:** `file_cluster_13` (Distance: 11.348 IQR)
- **Magnitude:** 22.48 | **LOC:** 94 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (65.7681%), Tech Debt (63.1938%), State Flux (58.2351%)
- **Heaviest Functions:** `lessThan` (Impact: 3.0), `handler` (Impact: 2.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/utility/position_context.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.966 IQR)
- **Top Global Matches:** file_cluster_8: 13.966, file_cluster_13: 14.14, file_cluster_17: 14.202
- **Magnitude:** 17056.3 | **LOC:** 768 | **CtrlFlow:** 78.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.2553%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 81`, `args: 30`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 219`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `import: 9`
* *Defense:* `safety: 202`, `doc: 6`, `test: 36`, `immutability_locks: 51`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` zls, std, helper.zig, ErrorBuilder.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/analysis.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.849 IQR)
- **Top Global Matches:** file_cluster_8: 14.849, file_cluster_0: 15.023, file_cluster_11: 15.027
- **Magnitude:** 5640.26 | **LOC:** 7016 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 77.3%
- **Risk Profile:** Cognitive Load (63.5325%), Tech Debt (48.8264%)
**Top Internal Functions/Classes:**
  * `resolveTypeOfNodeUncached` (Impact: 1142.3)
  * `resolveExpressionTypeFromAncestors` (Impact: 511.1)
  * `getFieldAccessType` (Impact: 329.2)
  * `resolveType` (Impact: 185.5)
  * `eql` (Impact: 136.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3250`, `structural_boundaries: 1173`, `args: 201`, `func_start: 197`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 579`, `dead_code: 9`, `planned_debt: 15`, `fragile_debt: 1`, `duplicate_logic: 37`
* *Architecture:* `api: 193`, `concurrency: 2`, `import: 16`
* *Defense:* `safety: 1442`, `doc: 111`, `test: 1`, `immutability_locks: 913`, `cleanup: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.474
  * `Choke Point (Betweenness):` 0.00035 | `Ripple Effect (Closeness):` 0.129464
  * `Imports (Out-Degree: 5):` error_msg.zig, version_data, references.zig, DocumentScope.zig, std, InternPool.zig, tracy, builtin...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/analyser/InternPool.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.744 IQR)
- **Top Global Matches:** file_cluster_8: 13.744, file_cluster_7: 13.988, file_cluster_0: 14.025
- **Magnitude:** 3249.58 | **LOC:** 5361 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (31.6529%), Tech Debt (45.2955%)
**Top Internal Functions/Classes:**
  * `resolvePeerTypes` (Impact: 410.8)
  * `coerce` (Impact: 363.3)
    * *Intent:* // --------------------------------------------- // UTILITY // -------------------------------------...
  * `printInternal` (Impact: 358.1)
  * `coerceInMemoryAllowed` (Impact: 187.4)
    * *Intent:* /// If types have the same representation in runtime memory /// * int/float: same number of bits ///...
  * `eqlCustom` (Impact: 161.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1731`, `structural_boundaries: 522`, `args: 134`, `func_start: 113`, `class_start: 67`
* *Risk/State:* `safety_bypasses: 117`, `high_risk_execution: 2`, `state_mutation: 198`, `dead_code: 5`, `planned_debt: 32`, `duplicate_logic: 22`
* *Architecture:* `api: 145`, `concurrency: 12`, `import: 6`
* *Defense:* `safety: 1053`, `doc: 166`, `test: 50`, `sync_locks: 80`, `immutability_locks: 518`, `cleanup: 64`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.758
  * `Choke Point (Betweenness):` 0.00075 | `Ripple Effect (Closeness):` 0.034483
  * `Imports (Out-Degree: 3):` error_msg.zig, string_pool.zig, segmented_list.zig, std, builtin
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/features/completions.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.173 IQR)
- **Top Global Matches:** file_cluster_8: 13.173, file_cluster_13: 13.491, file_cluster_7: 13.539
- **Magnitude:** 1773.7 | **LOC:** 1872 | **CtrlFlow:** 82.0% | **Authorship Centralization:** 38.5%
- **Risk Profile:** Cognitive Load (34.5272%), Tech Debt (9.8286%)
**Top Internal Functions/Classes:**
  * `getSwitchOrStructInitContext` (Impact: 245.4)
    * *Intent:* /// Looks for an identifier that can be passed to `collectContainerNodes()` /// Returns the token in...
  * `collectContainerFields` (Impact: 205.6)
    * *Intent:* /// Given a Type that is a container, adds it's `.container_field*`s to completions
  * `completeFileSystemStringLiteral` (Impact: 190.8)
    * *Intent:* /// Asserts that `pos_context` is one of the following: /// - `.import_string_literal` /// - `.cincl...
  * `declToCompletion` (Impact: 149.8)
  * `getEnumLiteralContext` (Impact: 79.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 809`, `structural_boundaries: 178`, `args: 40`, `func_start: 40`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 114`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 9`, `import: 14`
* *Defense:* `safety: 309`, `doc: 22`, `immutability_locks: 239`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Server.zig, lsp, version_data, DocumentStore.zig, std, Uri.zig, analysis.zig, snippets.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Server.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.435 IQR)
- **Top Global Matches:** file_cluster_8: 13.435, file_cluster_13: 13.592, file_cluster_7: 13.726
- **Magnitude:** 1481.26 | **LOC:** 2030 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (27.1804%), Tech Debt (18.1129%)
**Top Internal Functions/Classes:**
  * `initializeHandler` (Impact: 196.2)
  * `codeActionHandler` (Impact: 46.1)
  * `validateMessage` (Impact: 45.5)
  * `handleResponse` (Impact: 43.8)
  * `sendRequestSync` (Impact: 42.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 759`, `structural_boundaries: 261`, `args: 71`, `func_start: 71`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 106`, `planned_debt: 11`, `duplicate_logic: 2`
* *Architecture:* `api: 19`, `concurrency: 1`, `import: 28`
* *Defense:* `safety: 330`, `doc: 56`, `immutability_locks: 190`, `cleanup: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.677
  * `Choke Point (Betweenness):` 0.000312 | `Ripple Effect (Closeness):` 0.112069
  * `Imports (Out-Degree: 8):` semantic_tokens.zig, code_actions.zig, folding_range.zig, references.zig, tracy, selection_range.zig, offsets.zig, DocumentStore.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/build_runner/build_runner.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.665 IQR)
- **Top Global Matches:** file_cluster_8: 13.665, file_cluster_13: 13.841, file_cluster_0: 13.859
- **Magnitude:** 1381.48 | **LOC:** 1503 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (52.252%), Tech Debt (8.846%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 402.9)
  * `extractBuildInformation` (Impact: 245.0)
  * `runPkgConfig` (Impact: 119.0)
    * *Intent:* /// Run pkg-config for the given library name and parse the output, returning the arguments /// that...
  * `makeStep` (Impact: 46.5)
    * *Intent:* /// Runs the "make" function of the single step `s`, updates its state, and then spawns newly-ready ...
  * `processModule` (Impact: 40.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 548`, `structural_boundaries: 134`, `args: 31`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 1`, `state_mutation: 144`, `dead_code: 7`, `orphaned_logic: 1`
* *Architecture:* `api: 10`, `concurrency: 10`, `import: 6`
* *Defense:* `safety: 254`, `doc: 49`, `test: 1`, `sync_locks: 5`, `immutability_locks: 161`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` @build, std, @dependencies, builtin, shared.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/DocumentStore.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.812 IQR)
- **Top Global Matches:** file_cluster_8: 13.812, file_cluster_13: 13.848, file_cluster_7: 13.974
- **Magnitude:** 1224.74 | **LOC:** 2059 | **CtrlFlow:** 66.9% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (40.0665%), Tech Debt (57.0765%)
**Top Internal Functions/Classes:**
  * `loadBuildConfiguration` (Impact: 540.8)
    * *Intent:* /// Runs the build.zig and extracts include directories and packages
  * `invalidateBuildFileWorker` (Impact: 49.7)
  * `loadDirectoryRecursive` (Impact: 37.6)
  * `notifyBuildStart` (Impact: 28.1)
  * `readFile` (Impact: 25.9)
    * *Intent:* /// Must satisfy `uri.isFileScheme()`.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 641`, `structural_boundaries: 317`, `args: 59`, `func_start: 59`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 160`, `dead_code: 1`, `planned_debt: 12`, `duplicate_logic: 10`
* *Architecture:* `api: 52`, `concurrency: 30`, `import: 21`
* *Defense:* `safety: 323`, `doc: 101`, `sync_locks: 44`, `immutability_locks: 234`, `cleanup: 111`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.598
  * `Choke Point (Betweenness):` 0.001324 | `Ripple Effect (Closeness):` 0.131818
  * `Imports (Out-Degree: 9):` lsp, DocumentScope.zig, TrigramStore.zig, std, translate_c.zig, tracy, builtin, DiagnosticsCollection.zig...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/ast.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.628 IQR)
- **Top Global Matches:** file_cluster_8: 11.628, file_cluster_7: 11.958, file_cluster_0: 12.095
- **Magnitude:** 989.08 | **LOC:** 1847 | **CtrlFlow:** 70.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.0481%), Tech Debt (27.2591%)
**Top Internal Functions/Classes:**
  * `lastToken` (Impact: 167.7)
    * *Intent:* /// Similar to `std.zig.Ast.lastToken` but also handles ASTs with syntax errors.
  * `indexOfBreakTarget` (Impact: 80.0)
  * `init` (Impact: 68.7)
  * `next` (Impact: 59.8)
  * `next` (Impact: 49.7)
    * *Intent:* /// Iterates over FnProto Params w/ added bounds check to support incomplete ast nodes
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 425`, `structural_boundaries: 178`, `args: 56`, `func_start: 56`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 114`, `dead_code: 4`, `planned_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 66`, `concurrency: 4`, `import: 2`
* *Defense:* `safety: 126`, `doc: 34`, `test: 9`, `immutability_locks: 247`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` std, offsets.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/features/semantic_tokens.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.942 IQR)
- **Top Global Matches:** file_cluster_8: 12.942, file_cluster_7: 13.364, file_cluster_13: 13.373
- **Magnitude:** 855.26 | **LOC:** 1200 | **CtrlFlow:** 91.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (47.7868%), Tech Debt (8.7932%)
**Top Internal Functions/Classes:**
  * `writeNodeTokens` (Impact: 484.1)
  * `writeFieldAccess` (Impact: 60.2)
  * `writeVarDecl` (Impact: 59.2)
  * `writeIdentifier` (Impact: 44.0)
  * `writeContainerField` (Impact: 31.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 448`, `structural_boundaries: 44`, `args: 15`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 59`, `planned_debt: 1`
* *Architecture:* `api: 6`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 324`, `doc: 8`, `immutability_locks: 111`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lsp, DocumentStore.zig, std, analysis.zig, offsets.zig, ast.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/features/references.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.267 IQR)
- **Top Global Matches:** file_cluster_8: 13.267, file_cluster_13: 13.342, file_cluster_0: 13.457
- **Magnitude:** 675.68 | **LOC:** 794 | **CtrlFlow:** 76.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (41.1883%), Tech Debt (75.8887%)
**Top Internal Functions/Classes:**
  * `referenceNode` (Impact: 199.6)
  * `referencesHandler` (Impact: 105.5)
  * `gatherWorkspaceReferenceCandidates` (Impact: 79.2)
  * `symbolReferences` (Impact: 66.2)
  * `referenceNode` (Impact: 51.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 100`, `args: 14`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 79`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 6`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 148`, `doc: 10`, `immutability_locks: 115`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Server.zig, lsp, DocumentStore.zig, std, Uri.zig, analysis.zig, offsets.zig, tracy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/analyser/segmented_list.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.687 IQR)
- **Top Global Matches:** file_cluster_8: 10.687, file_cluster_7: 10.915, file_cluster_16: 11.027
- **Magnitude:** 492.98 | **LOC:** 444 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.6782%), Tech Debt (14.1604%)
**Top Internal Functions/Classes:**
  * `SegmentedList` (Impact: 169.0)
    * *Intent:* /// This is a stack data structure where pointers to indexes have the same lifetime as the data stru...
  * `BaseIterator` (Impact: 43.2)
  * `shrinkCapacity` (Impact: 23.6)
    * *Intent:* /// Only shrinks capacity or retains current capacity. /// It may fail to reduce the capacity in whi...
  * `growCapacity` (Impact: 17.1)
    * *Intent:* /// Only grows capacity, or retains current capacity.
  * `next` (Impact: 15.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 48`, `args: 32`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 15`, `planned_debt: 3`
* *Architecture:* `api: 40`, `import: 1`
* *Defense:* `safety: 12`, `doc: 25`, `immutability_locks: 41`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.023946
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/features/goto.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.23 IQR)
- **Top Global Matches:** file_cluster_8: 12.23, file_cluster_13: 12.429, file_cluster_7: 12.644
- **Magnitude:** 432.06 | **LOC:** 379 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (31.0521%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `gotoHandler` (Impact: 104.1)
  * `gotoDefinitionString` (Impact: 77.5)
  * `gotoDefinitionSymbol` (Impact: 57.8)
  * `gotoDefinitionFieldAccess` (Impact: 43.4)
  * `gotoDefinitionStructInit` (Impact: 41.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 70`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 15`
* *Architecture:* `api: 3`, `import: 9`
* *Defense:* `safety: 70`, `doc: 5`, `immutability_locks: 73`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Server.zig, lsp, DocumentStore.zig, std, Uri.zig, analysis.zig, offsets.zig, tracy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/features/code_actions.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.933 IQR)
- **Top Global Matches:** file_cluster_8: 12.933, file_cluster_13: 12.97, file_cluster_0: 13.081
- **Magnitude:** 394.66 | **LOC:** 1230 | **CtrlFlow:** 74.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.4399%), Tech Debt (9.2788%)
**Top Internal Functions/Classes:**
  * `detectIndentation` (Impact: 37.1)
  * `getParamRemovalRange` (Impact: 34.8)
  * `lessThan` (Impact: 25.1)
  * `getCaptureLoc` (Impact: 21.7)
    * *Intent:* /// takes the location of a capture ie `value` from `...|value...|...`. /// returns the location fro...
  * `getKind` (Impact: 21.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 478`, `structural_boundaries: 161`, `args: 40`, `func_start: 38`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 90`, `dead_code: 7`, `planned_debt: 2`
* *Architecture:* `api: 31`, `import: 15`
* *Defense:* `safety: 146`, `doc: 21`, `test: 9`, `immutability_locks: 233`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` lsp, DocumentStore.zig, std, analysis.zig, offsets.zig, tracy, ast.zig, DocumentScope.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/features/inlay_hints.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.888 IQR)
- **Top Global Matches:** file_cluster_8: 11.888, file_cluster_13: 12.184, file_cluster_7: 12.267
- **Magnitude:** 366.12 | **LOC:** 576 | **CtrlFlow:** 79.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (20.7698%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `writeNodeInlayHint` (Impact: 154.2)
  * `writeCallHint` (Impact: 56.8)
    * *Intent:* /// writes parameter hints into `builder.hints`
  * `writeRangeInlayHint` (Impact: 31.8)
    * *Intent:* /// creates a list of `InlayHint`'s from the given document /// only parameter hints are created ///...
  * `typeStrOfToken` (Impact: 16.2)
  * `writeCallNodeHint` (Impact: 14.7)
    * *Intent:* /// takes a Ast.full.Call (a function call), analysis its function expression, finds its declaration...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 45`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 31`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `safety: 79`, `doc: 11`, `immutability_locks: 85`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` lsp, version_data, Config.zig, DocumentStore.zig, std, analysis.zig, offsets.zig, tracy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/features/diagnostics.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.229 IQR)
- **Top Global Matches:** file_cluster_8: 13.229, file_cluster_13: 13.265, file_cluster_11: 13.436
- **Magnitude:** 338.56 | **LOC:** 750 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (62.3841%), Tech Debt (21.8288%)
**Top Internal Functions/Classes:**
  * `loop` (Impact: 108.2)
  * `getErrorBundleFromAstCheck` (Impact: 43.9)
  * `generateDiagnostics` (Impact: 43.6)
  * `sendManualWatchUpdate` (Impact: 5.7)
  * `isCamelCase` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 107`, `args: 16`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 84`, `planned_debt: 13`
* *Architecture:* `api: 10`, `concurrency: 1`, `import: 14`
* *Defense:* `safety: 129`, `doc: 3`, `sync_locks: 3`, `immutability_locks: 115`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Server.zig, lsp, DocumentStore.zig, std, Uri.zig, analysis.zig, offsets.zig, code_actions.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/offsets.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.445 IQR)
- **Top Global Matches:** file_cluster_8: 13.445, file_cluster_7: 13.654, file_cluster_13: 13.699
- **Magnitude:** 331.28 | **LOC:** 806 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.0805%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sourceIndexToTokenIndex` (Impact: 41.0)
  * `pickTokenTag` (Impact: 25.3)
  * `tokenToLoc` (Impact: 24.5)
  * `pickPreferred` (Impact: 21.1)
  * `preferLeft` (Impact: 10.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 97`, `args: 42`, `func_start: 42`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 75`
* *Architecture:* `api: 74`, `import: 3`
* *Defense:* `safety: 141`, `doc: 42`, `test: 68`, `immutability_locks: 127`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 47.989
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.176145
  * `Imports (Out-Degree: 0):` lsp, std, ast.zig
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/print_ast.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.886 IQR)
- **Top Global Matches:** file_cluster_8: 11.886, file_cluster_7: 12.426, file_cluster_0: 12.489
- **Magnitude:** 326.1 | **LOC:** 950 | **CtrlFlow:** 83.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.0953%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderNode` (Impact: 68.7)
  * `renderToFile` (Impact: 27.7)
  * `renderNodeSliceField` (Impact: 23.3)
  * `main` (Impact: 20.8)
  * `moveSourceCursor` (Impact: 16.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 49`, `args: 21`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 48`
* *Architecture:* `api: 11`, `concurrency: 4`, `import: 3`
* *Defense:* `safety: 193`, `doc: 1`, `test: 2`, `immutability_locks: 95`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.805
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.118575
  * `Imports (Out-Degree: 1):` std, testing.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/features/signature_help.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.577 IQR)
- **Top Global Matches:** file_cluster_8: 11.577, file_cluster_13: 11.83, file_cluster_7: 12.061
- **Magnitude:** 323.22 | **LOC:** 323 | **CtrlFlow:** 84.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.9573%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getSignatureInfo` (Impact: 274.5)
  * `from` (Impact: 7.5)
  * `fnProtoToSignatureInfo` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 21`, `args: 5`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 30`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `safety: 40`, `doc: 1`, `immutability_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lsp, version_data, DocumentStore.zig, std, analysis.zig, offsets.zig, ast.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.454 IQR)
- **Top Global Matches:** file_cluster_8: 13.454, file_cluster_13: 13.568, file_cluster_7: 13.722
- **Magnitude:** 317.72 | **LOC:** 605 | **CtrlFlow:** 67.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (53.5801%), Tech Debt (36.4329%)
**Top Internal Functions/Classes:**
  * `parseArgs` (Impact: 86.8)
  * `main` (Impact: 66.8)
  * `logFn` (Impact: 48.8)
  * `deinit` (Impact: 5.8)
  * `deinit` (Impact: 5.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 102`, `args: 12`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 76`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 121`, `doc: 21`, `sync_locks: 2`, `immutability_locks: 84`, `cleanup: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` known-folders, exe_options, std, zls, builtin, tracy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/DocumentScope.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.21%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.125 IQR)
- **Top Global Matches:** file_cluster_8: 12.125, file_cluster_7: 12.483, file_cluster_13: 12.636
- **Magnitude:** 316.52 | **LOC:** 1346 | **CtrlFlow:** 80.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.0006%), Tech Debt (33.336%)
**Top Internal Functions/Classes:**
  * `nameToken` (Impact: 19.9)
    * *Intent:* /// Returns a `.identifier` or `.builtin` token.
  * `getScopeDeclarationsConst` (Impact: 17.1)
  * `getScopeChildScopesConst` (Impact: 17.1)
  * `get` (Impact: 9.2)
  * `getScopeDeclaration` (Impact: 8.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 287`, `structural_boundaries: 68`, `args: 45`, `func_start: 45`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 46`, `duplicate_logic: 8`
* *Architecture:* `api: 48`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 184`, `doc: 38`, `immutability_locks: 160`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.758
  * `Choke Point (Betweenness):` 0.000612 | `Ripple Effect (Closeness):` 0.144715
  * `Imports (Out-Degree: 2):` tracy, std, offsets.zig, ast.zig
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/tracy.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.941 IQR)
- **Top Global Matches:** file_cluster_8: 9.941, file_cluster_7: 10.516, file_cluster_13: 10.668
- **Magnitude:** 315.46 | **LOC:** 344 | **CtrlFlow:** 73.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.5882%), Tech Debt (99.9333%)
**Top Internal Functions/Classes:**
  * `TracyAllocator` (Impact: 50.9)
  * `resizeFn` (Impact: 15.3)
  * `remapFn` (Impact: 15.3)
  * `trace` (Impact: 14.9)
  * `allocFn` (Impact: 14.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 30`, `args: 57`, `func_start: 57`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `duplicate_logic: 11`
* *Architecture:* `api: 36`, `import: 3`
* *Defense:* `safety: 10`, `doc: 1`, `immutability_locks: 64`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 69.793
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.172058
  * `Imports (Out-Degree: 0):` builtin, std, options
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `tests/lsp_features/completion.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.933 IQR)
- **Top Global Matches:** file_cluster_8: 11.933, file_cluster_7: 12.528, file_cluster_13: 12.56
- **Magnitude:** 297.2 | **LOC:** 5074 | **CtrlFlow:** 85.2% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (6.9408%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `searchCompletionItemWithLabel` (Impact: 14.9)
  * `sort` (Impact: 4.2)
  * `testCompletion` (Impact: 3.6)
  * `extractCompletionLabels` (Impact: 1.8)
  * `testCompletionWithOptions` (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 745`, `structural_boundaries: 129`, `args: 297`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 118`, `state_mutation: 100`, `dead_code: 2`, `planned_debt: 15`, `fragile_debt: 1`
* *Architecture:* `api: 54`, `concurrency: 15`, `import: 37`
* *Defense:* `safety: 510`, `doc: 9`, `test: 175`, `immutability_locks: 1082`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` zls, context.zig, std, ErrorBuilder.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/lsp_features/definition.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.415 IQR)
- **Top Global Matches:** file_cluster_8: 12.415, file_cluster_13: 12.73, file_cluster_7: 12.821
- **Magnitude:** 294.02 | **LOC:** 587 | **CtrlFlow:** 82.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (14.3467%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDefinition` (Impact: 189.4)
    * *Intent:* /// - use `<>` to indicate the cursor position /// - use `<decl>content</decl>` to set the expected ...
  * `parseTaggedLoc` (Impact: 35.9)
    * *Intent:* /// finds the source location that is enclosed by `<tag_name>return_value</tag_name>`
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 38`, `args: 9`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 58`, `planned_debt: 1`
* *Architecture:* `import: 5`
* *Defense:* `safety: 109`, `doc: 8`, `test: 29`, `immutability_locks: 122`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ErrorBuilder.zig, std, helper.zig, zls, context.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/TrigramStore.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.322 IQR)
- **Top Global Matches:** file_cluster_8: 13.322, file_cluster_13: 13.36, file_cluster_0: 13.38
- **Magnitude:** 286.54 | **LOC:** 695 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (33.0026%), Tech Debt (27.4825%)
**Top Internal Functions/Classes:**
  * `isVarDeclAlias` (Impact: 25.3)
    * *Intent:* /// Check if the init expression is a sequence of field accesses /// where the last field name match...
  * `next` (Impact: 22.0)
  * `mergeIntersection` (Impact: 17.2)
    * *Intent:* /// Asserts `@min(a.len, b.len) <= out.len`.
  * `appendToBucket` (Impact: 10.7)
  * `containsInBucket` (Impact: 10.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 77`, `args: 23`, `func_start: 23`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 95`, `dead_code: 4`, `duplicate_logic: 3`
* *Architecture:* `api: 23`, `import: 4`
* *Defense:* `safety: 76`, `doc: 17`, `test: 4`, `immutability_locks: 82`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.339
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.131502
  * `Imports (Out-Degree: 1):` std, offsets.zig, ast.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/lsp_features/semantic_tokens.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.987 IQR)
- **Top Global Matches:** file_cluster_8: 11.987, file_cluster_16: 12.223, file_cluster_7: 12.496
- **Magnitude:** 276.56 | **LOC:** 2238 | **CtrlFlow:** 78.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.9994%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 14.9)
  * `init` (Impact: 3.9)
  * `testSemanticTokens` (Impact: 3.6)
  * `testSemanticTokensOptions` (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 65`, `args: 33`, `func_start: 4`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 202`, `planned_debt: 1`
* *Architecture:* `api: 9`, `import: 7`
* *Defense:* `safety: 197`, `doc: 24`, `test: 69`, `immutability_locks: 245`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` zls, context.zig, std, ErrorBuilder.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/context.zig` (ZIG) | Magnitude: 60.3 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 99, safety: 31, branch: 26, globals: 21
- `tests/lsp_features/code_actions.zig` (ZIG) | Magnitude: 109.84 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 916, immutability_locks: 222, branch: 142, safety: 122
- `tests/build_runner_check.zig` (ZIG) | Magnitude: 88.62 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 79, branch: 44, safety: 30, bitwise_ops: 25
- `tests/utility/ast.zig` (ZIG) | Magnitude: 89.42 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 90, state_mutation: 57, structural_boundaries: 27, safety: 25
- `src/diff.zig` (ZIG) | Magnitude: 45.1 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 105, branch: 32, immutability_locks: 25, encapsulation: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/analysis/function.zig` (ZIG) | Magnitude: 3.6 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: bitwise_ops: 32, generics: 4, args: 3, encapsulation: 3
- `tests/analysis/assembly.zig` (ZIG) | Magnitude: 11.56 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: bitwise_ops: 8, globals: 1, generics: 1, inline_asm: 1
- `tests/analysis/either.zig` (ZIG) | Magnitude: 16.6 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: bitwise_ops: 190, encapsulation: 25, generics: 21, immutability_locks: 20
- `tests/analysis/error_union.zig` (ZIG) | Magnitude: 15.3 | Delta: **0.311 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: bitwise_ops: 122, generics: 10, globals: 7, immutability_locks: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/analyser/string_pool.zig` (ZIG) | Magnitude: 202.66 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 217, immutability_locks: 62, branch: 56, globals: 54
- `tests/lsp_features/selection_range.zig` (ZIG) | Magnitude: 14.48 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, immutability_locks: 25, encapsulation: 19, globals: 18
- `src/DocumentStore.zig` (ZIG) | Magnitude: 1224.74 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1560, branch: 641, safety: 323, structural_boundaries: 317
- `src/features/diagnostics.zig` (ZIG) | Magnitude: 338.56 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 585, branch: 226, safety: 129, encapsulation: 125
- `src/features/code_actions.zig` (ZIG) | Magnitude: 394.66 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 946, branch: 478, encapsulation: 234, immutability_locks: 233

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/analysis.zig` -> Churn: **100.0%** | Cog Load: 63.5325% | Debt: 48.8264%
- `src/build_runner/build_runner.zig` -> Churn: **57.14%** | Cog Load: 52.252% | Debt: 8.846%
- `src/DocumentStore.zig` -> Churn: **51.33%** | Cog Load: 40.0665% | Debt: 57.0765%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/utility/position_context.zig` -> **Techatrix** (100.0% isolated ownership) | Magnitude: 17056.3
- `src/build_runner/build_runner.zig` -> **Techatrix** (100.0% isolated ownership) | Magnitude: 1381.48
- `src/features/code_actions.zig` -> **Techatrix** (100.0% isolated ownership) | Magnitude: 394.66
- `src/features/diagnostics.zig` -> **Techatrix** (100.0% isolated ownership) | Magnitude: 338.56
- `src/main.zig` -> **Techatrix** (100.0% isolated ownership) | Magnitude: 317.72

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/DocumentStore.zig` -> **Severity: 0.033** (Bridge: 0.0013 * Flux: 24.7911%)
- `src/DiagnosticsCollection.zig` -> **Severity: 0.02** (Bridge: 0.0003 * Flux: 64.422%)
- `src/translate_c.zig` -> **Severity: 0.009** (Bridge: 0.0003 * Flux: 30.2551%)
- `src/testing.zig` -> **Severity: 0.008** (Bridge: 0.0002 * Flux: 35.2921%)
- `src/analysis.zig` -> **Severity: 0.007** (Bridge: 0.0003 * Flux: 21.0799%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/tracy.zig` -> **Severity: 9.7** (Embedded: 0.1721 * Error Risk: 56.3772%)
- `src/snippets.zig` -> **Severity: 8.77** (Embedded: 0.1121 * Error Risk: 78.2536%)
- `src/TrigramStore.zig` -> **Severity: 7.725** (Embedded: 0.1315 * Error Risk: 58.742%)
- `src/Config.zig` -> **Severity: 7.623** (Embedded: 0.1252 * Error Risk: 60.9033%)
- `src/testing.zig` -> **Severity: 7.331** (Embedded: 0.1186 * Error Risk: 61.8236%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/zls.zig` -> **Severity: 10372.4** (Blast Radius: 103.724 * Doc Risk: 100.0%)
- `src/tracy.zig` -> **Severity: 6979.3** (Blast Radius: 69.793 * Doc Risk: 100.0%)
- `src/offsets.zig` -> **Severity: 4231.209** (Blast Radius: 47.989 * Doc Risk: 88.1704%)
- `src/testing.zig` -> **Severity: 1763.365** (Blast Radius: 30.914 * Doc Risk: 57.041%)
- `src/analyser/string_pool.zig` -> **Severity: 1345.7** (Blast Radius: 13.457 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
