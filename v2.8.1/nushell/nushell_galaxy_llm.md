# ARCHITECTURAL_BRIEF: nushell
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/nushell/nushell.git` |
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
| Total Artifacts | 2227 |
| Analyzed Artifacts (Scanned) | 1782 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 445 |
| Total LOC | 295400 |
| Volatility Index | 0.008 |
| % Scanned of codebase = | 80.0% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8663 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3038 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0109 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 20 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1616 | 293473 | 90.7% |
| MARKDOWN | 61 | 0 | 3.4% |
| JSON | 39 | 609 | 2.2% |
| PLAINTEXT | 27 | 3 | 1.5% |
| YAML | 21 | 362 | 1.2% |
| SHELL | 5 | 92 | 0.3% |
| CSV | 3 | 71 | 0.2% |
| DOCKERFILE | 2 | 80 | 0.1% |
| POWERSHELL | 2 | 25 | 0.1% |
| NIX | 2 | 289 | 0.1% |
| JAVASCRIPT | 1 | 182 | 0.1% |
| PYTHON | 1 | 189 | 0.1% |
| BATCH | 1 | 25 | 0.1% |
| XML | 1 | 0 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +1.79; from the repo's file-archetype mix)
> **File Composition:** State Mutators Files 36%, Tests & Verification Files 19%, Large Core Modules 14%, Data / Markup / Trivial 14%, Declarative / Non-Code 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1692 | 94.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 87 | 4.9% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 445*

**Composition by Extension & Reason:**
- `.nu`: 156x Unsupported Format (.nu), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 47x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 31x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.blockcommandparser')
- `.hjson`: 59x Excluded (Unsupported Extension: '.hjson')
- `.toml`: 43x Unsupported Format (.toml), 7x Excluded (Unsupported Extension: '.toml'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 39 exceeds 500 chars), 1x Excluded (Saturation: Line 43 exceeds 500 chars)
- `.yml`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 14x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.nuon`: 3x Excluded (Unsupported Extension: '.nuon')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock'), 1x Unsupported Format (.lock)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.exe`: 2x Excluded (Explicitly Denied Extension: '.exe')
- `.ini`: 2x Excluded (Unsupported Extension: '.ini')
- `.ods`: 2x Excluded (Explicitly Denied Extension: '.ods')
- `.xlsx`: 2x Excluded (Explicitly Denied Extension: '.xlsx')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 86.6 | 7.4 | 6.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.7 | 25.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 39.1 | 29.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.3 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.7 | 3.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 14.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 86.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.7 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 22.5 | 20.6 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 77.3 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 16038 | 1315 | 19 | `crates/nu-protocol/src/value/mod.rs` |
| cleanup | 88 | 38 | 0 | `crates/nu-plugin-core/src/interface/stream/tests.rs` |
| guards | 5032 | 835 | 7 | `crates/nu-parser/src/parser.rs` |
| danger | 3683 | 522 | 4 | `crates/nu-parser/tests/test_parser.rs` |
| concurrency | 923 | 155 | 0 | `crates/nu-protocol/src/process/child.rs` |
| connectivity | 7913 | 1294 | 11 | `crates/nu-protocol/src/value/mod.rs` |
| io | 506 | 156 | 0 | `crates/nu-protocol/src/errors/shell_error/io.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 81 | 37 | 0 | `crates/nu-plugin-core/src/interface/stream/tests.rs` |
| time | 56 | 40 | 0 | `crates/nu-lsp/src/workspace.rs` |
| serialization | 23 | 14 | 0 | `crates/nu_plugin_javascript/nu_plugin_node_example.js` |
| regex | 42 | 21 | 0 | `crates/nu-command/src/strings/detect_type.rs` |
| events | 313 | 74 | 0 | `crates/nu-parser/src/parser.rs` |
| tests | 14875 | 941 | 20 | `crates/nu-parser/tests/test_parser.rs` |
| docs | 12551 | 413 | 11 | `crates/nu-path/src/path.rs` |
| debt | 1226 | 392 | 2 | `crates/nu-parser/tests/test_parser.rs` |
| mutation | 33018 | 1345 | 45 | `crates/nu-parser/src/parser.rs` |
| dead_code | 9328 | 1253 | 11 | `crates/nu-path/src/path.rs` |
| credential | 10 | 8 | 0 | `tests/assets/nu_json/charset_result.json` |
| threat | 74 | 35 | 0 | `crates/nu-path/src/path.rs` |
| ml_ai | 386 | 105 | 0 | `crates/nu-protocol/src/value/mod.rs` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `crates/nu-protocol/src/errors/shell_error/io.rs` (Hits: 44)
- `crates/nu-command/src/strings/guess_width.rs` (Hits: 37)
- `crates/nu-command/src/network/http/interruptible_tcp.rs` (Hits: 15)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **col.rs** (`crates/nu_plugin_polars/src/dataframe/command/data/col.rs`) — 16 inbound connections
2. **lit.rs** (`crates/nu_plugin_polars/src/dataframe/command/data/lit.rs`) — 9 inbound connections
3. **io.rs** (`crates/nu-protocol/src/errors/shell_error/io.rs`) — 7 inbound connections
4. **nu.rs** (`crates/nu-explore/src/explore/commands/nu.rs`) — 6 inbound connections
5. **ast.rs** (`crates/nu-lsp/src/ast.rs`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **repl.rs** (`crates/nu-cli/src/repl.rs`) — 95 outbound dependencies
2. **windows.rs** (`crates/nu-system/src/windows.rs`) — 83 outbound dependencies
3. **lib.rs** (`crates/nu-lsp/src/lib.rs`) — 79 outbound dependencies
4. **parse_keywords.rs** (`crates/nu-parser/src/parse_keywords.rs`) — 79 outbound dependencies
5. **engine_state.rs** (`crates/nu-protocol/src/engine/engine_state.rs`) — 77 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `compile_expression` **(Many-Argument Workhorses)** (@ `crates/nu-engine/src/compile/expression.rs`) -> Impact: **306.4** | LOC: 571
- `eval_instruction` **(Many-Argument Workhorses)** (@ `crates/nu-engine/src/eval_ir.rs`) -> Impact: **301.4** | LOC: 640
  * *Intent:* /// Perform an instruction
- `series_to_values` **(Many-Argument Workhorses)** (@ `crates/nu_plugin_polars/src/dataframe/values/nu_dataframe/conversion.rs`) -> Impact: **251.8** | LOC: 520
- `parse_signature_helper` **(Many-Argument Workhorses)** (@ `crates/nu-parser/src/parser.rs`) -> Impact: **237.2** | LOC: 704
- `rm` **(Many-Argument Workhorses)** (@ `crates/nu-command/src/filesystem/rm.rs`) -> Impact: **215.8** | LOC: 395
- `lex_item` **(Many-Argument Workhorses)** (@ `crates/nu-parser/src/lex.rs`) -> Impact: **200.1** | LOC: 297
- `discover_captures_in_expr` **(Many-Argument Workhorses)** (@ `crates/nu-parser/src/parser.rs`) -> Impact: **198.3** | LOC: 292
  * *Intent:* // Closes over captured variables
- `compile_try` **(Many-Argument Workhorses)** (@ `crates/nu-engine/src/compile/keyword.rs`) -> Impact: **194.5** | LOC: 292
  * *Intent:* /// Compile a call to `try`, setting an error handler over the evaluated block
- `parse_internal_call` **(Many-Argument Workhorses)** (@ `crates/nu-parser/src/parser.rs`) -> Impact: **180.5** | LOC: 377
- `run` **(Many-Argument Workhorses)** (@ `crates/nu-command/src/filters/last.rs`) -> Impact: **174.4** | LOC: 255

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `crates/nu-parser/src` | 12 | 8007.6 | 29.03% | 22.46% |
| `crates/nu-command/src/filters` | 53 | 4637.24 | 11.32% | 55.8% |
| `crates/nu-command/tests/commands` | 121 | 4534.82 | 1.91% | 0.0% |
| `crates/nu-protocol/src/value` | 10 | 3319.94 | 8.19% | 70.52% |
| `crates/nu-protocol/src/engine` | 20 | 2955.38 | 10.63% | 52.3% |
| `crates/nu-command/src/platform/input` | 6 | 2758.42 | 12.74% | 42.11% |
| `crates/nu-engine/src` | 13 | 2671.92 | 9.42% | 26.71% |
| `crates/nu-command/src/filesystem` | 16 | 2580.58 | 14.83% | 40.76% |
| `crates/nu-cli/src` | 13 | 2352.8 | 10.2% | 25.7% |
| `crates/nu-engine/src/compile` | 7 | 2266.28 | 15.33% | 20.95% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `crates/nu-command/src/experimental/is_admin.rs` -> **100.0%** Exposure
- `crates/nu-command/src/experimental/job_describe.rs` -> **100.0%** Exposure
- `crates/nu-command/src/experimental/job_flush.rs` -> **100.0%** Exposure
- `crates/nu-command/src/experimental/job_id.rs` -> **100.0%** Exposure
- `crates/nu-command/src/experimental/job_kill.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `crates/nu-explore/src/explore/views/binary/binary_widget.rs` -> **100.0%** Exposure
- `crates/nu-explore/src/explore/views/colored_text_widget.rs` -> **100.0%** Exposure
- `crates/nu-explore/src/explore/views/cursor/mod.rs` -> **100.0%** Exposure
- `crates/nu-explore/src/explore/views/record/table_widget.rs` -> **100.0%** Exposure
- `crates/nu-explore/src/explore/views/util.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/repl/test_parser.rs` -> **161** Orphaned Functions | **0** Duplicates
- `tests/shell/pipeline/commands/internal.rs` -> **109** Orphaned Functions | **0** Duplicates
- `tests/integration/cli.rs` -> **106** Orphaned Functions | **0** Duplicates
- `crates/nu-parser/tests/test_parser.rs` -> **85** Orphaned Functions | **18** Duplicates
- `tests/overlays/mod.rs` -> **98** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `15991` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `crates/nu-protocol/src/value/record.rs` (RUST) -> Cumulative Risk: **652.4**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.31)
- **Magnitude:** 297.9 | **LOC:** 958 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Api Exposure (100.0%), Spec Match (100.0%), Verification (80.0%)
- **Heaviest Functions:** `visit_map` (Generic / Templated Code, Impact: 9.5), `from_raw_cols_vals` (Generic / Templated Code, Impact: 7.5), `serialize` (Generic / Templated Code, Impact: 7.4)

