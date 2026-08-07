# ARCHITECTURAL_BRIEF: cyber
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_zig/cyber` |
| **Timestamp** | `2026-08-07T04:29:17.575690+00:00` |
| **Scan Duration** | `2.42s` |
| **Git Branch** | `master` |
| **Git Commit** | `c853fcc2b79da014ac40e9418db7c4cebea63177` |
| **Git Remote** | `https://github.com/fubark/cyber.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 140 malicious artifacts.

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
| Total Artifacts | 594 |
| Analyzed Artifacts (Scanned) | 163 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 431 |
| Total LOC | 67482 |
| Volatility Index | 0.037 |
| % Scanned of codebase = | 27.4% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3893 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4774 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 20.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5975 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 86 | 62160 | 52.8% |
| C | 15 | 2868 | 9.2% |
| MARKDOWN | 10 | 0 | 6.1% |
| LUA | 10 | 742 | 6.1% |
| PLAINTEXT | 7 | 0 | 4.3% |
| JAVASCRIPT | 6 | 570 | 3.7% |
| PYTHON | 5 | 208 | 3.1% |
| JAVA | 4 | 272 | 2.5% |
| PHP | 4 | 50 | 2.5% |
| RUBY | 4 | 38 | 2.5% |
| MAKEFILE | 2 | 14 | 1.2% |
| JSON | 2 | 74 | 1.2% |
| PERL | 2 | 17 | 1.2% |
| HTML | 1 | 241 | 0.6% |
| CSS | 1 | 141 | 0.6% |
| SHELL | 1 | 40 | 0.6% |
| GO | 1 | 15 | 0.6% |
| CPP | 1 | 22 | 0.6% |
| RUST | 1 | 10 | 0.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.518`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 86 | 52.8% |
| file_cluster_13 | 26 | 16.0% |
| file_cluster_0 | 10 | 6.1% |
| file_cluster_4 | 6 | 3.7% |
| file_cluster_11 | 5 | 3.1% |
| file_cluster_16 | 4 | 2.5% |
| file_cluster_6 | 3 | 1.8% |
| file_cluster_17 | 3 | 1.8% |
| file_cluster_9 | 2 | 1.2% |
| file_cluster_12 | 1 | 0.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 17 | 10.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 431*

**Composition by Extension & Reason:**
- `.cy`: 324x Unsupported Format (.cy), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2578 LOC)
- `.c`: 43x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.tmPreferences'), 1x Excluded (Unsupported Extension: '.sublime-syntax')
- `.wren`: 5x Unsupported Format (.wren)
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zig`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.vim`: 4x Excluded (Unsupported Extension: '.vim')
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.def`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 25.0 | 20.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 58.5 | 68.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 35.0 | 2.6 | 80.0 |
| API Exposure | 0.0 | 19.7 | 5.0 | 3.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 14.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 91.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.1 | 0.9 | 0.5 | 2.1 |
| Volatility Exposure | 0.0 | 100.0 | 28.3 | 15.6 | 15.6 |
| Documentation Exposure | 0.0 | 100.0 | 50.4 | 52.9 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/app_debug.zig` (Hits: 44)
- `src/platform.zig` (Hits: 32)
- `src/cli.zig` (Hits: 17)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **stdx.zig** (`src/stdx/stdx.zig`) — 40 inbound connections
2. **cyber.zig** (`src/cyber.zig`) — 38 inbound connections
3. **capi.zig** (`src/capi.zig`) — 29 inbound connections
4. **fmt.zig** (`src/fmt.zig`) — 11 inbound connections
5. **time.zig** (`src/stdx/time.zig`) — 7 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **cyber.zig** (`src/cyber.zig`) — 40 outbound dependencies
2. **compiler.zig** (`src/compiler.zig`) — 20 outbound dependencies
3. **vm.zig** (`src/vm.zig`) — 14 outbound dependencies
4. **cli.zig** (`src/cli.zig`) — 12 outbound dependencies
5. **core.zig** (`src/builtins/core.zig`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `resolveUserFuncVariant` (@ `src/sema.zig`) -> Impact: **1158.9** | LOC: 1398
- `getBinOpName` (@ `src/sema.zig`) -> Impact: **654.7** | LOC: 762
- `gen_declare_local` (@ `src/bc_gen.zig`) -> Impact: **624.9** | LOC: 1097
- `evalExprNoCheck` (@ `src/cte.zig`) -> Impact: **588.5** | LOC: 650
- `genHeader` (@ `src/cgen.zig`) -> Impact: **544.6** | LOC: 612
- `genVmToExternFunc` (@ `src/cgen.zig`) -> Impact: **429.2** | LOC: 403
  * *Intent:* /// If `func` is an extern variant (for variadic), `call_func` is the extern function. /// Otherwise, `func == call_func`.
- `genArrayConvDecls` (@ `src/std/os_ffi.zig`) -> Impact: **414.4** | LOC: 633
  * *Intent:* // Generate array conversions declarations.
- `writeSymName` (@ `src/sym.zig`) -> Impact: **329.4** | LOC: 237
- `parseTightTermLeft` (@ `src/parser.zig`) -> Impact: **304.9** | LOC: 348
- `semaAssignStmt` (@ `src/sema.zig`) -> Impact: **268.5** | LOC: 227
  * *Intent:* /// Pass rightId explicitly to perform custom sema on op assign rhs.

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 61 | 46604.34 | 25.84% | 32.96% |
| `src/builtins` | 6 | 4461.68 | 39.18% | 9.36% |
| `src/jit` | 9 | 2676.4 | 20.81% | 24.1% |
| `src/test/bench/heap` | 6 | 1977.3 | 34.33% | 0.0% |
| `src/std` | 5 | 1148.02 | 37.23% | 6.84% |
| `examples/web-playground` | 4 | 991.97 | 34.93% | 0.0% |
| `src/stdx` | 7 | 669.8 | 35.35% | 60.49% |
| `src/test` | 1 | 402.5 | 24.9% | 0.0% |
| `examples/android/ndk_app` | 5 | 247.58 | 18.25% | 0.0% |
| `src/include` | 1 | 235.9 | 0.0% | 16.08% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/hash.zig` -> **100.0%** Exposure
- `src/http.zig` -> **100.0%** Exposure
- `src/stdx/stdx.zig` -> **100.0%** Exposure
- `src/sync.zig` -> **99.9998%** Exposure
- `src/runtime.zig` -> **99.9997%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/aot.c` -> **100.0%** Exposure
- `src/vm.c` -> **100.0%** Exposure
- `install.sh` -> **100.0%** Exposure
- `src/std/math.zig` -> **99.999%** Exposure
- `src/simd.zig` -> **99.992%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/aot.c` -> **34** Orphaned Functions | **0** Duplicates
- `src/runtime.zig` -> **25** Orphaned Functions | **4** Duplicates
- `src/types.zig` -> **0** Orphaned Functions | **29** Duplicates
- `src/sym.zig` -> **0** Orphaned Functions | **27** Duplicates
- `src/http.zig` -> **0** Orphaned Functions | **25** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/builtins/c.zig`** -> AI Confidence: **99.48%**
2. **`src/std/os_ffi.zig`** -> AI Confidence: **99.48%**
3. **`src/jit/gen.zig`** -> AI Confidence: **99.43%**
4. **`src/jit/x64_assembler.zig`** -> AI Confidence: **99.43%**
5. **`src/bytecode.zig`** -> AI Confidence: **99.42%**
6. **`src/cgen.zig`** -> AI Confidence: **99.42%**
7. **`src/compiler.zig`** -> AI Confidence: **99.42%**
8. **`src/behavior_test.zig`** -> AI Confidence: **99.39%**
9. **`src/debug.zig`** -> AI Confidence: **99.39%**
10. **`src/fiber.zig`** -> AI Confidence: **99.39%**
11. **`src/main.zig`** -> AI Confidence: **99.39%**
12. **`src/runtime.zig`** -> AI Confidence: **99.39%**
13. **`src/heap.zig`** -> AI Confidence: **99.34%**
14. **`src/builtins/bindings.zig`** -> AI Confidence: **99.33%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `467` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/aot.c` (C) -> Cumulative Risk: **671.94**
- **Archetype:** `file_cluster_8` (Distance: 13.047 IQR)
- **Magnitude:** 388.84 | **LOC:** 377 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9998%), Tech Debt (99.9681%)
- **Heaviest Functions:** `cb_byte_fmt` (Impact: 13.7), `cb_float_fmt` (Impact: 7.8), `printStackTrace` (Impact: 3.9)

