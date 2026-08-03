# ARCHITECTURAL_BRIEF: assemblyscript
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/assemblyscript` |
| **Timestamp** | `2026-08-03T19:53:50.230640+00:00` |
| **Scan Duration** | `3.02s` |
| **Git Branch** | `main` |
| **Git Commit** | `be8e56d524a4deccfb6f2242b93a6d30fcf1a589` |
| **Git Remote** | `https://github.com/AssemblyScript/assemblyscript.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 507 malicious artifacts.

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
| Total Artifacts | 1274 |
| Analyzed Artifacts (Scanned) | 694 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 580 |
| Total LOC | 72578 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 54.5% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6987 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
> **Architectural Drift Z-Score:** `6.51`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 527 | 75.9% |
| file_cluster_13 | 35 | 5.0% |
| file_cluster_0 | 35 | 5.0% |
| file_cluster_16 | 28 | 4.0% |
| file_cluster_2 | 11 | 1.6% |
| file_cluster_4 | 6 | 0.9% |
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
| Error & Exception Exposure | 0.0 | 100.0 | 21.7 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 6.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 6.5 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.6 | 3.1 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 10.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.4 | 1.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 69.2 | 80.0 | 100.0 |
| Instability Exposure | 0.0 | 6.7 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 9.0 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 7.0 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `compileTopLevelStatement` (@ `src/compiler.ts`) -> Impact: **3022.4** | LOC: 1558
- `doProcessOverride` (@ `src/program.ts`) -> Impact: **1312.4** | LOC: 1204
  * *Intent:* // TODO: for (let [exportName, queuedExport] of exports) {
