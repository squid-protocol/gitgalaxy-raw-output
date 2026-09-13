# ARCHITECTURAL_BRIEF: assemblyscript
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/AssemblyScript/assemblyscript.git` |
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
| Total Artifacts | 1274 |
| Analyzed Artifacts (Scanned) | 710 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 564 |
| Total LOC | 90476 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 55.7% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7303 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0607 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 6.8427 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 40 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 451 | 79055 | 63.5% |
| JSON | 151 | 1900 | 21.3% |
| JAVASCRIPT | 66 | 9231 | 9.3% |
| PLAINTEXT | 23 | 1 | 3.2% |
| MARKDOWN | 14 | 0 | 2.0% |
| HTML | 3 | 287 | 0.4% |
| XML | 2 | 2 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 672 | 94.6% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 36 | 5.1% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 564*

**Composition by Extension & Reason:**
- `.wat`: 381x Excluded (Unsupported Extension: '.wat')
- `.json`: 112x Excluded: Neighborhood Micro-Mass Limit Exceeded, 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1356 LOC)
- `.ts`: 19x Excluded: Neighborhood Micro-Mass Limit Exceeded, 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 2940 commas in 803 LOC)
- `.yml`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 139 LOC)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 542 LOC), 1x Excluded (Machine-Generated Source Code Signature: 391 LOC)
- `.wasm`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.cjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 1x Excluded (Saturation: Line 1 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.4 | 8.0 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 22.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 10.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.4 | 1.4 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 55.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.0 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 43.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 619 | 52 | 0 | `src/compiler.ts` |
| cleanup | 3 | 3 | 0 | `bin/asinit.js` |
| guards | 1351 | 103 | 3 | `cli/index.js` |
| danger | 722 | 94 | 1 | `std/assembly/index.d.ts` |
| concurrency | 211 | 31 | 0 | `cli/index.js` |
| connectivity | 5101 | 270 | 10 | `std/assembly/builtins.ts` |
| io | 324 | 47 | 0 | `bin/asinit.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 10 | 4 | 0 | `tests/compiler.js` |
| time | 73 | 15 | 0 | `tests/compiler/std/date.ts` |
| serialization | 28 | 10 | 0 | `bin/asinit.js` |
| regex | 101 | 17 | 0 | `tests/compiler/std/string.ts` |
| events | 113 | 15 | 0 | `eslint.config.js` |
| tests | 7731 | 172 | 10 | `tests/compiler/std/math.ts` |
| docs | 4647 | 98 | 2 | `std/assembly/index.d.ts` |
| debt | 1087 | 114 | 2 | `std/assembly/index.d.ts` |
| mutation | 26744 | 357 | 52 | `src/builtins.ts` |
| dead_code | 1199 | 182 | 3 | `std/assembly/index.d.ts` |
| credential | 5 | 2 | 0 | `tests/compiler/std/string-casemapping.ts` |
| threat | 483 | 36 | 0 | `src/compiler.ts` |
| ml_ai | 68 | 11 | 0 | `std/assembly/bindings/dom.ts` |
| ui | 538 | 22 | 0 | `src/compiler.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `bin/asinit.js` (Hits: 44)
- `cli/index.js` (Hits: 30)
- `src/util/path.ts` (Hits: 30)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **error.ts** (`std/assembly/util/error.ts`) — 16 inbound connections
2. **fs.js** (`util/browser/fs.js`) — 15 inbound connections
3. **url.js** (`util/browser/url.js`) — 13 inbound connections
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

- `replaceChild` (@ `src/passes/pass.ts`) -> Impact: **425.9** | LOC: 799
  * *Intent:* /** Replaces an expression within a parent expression. Returns the replaced expression on success, otherwise `0`. */
- `main` (@ `cli/index.js`) -> Impact: **411.8** | LOC: 961
  * *Intent:* /** Runs the command line utility using the specified arguments array. */
- `compileBinaryExpression` (@ `src/compiler.ts`) -> Impact: **351.4** | LOC: 747
- `parseClassMember` (@ `src/parser.ts`) -> Impact: **296.4** | LOC: 559
- `unsafeNext` (@ `src/tokenizer.ts`) -> Impact: **275.1** | LOC: 445
- `convertExpression` (@ `src/compiler.ts`) -> Impact: **247.6** | LOC: 249
  * *Intent:* /** Converts an expression's result from one type to another. */
- `canOverflow` (@ `src/flow.ts`) -> Impact: **225.8** | LOC: 256
  * *Intent:* /** * Tests if an expression can possibly overflow in the context of this flow. Assumes that the * expression might already have overflown and returns...
- `compileUnaryPrefixExpression` (@ `src/compiler.ts`) -> Impact: **205.8** | LOC: 355
- `resolveBinaryExpression` (@ `src/resolver.ts`) -> Impact: **180.3** | LOC: 207
  * *Intent:* /** Resolves a binary expression to its static type. */
- `build` (@ `src/bindings/js.ts`) -> Impact: **179.3** | LOC: 507

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 21 | 31256.48 | 23.08% | 7.11% |
| `std/assembly` | 34 | 9370.31 | 19.7% | 56.76% |
| `tests/compiler` | 227 | 5063.3 | 2.56% | 0.0% |
| `__monolith__` | 7 | 5041.28 | 0.36% | 3.13% |
| `tests/compiler/bindings` | 20 | 2996.14 | 17.58% | 0.0% |
| `src/bindings` | 3 | 2961.36 | 60.68% | 21.67% |
| `tests/compiler/std` | 53 | 2354.12 | 4.13% | 0.0% |
| `std/assembly/util` | 8 | 2042.6 | 57.15% | 4.85% |
| `src/passes` | 4 | 1720.84 | 31.47% | 19.28% |
| `cli` | 5 | 1562.39 | 20.54% | 21.69% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lib/loader/index.d.ts` -> **100.0%** Exposure
- `lib/rtrace/index.d.ts` -> **100.0%** Exposure
- `src/glue/js/i64.d.ts` -> **100.0%** Exposure
- `std/assembly/builtins.ts` -> **100.0%** Exposure
- `std/assembly/console.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `bin/asc.js` -> **100.0%** Exposure
- `cli/index.js` -> **100.0%** Exposure
- `scripts/hexfloat.js` -> **100.0%** Exposure
- `scripts/unicode-identifier.js` -> **100.0%** Exposure
- `src/glue/js/i64.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `std/assembly/index.d.ts` -> **287** Orphaned Functions | **242** Duplicates
- `std/assembly/builtins.ts` -> **0** Orphaned Functions | **196** Duplicates
- `src/glue/js/i64.d.ts` -> **47** Orphaned Functions | **0** Duplicates
- `std/portable/index.d.ts` -> **37** Orphaned Functions | **6** Duplicates
- `lib/loader/index.d.ts` -> **42** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `122` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `cli/index.js` (JAVASCRIPT) -> Cumulative Risk: **720.03**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1521.4 | **LOC:** 1291 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (91.8857%)
- **Heaviest Functions:** `main` (Impact: 411.8), `prepareResult` (Impact: 57.1), `getFile` (Impact: 52.1)

