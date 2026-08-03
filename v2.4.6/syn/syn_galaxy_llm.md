# ARCHITECTURAL_BRIEF: syn
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/syn` |
| **Timestamp** | `2026-08-03T19:47:29.607453+00:00` |
| **Scan Duration** | `0.67s` |
| **Git Branch** | `master` |
| **Git Commit** | `ae257c4e05a338f73655aa1fa3d144e047daccf1` |
| **Git Remote** | `https://github.com/dtolnay/syn.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 123 malicious artifacts.

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
| Total Artifacts | 165 |
| Analyzed Artifacts (Scanned) | 132 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 33 |
| Total LOC | 24780 |
| Volatility Index | 0.008 |
| % Scanned of codebase = | 80.0% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5176 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.2257 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0727 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 122 | 24143 | 92.4% |
| MARKDOWN | 6 | 0 | 4.5% |
| PLAINTEXT | 2 | 0 | 1.5% |
| SHELL | 1 | 10 | 0.8% |
| CSS | 1 | 627 | 0.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.206`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 50 | 37.9% |
| file_cluster_13 | 33 | 25.0% |
| file_cluster_0 | 30 | 22.7% |
| file_cluster_16 | 9 | 6.8% |
| file_cluster_17 | 1 | 0.8% |
| file_cluster_4 | 1 | 0.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 6.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 33*

**Composition by Extension & Reason:**
- `.toml`: 14x Unsupported Format (.toml)
- `.rs`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2268 LOC), 1x Excluded (Machine-Generated Source Code Signature: 3239 LOC)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 73 LOC)
- `.json`: 1x Excluded (Massive Static Asset Blob: 5687 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 71.1 | 12.7 | 8.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 97.8 | 30.9 | 30.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 26.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 28.4 | 2.3 | 0.0 |
| API Exposure | 0.0 | 8.1 | 2.6 | 2.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 6.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 33.8 | 6.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.9 | 13.4 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 94.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 8.1 | 1.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 10.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 39.8 | 16.4 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 54.5 | 89.4 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 7.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `dev/import.sh` (Hits: 7)
- `codegen/src/file.rs` (Hits: 2)
- `examples/dump-syntax/src/main.rs` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **full.rs** (`codegen/src/full.rs`) — 7 inbound connections
2. **lookup.rs** (`codegen/src/lookup.rs`) — 5 inbound connections
3. **parse_quote.rs** (`src/parse_quote.rs`) — 5 inbound connections
4. **gen.rs** (`codegen/src/gen.rs`) — 3 inbound connections
5. **workspace_path.rs** (`codegen/src/workspace_path.rs`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`src/lib.rs`) — 222 outbound dependencies
2. **eq.rs** (`tests/common/eq.rs`) — 208 outbound dependencies
3. **expr.rs** (`src/expr.rs`) — 111 outbound dependencies
4. **item.rs** (`src/item.rs`) — 99 outbound dependencies
5. **test_expr.rs** (`tests/test_expr.rs`) — 76 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `scan_right` (@ `src/fixup.rs`) -> Impact: **1514.2** | LOC: 282
- `expand_impl_body` (@ `codegen/src/snapshot.rs`) -> Impact: **791.1** | LOC: 170
- `parse` (@ `src/op.rs`) -> Impact: **593.0** | LOC: 61
- `skip` (@ `src/whitespace.rs`) -> Impact: **488.2** | LOC: 60
- `parse` (@ `src/generics.rs`) -> Impact: **479.2** | LOC: 65
- `parse` (@ `src/path.rs`) -> Impact: **452.4** | LOC: 89
- `parse_stmt` (@ `src/stmt.rs`) -> Impact: **361.0** | LOC: 67
  * *Intent:* /// /// ``` /// use syn::{braced, token, Attribute, Block, Ident, Result, Stmt, Token}; /// use syn::parse::{Parse, ParseStream}; /// /// // Parse a f...