- `visit` (@ `src/passes/pass.ts`) -> Impact: **1242.6** | LOC: 603
- `main` (@ `cli/index.js`) -> Impact: **1208.5** | LOC: 961
- `replaceChild` (@ `src/passes/pass.ts`) -> Impact: **838.0** | LOC: 799
- `unsafeNext` (@ `src/tokenizer.ts`) -> Impact: **817.3** | LOC: 445
- `parseExpression` (@ `src/parser.ts`) -> Impact: **764.3** | LOC: 218
- `parseExpressionStart` (@ `src/parser.ts`) -> Impact: **749.3** | LOC: 362
- `compileModuleExport` (@ `src/compiler.ts`) -> Impact: **558.8** | LOC: 136
- `compileUnaryPrefixExpression` (@ `src/compiler.ts`) -> Impact: **501.8** | LOC: 355

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `compileModuleExport` (@ `src/compiler.ts`) -> **O(2^N) [Recursive]**
- `canOverflow` (@ `src/flow.ts`) -> **O(2^N) [Recursive]**
- `compileTopLevelStatement` (@ `src/compiler.ts`) -> **O(2^N) [Recursive]**
- `assert` (@ `src/compiler.ts`) -> **O(2^N) [Recursive]**
- `prepareType` (@ `src/module.ts`) -> **O(2^N) [Recursive]**
- `parseExpression` (@ `src/parser.ts`) -> **O(2^N) [Recursive]**
- `resolve` (@ `util/web.js`) -> **O(2^N) [Recursive]**
- `toTypeScriptType` (@ `src/bindings/tsd.ts`) -> **O(2^N) [Recursive]**
- `hasCompiledMember` (@ `src/bindings/util.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* // Helpers /** Tests if a namespace-like element has at least one compiled member. */
- `assert` (@ `src/compiler.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `visit` (@ `src/passes/pass.ts`) -> DB Complexity: **488**
- `compileTopLevelStatement` (@ `src/compiler.ts`) -> DB Complexity: **487**
- `build` (@ `src/bindings/js.ts`) -> DB Complexity: **291**
  * *Intent:* // not implemented // let sb = this.sb; // sb.push("export const "); // sb.push(name); // sb.push(" = ");
- `main` (@ `cli/index.js`) -> DB Complexity: **254**
- `doProcessOverride` (@ `src/program.ts`) -> DB Complexity: **224**
  * *Intent:* // TODO: for (let [exportName, queuedExport] of exports) {
- `makeNativeFunctionDeclaration` (@ `src/program.ts`) -> DB Complexity: **138**
- `replaceChild` (@ `src/passes/pass.ts`) -> DB Complexity: **129**
- `testI32` (@ `tests/compiler/many-locals.ts`) -> DB Complexity: **128**
- `testI8` (@ `tests/compiler/many-locals.ts`) -> DB Complexity: **128**
- `maybeDropCondition` (@ `src/module.ts`) -> DB Complexity: **111**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 7 | 5030.78 | 1.12% | 2.81% |
| `src` | 21 | 4086.84 | 28.58% | 19.6% |
| `tests/compiler/bindings` | 20 | 3013.05 | 8.85% | 0.0% |
| `cli` | 5 | 2043.69 | 21.06% | 20.18% |
| `tests/compiler` | 228 | 1495.26 | 7.18% | 0.0% |
| `util` | 16 | 1086.45 | 26.31% | 15.86% |
| `std/assembly` | 34 | 940.2 | 31.44% | 63.81% |
| `util/browser` | 5 | 898.46 | 46.07% | 0.0% |
| `tests` | 5 | 673.26 | 17.56% | 0.0% |
| `scripts` | 9 | 629.22 | 45.31% | 15.65% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/ast.ts` -> **100.0%** Exposure
- `src/glue/js/node.d.ts` -> **100.0%** Exposure
- `std/assembly/dataview.ts` -> **100.0%** Exposure
- `std/assembly/error.ts` -> **100.0%** Exposure
- `std/assembly/function.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `scripts/unicode-identifier.js` -> **100.0%** Exposure
- `scripts/update-constants.js` -> **100.0%** Exposure
- `util/browser/path.js` -> **100.0%** Exposure
- `util/browser/process.js` -> **100.0%** Exposure
- `util/browser/url.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `std/assembly/typedarray.ts` -> **0** Orphaned Functions | **250** Duplicates
- `src/ast.ts` -> **0** Orphaned Functions | **85** Duplicates
- `std/assembly/number.ts` -> **0** Orphaned Functions | **34** Duplicates
- `std/assembly/math.ts` -> **23** Orphaned Functions | **10** Duplicates
- `tests/compiler/field-initialization.ts` -> **0** Orphaned Functions | **24** Duplicates

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

### Obfuscation & Evasion Surface
- `tests/compiler/std/math.ts` -> **100.0%** Exposure
- `tests/compiler/std/string-casemapping.ts` -> **100.0%** Exposure
- `tests/compiler/std/string.ts` -> **100.0%** Exposure
- `tests/compiler/std/uri.ts` -> **100.0%** Exposure
- `tests/compiler/std/string-encoding.ts` -> **0.3344%** Exposure
### Exploit Generation Surface
- `cli/index.js` -> **100.0%** Exposure
- `scripts/build-dts.js` -> **100.0%** Exposure
- `scripts/build.js` -> **100.0%** Exposure
- `std/portable/index.js` -> **100.0%** Exposure
- `tests/compiler.js` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `cli/index.js` -> **100.0%** Exposure
- `lib/rtrace/bin/rtplot.js` -> **100.0%** Exposure
- `tests/allocators/forever.js` -> **100.0%** Exposure
- `tests/asconfig/index.js` -> **100.0%** Exposure
- `tests/parser.js` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `bin/asinit.js` -> **100.0%** Exposure
- `cli/index.js` -> **100.0%** Exposure
- `scripts/build-dts.js` -> **100.0%** Exposure
- `scripts/build.js` -> **100.0%** Exposure
- `tests/allocators/runner.js` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `112` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `cli/index.js` (JAVASCRIPT) -> Cumulative Risk: **889.32**
- **Archetype:** `file_cluster_4` (Distance: 13.593 IQR)
- **Magnitude:** 2000.8 | **LOC:** 1291 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `main` (Impact: 1208.5), `checkDiagnostics` (Impact: 68.2), `getConfig` (Impact: 44.0)

### 2. `std/assembly/string.ts` (TYPESCRIPT) -> Cumulative Risk: **860.16**
- **Archetype:** `file_cluster_2` (Distance: 13.705 IQR)
- **Magnitude:** 99.75 | **LOC:** 848 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `encodeUnsafe` (Impact: 94.6), `decodeUnsafe` (Impact: 74.1), `toLowerCase` (Impact: 59.4)

### 3. `src/bindings/js.ts` (TYPESCRIPT) -> Cumulative Risk: **839.44**
- **Archetype:** `file_cluster_11` (Distance: 14.857 IQR)
- **Magnitude:** 353.55 | **LOC:** 1607 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `build` (Impact: 463.8), `makeLowerToValue` (Impact: 225.4), `makeLiftFromValue` (Impact: 87.7)

### 4. `src/bindings/tsd.ts` (TYPESCRIPT) -> Cumulative Risk: **792.26**
- **Archetype:** `file_cluster_13` (Distance: 14.953 IQR)
- **Magnitude:** 118.86 | **LOC:** 416 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `toTypeScriptType` (Impact: 337.0), `build` (Impact: 41.2), `makeRecordType` (Impact: 24.9)

### 5. `src/compiler.ts` (TYPESCRIPT) -> Cumulative Risk: **787.34**
- **Archetype:** `file_cluster_11` (Distance: 14.571 IQR)
- **Magnitude:** 858.69 | **LOC:** 10689 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `compileTopLevelStatement` (Impact: 3022.4), `compileModuleExport` (Impact: 558.8), `compileUnaryPrefixExpression` (Impact: 501.8)

### 6. `std/assembly/date.ts` (TYPESCRIPT) -> Cumulative Risk: **783.82**
- **Archetype:** `file_cluster_8` (Distance: 13.208 IQR)
- **Magnitude:** 43.71 | **LOC:** 376 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `fromString` (Impact: 83.9), `toISOString` (Impact: 6.5), `toUTCString` (Impact: 5.4)

### 7. `src/builtins.ts` (TYPESCRIPT) -> Cumulative Risk: **778.85**
- **Archetype:** `file_cluster_8` (Distance: 13.505 IQR)
- **Magnitude:** 974.73 | **LOC:** 11395 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `builtin_assert` (Impact: 345.4), `builtin_v128_shuffle` (Impact: 170.4), `builtin_v128_load_lane` (Impact: 104.2)

### 8. `std/assembly/math.ts` (TYPESCRIPT) -> Cumulative Risk: **756.62**
- **Archetype:** `file_cluster_8` (Distance: 12.866 IQR)
- **Magnitude:** 233.63 | **LOC:** 3290 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `atan2` (Impact: 80.1), `sincos` (Impact: 79.9), `rem` (Impact: 76.1)

### 9. `src/diagnostics.ts` (TYPESCRIPT) -> Cumulative Risk: **755.87**
- **Archetype:** `file_cluster_8` (Distance: 13.4 IQR)
- **Magnitude:** 61.42 | **LOC:** 472 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `formatDiagnosticContext` (Impact: 60.2), `emitDiagnostic` (Impact: 58.5), `equals` (Impact: 42.5)

### 10. `src/tokenizer.ts` (TYPESCRIPT) -> Cumulative Risk: **752.15**
- **Archetype:** `file_cluster_8` (Distance: 13.354 IQR)
- **Magnitude:** 350.11 | **LOC:** 1798 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `unsafeNext` (Impact: 817.3), `tokenFromKeyword` (Impact: 440.5), `operatorTokenToString` (Impact: 108.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cli/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.593 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.224 IQR)
- **Top Global Matches:** file_cluster_4: 13.593, file_cluster_17: 13.88, file_cluster_11: 14.004
- **Magnitude:** 2000.8 | **LOC:** 1291 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 254
- **Risk Profile:** Cognitive Load (86.8421%), Tech Debt (16.2077%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 1208.5 | O(N^4) | DB: 254)
  * `checkDiagnostics` (Impact: 68.2 | O(N^2) | DB: 2)
  * `getConfig` (Impact: 44.0 | O(N^2) | DB: 7)
  * `configToArguments` (Impact: 21.5 | O(N^2) | DB: 3)
    * *Intent:* /** Ensures that an object is a wrapper class instead of just a pointer. */ // function __wrap(ptrOr...
  * `createMemoryStream` (Impact: 10.3 | O(N^1) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 321`, `structural_boundaries: 264`, `args: 52`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 1`, `state_mutation: 430`, `dead_code: 7`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 46`, `api: 16`, `concurrency: 157`, `import: 12`
* *Defense:* `safety: 102`, `doc: 16`, `immutability_locks: 93`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` options.js, text.js, binaryen.js, node.js, terminal.js, assemblyscript, index.generated.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/builtins.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.505 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.282 IQR)
- **Top Global Matches:** file_cluster_8: 13.505, file_cluster_7: 13.898, file_cluster_13: 13.908
- **Magnitude:** 974.73 | **LOC:** 11395 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (63.6583%), Tech Debt (9.2777%)
**Top Internal Functions/Classes:**
  * `builtin_assert` (Impact: 345.4 | O(N^3) | DB: 22)
  * `builtin_v128_shuffle` (Impact: 170.4 | O(N^4) | DB: 22)
  * `builtin_v128_load_lane` (Impact: 104.2 | O(N^3) | DB: 14)
  * `builtin_v128_store_lane` (Impact: 104.2 | O(N^3) | DB: 14)
  * `builtin_abs` (Impact: 100.1 | O(N^4) | DB: 19)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1550`, `structural_boundaries: 3678`, `args: 1405`, `func_start: 1401`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 3714`, `dead_code: 1`, `planned_debt: 11`, `fragile_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 638`, `import: 10`
* *Defense:* `safety: 37`, `doc: 35`, `test: 44`, `immutability_locks: 619`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` diagnostics, util, flow, types, compiler, program, common, ast...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/compiler.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.571 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.739 IQR)
- **Top Global Matches:** file_cluster_11: 14.571, file_cluster_8: 14.636, file_cluster_13: 14.648
- **Magnitude:** 858.69 | **LOC:** 10689 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 487
- **Risk Profile:** Cognitive Load (54.4948%), Tech Debt (27.2753%)
**Top Internal Functions/Classes:**
  * `compileTopLevelStatement` (Impact: 3022.4 | O(2^N) | DB: 487)
  * `compileModuleExport` (Impact: 558.8 | O(2^N) | DB: 45)
  * `compileUnaryPrefixExpression` (Impact: 501.8 | O(N^3) | DB: 94)
  * `compileTypeof` (Impact: 214.2 | O(N^5) | DB: 27)
  * `compile` (Impact: 192.7 | O(N^3) | DB: 82)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 924`, `structural_boundaries: 653`, `args: 148`, `func_start: 147`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 3050`, `dead_code: 10`, `planned_debt: 29`, `duplicate_logic: 9`
