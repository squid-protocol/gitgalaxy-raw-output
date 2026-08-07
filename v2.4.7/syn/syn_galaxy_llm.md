# ARCHITECTURAL_BRIEF: syn
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/syn` |
| **Timestamp** | `2026-08-07T04:08:21.259332+00:00` |
| **Scan Duration** | `0.61s` |
| **Git Branch** | `master` |
| **Git Commit** | `ae257c4e05a338f73655aa1fa3d144e047daccf1` |
| **Git Remote** | `https://github.com/dtolnay/syn.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 123 malicious artifacts.

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
> **Architectural Drift Z-Score:** `4.242`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 51 | 38.6% |
| file_cluster_13 | 33 | 25.0% |
| file_cluster_0 | 30 | 22.7% |
| file_cluster_16 | 8 | 6.1% |
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
| Cognitive Load Exposure | 0.0 | 71.1 | 12.3 | 7.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 97.8 | 30.8 | 30.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 30.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.9 | 2.3 | 0.0 |
| API Exposure | 0.0 | 8.1 | 2.6 | 2.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 33.1 | 6.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.9 | 13.4 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 94.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 8.1 | 1.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 10.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 19.2 | 14.9 | 0.0 |
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

- `scan_right` (@ `src/fixup.rs`) -> Impact: **228.4** | LOC: 282
- `parse` (@ `src/op.rs`) -> Impact: **121.0** | LOC: 61
- `expand_impl_body` (@ `codegen/src/snapshot.rs`) -> Impact: **118.1** | LOC: 170
- `parse_with_earlier_boundary_rule` (@ `src/expr.rs`) -> Impact: **107.0** | LOC: 60
  * *Intent:* /// A cast expression: `foo as f64`. #[cfg_attr(docsrs, doc(cfg(any(feature = "full", feature = "derive"))))]
- `parse_stmt` (@ `src/stmt.rs`) -> Impact: **103.8** | LOC: 67
  * *Intent:* /// /// ``` /// use syn::{braced, token, Attribute, Block, Ident, Result, Stmt, Token}; /// use syn::parse::{Parse, ParseStream}; /// /// // Parse a f...
- `parse_expr` (@ `src/expr.rs`) -> Impact: **92.2** | LOC: 80
- `test_permutations` (@ `tests/test_expr.rs`) -> Impact: **91.5** | LOC: 790
- `test_fixup` (@ `tests/test_expr.rs`) -> Impact: **76.2** | LOC: 70
- `scan_expr` (@ `src/scan_expr.rs`) -> Impact: **75.7** | LOC: 73
- `skip` (@ `src/whitespace.rs`) -> Impact: **72.3** | LOC: 60

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 48 | 7598.54 | 13.81% | 63.49% |
| `codegen/src` | 20 | 1789.87 | 19.98% | 22.47% |
| `tests` | 28 | 1785.06 | 6.05% | 0.0% |
| `tests/repo` | 2 | 467.14 | 32.65% | 0.0% |
| `tests/common` | 4 | 349.0 | 23.89% | 0.0% |
| `benches` | 2 | 71.12 | 12.63% | 49.62% |
| `examples/trace-var/trace-var/src` | 1 | 69.88 | 8.02% | 0.0% |
| `examples/lazy-static/lazy-static/src` | 1 | 47.28 | 11.55% | 0.0% |
| `examples/dump-syntax/src` | 1 | 40.7 | 6.75% | 0.0% |
| `examples/heapsize/heapsize_derive/src` | 1 | 34.08 | 17.33% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/attr.rs` -> **100.0%** Exposure
- `src/error.rs` -> **100.0%** Exposure
- `src/ext.rs` -> **100.0%** Exposure
- `src/item.rs` -> **100.0%** Exposure
- `src/parse_quote.rs` -> **100.0%** Exposure
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
- `src/token.rs` -> **0** Orphaned Functions | **32** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/op.rs`** -> AI Confidence: **99.48%**
2. **`codegen/src/eq.rs`** -> AI Confidence: **99.31%**
3. **`codegen/src/parse.rs`** -> AI Confidence: **99.31%**
4. **`src/classify.rs`** -> AI Confidence: **99.31%**
5. **`src/expr.rs`** -> AI Confidence: **99.31%**
6. **`src/fixup.rs`** -> AI Confidence: **99.31%**
7. **`src/generics.rs`** -> AI Confidence: **99.31%**
8. **`src/meta.rs`** -> AI Confidence: **99.31%**
9. **`src/pat.rs`** -> AI Confidence: **99.31%**
10. **`src/path.rs`** -> AI Confidence: **99.31%**
11. **`src/scan_expr.rs`** -> AI Confidence: **99.31%**
12. **`src/stmt.rs`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2419` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/error.rs` (RUST) -> Cumulative Risk: **560.57**
- **Archetype:** `file_cluster_0` (Distance: 20.121 IQR)
- **Magnitude:** 111.8 | **LOC:** 474 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 70.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (91.6827%), Dead Code (87.5257%)
- **Heaviest Functions:** `new_at` (Impact: 6.5), `to_compile_error` (Impact: 5.8), `fmt` (Impact: 5.8)

