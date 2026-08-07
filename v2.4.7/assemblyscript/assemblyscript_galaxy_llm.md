# ARCHITECTURAL_BRIEF: assemblyscript
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/assemblyscript` |
| **Timestamp** | `2026-08-07T04:14:40.196081+00:00` |
| **Scan Duration** | `2.97s` |
| **Git Branch** | `main` |
| **Git Commit** | `be8e56d524a4deccfb6f2242b93a6d30fcf1a589` |
| **Git Remote** | `https://github.com/AssemblyScript/assemblyscript.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 507 malicious artifacts.

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
| Total Artifacts | 1274 |
| Analyzed Artifacts (Scanned) | 694 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 580 |
| Total LOC | 72578 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 54.5% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7002 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0631 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.732 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 24 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 448 | 62424 | 64.6% |
| JSON | 150 | 1894 | 21.6% |
| JAVASCRIPT | 59 | 8219 | 8.5% |
| PLAINTEXT | 23 | 1 | 3.3% |
| MARKDOWN | 11 | 0 | 1.6% |
| XML | 2 | 2 | 0.3% |
| HTML | 1 | 38 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.495`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 526 | 75.8% |
| file_cluster_13 | 35 | 5.0% |
| file_cluster_0 | 35 | 5.0% |
| file_cluster_16 | 28 | 4.0% |
| file_cluster_2 | 11 | 1.6% |
| file_cluster_4 | 7 | 1.0% |
| file_cluster_17 | 5 | 0.7% |
| file_cluster_11 | 5 | 0.7% |
| file_cluster_7 | 2 | 0.3% |
| file_cluster_6 | 2 | 0.3% |
| file_cluster_9 | 2 | 0.3% |
| Unknown | 1 | 0.1% |
| file_cluster_1 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 33 | 4.8% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 580*

**Composition by Extension & Reason:**
- `.wat`: 379x Excluded (Unsupported Extension: '.wat'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 112x Excluded: Neighborhood Micro-Mass Limit Exceeded, 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1889 LOC)
- `.ts`: 19x Excluded: Neighborhood Micro-Mass Limit Exceeded, 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 2940 commas in 803 LOC)
- `.js`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 139 LOC)
- `.wasm`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.cjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 1x Excluded (Saturation: Line 1 exceeds 500 chars)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 11.8 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 24.2 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 6.2 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.6 | 3.1 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 10.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.4 | 1.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 69.2 | 80.0 | 100.0 |
| Instability Exposure | 0.0 | 6.7 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `util/browser/path.js` (Hits: 72)
- `bin/asinit.js` (Hits: 50)
- `cli/index.js` (Hits: 46)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **js.ts** (`src/bindings/js.ts`) — 26 inbound connections
2. **fs.js** (`util/browser/fs.js`) — 14 inbound connections
3. **url.js** (`util/browser/url.js`) — 12 inbound connections
4. **program.ts** (`src/program.ts`) — 12 inbound connections
5. **types.ts** (`src/types.ts`) — 10 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index-js.ts** (`src/index-js.ts`) — 16 outbound dependencies
2. **compiler.js** (`tests/compiler.js`) — 15 outbound dependencies
3. **program.ts** (`src/program.ts`) — 15 outbound dependencies
4. **compiler.ts** (`src/compiler.ts`) — 14 outbound dependencies
5. **build.js** (`scripts/build.js`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `makeAssignment` (@ `src/compiler.ts`) -> Impact: **1067.5** | LOC: 1607
  * *Intent:* /** Adds an array header to static memory and returns the created segment. */
- `compileCallDirect` (@ `src/compiler.ts`) -> Impact: **1012.1** | LOC: 1576
- `compileIdentifierExpression` (@ `src/compiler.ts`) -> Impact: **892.1** | LOC: 1603
- `assert` (@ `src/compiler.ts`) -> Impact: **857.0** | LOC: 1579
- `finalizeAnyInstanceOf` (@ `src/compiler.ts`) -> Impact: **720.5** | LOC: 1489
- `compileTopLevelStatement` (@ `src/compiler.ts`) -> Impact: **666.8** | LOC: 1558
- `compileNewExpression` (@ `src/compiler.ts`) -> Impact: **648.1** | LOC: 1082
- `assert` (@ `src/compiler.ts`) -> Impact: **641.5** | LOC: 1601
- `replaceChild` (@ `src/passes/pass.ts`) -> Impact: **572.0** | LOC: 799
- `doProcessOverride` (@ `src/program.ts`) -> Impact: **561.1** | LOC: 1204
  * *Intent:* // TODO: for (let [exportName, queuedExport] of exports) {

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 7 | 5030.28 | 1.12% | 2.81% |
| `src` | 21 | 4043.33 | 29.66% | 44.88% |
| `tests/compiler/bindings` | 20 | 2121.2 | 8.86% | 0.0% |
| `cli` | 5 | 1554.69 | 21.05% | 36.91% |
| `tests/compiler` | 228 | 1531.45 | 7.16% | 0.0% |
| `std/assembly` | 34 | 912.95 | 30.91% | 68.54% |
| `util` | 16 | 807.65 | 26.31% | 28.36% |
| `util/browser` | 5 | 710.86 | 46.07% | 18.82% |
| `scripts` | 9 | 693.02 | 45.31% | 20.67% |
| `tests/compiler/std` | 53 | 622.57 | 7.69% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `scripts/build-dts.js` -> **100.0%** Exposure
- `util/find.js` -> **100.0%** Exposure
- `src/ast.ts` -> **100.0%** Exposure
- `src/glue/js/node.d.ts` -> **100.0%** Exposure
- `std/assembly/dataview.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `scripts/unicode-identifier.js` -> **100.0%** Exposure
- `scripts/update-constants.js` -> **100.0%** Exposure
- `util/browser/path.js` -> **100.0%** Exposure
- `util/browser/process.js` -> **100.0%** Exposure
- `util/browser/url.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `std/assembly/typedarray.ts` -> **1** Orphaned Functions | **332** Duplicates
- `src/ast.ts` -> **0** Orphaned Functions | **155** Duplicates
- `src/builtins.ts` -> **0** Orphaned Functions | **149** Duplicates
- `src/passes/pass.ts` -> **0** Orphaned Functions | **64** Duplicates
- `src/compiler.ts` -> **0** Orphaned Functions | **47** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/extra/ast.ts`** -> AI Confidence: **99.48%**
2. **`src/flow.ts`** -> AI Confidence: **99.48%**
3. **`src/parser.ts`** -> AI Confidence: **99.39%**
4. **`src/bindings/util.ts`** -> AI Confidence: **99.32%**
5. **`bin/asinit.js`** -> AI Confidence: **99.31%**
6. **`cli/index.js`** -> AI Confidence: **99.31%**
7. **`tests/compiler.js`** -> AI Confidence: **99.31%**
8. **`tests/parser.js`** -> AI Confidence: **99.31%**
9. **`src/bindings/js.ts`** -> AI Confidence: **99.31%**
10. **`src/compiler.ts`** -> AI Confidence: **99.31%**
11. **`src/program.ts`** -> AI Confidence: **99.31%**
12. **`src/resolver.ts`** -> AI Confidence: **99.31%**
13. **`std/assembly/staticarray.ts`** -> AI Confidence: **99.31%**
14. **`src/passes/pass.ts`** -> AI Confidence: **99.29%**
15. **`std/assembly/util/bytes.ts`** -> AI Confidence: **99.29%**
16. **`std/assembly/util/uri.ts`** -> AI Confidence: **99.29%**
17. **`tests/compiler/assert.ts`** -> AI Confidence: **99.29%**
18. **`tests/compiler/continue.ts`** -> AI Confidence: **99.29%**
19. **`tests/compiler/features/threads.ts`** -> AI Confidence: **99.29%**
20. **`tests/compiler/localinit.ts`** -> AI Confidence: **99.29%**
21. **`tests/compiler/memcpy.ts`** -> AI Confidence: **99.29%**
22. **`tests/compiler/overflow.ts`** -> AI Confidence: **99.29%**
23. **`tests/compiler/rt/alloc-large-memory.ts`** -> AI Confidence: **99.29%**
24. **`tests/compiler/std/string-casemapping.ts`** -> AI Confidence: **99.29%**
25. **`tests/compiler/std/string-nonnull.ts`** -> AI Confidence: **99.29%**
26. **`tests/compiler/std/string.ts`** -> AI Confidence: **99.29%**
27. **`tests/compiler/std/uri.ts`** -> AI Confidence: **99.29%**
28. **`tests/parser/continue-on-error.ts`** -> AI Confidence: **99.29%**
29. **`tests/parser/continue-on-error.ts.fixture.ts`** -> AI Confidence: **99.29%**
30. **`tests/parser/do.ts`** -> AI Confidence: **99.29%**
31. **`tests/parser/do.ts.fixture.ts`** -> AI Confidence: **99.29%**
32. **`tests/parser/forof.ts`** -> AI Confidence: **99.29%**
33. **`tests/parser/forof.ts.fixture.ts`** -> AI Confidence: **99.29%**
34. **`tests/parser/parameter-order.ts`** -> AI Confidence: **99.29%**
35. **`tests/parser/parameter-order.ts.fixture.ts`** -> AI Confidence: **99.29%**
36. **`tests/parser/while.ts`** -> AI Confidence: **99.29%**
37. **`tests/parser/while.ts.fixture.ts`** -> AI Confidence: **99.29%**
38. **`tests/tokenizer.js`** -> AI Confidence: **99.17%**
39. **`std/assembly/symbol.ts`** -> AI Confidence: **99.17%**
40. **`std/assembly/util/memory.ts`** -> AI Confidence: **99.17%**
41. **`tests/compiler/std/set.ts`** -> AI Confidence: **99.17%**
42. **`tests/parser/for.ts`** -> AI Confidence: **99.17%**
43. **`tests/parser/for.ts.fixture.ts`** -> AI Confidence: **99.17%**
44. **`scripts/build.js`** -> AI Confidence: **99.16%**
45. **`src/builtins.ts`** -> AI Confidence: **99.15%**
46. **`src/passes/shadowstack.ts`** -> AI Confidence: **99.15%**
47. **`std/assembly/array.ts`** -> AI Confidence: **99.15%**
48. **`std/assembly/dataview.ts`** -> AI Confidence: **99.14%**
49. **`scripts/build-dts.js`** -> AI Confidence: **99.13%**
50. **`tests/asconfig/index.js`** -> AI Confidence: **99.13%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `112` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `cli/index.js` (JAVASCRIPT) -> Cumulative Risk: **721.86**
- **Archetype:** `file_cluster_4` (Distance: 13.56 IQR)
- **Magnitude:** 1511.7 | **LOC:** 1291 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9996%), Concurrency (99.9947%), Tech Debt (99.8602%)
- **Heaviest Functions:** `main` (Impact: 512.2), `getFile` (Impact: 59.0), `checkDiagnostics` (Impact: 46.2)