### 2. `src/jit/stencils.c` (C) -> Cumulative Risk: **640.38**
- **Archetype:** `file_cluster_0` (Distance: 19.224 IQR)
- **Magnitude:** 86.02 | **LOC:** 194 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9918%), Dead Code (96.8392%)

### 3. `src/builtins/string.zig` (ZIG) -> Cumulative Risk: **605.27**
- **Archetype:** `file_cluster_8` (Distance: 13.866 IQR)
- **Magnitude:** 708.8 | **LOC:** 584 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9528%), Safety Score (91.0696%)
- **Heaviest Functions:** `index_any_rune` (Impact: 50.1), `repeat` (Impact: 33.3), `slice2` (Impact: 31.2)

### 4. `src/sync.zig` (ZIG) -> Cumulative Risk: **602.63**
- **Archetype:** `file_cluster_4` (Distance: 11.608 IQR)
- **Magnitude:** 97.64 | **LOC:** 83 | **CtrlFlow:** 70.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9998%), Documentation (99.4246%)
- **Heaviest Functions:** `write_lock` (Impact: 11.0), `read_lock` (Impact: 9.3), `write_lock` (Impact: 9.3)

### 5. `src/debug.zig` (ZIG) -> Cumulative Risk: **586.44**
- **Archetype:** `file_cluster_11` (Distance: 15.047 IQR)
- **Magnitude:** 852.8 | **LOC:** 878 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Verification (80.0%), State Flux (77.1439%)
- **Heaviest Functions:** `dumpBytecode` (Impact: 50.5), `write_value_desc` (Impact: 42.2), `writeUserErrorTrace2` (Impact: 38.0)

### 6. `src/std/os.zig` (ZIG) -> Cumulative Risk: **582.76**
- **Archetype:** `file_cluster_13` (Distance: 16.571 IQR)
- **Magnitude:** 191.22 | **LOC:** 261 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (80.1865%), Verification (80.0%), Dead Code (69.8377%)
- **Heaviest Functions:** `allocCacheUrl` (Impact: 25.6), `_args` (Impact: 17.2), `dlopen` (Impact: 17.0)

### 7. `src/vm.c` (C) -> Cumulative Risk: **575.9**
- **Archetype:** `file_cluster_8` (Distance: 13.167 IQR)
- **Magnitude:** 794.96 | **LOC:** 1771 | **CtrlFlow:** 77.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.9313%)
- **Heaviest Functions:** `i2c` (Impact: 1.2)

### 8. `src/cli.zig` (ZIG) -> Cumulative Risk: **565.82**
- **Archetype:** `file_cluster_13` (Distance: 14.212 IQR)
- **Magnitude:** 567.84 | **LOC:** 750 | **CtrlFlow:** 66.6% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (83.3926%), Verification (80.0%), Safety Score (70.3349%)
- **Heaviest Functions:** `zResolve` (Impact: 71.4), `loadUrl` (Impact: 61.3), `loader` (Impact: 44.6)

### 9. `src/http.zig` (ZIG) -> Cumulative Risk: **553.47**
- **Archetype:** `file_cluster_6` (Distance: 15.035 IQR)
- **Magnitude:** 178.26 | **LOC:** 280 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (99.1135%), Verification (80.0%)
- **Heaviest Functions:** `fetch` (Impact: 17.9), `request` (Impact: 17.7), `fetch` (Impact: 13.0)