### 2. `src/generics.rs` (RUST) -> Cumulative Risk: **556.71**
- **Archetype:** `file_cluster_0` (Distance: 13.169 IQR)
- **Magnitude:** 951.56 | **LOC:** 1483 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 86.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.4707%), State Flux (83.7411%), Documentation (80.7979%)
- **Heaviest Functions:** `parse` (Impact: 71.2), `do_parse` (Impact: 51.3), `parse` (Impact: 49.0)

### 3. `src/stmt.rs` (RUST) -> Cumulative Risk: **532.48**
- **Archetype:** `file_cluster_13` (Distance: 16.378 IQR)
- **Magnitude:** 299.46 | **LOC:** 489 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (85.692%), Tech Debt (84.4217%), Verification (80.0%)
- **Heaviest Functions:** `parse_stmt` (Impact: 103.8), `stmt_expr` (Impact: 35.2), `stmt_local` (Impact: 33.7)

### 4. `src/bigint.rs` (RUST) -> Cumulative Risk: **519.0**
- **Archetype:** `file_cluster_13` (Distance: 11.479 IQR)
- **Magnitude:** 49.08 | **LOC:** 69 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (95.5022%), Safety Score (88.3606%)
- **Heaviest Functions:** `to_string` (Impact: 7.8), `add_assign` (Impact: 4.0), `mul_assign` (Impact: 4.0)

### 5. `src/ident.rs` (RUST) -> Cumulative Risk: **499.7**
- **Archetype:** `file_cluster_13` (Distance: 10.974 IQR)
- **Magnitude:** 75.84 | **LOC:** 110 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (93.4296%), Documentation (85.4131%), Verification (80.0%)
- **Heaviest Functions:** `accept_as_ident` (Impact: 20.8), `parse` (Impact: 10.8), `xid_ok` (Impact: 10.7)

### 6. `src/drops.rs` (RUST) -> Cumulative Risk: **481.74**
- **Archetype:** `file_cluster_16` (Distance: 11.191 IQR)
- **Magnitude:** 24.62 | **LOC:** 59 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.7966%), State Flux (98.9611%), Documentation (66.3455%)
- **Heaviest Functions:** `test_needs_drop` (Impact: 4.4), `new` (Impact: 2.3), `deref_mut` (Impact: 2.1)

### 7. `src/token.rs` (RUST) -> Cumulative Risk: **462.95**
- **Archetype:** `file_cluster_0` (Distance: 13.588 IQR)
- **Magnitude:** 348.68 | **LOC:** 1095 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9929%), Documentation (99.4193%), State Flux (44.9868%)
- **Heaviest Functions:** `punct_helper` (Impact: 23.2), `peek_punct` (Impact: 20.0), `parse` (Impact: 10.8)

### 8. `src/expr.rs` (RUST) -> Cumulative Risk: **450.24**
- **Archetype:** `file_cluster_0` (Distance: 17.02 IQR)
- **Magnitude:** 624.36 | **LOC:** 4180 | **CtrlFlow:** 59.1% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (73.3641%), Tech Debt (62.1051%)
- **Heaviest Functions:** `parse_with_earlier_boundary_rule` (Impact: 107.0), `parse_expr` (Impact: 92.2), `trailer_helper` (Impact: 70.4)

### 9. `src/ext.rs` (RUST) -> Cumulative Risk: **443.63**
- **Archetype:** `file_cluster_0` (Distance: 21.911 IQR)
- **Magnitude:** 32.36 | **LOC:** 181 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Dead Code (94.588%), State Flux (61.2336%)
- **Heaviest Functions:** `parse_any` (Impact: 5.7), `new_spanned` (Impact: 4.5), `append` (Impact: 3.9)