- `node` (@ `codegen/src/fold.rs`) -> Impact: **352.0** | LOC: 152
- `node` (@ `codegen/src/visit_mut.rs`) -> Impact: **350.5** | LOC: 122
- `node` (@ `codegen/src/visit.rs`) -> Impact: **350.1** | LOC: 114

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `node` (@ `codegen/src/fold.rs`) -> **O(2^N) [Recursive]**
- `introspect_type` (@ `codegen/src/parse.rs`) -> **O(2^N) [Recursive]**
- `expand_impl_body` (@ `codegen/src/snapshot.rs`) -> **O(2^N) [Recursive]**
- `format_field` (@ `codegen/src/snapshot.rs`) -> **O(2^N) [Recursive]**
- `node` (@ `codegen/src/visit.rs`) -> **O(2^N) [Recursive]**
- `node` (@ `codegen/src/visit_mut.rs`) -> **O(2^N) [Recursive]**
- `recursive_new` (@ `src/buffer.rs`) -> **O(2^N) [Recursive]**
- `parse` (@ `src/custom_keyword.rs`) -> **O(2^N) [Recursive]**
- `parse` (@ `src/data.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* #[cfg(all(feature = "parsing", feature = "printing"))]
- `parse` (@ `src/derive.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `test_permutations` (@ `tests/test_expr.rs`) -> DB Complexity: **38**
- `node` (@ `codegen/src/visit_mut.rs`) -> DB Complexity: **14**
- `node` (@ `codegen/src/fold.rs`) -> DB Complexity: **13**
- `librustc_parenthesize` (@ `tests/test_precedence.rs`) -> DB Complexity: **11**
- `node` (@ `codegen/src/visit.rs`) -> DB Complexity: **8**
- `traverse` (@ `codegen/src/gen.rs`) -> DB Complexity: **7**
- `stmt_expr` (@ `src/stmt.rs`) -> DB Complexity: **7**
- `visit_expr_mut` (@ `tests/common/visit.rs`) -> DB Complexity: **7**
- `test_mut_self` (@ `tests/test_ty.rs`) -> DB Complexity: **7**
- `parse_bare_fn_arg` (@ `src/ty.rs`) -> DB Complexity: **6**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 48 | 21970.94 | 14.53% | 57.05% |
| `codegen/src` | 20 | 5414.37 | 19.67% | 13.27% |
| `tests` | 28 | 2903.36 | 6.41% | 0.0% |
| `tests/common` | 4 | 833.9 | 24.13% | 0.0% |
| `tests/repo` | 2 | 624.64 | 32.65% | 0.0% |
| `examples/trace-var/trace-var/src` | 1 | 223.58 | 8.48% | 0.0% |
| `examples/lazy-static/lazy-static/src` | 1 | 119.08 | 11.55% | 0.0% |
| `benches` | 2 | 110.52 | 13.02% | 49.3% |
| `examples/dump-syntax/src` | 1 | 74.0 | 6.98% | 0.0% |
| `examples/heapsize/heapsize_derive/src` | 1 | 57.88 | 22.27% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/attr.rs` -> **100.0%** Exposure
- `src/error.rs` -> **100.0%** Exposure
- `src/item.rs` -> **100.0%** Exposure
- `src/parse_quote.rs` -> **100.0%** Exposure
- `src/span.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `codegen/src/gen.rs` -> **100.0%** Exposure
- `src/bigint.rs` -> **100.0%** Exposure
- `tests/common/visit.rs` -> **100.0%** Exposure
- `dev/import.sh` -> **99.995%** Exposure
- `src/verbatim.rs` -> **99.9254%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/punctuated.rs` -> **0** Orphaned Functions | **51** Duplicates
- `src/item.rs` -> **0** Orphaned Functions | **39** Duplicates
- `src/ty.rs` -> **0** Orphaned Functions | **39** Duplicates
- `src/generics.rs` -> **0** Orphaned Functions | **38** Duplicates
- `src/token.rs` -> **0** Orphaned Functions | **31** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/op.rs`** -> AI Confidence: **99.48%**
2. **`codegen/src/eq.rs`** -> AI Confidence: **99.31%**
3. **`codegen/src/parse.rs`** -> AI Confidence: **99.31%**
4. **`src/classify.rs`** -> AI Confidence: **99.31%**
5. **`src/custom_punctuation.rs`** -> AI Confidence: **99.31%**
6. **`src/expr.rs`** -> AI Confidence: **99.31%**
7. **`src/fixup.rs`** -> AI Confidence: **99.31%**
8. **`src/generics.rs`** -> AI Confidence: **99.31%**
9. **`src/meta.rs`** -> AI Confidence: **99.31%**
10. **`src/pat.rs`** -> AI Confidence: **99.31%**
11. **`src/path.rs`** -> AI Confidence: **99.31%**
12. **`src/scan_expr.rs`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `codegen/src/debug.rs` -> **20.0%** Exposure
- `codegen/src/fold.rs` -> **20.0%** Exposure
- `codegen/src/gen.rs` -> **20.0%** Exposure
- `codegen/src/hash.rs` -> **20.0%** Exposure
- `codegen/src/parse.rs` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `src/verbatim.rs` -> **99.9999%** Exposure
- `src/parse.rs` -> **0.7017%** Exposure
### Algorithmic DoS Exposure
- `benches/rust.rs` -> **100.0%** Exposure
- `codegen/src/clone.rs` -> **100.0%** Exposure
- `codegen/src/css.rs` -> **100.0%** Exposure
- `codegen/src/debug.rs` -> **100.0%** Exposure
- `codegen/src/eq.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2419` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/stmt.rs` (RUST) -> Cumulative Risk: **776.87**
- **Archetype:** `file_cluster_13` (Distance: 16.399 IQR)
- **Magnitude:** 817.46 | **LOC:** 489 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.0843%), State Flux (85.692%)
- **Heaviest Functions:** `parse_stmt` (Impact: 361.0), `stmt_expr` (Impact: 97.8), `stmt_local` (Impact: 96.0)

### 2. `src/verbatim.rs` (RUST) -> Cumulative Risk: **712.39**
- **Archetype:** `file_cluster_13` (Distance: 11.572 IQR)
- **Magnitude:** 34.9 | **LOC:** 34 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Injection Surface (99.9999%), State Flux (99.9254%)
- **Heaviest Functions:** `between` (Impact: 27.4)

### 3. `src/punctuated.rs` (RUST) -> Cumulative Risk: **698.82**
- **Archetype:** `file_cluster_16` (Distance: 14.111 IQR)
- **Magnitude:** 1106.14 | **LOC:** 1171 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9996%)
- **Heaviest Functions:** `fold` (Impact: 61.5), `get` (Impact: 35.1), `get_mut` (Impact: 35.1)

### 4. `src/ident.rs` (RUST) -> Cumulative Risk: **697.09**
- **Archetype:** `file_cluster_13` (Distance: 11.307 IQR)
- **Magnitude:** 149.54 | **LOC:** 110 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (99.9929%), Concurrency (96.2526%)
- **Heaviest Functions:** `accept_as_ident` (Impact: 40.8), `parse` (Impact: 35.8), `xid_ok` (Impact: 20.6)

### 5. `src/generics.rs` (RUST) -> Cumulative Risk: **696.04**
- **Archetype:** `file_cluster_0` (Distance: 13.162 IQR)
- **Magnitude:** 3973.56 | **LOC:** 1483 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 86.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.4707%)
- **Heaviest Functions:** `parse` (Impact: 479.2), `parse` (Impact: 324.9), `parse` (Impact: 268.2)

### 6. `src/bigint.rs` (RUST) -> Cumulative Risk: **682.93**
- **Archetype:** `file_cluster_13` (Distance: 11.479 IQR)
- **Magnitude:** 71.78 | **LOC:** 69 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `to_string` (Impact: 18.2), `add_assign` (Impact: 7.5), `mul_assign` (Impact: 7.4)

### 7. `src/ty.rs` (RUST) -> Cumulative Risk: **680.68**
- **Archetype:** `file_cluster_0` (Distance: 13.045 IQR)
- **Magnitude:** 1341.58 | **LOC:** 1276 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 85.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `parse` (Impact: 282.1), `parse_bare_fn_arg` (Impact: 127.9), `parse` (Impact: 127.5)

### 8. `src/error.rs` (RUST) -> Cumulative Risk: **680.57**
- **Archetype:** `file_cluster_0` (Distance: 20.122 IQR)
- **Magnitude:** 229.0 | **LOC:** 474 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 70.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (91.6827%)
- **Heaviest Functions:** `fmt` (Impact: 26.6), `next` (Impact: 16.2), `next` (Impact: 16.2)

### 9. `src/buffer.rs` (RUST) -> Cumulative Risk: **676.01**
- **Archetype:** `file_cluster_16` (Distance: 13.483 IQR)
- **Magnitude:** 534.36 | **LOC:** 438 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (89.3464%)
- **Heaviest Functions:** `skip` (Impact: 73.0), `lifetime` (Impact: 60.8), `span` (Impact: 48.8)

### 10. `src/path.rs` (RUST) -> Cumulative Risk: **671.17**
- **Archetype:** `file_cluster_0` (Distance: 14.047 IQR)
- **Magnitude:** 1462.02 | **LOC:** 966 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (96.6904%)
- **Heaviest Functions:** `parse` (Impact: 452.4), `qpath` (Impact: 111.7), `parse_helper` (Impact: 100.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/generics.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.162 IQR)
- **Top Global Matches:** file_cluster_0: 13.162, file_cluster_13: 13.384, file_cluster_16: 13.431
- **Magnitude:** 3973.56 | **LOC:** 1483 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 86.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (12.8474%), Tech Debt (99.4707%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 479.2 | O(2^N) | DB: 2)
  * `parse` (Impact: 324.9 | O(2^N) | DB: 1)
  * `parse` (Impact: 268.2 | O(2^N) | DB: 1)
  * `parse` (Impact: 267.6 | O(2^N) | DB: 1)
  * `parse` (Impact: 239.7 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 287`, `args: 84`, `func_start: 58`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 129`, `dead_code: 6`, `duplicate_logic: 38`
* *Architecture:* `api: 92`, `import: 36`
* *Defense:* `safety: 148`, `doc: 83`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::lifetime::Lifetime, crate::token, crate::print::TokensOrDefault, Path, ParseStream, ConstParam, crate::path::Path, ImplGenerics...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/fixup.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.693 IQR)
- **Top Global Matches:** file_cluster_0: 13.693, file_cluster_8: 14.305, file_cluster_13: 14.336
- **Magnitude:** 1827.6 | **LOC:** 774 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.3419%), Tech Debt (34.9859%)
**Top Internal Functions/Classes:**
  * `scan_right` (Impact: 1514.2 | O(2^N))
  * `parenthesize` (Impact: 94.7 | O(N^5))
    * *Intent:* /// Determine whether parentheses are needed around the given expression to /// head off the early t...
  * `precedence` (Impact: 48.8 | O(N^5))
    * *Intent:* /// Determines the effective precedence of a subexpression. Some expressions /// have higher or lowe...
  * `rightmost_subexpression_precedence` (Impact: 37.5 | O(N^5))
  * `leftmost_subexpression_precedence` (Impact: 26.6 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 65`, `args: 62`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `dead_code: 19`, `duplicate_logic: 2`, `orphaned_logic: 6`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 49`, `doc: 40`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ExprUnary, crate::expr::Expr, ExprReturn, ExprReference, crate::precedence::Precedence, crate::ty::ReturnType, crate::expr::
    ExprBreak, ExprRange...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/expr.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 17.048 IQR)
- **Top Global Matches:** file_cluster_0: 17.048, file_cluster_13: 17.125, file_cluster_11: 17.31
- **Magnitude:** 1769.46 | **LOC:** 4180 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (16.2538%), Tech Debt (62.1051%)
**Top Internal Functions/Classes:**
  * `parse_expr` (Impact: 312.6 | O(N^6) | DB: 1)
  * `unary_expr` (Impact: 251.9 | O(2^N) | DB: 2)
  * `trailer_helper` (Impact: 241.0 | O(N^6) | DB: 4)
  * `trailer_expr` (Impact: 220.7 | O(N^6) | DB: 4)
    * *Intent:* /// An alternative to the primary `Expr::parse` parser (from the [`Parse`] /// trait) for syntactic ...
  * `parse_with_earlier_boundary_rule` (Impact: 215.0 | O(N^3) | DB: 2)
    * *Intent:* /// A cast expression: `foo as f64`. #[cfg_attr(docsrs, doc(cfg(any(feature = "full", feature = "der...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 165`, `args: 26`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 59`, `dead_code: 27`, `duplicate_logic: 8`
* *Architecture:* `api: 11`, `concurrency: 7`, `import: 54`
* *Defense:* `safety: 103`, `doc: 382`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::attr, ExprArray, TokenStream, PatType, Index, crate::ty::ReturnType, ExprAssign, ExprLit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/path.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.047 IQR)
- **Top Global Matches:** file_cluster_0: 14.047, file_cluster_13: 14.178, file_cluster_11: 14.363
- **Magnitude:** 1462.02 | **LOC:** 966 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (15.1495%), Tech Debt (96.6904%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 452.4 | O(2^N) | DB: 3)
  * `qpath` (Impact: 111.7 | O(N^6) | DB: 2)
  * `parse_helper` (Impact: 100.2 | O(N^5))
    * *Intent:* #[cfg_attr(docsrs, doc(cfg(feature = "parsing")))]
  * `parse_mod_style` (Impact: 97.6 | O(N^5) | DB: 1)
  * `do_parse` (Impact: 71.3 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 177`, `args: 54`, `func_start: 41`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 73`, `dead_code: 12`, `duplicate_logic: 18`
* *Architecture:* `api: 65`, `import: 33`
* *Defense:* `safety: 108`, `doc: 123`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::lifetime::Lifetime, crate::token, crate::print::TokensOrDefault, Path, ParseStream, alloc::collections::HashMap, proc_macro2::TokenStream, crate::punctuated::Punctuated...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ty.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.045 IQR)
- **Top Global Matches:** file_cluster_0: 13.045, file_cluster_13: 13.161, file_cluster_16: 13.252
- **Magnitude:** 1341.58 | **LOC:** 1276 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 85.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (19.5751%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 282.1 | O(2^N) | DB: 2)
  * `parse_bare_fn_arg` (Impact: 127.9 | O(N^4) | DB: 6)
  * `parse` (Impact: 127.5 | O(2^N) | DB: 1)
  * `parse` (Impact: 99.4 | O(2^N) | DB: 2)
    * *Intent:* /// In some positions, types may not contain the `+` character, to /// disambiguate them. For exampl...
  * `parse_bounds` (Impact: 56.6 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 154`, `args: 30`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 65`, `dead_code: 1`, `duplicate_logic: 39`
* *Architecture:* `api: 7`, `import: 20`
* *Defense:* `safety: 84`, `doc: 55`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::lifetime::Lifetime, crate::token, crate::print::TokensOrDefault, ParseStream, crate::path::Path, TypeInfer, proc_macro2::TokenStream, TypeNever...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/punctuated.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.111 IQR)
- **Top Global Matches:** file_cluster_16: 14.111, file_cluster_0: 14.281, file_cluster_13: 14.336
- **Magnitude:** 1106.14 | **LOC:** 1171 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (16.3286%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `fold` (Impact: 61.5 | O(2^N) | DB: 4)
    * *Intent:* /// Mutably borrows the punctuation from this punctuated pair, unless the /// pair is the final one ...
  * `get` (Impact: 35.1 | O(2^N))
  * `get_mut` (Impact: 35.1 | O(2^N) | DB: 2)
  * `index` (Impact: 35.1 | O(2^N))
  * `do_extend` (Impact: 25.4 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 230`, `args: 109`, `func_start: 86`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 178`, `dead_code: 2`, `duplicate_logic: 51`
* *Architecture:* `api: 52`, `import: 19`
* *Defense:* `safety: 116`, `doc: 182`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ParseStream, crate::punctuated::Pair, core::iter, proc_macro2::TokenStream, Hasher, crate::drops::NoDrop, alloc::collections::VecDeque, core::fmt::self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pat.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.69 IQR)
- **Top Global Matches:** file_cluster_0: 13.69, file_cluster_13: 13.71, file_cluster_11: 13.867
- **Magnitude:** 1078.2 | **LOC:** 960 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (10.8377%), Tech Debt (94.8113%)
**Top Internal Functions/Classes:**
  * `pat_range_bound` (Impact: 101.6 | O(N^3))
  * `field_pat` (Impact: 97.3 | O(N^4) | DB: 1)
  * `pat_path_or_macro_or_struct_or_range` (Impact: 85.8 | O(N^5))
  * `pat_slice` (Impact: 71.7 | O(N^6) | DB: 1)
  * `pat_ident` (Impact: 67.2 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 121`, `args: 46`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 41`, `dead_code: 5`, `duplicate_logic: 12`
* *Architecture:* `api: 13`, `import: 17`
* *Defense:* `safety: 91`, `doc: 116`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::token, ExprMacro, Path, ParseStream, PatReference, crate::path::Path, proc_macro2::TokenStream, PatTupleStruct...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codegen/src/snapshot.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.669 IQR)
- **Top Global Matches:** file_cluster_8: 11.669, file_cluster_13: 11.896, file_cluster_0: 11.953
- **Magnitude:** 1060.58 | **LOC:** 374 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (15.1464%), Tech Debt (9.8189%)
**Top Internal Functions/Classes:**
  * `expand_impl_body` (Impact: 791.1 | O(2^N) | DB: 4)
  * `format_field` (Impact: 148.5 | O(2^N) | DB: 1)
  * `syntax_tree_enum` (Impact: 21.0 | O(N^3))
  * `rust_type` (Impact: 18.1 | O(2^N))
  * `generate` (Impact: 17.4 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 88`, `args: 22`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 20`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 61`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` core::fmt::self, Present, Operand, TokenStream, Debug, lookup, Owned, Display...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lit.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.847 IQR)
- **Top Global Matches:** file_cluster_0: 14.847, file_cluster_13: 14.914, file_cluster_11: 15.043
- **Magnitude:** 989.48 | **LOC:** 1929 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 63.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (12.3704%), Tech Debt (59.7129%)
**Top Internal Functions/Classes:**
  * `parse_lit_c_str_cooked` (Impact: 144.7 | O(N^6) | DB: 4)
    * *Intent:* #[cfg_attr(docsrs, doc(cfg(feature = "extra-traits")))]
  * `parse_lit_byte_str_cooked` (Impact: 104.8 | O(N^6) | DB: 3)
  * `from_str` (Impact: 89.0 | O(N^6))
  * `backslash_u` (Impact: 82.5 | O(N^5) | DB: 3)
  * `parse_lit_char` (Impact: 72.9 | O(N^6) | DB: 1)
    * *Intent:* #[cfg(feature = "clone-impls")] #[cfg_attr(docsrs, doc(cfg(feature = "clone-impls")))]
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 206`, `args: 50`, `func_start: 33`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 77`, `dead_code: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 27`, `import: 29`
* *Defense:* `safety: 139`, `doc: 119`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core::ffi::CStr, core::char, Path, alloc::rc::Rc, ParseStream, Token, crate::token::self, LitFloatRepr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codegen/src/parse.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.87 IQR)
- **Top Global Matches:** file_cluster_8: 11.87, file_cluster_13: 11.954, file_cluster_17: 12.012
- **Magnitude:** 964.18 | **LOC:** 672 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (16.9886%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `do_load_file` (Impact: 200.5 | O(N^6) | DB: 2)
  * `introspect_type` (Impact: 100.1 | O(2^N) | DB: 1)
  * `parse_features` (Impact: 79.3 | O(N^5) | DB: 1)
  * `ast_enum_of_structs` (Impact: 55.8 | O(N^5) | DB: 1)
  * `path_attr` (Impact: 42.6 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 142`, `args: 25`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 2`, `state_mutation: 35`
* *Architecture:* `io: 1`, `api: 15`, `import: 18`
* *Defense:* `safety: 71`, `doc: 2`, `test: 4`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Path, token, BTreeSet, parse_quote, Parser, proc_macro2::TokenStream, syn::
        braced, Item...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/item.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.791 IQR)
- **Top Global Matches:** file_cluster_0: 12.791, file_cluster_13: 12.955, file_cluster_16: 13.124
- **Magnitude:** 924.96 | **LOC:** 3519 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 88.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (7.9341%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `to_tokens` (Impact: 122.7 | O(2^N) | DB: 1)
    * *Intent:* // TODO: https://rust-lang.github.io/rfcs/3323-restrictions.html // // pub struct ImplRestriction { ...
  * `parse` (Impact: 111.2 | O(2^N) | DB: 1)
    * *Intent:* /// A union definition: `union Foo<A, B> { x: A, y: B }`. #[cfg_attr(docsrs, doc(cfg(feature = "full...
  * `parse` (Impact: 60.7 | O(2^N))
  * `to_tokens` (Impact: 37.4 | O(2^N) | DB: 1)
  * `to_tokens` (Impact: 31.9 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 153`, `args: 54`, `func_start: 41`, `class_start: 11`
* *Risk/State:* `state_mutation: 50`, `dead_code: 7`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 39`
* *Architecture:* `api: 73`, `concurrency: 1`, `import: 29`
* *Defense:* `safety: 64`, `doc: 135`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ForeignItemFn, TraitItemConst, ItemType, UseTree, PatType, UseName, crate::expr::Expr, ImplItemFn...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_expr.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.018 IQR)
- **Top Global Matches:** file_cluster_8: 12.018, file_cluster_0: 12.29, file_cluster_16: 12.478
- **Magnitude:** 819.9 | **LOC:** 1703 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (7.6437%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_permutations` (Impact: 245.6 | O(N^6) | DB: 38)
  * `test_fixup` (Impact: 155.9 | O(N^3) | DB: 4)
  * `test_ambiguous_label` (Impact: 60.3 | O(N^3))
  * `test_ranges_bailout` (Impact: 43.6 | O(N^4))
  * `test_extended_interpolated_path` (Impact: 35.7 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 128`, `args: 64`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 91`, `fragile_debt: 1`, `orphaned_logic: 22`
* *Architecture:* `concurrency: 12`, `import: 7`
* *Defense:* `safety: 163`, `test: 28`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ExprMacro, Path, token, ExprReturn, ExprIndex, Block, ExprBlock, LitInt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/stmt.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 16.399 IQR)
- **Top Global Matches:** file_cluster_13: 16.399, file_cluster_0: 16.442, file_cluster_11: 16.565
- **Magnitude:** 817.46 | **LOC:** 489 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (28.452%), Tech Debt (84.4217%)
**Top Internal Functions/Classes:**
  * `parse_stmt` (Impact: 361.0 | O(N^6) | DB: 2)
    * *Intent:* /// /// ``` /// use syn::{braced, token, Attribute, Block, Ident, Result, Stmt, Token}; /// use syn:...
  * `stmt_expr` (Impact: 97.8 | O(N^5) | DB: 7)
  * `stmt_local` (Impact: 96.0 | O(N^5) | DB: 1)
    * *Intent:* // brace-style macros; paren and bracket macros get parsed as // expression statements.
  * `parse_within` (Impact: 66.3 | O(N^4) | DB: 1)
    * *Intent:* /// A macro invocation in statement position. /// /// Syntactically it's ambiguous which other kind ...
  * `to_tokens` (Impact: 61.8 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 109`, `args: 67`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `state_mutation: 39`, `dead_code: 15`, `duplicate_logic: 6`
* *Architecture:* `api: 12`, `concurrency: 8`, `import: 32`
* *Defense:* `safety: 51`, `doc: 71`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::token, ExprMacro, ParseStream, token, Local, crate::path::Path, proc_macro2::TokenStream, crate::item...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/op.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_17` (Drift: 10.819 IQR)
- **Top Global Matches:** file_cluster_17: 10.819, file_cluster_8: 10.858, file_cluster_13: 10.944
- **Magnitude:** 712.78 | **LOC:** 220 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (12.2736%), Tech Debt (95.6336%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 593.0 | O(2^N))
  * `parse` (Impact: 70.6 | O(2^N))
  * `to_tokens` (Impact: 18.9 | O(2^N) | DB: 1)
  * `to_tokens` (Impact: 17.7 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 17`, `args: 8`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `state_mutation: 6`, `duplicate_logic: 4`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `safety: 7`, `doc: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ParseStream, quote::ToTokens, crate::error::Result, crate::op::BinOp, proc_macro2::TokenStream, UnOp, crate::parse::Parse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codegen/src/visit_mut.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.867 IQR)
- **Top Global Matches:** file_cluster_13: 11.867, file_cluster_8: 11.94, file_cluster_0: 12.104
- **Magnitude:** 691.48 | **LOC:** 262 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (26.3275%), Tech Debt (11.2713%)
**Top Internal Functions/Classes:**
  * `node` (Impact: 350.5 | O(2^N) | DB: 14)
  * `visit` (Impact: 268.3 | O(2^N) | DB: 3)
  * `generate` (Impact: 11.8 | O(N^4))
  * `noop_visit` (Impact: 3.3 | O(N^2))
  * `simple_visit` (Impact: 3.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 71`, `args: 12`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 47`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `import: 10`
* *Defense:* `safety: 22`, `doc: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` crate::punctuated::Punctuated, Operand, DocCfg, TokenStream, Owned, crate::cfg::self, gen, syn::Index...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codegen/src/fold.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.64 IQR)
- **Top Global Matches:** file_cluster_13: 11.64, file_cluster_8: 11.675, file_cluster_0: 11.82
- **Magnitude:** 639.5 | **LOC:** 288 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (23.3218%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `node` (Impact: 352.0 | O(2^N) | DB: 13)
  * `visit` (Impact: 209.2 | O(2^N) | DB: 2)
  * `generate` (Impact: 17.2 | O(N^4) | DB: 3)
  * `method_name` (Impact: 2.2 | O(N^1))
  * `simple_fold` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 72`, `args: 9`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 48`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 20`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` DocCfg, TokenStream, gen, crate::cfg::self, syn::Index, Type, Span, Node...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codegen/src/visit.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.356 IQR)
- **Top Global Matches:** file_cluster_8: 11.356, file_cluster_13: 11.387, file_cluster_0: 11.62
- **Magnitude:** 631.24 | **LOC:** 244 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (16.9096%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `node` (Impact: 350.1 | O(2^N) | DB: 8)
  * `visit` (Impact: 223.9 | O(2^N) | DB: 2)
  * `generate` (Impact: 16.6 | O(N^4))
  * `noop_visit` (Impact: 3.3 | O(N^2))
  * `simple_visit` (Impact: 3.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 61`, `args: 11`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 26`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 23`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` crate::punctuated::Punctuated, Operand, TokenStream, Owned, gen, syn::Index, Type, Span...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/repo/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.995 IQR)
- **Top Global Matches:** file_cluster_4: 10.995, file_cluster_8: 11.733, file_cluster_13: 11.775
- **Magnitude:** 586.28 | **LOC:** 631 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (49.9873%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `for_each_rust_file` (Impact: 96.0 | O(N^6) | DB: 2)
  * `clone_rust` (Impact: 54.2 | O(N^4) | DB: 3)
  * `download_and_unpack` (Impact: 49.9 | O(N^3) | DB: 5)
  * `base_dir_filter` (Impact: 25.2 | O(N^2) | DB: 1)
  * `rayon_init` (Impact: 10.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 174`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 3`, `state_mutation: 34`, `planned_debt: 24`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 6`, `concurrency: 288`, `import: 12`
* *Defense:* `safety: 30`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rayon::iter::IntoParallelRefIterator, std::path::Path, anyhow::Result, self::progress::Progress, tar::Archive, std::collections::BTreeSet, std::ffi::OsStr, walkdir::DirEntry...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.077 IQR)
- **Top Global Matches:** file_cluster_0: 14.077, file_cluster_13: 14.139, file_cluster_11: 14.396
- **Magnitude:** 567.96 | **LOC:** 426 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (11.0878%), Tech Debt (99.6377%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 253.9 | O(2^N) | DB: 1)
    * *Intent:* #[cfg(all(feature = "parsing", feature = "printing"))]
  * `parse_named` (Impact: 65.8 | O(N^3))
  * `next` (Impact: 36.9 | O(2^N) | DB: 1)
  * `to_tokens` (Impact: 17.8 | O(2^N) | DB: 1)
  * `to_tokens` (Impact: 17.8 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 91`, `args: 20`, `func_start: 17`, `class_start: 6`
* *Risk/State:* `state_mutation: 21`, `dead_code: 7`, `duplicate_logic: 10`
* *Architecture:* `api: 26`, `import: 25`
* *Defense:* `safety: 37`, `doc: 64`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::token, crate::print::TokensOrDefault, ParseStream, proc_macro2::TokenStream, Fields, crate::restriction::FieldMutability, Variant, crate::scan_expr::scan_expr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/token.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.598 IQR)
- **Top Global Matches:** file_cluster_0: 13.598, file_cluster_13: 13.895, file_cluster_11: 14.112
- **Magnitude:** 549.58 | **LOC:** 1095 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (12.378%), Tech Debt (99.9896%)
**Top Internal Functions/Classes:**
  * `punct_helper` (Impact: 78.2 | O(N^6) | DB: 2)
  * `peek_punct` (Impact: 58.1 | O(N^5) | DB: 1)
  * `parse` (Impact: 30.8 | O(N^5))
  * `keyword` (Impact: 16.1 | O(N^5))
  * `peek` (Impact: 12.4 | O(N^3))
    * *Intent:* #[cfg_attr(not(doc), repr(transparent))] #[allow(unknown_lints, repr_transparent_non_zst_fields)] //...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 262`, `args: 50`, `func_start: 43`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 44`, `dead_code: 12`, `duplicate_logic: 31`
* *Architecture:* `api: 137`, `concurrency: 4`, `import: 27`
* *Defense:* `safety: 41`, `doc: 242`, `test: 2`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::lifetime::Lifetime, self::private::CustomToken, crate::span::IntoSpans, ParseStream, proc_macro2::TokenStream, Hasher, core::ops::Deref, core::fmt::self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/buffer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.483 IQR)
- **Top Global Matches:** file_cluster_16: 13.483, file_cluster_13: 13.548, file_cluster_8: 13.668
- **Magnitude:** 534.36 | **LOC:** 438 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (11.5046%), Tech Debt (89.3464%)
**Top Internal Functions/Classes:**
  * `skip` (Impact: 73.0 | O(2^N) | DB: 1)
  * `lifetime` (Impact: 60.8 | O(2^N) | DB: 1)
  * `span` (Impact: 48.8 | O(2^N) | DB: 1)
    * *Intent:* /// If the cursor is pointing at a `TokenTree`, returns it along with a /// cursor pointing at the n...
  * `recursive_new` (Impact: 37.4 | O(2^N) | DB: 1)
  * `group` (Impact: 35.6 | O(2^N) | DB: 1)
    * *Intent:* /// If the cursor is pointing at a `Lifetime`, returns it along with a /// cursor pointing at the ne...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 75`, `args: 30`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `state_mutation: 37`, `planned_debt: 1`, `orphaned_logic: 9`
* *Architecture:* `api: 24`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 60`, `doc: 68`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core::marker::PhantomData, core::ptr, crate::Lifetime, Punct, proc_macro2::Delimiter, Span, proc_macro2::extra::DelimSpan, TokenStream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/whitespace.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.339 IQR)
- **Top Global Matches:** file_cluster_8: 10.339, file_cluster_7: 10.788, file_cluster_16: 10.797
- **Magnitude:** 511.66 | **LOC:** 66 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (28.058%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `skip` (Impact: 488.2 | O(2^N) | DB: 3)
  * `is_whitespace` (Impact: 12.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 13`, `args: 5`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 9`
* *Architecture:* `api: 1`
* *Defense:* `safety: 3`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/derive.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.913 IQR)
- **Top Global Matches:** file_cluster_13: 10.913, file_cluster_16: 11.205, file_cluster_0: 11.231
- **Magnitude:** 492.82 | **LOC:** 261 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (6.9681%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 297.2 | O(2^N))
  * `data_struct` (Impact: 79.7 | O(N^4) | DB: 2)
  * `to_tokens` (Impact: 62.6 | O(2^N) | DB: 1)
  * `data_union` (Impact: 9.2 | O(N^2))
  * `data_enum` (Impact: 8.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 74`, `args: 6`, `func_start: 5`, `class_start: 5`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 22`, `import: 24`
* *Defense:* `safety: 30`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::token, crate::print::TokensOrDefault, ParseStream, proc_macro2::TokenStream, crate::punctuated::Punctuated, crate::restriction::Visibility, Variant, FieldsNamed...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parse.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 24.631 IQR)
- **Top Global Matches:** file_cluster_0: 24.631, file_cluster_11: 24.732, file_cluster_6: 24.809
- **Magnitude:** 433.8 | **LOC:** 1421 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (9.3083%), Tech Debt (99.9985%)
**Top Internal Functions/Classes:**
  * `span_of_unexpected_ignoring_nones` (Impact: 54.5 | O(2^N) | DB: 1)
  * `parse` (Impact: 32.4 | O(2^N))
    * *Intent:* /// ``` /// use syn::{Ident, ItemUnion, Macro, Result, Token}; /// use syn::parse::{Parse, ParseStre...
  * `parse` (Impact: 21.9 | O(2^N))
    * *Intent:* //! ``` //! //! # The `syn::parse*` functions //! //! The [`syn::parse`], [`syn::parse2`], and [`syn...
  * `__parse_scoped` (Impact: 20.8 | O(N^3) | DB: 1)
  * `parse` (Impact: 18.5 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 148`, `args: 58`, `func_start: 49`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 26`, `dead_code: 122`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 19`
* *Architecture:* `api: 34`, `import: 29`
* *Defense:* `safety: 125`, `doc: 894`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` syn::parenthesized, alloc::rc::Rc, core::mem, token, proc_macro::TokenStream, ParseStream, crate::lookahead::End, Path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/common/eq.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.501 IQR)
- **Top Global Matches:** file_cluster_13: 11.501, file_cluster_8: 11.656, file_cluster_16: 12.21
- **Magnitude:** 431.28 | **LOC:** 922 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (8.7751%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `doc_comment` (Impact: 69.7 | O(N^5) | DB: 2)
  * `eq` (Impact: 62.2 | O(N^6) | DB: 4)
  * `eq` (Impact: 43.8 | O(N^6))
  * `eq` (Impact: 37.6 | O(N^5))
  * `eq` (Impact: 25.2 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 239`, `args: 29`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `duplicate_logic: 24`
* *Architecture:* `api: 1`, `import: 186`
* *Defense:* `safety: 61`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rustc_ast::ast::StaticItem, rustc_ast::ast::StructExpr, DUMMY_SP, rustc_ast::ast::CoroutineKind, rustc_ast::ast::PathSegment, rustc_ast::ast::TyPat, rustc_ast::ast::AttrItem, Hash...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/export.rs` (RUST) | Magnitude: 43.2 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: decorators: 34, api: 27, encapsulation: 27, structural_boundaries: 26
- `src/file.rs` (RUST) | Magnitude: 71.3 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 73, indent_spaces: 38, structural_boundaries: 21, import: 13
- `json/src/lib.rs` (RUST) | Magnitude: 34.28 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 109, indent_spaces: 50, decorators: 24, api: 18
- `src/pat.rs` (RUST) | Magnitude: 1078.2 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 538, branch: 156, structural_boundaries: 121, doc: 116
- `tests/test_unparenthesize.rs` (RUST) | Magnitude: 73.9 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, state_mutation: 22, structural_boundaries: 21, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `dev/parse.rs` (RUST) | Magnitude: 4.08 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 5, args: 3, import: 3
- `src/print.rs` (RUST) | Magnitude: 19.48 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 6, generics: 6, safety: 4
- `src/tt.rs` (RUST) | Magnitude: 93.86 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 45, branch: 10, structural_boundaries: 10, safety: 8
- `tests/repo/progress.rs` (RUST) | Magnitude: 38.36 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 11, state_mutation: 7, generics: 7
- `codegen/src/hash.rs` (RUST) | Magnitude: 230.58 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 145, structural_boundaries: 42, branch: 32, state_mutation: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/spanned.rs` (RUST) | Magnitude: 18.34 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 95, structural_boundaries: 9, indent_spaces: 9, branch: 5
- `src/drops.rs` (RUST) | Magnitude: 32.12 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 26, indent_spaces: 24, generics: 22, branch: 11
- `src/buffer.rs` (RUST) | Magnitude: 534.36 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 271, structural_boundaries: 75, doc: 68, safety: 60
- `src/span.rs` (RUST) | Magnitude: 35.56 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 14, generics: 13, args: 10
- `codegen/src/workspace_path.rs` (RUST) | Magnitude: 4.64 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, generics: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/op.rs` (RUST) | Magnitude: 712.78 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 169, branch: 72, doc: 33, comprehensions: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/repo/mod.rs` (RUST) | Magnitude: 586.28 | Delta: **0.738 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 324, concurrency: 288, structural_boundaries: 174, branch: 65

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/meta.rs` (RUST) | Magnitude: 113.7 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 336, indent_spaces: 79, dead_code: 43, structural_boundaries: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `examples/heapsize/heapsize_derive/src/lib.rs` (RUST) | Magnitude: 57.88 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 23, state_mutation: 9, args: 6
- `examples/trace-var/example/src/main.rs` (RUST) | Magnitude: 15.36 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, state_mutation: 6, structural_boundaries: 4, args: 2
- `codegen/src/visit.rs` (RUST) | Magnitude: 631.24 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 198, structural_boundaries: 61, branch: 37, state_mutation: 26
- `tests/test_ident.rs` (RUST) | Magnitude: 34.82 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: decorators: 20, args: 16, func_start: 16, indent_spaces: 16
- `tests/test_parse_buffer.rs` (RUST) | Magnitude: 47.18 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 18, safety: 14, args: 12

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/lit.rs` -> Churn: **69.82%** | Cog Load: 12.3704% | Debt: 59.7129%
- `src/expr.rs` -> Churn: **51.6%** | Cog Load: 16.2538% | Debt: 62.1051%
- `src/generics.rs` -> Churn: **50.53%** | Cog Load: 12.8474% | Debt: 99.4707%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/generics.rs` -> **David Tolnay** (86.7% isolated ownership) | Magnitude: 3973.56
- `src/ty.rs` -> **David Tolnay** (85.7% isolated ownership) | Magnitude: 1341.58
- `codegen/src/parse.rs` -> **David Tolnay** (100.0% isolated ownership) | Magnitude: 964.18
- `src/item.rs` -> **David Tolnay** (88.9% isolated ownership) | Magnitude: 924.96
- `codegen/src/fold.rs` -> **Tamir Duberstein** (100.0% isolated ownership) | Magnitude: 639.5

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `codegen/src/lookup.rs` -> **Severity: 3.205** (Embedded: 0.0382 * Error Risk: 83.9589%)
- `codegen/src/full.rs` -> **Severity: 3.116** (Embedded: 0.0534 * Error Risk: 58.3219%)
- `codegen/src/gen.rs` -> **Severity: 2.008** (Embedded: 0.0229 * Error Risk: 87.6699%)
- `codegen/src/workspace_path.rs` -> **Severity: 0.382** (Embedded: 0.0076 * Error Risk: 50.0%)
- `src/parse_quote.rs` -> **Severity: 0.117** (Embedded: 0.0382 * Error Risk: 3.0672%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `codegen/src/full.rs` -> **Severity: 2760.985** (Blast Radius: 27.622 * Doc Risk: 99.956%)
- `codegen/src/gen.rs` -> **Severity: 1580.835** (Blast Radius: 15.809 * Doc Risk: 99.9959%)
- `codegen/src/lookup.rs` -> **Severity: 1361.958** (Blast Radius: 24.669 * Doc Risk: 55.2093%)
- `benches/rust.rs` -> **Severity: 694.9** (Blast Radius: 6.949 * Doc Risk: 100.0%)
- `codegen/src/debug.rs` -> **Severity: 694.9** (Blast Radius: 6.949 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
