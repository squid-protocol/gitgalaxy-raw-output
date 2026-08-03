# ARCHITECTURAL_BRIEF: quote
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/quote` |
| **Timestamp** | `2026-08-03T19:44:25.243352+00:00` |
| **Scan Duration** | `0.22s` |
| **Git Branch** | `master` |
| **Git Commit** | `ba07807af385afeff97a5e75186f7a92eb629a79` |
| **Git Remote** | `https://github.com/dtolnay/quote.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 16 malicious artifacts.

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
| Total Artifacts | 37 |
| Analyzed Artifacts (Scanned) | 20 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17 |
| Total LOC | 1386 |
| Volatility Index | 0.05 |
| % Scanned of codebase = | 54.1% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 16 | 1386 | 80.0% |
| PLAINTEXT | 2 | 0 | 10.0% |
| MARKDOWN | 2 | 0 | 10.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.851`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 8 | 40.0% |
| file_cluster_13 | 4 | 20.0% |
| file_cluster_0 | 2 | 10.0% |
| file_cluster_16 | 2 | 10.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 20.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 17*

**Composition by Extension & Reason:**
- `.stderr`: 7x Excluded (Unsupported Extension: '.stderr')
- `.rs`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Unsupported Format (.toml), 1x Excluded (Unsupported Extension: '.toml')
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 35.3 | 12.8 | 7.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 69.8 | 22.0 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 30.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 20.8 | 2.3 | 0.0 |
| API Exposure | 0.0 | 6.1 | 1.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 38.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 96.3 | 13.1 | 0.0 | 0.0 |
| Specification Exposure | 26.7 | 100.0 | 71.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.7 | 0.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 15.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 26.4 | 13.4 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 31.2 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 2.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `benches/timer.rs` (Hits: 1)
- `tests/ui/not-quotable.rs` (Hits: 1)
- `LICENSE-APACHE` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **LICENSE-APACHE** (`LICENSE-APACHE`) — 0 inbound connections
2. **LICENSE-MIT** (`LICENSE-MIT`) — 0 inbound connections
3. **README.md** (`README.md`) — 0 inbound connections
4. **README.md** (`benches/README.md`) — 0 inbound connections
5. **main.rs** (`benches/main.rs`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **runtime.rs** (`src/runtime.rs`) — 27 outbound dependencies
2. **to_tokens.rs** (`src/to_tokens.rs`) — 21 outbound dependencies
3. **lib.rs** (`src/lib.rs`) — 18 outbound dependencies
4. **timer.rs** (`benches/timer.rs`) — 7 outbound dependencies
5. **ext.rs** (`src/ext.rs`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `append_terminated` (@ `src/ext.rs`) -> Impact: **84.4** | LOC: 79
- `respan_token_tree` (@ `src/runtime.rs`) -> Impact: **26.7** | LOC: 14
  * *Intent:* // Token tree with every span replaced by the given one.
- `quote_into_iter` (@ `src/runtime.rs`) -> Impact: **24.5** | LOC: 10
- `fmt` (@ `src/ident_fragment.rs`) -> Impact: **21.2** | LOC: 8
- `to_tokens` (@ `src/to_tokens.rs`) -> Impact: **14.1** | LOC: 5
- `fmt` (@ `src/ident_fragment.rs`) -> Impact: **10.5** | LOC: 3
- `quote` (@ `benches/main.rs`) -> Impact: **8.9** | LOC: 4
- `quote_into_iter` (@ `src/runtime.rs`) -> Impact: **8.2** | LOC: 3
- `quote_into_iter` (@ `src/runtime.rs`) -> Impact: **8.2** | LOC: 3
- `ident_maybe_raw` (@ `src/runtime.rs`) -> Impact: **8.1** | LOC: 7

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `append_terminated` (@ `src/ext.rs`) -> **O(2^N) [Recursive]**
- `fmt` (@ `src/ident_fragment.rs`) -> **O(2^N) [Recursive]**
- `quote` (@ `benches/main.rs`) -> **O(2^N) [Recursive]**
- `respan_token_tree` (@ `src/runtime.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* // Token tree with every span replaced by the given one.
- `fmt` (@ `src/ident_fragment.rs`) -> **O(2^N) [Recursive]**
- `quote_into_iter` (@ `src/runtime.rs`) -> **O(2^N) [Recursive]**
- `quote_into_iter` (@ `src/runtime.rs`) -> **O(2^N) [Recursive]**
- `quote_into_iter` (@ `src/runtime.rs`) -> **O(2^N) [Recursive]**
- `to_tokens` (@ `src/to_tokens.rs`) -> **O(2^N) [Recursive]**
- `span` (@ `src/ident_fragment.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `append_terminated` (@ `src/ext.rs`) -> DB Complexity: **9**
- `respan_token_tree` (@ `src/runtime.rs`) -> DB Complexity: **3**
  * *Intent:* // Token tree with every span replaced by the given one.
- `time` (@ `benches/timer.rs`) -> DB Complexity: **2**
- `push_lifetime_spanned` (@ `src/runtime.rs`) -> DB Complexity: **2**
- `push_group_spanned` (@ `src/runtime.rs`) -> DB Complexity: **2**
- `to_token_stream` (@ `src/to_tokens.rs`) -> DB Complexity: **2**
  * *Intent:* /// trait may be useful for implementing `ToTokens`. /// /// # Example /// /// Example implementation for a struct representing Rust paths like /// `s...
- `fmt` (@ `src/ident_fragment.rs`) -> DB Complexity: **1**
- `fmt` (@ `src/ident_fragment.rs`) -> DB Complexity: **1**
- `fmt` (@ `src/ident_fragment.rs`) -> DB Complexity: **1**
- `fmt` (@ `src/ident_fragment.rs`) -> DB Complexity: **1**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 7 | 882.5 | 20.49% | 58.34% |
| `benches` | 3 | 23.3 | 8.62% | 27.25% |
| `tests/ui` | 7 | 14.52 | 5.0% | 0.0% |
| `__monolith__` | 3 | 9.96 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/ident_fragment.rs` -> **100.0%** Exposure
- `src/runtime.rs` -> **100.0%** Exposure
- `src/spanned.rs` -> **100.0%** Exposure
- `src/to_tokens.rs` -> **100.0%** Exposure
- `benches/main.rs` -> **81.7574%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/lib.rs` -> **99.9911%** Exposure
- `src/ext.rs` -> **99.9144%** Exposure
- `src/to_tokens.rs` -> **99.8375%** Exposure
- `src/ident_fragment.rs` -> **99.714%** Exposure
- `src/runtime.rs` -> **86.8266%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/runtime.rs` -> **9** Orphaned Functions | **26** Duplicates
- `src/to_tokens.rs` -> **0** Orphaned Functions | **35** Duplicates
- `src/ident_fragment.rs` -> **0** Orphaned Functions | **10** Duplicates
- `src/spanned.rs` -> **0** Orphaned Functions | **3** Duplicates
- `benches/main.rs` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/format.rs`** -> AI Confidence: **99.29%**
2. **`src/to_tokens.rs`** -> AI Confidence: **99.16%**
3. **`src/ident_fragment.rs`** -> AI Confidence: **99.15%**
4. **`src/lib.rs`** -> AI Confidence: **99.09%**
5. **`benches/timer.rs`** -> AI Confidence: **99.08%**
6. **`src/ext.rs`** -> AI Confidence: **99.07%**
7. **`src/runtime.rs`** -> AI Confidence: **99.07%**
8. **`src/spanned.rs`** -> AI Confidence: **98.85%**
9. **`benches/main.rs`** -> AI Confidence: **98.84%**
10. **`tests/ui/does-not-have-iter-interpolated-dup.rs`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/ext.rs` -> **20.0%** Exposure
- `src/runtime.rs` -> **20.0%** Exposure
- `src/ident_fragment.rs` -> **4.1235%** Exposure
- `src/to_tokens.rs` -> **0.6264%** Exposure
- `benches/main.rs` -> **0.0598%** Exposure
### Algorithmic DoS Exposure
- `src/ext.rs` -> **100.0%** Exposure
- `src/to_tokens.rs` -> **100.0%** Exposure
- `src/runtime.rs` -> **99.9994%** Exposure
- `src/ident_fragment.rs` -> **99.8677%** Exposure
- `benches/main.rs` -> **72.8241%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `104` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/runtime.rs` (RUST) -> Cumulative Risk: **695.16**
- **Archetype:** `file_cluster_16` (Distance: 11.813 IQR)
- **Magnitude:** 303.92 | **LOC:** 507 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (99.9994%)
- **Heaviest Functions:** `respan_token_tree` (Impact: 26.7), `quote_into_iter` (Impact: 24.5), `quote_into_iter` (Impact: 8.2)

### 2. `src/to_tokens.rs` (RUST) -> Cumulative Risk: **677.57**
- **Archetype:** `file_cluster_13` (Distance: 15.347 IQR)
- **Magnitude:** 180.3 | **LOC:** 282 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.8375%)
- **Heaviest Functions:** `to_tokens` (Impact: 14.1), `to_tokens` (Impact: 8.0), `to_tokens` (Impact: 5.3)