### 10. `codegen/src/gen.rs` (RUST) -> Cumulative Risk: **438.75**
- **Archetype:** `file_cluster_13` (Distance: 11.259 IQR)
- **Magnitude:** 32.04 | **LOC:** 38 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (87.6699%), Documentation (86.3675%)
- **Heaviest Functions:** `traverse` (Impact: 7.3), `under_name` (Impact: 2.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/generics.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.169 IQR)
- **Top Global Matches:** file_cluster_0: 13.169, file_cluster_13: 13.391, file_cluster_16: 13.438
- **Magnitude:** 951.56 | **LOC:** 1483 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 86.7%
- **Risk Profile:** Cognitive Load (12.7234%), Tech Debt (99.4707%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 71.2)
  * `do_parse` (Impact: 51.3)
  * `parse` (Impact: 49.0)
  * `parse_multiple` (Impact: 40.5)
  * `parse` (Impact: 40.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 328`, `structural_boundaries: 287`, `args: 90`, `func_start: 58`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 129`, `dead_code: 6`, `duplicate_logic: 38`
* *Architecture:* `api: 92`, `import: 36`
* *Defense:* `safety: 148`, `doc: 83`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IterMut, crate::print::TokensOrDefault, crate::punctuated::Punctuated, alloc::vec::Vec, TypeParam, Result, crate::error, quote::ToTokens...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/expr.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 17.02 IQR)
- **Top Global Matches:** file_cluster_0: 17.02, file_cluster_13: 17.097, file_cluster_11: 17.282
- **Magnitude:** 624.36 | **LOC:** 4180 | **CtrlFlow:** 59.1% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (16.1227%), Tech Debt (62.1051%)
**Top Internal Functions/Classes:**
  * `parse_with_earlier_boundary_rule` (Impact: 107.0)
    * *Intent:* /// A cast expression: `foo as f64`. #[cfg_attr(docsrs, doc(cfg(any(feature = "full", feature = "der...
  * `parse_expr` (Impact: 92.2)
  * `trailer_helper` (Impact: 70.4)
  * `trailer_expr` (Impact: 65.7)
    * *Intent:* /// An alternative to the primary `Expr::parse` parser (from the [`Parse`] /// trait) for syntactic ...
  * `unary_expr` (Impact: 44.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 165`, `args: 17`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 59`, `dead_code: 27`, `duplicate_logic: 8`
* *Architecture:* `api: 11`, `concurrency: 7`, `import: 54`
* *Defense:* `safety: 103`, `doc: 382`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FieldValue, ExprParen, UnOp, crate::path::printing::PathStyle, ExprMethodCall, crate::parse::ParseBuffer, alloc::string::ToString, core::hash::Hash...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/punctuated.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.081 IQR)
- **Top Global Matches:** file_cluster_16: 14.081, file_cluster_0: 14.253, file_cluster_13: 14.309
- **Magnitude:** 529.44 | **LOC:** 1171 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (15.8647%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `fold` (Impact: 10.4)
    * *Intent:* /// Mutably borrows the punctuation from this punctuated pair, unless the /// pair is the final one ...
  * `parse_separated_nonempty_with` (Impact: 9.6)
    * *Intent:* /// Inserts an element at position `index`. /// /// # Panics /// /// Panics if `index` is greater th...
  * `get_mut` (Impact: 9.2)
  * `get` (Impact: 9.1)
  * `do_extend` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 230`, `args: 109`, `func_start: 86`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 174`, `dead_code: 2`, `duplicate_logic: 51`
* *Architecture:* `api: 52`, `import: 19`
* *Defense:* `safety: 116`, `doc: 182`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core::slice, proc_macro2::TokenStream, quote::ToTokens, crate::parse::Parse, ParseStream, crate::punctuated::Pair, core::option, Token...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/path.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.021 IQR)
- **Top Global Matches:** file_cluster_0: 14.021, file_cluster_13: 14.152, file_cluster_11: 14.34
- **Magnitude:** 518.32 | **LOC:** 966 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (14.8423%), Tech Debt (97.5898%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 68.5)
  * `parse_helper` (Impact: 34.4)
    * *Intent:* #[cfg_attr(docsrs, doc(cfg(feature = "parsing")))]
  * `qpath` (Impact: 33.7)
  * `parse_mod_style` (Impact: 33.6)
  * `do_parse` (Impact: 21.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 177`, `args: 52`, `func_start: 41`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 71`, `dead_code: 12`, `duplicate_logic: 19`
* *Architecture:* `api: 65`, `import: 33`
* *Defense:* `safety: 108`, `doc: 123`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AssocConst, crate::print::TokensOrDefault, crate::punctuated::Punctuated, alloc::vec::Vec, syn::Path, Result, quote::ToTokens, ParenthesizedGenericArguments...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_expr.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.921 IQR)
- **Top Global Matches:** file_cluster_8: 11.921, file_cluster_0: 12.198, file_cluster_16: 12.386
- **Magnitude:** 500.9 | **LOC:** 1703 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.337%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_permutations` (Impact: 91.5)
  * `test_fixup` (Impact: 76.2)
  * `iter` (Impact: 70.3)
  * `test_ambiguous_label` (Impact: 30.8)
  * `test_extended_interpolated_path` (Impact: 14.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 128`, `args: 28`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 91`, `fragile_debt: 1`, `orphaned_logic: 22`
* *Architecture:* `concurrency: 12`, `import: 7`
* *Defense:* `safety: 163`, `test: 28`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Lit, crate::common::visit::AsIfPrinted, TokenStream, AngleBracketedGenericArguments, ExprStruct, ExprConst, ExprField, ExprBreak...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/repo/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.995 IQR)
- **Top Global Matches:** file_cluster_4: 10.995, file_cluster_8: 11.733, file_cluster_13: 11.775
- **Magnitude:** 447.28 | **LOC:** 631 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.985%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `for_each_rust_file` (Impact: 28.6)
  * `download_and_unpack` (Impact: 25.7)
  * `clone_rust` (Impact: 23.0)
  * `base_dir_filter` (Impact: 17.2)
  * `rayon_init` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 174`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 3`, `state_mutation: 34`, `planned_debt: 24`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 6`, `concurrency: 288`, `import: 12`