* *Architecture:* `io: 2`, `api: 25`, `import: 14`
* *Defense:* `safety: 32`, `doc: 156`, `test: 98`, `immutability_locks: 18`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` diagnostics, util, builtins, flow, js, types, rtrace, program...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `util/browser/path.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.062 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.128 IQR)
- **Top Global Matches:** file_cluster_8: 14.062, file_cluster_17: 14.136, file_cluster_11: 14.141
- **Magnitude:** 833.68 | **LOC:** 521 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 52
- **Risk Profile:** Cognitive Load (94.0364%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `normalizeStringPosix` (Impact: 159.1 | O(N^4) | DB: 25)
    * *Intent:* // Resolves . and .. elements in a path with directory names
  * `basename` (Impact: 104.0 | O(N^3) | DB: 43)
  * `relative` (Impact: 95.5 | O(N^2) | DB: 12)
  * `parse` (Impact: 89.5 | O(N^2) | DB: 52)
  * `extname` (Impact: 51.8 | O(N^2) | DB: 22)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 109`, `args: 13`, `func_start: 23`
* *Risk/State:* `state_mutation: 180`
* *Architecture:* `io: 72`, `api: 20`, `import: 2`
* *Defense:* `safety: 98`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` process.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `util/options.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.629 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.25 IQR)
- **Top Global Matches:** file_cluster_17: 12.629, file_cluster_8: 12.934, file_cluster_13: 12.978
- **Magnitude:** 682.4 | **LOC:** 263 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (64.171%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 315.8 | O(N^3) | DB: 14)
    * *Intent:* // type | meaning // -----|--------------- // b | boolean // i | integer // f | float // s | string ...
  * `merge` (Impact: 123.8 | O(N^3) | DB: 4)
  * `sanitizeValue` (Impact: 53.4 | O(N^2))
  * `help` (Impact: 48.9 | O(N^2) | DB: 17)
  * `resolvePath` (Impact: 10.3 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 66`, `args: 20`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 105`
* *Architecture:* `io: 5`, `api: 8`, `import: 2`
* *Defense:* `safety: 13`, `doc: 8`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` node.js, terminal.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/compiler/bindings/esm.debug.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.441 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.72 IQR)
- **Top Global Matches:** file_cluster_8: 11.441, file_cluster_0: 11.922, file_cluster_4: 11.946
- **Magnitude:** 648.32 | **LOC:** 562 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (11.1268%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `arrayOfStringsFunction` (Impact: 36.9 | O(2^N))
  * `bufferFunction` (Impact: 26.5 | O(2^N))
  * `stringFunction` (Impact: 26.5 | O(2^N))
  * `stringFunctionOptional` (Impact: 26.5 | O(2^N))
  * `typedarrayFunction` (Impact: 26.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 108`, `args: 71`, `func_start: 88`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 36`, `duplicate_logic: 7`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 44`, `concurrency: 9`, `import: 1`
* *Defense:* `safety: 53`, `immutability_locks: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/compiler/bindings/esm.release.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.441 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.72 IQR)
- **Top Global Matches:** file_cluster_8: 11.441, file_cluster_0: 11.922, file_cluster_4: 11.946
- **Magnitude:** 648.32 | **LOC:** 562 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (11.1268%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `arrayOfStringsFunction` (Impact: 36.9 | O(2^N))
  * `bufferFunction` (Impact: 26.5 | O(2^N))
  * `stringFunction` (Impact: 26.5 | O(2^N))
  * `stringFunctionOptional` (Impact: 26.5 | O(2^N))
  * `typedarrayFunction` (Impact: 26.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 108`, `args: 71`, `func_start: 88`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 36`, `duplicate_logic: 7`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 44`, `concurrency: 9`, `import: 1`
* *Defense:* `safety: 53`, `immutability_locks: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/compiler/bindings/raw.debug.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.533 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.749 IQR)
- **Top Global Matches:** file_cluster_8: 11.533, file_cluster_0: 12.032, file_cluster_7: 12.113
- **Magnitude:** 616.34 | **LOC:** 523 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (10.5041%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `arrayOfStringsFunction` (Impact: 36.9 | O(2^N))
  * `bufferFunction` (Impact: 26.5 | O(2^N))
  * `stringFunction` (Impact: 26.5 | O(2^N))
  * `stringFunctionOptional` (Impact: 26.5 | O(2^N))
  * `typedarrayFunction` (Impact: 26.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 97`, `args: 70`, `func_start: 87`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 36`, `duplicate_logic: 7`, `orphaned_logic: 2`
* *Architecture:* `api: 44`, `concurrency: 2`
* *Defense:* `safety: 52`, `immutability_locks: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/compiler/bindings/raw.release.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.533 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.749 IQR)
- **Top Global Matches:** file_cluster_8: 11.533, file_cluster_0: 12.032, file_cluster_7: 12.113
- **Magnitude:** 616.34 | **LOC:** 523 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (10.5041%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `arrayOfStringsFunction` (Impact: 36.9 | O(2^N))
  * `bufferFunction` (Impact: 26.5 | O(2^N))
  * `stringFunction` (Impact: 26.5 | O(2^N))
  * `stringFunctionOptional` (Impact: 26.5 | O(2^N))
  * `typedarrayFunction` (Impact: 26.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 97`, `args: 70`, `func_start: 87`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 36`, `duplicate_logic: 7`, `orphaned_logic: 2`
* *Architecture:* `api: 44`, `concurrency: 2`
* *Defense:* `safety: 52`, `immutability_locks: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/compiler.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.729 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.902 IQR)
- **Top Global Matches:** file_cluster_8: 11.729, file_cluster_13: 11.741, file_cluster_4: 11.742
- **Magnitude:** 593.9 | **LOC:** 657 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (38.3939%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `runTest` (Impact: 265.4 | O(N^3) | DB: 43)
    * *Intent:* // Runs a single test
  * `testInstantiate` (Impact: 86.2 | O(N^3) | DB: 8)
  * `evaluateResult` (Impact: 25.3 | O(N^1) | DB: 2)
  * `section` (Impact: 21.5 | O(N^2))
    * *Intent:* // Starts a new section within a test
  * `getTests` (Impact: 7.6 | O(N^1) | DB: 1)
    * *Intent:* // Gets a list of all relevant tests
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 109`, `args: 35`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 120`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 14`, `api: 13`, `concurrency: 39`, `import: 17`
* *Defense:* `safety: 9`, `test: 1`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` index.js, cluster, options.js, features.json, os, v8, fs, cpu.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.364 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.196 IQR)
- **Top Global Matches:** file_cluster_8: 13.364, file_cluster_13: 13.679, file_cluster_11: 13.706
- **Magnitude:** 593.16 | **LOC:** 4588 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 67
- **Risk Profile:** Cognitive Load (69.5681%), Tech Debt (10.5666%)
**Top Internal Functions/Classes:**
  * `parseExpression` (Impact: 764.3 | O(2^N) | DB: 34)
  * `parseExpressionStart` (Impact: 749.3 | O(N^5) | DB: 67)
  * `parseTopLevelStatement` (Impact: 314.3 | O(N^4) | DB: 48)
  * `parseForStatement` (Impact: 202.3 | O(N^4) | DB: 30)
  * `skipBlock` (Impact: 155.0 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 804`, `structural_boundaries: 302`, `args: 56`, `func_start: 55`, `class_start: 2`
* *Risk/State:* `state_mutation: 1738`, `dead_code: 8`, `planned_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 17`, `api: 6`, `import: 5`
* *Defense:* `safety: 5`, `doc: 22`, `test: 12`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` diagnostics, util, : Identifier (, common, StringLiteral)?, StringLiteral, file, ast...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/passes/pass.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.79 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.782 IQR)
- **Top Global Matches:** file_cluster_8: 14.79, file_cluster_13: 15.097, file_cluster_11: 15.125
- **Magnitude:** 428.77 | **LOC:** 2121 | **CtrlFlow:** 78.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 488
- **Risk Profile:** Cognitive Load (84.7206%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `visit` (Impact: 1242.6 | O(2^N) | DB: 488)
  * `replaceChild` (Impact: 838.0 | O(N^2) | DB: 129)
  * `replaceCurrent` (Impact: 7.6 | O(N^1) | DB: 8)
  * `currentExpression` (Impact: 7.2 | O(2^N) | DB: 2)
    * *Intent:* /** Expression stack. */
  * `currentFunction` (Impact: 7.2 | O(2^N) | DB: 2)
    * *Intent:* /** Base class of custom Binaryen passes. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 450`, `structural_boundaries: 125`, `args: 272`, `func_start: 272`, `class_start: 2`
* *Risk/State:* `state_mutation: 1948`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 91`, `doc: 20`, `test: 66`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004618
  * `Imports (Out-Degree: 1):` module, binaryen
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/program.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.405 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.224 IQR)
- **Top Global Matches:** file_cluster_13: 14.405, file_cluster_11: 14.564, file_cluster_8: 14.63
- **Magnitude:** 385.17 | **LOC:** 5125 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 224
- **Risk Profile:** Cognitive Load (47.6971%), Tech Debt (21.1002%)
**Top Internal Functions/Classes:**
  * `doProcessOverride` (Impact: 1312.4 | O(N^4) | DB: 224)
    * *Intent:* // TODO: for (let [exportName, queuedExport] of exports) {
  * `makeNativeFunctionDeclaration` (Impact: 412.3 | O(N^4) | DB: 138)
  * `fromDecorator` (Impact: 289.7 | O(N^3))
  * `fromBinaryToken` (Impact: 69.8 | O(N^1))
  * `fromUnaryPrefixToken` (Impact: 16.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 482`, `structural_boundaries: 260`, `args: 144`, `func_start: 141`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1439`, `dead_code: 5`, `planned_debt: 7`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 83`, `import: 29`
* *Defense:* `safety: 16`, `doc: 236`, `test: 35`, `immutability_locks: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 68.197
  * `Choke Point (Betweenness):` 0.00035 | `Ripple Effect (Closeness):` 0.036439
  * `Imports (Out-Degree: 3):` diagnostics, util, builtins, baz, flow, types, bar, compiler...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/bindings/js.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.857 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.001 IQR)
- **Top Global Matches:** file_cluster_11: 14.857, file_cluster_4: 14.897, file_cluster_8: 14.922
- **Magnitude:** 353.55 | **LOC:** 1607 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 291
- **Risk Profile:** Cognitive Load (89.3313%), Tech Debt (15.2738%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 463.8 | O(N^3) | DB: 291)
    * *Intent:* // not implemented // let sb = this.sb; // sb.push("export const "); // sb.push(name); // sb.push(" ...
  * `makeLowerToValue` (Impact: 225.4 | O(N^3) | DB: 75)
  * `makeLiftFromValue` (Impact: 87.7 | O(N^2) | DB: 53)
  * `visitFunction` (Impact: 77.1 | O(N^3) | DB: 63)
  * `makeFunctionImport` (Impact: 58.1 | O(N^2) | DB: 64)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 397`, `structural_boundaries: 201`, `args: 143`, `func_start: 135`, `class_start: 2`
* *Risk/State:* `state_mutation: 2098`, `dead_code: 3`, `planned_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 37`, `concurrency: 44`, `import: 8`
* *Defense:* `safety: 24`, `doc: 11`, `test: 13`, `immutability_locks: 26`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.705
  * `Choke Point (Betweenness):` 0.000672 | `Ripple Effect (Closeness):` 0.043464
  * `Imports (Out-Degree: 2):` promises, util, util, compiler, program, types, common, ast
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `src/tokenizer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.354 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 2.983 IQR)
- **Top Global Matches:** file_cluster_8: 13.354, file_cluster_13: 13.668, file_cluster_11: 13.7
- **Magnitude:** 350.11 | **LOC:** 1798 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 96
- **Risk Profile:** Cognitive Load (89.3158%), Tech Debt (11.8856%)
**Top Internal Functions/Classes:**
  * `unsafeNext` (Impact: 817.3 | O(N^5) | DB: 96)
  * `tokenFromKeyword` (Impact: 440.5 | O(N^2) | DB: 3)
    * *Intent:* // meta
  * `operatorTokenToString` (Impact: 108.8 | O(N^1))
  * `readEscapeSequence` (Impact: 100.2 | O(N^2) | DB: 24)
  * `readDecimalFloatPartial` (Impact: 70.7 | O(N^3) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 600`, `structural_boundaries: 270`, `args: 56`, `func_start: 55`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1267`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 30`, `concurrency: 7`, `import: 3`
* *Defense:* `safety: 11`, `doc: 11`, `test: 5`, `immutability_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ) return Token.Import;
          break;
        
        case CharCode.t: 
          if (text ==, util, diagnostics, ast
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extra/ast.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.385 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.617 IQR)
- **Top Global Matches:** file_cluster_8: 15.385, file_cluster_11: 15.461, file_cluster_17: 15.461
- **Magnitude:** 343.27 | **LOC:** 1631 | **CtrlFlow:** 87.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 56
- **Risk Profile:** Cognitive Load (73.4869%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `visitNode` (Impact: 326.9 | O(N^2) | DB: 56)
  * `visitFunctionCommon` (Impact: 80.1 | O(N^3) | DB: 39)
  * `visitClassDeclaration` (Impact: 63.3 | O(N^2) | DB: 41)
  * `visitLiteralExpression` (Impact: 48.6 | O(N^2) | DB: 7)
  * `visitExportDefaultStatement` (Impact: 35.1 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 414`, `structural_boundaries: 57`, `args: 114`, `func_start: 112`, `class_start: 1`
* *Risk/State:* `state_mutation: 2117`
* *Architecture:* `io: 5`, `api: 14`, `import: 4`
* *Defense:* `safety: 77`, `doc: 3`, `test: 17`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` );
    let declarations = node.declarations;
    let namespaceName = node.namespaceName;
    if (declarations) 
      let numDeclarations = declarations.length;
      if (numDeclarations) 
        sb.push(, );
    this.visitIdentifierExpression(node.externalName);
    sb.push(, util, tokenizer, );
     else if (node.is(CommonFlags.Declare)) 
      sb.push(, common, ast
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/build-dts.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.373 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.723 IQR)
- **Top Global Matches:** file_cluster_13: 11.373, file_cluster_8: 11.463, file_cluster_11: 11.507
- **Magnitude:** 306.66 | **LOC:** 394 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (25.9246%), Tech Debt (72.0155%)
**Top Internal Functions/Classes:**
  * `generate` (Impact: 143.0 | O(N^3) | DB: 30)
  * `transformTypes` (Impact: 63.7 | O(N^3) | DB: 2)
    * *Intent:* // prefix the import with options.prefix, so that both non-relative imports
  * `generateCli` (Impact: 12.0 | O(N^2) | DB: 3)
  * `processTree` (Impact: 9.0 | O(N^2) | DB: 2)
  * `generate` (Impact: 8.4 | O(N^2))
    * *Intent:* // © 2015-2019 SitePen, Inc. New BSD License. // see: https://github.com/SitePen/dts-generator
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 42`, `args: 22`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 42`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 12`, `api: 4`, `import: 6`
* *Defense:* `safety: 9`, `doc: 5`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fs, path, util, glob, url, typescript
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/module.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.581 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.281 IQR)
- **Top Global Matches:** file_cluster_8: 13.581, file_cluster_7: 13.62, file_cluster_13: 13.678
- **Magnitude:** 283.57 | **LOC:** 4010 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 111
- **Risk Profile:** Cognitive Load (45.7012%), Tech Debt (35.7758%)
**Top Internal Functions/Classes:**
  * `prepareType` (Impact: 410.8 | O(2^N) | DB: 39)
  * `binary` (Impact: 238.9 | O(N^2) | DB: 3)
  * `readStringCached` (Impact: 125.6 | O(N^4) | DB: 13)
  * `maybeDropCondition` (Impact: 120.7 | O(N^2) | DB: 111)
  * `tryEnsureBasicType` (Impact: 58.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 357`, `structural_boundaries: 561`, `args: 173`, `func_start: 172`, `class_start: 5`
* *Risk/State:* `state_mutation: 907`, `dead_code: 5`, `planned_debt: 7`, `fragile_debt: 4`, `duplicate_logic: 7`
* *Architecture:* `api: 264`, `import: 6`
* *Defense:* `safety: 10`, `doc: 504`, `test: 20`, `immutability_locks: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` util, builtins, types, program, common, binaryen
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `std/portable/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.171 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.729 IQR)
- **Top Global Matches:** file_cluster_8: 12.171, file_cluster_12: 12.627, file_cluster_17: 12.643
- **Magnitude:** 281.86 | **LOC:** 417 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (88.3516%), Tech Debt (99.9944%)
**Top Internal Functions/Classes:**
  * `defaultComparator` (Impact: 14.5 | O(N^1) | DB: 1)
  * `AssertionError` (Impact: 14.3 | O(2^N) | DB: 4)
  * `UnreachableError` (Impact: 10.7 | O(2^N) | DB: 3)
  * `findLastIndex` (Impact: 10.7 | O(N^3) | DB: 2)
  * `isArrayLike` (Impact: 9.0 | O(N^1))
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

### `std/assembly/math.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.866 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.132 IQR)
- **Top Global Matches:** file_cluster_8: 12.866, file_cluster_0: 12.924, file_cluster_11: 13.218
- **Magnitude:** 233.63 | **LOC:** 3290 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (67.702%), Tech Debt (83.4292%)
**Top Internal Functions/Classes:**
  * `atan2` (Impact: 80.1 | O(N^2) | DB: 6)
  * `sincos` (Impact: 79.9 | O(N^3) | DB: 8)
  * `rem` (Impact: 76.1 | O(N^2) | DB: 12)
  * `rem` (Impact: 76.0 | O(N^2) | DB: 11)
  * `atan` (Impact: 72.2 | O(N^2) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 441`, `structural_boundaries: 300`, `args: 79`, `func_start: 73`
* *Risk/State:* `state_mutation: 821`, `dead_code: 5`, `planned_debt: 4`, `duplicate_logic: 10`, `orphaned_logic: 23`
* *Architecture:* `api: 72`, `import: 3`
* *Defense:* `safety: 3`, `doc: 12`, `immutability_locks: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math, builtins, dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `std/assembly/builtins.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.26 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.571 IQR)
- **Top Global Matches:** file_cluster_0: 10.26, file_cluster_8: 10.893, file_cluster_16: 11.08
- **Magnitude:** 179.58 | **LOC:** 2632 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (10.8822%), Tech Debt (8.3936%)
**Top Internal Functions/Classes:**
  * `v128` (Impact: 472.5 | O(2^N))
    * *Intent:* // @ts-ignore: decorator
  * `i64` (Impact: 246.1 | O(2^N) | DB: 2)
    * *Intent:* // @ts-ignore: decorator
  * `i32` (Impact: 187.5 | O(2^N) | DB: 2)
    * *Intent:* // @ts-ignore: decorator
  * `f32` (Impact: 25.9 | O(2^N))
    * *Intent:* // @ts-ignore: decorator
  * `f64` (Impact: 25.9 | O(2^N))
    * *Intent:* // @ts-ignore: decorator
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 1254`, `args: 575`, `func_start: 574`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`, `fragile_debt: 1`
* *Architecture:* `api: 645`, `import: 1`
* *Defense:* `safety: 27`, `doc: 2`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` string
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/asinit.js` (JAVASCRIPT | Tier 0 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.638 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.125 IQR)
- **Top Global Matches:** file_cluster_8: 9.638, file_cluster_13: 10.088, file_cluster_7: 10.362
- **Magnitude:** 175.78 | **LOC:** 469 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (12.5176%), Tech Debt (39.5018%)
**Top Internal Functions/Classes:**
  * `ensurePackageJson` (Impact: 42.7 | O(N^2) | DB: 25)
  * `formatPath` (Impact: 14.5 | O(2^N) | DB: 11)
  * `createProject` (Impact: 11.7 | O(N^1) | DB: 3)
  * `createProject` (Impact: 10.9 | O(2^N))
  * `ensureAsconfigJson` (Impact: 9.4 | O(N^2) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 30`, `args: 18`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 21`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 50`, `api: 1`, `import: 12`
* *Defense:* `safety: 5`, `doc: 1`, `test: 4`, `immutability_locks: 28`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` readline, package.json, options.js, fs, path, terminal.js, module, url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/flow.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.508 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.728 IQR)
- **Top Global Matches:** file_cluster_8: 13.508, file_cluster_13: 13.534, file_cluster_11: 13.754
- **Magnitude:** 171.18 | **LOC:** 1480 | **CtrlFlow:** 79.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (45.201%), Tech Debt (8.9468%)
**Top Internal Functions/Classes:**
  * `inheritNonnullIfTrue` (Impact: 365.9 | O(2^N) | DB: 30)
  * `canOverflow` (Impact: 327.6 | O(2^N) | DB: 23)
  * `inheritNonnullIfFalse` (Impact: 295.4 | O(2^N) | DB: 24)
  * `inheritAlternatives` (Impact: 150.0 | O(N^2) | DB: 28)
    * *Intent:* /** This flow always throws. */
  * `resetIfNeedsRecompile` (Impact: 27.9 | O(N^2) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 54`, `args: 35`, `func_start: 35`
* *Risk/State:* `state_mutation: 472`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `safety: 3`, `doc: 25`, `test: 20`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.854
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025227
  * `Imports (Out-Degree: 2):` diagnostics, util, builtins, types, common, compiler, program, module...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/glue/js/i64.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.691 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.271 IQR)
- **Top Global Matches:** file_cluster_8: 10.691, file_cluster_7: 11.294, file_cluster_13: 11.328
- **Magnitude:** 169.64 | **LOC:** 235 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (26.6381%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `i64_pow` (Impact: 29.8 | O(N^2) | DB: 3)
  * `i64_is_i8` (Impact: 10.6 | O(N^1))
  * `i64_is_i16` (Impact: 10.6 | O(N^1))
  * `i64_is_i32` (Impact: 7.1 | O(N^1))
  * `i64_align` (Impact: 3.7 | O(N^1) | DB: 2)
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

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/glue/wasm/float.ts` (TYPESCRIPT) | Magnitude: 1.27 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: decorators: 8, structural_boundaries: 4, args: 4, func_start: 4
- `std/assembly/typedarray.ts` (TYPESCRIPT) | Magnitude: 116.58 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 1450, state_mutation: 568, structural_boundaries: 516, func_start: 487
- `tests/compiler/rt/finalize.ts` (TYPESCRIPT) | Magnitude: 0.44 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 4, func_start: 4, structural_boundaries: 3, state_mutation: 2
- `std/assembly/function.ts` (TYPESCRIPT) | Magnitude: 1.08 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 8, args: 5, func_start: 5
- `tests/parser/function.ts` (TYPESCRIPT) | Magnitude: 0.95 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 5, func_start: 5, orphaned_logic: 5, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `eslint.config.js` (JAVASCRIPT) | Magnitude: 9.16 | Delta: **0.295 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 177, doc: 51, events: 45, decorators: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/passes/shadowstack.ts` (TYPESCRIPT) | Magnitude: 84.6 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 588, indent_spaces: 407, structural_boundaries: 103, branch: 58
- `src/bindings/js.ts` (TYPESCRIPT) | Magnitude: 353.55 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 2098, indent_spaces: 1371, branch: 397, structural_boundaries: 201
- `src/bindings/util.ts` (TYPESCRIPT) | Magnitude: 46.68 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 169, state_mutation: 155, branch: 65, args: 18
- `src/compiler.ts` (TYPESCRIPT) | Magnitude: 858.69 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 3603, state_mutation: 3050, branch: 924, structural_boundaries: 653
- `std/assembly/util/bytes.ts` (TYPESCRIPT) | Magnitude: 15.01 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 85, state_mutation: 30, branch: 24, generics: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/resolver.ts` (TYPESCRIPT) | Magnitude: 120.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 798, state_mutation: 446, branch: 192, structural_boundaries: 151
- `std/assembly/rt/rtrace.ts` (TYPESCRIPT) | Magnitude: 4.58 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 19, args: 9, func_start: 9, api: 9
- `tests/allocators/index.js` (JAVASCRIPT) | Magnitude: 50.08 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 15, state_mutation: 13, branch: 10
- `util/browser/url.js` (JAVASCRIPT) | Magnitude: 13.32 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 5, regex_execution: 5, io: 4
- `src/util/path.ts` (TYPESCRIPT) | Magnitude: 17.63 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 84, branch: 33, io: 28, state_mutation: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `std/assembly/set.ts` (TYPESCRIPT) | Magnitude: 30.14 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 179, indent_spaces: 145, generics: 34, branch: 23
- `tests/compiler/std/pointer.ts` (TYPESCRIPT) | Magnitude: 1.19 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 49, generics: 36, func_start: 29, args: 27
- `tests/compiler/function-types.ts` (TYPESCRIPT) | Magnitude: 1.29 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 16, func_start: 13, structural_boundaries: 12, generics: 9
- `src/util/collections.ts` (TYPESCRIPT) | Magnitude: 18.99 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 122, indent_spaces: 85, structural_boundaries: 16, branch: 15
- `tests/compiler/instanceof.ts` (TYPESCRIPT) | Magnitude: 8.16 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: func_start: 232, generics: 151, args: 100, test: 91

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/compiler/merge.ts` (TYPESCRIPT) | Magnitude: 4.66 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 36, args: 18, func_start: 18, safety: 16
- `tests/allocators/runner.js` (JAVASCRIPT) | Magnitude: 137.32 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 73, state_mutation: 51, branch: 27, structural_boundaries: 16
- `util/cpu.js` (JAVASCRIPT) | Magnitude: 10.5 | Delta: **0.228 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 10, immutability_locks: 9, branch: 7
- `util/find.js` (JAVASCRIPT) | Magnitude: 32.56 | Delta: **0.251 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 9, indent_spaces: 9, structural_boundaries: 7, branch: 6
- `util/options.js` (JAVASCRIPT) | Magnitude: 682.4 | Delta: **0.305 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 203, branch: 148, state_mutation: 105, structural_boundaries: 66

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `std/assembly/string.ts` (TYPESCRIPT) | Magnitude: 99.75 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 553, state_mutation: 456, branch: 144, structural_boundaries: 121
- `tests/compiler/NonNullable.ts` (TYPESCRIPT) | Magnitude: 0.97 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: func_start: 10, args: 9, generics: 7, test: 5
- `tests/compiler/std/typedarray.ts` (TYPESCRIPT) | Magnitude: 37.27 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 507, func_start: 406, generics: 362, ui_framework: 220
- `scripts/hexfloat.html` (HTML) | Magnitude: 30.76 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 29, args: 12, structural_boundaries: 11, state_mutation: 9
- `util/web.d.ts` (TYPESCRIPT) | Magnitude: 0.73 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: args: 4, func_start: 4, concurrency: 4, doc: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `scripts/build-web.js` (JAVASCRIPT) | Magnitude: 32.96 | Delta: **0.185 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, state_mutation: 12, io: 10, structural_boundaries: 9
- `bin/asc.js` (JAVASCRIPT) | Magnitude: 16.12 | Delta: **0.253 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, branch: 10, concurrency: 8, immutability_locks: 8
- `cli/index.js` (JAVASCRIPT) | Magnitude: 2000.8 | Delta: **0.287 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 1000, state_mutation: 430, branch: 321, structural_boundaries: 264
- `util/node.js` (JAVASCRIPT) | Magnitude: 56.52 | Delta: **0.391 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 25, concurrency: 24, state_mutation: 15, indent_spaces: 15
- `tests/transform/index.js` (JAVASCRIPT) | Magnitude: 136.16 | Delta: **0.491 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, func_start: 27, branch: 25, state_mutation: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `tests/compiler/call-inferred.ts` (TYPESCRIPT) | Magnitude: 1.17 | Delta: **0.123 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: func_start: 13, args: 11, generics: 9, indent_spaces: 9
- `std/assembly/object.ts` (TYPESCRIPT) | Magnitude: 1.71 | Delta: **0.337 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 5, func_start: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `util/cpu.d.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, api: 2, immutability_locks: 2
- `src/util/vector.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.143 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, api: 2, memory_alloc: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `util/terminal.js` (JAVASCRIPT) | Magnitude: 90.14 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 42, structural_boundaries: 23, api: 20, branch: 13
- `tests/compiler.js` (JAVASCRIPT) | Magnitude: 593.9 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 499, branch: 138, state_mutation: 120, structural_boundaries: 109
- `std/assembly/date.ts` (TYPESCRIPT) | Magnitude: 43.71 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 268, state_mutation: 263, structural_boundaries: 38, branch: 36
- `tests/compiler/infer-generic.ts` (TYPESCRIPT) | Magnitude: 4.01 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 32, args: 24, func_start: 17, indent_spaces: 14
- `tests/compiler/bindings/esm.ts` (TYPESCRIPT) | Magnitude: 14.77 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 69, api: 46, state_mutation: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tests/compiler/resolve-ternary.ts` (TYPESCRIPT) | Magnitude: 0.76 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 15, args: 9, func_start: 9, branch: 5
- `tests/compiler/issues/2166.ts` (TYPESCRIPT) | Magnitude: 0.7 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 12, func_start: 9, generics: 9, args: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/compiler.ts` -> Churn: **100.0%** | Cog Load: 54.4948% | Debt: 27.2753%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `cli/index.js` -> **Max Graey** (100.0% isolated ownership) | Magnitude: 2000.8
- `src/builtins.ts` -> **Congcong Cai** (100.0% isolated ownership) | Magnitude: 974.73
- `src/module.ts` -> **Congcong Cai** (100.0% isolated ownership) | Magnitude: 283.57
- `std/portable/index.js` -> **Max Graey** (100.0% isolated ownership) | Magnitude: 281.86
- `util/text.js` -> **Max Graey** (100.0% isolated ownership) | Magnitude: 145.24

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

- `src/bindings/js.ts` -> **Severity: 4.345** (Embedded: 0.0435 * Error Risk: 99.978%)
- `src/program.ts` -> **Severity: 3.587** (Embedded: 0.0364 * Error Risk: 98.4305%)
- `src/types.ts` -> **Severity: 3.489** (Embedded: 0.0357 * Error Risk: 97.6878%)
- `src/flow.ts` -> **Severity: 2.497** (Embedded: 0.0252 * Error Risk: 98.9986%)
- `src/resolver.ts` -> **Severity: 2.375** (Embedded: 0.0251 * Error Risk: 94.7917%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/bindings/js.ts` -> **Severity: 2050.179** (Blast Radius: 48.705 * Doc Risk: 42.0938%)
- `src/program.ts` -> **Severity: 1016.163** (Blast Radius: 68.197 * Doc Risk: 14.9004%)
- `src/types.ts` -> **Severity: 725.243** (Blast Radius: 60.841 * Doc Risk: 11.9203%)
- `std/assembly/bindings/dom.ts` -> **Severity: 616.3** (Blast Radius: 6.163 * Doc Risk: 100.0%)
- `util/browser/url.js` -> **Severity: 424.26** (Blast Radius: 4.346 * Doc Risk: 97.6207%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