### 10. `src/std/math.zig` (ZIG) -> Cumulative Risk: **545.7**
- **Archetype:** `file_cluster_8` (Distance: 13.532 IQR)
- **Magnitude:** 341.04 | **LOC:** 345 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.999%), Safety Score (86.4491%)
- **Heaviest Functions:** `isInt` (Impact: 7.4), `bind` (Impact: 5.5), `frac` (Impact: 3.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/sema.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.261 IQR)
- **Top Global Matches:** file_cluster_11: 15.261, file_cluster_0: 15.338, file_cluster_16: 15.375
- **Magnitude:** 7404.98 | **LOC:** 10486 | **CtrlFlow:** 74.2% | **Authorship Centralization:** 90.0%
- **Risk Profile:** Cognitive Load (54.1095%), Tech Debt (18.4466%)
**Top Internal Functions/Classes:**
  * `resolveUserFuncVariant` (Impact: 1158.9)
  * `getBinOpName` (Impact: 654.7)
  * `semaAssignStmt` (Impact: 268.5)
    * *Intent:* /// Pass rightId explicitly to perform custom sema on op assign rhs.
  * `semaStmt` (Impact: 266.4)
  * `sema_bin_expr2` (Impact: 200.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3977`, `structural_boundaries: 1381`, `args: 384`, `func_start: 379`, `class_start: 50`
* *Risk/State:* `safety_bypasses: 506`, `high_risk_execution: 2`, `state_mutation: 852`, `dead_code: 91`, `planned_debt: 45`, `duplicate_logic: 16`
* *Architecture:* `api: 328`, `import: 8`
* *Defense:* `safety: 1785`, `doc: 97`, `test: 1`, `immutability_locks: 1602`, `cleanup: 77`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.553
  * `Choke Point (Betweenness):` 0.000133 | `Ripple Effect (Closeness):` 0.123737
  * `Imports (Out-Degree: 4):` builtin, vm.zig, cyber.zig, stdx, capi.zig, vmc, build_options, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/parser.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.691 IQR)
- **Top Global Matches:** file_cluster_8: 13.691, file_cluster_0: 13.898, file_cluster_11: 13.961
- **Magnitude:** 4123.7 | **LOC:** 4810 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (32.3926%), Tech Debt (12.2075%)
**Top Internal Functions/Classes:**
  * `parseTightTermLeft` (Impact: 304.9)
  * `parseExprWithLeft` (Impact: 182.5)
  * `parseForCase` (Impact: 123.8)
  * `parseTightTermWithLeft` (Impact: 121.6)
  * `parseStatement` (Impact: 118.4)
    * *Intent:* /// Does not consume line end.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1764`, `structural_boundaries: 680`, `args: 132`, `func_start: 121`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 135`, `state_mutation: 377`, `dead_code: 25`, `planned_debt: 3`, `duplicate_logic: 5`
* *Architecture:* `api: 18`, `import: 6`
* *Defense:* `safety: 631`, `doc: 29`, `test: 1`, `immutability_locks: 403`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.553
  * `Choke Point (Betweenness):` 0.000133 | `Ripple Effect (Closeness):` 0.123737
  * `Imports (Out-Degree: 4):` builtin, cyber.zig, stdx, capi.zig, fmt.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cgen.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.42%)
- **Global Archetype:** `file_cluster_0` (Drift: 16.594 IQR)
- **Top Global Matches:** file_cluster_0: 16.594, file_cluster_11: 16.597, file_cluster_6: 16.607
- **Magnitude:** 3240.82 | **LOC:** 3188 | **CtrlFlow:** 86.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.2226%), Tech Debt (18.7777%)
**Top Internal Functions/Classes:**
  * `genHeader` (Impact: 544.6)
  * `genVmToExternFunc` (Impact: 429.2)
    * *Intent:* /// If `func` is an extern variant (for variadic), `call_func` is the extern function. /// Otherwise...
  * `declareType` (Impact: 267.0)
    * *Intent:* /// DFS declaration to ensure type dependencies are declared first.
  * `gen` (Impact: 224.5)
  * `genBinOp` (Impact: 178.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1238`, `structural_boundaries: 189`, `args: 143`, `func_start: 143`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 119`, `dead_code: 100`, `planned_debt: 17`, `duplicate_logic: 4`
* *Architecture:* `io: 8`, `api: 37`, `import: 7`
* *Defense:* `safety: 816`, `doc: 11`, `immutability_locks: 266`, `cleanup: 34`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.553
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.123737
  * `Imports (Out-Degree: 2):` builtin, tcc, cyber.zig, build_config, capi.zig, vmc, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/bc_gen.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.27%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.317 IQR)
- **Top Global Matches:** file_cluster_8: 14.317, file_cluster_16: 14.352, file_cluster_11: 14.409
- **Magnitude:** 2757.86 | **LOC:** 3082 | **CtrlFlow:** 84.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.0868%), Tech Debt (9.5774%)
**Top Internal Functions/Classes:**
  * `gen_declare_local` (Impact: 624.9)
  * `genAll` (Impact: 102.4)
  * `genCompare` (Impact: 74.5)
  * `genStmt` (Impact: 65.2)
  * `genBinOp` (Impact: 55.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1037`, `structural_boundaries: 198`, `args: 166`, `func_start: 166`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 106`, `high_risk_execution: 2`, `state_mutation: 133`, `dead_code: 17`, `planned_debt: 11`
* *Architecture:* `api: 49`, `import: 5`
* *Defense:* `safety: 628`, `doc: 39`, `immutability_locks: 381`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.516
  * `Choke Point (Betweenness):` 3.8e-05 | `Ripple Effect (Closeness):` 0.09387
  * `Imports (Out-Degree: 2):` builtin, gen.zig, cyber.zig, capi.zig, std
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/cte.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.01%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.42 IQR)
- **Top Global Matches:** file_cluster_8: 13.42, file_cluster_16: 13.42, file_cluster_11: 13.495
- **Magnitude:** 2678.22 | **LOC:** 2800 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 88.9%
- **Risk Profile:** Cognitive Load (35.0013%), Tech Debt (11.0164%)
**Top Internal Functions/Classes:**
  * `evalExprNoCheck` (Impact: 588.5)
  * `eval_bin_expr2` (Impact: 241.1)
  * `switchStmt` (Impact: 239.8)
  * `evalCallExpr` (Impact: 131.4)
  * `eval_un_expr` (Impact: 91.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1047`, `structural_boundaries: 466`, `args: 64`, `func_start: 63`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 54`, `dead_code: 27`, `planned_debt: 19`
* *Architecture:* `api: 40`, `import: 4`
* *Defense:* `safety: 343`, `doc: 6`, `immutability_locks: 550`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.553
  * `Choke Point (Betweenness):` 0.000261 | `Ripple Effect (Closeness):` 0.123737
  * `Imports (Out-Degree: 3):` bc_gen.zig, capi.zig, cyber.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/builtins/core.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.072 IQR)
- **Top Global Matches:** file_cluster_11: 14.072, file_cluster_8: 14.074, file_cluster_0: 14.084
- **Magnitude:** 1888.88 | **LOC:** 2220 | **CtrlFlow:** 66.9% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (35.6348%), Tech Debt (23.6422%)
**Top Internal Functions/Classes:**
  * `bitCast` (Impact: 51.3)
  * `Int_init` (Impact: 37.0)
    * *Intent:* /// Compile-time version of Int conversions. It should be faster than interpreting `Int[].@init`.
  * `intFmtExt` (Impact: 34.9)
  * `rawFmtExt` (Impact: 30.2)
  * `call` (Impact: 29.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 563`, `structural_boundaries: 279`, `args: 147`, `func_start: 146`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 124`, `high_risk_execution: 5`, `state_mutation: 304`, `dead_code: 12`, `planned_debt: 7`, `duplicate_logic: 5`
* *Architecture:* `api: 88`, `import: 10`
* *Defense:* `safety: 216`, `doc: 1`, `sync_locks: 2`, `immutability_locks: 482`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` builtin, string.zig, fmt.zig, stdx, cyber.zig, bindings.zig, capi.zig, build_options...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sema_func.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.04%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.979 IQR)
- **Top Global Matches:** file_cluster_11: 13.979, file_cluster_0: 14.066, file_cluster_16: 14.148
- **Magnitude:** 1615.3 | **LOC:** 1430 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.5593%), Tech Debt (20.3937%)
**Top Internal Functions/Classes:**
  * `resolveRtArg` (Impact: 178.9)
  * `inferCtArgs` (Impact: 110.4)
    * *Intent:* /// CtInfer types are extracted from `arg_t`.
  * `matchTemplateArg` (Impact: 94.4)
  * `matchTemplateArgCt` (Impact: 92.1)
  * `matchPreArgCt` (Impact: 91.9)
    * *Intent:* // Owns a copy of the argument, unless its obtaining a borrow to a receiver.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 477`, `structural_boundaries: 206`, `args: 31`, `func_start: 30`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 223`, `dead_code: 15`, `planned_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 23`, `import: 3`