* *Defense:* `safety: 30`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tar::Archive, anyhow::Result, PathBuf, std::ffi::OsStr, walkdir::DirEntry, std::collections::BTreeSet, WalkDir, std::fs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pat.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.693 IQR)
- **Top Global Matches:** file_cluster_0: 13.693, file_cluster_13: 13.714, file_cluster_11: 13.87
- **Magnitude:** 430.1 | **LOC:** 960 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (10.8377%), Tech Debt (94.8113%)
**Top Internal Functions/Classes:**
  * `pat_range_bound` (Impact: 51.6)
  * `field_pat` (Impact: 40.4)
  * `pat_path_or_macro_or_struct_or_range` (Impact: 29.8)
  * `multi_pat_impl` (Impact: 23.6)
  * `pat_ident` (Impact: 23.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 121`, `args: 47`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 41`, `dead_code: 5`, `duplicate_logic: 12`
* *Architecture:* `api: 13`, `import: 17`
* *Defense:* `safety: 91`, `doc: 116`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::punctuated::Punctuated, alloc::vec::Vec, ExprConst, PatTuple, Result, ParseBuffer, quote::ToTokens, crate::attr::Attribute...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lit.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.807 IQR)
- **Top Global Matches:** file_cluster_0: 14.807, file_cluster_13: 14.873, file_cluster_11: 15.004
- **Magnitude:** 413.58 | **LOC:** 1929 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 63.2%
- **Risk Profile:** Cognitive Load (12.2608%), Tech Debt (59.7129%)
**Top Internal Functions/Classes:**
  * `parse_lit_c_str_cooked` (Impact: 44.0)
    * *Intent:* #[cfg_attr(docsrs, doc(cfg(feature = "extra-traits")))]
  * `parse_lit_byte_str_cooked` (Impact: 32.2)
  * `from_str` (Impact: 28.4)
  * `backslash_u` (Impact: 26.6)
  * `parse_lit_char` (Impact: 22.6)
    * *Intent:* #[cfg(feature = "clone-impls")] #[cfg_attr(docsrs, doc(cfg(feature = "clone-impls")))]
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 206`, `args: 34`, `func_start: 33`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 77`, `dead_code: 18`, `duplicate_logic: 10`
* *Architecture:* `api: 27`, `import: 29`
* *Defense:* `safety: 139`, `doc: 119`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Parser, FromStr, Lit, proc_macro2::Group, alloc::vec::Vec, LitIntRepr, crate::lit::
        Lit, Result...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codegen/src/parse.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.938 IQR)
- **Top Global Matches:** file_cluster_8: 11.938, file_cluster_13: 12.022, file_cluster_17: 12.08
- **Magnitude:** 393.78 | **LOC:** 672 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (15.9421%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `do_load_file` (Impact: 60.8)
  * `parse_features` (Impact: 25.4)
  * `ast_enum_of_structs` (Impact: 19.8)
  * `introspect_features` (Impact: 17.1)
  * `introspect_type` (Impact: 17.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 142`, `args: 42`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 2`, `state_mutation: 35`
* *Architecture:* `io: 1`, `api: 15`, `import: 18`
* *Defense:* `safety: 71`, `doc: 2`, `test: 4`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Parser, Lit, std::collections::BTreeMap, TypeMacro, bracketed, super::AstItem, Result, syn::
        braced...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/fixup.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.645 IQR)
- **Top Global Matches:** file_cluster_0: 13.645, file_cluster_8: 14.259, file_cluster_13: 14.29
- **Magnitude:** 370.7 | **LOC:** 774 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.3419%), Tech Debt (34.9859%)
**Top Internal Functions/Classes:**
  * `scan_right` (Impact: 228.4)
  * `parenthesize` (Impact: 32.4)
    * *Intent:* /// Determine whether parentheses are needed around the given expression to /// head off the early t...
  * `precedence` (Impact: 17.6)
    * *Intent:* /// Determines the effective precedence of a subexpression. Some expressions /// have higher or lowe...
  * `rightmost_subexpression_precedence` (Impact: 13.3)
  * `leftmost_subexpression_with_operator` (Impact: 9.5)
    * *Intent:* /// Transform this fixup into the one that should apply when printing the /// leftmost subexpression...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 65`, `args: 45`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `dead_code: 19`, `duplicate_logic: 2`, `orphaned_logic: 6`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 49`, `doc: 40`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::expr::
    ExprBreak, crate::precedence::Precedence, crate::ty::ReturnType, ExprRange, crate::classify, crate::expr::Expr, ExprUnary, ExprYield...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ty.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.111 IQR)