### 2. `src/builtins.ts` (TYPESCRIPT) -> Cumulative Risk: **679.15**
- **Archetype:** `file_cluster_8` (Distance: 13.489 IQR)
- **Magnitude:** 1032.3 | **LOC:** 11395 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9987%), Tech Debt (96.2777%), Safety Score (90.5528%)
- **Heaviest Functions:** `builtin_assert` (Impact: 177.4), `builtin_v128_shuffle` (Impact: 71.5), `builtin_max` (Impact: 61.2)

### 3. `src/bindings/js.ts` (TYPESCRIPT) -> Cumulative Risk: **667.99**
- **Archetype:** `file_cluster_11` (Distance: 14.824 IQR)
- **Magnitude:** 332.93 | **LOC:** 1607 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9759%), Tech Debt (99.9739%)
- **Heaviest Functions:** `build` (Impact: 244.6), `makeLowerToValue` (Impact: 115.5), `makeLiftFromValue` (Impact: 59.6)

### 4. `src/compiler.ts` (TYPESCRIPT) -> Cumulative Risk: **655.98**
- **Archetype:** `file_cluster_11` (Distance: 14.563 IQR)
- **Magnitude:** 1165.41 | **LOC:** 10689 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Safety Score (99.0563%)
- **Heaviest Functions:** `makeAssignment` (Impact: 1067.5), `compileCallDirect` (Impact: 1012.1), `compileIdentifierExpression` (Impact: 892.1)