* *Defense:* `safety: 153`, `doc: 3`, `immutability_locks: 226`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.553
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.123737
  * `Imports (Out-Degree: 2):` capi.zig, cyber.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/heap.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.538 IQR)
- **Top Global Matches:** file_cluster_8: 12.538, file_cluster_7: 12.825, file_cluster_13: 12.827
- **Magnitude:** 1324.74 | **LOC:** 1828 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.8285%), Tech Debt (40.9357%)
**Top Internal Functions/Classes:**
  * `allocClosure` (Impact: 31.4)
    * *Intent:* /// Captured values are retained during alloc.
  * `newChoice` (Impact: 23.5)
  * `deinit` (Impact: 20.9)
  * `allocVector` (Impact: 19.2)
    * *Intent:* /// Reuse `Object` so that address_of refers to the first element for both structs and arrays.
  * `newInstance` (Impact: 17.4)
    * *Intent:* /// Arguments are consumed.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 367`, `structural_boundaries: 160`, `args: 133`, `func_start: 132`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 103`, `high_risk_execution: 1`, `state_mutation: 75`, `dead_code: 3`, `duplicate_logic: 13`
* *Architecture:* `api: 279`, `import: 8`
* *Defense:* `safety: 131`, `doc: 34`, `test: 2`, `immutability_locks: 400`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` builtin, tcc, heap_value.zig, cyber.zig, stdx, build_config, capi.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sym.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.538 IQR)
- **Top Global Matches:** file_cluster_8: 12.538, file_cluster_16: 12.59, file_cluster_0: 12.813
- **Magnitude:** 1313.38 | **LOC:** 1733 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.2691%), Tech Debt (98.9956%)
**Top Internal Functions/Classes:**
  * `writeSymName` (Impact: 329.4)
  * `declNode` (Impact: 42.9)
  * `getSymValueType` (Impact: 34.7)
  * `writeFuncName` (Impact: 23.2)
  * `write_func_base_name` (Impact: 18.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 425`, `structural_boundaries: 165`, `args: 98`, `func_start: 97`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 88`, `high_risk_execution: 2`, `state_mutation: 37`, `dead_code: 3`, `planned_debt: 5`, `fragile_debt: 1`, `duplicate_logic: 27`
* *Architecture:* `api: 163`, `import: 5`
* *Defense:* `safety: 160`, `doc: 38`, `test: 1`, `immutability_locks: 165`, `cleanup: 57`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.553
  * `Choke Point (Betweenness):` 0.000133 | `Ripple Effect (Closeness):` 0.123737
  * `Imports (Out-Degree: 3):` builtin, cyber.zig, stdx, capi.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/llvm_gen.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_9` (Drift: 24.257 IQR)