### 3. `src/ident_fragment.rs` (RUST) -> Cumulative Risk: **654.6**
- **Archetype:** `file_cluster_16` (Distance: 13.827 IQR)
- **Magnitude:** 86.76 | **LOC:** 90 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (99.8677%)
- **Heaviest Functions:** `fmt` (Impact: 21.2), `fmt` (Impact: 10.5), `span` (Impact: 5.3)

### 4. `src/ext.rs` (RUST) -> Cumulative Risk: **574.36**
- **Archetype:** `file_cluster_13` (Distance: 15.646 IQR)
- **Magnitude:** 110.26 | **LOC:** 139 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9144%), Verification (80.0%)
- **Heaviest Functions:** `append_terminated` (Impact: 84.4)

### 5. `src/lib.rs` (RUST) -> Cumulative Risk: **436.74**
- **Archetype:** `file_cluster_0` (Distance: 17.786 IQR)
- **Magnitude:** 160.28 | **LOC:** 1478 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 81.8%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), State Flux (99.9911%), Safety Score (56.0447%)

### 6. `src/spanned.rs` (RUST) -> Cumulative Risk: **391.36**
- **Archetype:** `file_cluster_13` (Distance: 10.701 IQR)
- **Magnitude:** 24.98 | **LOC:** 50 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (66.3052%), Documentation (49.1667%)
- **Heaviest Functions:** `__span` (Impact: 7.3), `join_spans` (Impact: 6.5), `__span` (Impact: 2.7)