### 5. `std/assembly/util/bytes.ts` (TYPESCRIPT) -> Cumulative Risk: **643.35**
- **Archetype:** `file_cluster_11` (Distance: 16.455 IQR)
- **Magnitude:** 14.32 | **LOC:** 108 | **CtrlFlow:** 85.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (80.5053%)
- **Heaviest Functions:** `FILL` (Impact: 46.7), `u8` (Impact: 21.6), `REVERSE` (Impact: 16.6)

### 6. `std/assembly/util/uri.ts` (TYPESCRIPT) -> Cumulative Risk: **631.52**
- **Archetype:** `file_cluster_0` (Distance: 14.822 IQR)
- **Magnitude:** 26.37 | **LOC:** 276 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9433%), Cognitive Load (84.6779%)
- **Heaviest Functions:** `encode` (Impact: 66.8), `decode` (Impact: 64.3), `storeHex` (Impact: 13.2)

### 7. `std/assembly/arraybuffer.ts` (TYPESCRIPT) -> Cumulative Risk: **620.2**
- **Archetype:** `file_cluster_13` (Distance: 11.552 IQR)
- **Magnitude:** 8.75 | **LOC:** 78 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Tech Debt (99.4472%), Safety Score (87.0556%)
- **Heaviest Functions:** `isView` (Impact: 30.9), `constructor` (Impact: 5.7), `constructor` (Impact: 5.6)

### 8. `src/program.ts` (TYPESCRIPT) -> Cumulative Risk: **606.8**
- **Archetype:** `file_cluster_13` (Distance: 14.388 IQR)
- **Magnitude:** 381.15 | **LOC:** 5125 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.3717%), Tech Debt (98.1944%)
- **Heaviest Functions:** `doProcessOverride` (Impact: 561.1), `makeNativeFunctionDeclaration` (Impact: 175.9), `initializeExport` (Impact: 161.2)

### 9. `src/bindings/tsd.ts` (TYPESCRIPT) -> Cumulative Risk: **606.41**
- **Archetype:** `file_cluster_13` (Distance: 14.933 IQR)
- **Magnitude:** 96.73 | **LOC:** 416 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9907%), Tech Debt (99.9807%)
- **Heaviest Functions:** `toTypeScriptType` (Impact: 87.6), `build` (Impact: 28.5), `makeRecordType` (Impact: 17.1)