- **Top Global Matches:** file_cluster_9: 24.257, file_cluster_6: 24.306, file_cluster_17: 24.334
- **Magnitude:** 1174.02 | **LOC:** 1456 | **CtrlFlow:** 77.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.8609%), Tech Debt (9.567%)
**Top Internal Functions/Classes:**
  * `postExpr` (Impact: 206.9)
  * `genCallExpr` (Impact: 146.0)
  * `genStatement` (Impact: 128.6)
  * `genBinExpr2` (Impact: 109.4)
    * *Intent:* /// Abstracted to allow assign op to share codegen with binExpr.
  * `genIdent` (Impact: 106.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 556`, `structural_boundaries: 158`, `args: 23`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 90`, `dead_code: 346`, `planned_debt: 4`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 235`, `doc: 4`, `immutability_locks: 221`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 5.8e-05 | `Ripple Effect (Closeness):` 0.08642
  * `Imports (Out-Degree: 3):` fmt.zig, llvm.zig, cyber.zig, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/sema_type.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.25 IQR)
- **Top Global Matches:** file_cluster_8: 13.25, file_cluster_16: 13.374, file_cluster_0: 13.403
- **Magnitude:** 1137.48 | **LOC:** 1339 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.9517%), Tech Debt (9.7794%)
**Top Internal Functions/Classes:**
  * `resolveStructFields` (Impact: 66.8)
    * *Intent:* /// Explicit `decl` node for distinct type declarations. Must belong to `c`.
  * `reserve_template_instance` (Impact: 65.9)
    * *Intent:* /// Allow an explicit `opt_header_decl` so that template specialization can use it to override @host...
  * `ensure_resolved_type` (Impact: 51.8)
  * `resolveAnyParamType` (Impact: 48.0)
    * *Intent:* /// Handles generic and dependent types.
  * `declare_choice_cases` (Impact: 44.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 381`, `structural_boundaries: 137`, `args: 44`, `func_start: 44`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 136`, `state_mutation: 144`, `dead_code: 3`, `planned_debt: 4`
* *Architecture:* `api: 53`, `import: 3`
* *Defense:* `safety: 177`, `doc: 8`, `immutability_locks: 192`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.553
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.123737
  * `Imports (Out-Degree: 2):` capi.zig, cyber.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/compiler.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.42%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.724 IQR)
- **Top Global Matches:** file_cluster_13: 13.724, file_cluster_8: 13.762, file_cluster_0: 13.82
- **Magnitude:** 1107.34 | **LOC:** 1504 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (20.4721%), Tech Debt (20.947%)
**Top Internal Functions/Classes:**
  * `compileInner` (Impact: 220.7)
    * *Intent:* /// Wrap compile so all errors can be handled in one place.
  * `loadBuiltinChunk` (Impact: 105.6)
  * `reserveChunkSyms` (Impact: 76.1)
    * *Intent:* // /// `src` is consumed. // pub fn createModule(self: *Compiler, r_uri: []const u8, src: ?[]const u...
  * `deinit` (Impact: 41.3)
  * `loadChunk` (Impact: 35.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 436`, `structural_boundaries: 93`, `args: 47`, `func_start: 45`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 80`, `dead_code: 9`, `planned_debt: 3`, `duplicate_logic: 3`
* *Architecture:* `io: 1`, `api: 34`, `import: 20`
* *Defense:* `safety: 274`, `doc: 30`, `test: 1`, `immutability_locks: 195`, `cleanup: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.553
  * `Choke Point (Betweenness):` 0.00116 | `Ripple Effect (Closeness):` 0.123737
  * `Imports (Out-Degree: 6):` stdx, builtin, gen.zig, a64.zig, cyber.zig, io.zig, vmc, math.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/types.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.939 IQR)
- **Top Global Matches:** file_cluster_8: 10.939, file_cluster_7: 11.253, file_cluster_13: 11.363
- **Magnitude:** 1062.98 | **LOC:** 1508 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.9073%), Tech Debt (99.8501%)
**Top Internal Functions/Classes:**
  * `size` (Impact: 44.8)
    * *Intent:* /// Returns the size in bytes.
  * `alignment` (Impact: 44.7)
  * `isRtTypeCompat` (Impact: 38.0)
  * `isConstEligible` (Impact: 28.2)
    * *Intent:* /// What is const eligible is a subset of what is eval eligible. /// The type must be immutable.
  * `get_trait_method_impl` (Impact: 27.5)
    * *Intent:* /// Assumes types and functions are already resolved.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 357`, `structural_boundaries: 214`, `args: 93`, `func_start: 90`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 55`, `high_risk_execution: 7`, `state_mutation: 20`, `dead_code: 3`, `planned_debt: 9`, `duplicate_logic: 29`
* *Architecture:* `api: 191`, `import: 6`
* *Defense:* `safety: 34`, `doc: 40`, `test: 1`, `immutability_locks: 178`, `cleanup: 55`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.553
  * `Choke Point (Betweenness):` 0.000133 | `Ripple Effect (Closeness):` 0.123737
  * `Imports (Out-Degree: 4):` cyber.zig, stdx, capi.zig, vmc, fmt.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/builtins/meta.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.756 IQR)
- **Top Global Matches:** file_cluster_11: 13.756, file_cluster_0: 13.766, file_cluster_8: 13.805
- **Magnitude:** 1008.18 | **LOC:** 1185 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (29.0625%), Tech Debt (10.4716%)
**Top Internal Functions/Classes:**
  * `type_info2` (Impact: 210.2)
  * `init_type` (Impact: 58.6)
  * `type_init` (Impact: 31.2)
  * `type_field` (Impact: 22.1)
  * `newFuncInfo` (Impact: 19.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 379`, `structural_boundaries: 167`, `args: 67`, `func_start: 67`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 50`, `high_risk_execution: 1`, `state_mutation: 87`, `dead_code: 8`, `planned_debt: 5`
* *Architecture:* `io: 2`, `api: 53`, `import: 5`
* *Defense:* `safety: 191`, `immutability_locks: 305`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` builtin, cyber.zig, build_config, capi.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/heap_value.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.5 IQR)
- **Top Global Matches:** file_cluster_8: 11.5, file_cluster_0: 11.799, file_cluster_13: 11.856
- **Magnitude:** 966.2 | **LOC:** 1171 | **CtrlFlow:** 77.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.6287%), Tech Debt (9.8988%)
**Top Internal Functions/Classes:**
  * `writeValue` (Impact: 149.6)
    * *Intent:* /// Assumes `val` is unboxed. /// Returns whether the string written can be assumed to be ASCII. ///...
  * `destroyObject` (Impact: 114.3)
  * `copyValue3` (Impact: 56.4)
  * `box` (Impact: 49.1)
  * `bufPrintValueShortStr` (Impact: 45.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 339`, `structural_boundaries: 100`, `args: 43`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 66`, `high_risk_execution: 14`, `state_mutation: 26`, `dead_code: 6`, `planned_debt: 4`
* *Architecture:* `io: 1`, `api: 55`, `import: 6`
* *Defense:* `safety: 78`, `doc: 5`, `immutability_locks: 145`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.894
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006173
  * `Imports (Out-Degree: 2):` tcc, cyber.zig, build_config, capi.zig, vmc, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/vm.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.249 IQR)
- **Top Global Matches:** file_cluster_13: 13.249, file_cluster_0: 13.255, file_cluster_8: 13.275
- **Magnitude:** 945.98 | **LOC:** 1397 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.8653%), Tech Debt (41.975%)
**Top Internal Functions/Classes:**
  * `deinit` (Impact: 70.8)
  * `eval` (Impact: 67.1)
  * `findType` (Impact: 47.4)
  * `zAwait` (Impact: 31.6)
  * `zCallTrait` (Impact: 26.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `structural_boundaries: 120`, `args: 89`, `func_start: 82`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 40`, `dead_code: 14`, `planned_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 2`, `api: 122`, `concurrency: 15`, `import: 14`
* *Defense:* `safety: 112`, `doc: 19`, `test: 1`, `sync_locks: 2`, `immutability_locks: 168`, `cleanup: 54`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.732
  * `Choke Point (Betweenness):` 0.001946 | `Ripple Effect (Closeness):` 0.12516
  * `Imports (Out-Degree: 6):` builtin, tcc, bindings.zig, bc_gen.zig, cyber.zig, stdx, build_config, capi.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/web-playground/cyber-mode.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.233 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.527 IQR)