- **Top Global Matches:** file_cluster_0: 13.111, file_cluster_13: 13.227, file_cluster_16: 13.318
- **Magnitude:** 370.68 | **LOC:** 1276 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (19.5751%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `parse_bare_fn_arg` (Impact: 52.6)
  * `parse` (Impact: 42.1)
  * `parse` (Impact: 19.4)
  * `parse_bounds` (Impact: 17.5)
  * `parse` (Impact: 16.3)
    * *Intent:* /// In some positions, types may not contain the `+` character, to /// disambiguate them. For exampl...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 154`, `args: 49`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 65`, `dead_code: 1`, `duplicate_logic: 39`
* *Architecture:* `api: 7`, `import: 20`
* *Defense:* `safety: 84`, `doc: 55`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TypeArray, crate::print::TokensOrDefault, crate::punctuated::Punctuated, alloc::vec::Vec, TypeMacro, TypeSlice, Result, quote::ToTokens...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/token.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.588 IQR)
- **Top Global Matches:** file_cluster_0: 13.588, file_cluster_13: 13.885, file_cluster_11: 14.105
- **Magnitude:** 348.68 | **LOC:** 1095 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (12.1773%), Tech Debt (99.9929%)
**Top Internal Functions/Classes:**
  * `punct_helper` (Impact: 23.2)
  * `peek_punct` (Impact: 20.0)
  * `parse` (Impact: 10.8)
  * `peek` (Impact: 6.5)
    * *Intent:* #[cfg_attr(not(doc), repr(transparent))] #[allow(unknown_lints, repr_transparent_non_zst_fields)] //...
  * `keyword` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 262`, `args: 48`, `func_start: 43`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 44`, `dead_code: 12`, `duplicate_logic: 32`