### 10. `std/assembly/string.ts` (TYPESCRIPT) -> Cumulative Risk: **604.92**
- **Archetype:** `file_cluster_2` (Distance: 13.778 IQR)
- **Magnitude:** 106.94 | **LOC:** 848 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.0015%)
- **Heaviest Functions:** `encodeUnsafe` (Impact: 39.5), `decodeUnsafe` (Impact: 38.1), `assert` (Impact: 37.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cli/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.56 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.464 IQR)
- **Top Global Matches:** file_cluster_4: 13.56, file_cluster_17: 13.851, file_cluster_11: 13.987
- **Magnitude:** 1511.7 | **LOC:** 1291 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (86.8046%), Tech Debt (99.8602%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 512.2)
  * `getFile` (Impact: 59.0)
  * `checkDiagnostics` (Impact: 46.2)
  * `getConfig` (Impact: 30.1)
  * `crash` (Impact: 17.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 321`, `structural_boundaries: 264`, `args: 52`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 1`, `state_mutation: 432`, `dead_code: 7`, `planned_debt: 1`, `duplicate_logic: 25`
* *Architecture:* `io: 46`, `api: 17`, `concurrency: 157`, `import: 12`
* *Defense:* `safety: 102`, `doc: 16`, `immutability_locks: 93`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` index.generated.js, assemblyscript, text.js, options.js, binaryen.js, index.js, terminal.js, node.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/compiler.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.563 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.724 IQR)
- **Top Global Matches:** file_cluster_11: 14.563, file_cluster_13: 14.637, file_cluster_8: 14.64
- **Magnitude:** 1165.41 | **LOC:** 10689 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (54.6547%), Tech Debt (94.8836%)
**Top Internal Functions/Classes:**
  * `makeAssignment` (Impact: 1067.5)
    * *Intent:* /** Adds an array header to static memory and returns the created segment. */
  * `compileCallDirect` (Impact: 1012.1)
  * `compileIdentifierExpression` (Impact: 892.1)
  * `assert` (Impact: 857.0)
  * `finalizeAnyInstanceOf` (Impact: 720.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 924`, `structural_boundaries: 653`, `args: 147`, `func_start: 147`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 3030`, `dead_code: 10`, `planned_debt: 29`, `duplicate_logic: 47`
* *Architecture:* `io: 2`, `api: 34`, `import: 14`
* *Defense:* `safety: 32`, `doc: 156`, `test: 98`, `immutability_locks: 18`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` builtins, js, flow, resolver, module, shadowstack, ast, common...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/builtins.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.489 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.271 IQR)
- **Top Global Matches:** file_cluster_8: 13.489, file_cluster_7: 13.882, file_cluster_13: 13.884
- **Magnitude:** 1032.3 | **LOC:** 11395 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (86.6596%), Tech Debt (96.2777%)
**Top Internal Functions/Classes:**
  * `builtin_assert` (Impact: 177.4)
  * `builtin_v128_shuffle` (Impact: 71.5)
  * `builtin_max` (Impact: 61.2)
  * `builtin_min` (Impact: 61.2)
  * `assert` (Impact: 60.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1550`, `structural_boundaries: 3678`, `args: 1405`, `func_start: 1401`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 3692`, `dead_code: 1`, `planned_debt: 11`, `fragile_debt: 1`, `duplicate_logic: 149`
* *Architecture:* `api: 642`, `import: 10`
* *Defense:* `safety: 37`, `doc: 35`, `test: 44`, `immutability_locks: 619`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` flow, program, compiler, resolver, module, ast, common, util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `util/browser/path.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.025 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.373 IQR)
- **Top Global Matches:** file_cluster_8: 14.025, file_cluster_17: 14.083, file_cluster_0: 14.096
- **Magnitude:** 645.38 | **LOC:** 521 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.0364%), Tech Debt (94.1029%)
**Top Internal Functions/Classes:**
  * `normalizeStringPosix` (Impact: 65.6)
    * *Intent:* // Resolves . and .. elements in a path with directory names
  * `relative` (Impact: 65.2)
  * `parse` (Impact: 60.9)
  * `basename` (Impact: 53.7)
  * `extname` (Impact: 35.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 109`, `args: 13`, `func_start: 23`
* *Risk/State:* `state_mutation: 178`, `duplicate_logic: 8`
* *Architecture:* `io: 72`, `api: 20`, `import: 2`
* *Defense:* `safety: 98`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` process.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/compiler.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.739 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.903 IQR)
- **Top Global Matches:** file_cluster_4: 11.739, file_cluster_13: 11.74, file_cluster_8: 11.741
- **Magnitude:** 512.4 | **LOC:** 657 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.8553%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `runTest` (Impact: 139.4)
    * *Intent:* // Runs a single test
  * `testInstantiate` (Impact: 46.1)
  * `prepareResult` (Impact: 43.4)
    * *Intent:* // Makes sure to reset the environment after
  * `evaluateResult` (Impact: 25.3)
  * `section` (Impact: 14.6)
    * *Intent:* // Starts a new section within a test
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 109`, `args: 35`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 120`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 14`, `api: 18`, `concurrency: 39`, `import: 17`
* *Defense:* `safety: 9`, `test: 1`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cluster, glob, text.js, options.js, asc.js, features.json, os, url...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/compiler/bindings/esm.debug.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.441 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.78 IQR)
- **Top Global Matches:** file_cluster_8: 11.441, file_cluster_0: 11.919, file_cluster_4: 11.943
- **Magnitude:** 439.72 | **LOC:** 562 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.1268%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__lowerStaticArray` (Impact: 12.9)
  * `arrayOfStringsFunction` (Impact: 12.6)
  * `__release` (Impact: 12.5)
  * `await` (Impact: 12.2)
  * `__lowerRecord13` (Impact: 11.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 108`, `args: 71`, `func_start: 88`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 36`, `duplicate_logic: 9`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 44`, `concurrency: 9`, `import: 1`
* *Defense:* `safety: 53`, `immutability_locks: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/compiler/bindings/esm.release.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.441 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.78 IQR)
- **Top Global Matches:** file_cluster_8: 11.441, file_cluster_0: 11.919, file_cluster_4: 11.943
- **Magnitude:** 439.72 | **LOC:** 562 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.1268%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__lowerStaticArray` (Impact: 12.9)
  * `arrayOfStringsFunction` (Impact: 12.6)
  * `__release` (Impact: 12.5)
  * `await` (Impact: 12.2)
  * `__lowerRecord13` (Impact: 11.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 108`, `args: 71`, `func_start: 88`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 36`, `duplicate_logic: 9`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 44`, `concurrency: 9`, `import: 1`
* *Defense:* `safety: 53`, `immutability_locks: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/passes/pass.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.782 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.81 IQR)
- **Top Global Matches:** file_cluster_8: 14.782, file_cluster_13: 15.076, file_cluster_11: 15.11
- **Magnitude:** 438.72 | **LOC:** 2121 | **CtrlFlow:** 78.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.9137%), Tech Debt (99.7301%)
**Top Internal Functions/Classes:**
  * `replaceChild` (Impact: 572.0)
  * `visit` (Impact: 333.3)
  * `assert` (Impact: 21.6)
  * `_BinaryenArrayLenSetRef` (Impact: 17.2)
  * `_BinaryenBlockSetChildAt` (Impact: 15.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 450`, `structural_boundaries: 125`, `args: 272`, `func_start: 272`, `class_start: 2`