- **Top Global Matches:** file_cluster_8: 12.233, file_cluster_4: 12.319, file_cluster_11: 12.534
- **Magnitude:** 888.08 | **LOC:** 385 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.4142%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cyber` (Impact: 261.0)
  * `formatStringFactory` (Impact: 178.5)
  * `tokenString` (Impact: 165.1)
  * `tokenBaseInner` (Impact: 76.0)
  * `tokenBase` (Impact: 25.3)
    * *Intent:* // tokenizers
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 93`, `args: 19`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 139`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `concurrency: 12`
* *Defense:* `safety: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006173
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/jit/gen.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.43%)
- **Global Archetype:** `file_cluster_6` (Drift: 17.6 IQR)
- **Top Global Matches:** file_cluster_6: 17.6, file_cluster_0: 17.656, file_cluster_9: 17.663
- **Magnitude:** 875.92 | **LOC:** 1087 | **CtrlFlow:** 87.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.0947%), Tech Debt (14.3506%)
**Top Internal Functions/Classes:**
  * `gen_func` (Impact: 190.5)
  * `genStmt` (Impact: 83.7)
  * `mainBlock` (Impact: 44.0)
  * `funcBlock` (Impact: 38.1)
  * `genCallFuncSym` (Impact: 32.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 362`, `structural_boundaries: 52`, `args: 42`, `func_start: 41`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 35`, `dead_code: 58`, `planned_debt: 11`
* *Architecture:* `io: 16`, `api: 37`, `import: 12`
* *Defense:* `safety: 206`, `doc: 6`, `immutability_locks: 170`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.74
  * `Choke Point (Betweenness):` 0.000249 | `Ripple Effect (Closeness):` 0.019753
  * `Imports (Out-Degree: 5):` builtin, bc_gen.zig, assembler.zig, a64_assembler.zig, cyber.zig, x64_assembler.zig, capi.zig, a64.zig...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/lib.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.512 IQR)
- **Top Global Matches:** file_cluster_0: 14.512, file_cluster_13: 14.623, file_cluster_9: 14.633
- **Magnitude:** 874.62 | **LOC:** 1063 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.3444%), Tech Debt (20.2623%)
**Top Internal Functions/Classes:**
  * `loader` (Impact: 56.4)
  * `loader` (Impact: 26.9)
  * `cl_vm_evalx` (Impact: 15.8)
  * `cl_vm_eval_path` (Impact: 14.6)
  * `cl_vm_error_summary` (Impact: 14.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 142`, `args: 121`, `func_start: 113`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 87`, `dead_code: 16`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 201`, `import: 8`
* *Defense:* `safety: 111`, `doc: 1`, `test: 17`, `immutability_locks: 93`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.121
  * `Choke Point (Betweenness):` 0.000153 | `Ripple Effect (Closeness):` 0.006173
  * `Imports (Out-Degree: 3):` builtin, std, meta.zig, cyber.zig, stdx, build_config, capi.zig, mimalloc
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/thread.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.27%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.398 IQR)
- **Top Global Matches:** file_cluster_8: 12.398, file_cluster_13: 12.549, file_cluster_0: 12.591
- **Magnitude:** 863.56 | **LOC:** 1226 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.9857%), Tech Debt (25.853%)
**Top Internal Functions/Classes:**
  * `callUnion` (Impact: 41.7)
  * `unwindStack` (Impact: 32.4)
    * *Intent:* /// Unwind from `ctx` and release each frame. /// TODO: See if releaseFiberStack can resuse the same...
  * `freeHeapPages` (Impact: 23.4)
    * *Intent:* /// Sweep frees each heap object disregarding any dependencies. Triggered from fatal error. /// Only...
  * `get_ptr_layout` (Impact: 21.8)
  * `callTraitSymInst` (Impact: 21.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 116`, `args: 75`, `func_start: 75`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 84`, `high_risk_execution: 2`, `state_mutation: 81`, `dead_code: 4`, `planned_debt: 8`, `duplicate_logic: 2`
* *Architecture:* `api: 113`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 69`, `doc: 24`, `test: 1`, `immutability_locks: 140`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.553
  * `Choke Point (Betweenness):` 0.000133 | `Ripple Effect (Closeness):` 0.123737
  * `Imports (Out-Degree: 4):` builtin, cyber.zig, stdx, build_config, capi.zig, vmc, fmt.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/module.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.072 IQR)
- **Top Global Matches:** file_cluster_8: 13.072, file_cluster_13: 13.237, file_cluster_0: 13.275
- **Magnitude:** 858.48 | **LOC:** 670 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (24.7825%), Tech Debt (12.3259%)
**Top Internal Functions/Classes:**
  * `getResolvedSym` (Impact: 104.2)
    * *Intent:* /// Note that resolved refers to a resolved symbol path and not the underlying symbol content.
  * `getRefLikeChildSym` (Impact: 62.0)
  * `reserveFunc` (Impact: 38.4)
  * `get_pub_resolved_chunk_sym` (Impact: 35.3)
  * `reserveVariantFunc` (Impact: 30.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 78`, `args: 53`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 18`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `api: 89`, `import: 6`
* *Defense:* `safety: 125`, `doc: 7`, `test: 1`, `immutability_locks: 149`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.553
  * `Choke Point (Betweenness):` 0.000133 | `Ripple Effect (Closeness):` 0.123737
  * `Imports (Out-Degree: 3):` builtin, cyber.zig, stdx, capi.zig, build_options, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/debug.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.047 IQR)