### 2. `crates/nu-command/src/bytes/remove.rs` (RUST) -> Cumulative Risk: **618.53**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +0.54)
- **Magnitude:** 100.9 | **LOC:** 202 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.5374%), Verification (80.0%)
- **Heaviest Functions:** `remove_impl` (Many-Argument Workhorses, Impact: 26.5), `run` (Many-Argument Workhorses, Impact: 18.8), `remove` (Many-Argument Workhorses, Impact: 4.8)

### 3. `crates/nu-command/src/path/type.rs` (RUST) -> Cumulative Risk: **612.63**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.56)
- **Magnitude:** 79.92 | **LOC:** 151 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.2228%), Tech Debt (88.8959%)
- **Heaviest Functions:** `get_file_type` (Compute Cores, Impact: 21.1), `run` (Many-Argument Workhorses, Impact: 8.4), `run_const` (Many-Argument Workhorses, Impact: 7.7)

### 4. `crates/nu-table/src/util.rs` (RUST) -> Cumulative Risk: **608.68**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.12)
- **Magnitude:** 100.12 | **LOC:** 184 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.6896%), State Flux (99.6093%)
- **Heaviest Functions:** `colorize_space_one` (Generic / Templated Code, Impact: 11.7), `clean_charset` (Compute Cores, Impact: 7.6), `string_wrap` (Compute Cores, Impact: 6.6)