* *Risk/State:* `state_mutation: 1948`, `duplicate_logic: 64`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 91`, `doc: 20`, `test: 66`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004618
  * `Imports (Out-Degree: 1):` binaryen, module
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `util/options.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.629 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.25 IQR)
- **Top Global Matches:** file_cluster_17: 12.629, file_cluster_8: 12.934, file_cluster_13: 12.978
- **Magnitude:** 433.1 | **LOC:** 263 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.171%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 159.8)
    * *Intent:* // type | meaning // -----|--------------- // b | boolean // i | integer // f | float // s | string ...
  * `merge` (Impact: 63.5)
  * `sanitizeValue` (Impact: 36.0)
  * `help` (Impact: 33.3)
  * `resolvePath` (Impact: 10.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 66`, `args: 20`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 105`
* *Architecture:* `io: 5`, `api: 8`, `import: 2`
* *Defense:* `safety: 13`, `doc: 8`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` terminal.js, node.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/compiler/bindings/raw.debug.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.533 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.813 IQR)
- **Top Global Matches:** file_cluster_8: 11.533, file_cluster_0: 12.03, file_cluster_7: 12.112
- **Magnitude:** 419.74 | **LOC:** 523 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.5041%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__lowerStaticArray` (Impact: 12.9)
  * `arrayOfStringsFunction` (Impact: 12.6)
  * `__release` (Impact: 12.5)
  * `__lowerRecord13` (Impact: 11.6)
  * `bufferFunction` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 97`, `args: 70`, `func_start: 87`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 36`, `duplicate_logic: 9`, `orphaned_logic: 2`
* *Architecture:* `api: 44`, `concurrency: 2`
* *Defense:* `safety: 52`, `immutability_locks: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/compiler/bindings/raw.release.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.533 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.813 IQR)
- **Top Global Matches:** file_cluster_8: 11.533, file_cluster_0: 12.03, file_cluster_7: 12.112
- **Magnitude:** 419.74 | **LOC:** 523 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.5041%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__lowerStaticArray` (Impact: 12.9)
  * `arrayOfStringsFunction` (Impact: 12.6)
  * `__release` (Impact: 12.5)
  * `__lowerRecord13` (Impact: 11.6)
  * `bufferFunction` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 97`, `args: 70`, `func_start: 87`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 36`, `duplicate_logic: 9`, `orphaned_logic: 2`
* *Architecture:* `api: 44`, `concurrency: 2`
* *Defense:* `safety: 52`, `immutability_locks: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/build-dts.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.337 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.963 IQR)
- **Top Global Matches:** file_cluster_13: 11.337, file_cluster_8: 11.447, file_cluster_11: 11.482
- **Magnitude:** 384.86 | **LOC:** 394 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.9246%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `generate` (Impact: 75.5)
  * `transformTypes` (Impact: 32.5)
    * *Intent:* // prefix the import with options.prefix, so that both non-relative imports
  * `debug` (Impact: 32.2)
    * *Intent:* // prefix the import with options.prefix, so that both non-relative imports // and relative imports ...
  * `visit` (Impact: 31.9)
    * *Intent:* // prefix the import with options.prefix, so that both non-relative imports // and relative imports ...
  * `writeDeclaration` (Impact: 26.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 42`, `args: 22`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 42`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 25`
* *Architecture:* `io: 12`, `api: 4`, `import: 6`
* *Defense:* `safety: 9`, `doc: 5`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` util, typescript, glob, url, path, fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.358 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.19 IQR)
- **Top Global Matches:** file_cluster_8: 13.358, file_cluster_13: 13.673, file_cluster_11: 13.7
- **Magnitude:** 383.21 | **LOC:** 4588 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.5681%), Tech Debt (14.8606%)
**Top Internal Functions/Classes:**
  * `parseExpressionStart` (Impact: 261.8)
  * `assert` (Impact: 184.6)
  * `parseExpression` (Impact: 161.6)
  * `parseTopLevelStatement` (Impact: 132.4)
  * `determinePrecedence` (Impact: 96.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 804`, `structural_boundaries: 302`, `args: 56`, `func_start: 55`, `class_start: 2`
* *Risk/State:* `state_mutation: 1734`, `dead_code: 8`, `planned_debt: 4`, `duplicate_logic: 5`
* *Architecture:* `io: 17`, `api: 6`, `import: 5`
* *Defense:* `safety: 5`, `doc: 22`, `test: 12`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` file, : Identifier (, ast, common, util, StringLiteral)?, tokenizer, StringLiteral...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/program.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.388 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.22 IQR)
- **Top Global Matches:** file_cluster_13: 14.388, file_cluster_11: 14.549, file_cluster_2: 14.627
- **Magnitude:** 381.15 | **LOC:** 5125 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (47.4797%), Tech Debt (98.1944%)
**Top Internal Functions/Classes:**
  * `doProcessOverride` (Impact: 561.1)
    * *Intent:* // TODO: for (let [exportName, queuedExport] of exports) {
  * `makeNativeFunctionDeclaration` (Impact: 175.9)
  * `initializeExport` (Impact: 161.2)
  * `fromDecorator` (Impact: 147.6)
  * `assert` (Impact: 121.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 482`, `structural_boundaries: 260`, `args: 141`, `func_start: 141`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1427`, `dead_code: 5`, `planned_debt: 7`, `fragile_debt: 1`, `duplicate_logic: 31`
* *Architecture:* `io: 1`, `api: 102`, `import: 29`
* *Defense:* `safety: 16`, `doc: 236`, `test: 35`, `immutability_locks: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 68.197
  * `Choke Point (Betweenness):` 0.00035 | `Ripple Effect (Closeness):` 0.036439
  * `Imports (Out-Degree: 3):` parser, builtins, flow, compiler, resolver, foo, module, bar...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/bindings/js.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.824 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.017 IQR)