- **Top Global Matches:** file_cluster_11: 15.047, file_cluster_0: 15.048, file_cluster_13: 15.141
- **Magnitude:** 852.8 | **LOC:** 878 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.887%), Tech Debt (28.2206%)
**Top Internal Functions/Classes:**
  * `dumpBytecode` (Impact: 50.5)
    * *Intent:* /// When `optPcContext` is null, all the bytecode is dumped along with constants. /// When `optPcCon...
  * `write_value_desc` (Impact: 42.2)
  * `writeUserErrorTrace2` (Impact: 38.0)
  * `write_object_trace` (Impact: 37.7)
  * `getStackFrame` (Impact: 26.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 113`, `args: 51`, `func_start: 46`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 3`, `state_mutation: 148`, `dead_code: 14`, `planned_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 63`, `import: 8`
* *Defense:* `safety: 146`, `doc: 7`, `test: 1`, `immutability_locks: 165`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` builtin, cyber.zig, stdx, capi.zig, vmc, bytecode.zig, fmt.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/vm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.167 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.491 IQR)
- **Top Global Matches:** file_cluster_8: 13.167, file_cluster_7: 13.559, file_cluster_13: 13.559
- **Magnitude:** 794.96 | **LOC:** 1771 | **CtrlFlow:** 77.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (55.8207%), Tech Debt (9.4376%)
**Top Internal Functions/Classes:**
  * `i2c` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 14`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 616`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `api: 161`, `import: 2`
* *Defense:* `safety: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vm.h, stdarg.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ast.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.494 IQR)
- **Top Global Matches:** file_cluster_8: 11.494, file_cluster_7: 11.847, file_cluster_0: 11.854
- **Magnitude:** 775.0 | **LOC:** 2098 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.6548%), Tech Debt (30.4328%)
**Top Internal Functions/Classes:**
  * `end` (Impact: 183.6)
  * `name` (Impact: 163.3)
  * `findAttr` (Impact: 19.9)
    * *Intent:* // var i: u32 = 0; // var cur = head; // while (cur != cy.NullNode) { // self.stack.items[self.stack...
  * `getString` (Impact: 16.5)
  * `src` (Impact: 15.9)
    * *Intent:* /// Source id.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 145`, `args: 59`, `func_start: 54`, `class_start: 106`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 3`, `state_mutation: 35`, `dead_code: 20`, `planned_debt: 5`, `duplicate_logic: 7`
* *Architecture:* `api: 148`, `import: 4`
* *Defense:* `safety: 34`, `doc: 15`, `test: 1`, `immutability_locks: 238`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.553
  * `Choke Point (Betweenness):` 0.000133 | `Ripple Effect (Closeness):` 0.123737
  * `Imports (Out-Degree: 2):` builtin, stdx, cyber.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/string.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.027 IQR)
- **Top Global Matches:** file_cluster_8: 13.027, file_cluster_11: 13.144, file_cluster_13: 13.144
- **Magnitude:** 743.6 | **LOC:** 776 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.7519%), Tech Debt (10.8136%)
**Top Internal Functions/Classes:**
  * `indexOfAsciiSetSimdFixed` (Impact: 39.6)
  * `indexOfAsciiSetSimdRemain` (Impact: 35.5)
  * `indexOfCharSimdFixed4` (Impact: 33.0)
  * `ustringSeekByRuneIndex` (Impact: 25.8)
    * *Intent:* /// `out_bad_byte` can be used to determine if it's an ascii string.
  * `indexOfChar` (Impact: 25.6)
    * *Intent:* /// For Ascii needle.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 224`, `structural_boundaries: 122`, `args: 42`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 141`, `dead_code: 3`, `planned_debt: 3`