### 5. `crates/nu-command/src/bytes/index_of.rs` (RUST) -> Cumulative Risk: **602.89**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +0.76)
- **Magnitude:** 104.38 | **LOC:** 210 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.1094%), Tech Debt (96.9302%)
- **Heaviest Functions:** `search_all_index` (Many-Argument Workhorses, Impact: 22.0), `run` (Many-Argument Workhorses, Impact: 13.1), `index_of_impl` (Defensive Guards, Impact: 11.2)

### 6. `crates/nu-parser/src/lite_parser.rs` (RUST) -> Cumulative Risk: **600.2**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.29)
- **Magnitude:** 309.02 | **LOC:** 521 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9995%), Documentation (95.4545%), Safety Score (87.4506%)
- **Heaviest Functions:** `lite_parse` (Many-Argument Workhorses, Impact: 68.8), `try_add_redirection` (Many-Argument Workhorses, Impact: 10.8), `last_non_comment_token` (Generic / Templated Code, Impact: 5.8)

### 7. `crates/nu-command/src/help/help_modules.rs` (RUST) -> Cumulative Risk: **598.32**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.51)
- **Magnitude:** 122.16 | **LOC:** 253 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (95.7082%), Verification (80.0%)
- **Heaviest Functions:** `help_modules` (Many-Argument Workhorses, Impact: 58.2), `examples` (State Mutators, Impact: 5.2), `extra_description` (Interface Declarations, Impact: 4.5)

### 8. `crates/nu-command/src/filters/tee.rs` (RUST) -> Cumulative Risk: **597.51**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.46)
- **Magnitude:** 290.5 | **LOC:** 665 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (92.0%), Verification (80.0%), Concurrency (79.4199%)
- **Heaviest Functions:** `run` (Many-Argument Workhorses, Impact: 110.9), `read` (Defensive Guards, Impact: 22.0), `next` (Defensive Guards, Impact: 8.7)

### 9. `crates/nu-protocol/src/engine/jobs.rs` (RUST) -> Cumulative Risk: **593.43**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.73)
- **Magnitude:** 238.64 | **LOC:** 410 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7417%), Documentation (88.8889%), Verification (80.0%)
- **Heaviest Functions:** `recv_timeout` (Defensive Guards, Impact: 17.5), `try_recv` (Defensive Guards, Impact: 14.8), `pop_oldest` (Defensive Guards, Impact: 9.4)