### 2. `std/assembly/util/bytes.ts` (TYPESCRIPT) -> Cumulative Risk: **667.86**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 101.1 | **LOC:** 108 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (87.6926%)
- **Heaviest Functions:** `FILL` (Impact: 46.7), `REVERSE` (Impact: 16.6)

### 3. `bin/asc.js` (JAVASCRIPT) -> Cumulative Risk: **665.1**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 43.72 | **LOC:** 36 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `on` (Impact: 1.1)

### 4. `std/assembly/util/uri.ts` (TYPESCRIPT) -> Cumulative Risk: **643.06**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 246.46 | **LOC:** 276 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (93.6469%)
- **Heaviest Functions:** `encode` (Impact: 60.8), `decode` (Impact: 58.3), `loadHex` (Impact: 5.5)

### 5. `std/portable/index.js` (JAVASCRIPT) -> Cumulative Risk: **642.11**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 303.26 | **LOC:** 417 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (92.4669%)
- **Heaviest Functions:** `defaultComparator` (Impact: 14.5), `isArrayLike` (Impact: 7.4), `AssertionError` (Impact: 6.1)

### 6. `src/bindings/js.ts` (TYPESCRIPT) -> Cumulative Risk: **635.02**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2160.78 | **LOC:** 1607 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.6071%), Cognitive Load (87.8426%)
- **Heaviest Functions:** `build` (Impact: 179.3), `makeLowerToValue` (Impact: 115.5), `makeLiftFromValue` (Impact: 59.6)