* *Architecture:* `api: 55`, `import: 4`
* *Defense:* `safety: 45`, `doc: 13`, `test: 1`, `immutability_locks: 146`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` builtin, stdx, cyber.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/template.zig` (ZIG) | Magnitude: 488.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 412, branch: 166, immutability_locks: 86, pointers: 77
- `src/cgen.zig` (ZIG) | Magnitude: 3240.82 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 2612, branch: 1238, safety: 816, pointers: 337
- `src/jit/x64_assembler.zig` (ZIG) | Magnitude: 525.36 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 405, branch: 163, safety: 107, bitwise_ops: 98
- `src/bytecode.zig` (ZIG) | Magnitude: 373.96 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1077, immutability_locks: 249, branch: 185, globals: 177
- `src/jit/a64_assembler.zig` (ZIG) | Magnitude: 369.2 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 284, branch: 110, safety: 51, api: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/debug.zig` (ZIG) | Magnitude: 852.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 648, branch: 271, immutability_locks: 165, encapsulation: 162
- `src/builtins/core.zig` (ZIG) | Magnitude: 1888.88 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1614, encapsulation: 583, branch: 563, globals: 519
- `src/builtins/meta.zig` (ZIG) | Magnitude: 1008.18 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 893, branch: 379, encapsulation: 323, globals: 308
- `src/sema.zig` (ZIG) | Magnitude: 7404.98 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 8663, branch: 3977, safety: 1785, encapsulation: 1777
- `src/sema_func.zig` (ZIG) | Magnitude: 1615.3 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1167, branch: 477, encapsulation: 246, globals: 235

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `install.sh` (SHELL) | Magnitude: 71.6 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 36, branch: 27, indent_spaces: 21, reflection_metaprogramming: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/cli.zig` (ZIG) | Magnitude: 567.84 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 512, branch: 201, encapsulation: 117, immutability_locks: 115
- `src/vm.zig` (ZIG) | Magnitude: 945.98 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1016, branch: 309, immutability_locks: 168, encapsulation: 139
- `src/builtins/bindings.zig` (ZIG) | Magnitude: 181.48 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 154, immutability_locks: 64, branch: 49, pointers: 43
- `src/map.zig` (ZIG) | Magnitude: 322.04 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 358, branch: 116, encapsulation: 74, globals: 70
- `src/test/setup.zig` (ZIG) | Magnitude: 402.5 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 383, branch: 128, structural_boundaries: 70, immutability_locks: 62

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/log_wasm.zig` (ZIG) | Magnitude: 80.76 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, immutability_locks: 24, branch: 15, globals: 14
- `src/simd.zig` (ZIG) | Magnitude: 39.82 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, state_mutation: 9, branch: 8, explicit_casts: 8
- `src/utils.zig` (ZIG) | Magnitude: 92.58 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 62, api: 23, immutability_locks: 19, branch: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/test/bench/string/index.rs` (RUST) | Magnitude: 7.2 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 5, state_mutation: 3, branch: 1
- `src/test/bench/for/for.lua` (LUA) | Magnitude: 26.92 | Delta: **0.365 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 18, branch: 5, structural_boundaries: 5, encapsulation: 3
- `src/test/bench/for/for.luau` (LUA) | Magnitude: 26.92 | Delta: **0.365 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 18, branch: 5, structural_boundaries: 5, encapsulation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/app_debug.zig` (ZIG) | Magnitude: 217.8 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 270, branch: 80, io: 44, encapsulation: 37
- `src/test/bench/fiber/fiber.rb` (RUBY) | Magnitude: 17.26 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 12, indent_spaces: 7, globals: 4, closures: 3
- `src/sync.zig` (ZIG) | Magnitude: 97.64 | Delta: **0.39 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, concurrency: 26, branch: 17, api: 15
- `src/test/bench/fiber/fiber.lua` (LUA) | Magnitude: 52.42 | Delta: **0.528 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 23, concurrency: 18, structural_boundaries: 11, encapsulation: 8
- `src/test/bench/fiber/fiber.luau` (LUA) | Magnitude: 52.42 | Delta: **0.528 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 23, concurrency: 18, structural_boundaries: 11, encapsulation: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/behavior_test.zig` (ZIG) | Magnitude: 213.08 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 527, branch: 112, encapsulation: 86, immutability_locks: 71
- `src/jit/gen.zig` (ZIG) | Magnitude: 875.92 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 842, branch: 362, safety: 206, immutability_locks: 170
- `src/http.zig` (ZIG) | Magnitude: 178.26 | Delta: **0.179 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 218, pointers: 54, branch: 45, args: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/cte.zig` (ZIG) | Magnitude: 2678.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 2475, branch: 1047, encapsulation: 559, immutability_locks: 550
- `src/ct_inline.zig` (ZIG) | Magnitude: 294.84 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 333, branch: 137, immutability_locks: 60, encapsulation: 57
- `src/tools/llvm.h` (C) | Magnitude: 0.01 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 3
- `src/bc_gen.zig` (ZIG) | Magnitude: 2757.86 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 2264, branch: 1037, safety: 628, encapsulation: 514
- `src/sym.zig` (ZIG) | Magnitude: 1313.38 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1361, branch: 425, pointers: 232, structural_boundaries: 165

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/builtins/c.zig` (ZIG) | Magnitude: 441.5 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 385, branch: 186, safety: 114, encapsulation: 94
- `src/llvm_gen.zig` (ZIG) | Magnitude: 1174.02 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 1222, branch: 556, dead_code: 346, safety: 235

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/vm.c` -> Churn: **89.62%** | Cog Load: 55.8207% | Debt: 9.4376%
- `src/sema.zig` -> Churn: **86.49%** | Cog Load: 54.1095% | Debt: 18.4466%
- `src/behavior_test.zig` -> Churn: **79.25%** | Cog Load: 22.8583% | Debt: 78.3289%
- `src/jit/stencils.c` -> Churn: **75.0%** | Cog Load: 56.1567% | Debt: 18.0953%
- `src/cli.zig` -> Churn: **64.62%** | Cog Load: 32.8707% | Debt: 67.9924%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/sema.zig` -> **fubark** (90.0% isolated ownership) | Magnitude: 7404.98
- `src/parser.zig` -> **fubark** (100.0% isolated ownership) | Magnitude: 4123.7
- `src/cgen.zig` -> **fubark** (100.0% isolated ownership) | Magnitude: 3240.82
- `src/bc_gen.zig` -> **fubark** (100.0% isolated ownership) | Magnitude: 2757.86
- `src/cte.zig` -> **fubark** (88.9% isolated ownership) | Magnitude: 2678.22

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/cli.zig` -> **Severity: 0.065** (Bridge: 0.0015 * Flux: 42.459%)
- `src/fmt.zig` -> **Severity: 0.056** (Bridge: 0.003 * Flux: 18.6981%)
- `src/cache.zig` -> **Severity: 0.036** (Bridge: 0.0027 * Flux: 13.0427%)
- `src/lib.zig` -> **Severity: 0.007** (Bridge: 0.0002 * Flux: 42.7523%)
- `src/parser.zig` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 38.1665%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/cyber.zig` -> **Severity: 19.455** (Embedded: 0.2317 * Error Risk: 83.9733%)
- `src/capi.zig` -> **Severity: 14.716** (Embedded: 0.2016 * Error Risk: 72.992%)
- `src/stdx/time.zig` -> **Severity: 13.63** (Embedded: 0.1724 * Error Risk: 79.0765%)
- `src/simd.zig` -> **Severity: 12.099** (Embedded: 0.1268 * Error Risk: 95.4026%)
- `src/utils.zig` -> **Severity: 11.06** (Embedded: 0.1237 * Error Risk: 89.384%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/cyber.zig` -> **Severity: 8259.4** (Blast Radius: 82.594 * Doc Risk: 100.0%)
- `src/stdx/time.zig` -> **Severity: 5364.463** (Blast Radius: 53.715 * Doc Risk: 99.869%)
- `src/stdx/time_wasm.zig` -> **Severity: 4885.015** (Blast Radius: 48.863 * Doc Risk: 99.9737%)
- `src/capi.zig` -> **Severity: 4838.4** (Blast Radius: 48.384 * Doc Risk: 100.0%)
- `src/stdx/stdx.zig` -> **Severity: 4452.729** (Blast Radius: 83.492 * Doc Risk: 53.3312%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