- **Top Global Matches:** file_cluster_11: 14.824, file_cluster_4: 14.85, file_cluster_13: 14.888
- **Magnitude:** 332.93 | **LOC:** 1607 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.2603%), Tech Debt (99.9739%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 244.6)
    * *Intent:* // not implemented // let sb = this.sb; // sb.push("export const "); // sb.push(name); // sb.push(" ...
  * `makeLowerToValue` (Impact: 115.5)
  * `makeLiftFromValue` (Impact: 59.6)
  * `assert` (Impact: 49.8)
  * `indent` (Impact: 43.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 397`, `structural_boundaries: 201`, `args: 142`, `func_start: 134`, `class_start: 2`
* *Risk/State:* `state_mutation: 2076`, `dead_code: 3`, `planned_debt: 5`, `duplicate_logic: 40`
* *Architecture:* `io: 2`, `api: 37`, `concurrency: 44`, `import: 8`
* *Defense:* `safety: 24`, `doc: 11`, `test: 13`, `immutability_locks: 26`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.705
  * `Choke Point (Betweenness):` 0.000672 | `Ripple Effect (Closeness):` 0.043464
  * `Imports (Out-Degree: 2):` compiler, ast, types, util, promises, util, program, common
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `src/extra/ast.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.383 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.61 IQR)
- **Top Global Matches:** file_cluster_8: 15.383, file_cluster_17: 15.445, file_cluster_11: 15.454
- **Magnitude:** 321.38 | **LOC:** 1631 | **CtrlFlow:** 87.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.4869%), Tech Debt (78.7592%)
**Top Internal Functions/Classes:**
  * `visitNode` (Impact: 222.1)
  * `visitClassDeclaration` (Impact: 43.3)
  * `visitFunctionCommon` (Impact: 42.0)
  * `visitLiteralExpression` (Impact: 33.0)
  * `visitExportDefaultStatement` (Impact: 23.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 414`, `structural_boundaries: 57`, `args: 114`, `func_start: 112`, `class_start: 1`
* *Risk/State:* `state_mutation: 2119`, `duplicate_logic: 23`
* *Architecture:* `io: 5`, `api: 14`, `import: 4`
* *Defense:* `safety: 77`, `doc: 3`, `test: 17`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` );
    this.visitIdentifierExpression(node.externalName);
    sb.push(, ast, );
    let declarations = node.declarations;
    let namespaceName = node.namespaceName;
    if (declarations) 
      let numDeclarations = declarations.length;
      if (numDeclarations) 
        sb.push(, util, tokenizer, );
     else if (node.is(CommonFlags.Declare)) 
      sb.push(, common
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tokenizer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.326 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 2.964 IQR)
- **Top Global Matches:** file_cluster_8: 13.326, file_cluster_13: 13.638, file_cluster_11: 13.673
- **Magnitude:** 284.19 | **LOC:** 1798 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.4357%), Tech Debt (56.3251%)
**Top Internal Functions/Classes:**
  * `tokenFromKeyword` (Impact: 296.5)
    * *Intent:* // meta
  * `unsafeNext` (Impact: 287.3)
  * `assert` (Impact: 211.9)
  * `operatorTokenToString` (Impact: 108.8)
  * `readEscapeSequence` (Impact: 67.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 600`, `structural_boundaries: 270`, `args: 56`, `func_start: 55`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1251`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 12`
* *Architecture:* `api: 30`, `concurrency: 2`, `import: 3`
* *Defense:* `safety: 11`, `doc: 11`, `test: 5`, `immutability_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util, ) return Token.Import;
          break;
        
        case CharCode.t: 
          if (text ==, ast, diagnostics
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `std/portable/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.171 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.729 IQR)
- **Top Global Matches:** file_cluster_8: 12.171, file_cluster_12: 12.627, file_cluster_17: 12.643
- **Magnitude:** 250.66 | **LOC:** 417 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (88.3516%), Tech Debt (99.9944%)
**Top Internal Functions/Classes:**
  * `defaultComparator` (Impact: 14.5)
  * `isArrayLike` (Impact: 9.0)
  * `AssertionError` (Impact: 7.3)
  * `fromCharCodes` (Impact: 6.0)
  * `fromCodePoints` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 68`, `args: 57`, `func_start: 63`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 83`, `planned_debt: 1`, `duplicate_logic: 11`
* *Architecture:* None
* *Defense:* `safety: 26`, `doc: 2`, `test: 2`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/module.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.572 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.277 IQR)
- **Top Global Matches:** file_cluster_8: 13.572, file_cluster_7: 13.611, file_cluster_13: 13.664
- **Magnitude:** 234.31 | **LOC:** 4010 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.5957%), Tech Debt (86.957%)
**Top Internal Functions/Classes:**
  * `binary` (Impact: 159.9)
  * `maybeDropCondition` (Impact: 83.5)
  * `prepareType` (Impact: 80.3)
  * `tryEnsureBasicType` (Impact: 58.4)
  * `readStringCached` (Impact: 52.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 357`, `structural_boundaries: 561`, `args: 172`, `func_start: 172`, `class_start: 5`
* *Risk/State:* `state_mutation: 903`, `dead_code: 5`, `planned_debt: 7`, `fragile_debt: 4`, `duplicate_logic: 21`
* *Architecture:* `api: 268`, `import: 6`
* *Defense:* `safety: 10`, `doc: 504`, `test: 20`, `immutability_locks: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` builtins, binaryen, common, util, types, program
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `std/assembly/math.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.856 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.131 IQR)
- **Top Global Matches:** file_cluster_8: 12.856, file_cluster_0: 12.914, file_cluster_11: 13.209
- **Magnitude:** 196.62 | **LOC:** 3290 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.702%), Tech Debt (83.4292%)
**Top Internal Functions/Classes:**
  * `atan2` (Impact: 54.1)
  * `rem` (Impact: 51.9)
  * `rem` (Impact: 51.7)
  * `atan` (Impact: 49.2)
  * `ipow64` (Impact: 47.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 441`, `structural_boundaries: 300`, `args: 73`, `func_start: 73`
* *Risk/State:* `state_mutation: 821`, `dead_code: 5`, `planned_debt: 4`, `duplicate_logic: 10`, `orphaned_logic: 23`
* *Architecture:* `api: 72`, `import: 3`
* *Defense:* `safety: 3`, `doc: 12`, `immutability_locks: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math, dom, builtins
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `std/assembly/builtins.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.215 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.564 IQR)
- **Top Global Matches:** file_cluster_0: 10.215, file_cluster_8: 10.864, file_cluster_16: 11.052
- **Magnitude:** 165.71 | **LOC:** 2632 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.8183%), Tech Debt (97.6185%)
**Top Internal Functions/Classes:**
  * `v128` (Impact: 245.7)
    * *Intent:* // @ts-ignore: decorator
  * `i64` (Impact: 130.1)
    * *Intent:* // @ts-ignore: decorator
  * `i32` (Impact: 99.5)
    * *Intent:* // @ts-ignore: decorator
  * `store` (Impact: 95.2)
    * *Intent:* // @ts-ignore: decorator
  * `store` (Impact: 73.1)
    * *Intent:* // @ts-ignore: decorator
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 1254`, `args: 574`, `func_start: 574`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`, `fragile_debt: 1`, `duplicate_logic: 22`
* *Architecture:* `api: 646`, `import: 1`
* *Defense:* `safety: 27`, `doc: 2`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` string
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/glue/js/i64.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.691 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.271 IQR)
- **Top Global Matches:** file_cluster_8: 10.691, file_cluster_7: 11.294, file_cluster_13: 11.328
- **Magnitude:** 160.14 | **LOC:** 235 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.6381%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `i64_pow` (Impact: 20.3)
  * `i64_is_i8` (Impact: 10.6)
  * `i64_is_i16` (Impact: 10.6)
  * `i64_is_i32` (Impact: 7.1)
  * `i64_align` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 57`, `args: 47`, `func_start: 95`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 16`
* *Architecture:* `import: 1`
* *Defense:* `safety: 10`, `doc: 1`, `test: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` long
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/allocators/runner.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.254 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.269 IQR)
- **Top Global Matches:** file_cluster_17: 16.254, file_cluster_0: 16.3, file_cluster_11: 16.369
- **Magnitude:** 155.82 | **LOC:** 118 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (41.0733%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `runner` (Impact: 54.8)
  * `randomAlloc` (Impact: 11.0)
  * `testMemChanged` (Impact: 8.9)
  * `preciseFree` (Impact: 5.6)
  * `randomFree` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 16`, `args: 5`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 51`, `dead_code: 2`, `duplicate_logic: 5`
* *Architecture:* `api: 5`
* *Defense:* `safety: 16`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/glue/binaryen.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.728 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.558 IQR)
- **Top Global Matches:** file_cluster_8: 12.728, file_cluster_16: 13.129, file_cluster_2: 13.217
- **Magnitude:** 153.91 | **LOC:** 958 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1842`, `args: 797`, `func_start: 797`
* *Risk/State:* None
* *Architecture:* `api: 826`, `import: 2`
* *Defense:* `safety: 307`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/glue/wasm/float.ts` (TYPESCRIPT) | Magnitude: 1.27 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: decorators: 8, structural_boundaries: 4, args: 4, func_start: 4
- `std/assembly/typedarray.ts` (TYPESCRIPT) | Magnitude: 150.19 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 1450, state_mutation: 560, structural_boundaries: 516, func_start: 487
- `tests/compiler/rt/finalize.ts` (TYPESCRIPT) | Magnitude: 0.66 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 4, func_start: 4, structural_boundaries: 3, state_mutation: 2
- `std/assembly/function.ts` (TYPESCRIPT) | Magnitude: 1.08 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 8, args: 5, func_start: 5
- `tests/parser/function.ts` (TYPESCRIPT) | Magnitude: 0.92 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 5, func_start: 5, orphaned_logic: 5, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `eslint.config.js` (JAVASCRIPT) | Magnitude: 8.66 | Delta: **0.295 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 177, doc: 51, events: 45, decorators: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/bindings/js.ts` (TYPESCRIPT) | Magnitude: 332.93 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 2076, indent_spaces: 1371, branch: 397, structural_boundaries: 201
- `src/passes/shadowstack.ts` (TYPESCRIPT) | Magnitude: 81.53 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 578, indent_spaces: 407, structural_boundaries: 103, branch: 58
- `src/bindings/util.ts` (TYPESCRIPT) | Magnitude: 30.17 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 169, state_mutation: 155, branch: 65, args: 18
- `src/compiler.ts` (TYPESCRIPT) | Magnitude: 1165.41 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 3603, state_mutation: 3030, branch: 924, structural_boundaries: 653
- `std/assembly/util/bytes.ts` (TYPESCRIPT) | Magnitude: 14.32 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 85, state_mutation: 30, branch: 24, generics: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `std/assembly/rt/rtrace.ts` (TYPESCRIPT) | Magnitude: 4.58 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 19, args: 9, func_start: 9, api: 9
- `tests/allocators/index.js` (JAVASCRIPT) | Magnitude: 62.78 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 15, state_mutation: 13, branch: 10
- `src/resolver.ts` (TYPESCRIPT) | Magnitude: 114.72 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 798, state_mutation: 446, branch: 192, structural_boundaries: 151
- `util/browser/url.js` (JAVASCRIPT) | Magnitude: 13.32 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 5, regex_execution: 5, io: 4
- `src/util/path.ts` (TYPESCRIPT) | Magnitude: 9.52 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 84, branch: 33, io: 28, state_mutation: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `std/assembly/set.ts` (TYPESCRIPT) | Magnitude: 25.75 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 179, indent_spaces: 145, generics: 34, branch: 23
- `tests/compiler/std/pointer.ts` (TYPESCRIPT) | Magnitude: 1.28 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 49, generics: 36, args: 29, func_start: 29
- `tests/compiler/function-types.ts` (TYPESCRIPT) | Magnitude: 1.26 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 15, func_start: 13, structural_boundaries: 12, generics: 9
- `src/util/collections.ts` (TYPESCRIPT) | Magnitude: 17.63 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 122, indent_spaces: 85, structural_boundaries: 16, branch: 15
- `tests/compiler/instanceof.ts` (TYPESCRIPT) | Magnitude: 8.07 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: args: 232, func_start: 232, generics: 151, test: 91

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/compiler/merge.ts` (TYPESCRIPT) | Magnitude: 4.7 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 36, args: 18, func_start: 18, safety: 16
- `tests/allocators/runner.js` (JAVASCRIPT) | Magnitude: 155.82 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 73, state_mutation: 51, branch: 27, structural_boundaries: 16
- `util/cpu.js` (JAVASCRIPT) | Magnitude: 10.5 | Delta: **0.228 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 10, immutability_locks: 9, branch: 7
- `util/find.js` (JAVASCRIPT) | Magnitude: 31.06 | Delta: **0.27 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 9, indent_spaces: 9, structural_boundaries: 7, branch: 6
- `util/options.js` (JAVASCRIPT) | Magnitude: 433.1 | Delta: **0.305 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 203, branch: 148, state_mutation: 105, structural_boundaries: 66

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `std/assembly/string.ts` (TYPESCRIPT) | Magnitude: 106.94 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 553, state_mutation: 456, branch: 144, structural_boundaries: 121
- `tests/compiler/NonNullable.ts` (TYPESCRIPT) | Magnitude: 0.97 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: args: 10, func_start: 10, generics: 7, test: 5
- `tests/compiler/std/typedarray.ts` (TYPESCRIPT) | Magnitude: 38.74 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 507, args: 420, func_start: 406, generics: 362
- `scripts/hexfloat.html` (HTML) | Magnitude: 30.76 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 29, args: 12, structural_boundaries: 11, state_mutation: 9
- `util/web.d.ts` (TYPESCRIPT) | Magnitude: 0.73 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: args: 4, func_start: 4, concurrency: 4, doc: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/compiler.js` (JAVASCRIPT) | Magnitude: 512.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 499, branch: 138, state_mutation: 120, structural_boundaries: 109
- `scripts/build-web.js` (JAVASCRIPT) | Magnitude: 32.96 | Delta: **0.185 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, state_mutation: 12, io: 10, structural_boundaries: 9
- `bin/asc.js` (JAVASCRIPT) | Magnitude: 16.12 | Delta: **0.253 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, branch: 10, concurrency: 8, immutability_locks: 8
- `cli/index.js` (JAVASCRIPT) | Magnitude: 1511.7 | Delta: **0.291 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 1000, state_mutation: 432, branch: 321, structural_boundaries: 264
- `util/node.js` (JAVASCRIPT) | Magnitude: 56.52 | Delta: **0.391 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 25, concurrency: 24, state_mutation: 15, indent_spaces: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `tests/compiler/call-inferred.ts` (TYPESCRIPT) | Magnitude: 1.77 | Delta: **0.126 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: args: 13, func_start: 13, generics: 9, indent_spaces: 9
- `std/assembly/object.ts` (TYPESCRIPT) | Magnitude: 1.25 | Delta: **0.339 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 5, args: 5, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `util/cpu.d.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, api: 2, immutability_locks: 2
- `src/util/vector.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.143 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, api: 2, memory_alloc: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `util/terminal.js` (JAVASCRIPT) | Magnitude: 90.14 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 42, structural_boundaries: 23, api: 20, branch: 13
- `std/assembly/date.ts` (TYPESCRIPT) | Magnitude: 39.43 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 268, state_mutation: 263, structural_boundaries: 38, branch: 36
- `src/flow.ts` (TYPESCRIPT) | Magnitude: 96.91 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 534, state_mutation: 472, branch: 212, structural_boundaries: 54
- `tests/compiler/infer-generic.ts` (TYPESCRIPT) | Magnitude: 3.84 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 32, args: 24, func_start: 17, indent_spaces: 14
- `tests/compiler/bindings/esm.ts` (TYPESCRIPT) | Magnitude: 14.56 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 69, api: 46, state_mutation: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tests/compiler/resolve-ternary.ts` (TYPESCRIPT) | Magnitude: 0.76 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 15, args: 9, func_start: 9, branch: 5
- `tests/compiler/issues/2166.ts` (TYPESCRIPT) | Magnitude: 1.08 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 12, args: 9, func_start: 9, generics: 9

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/compiler.ts` -> Churn: **100.0%** | Cog Load: 54.6547% | Debt: 94.8836%
- `bin/asinit.js` -> Churn: **52.83%** | Cog Load: 11.5453% | Debt: 78.6145%
- `src/program.ts` -> Churn: **52.83%** | Cog Load: 47.4797% | Debt: 98.1944%
- `src/resolver.ts` -> Churn: **52.83%** | Cog Load: 44.3404% | Debt: 94.7665%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `cli/index.js` -> **Max Graey** (100.0% isolated ownership) | Magnitude: 1511.7
- `src/builtins.ts` -> **Congcong Cai** (100.0% isolated ownership) | Magnitude: 1032.3
- `std/portable/index.js` -> **Max Graey** (100.0% isolated ownership) | Magnitude: 250.66
- `src/module.ts` -> **Congcong Cai** (100.0% isolated ownership) | Magnitude: 234.31
- `tests/allocators/runner.js` -> **Max Graey** (100.0% isolated ownership) | Magnitude: 155.82

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/bindings/js.ts` -> **Severity: 0.067** (Bridge: 0.0007 * Flux: 100.0%)
- `src/program.ts` -> **Severity: 0.035** (Bridge: 0.0003 * Flux: 100.0%)
- `src/types.ts` -> **Severity: 0.019** (Bridge: 0.0002 * Flux: 100.0%)
- `util/browser/url.js` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 100.0%)
- `util/text.js` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/bindings/js.ts` -> **Severity: 4.345** (Embedded: 0.0435 * Error Risk: 99.9759%)
- `src/program.ts` -> **Severity: 3.585** (Embedded: 0.0364 * Error Risk: 98.3717%)
- `src/types.ts` -> **Severity: 3.489** (Embedded: 0.0357 * Error Risk: 97.6878%)
- `src/flow.ts` -> **Severity: 2.497** (Embedded: 0.0252 * Error Risk: 98.9986%)
- `src/resolver.ts` -> **Severity: 2.375** (Embedded: 0.0251 * Error Risk: 94.7917%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/bindings/js.ts` -> **Severity: 1248.83** (Blast Radius: 48.705 * Doc Risk: 25.6407%)
- `src/program.ts` -> **Severity: 1016.163** (Blast Radius: 68.197 * Doc Risk: 14.9004%)
- `src/types.ts` -> **Severity: 725.243** (Blast Radius: 60.841 * Doc Risk: 11.9203%)
- `std/assembly/bindings/dom.ts` -> **Severity: 616.299** (Blast Radius: 6.163 * Doc Risk: 99.9999%)
- `src/glue/binaryen.js` -> **Severity: 421.013** (Blast Radius: 31.931 * Doc Risk: 13.1851%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