### 7. `std/assembly/date.ts` (TYPESCRIPT) -> Cumulative Risk: **633.23**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 190.26 | **LOC:** 376 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9912%), Tech Debt (97.1122%)
- **Heaviest Functions:** `fromString` (Impact: 29.4), `toISOString` (Impact: 4.8), `daysSinceEpoch` (Impact: 4.4)

### 8. `std/assembly/staticarray.ts` (TYPESCRIPT) -> Cumulative Risk: **627.95**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 307.98 | **LOC:** 402 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9986%), Tech Debt (99.9518%), Documentation (88.4615%)
- **Heaviest Functions:** `slice` (Impact: 26.5), `concat` (Impact: 24.3), `includes` (Impact: 16.4)

### 9. `src/builtins.ts` (TYPESCRIPT) -> Cumulative Risk: **620.62**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 6975.3 | **LOC:** 11395 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), Spec Match (100.0%), State Flux (99.978%), Safety Score (84.4485%)
- **Heaviest Functions:** `builtin_assert` (Impact: 122.6), `builtin_v128_shuffle` (Impact: 46.5), `ensureVisitMembersOf` (Impact: 43.2)

### 10. `util/text.js` (JAVASCRIPT) -> Cumulative Risk: **614.59**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 200.04 | **LOC:** 115 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.5041%), Verification (80.0%)
- **Heaviest Functions:** `utf8Read` (Impact: 31.6), `utf8Write` (Impact: 21.2), `utf8Length` (Impact: 15.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/compiler.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 8223.54 | **LOC:** 10689 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (53.1953%), Tech Debt (11.7106%)
**Top Internal Functions/Classes:**
  * `compileBinaryExpression` (Impact: 351.4)
  * `convertExpression` (Impact: 247.6)
    * *Intent:* /** Converts an expression's result from one type to another. */
  * `compileUnaryPrefixExpression` (Impact: 205.8)
  * `makePow` (Impact: 145.9)
  * `compileIdentifierExpression` (Impact: 137.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 991 instances
* *State Mutation (weighted view):* 3147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2176`, `structural_boundaries: 2394`, `args: 156`, `func_start: 156`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 3`, `state_mutation: 1165`, `dead_code: 26`, `planned_debt: 78`, `fragile_debt: 3`
* *Architecture:* `io: 2`, `api: 21`, `import: 14`
* *Defense:* `doc: 236`, `test: 231`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` ast, js, builtins, common, diagnostics, flow, module, rtrace...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/builtins.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6975.3 | **LOC:** 11395 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (70.3623%), Tech Debt (8.1157%)
**Top Internal Functions/Classes:**
  * `builtin_assert` (Impact: 122.6)
    * *Intent:* // assert<T?>(isTrueish: T, message?: string) -> T{!= null}
  * `builtin_v128_shuffle` (Impact: 46.5)
    * *Intent:* // v128.shuffle<T!>(a: v128, b: v128, ...lanes: u8[]) -> v128
  * `ensureVisitMembersOf` (Impact: 43.2)
    * *Intent:* /** Ensures that the visitor function of the specified class is compiled. */
  * `builtin_v128_load_lane` (Impact: 39.5)
    * *Intent:* // v128.load_lane<TFrom!>(ptr: usize, vec: v128, idx: u8, immOffset?: usize, immAlign?: usize) -> v1...
  * `builtin_v128_store_lane` (Impact: 39.5)
    * *Intent:* // v128.store_lane<TFrom!>(ptr: usize, vec: v128, idx: u8, immOffset?: usize, immAlign?: usize) -> v...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 403 instances
* *State Mutation (weighted view):* 2677
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1497`, `structural_boundaries: 3768`, `args: 620`, `func_start: 616`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 1871`, `dead_code: 1`, `planned_debt: 11`, `fragile_debt: 1`
* *Architecture:* `api: 638`, `import: 10`
* *Defense:* `doc: 35`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ast, common, compiler, diagnostics, flow, module, program, resolver...
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `std/assembly/math.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3645.34 | **LOC:** 3290 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.7983%), Tech Debt (9.7973%)
**Top Internal Functions/Classes:**
  * `pow` (Impact: 137.3)
  * `atan2` (Impact: 54.2)
  * `atan2` (Impact: 54.1)
  * `rem` (Impact: 48.4)
  * `rem` (Impact: 48.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 575 instances
* *State Mutation (weighted view):* 2079
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 696`, `structural_boundaries: 494`, `args: 107`, `func_start: 107`
* *Risk/State:* `state_mutation: 929`, `dead_code: 7`, `planned_debt: 6`, `unreferenced_by_name: 2`
* *Architecture:* `api: 109`, `import: 3`
* *Defense:* `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` dom, builtins, math
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3329.18 | **LOC:** 4588 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.6951%), Tech Debt (8.0697%)
**Top Internal Functions/Classes:**
  * `parseClassMember` (Impact: 296.4)
  * `parseExpressionStart` (Impact: 158.1)
    * *Intent:* // expressions
  * `parseExpression` (Impact: 144.3)
  * `parseType` (Impact: 133.9)
    * *Intent:* /** Parses a type. */
  * `parseTopLevelStatement` (Impact: 131.9)
    * *Intent:* /** Parses a top-level statement. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 367 instances
* *State Mutation (weighted view):* 1120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1060`, `structural_boundaries: 505`, `args: 63`, `func_start: 63`, `class_start: 3`
* *Risk/State:* `state_mutation: 386`, `dead_code: 8`, `planned_debt: 5`
* *Architecture:* `io: 17`, `api: 9`, `import: 5`
* *Defense:* `safety: 2`, `doc: 28`, `test: 17`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ast, common, diagnostics, tokenizer, util, : Identifier (, StringLiteral, StringLiteral)?...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/program.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3115.98 | **LOC:** 5125 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (41.152%), Tech Debt (17.0196%)
**Top Internal Functions/Classes:**
  * `initialize` (Impact: 137.8)
    * *Intent:* /** Initializes the program and its elements prior to compilation. */
  * `fromDecorator` (Impact: 107.8)
    * *Intent:* /** Returns the operator kind represented by the specified decorator and string argument. */
  * `doProcessOverride` (Impact: 72.6)
    * *Intent:* /** Processes a single overridden member by this class in a base class. */
  * `writeField` (Impact: 61.6)
    * *Intent:* /** Writes a field value to a buffer and returns the number of bytes written. */
  * `tryMerge` (Impact: 60.3)
    * *Intent:* /** Attempts to merge two elements. Returns the merged element on success. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 307 instances
* *State Mutation (weighted view):* 997
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 860`, `structural_boundaries: 660`, `args: 226`, `func_start: 226`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 383`, `dead_code: 12`, `planned_debt: 27`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 123`, `import: 33`
* *Defense:* `doc: 524`, `test: 99`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.18
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.020617
  * `Imports (Out-Degree: 3):` ast, bar, baz, builtins, common, compiler, diagnostics, flow...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/resolver.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2640.32 | **LOC:** 3716 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (24.6333%), Tech Debt (8.5922%)
**Top Internal Functions/Classes:**
  * `resolveBinaryExpression` (Impact: 180.3)
    * *Intent:* /** Resolves a binary expression to its static type. */
  * `finishResolveClass` (Impact: 145.2)
    * *Intent:* /** Finishes resolving the specified class. */
  * `resolveFunction` (Impact: 131.2)
    * *Intent:* // ==================================================== Elements ===================================...
  * `lookupPropertyAccessExpression` (Impact: 130.7)
    * *Intent:* /** Looks up the program element the specified property access expression refers to. */
  * `resolveNamedType` (Impact: 114.2)
    * *Intent:* /** Resolves a {@link NamedTypeNode} to a concrete {@link Type}. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 187 instances
* *State Mutation (weighted view):* 571
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 767`, `structural_boundaries: 517`, `args: 58`, `func_start: 58`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 197`, `dead_code: 6`, `planned_debt: 8`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `doc: 275`, `test: 75`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.013446
  * `Imports (Out-Degree: 3):` ast, builtins, common, diagnostics, flow, program, tokenizer, types...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/bindings/js.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2160.78 | **LOC:** 1607 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.8426%), Tech Debt (9.0444%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 179.3)
  * `makeLowerToValue` (Impact: 115.5)
    * *Intent:* /** Lowers a JavaScript value to a WebAssembly value, as an expression. */
  * `makeLiftFromValue` (Impact: 59.6)
    * *Intent:* /** Lifts a WebAssembly value to a JavaScript value, as an expression. */
  * `makeFunctionImport` (Impact: 40.2)
  * `visitFunction` (Impact: 37.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 422 instances
* *Amplified Sql Injection:* 2 instances
* *Concurrency (weighted view):* 39
* *State Mutation (weighted view):* 1363
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 386`, `structural_boundaries: 227`, `args: 60`, `func_start: 53`, `class_start: 2`
* *Risk/State:* `state_mutation: 519`, `dead_code: 3`, `planned_debt: 5`
* *Architecture:* `io: 2`, `api: 36`, `concurrency: 9`, `import: 8`
* *Defense:* `safety: 6`, `doc: 13`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.188
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011314
  * `Imports (Out-Degree: 2):` ast, common, compiler, program, types, util, util, promises
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/module.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2141.9 | **LOC:** 4010 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.5295%), Tech Debt (10.5339%)
**Top Internal Functions/Classes:**
  * `optimize` (Impact: 124.9)
  * `binary` (Impact: 109.9)
  * `prepareType` (Impact: 76.3)
    * *Intent:* /** Recursively prepares the given GC type, potentially returning a temporary type. */
  * `tryEnsureBasicType` (Impact: 40.5)
    * *Intent:* /** Obtains the basic type of the given type, if any. */
  * `leastUpperBound` (Impact: 38.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 180 instances
* *State Mutation (weighted view):* 599
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 391`, `structural_boundaries: 733`, `args: 247`, `func_start: 249`, `class_start: 25`
* *Risk/State:* `state_mutation: 239`, `dead_code: 5`, `planned_debt: 9`, `fragile_debt: 4`
* *Architecture:* `api: 283`, `import: 6`
* *Defense:* `safety: 1`, `doc: 507`, `test: 25`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` builtins, common, binaryen, program, types, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `std/assembly/builtins.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2119.18 | **LOC:** 2632 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.2097%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `trace` (Impact: 20.2)
    * *Intent:* // @ts-ignore: decorator
  * `abort` (Impact: 11.5)
    * *Intent:* /* eslint-disable @typescript-eslint/no-unused-vars */ // @ts-ignore: decorator
  * `load_lane` (Impact: 7.4)
    * *Intent:* // @ts-ignore: decorator
  * `store_lane` (Impact: 7.4)
    * *Intent:* // @ts-ignore: decorator
  * `load8_lane` (Impact: 7.4)
    * *Intent:* // @ts-ignore: decorator
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 1281`, `args: 574`, `func_start: 574`, `class_start: 2`
* *Risk/State:* `state_mutation: 1`, `fragile_debt: 1`, `duplicate_logic: 196`
* *Architecture:* `api: 644`, `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` string
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tokenizer.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1579.42 | **LOC:** 1798 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.4237%), Tech Debt (7.9085%)
**Top Internal Functions/Classes:**
  * `unsafeNext` (Impact: 275.1)
  * `tokenFromKeyword` (Impact: 158.4)
  * `operatorTokenToString` (Impact: 77.8)
  * `readEscapeSequence` (Impact: 43.9)
  * `tokenIsAlsoIdentifier` (Impact: 30.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 200 instances
* *State Mutation (weighted view):* 625
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 535`, `structural_boundaries: 340`, `args: 37`, `func_start: 36`, `class_start: 5`
* *Risk/State:* `state_mutation: 225`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 27`, `concurrency: 2`, `import: 3`
* *Defense:* `safety: 3`, `doc: 11`, `test: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ) return Token.Import;
          break;
        
        case CharCode.t: 
          if (text ==, ast, diagnostics, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cli/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1521.4 | **LOC:** 1291 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (84.6506%), Tech Debt (8.4637%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 411.8)
    * *Intent:* /** Runs the command line utility using the specified arguments array. */
  * `prepareResult` (Impact: 57.1)
    * *Intent:* // Prepares the result object
  * `getFile` (Impact: 52.1)
    * *Intent:* // Gets the file matching the specified source path, imported at the given dependee path
  * `checkDiagnostics` (Impact: 43.7)
    * *Intent:* /** Checks diagnostics emitted so far for errors. */
  * `getConfig` (Impact: 26.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 36 instances
* *Amplified Cascading Flux:* 170 instances
* *Concurrency (weighted view):* 222
* *State Mutation (weighted view):* 542
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 279`, `args: 52`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 1`, `state_mutation: 202`, `dead_code: 7`, `planned_debt: 1`
* *Architecture:* `io: 30`, `api: 18`, `concurrency: 42`, `import: 12`
* *Defense:* `safety: 102`, `doc: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` binaryen.js, node.js, options.js, terminal.js, text.js, index.generated.js, index.js, assemblyscript
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/extra/ast.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1500.08 | **LOC:** 1631 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.1703%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `visitNode` (Impact: 104.4)
  * `visitClassDeclaration` (Impact: 43.3)
  * `visitFunctionCommon` (Impact: 35.0)
  * `visitInterfaceDeclaration` (Impact: 21.1)
  * `visitNamespaceDeclaration` (Impact: 17.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 253 instances
* *State Mutation (weighted view):* 792
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 212`, `args: 77`, `func_start: 75`, `class_start: 1`
* *Risk/State:* `state_mutation: 286`
* *Architecture:* `io: 5`, `api: 13`, `import: 4`
* *Defense:* `safety: 3`, `doc: 3`, `test: 17`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00187
  * `Imports (Out-Degree: 0):` );
     else if (node.is(CommonFlags.Declare)) 
      sb.push(, );
    let declarations = node.declarations;
    let namespaceName = node.namespaceName;
    if (declarations) 
      let numDeclarations = declarations.length;
      if (numDeclarations) 
        sb.push(, );
    this.visitIdentifierExpression(node.externalName);
    sb.push(, ast, common, tokenizer, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/passes/pass.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1278.54 | **LOC:** 2121 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.9778%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `replaceChild` (Impact: 425.9)
    * *Intent:* /** Replaces an expression within a parent expression. Returns the replaced expression on success, o...
  * `visit` (Impact: 174.4)
    * *Intent:* // Delegate /** Visits any expression, delegating to the respective visitor methods. */
  * `replaceCurrent` (Impact: 6.3)
    * *Intent:* // Utility /** Replaces the current expression with the specified replacement. */
  * `walkFunction` (Impact: 3.2)
    * *Intent:* /** Walks a specific function. */
  * `walkGlobal` (Impact: 3.1)
    * *Intent:* /** Walks a specific global variable. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 155 instances
* *State Mutation (weighted view):* 465
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 304`, `structural_boundaries: 362`, `args: 97`, `func_start: 97`, `class_start: 2`
* *Risk/State:* `state_mutation: 155`
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* `doc: 20`, `test: 66`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.557
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004488
  * `Imports (Out-Degree: 1):` binaryen, module
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/flow.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1252.04 | **LOC:** 1480 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.6373%), Tech Debt (8.727%)
**Top Internal Functions/Classes:**
  * `canOverflow` (Impact: 225.8)
    * *Intent:* /** * Tests if an expression can possibly overflow in the context of this flow. Assumes that the * e...
  * `inheritAlternatives` (Impact: 102.4)
    * *Intent:* /** Inherits two alternate branches to become this flow, i.e. then with else. */
  * `inheritNonnullIfTrue` (Impact: 78.3)
    * *Intent:* /** Updates local states to reflect that this branch is only taken when `expr` is true-ish. */
  * `inheritNonnullIfFalse` (Impact: 65.1)
    * *Intent:* /** Updates local states to reflect that this branch is only taken when `expr` is false-ish. */
  * `mergeSideEffects` (Impact: 41.8)
    * *Intent:* /** Merges only the side effects of a branch, i.e. when not taken. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 135 instances
* *State Mutation (weighted view):* 420
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 390`, `structural_boundaries: 203`, `args: 49`, `func_start: 49`, `class_start: 5`
* *Risk/State:* `state_mutation: 150`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `api: 36`, `import: 9`
* *Defense:* `doc: 104`, `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.013745
  * `Imports (Out-Degree: 2):` ast, builtins, common, compiler, diagnostics, module, program, types...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/ast.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1030.82 | **LOC:** 2420 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.8081%), Tech Debt (32.5742%)
**Top Internal Functions/Classes:**
  * `fromNode` (Impact: 53.0)
    * *Intent:* /** Returns the kind of the specified decorator name node. Defaults to {@link DecoratorKind.CUSTOM}....
  * `hasGenericComponent` (Impact: 27.0)
    * *Intent:* /** Tests if this type has a generic component matching one of the given type parameters. */
  * `lineAt` (Impact: 15.5)
    * *Intent:* /** Determines the line number at the specified position. Starts at `1`. */
  * `constructor` (Impact: 14.6)
    * *Intent:* /** Represents an `export` statement. */
  * `compilesToConst` (Impact: 10.8)
    * *Intent:* /** Tests whether this node is guaranteed to compile to a constant value. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 442`, `args: 187`, `func_start: 187`, `class_start: 89`
* *Risk/State:* `state_mutation: 37`, `planned_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 21`, `api: 319`, `import: 6`
* *Defense:* `doc: 413`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` common, diagnostics, module, tokenizer, types, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `std/assembly/typedarray.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 922.44 | **LOC:** 1946 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.4764%), Tech Debt (95.9777%)
**Top Internal Functions/Classes:**
  * `SET` (Impact: 49.0)
    * *Intent:* // @ts-ignore: decorator
  * `INCLUDES` (Impact: 19.1)
    * *Intent:* // @ts-ignore: decorator
  * `WRAP` (Impact: 17.6)
    * *Intent:* // @ts-ignore: decorator
  * `LAST_INDEX_OF` (Impact: 14.8)
    * *Intent:* // @ts-ignore: decorator
  * `INDEX_OF` (Impact: 12.8)
    * *Intent:* // @ts-ignore: decorator
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 575`, `args: 336`, `func_start: 341`, `class_start: 11`
* *Risk/State:* `state_mutation: 41`, `dead_code: 2`, `duplicate_logic: 35`
* *Architecture:* `api: 11`, `import: 6`
* *Defense:* `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` arraybuffer, builtins, bytes, error, sort, string
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `std/assembly/util/number.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 714.12 | **LOC:** 874 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.9222%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `genDigits` (Impact: 56.6)
  * `itoa_buffered` (Impact: 36.8)
  * `prettify` (Impact: 32.8)
  * `itoa64` (Impact: 22.4)
  * `utoa64` (Impact: 18.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 97 instances
* *State Mutation (weighted view):* 303
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 92`, `args: 33`, `func_start: 33`
* *Risk/State:* `state_mutation: 109`, `dead_code: 1`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002805
  * `Imports (Out-Degree: 0):` builtins, string
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `std/assembly/string.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 655.36 | **LOC:** 848 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.2909%), Tech Debt (8.8618%)
**Top Internal Functions/Classes:**
  * `encodeUnsafe` (Impact: 37.0)
    * *Intent:* // @ts-ignore: decorator
  * `split` (Impact: 30.4)
  * `replaceAll` (Impact: 30.2)
  * `decodeUnsafe` (Impact: 30.1)
    * *Intent:* // @ts-ignore: decorator
  * `toLowerCase` (Impact: 21.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 240
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 151`, `args: 45`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `state_mutation: 84`, `planned_debt: 2`
* *Architecture:* `api: 46`, `import: 6`
* *Defense:* `test: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` array, builtins, common, casemap, error, string
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bindings/tsd.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 641.0 | **LOC:** 416 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.2037%), Tech Debt (9.0905%)
**Top Internal Functions/Classes:**
  * `toTypeScriptType` (Impact: 87.6)
  * `build` (Impact: 21.1)
  * `visitFunction` (Impact: 16.2)
  * `makeRecordType` (Impact: 13.6)
  * `isPlainObject` (Impact: 12.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 135 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 418
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 99`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `state_mutation: 148`, `planned_debt: 1`
* *Architecture:* `api: 20`, `concurrency: 1`, `import: 6`
* *Defense:* `doc: 14`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.972
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002805
  * `Imports (Out-Degree: 2):` ast, common, program, types, util, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `util/browser/path.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 615.08 | **LOC:** 521 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.1975%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `normalizeStringPosix` (Impact: 60.4)
    * *Intent:* // Resolves . and .. elements in a path with directory names
  * `relative` (Impact: 58.2)
  * `basename` (Impact: 50.3)
  * `parse` (Impact: 47.6)
  * `extname` (Impact: 26.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 93 instances
* *State Mutation (weighted view):* 279
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 124`, `args: 13`, `func_start: 13`
* *Risk/State:* `state_mutation: 93`
* *Architecture:* `api: 13`, `import: 2`
* *Defense:* `safety: 98`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.221
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.014025
  * `Imports (Out-Degree: 1):` process.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/compiler/bindings/esm.debug.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 603.32 | **LOC:** 562 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.3286%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `instantiate` (Impact: 138.7)
  * `__lowerStaticArray` (Impact: 12.9)
  * `__release` (Impact: 10.3)
  * `__lowerRecord13` (Impact: 9.7)
  * `arrayOfStringsFunction` (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 108`, `args: 71`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 77`, `duplicate_logic: 3`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 44`, `concurrency: 9`, `import: 1`
* *Defense:* `safety: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/compiler/bindings/esm.release.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 603.32 | **LOC:** 562 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.3286%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `instantiate` (Impact: 138.7)
  * `__lowerStaticArray` (Impact: 12.9)
  * `__release` (Impact: 10.3)
  * `__lowerRecord13` (Impact: 9.7)
  * `arrayOfStringsFunction` (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 108`, `args: 71`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 77`, `duplicate_logic: 3`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 44`, `concurrency: 9`, `import: 1`
* *Defense:* `safety: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/compiler/bindings/raw.debug.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 595.54 | **LOC:** 523 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.5854%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `instantiate` (Impact: 138.7)
  * `__lowerStaticArray` (Impact: 12.9)
  * `__release` (Impact: 10.3)
  * `__lowerRecord13` (Impact: 9.7)
  * `arrayOfStringsFunction` (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 97`, `args: 70`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 77`, `duplicate_logic: 3`, `unreferenced_by_name: 19`
* *Architecture:* `api: 44`, `concurrency: 2`
* *Defense:* `safety: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/compiler/bindings/raw.release.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 595.54 | **LOC:** 523 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.5854%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `instantiate` (Impact: 138.7)
  * `__lowerStaticArray` (Impact: 12.9)
  * `__release` (Impact: 10.3)
  * `__lowerRecord13` (Impact: 9.7)
  * `arrayOfStringsFunction` (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 97`, `args: 70`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 77`, `duplicate_logic: 3`, `unreferenced_by_name: 19`
* *Architecture:* `api: 44`, `concurrency: 2`
* *Defense:* `safety: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/compiler.ts` -> Churn: **100.0%** | Cog Load: 53.1953% | Debt: 11.7106%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/builtins.ts` -> **Congcong Cai** (100.0% isolated ownership) | Magnitude: 6975.3
- `cli/index.js` -> **Max Graey** (100.0% isolated ownership) | Magnitude: 1521.4
- `src/ast.ts` -> **Congcong Cai** (100.0% isolated ownership) | Magnitude: 1030.82
- `std/portable/index.js` -> **Max Graey** (100.0% isolated ownership) | Magnitude: 303.26
- `std/assembly/rt/itcms.ts` -> **Congcong Cai** (100.0% isolated ownership) | Magnitude: 259.9

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `util/node.js` -> **Severity: 0.016** (Bridge: 0.0002 * Flux: 100.0%)
- `util/options.js` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 100.0%)
- `util/text.js` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `src/program.ts` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.9411%)
- `src/types.ts` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 90.7238%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/program.ts` -> **Severity: 1.587** (Embedded: 0.0206 * Error Risk: 76.9937%)
- `util/browser/url.js` -> **Severity: 1.247** (Embedded: 0.0188 * Error Risk: 66.5013%)
- `src/types.ts` -> **Severity: 1.235** (Embedded: 0.0193 * Error Risk: 63.8887%)
- `src/flow.ts` -> **Severity: 1.184** (Embedded: 0.0137 * Error Risk: 86.1311%)
- `src/bindings/js.ts` -> **Severity: 1.127** (Embedded: 0.0113 * Error Risk: 99.6071%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `util/browser/process.js` -> **Severity: 784.8** (Blast Radius: 7.848 * Doc Risk: 100.0%)
- `util/browser/path.js` -> **Severity: 722.1** (Blast Radius: 7.221 * Doc Risk: 100.0%)
- `util/browser/url.js` -> **Severity: 648.4** (Blast Radius: 6.484 * Doc Risk: 100.0%)
- `std/assembly/bindings/dom.ts` -> **Severity: 559.923** (Blast Radius: 6.488 * Doc Risk: 86.3014%)
- `util/terminal.js` -> **Severity: 498.314** (Blast Radius: 5.793 * Doc Risk: 86.02%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