### 7. `benches/main.rs` (RUST) -> Cumulative Risk: **368.67**
- **Archetype:** `file_cluster_8` (Distance: 7.63 IQR)
- **Magnitude:** 13.3 | **LOC:** 33 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (98.3826%), Tech Debt (81.7574%), Algorithmic Dos (72.8241%)
- **Heaviest Functions:** `quote` (Impact: 8.9), `main` (Impact: 1.9)

### 8. `benches/timer.rs` (RUST) -> Cumulative Risk: **256.19**
- **Archetype:** `file_cluster_13` (Distance: 10.386 IQR)
- **Magnitude:** 9.0 | **LOC:** 18 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (56.6274%), Safety Score (50.0%), Algorithmic Dos (16.9256%)
- **Heaviest Functions:** `time` (Impact: 5.7)

### 9. `src/format.rs` (RUST) -> Cumulative Risk: **254.77**
- **Archetype:** `file_cluster_0` (Distance: 23.386 IQR)
- **Magnitude:** 16.0 | **LOC:** 169 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Dead Code (96.2648%), Churn (32.34%), Documentation (15.8957%)

### 10. `tests/ui/not-quotable.rs` (RUST) -> Cumulative Risk: **45.0**
- **Archetype:** `file_cluster_8` (Distance: 8.167 IQR)
- **Magnitude:** 2.02 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (40.0%), Cognitive Load (5.0%)
- **Heaviest Functions:** `main` (Impact: 1.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/runtime.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.813 IQR)
- **Top Global Matches:** file_cluster_16: 11.813, file_cluster_0: 11.877, file_cluster_13: 11.985
- **Magnitude:** 303.92 | **LOC:** 507 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (11.7966%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `respan_token_tree` (Impact: 26.7 | O(2^N) | DB: 3)
    * *Intent:* // Token tree with every span replaced by the given one.
  * `quote_into_iter` (Impact: 24.5 | O(2^N))
  * `quote_into_iter` (Impact: 8.2 | O(2^N))
  * `quote_into_iter` (Impact: 8.2 | O(2^N))
  * `ident_maybe_raw` (Impact: 8.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 124`, `args: 46`, `func_start: 44`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 45`, `duplicate_logic: 26`, `orphaned_logic: 9`
* *Architecture:* `api: 45`, `import: 17`
* *Defense:* `safety: 16`, `doc: 47`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core::fmt, alloc::format, self::get_span::GetSpan, alloc::vec::Vec, super::HasIterator, alloc::collections::btree_set::self, Spacing, TokenTree...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/to_tokens.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.347 IQR)
- **Top Global Matches:** file_cluster_13: 15.347, file_cluster_11: 15.501, file_cluster_16: 15.545
- **Magnitude:** 180.3 | **LOC:** 282 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (35.3171%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `to_tokens` (Impact: 14.1 | O(2^N) | DB: 1)
  * `to_tokens` (Impact: 8.0 | O(N^2) | DB: 1)
  * `to_tokens` (Impact: 5.3 | O(2^N) | DB: 1)
    * *Intent:* /// if i > 0 || self.global { /// // Double colon `::` /// tokens.append(Punct::new(':', Spacing::Jo...
  * `to_tokens` (Impact: 5.3 | O(2^N) | DB: 1)
  * `to_tokens` (Impact: 5.3 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 85`, `args: 37`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `state_mutation: 43`, `dead_code: 6`, `duplicate_logic: 35`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 9`, `doc: 49`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` alloc::ffi::CString, Span, Spacing, proc_macro2::TokenTree, TokenTree, super::TokenStreamExt, alloc::borrow::Cow, core::ffi::CStr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_0` (Drift: 17.786 IQR)
- **Top Global Matches:** file_cluster_0: 17.786, file_cluster_6: 18.08, file_cluster_17: 18.094
- **Magnitude:** 160.28 | **LOC:** 1478 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 81.8%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (22.5296%), Tech Debt (8.3766%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 120`, `args: 4`
* *Risk/State:* `state_mutation: 136`, `dead_code: 29`, `planned_debt: 1`
* *Architecture:* None
* *Defense:* `safety: 3`, `doc: 552`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ToTokens, proc_macro2::Literal, quote::quote, quote::quote_spanned, proc_macro2::Span, quote, quote::format_ident, proc_macro::TokenStream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ext.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.646 IQR)
- **Top Global Matches:** file_cluster_13: 15.646, file_cluster_16: 15.662, file_cluster_11: 15.872
- **Magnitude:** 110.26 | **LOC:** 139 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (14.9773%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `append_terminated` (Impact: 84.4 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 33`, `args: 11`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 22`, `dead_code: 4`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ToTokens, quote::quote, TokenTree, super::ToTokens, proc_macro2::TokenStream, core::iter, TokenStreamExt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ident_fragment.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.827 IQR)
- **Top Global Matches:** file_cluster_16: 13.827, file_cluster_13: 13.835, file_cluster_8: 14.168
- **Magnitude:** 86.76 | **LOC:** 90 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (34.2258%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `fmt` (Impact: 21.2 | O(2^N) | DB: 1)
  * `fmt` (Impact: 10.5 | O(2^N) | DB: 1)
  * `span` (Impact: 5.3 | O(2^N))
  * `fmt` (Impact: 5.3 | O(2^N) | DB: 1)
  * `span` (Impact: 5.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 20`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 13`, `duplicate_logic: 10`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 15`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core::fmt, ToOwned, alloc::string::String, ToString, alloc::borrow::Cow, Span, proc_macro2::Ident
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/spanned.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.701 IQR)
- **Top Global Matches:** file_cluster_13: 10.701, file_cluster_8: 11.043, file_cluster_16: 11.057
- **Magnitude:** 24.98 | **LOC:** 50 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (18.8232%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__span` (Impact: 7.3 | O(2^N))
  * `join_spans` (Impact: 6.5 | O(N^2) | DB: 1)
  * `__span` (Impact: 2.7 | O(N^2))
  * `__span` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 19`, `args: 8`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 3`, `duplicate_logic: 3`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` proc_macro2::Span, crate::ToTokens, proc_macro2::extra::DelimSpan, TokenStream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/format.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_0` (Drift: 23.386 IQR)
- **Top Global Matches:** file_cluster_0: 23.386, file_cluster_9: 23.536, file_cluster_6: 23.552
- **Magnitude:** 16.0 | **LOC:** 169 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.7533%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`
* *Risk/State:* `dead_code: 11`
* *Architecture:* None
* *Defense:* `safety: 8`, `doc: 110`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` quote::format_ident
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `benches/main.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.63 IQR)
- **Top Global Matches:** file_cluster_8: 7.63, file_cluster_13: 8.131, file_cluster_0: 8.476
- **Magnitude:** 13.3 | **LOC:** 33 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.975%), Tech Debt (81.7574%)
**Top Internal Functions/Classes:**
  * `quote` (Impact: 8.9 | O(2^N))
  * `main` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 3`, `func_start: 2`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` benchmark, proc_macro2::Ident, benchmark::benchmark, Span
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `benches/timer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.386 IQR)
- **Top Global Matches:** file_cluster_13: 10.386, file_cluster_16: 10.754, file_cluster_8: 10.928
- **Magnitude:** 9.0 | **LOC:** 18 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (15.8869%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `time` (Impact: 5.7 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 13`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* `safety: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WriteColor, std::io::Write, ColorSpec, termcolor::Color, StandardStream, ColorChoice, std::time::Instant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 5.42 | **LOC:** 271 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `LICENSE-APACHE` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 3.54 | **LOC:** 177 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ui/does-not-have-iter-interpolated-dup.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.914 IQR)
- **Top Global Matches:** file_cluster_8: 7.914, file_cluster_13: 8.433, file_cluster_7: 9.002
- **Magnitude:** 2.2 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` quote::quote
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ui/does-not-have-iter-interpolated.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.914 IQR)
- **Top Global Matches:** file_cluster_8: 7.914, file_cluster_13: 8.433, file_cluster_7: 9.002
- **Magnitude:** 2.2 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` quote::quote
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ui/wrong-type-span.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.688 IQR)
- **Top Global Matches:** file_cluster_8: 7.688, file_cluster_13: 8.294, file_cluster_7: 8.803
- **Magnitude:** 2.12 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` quote::quote_spanned
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ui/not-quotable.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.167 IQR)
- **Top Global Matches:** file_cluster_8: 8.167, file_cluster_13: 8.291, file_cluster_7: 9.203
- **Magnitude:** 2.02 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `io: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::net::Ipv4Addr, quote::quote
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ui/not-repeatable.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.254 IQR)
- **Top Global Matches:** file_cluster_8: 8.254, file_cluster_13: 8.804, file_cluster_7: 9.298
- **Magnitude:** 2.02 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` quote::quote
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ui/does-not-have-iter-separated.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.181 IQR)
- **Top Global Matches:** file_cluster_8: 8.181, file_cluster_13: 8.61, file_cluster_7: 9.242
- **Magnitude:** 1.98 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` quote::quote
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ui/does-not-have-iter.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.181 IQR)
- **Top Global Matches:** file_cluster_8: 8.181, file_cluster_13: 8.61, file_cluster_7: 9.242
- **Magnitude:** 1.98 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` quote::quote
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `LICENSE-MIT` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 24 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `benches/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 19 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/format.rs` (RUST) | Magnitude: 16.0 | Delta: **0.15 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 110, indent_spaces: 43, dead_code: 11, safety: 8
- `src/lib.rs` (RUST) | Magnitude: 160.28 | Delta: **0.294 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 552, indent_spaces: 429, state_mutation: 136, structural_boundaries: 120

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/ext.rs` (RUST) | Magnitude: 110.26 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 33, doc: 31, generics: 26
- `src/to_tokens.rs` (RUST) | Magnitude: 180.3 | Delta: **0.154 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 117, structural_boundaries: 85, doc: 49, state_mutation: 43
- `src/spanned.rs` (RUST) | Magnitude: 24.98 | Delta: **0.342 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 19, branch: 9, args: 8
- `benches/timer.rs` (RUST) | Magnitude: 9.0 | Delta: **0.368 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 9, generics: 3, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/ident_fragment.rs` (RUST) | Magnitude: 86.76 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 20, safety: 15, generics: 14
- `src/runtime.rs` (RUST) | Magnitude: 303.92 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 255, structural_boundaries: 124, generics: 89, doc: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tests/ui/not-quotable.rs` (RUST) | Magnitude: 2.02 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, import: 2, indent_spaces: 2, args: 1
- `tests/ui/does-not-have-iter-separated.rs` (RUST) | Magnitude: 1.98 | Delta: **0.429 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, import: 1
- `tests/ui/does-not-have-iter.rs` (RUST) | Magnitude: 1.98 | Delta: **0.429 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, import: 1
- `benches/main.rs` (RUST) | Magnitude: 13.3 | Delta: **0.501 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 7, args: 3, import: 3
- `tests/ui/does-not-have-iter-interpolated-dup.rs` (RUST) | Magnitude: 2.2 | Delta: **0.519 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, indent_spaces: 2, args: 1, func_start: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/to_tokens.rs` -> Churn: **50.29%** | Cog Load: 35.3171% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/lib.rs` -> **David Tolnay** (81.8% isolated ownership) | Magnitude: 160.28
- `src/ident_fragment.rs` -> **Tamir Duberstein** (100.0% isolated ownership) | Magnitude: 86.76

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/ident_fragment.rs` -> **Severity: 5000.0** (Blast Radius: 50.0 * Doc Risk: 100.0%)
- `src/runtime.rs` -> **Severity: 5000.0** (Blast Radius: 50.0 * Doc Risk: 100.0%)
- `benches/main.rs` -> **Severity: 4919.13** (Blast Radius: 50.0 * Doc Risk: 98.3826%)
- `src/spanned.rs` -> **Severity: 2458.335** (Blast Radius: 50.0 * Doc Risk: 49.1667%)
- `src/lib.rs` -> **Severity: 839.785** (Blast Radius: 50.0 * Doc Risk: 16.7957%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