* *Architecture:* `api: 137`, `concurrency: 4`, `import: 27`
* *Defense:* `safety: 41`, `doc: 242`, `test: 2`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core::ops::Deref, self::private::WithSpan, TokenStream, Result, quote::ToTokens, proc_macro2::Literal, crate::parse::Parse, ParseStream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/item.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.791 IQR)
- **Top Global Matches:** file_cluster_0: 12.791, file_cluster_13: 12.955, file_cluster_16: 13.124
- **Magnitude:** 316.26 | **LOC:** 3519 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 88.9%
- **Risk Profile:** Cognitive Load (7.9341%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 23.1)
    * *Intent:* /// A union definition: `union Foo<A, B> { x: A, y: B }`. #[cfg_attr(docsrs, doc(cfg(feature = "full...
  * `to_tokens` (Impact: 18.8)
    * *Intent:* // TODO: https://rust-lang.github.io/rfcs/3323-restrictions.html // // pub struct ImplRestriction { ...
  * `parse` (Impact: 12.7)
  * `parse_impl_item_type` (Impact: 8.6)
    * *Intent:* #[cfg(feature = "parsing")]
  * `to_tokens` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 153`, `args: 54`, `func_start: 41`, `class_start: 11`
* *Risk/State:* `state_mutation: 50`, `dead_code: 7`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 39`
* *Architecture:* `api: 73`, `concurrency: 1`, `import: 29`
* *Defense:* `safety: 64`, `doc: 135`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` UsePath, ParseBuffer, crate::path::printing::PathStyle, TypePath, UseGroup, ItemEnum, crate::stmt::Block, alloc::boxed::Box...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/stmt.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 16.378 IQR)
- **Top Global Matches:** file_cluster_13: 16.378, file_cluster_0: 16.421, file_cluster_11: 16.545
- **Magnitude:** 299.46 | **LOC:** 489 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (28.2384%), Tech Debt (84.4217%)
**Top Internal Functions/Classes:**
  * `parse_stmt` (Impact: 103.8)
    * *Intent:* /// /// ``` /// use syn::{braced, token, Attribute, Block, Ident, Result, Stmt, Token}; /// use syn:...
  * `stmt_expr` (Impact: 35.2)
  * `stmt_local` (Impact: 33.7)
    * *Intent:* // brace-style macros; paren and bracket macros get parsed as // expression statements.
  * `parse_within` (Impact: 27.4)
    * *Intent:* /// A macro invocation in statement position. /// /// Syntactically it's ambiguous which other kind ...
  * `to_tokens` (Impact: 9.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 109`, `args: 60`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `state_mutation: 39`, `dead_code: 15`, `duplicate_logic: 6`
* *Architecture:* `api: 12`, `concurrency: 8`, `import: 32`
* *Defense:* `safety: 51`, `doc: 71`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` alloc::vec::Vec, crate::pat::Pat, Result, quote::ToTokens, crate::attr::Attribute, crate::mac::self, crate::parse::Parse, ParseStream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/parse.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 24.626 IQR)
- **Top Global Matches:** file_cluster_0: 24.626, file_cluster_11: 24.728, file_cluster_6: 24.805
- **Magnitude:** 243.1 | **LOC:** 1421 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (9.3128%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `span_of_unexpected_ignoring_nones` (Impact: 14.2)
  * `parse` (Impact: 11.9)
    * *Intent:* //! ``` //! //! # The `syn::parse*` functions //! //! The [`syn::parse`], [`syn::parse2`], and [`syn...
  * `__parse_scoped` (Impact: 10.8)
  * `parse2` (Impact: 9.3)
    * *Intent:* /// steps: Punctuated<Expr, Fin>, /// } /// /// impl Parse for Thing { /// fn parse(input: ParseStre...
  * `parse` (Impact: 8.3)
    * *Intent:* /// ``` /// use syn::{Ident, ItemUnion, Macro, Result, Token}; /// use syn::parse::{Parse, ParseStre...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 148`, `args: 57`, `func_start: 49`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 26`, `dead_code: 122`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 23`
* *Architecture:* `api: 34`, `import: 29`
* *Defense:* `safety: 125`, `doc: 894`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` core::ops::Deref, Parser, TokenStream, UnwindSafe, syn::buffer::Cursor, crate::punctuated::Punctuated, syn::parse::Parser, Lookahead1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codegen/src/snapshot.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.477 IQR)
- **Top Global Matches:** file_cluster_8: 11.477, file_cluster_13: 11.725, file_cluster_0: 11.78
- **Magnitude:** 228.88 | **LOC:** 374 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (19.6201%), Tech Debt (64.7335%)
**Top Internal Functions/Classes:**
  * `expand_impl_body` (Impact: 118.1)
  * `format_field` (Impact: 23.8)
  * `syntax_tree_enum` (Impact: 11.0)
  * `generate` (Impact: 9.3)
  * `fmt` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 88`, `args: 18`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 16`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 61`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` TokenStream, Operand, quote::format_ident, Display, proc_macro2::Ident, crate::file, lookup, syn_codegen::Data...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/buffer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.483 IQR)
- **Top Global Matches:** file_cluster_16: 13.483, file_cluster_13: 13.548, file_cluster_8: 13.668
- **Magnitude:** 210.16 | **LOC:** 438 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (11.5046%), Tech Debt (89.3464%)
**Top Internal Functions/Classes:**
  * `skip` (Impact: 13.0)
  * `lifetime` (Impact: 10.8)
  * `ignore_none` (Impact: 10.4)
  * `span` (Impact: 8.8)
    * *Intent:* /// If the cursor is pointing at a `TokenTree`, returns it along with a /// cursor pointing at the n...
  * `group` (Impact: 7.9)
    * *Intent:* /// If the cursor is pointing at a `Lifetime`, returns it along with a /// cursor pointing at the ne...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 75`, `args: 30`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `state_mutation: 37`, `planned_debt: 1`, `orphaned_logic: 9`
* *Architecture:* `api: 24`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 60`, `doc: 68`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Punct, TokenStream, core::marker::PhantomData, crate::Lifetime, Group, crate::ext::TokenStreamExt, alloc::vec::Vec, core::cmp::Ordering...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_precedence.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.126 IQR)
- **Top Global Matches:** file_cluster_13: 12.126, file_cluster_8: 12.349, file_cluster_0: 12.386
- **Magnitude:** 200.88 | **LOC:** 557 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (12.9736%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_expressions` (Impact: 36.0)
  * `librustc_parenthesize` (Impact: 21.3)
  * `make_parens_invisible` (Impact: 11.9)
  * `test_rustc_precedence` (Impact: 11.3)
  * `contains_let_chain` (Impact: 8.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 87`, `args: 21`, `func_start: 19`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 55`, `duplicate_logic: 4`, `orphaned_logic: 8`
* *Architecture:* `io: 1`, `import: 25`
* *Defense:* `safety: 22`, `doc: 1`, `test: 1`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Lit, ExprGroup, rustc_span::DUMMY_SP, Fold, crate::common::eq::SpanlessEq, syn::parse::Parser, ExprField, quote::ToTokens...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/common/eq.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.515 IQR)
- **Top Global Matches:** file_cluster_13: 11.515, file_cluster_8: 11.669, file_cluster_16: 12.223
- **Magnitude:** 194.38 | **LOC:** 922 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.666%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `doc_comment` (Impact: 22.6)
  * `eq` (Impact: 18.9)
  * `eq` (Impact: 13.5)
  * `eq` (Impact: 13.4)
  * `eq` (Impact: 7.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 239`, `args: 37`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `duplicate_logic: 25`
* *Architecture:* `api: 1`, `import: 186`
* *Defense:* `safety: 61`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rustc_ast::ast::FieldDef, rustc_ast::ast::GenericArgs, rustc_ast::ast::FormatArgs, rustc_ast::ast::Guard, rustc_ast::ast::FnPtrTy, rustc_ast::ast::InlineAsm, rustc_ast::ast::Movability, rustc_ast::ast::UnsafeBinderCastKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.077 IQR)
- **Top Global Matches:** file_cluster_0: 14.077, file_cluster_13: 14.139, file_cluster_11: 14.396
- **Magnitude:** 182.26 | **LOC:** 426 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (11.0878%), Tech Debt (99.6377%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 37.9)
    * *Intent:* #[cfg(all(feature = "parsing", feature = "printing"))]
  * `parse_named` (Impact: 33.8)
  * `parse_unnamed` (Impact: 8.6)
  * `next` (Impact: 6.9)
  * `iter_mut` (Impact: 4.3)
    * *Intent:* /// Get an iterator over the borrowed [`Field`] items in this object. This
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 91`, `args: 20`, `func_start: 17`, `class_start: 6`
* *Risk/State:* `state_mutation: 21`, `dead_code: 7`, `duplicate_logic: 10`
* *Architecture:* `api: 26`, `import: 25`
* *Defense:* `safety: 37`, `doc: 64`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::print::TokensOrDefault, alloc::vec::Vec, quote::ToTokens, crate::attr::Attribute, crate::parse::Parse, ParseStream, Fields, crate::token...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codegen/src/visit_mut.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.845 IQR)
- **Top Global Matches:** file_cluster_13: 11.845, file_cluster_8: 11.916, file_cluster_0: 12.082
- **Magnitude:** 173.58 | **LOC:** 262 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (26.0324%), Tech Debt (11.2713%)
**Top Internal Functions/Classes:**
  * `node` (Impact: 53.1)
  * `visit` (Impact: 47.8)
  * `generate` (Impact: 5.8)
  * `requires_full` (Impact: 4.2)
  * `visit_attributes_mut` (Impact: 3.7)
    * *Intent:* #features
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 71`, `args: 11`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 47`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `import: 10`
* *Defense:* `safety: 22`, `doc: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` TokenStream, crate::punctuated::Punctuated, alloc::vec::Vec, Operand, quote::format_ident, proc_macro2::Ident, full, crate::file...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codegen/src/fold.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.495 IQR)
- **Top Global Matches:** file_cluster_13: 11.495, file_cluster_8: 11.51, file_cluster_0: 11.677
- **Magnitude:** 162.1 | **LOC:** 288 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.9634%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `node` (Impact: 54.6)
  * `visit` (Impact: 37.7)
  * `generate` (Impact: 6.2)
  * `requires_full` (Impact: 4.2)
  * `fold_vec` (Impact: 2.4)
    * *Intent:* #impls
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 72`, `args: 11`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 42`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 20`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` TokenStream, alloc::vec::Vec, quote::format_ident, proc_macro2::Ident, full, crate::file, syn_codegen::Data, alloc::boxed::Box...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/op.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_17` (Drift: 10.803 IQR)
- **Top Global Matches:** file_cluster_17: 10.803, file_cluster_8: 10.841, file_cluster_13: 10.928
- **Magnitude:** 157.08 | **LOC:** 220 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.2736%), Tech Debt (95.6336%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 121.0)
  * `parse` (Impact: 14.6)
  * `to_tokens` (Impact: 5.1)
  * `to_tokens` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 17`, `args: 7`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `state_mutation: 6`, `duplicate_logic: 4`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `safety: 7`, `doc: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::error::Result, crate::parse::Parse, proc_macro2::TokenStream, quote::ToTokens, UnOp, ParseStream, crate::op::BinOp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/classify.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.286 IQR)
- **Top Global Matches:** file_cluster_8: 11.286, file_cluster_0: 11.393, file_cluster_13: 11.539
- **Magnitude:** 149.02 | **LOC:** 312 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.9845%), Tech Debt (94.7559%)
**Top Internal Functions/Classes:**
  * `expr_trailing_brace` (Impact: 48.9)
    * *Intent:* /// Whether the expression's first token is the label of a loop/block.
  * `trailing_unparameterized_path` (Impact: 25.2)
  * `type_trailing_brace` (Impact: 17.4)
  * `last_type_in_path` (Impact: 6.5)
  * `last_type_in_path` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 32`, `args: 43`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 9`, `duplicate_logic: 4`, `orphaned_logic: 3`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `safety: 44`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TokenStream, crate::path::Path, crate::ty::ReturnType, TokenTree, PathArguments, crate::punctuated::Punctuated, crate::expr::Expr, crate::generics::TypeParamBound...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codegen/src/visit.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.335 IQR)
- **Top Global Matches:** file_cluster_8: 11.335, file_cluster_13: 11.369, file_cluster_0: 11.601
- **Magnitude:** 143.44 | **LOC:** 244 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.6676%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `node` (Impact: 52.7)
  * `visit` (Impact: 40.2)
  * `generate` (Impact: 7.6)
  * `requires_full` (Impact: 4.2)
  * `noop_visit` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 61`, `args: 10`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 26`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 23`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.949
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` TokenStream, crate::punctuated::Punctuated, Operand, quote::format_ident, proc_macro2::Ident, full, crate::file, syn_codegen::Data...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/export.rs` (RUST) | Magnitude: 43.2 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: decorators: 34, api: 27, encapsulation: 27, structural_boundaries: 26
- `src/file.rs` (RUST) | Magnitude: 21.6 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 73, indent_spaces: 38, structural_boundaries: 21, import: 13
- `json/src/lib.rs` (RUST) | Magnitude: 31.58 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 109, indent_spaces: 50, decorators: 24, api: 18
- `src/pat.rs` (RUST) | Magnitude: 430.1 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 538, branch: 156, structural_boundaries: 121, doc: 116
- `tests/test_unparenthesize.rs` (RUST) | Magnitude: 41.0 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, state_mutation: 22, structural_boundaries: 21, safety: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/spanned.rs` (RUST) | Magnitude: 8.14 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 95, structural_boundaries: 9, indent_spaces: 9, branch: 3
- `codegen/src/fold.rs` (RUST) | Magnitude: 162.1 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 231, structural_boundaries: 72, state_mutation: 42, branch: 34
- `codegen/src/hash.rs` (RUST) | Magnitude: 97.98 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 145, structural_boundaries: 42, branch: 32, state_mutation: 19
- `src/print.rs` (RUST) | Magnitude: 9.08 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 6, generics: 6, safety: 4
- `tests/repo/progress.rs` (RUST) | Magnitude: 19.86 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 11, state_mutation: 7, generics: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/buffer.rs` (RUST) | Magnitude: 210.16 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 271, structural_boundaries: 75, doc: 68, safety: 60
- `src/span.rs` (RUST) | Magnitude: 24.16 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 14, generics: 13, args: 10
- `codegen/src/workspace_path.rs` (RUST) | Magnitude: 4.64 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, generics: 2, args: 1
- `src/drops.rs` (RUST) | Magnitude: 24.62 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 26, indent_spaces: 24, generics: 22, branch: 8
- `src/punctuated.rs` (RUST) | Magnitude: 529.44 | Delta: **0.172 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 598, generics: 251, structural_boundaries: 230, doc: 182

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/op.rs` (RUST) | Magnitude: 157.08 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 169, branch: 72, doc: 33, comprehensions: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/repo/mod.rs` (RUST) | Magnitude: 447.28 | Delta: **0.738 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 324, concurrency: 288, structural_boundaries: 174, branch: 65

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/meta.rs` (RUST) | Magnitude: 58.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 336, indent_spaces: 79, dead_code: 43, structural_boundaries: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tests/test_parse_buffer.rs` (RUST) | Magnitude: 43.28 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 18, safety: 14, args: 12
- `examples/heapsize/heapsize_derive/src/lib.rs` (RUST) | Magnitude: 34.08 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 23, state_mutation: 9, args: 6
- `examples/trace-var/example/src/main.rs` (RUST) | Magnitude: 13.06 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, state_mutation: 6, structural_boundaries: 4, args: 2
- `dev/parse.rs` (RUST) | Magnitude: 6.08 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, args: 3, import: 3
- `tests/test_ident.rs` (RUST) | Magnitude: 32.82 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: decorators: 20, args: 16, func_start: 16, indent_spaces: 16

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/lit.rs` -> Churn: **69.82%** | Cog Load: 12.2608% | Debt: 59.7129%
- `src/expr.rs` -> Churn: **51.6%** | Cog Load: 16.1227% | Debt: 62.1051%
- `src/generics.rs` -> Churn: **50.53%** | Cog Load: 12.7234% | Debt: 99.4707%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/generics.rs` -> **David Tolnay** (86.7% isolated ownership) | Magnitude: 951.56
- `tests/repo/mod.rs` -> **David Tolnay** (100.0% isolated ownership) | Magnitude: 447.28
- `codegen/src/parse.rs` -> **David Tolnay** (100.0% isolated ownership) | Magnitude: 393.78
- `src/ty.rs` -> **David Tolnay** (85.7% isolated ownership) | Magnitude: 370.68
- `src/item.rs` -> **David Tolnay** (88.9% isolated ownership) | Magnitude: 316.26

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

- `codegen/src/gen.rs` -> **Severity: 1365.384** (Blast Radius: 15.809 * Doc Risk: 86.3675%)
- `codegen/src/full.rs` -> **Severity: 937.471** (Blast Radius: 27.622 * Doc Risk: 33.9393%)
- `src/derive.rs` -> **Severity: 694.9** (Blast Radius: 6.949 * Doc Risk: 100.0%)
- `src/export.rs` -> **Severity: 694.9** (Blast Radius: 6.949 * Doc Risk: 100.0%)
- `src/macros.rs` -> **Severity: 694.9** (Blast Radius: 6.949 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