### 10. `crates/nu-command/src/filters/last.rs` (RUST) -> Cumulative Risk: **592.13**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +0.70)
- **Magnitude:** 220.54 | **LOC:** 340 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (86.6046%), Verification (80.0%)
- **Heaviest Functions:** `run` (Many-Argument Workhorses, Impact: 174.4), `signature` (I/O & Config Routines, Impact: 3.9), `examples` (State Mutators, Impact: 2.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/nu-parser/src/parser.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 4073.4 | **LOC:** 7520 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 55.6%
- **Risk Profile:** Cognitive Load (25.0627%), Tech Debt (12.2685%)
**Top Internal Functions/Classes:**
  * `parse_signature_helper` **(Many-Argument Workhorses)** (Impact: 237.2)
  * `discover_captures_in_expr` **(Many-Argument Workhorses)** (Impact: 198.3)
    * *Intent:* // Closes over captured variables
  * `parse_internal_call` **(Many-Argument Workhorses)** (Impact: 180.5)
  * `parse_record` **(Many-Argument Workhorses)** (Impact: 108.2)
  * `parse_string_interpolation` **(Many-Argument Workhorses)** (Impact: 100.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 286 instances
* *State Mutation (weighted view):* 964
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1192`, `structural_boundaries: 1326`, `args: 225`, `func_start: 104`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 6`, `state_mutation: 392`, `dead_code: 6`, `planned_debt: 10`, `fragile_debt: 9`, `unreferenced_by_name: 4`
* *Architecture:* `api: 79`, `import: 7`
* *Defense:* `safety: 170`, `doc: 30`, `test: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` DeclId, DidYouMean, ENV_VARIABLE_ID, FilesizeUnit, Flag, HashSet, IN_VARIABLE_ID, LitePipeline...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-command/src/platform/input/list.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2297.68 | **LOC:** 3702 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (25.5598%), Tech Debt (9.4062%)
**Top Internal Functions/Classes:**
  * `render` **(Many-Argument Workhorses)** (Impact: 164.6)
  * `render_table_cells` **(Many-Argument Workhorses)** (Impact: 159.6)
    * *Intent:* /// Render table cells with proper alignment and optional fuzzy highlighting
  * `run` **(Many-Argument Workhorses)** (Impact: 133.8)
  * `render_truncated_fuzzy_text` **(Many-Argument Workhorses)** (Impact: 87.4)
    * *Intent:* /// Render fuzzy-highlighted text, truncating with ellipsis if needed. /// The ellipsis is highlight...
  * `handle_fuzzy_multi_key` **(Many-Argument Workhorses)** (Impact: 67.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 154 instances
* *State Mutation (weighted view):* 502
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 757`, `structural_boundaries: 556`, `args: 151`, `func_start: 101`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 194`, `unreferenced_by_name: 7`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `safety: 34`, `doc: 98`, `test: 16`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BeginSynchronizedUpdate, Clear, ClearType, EndSynchronizedUpdate, Event, KeyCode, KeyEvent, KeyEventKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-protocol/src/value/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1871.34 | **LOC:** 4827 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.453%), Tech Debt (61.4436%)
**Top Internal Functions/Classes:**
  * `modulo` **(Many-Argument Workhorses)** (Impact: 120.0)
  * `floor_div` **(Many-Argument Workhorses)** (Impact: 111.0)
  * `get_value_member` **(Many-Argument Workhorses)** (Impact: 83.8)
  * `insert_data_at_cell_path` **(Many-Argument Workhorses)** (Impact: 75.4)
  * `div` **(Many-Argument Workhorses)** (Impact: 75.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 556`, `structural_boundaries: 413`, `args: 274`, `func_start: 164`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 2`, `state_mutation: 19`, `dead_code: 9`, `planned_debt: 2`, `unreferenced_by_name: 81`
* *Architecture:* `api: 137`, `import: 32`
* *Defense:* `safety: 115`, `doc: 323`, `test: 79`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Boolean, CellPath, Comparison, Config, ControlFlow, Datelike, Display, Duration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-parser/src/parse_keywords.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1725.74 | **LOC:** 4122 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (12.6337%), Tech Debt (15.8642%)
**Top Internal Functions/Classes:**
  * `parse_alias` **(Many-Argument Workhorses)** (Impact: 100.8)
  * `parse_def_inner` **(Many-Argument Workhorses)** (Impact: 91.3)
    * *Intent:* // Returns also the parsed command name and ID
  * `parse_overlay_use` **(Many-Argument Workhorses)** (Impact: 79.4)
  * `parse_export_in_module` **(Many-Argument Workhorses)** (Impact: 78.4)
    * *Intent:* // This one will trigger only in a module
  * `parse_hide` **(Many-Argument Workhorses)** (Impact: 75.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 556`, `structural_boundaries: 805`, `args: 97`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 91`, `dead_code: 8`, `planned_debt: 5`, `fragile_debt: 5`, `unreferenced_by_name: 9`
* *Architecture:* `api: 34`, `import: 8`
* *Defense:* `safety: 144`, `doc: 23`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AttributeBlock, Block, BlockId, Call, CallKind, CommandWideCompleter, CustomExample, DeclId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-engine/src/eval_ir.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 973.92 | **LOC:** 1838 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (18.2497%), Tech Debt (13.201%)
**Top Internal Functions/Classes:**
  * `eval_instruction` **(Many-Argument Workhorses)** (Impact: 301.4)
    * *Intent:* /// Perform an instruction
  * `binary_op` **(Many-Argument Workhorses)** (Impact: 107.0)
  * `gather_arguments` **(Many-Argument Workhorses)** (Impact: 71.5)
    * *Intent:* /// Move arguments from the stack into variables for a custom command
  * `literal_value` **(Many-Argument Workhorses)** (Impact: 40.0)
  * `eval_ir_block_impl` **(Many-Argument Workhorses)** (Impact: 30.6)
    * *Intent:* /// Eval an IR block on the provided slice of registers.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 283`, `structural_boundaries: 327`, `args: 76`, `func_start: 32`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 62`, `planned_debt: 2`, `fragile_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 8`
* *Defense:* `safety: 55`, `doc: 45`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Block, Boolean, CellPath, Closure, Comparison, DataSlice, ENV_VARIABLE_ID, EngineState...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-engine/src/compile/keyword.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 870.06 | **LOC:** 1131 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.5414%), Tech Debt (8.055%)
**Top Internal Functions/Classes:**
  * `compile_try` **(Many-Argument Workhorses)** (Impact: 194.5)
    * *Intent:* /// Compile a call to `try`, setting an error handler over the evaluated block
  * `compile_match` **(Many-Argument Workhorses)** (Impact: 97.5)
    * *Intent:* /// Compile a call to `match`
  * `compile_if` **(Many-Argument Workhorses)** (Impact: 77.8)
    * *Intent:* /// Compile a call to `if` as a branch-if
  * `compile_for` **(Many-Argument Workhorses)** (Impact: 74.1)
    * *Intent:* /// Compile a call to `for` (via `iterate`)
  * `compile_while` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* /// Compile a call to `while`, via branch instructions
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 125`, `args: 29`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 44`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 45`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Call, CompileError, Expr, Expression, RedirectModes, RegId, Span, Type...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-cli/src/reedline_config.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 781.6 | **LOC:** 1777 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (20.3696%), Tech Debt (23.9896%)
**Top Internal Functions/Classes:**
  * `edit_from_record` **(Many-Argument Workhorses)** (Impact: 133.5)
  * `add_ide_menu` **(Many-Argument Workhorses)** (Impact: 123.7)
    * *Intent:* // Adds an IDE menu to the line editor
  * `add_description_menu` **(Many-Argument Workhorses)** (Impact: 40.9)
    * *Intent:* // Adds a description menu to the line editor
  * `add_parsed_keybinding` **(Many-Argument Workhorses)** (Impact: 39.7)
  * `add_columnar_menu` **(Many-Argument Workhorses)** (Impact: 38.3)
    * *Intent:* // Adds a columnar menu to the editor engine
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 224`, `structural_boundaries: 282`, `args: 62`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 43`, `fragile_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 9`, `concurrency: 5`, `import: 15`
* *Defense:* `safety: 46`, `test: 23`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DescriptionMenu, DescriptionMode, EditBindings, EditCommand, EditCommandDiscriminants, FromValue, IdeMenu, KeyModifiers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-table/src/table.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 740.64 | **LOC:** 1384 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.6384%), Tech Debt (18.7823%)
**Top Internal Functions/Classes:**
  * `truncate_columns_by_content` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* // VERSION where we are showing AS LITTLE COLUMNS AS POSSIBLE but WITH AS MUCH CONTENT AS POSSIBLE.
  * `truncate_columns_by_head` **(Many-Argument Workhorses)** (Impact: 44.9)
    * *Intent:* // VERSION where we are showing AS MANY COLUMNS AS POSSIBLE solely based on first column.
  * `truncate_columns_by_columns` **(Many-Argument Workhorses)** (Impact: 36.3)
    * *Intent:* // VERSION where we are showing AS MANY COLUMNS AS POSSIBLE but as a side affect they MIGHT CONTAIN ...
  * `width_ctrl_truncate` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `load_theme` **(Many-Argument Workhorses)** (Impact: 17.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 57 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 225
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 326`, `args: 71`, `func_start: 68`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 111`, `dead_code: 4`, `planned_debt: 13`, `fragile_debt: 3`
* *Architecture:* `api: 31`, `import: 6`
* *Defense:* `safety: 12`, `doc: 11`, `test: 1`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CellOption, Color, ColoredConfig, Entity, Indent, Padding, PeekableGridDimension, PeekableRecords...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-command/src/filesystem/ls.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 694.68 | **LOC:** 1170 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (31.6778%), Tech Debt (16.6863%)
**Top Internal Functions/Classes:**
  * `ls_for_one_pattern` **(Many-Argument Workhorses)** (Impact: 162.2)
  * `dir_entry_dict` **(Many-Argument Workhorses)** (Impact: 158.0)
  * `run` **(Many-Argument Workhorses)** (Impact: 45.6)
  * `get_file_type` **(Many-Argument Workhorses)** (Impact: 39.9)
  * `dir_entry_dict_windows_fallback` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* /// A secondary way to get file info on Windows, for when std::fs::symlink_metadata() fails. /// dir...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 207`, `args: 57`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 45`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 5`
* *Architecture:* `io: 7`, `api: 4`, `concurrency: 5`, `import: 23`
* *Defense:* `safety: 33`, `doc: 16`, `test: 6`, `sync_locks: 4`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DirInfo, FILE_ATTRIBUTE_READONLY, FILE_ATTRIBUTE_REPARSE_POINT, FindClose, FindFirstFileW, IO_REPARSE_TAG_SYMLINK, Local, LocalResult...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-explore/src/explore/pager/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 687.72 | **LOC:** 1135 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.9963%), Tech Debt (11.5663%)
**Top Internal Functions/Classes:**
  * `render_ui` **(Many-Argument Workhorses)** (Impact: 64.8)
  * `search_input_key_event` **(Many-Argument Workhorses)** (Impact: 34.2)
  * `handle_general_key_events2` **(Many-Argument Workhorses)** (Impact: 32.9)
  * `render_cmd_bar_cmd` **(Many-Argument Workhorses)** (Impact: 30.1)
  * `cmd_input_key_event` **(Many-Argument Workhorses)** (Impact: 28.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 65 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 261`, `args: 48`, `func_start: 36`, `class_start: 11`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 83`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 31`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 25`, `doc: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ClearType, CommandRegistry, EnterAlternateScreen, KeyEvent, KeyModifiers, LeaveAlternateScreen, NuConfig, NuStyle...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-parser/tests/test_parser.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 687.66 | **LOC:** 3252 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (3.2167%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_int` **(Many-Argument Workhorses)** (Impact: 13.2)
  * `multi_test_parse_int` **(I/O & Config Routines)** (Impact: 13.0)
  * `parse_variable_range` **(Many-Argument Workhorses)** (Impact: 12.9)
  * `parse_bounded_range` **(Many-Argument Workhorses)** (Impact: 12.7)
  * `parse_cell_path_optional` **(Tests & Verification)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 10 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 83
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 716`, `args: 183`, `func_start: 155`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 93`, `state_mutation: 2`, `dead_code: 4`, `planned_debt: 14`, `duplicate_logic: 18`, `unreferenced_by_name: 85`
* *Architecture:* `api: 67`, `import: 18`
* *Defense:* `safety: 24`, `doc: 4`, `test: 380`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AttrEcho, Const, Def, EngineState, Expr, Expression, ExternalArgument, FilesizeUnit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu_plugin_polars/src/dataframe/values/nu_dataframe/conversion.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 678.58 | **LOC:** 1957 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (13.7458%), Tech Debt (17.9104%)
**Top Internal Functions/Classes:**
  * `series_to_values` **(Many-Argument Workhorses)** (Impact: 251.8)
  * `typed_column_to_series` **(Many-Argument Workhorses)** (Impact: 88.5)
  * `input_type_list_to_series` **(Many-Argument Workhorses)** (Impact: 41.9)
  * `test_any_value_to_value` **(Tests & Verification)** (Impact: 30.9)
  * `insert_value` **(Many-Argument Workhorses)** (Impact: 24.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 316`, `args: 174`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 15`, `dead_code: 1`, `unreferenced_by_name: 17`
* *Architecture:* `api: 13`, `import: 25`
* *Defense:* `safety: 59`, `test: 53`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ChunkAnyValue, Column, DataFrame, DataType, DatetimeChunked, DerefMut, Duration, FixedOffset...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-protocol/src/engine/state_working_set.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 672.2 | **LOC:** 1241 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.0642%), Tech Debt (99.1233%)
**Top Internal Functions/Classes:**
  * `read_span` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `find_decl_name` **(Compute Cores)** (Impact: 22.8)
    * *Intent:* /// Find the name of the declaration corresponding to `decl_id`. /// /// Extends [`EngineState::find...
  * `find_decl` **(Compute Cores)** (Impact: 20.8)
    * *Intent:* /// Find the [`DeclId`](crate::DeclId) corresponding to a declaration with `name`. /// /// Extends [...
  * `hide_decl` **(Compute Cores)** (Impact: 16.1)
  * `add_overlay` **(Many-Argument Workhorses)** (Impact: 14.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 240`, `args: 108`, `func_start: 85`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 4`, `state_mutation: 42`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 46`
* *Architecture:* `api: 91`, `import: 5`
* *Defense:* `safety: 28`, `doc: 62`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Category, Command, CommandType, CompileError, Config, DeclId, EngineState, FileId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-protocol/src/engine/engine_state.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 657.3 | **LOC:** 1444 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.5446%), Tech Debt (99.5561%)
**Top Internal Functions/Classes:**
  * `merge_delta` **(Many-Argument Workhorses)** (Impact: 43.2)
    * *Intent:* /// Merges a `StateDelta` onto the current state. These deltas come from a system, like the parser, ...
  * `cwd` **(Defensive Guards)** (Impact: 28.0)
    * *Intent:* /// Returns the current working directory, which is guaranteed to be an /// absolute path without tr...
  * `update_plugin_file` **(Compute Cores)** (Impact: 17.8)
  * `merge_env` **(Defensive Guards)** (Impact: 15.3)
    * *Intent:* /// Merge the environment from the runtime Stack into the engine state
  * `find_decl_name` **(Compute Cores)** (Impact: 10.8)
    * *Intent:* /// Find the name of the declaration corresponding to `decl_id`. /// /// Searches within active over...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 240`, `args: 141`, `func_start: 110`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 57`, `state_mutation: 53`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 57`
* *Architecture:* `io: 6`, `api: 117`, `concurrency: 2`, `import: 16`
* *Defense:* `safety: 20`, `doc: 95`, `test: 33`, `sync_locks: 20`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AtomicU32, Command, Config, DEFAULT_OVERLAY_NAME, DeclId, EnvName, EnvVars, FileId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-command/src/database/values/sqlite.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 649.1 | **LOC:** 1591 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (6.9087%), Tech Debt (96.6498%)
**Top Internal Functions/Classes:**
  * `prepared_statement_to_nu_list` **(Many-Argument Workhorses)** (Impact: 25.5)
  * `split_select_expressions` **(Compute Cores)** (Impact: 19.2)
    * *Intent:* /// Splits a SELECT projection list on top-level commas. /// /// We only split commas that are outsi...
  * `nu_value_to_params` **(Many-Argument Workhorses)** (Impact: 16.1)
  * `read_entire_sqlite_db` **(Many-Argument Workhorses)** (Impact: 15.3)
  * `convert_sqlite_value_to_nu_value_with_adapter` **(Defensive Guards)** (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Cascading Flux:* 23 instances
* *Api Near Db Sink:* 1 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 239`, `args: 131`, `func_start: 92`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 46`, `high_risk_execution: 8`, `state_mutation: 30`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 8`, `unreferenced_by_name: 29`
* *Architecture:* `io: 1`, `api: 56`, `concurrency: 1`, `import: 12`
* *Defense:* `safety: 21`, `doc: 60`, `test: 46`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Error, IntoPipelineData, OpenFlags, PathBuf, PipelineData, Record, Row, Serialize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-plugin-engine/src/interface/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 611.74 | **LOC:** 1482 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (7.1319%), Tech Debt (43.2968%)
**Top Internal Functions/Classes:**
  * `handle_engine_call` **(Many-Argument Workhorses)** (Impact: 40.7)
    * *Intent:* /// Handle an engine call.
  * `consume` **(Many-Argument Workhorses)** (Impact: 40.5)
  * `receive_plugin_call_response` **(Many-Argument Workhorses)** (Impact: 39.5)
    * *Intent:* /// Read the channel for plugin call messages and handle them until the response is received.
  * `write_plugin_call` **(Many-Argument Workhorses)** (Impact: 27.4)
    * *Intent:* /// Write a plugin call message. Returns the writer for the stream.
  * `spawn_engine_call_handler` **(Defensive Guards)** (Impact: 24.6)
    * *Intent:* /// Spawn a handler for engine calls for a plugin, in case we need to handle engine calls /// after ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 14 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 206`, `args: 96`, `func_start: 54`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 15`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 16`
* *Architecture:* `api: 26`, `concurrency: 21`, `import: 6`
* *Defense:* `safety: 46`, `doc: 110`, `test: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CustomValueOp, DynamicSuggestion, EngineCall, EngineCallId, EngineCallResponse, EvaluatedCall, GetCompletionInfo, InterfaceManager...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-cli/src/repl.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 590.22 | **LOC:** 1773 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (8.3487%), Tech Debt (20.0404%)
**Top Internal Functions/Classes:**
  * `loop_iteration` **(Compute Cores)** (Impact: 77.2)
    * *Intent:* /// Perform one iteration of the REPL loop /// Result is bool: continue loop, current reedline
  * `evaluate_repl` **(Many-Argument Workhorses)** (Impact: 55.5)
    * *Intent:* /// The main REPL loop, including spinning up the prompt itself.
  * `do_auto_cd` **(Many-Argument Workhorses)** (Impact: 28.3)
    * *Intent:* /// /// Execute an "auto-cd" operation, changing the current working directory. ///
  * `do_run_cmd` **(Many-Argument Workhorses)** (Impact: 25.5)
    * *Intent:* /// /// Run a command as received from reedline. This is where we are actually /// running a thing! ...
  * `get_command_finished_marker` **(Many-Argument Workhorses)** (Impact: 22.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 29 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 332`, `args: 72`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 49`, `high_risk_execution: 2`, `state_mutation: 56`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 1`, `unreferenced_by_name: 7`
* *Architecture:* `io: 14`, `api: 1`, `import: 30`
* *Defense:* `safety: 43`, `doc: 51`, `test: 40`, `sync_locks: 7`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CwdAwareHinter, DefaultCompleter, EditCommand, Emacs, FileBackedHistory, HistoryConfig, HistoryFileFormat, HistorySessionId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-glob/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 581.64 | **LOC:** 1622 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.3697%), Tech Debt (98.3978%)
**Top Internal Functions/Classes:**
  * `fill_todo` **(Many-Argument Workhorses)** (Impact: 66.7)
    * *Intent:* // Fills `todo` with paths under `path` to be matched by `patterns[idx]`, // special-casing patterns...
  * `matches_from` **(Many-Argument Workhorses)** (Impact: 65.4)
  * `next` **(Compute Cores)** (Impact: 53.4)
  * `new` **(Compute Cores)** (Impact: 42.7)
    * *Intent:* /// This function compiles Unix shell style patterns. /// /// An invalid glob pattern will yield a `...
  * `glob_with` **(Many-Argument Workhorses)** (Impact: 33.0)
    * *Intent:* /// Return an iterator that produces all the `Path`s that match the given /// pattern using the spec...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 179`, `args: 86`, `func_start: 59`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 80`, `high_risk_execution: 2`, `state_mutation: 37`, `dead_code: 18`, `planned_debt: 22`, `fragile_debt: 9`, `unreferenced_by_name: 25`
* *Architecture:* `io: 4`, `api: 29`, `import: 18`
* *Defense:* `safety: 12`, `doc: 234`, `test: 152`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AnyRecursiveSequence, AnySequence, AnyWithin, Char, CharSpecifier::CharRange, Component, Match, MatchOptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-parser/src/lex.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 560.98 | **LOC:** 700 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.9882%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `lex_item` **(Many-Argument Workhorses)** (Impact: 200.1)
  * `lex_internal` **(Many-Argument Workhorses)** (Impact: 113.7)
  * `lex_raw_string` **(Many-Argument Workhorses)** (Impact: 21.0)
  * `is_item_terminator` **(Many-Argument Workhorses)** (Impact: 20.9)
    * *Intent:* // A baseline token is terminated if it's not nested inside of a paired // delimiter and the next ch...
  * `lex_n_tokens` **(Many-Argument Workhorses)** (Impact: 6.2)
    * *Intent:* /// Lex until the output is `max_tokens` longer than before the call, or until the input is exhauste...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 97`, `args: 28`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `state_mutation: 54`
* *Architecture:* `api: 16`, `import: 1`
* *Defense:* `safety: 17`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.614
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002807
  * `Imports (Out-Degree: 0):` Span, nu_protocol::ParseError
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `crates/nu-command/src/network/http/client.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 557.08 | **LOC:** 1313 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (12.9258%), Tech Debt (40.9806%)
**Top Internal Functions/Classes:**
  * `transform_response_using_content_type` **(Many-Argument Workhorses)** (Impact: 31.0)
  * `send_form_request` **(Many-Argument Workhorses)** (Impact: 29.5)
  * `send_request` **(Many-Argument Workhorses)** (Impact: 29.0)
    * *Intent:* // remove once all commands have been migrated
  * `request_add_custom_headers` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `send_json_request` **(Many-Argument Workhorses)** (Impact: 24.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 226`, `args: 96`, `func_start: 39`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 3`, `state_mutation: 25`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 15`
* *Architecture:* `io: 2`, `api: 35`, `concurrency: 10`, `import: 19`
* *Defense:* `safety: 31`, `doc: 4`, `test: 12`, `sync_locks: 6`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Body, Connector, Cursor, DnsErrorKind, Error, LabeledError, LookupError, NetworkError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/command.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 555.2 | **LOC:** 1567 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (22.273%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_cli_args` **(Compute Cores)** (Impact: 89.3)
    * *Intent:* // Parse CLI args into nushell options and script details.
  * `prevalidate_short_groups_before_lexopt` **(Compute Cores)** (Impact: 63.8)
    * *Intent:* // Validate combined short flags and reject unsupported inline values.
  * `parse_experimental_options` **(Compute Cores)** (Impact: 30.8)
    * *Intent:* // Parse experimental options, allowing bracketed and comma-delimited forms.
  * `parse_log_filters` **(Defensive Guards)** (Impact: 28.5)
    * *Intent:* // Parse log filters and ensure they match known log levels. // Supports multiple formats: [error,wa...
  * `parse_validated_option` **(Many-Argument Workhorses)** (Impact: 14.8)
    * *Intent:* // Parse and validate a string value against a list of allowed values. // Returns the normalized (tr...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 43 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 217`, `args: 93`, `func_start: 35`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 2`, `state_mutation: 48`
* *Architecture:* `api: 47`, `import: 15`
* *Defense:* `safety: 22`, `test: 24`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ShellError, Span, Spanned, Value, Write, config::TableMode, crate::test_bins, did_you_mean...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-command/src/viewers/table.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 552.34 | **LOC:** 1369 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (14.4331%), Tech Debt (9.5961%)
**Top Internal Functions/Classes:**
  * `handle_row_stream` **(Many-Argument Workhorses)** (Impact: 45.9)
  * `handle_record` **(Many-Argument Workhorses)** (Impact: 30.4)
  * `get_cli_args` **(Many-Argument Workhorses)** (Impact: 27.6)
  * `stream_collect_abbreviated` **(Many-Argument Workhorses)** (Impact: 26.7)
  * `render_path_name` **(Many-Argument Workhorses)** (Impact: 25.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 232`, `args: 57`, `func_start: 41`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 45`, `dead_code: 5`, `planned_debt: 6`
* *Architecture:* `io: 1`, `api: 7`, `import: 13`
* *Defense:* `safety: 33`, `test: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Config, DataSource, ExpandedTable, HexStyles, JustTable, ListStream, NuTable, PipelineMetadata...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-command/src/formats/to/md.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 517.2 | **LOC:** 1548 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (18.7375%), Tech Debt (31.7096%)
**Top Internal Functions/Classes:**
  * `get_output_string` **(Many-Argument Workhorses)** (Impact: 79.0)
  * `table` **(Many-Argument Workhorses)** (Impact: 57.6)
  * `run` **(Many-Argument Workhorses)** (Impact: 34.0)
  * `group_by` **(Defensive Guards)** (Impact: 23.6)
  * `to_md` **(Many-Argument Workhorses)** (Impact: 22.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 147`, `args: 138`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 47`, `unreferenced_by_name: 24`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 11`, `doc: 8`, `test: 51`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IntoPipelineData, Metadata, Value, ast::PathMember, casing::Casing, crate::Get, indexmap::IndexMap, nu_cmd_base::formats::to::delimited::merge_descriptors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-command/src/strings/detect_columns.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 514.1 | **LOC:** 1069 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (11.8691%), Tech Debt (29.192%)
**Top Internal Functions/Classes:**
  * `process_with_box_filter` **(Many-Argument Workhorses)** (Impact: 62.9)
    * *Intent:* /// Process input when ignore_box_chars is enabled. /// Handles both position-based and whitespace-b...
  * `baseline` **(Compute Cores)** (Impact: 55.8)
    * *Intent:* /// Tokenizes a single "baseline" token from the input stream. /// A baseline token is a sequence of...
  * `guess_width` **(Many-Argument Workhorses)** (Impact: 33.0)
  * `process_standard` **(Many-Argument Workhorses)** (Impact: 33.0)
    * *Intent:* /// Process input with standard whitespace-based column detection.
  * `run` **(Many-Argument Workhorses)** (Impact: 21.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 170`, `args: 61`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `state_mutation: 39`, `dead_code: 4`, `planned_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `safety: 24`, `doc: 55`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Range, iter::Peekable, itertools::Itertools, nu_engine::command_prelude::*, nu_protocol::Config, std::io::Cursor, str::CharIndices, super::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/nu-protocol/src/pipeline/byte_stream.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 510.92 | **LOC:** 1301 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.753%), Tech Debt (96.7291%)
**Top Internal Functions/Classes:**
  * `generic_copy` **(Many-Argument Workhorses)** (Impact: 21.4)
    * *Intent:* // Copied from [`std::io::copy`]
  * `next` **(Compute Cores)** (Impact: 20.9)
  * `copy_with_signals` **(Many-Argument Workhorses)** (Impact: 19.8)
  * `slice` **(Many-Argument Workhorses)** (Impact: 19.7)
  * `next_string` **(Compute Cores)** (Impact: 17.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 230`, `args: 96`, `func_start: 77`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 23`, `dead_code: 5`, `planned_debt: 2`, `duplicate_logic: 5`, `unreferenced_by_name: 25`
* *Architecture:* `io: 3`, `api: 56`, `concurrency: 12`, `import: 9`
* *Defense:* `safety: 8`, `doc: 178`, `test: 17`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BufRead, BufReader, ChildProcess, Cursor, ErrorKind, PipelineData, Read, Serialize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/nu-protocol/src/pipeline/pipeline_data.rs` -> Churn: **90.31%** | Cog Load: 4.5536% | Debt: 65.5696%
- `crates/nu-protocol/src/errors/shell_error/mod.rs` -> Churn: **84.76%** | Cog Load: 3.5483% | Debt: 78.8301%
- `crates/nu-command/src/filters/sort.rs` -> Churn: **77.82%** | Cog Load: 7.9379% | Debt: 59.4986%
- `crates/nu-cli/src/commands/history/history_import.rs` -> Churn: **69.9%** | Cog Load: 14.0759% | Debt: 90.0226%
- `crates/nu-command/src/filters/default.rs` -> Churn: **69.9%** | Cog Load: 8.7757% | Debt: 79.635%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/nu-protocol/src/value/mod.rs` -> **Piepmatz** (100.0% isolated ownership) | Magnitude: 1871.34
- `crates/nu-engine/src/compile/keyword.rs` -> **Wind** (100.0% isolated ownership) | Magnitude: 870.06
- `crates/nu-cli/src/reedline_config.rs` -> **Juhan** (100.0% isolated ownership) | Magnitude: 781.6
- `crates/nu-table/src/table.rs` -> **Maxim Zhiburt** (100.0% isolated ownership) | Magnitude: 740.64
- `crates/nu-protocol/src/engine/state_working_set.rs` -> **Daniil Sivak** (100.0% isolated ownership) | Magnitude: 672.2

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/nu_plugin_polars/src/dataframe/command/data/col.rs` -> **Severity: 0.526** (Embedded: 0.009 * Error Risk: 58.494%)
- `crates/nu-parser/src/lex.rs` -> **Severity: 0.216** (Embedded: 0.0028 * Error Risk: 76.7793%)
- `crates/nu-explore/src/explore/commands/nu.rs` -> **Severity: 0.213** (Embedded: 0.0034 * Error Risk: 63.3642%)
- `crates/nu-lsp/src/ast.rs` -> **Severity: 0.16** (Embedded: 0.0034 * Error Risk: 47.5795%)
- `crates/nu-protocol/src/errors/shell_error/io.rs` -> **Severity: 0.156** (Embedded: 0.004 * Error Risk: 39.1403%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/nu_plugin_polars/src/dataframe/command/data/col.rs` -> **Severity: 745.0** (Blast Radius: 7.45 * Doc Risk: 100.0%)
- `crates/nu_plugin_polars/src/dataframe/command/data/lit.rs` -> **Severity: 422.6** (Blast Radius: 4.226 * Doc Risk: 100.0%)
- `crates/nu-explore/src/explore/commands/nu.rs` -> **Severity: 287.013** (Blast Radius: 3.305 * Doc Risk: 86.8421%)
- `crates/nu-protocol/src/did_you_mean.rs` -> **Severity: 284.4** (Blast Radius: 2.844 * Doc Risk: 100.0%)
- `crates/nu-protocol/src/errors/shell_error/io.rs` -> **Severity: 189.539** (Blast Radius: 3.696 * Doc Risk: 51.2821%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
