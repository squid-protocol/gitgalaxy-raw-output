# ARCHITECTURAL_BRIEF: blst
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/blst` |
| **Timestamp** | `2026-08-03T19:26:47.274798+00:00` |
| **Scan Duration** | `0.73s` |
| **Git Branch** | `master` |
| **Git Commit** | `f62244ef50ad1a603decdb8f215e982d2a467bb6` |
| **Git Remote** | `https://github.com/supranational/blst.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 62 malicious artifacts.

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
| Total Artifacts | 247 |
| Analyzed Artifacts (Scanned) | 102 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 145 |
| Total LOC | 34100 |
| Volatility Index | 0.01 |
| % Scanned of codebase = | 41.3% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3246 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5238 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3819 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 7 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 39 | 8406 | 38.2% |
| PERL | 25 | 18250 | 24.5% |
| JSON | 7 | 573 | 6.9% |
| MARKDOWN | 6 | 0 | 5.9% |
| RUST | 5 | 3124 | 4.9% |
| PYTHON | 4 | 257 | 3.9% |
| GO | 3 | 1837 | 2.9% |
| CPP | 2 | 1147 | 2.0% |
| JAVASCRIPT | 2 | 21 | 2.0% |
| TYPESCRIPT | 2 | 220 | 2.0% |
| CSHARP | 1 | 60 | 1.0% |
| HTML | 1 | 43 | 1.0% |
| ASSEMBLY | 1 | 0 | 1.0% |
| MAKEFILE | 1 | 19 | 1.0% |
| JAVA | 1 | 50 | 1.0% |
| SHELL | 1 | 8 | 1.0% |
| ZIG | 1 | 85 | 1.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.157`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 84 | 82.4% |
| file_cluster_13 | 7 | 6.9% |
| file_cluster_0 | 3 | 2.9% |
| file_cluster_11 | 1 | 1.0% |
| file_cluster_17 | 1 | 1.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 5.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 145*

**Composition by Extension & Reason:**
- `.s`: 79x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.asm`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.me`: 5x Excluded (Unsupported Extension: '.me')
- `.go`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tgo`: 4x Unsupported Format (.tgo)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zig`: 1x Excluded (Machine-Generated Source Code Signature: 608 LOC), 1x Excluded (Machine-Generated Source Code Signature: 508 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.rs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1416 LOC)
- `.swg`: 1x Excluded (Unsupported Extension: '.swg')
- `.csproj`: 1x Excluded (Unsupported Extension: '.csproj')
- `.cs`: 1x Excluded (Machine-Generated Source Code Signature: 1016 LOC)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 97.3 | 34.6 | 21.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 30.3 | 13.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 12.0 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 24.1 | 2.3 | 2.3 |
| API Exposure | 0.0 | 17.3 | 4.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 30.9 | 0.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 61.5 | 94.6 | 0.0 |
| Commented Logic Exposure | 0.0 | 20.6 | 1.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 10.6 | 1.6 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 100.0 | 53.2 | 32.8 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 35.3 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 13.2 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.1 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `bindings/go/generate.py` (Hits: 19)
- `bindings/zig/generate.py` (Hits: 15)
- `bindings/node.js/blst_wrap.py` (Hits: 13)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **fields.h** (`src/fields.h`) — 12 inbound connections
2. **point.h** (`src/point.h`) — 8 inbound connections
3. **vect.h** (`src/vect.h`) — 7 inbound connections
4. **bytes.h** (`src/bytes.h`) — 5 inbound connections
5. **consts.h** (`src/consts.h`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`bindings/rust/src/lib.rs`) — 22 outbound dependencies
2. **server.c** (`src/server.c`) — 20 outbound dependencies
3. **x86_64-xlate.pl** (`src/asm/x86_64-xlate.pl`) — 13 outbound dependencies
4. **client_min_pk.c** (`src/client_min_pk.c`) — 11 outbound dependencies
5. **client_min_sig.c** (`src/client_min_sig.c`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `joined_execute` (@ `bindings/rust/src/lib.rs`) -> Impact: **2947.8** | LOC: 1556
- `size` (@ `src/asm/x86_64-xlate.pl`) -> Impact: **463.5** | LOC: 559
- `mult` (@ `bindings/rust/src/pippenger.rs`) -> Impact: **429.6** | LOC: 193
- `re` (@ `src/asm/x86_64-xlate.pl`) -> Impact: **409.6** | LOC: 346
- `body_00_15` (@ `src/asm/sha256-x86_64.pl`) -> Impact: **329.0** | LOC: 523
- `ret` (@ `src/asm/add_mod_384-x86_64.pl`) -> Impact: **177.7** | LOC: 189
- `vec_select` (@ `src/vect.h`) -> Impact: **138.7** | LOC: 30
- `add` (@ `bindings/rust/src/pippenger.rs`) -> Impact: **124.0** | LOC: 55
- `insert` (@ `bindings/go/rb_tree.go`) -> Impact: **120.5** | LOC: 83
- `sqr_mont_382x` (@ `src/no_asm.h`) -> Impact: **104.3** | LOC: 268

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `mult_pippenger` (@ `bindings/blst.hpp`) -> **O(2^N) [Recursive]**
  * *Intent:* #endif
- `mult_pippenger` (@ `bindings/blst.hpp`) -> **O(2^N) [Recursive]**
  * *Intent:* #endif
- `mult_pippenger` (@ `bindings/blst.hpp`) -> **O(2^N) [Recursive]**
- `mult_pippenger` (@ `bindings/blst.hpp`) -> **O(2^N) [Recursive]**
- `joined_execute` (@ `bindings/rust/src/lib.rs`) -> **O(2^N) [Recursive]**
- `mult` (@ `bindings/rust/src/lib.rs`) -> **O(2^N) [Recursive]**
- `mult` (@ `bindings/rust/src/lib.rs`) -> **O(2^N) [Recursive]**
- `add` (@ `bindings/rust/src/lib.rs`) -> **O(2^N) [Recursive]**
- `add` (@ `bindings/rust/src/lib.rs`) -> **O(2^N) [Recursive]**
- `mult` (@ `bindings/rust/src/pippenger.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `size` (@ `src/asm/x86_64-xlate.pl`) -> DB Complexity: **147**
- `sqr_mont_382x` (@ `src/no_asm.h`) -> DB Complexity: **141**
- `body_00_15` (@ `src/asm/sha256-x86_64.pl`) -> DB Complexity: **139**
- `re` (@ `src/asm/x86_64-xlate.pl`) -> DB Complexity: **136**
- `joined_execute` (@ `bindings/rust/src/lib.rs`) -> DB Complexity: **107**
- `AUTOLOAD` (@ `src/asm/sha256-armv8.pl`) -> DB Complexity: **92**
- `mul_mont_n` (@ `src/no_asm.h`) -> DB Complexity: **43**
  * *Intent:* #if !defined(__STDC_VERSION__) || __STDC_VERSION__<199901 || defined(__STDC_NO_VLA__) # error "unsupported compiler" #endif #if defined(__clang__) # p...
- `mul_by_3_mod_n` (@ `src/no_asm.h`) -> DB Complexity: **32**
  * *Intent:* #define SUB_MOD_IMPL(bits) \
- `mult` (@ `bindings/rust/src/pippenger.rs`) -> DB Complexity: **30**
- `redc_mont_n` (@ `src/no_asm.h`) -> DB Complexity: **29**
  * *Intent:* #define FROM_MONT_IMPL(bits) \

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/asm` | 25 | 15495.95 | 38.22% | 3.12% |
| `src` | 37 | 8867.34 | 43.56% | 7.9% |
| `bindings/rust/src` | 4 | 4836.36 | 46.51% | 68.89% |
| `bindings/go` | 7 | 2732.52 | 21.67% | 17.11% |
| `bindings` | 3 | 1482.4 | 28.08% | 33.33% |
| `bindings/rust/benches` | 1 | 380.32 | 26.89% | 0.0% |
| `bindings/c#` | 1 | 107.6 | 11.92% | 0.0% |
| `bindings/vectors/hash_to_curve` | 7 | 102.32 | 0.0% | 0.0% |
| `bindings/java` | 2 | 92.48 | 36.68% | 48.53% |
| `bindings/node.js` | 6 | 67.4 | 11.76% | 15.25% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `bindings/blst.hpp` -> **100.0%** Exposure
- `src/blst_t.hpp` -> **100.0%** Exposure
- `bindings/go/blst.go` -> **100.0%** Exposure
- `bindings/rust/publish.sh` -> **100.0%** Exposure
- `bindings/rust/src/pippenger-no_std.rs` -> **99.8629%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/bulk_addition.c` -> **100.0%** Exposure
- `src/bytes.h` -> **100.0%** Exposure
- `src/cpuid.c` -> **100.0%** Exposure
- `src/ec_mult.h` -> **100.0%** Exposure
- `src/exp.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `bindings/blst.hpp` -> **0** Orphaned Functions | **184** Duplicates
- `bindings/go/blst.go` -> **0** Orphaned Functions | **80** Duplicates
- `src/blst_t.hpp` -> **20** Orphaned Functions | **17** Duplicates
- `bindings/rust/src/lib.rs` -> **8** Orphaned Functions | **10** Duplicates
- `src/asm/x86_64-xlate.pl` -> **0** Orphaned Functions | **9** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`bindings/go/blst.go`** -> AI Confidence: **99.25%**
2. **`src/exp.c`** -> AI Confidence: **99.23%**
3. **`src/pentaroot-addchain.h`** -> AI Confidence: **99.23%**
4. **`src/recip-addchain.h`** -> AI Confidence: **99.23%**
5. **`src/sqrt-addchain.h`** -> AI Confidence: **99.23%**
6. **`bindings/rust/src/lib.rs`** -> AI Confidence: **99.16%**
7. **`bindings/go/generate.py`** -> AI Confidence: **99.13%**
8. **`bindings/node.js/blst_wrap.py`** -> AI Confidence: **99.13%**
9. **`src/bulk_addition.c`** -> AI Confidence: **99.1%**
10. **`src/multi_scalar.c`** -> AI Confidence: **99.1%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `bindings/go/rb_tree.go` -> **100.0%** Exposure
- `bindings/zig/generate.py` -> **100.0%** Exposure
- `src/asm/add_mod_384-x86_64.pl` -> **100.0%** Exposure
- `src/asm/sha256-x86_64.pl` -> **100.0%** Exposure
- `src/asm/x86_64-xlate.pl` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `bindings/go/generate.py` -> **100.0%** Exposure
- `bindings/zig/generate.py` -> **100.0%** Exposure
- `src/asm/sha256-portable-x86_64.pl` -> **100.0%** Exposure
- `src/asm/sha256-armv8.pl` -> **4.1038%** Exposure
- `src/asm/sha256-x86_64.pl` -> **0.1007%** Exposure
### Raw Memory Manipulation
- `src/aggregate.c` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `src/aggregate.c` -> **100.0%** Exposure
- `src/bytes.h` -> **100.0%** Exposure
- `src/e1.c` -> **100.0%** Exposure
- `src/e2.c` -> **100.0%** Exposure
- `src/exp.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `202` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `bindings/blst.hpp` (CPP) -> Cumulative Risk: **814.02**
- **Archetype:** `file_cluster_8` (Distance: 13.135 IQR)
- **Magnitude:** 1255.78 | **LOC:** 959 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `finalverify` (Impact: 17.3), `mult_pippenger` (Impact: 15.9), `mult_pippenger` (Impact: 15.9)

### 2. `src/blst_t.hpp` (CPP) -> Cumulative Risk: **787.68**
- **Archetype:** `file_cluster_8` (Distance: 13.27 IQR)
- **Magnitude:** 428.86 | **LOC:** 673 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `operator^` (Impact: 31.2), `operator^=` (Impact: 14.4), `vec_left_align` (Impact: 11.0)

### 3. `bindings/rust/src/pippenger.rs` (RUST) -> Cumulative Risk: **783.5**
- **Archetype:** `file_cluster_8` (Distance: 11.415 IQR)
- **Magnitude:** 935.44 | **LOC:** 549 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.9788%)
- **Heaviest Functions:** `mult` (Impact: 429.6), `add` (Impact: 124.0), `validate` (Impact: 99.9)

### 4. `bindings/go/rb_tree.go` (GO) -> Cumulative Risk: **753.69**
- **Archetype:** `file_cluster_8` (Distance: 12.432 IQR)
- **Magnitude:** 243.32 | **LOC:** 154 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `insert` (Impact: 120.5), `Uniq` (Impact: 25.0)

### 5. `src/asm/x86_64-xlate.pl` (PERL) -> Cumulative Risk: **752.64**
- **Archetype:** `file_cluster_8` (Distance: 14.623 IQR)
- **Magnitude:** 2501.92 | **LOC:** 1974 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `size` (Impact: 463.5), `re` (Impact: 409.6), `out` (Impact: 74.6)

### 6. `src/exports.c` (C) -> Cumulative Risk: **705.79**
- **Archetype:** `file_cluster_8` (Distance: 13.588 IQR)
- **Magnitude:** 777.96 | **LOC:** 621 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `blst_uint64_from_fr` (Impact: 18.3), `blst_uint64_from_fp` (Impact: 18.2), `blst_sk_inverse` (Impact: 15.2)

### 7. `bindings/rust/src/lib.rs` (RUST) -> Cumulative Risk: **697.46**
- **Archetype:** `file_cluster_0` (Distance: 12.538 IQR)
- **Magnitude:** 3762.34 | **LOC:** 2386 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (97.2082%)
- **Heaviest Functions:** `joined_execute` (Impact: 2947.8), `aggregate_serialized` (Impact: 78.5), `test_multiple_agg_sigs` (Impact: 54.8)

### 8. `src/keygen.c` (C) -> Cumulative Risk: **690.9**
- **Archetype:** `file_cluster_8` (Distance: 13.468 IQR)
- **Magnitude:** 387.1 | **LOC:** 320 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `HKDF_Expand` (Impact: 81.2), `keygen` (Impact: 41.9), `HKDF_Extract` (Impact: 30.7)

### 9. `src/rb_tree.c` (C) -> Cumulative Risk: **690.66**
- **Archetype:** `file_cluster_13` (Distance: 15.441 IQR)
- **Magnitude:** 239.36 | **LOC:** 146 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9998%)
- **Heaviest Functions:** `rb_tree_insert` (Impact: 73.5), `bytes_compare` (Impact: 32.0), `blst_uniq_init` (Impact: 2.2)

### 10. `src/e1.c` (C) -> Cumulative Risk: **689.78**
- **Archetype:** `file_cluster_8` (Distance: 11.779 IQR)
- **Magnitude:** 580.8 | **LOC:** 565 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.4226%)
- **Heaviest Functions:** `blst_p1_mult` (Impact: 36.5), `POINTonE1_Uncompress_Z` (Impact: 26.1), `blst_sign_pk2_in_g2` (Impact: 24.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/asm/arm-xlate.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.798 IQR)
- **Top Global Matches:** file_cluster_0: 14.798, file_cluster_11: 14.876, file_cluster_8: 14.952
- **Magnitude:** 8186.14 | **LOC:** 516 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (87.3113%), Tech Debt (20.8232%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 100`, `args: 17`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 699`, `dead_code: 3`, `fragile_debt: 2`
* *Architecture:* `io: 4`, `import: 1`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/rust/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.538 IQR)
- **Top Global Matches:** file_cluster_0: 12.538, file_cluster_8: 12.608, file_cluster_17: 12.694
- **Magnitude:** 3762.34 | **LOC:** 2386 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 107
- **Risk Profile:** Cognitive Load (38.7541%), Tech Debt (56.1665%)
**Top Internal Functions/Classes:**
  * `joined_execute` (Impact: 2947.8 | O(2^N) | DB: 107)
  * `aggregate_serialized` (Impact: 78.5 | O(N^6) | DB: 3)
  * `test_multiple_agg_sigs` (Impact: 54.8 | O(N^5) | DB: 11)
  * `aggregate_with_randomness` (Impact: 30.1 | O(N^5))
  * `miller_loop_n` (Impact: 28.2 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 514`, `args: 174`, `func_start: 128`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 2`, `state_mutation: 312`, `dead_code: 2`, `planned_debt: 9`, `duplicate_logic: 10`, `orphaned_logic: 8`
* *Architecture:* `api: 86`, `concurrency: 5`, `import: 23`
* *Defense:* `safety: 155`, `doc: 2`, `test: 53`, `sync_locks: 5`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rand_chacha::ChaCha20Rng, std::sync::Mutex, MaybeUninit, core::any::Any, Deserializer, threadpool::ThreadPool, Once, SeedableRng...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/asm/x86_64-xlate.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.623 IQR)
- **Top Global Matches:** file_cluster_8: 14.623, file_cluster_0: 14.74, file_cluster_11: 14.744
- **Magnitude:** 2501.92 | **LOC:** 1974 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 147
- **Risk Profile:** Cognitive Load (97.2795%), Tech Debt (57.0826%)
**Top Internal Functions/Classes:**
  * `size` (Impact: 463.5 | O(N^3) | DB: 147)
  * `re` (Impact: 409.6 | O(N^2) | DB: 136)
  * `out` (Impact: 74.6 | O(N^1) | DB: 21)
  * `out` (Impact: 34.4 | O(N^1) | DB: 18)
  * `re` (Impact: 21.0 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 538`, `structural_boundaries: 286`, `args: 44`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 2`, `state_mutation: 1421`, `dead_code: 6`, `planned_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `io: 4`, `import: 5`
* *Defense:* `safety: 1`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DWP_OP_reg, warnings, dynamic, integer, occasion, non, following, even...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/go/blst.go` (GO | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.055 IQR)
- **Top Global Matches:** file_cluster_11: 15.055, file_cluster_4: 15.066, file_cluster_12: 15.109
- **Magnitude:** 2402.6 | **LOC:** 3631 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (49.9024%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `coreAggregateVerifyPkInG1` (Impact: 87.4 | O(N^1) | DB: 28)
  * `coreAggregateVerifyPkInG2` (Impact: 87.4 | O(N^1) | DB: 28)
  * `coreAggregate` (Impact: 58.4 | O(N^1) | DB: 26)
  * `coreAggregate` (Impact: 58.4 | O(N^1) | DB: 26)
  * `multipleAggregateVerifyPkInG1` (Impact: 55.0 | O(N^1) | DB: 21)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 381`, `structural_boundaries: 319`, `args: 132`, `func_start: 132`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1043`, `dead_code: 24`, `planned_debt: 2`, `duplicate_logic: 80`
* *Architecture:* `api: 171`, `concurrency: 96`, `import: 2`
* *Defense:* `safety: 3`, `doc: 89`, `sync_locks: 67`, `immutability_locks: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sync, C, runtime, atomic, unsafe, bits, fmt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/no_asm.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.129 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 4.519 IQR)
- **Top Global Matches:** file_cluster_8: 15.129, file_cluster_11: 15.265, file_cluster_0: 15.274
- **Magnitude:** 1584.28 | **LOC:** 1346 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 141
- **Risk Profile:** Cognitive Load (63.6514%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sqr_mont_382x` (Impact: 104.3 | O(N^6) | DB: 141)
  * `mul_mont_n` (Impact: 32.7 | O(N^5) | DB: 43)
    * *Intent:* #if !defined(__STDC_VERSION__) || __STDC_VERSION__<199901 || defined(__STDC_NO_VLA__) # error "unsup...
  * `mul_mont_nonred_n` (Impact: 30.0 | O(N^6) | DB: 28)
  * `mul_by_3_mod_n` (Impact: 26.7 | O(N^6) | DB: 32)
    * *Intent:* #define SUB_MOD_IMPL(bits) \
  * `redc_mont_n` (Impact: 26.5 | O(N^6) | DB: 29)
    * *Intent:* #define FROM_MONT_IMPL(bits) \
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 52`, `args: 5`, `func_start: 30`
* *Risk/State:* `state_mutation: 1076`, `dead_code: 1`
* *Architecture:* `api: 141`
* *Defense:* `safety: 42`, `immutability_locks: 96`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.509
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.024752
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bindings/blst.hpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.135 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 6.883 IQR)
- **Top Global Matches:** file_cluster_8: 13.135, file_cluster_13: 13.441, file_cluster_0: 13.556
- **Magnitude:** 1255.78 | **LOC:** 959 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (74.1741%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `finalverify` (Impact: 17.3 | O(N^6) | DB: 1)
  * `mult_pippenger` (Impact: 15.9 | O(2^N) | DB: 1)
    * *Intent:* #endif
  * `mult_pippenger` (Impact: 15.9 | O(2^N) | DB: 1)
    * *Intent:* #endif
  * `mult_pippenger` (Impact: 14.2 | O(2^N) | DB: 2)
  * `mult_pippenger` (Impact: 14.2 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 244`, `args: 113`, `func_start: 209`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 6`, `state_mutation: 512`, `duplicate_logic: 184`
* *Architecture:* `api: 27`, `import: 5`
* *Defense:* `safety: 8`, `immutability_locks: 368`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vector, string, blst.h, memory, cstring
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/rust/src/pippenger.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.415 IQR)
- **Top Global Matches:** file_cluster_8: 11.415, file_cluster_0: 11.553, file_cluster_13: 11.692
- **Magnitude:** 935.44 | **LOC:** 549 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (80.6921%), Tech Debt (60.7069%)
**Top Internal Functions/Classes:**
  * `mult` (Impact: 429.6 | O(2^N) | DB: 30)
  * `add` (Impact: 124.0 | O(2^N) | DB: 10)
  * `validate` (Impact: 99.9 | O(N^6) | DB: 3)
  * `breakdown` (Impact: 46.5 | O(N^4) | DB: 2)
  * `from` (Impact: 44.1 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 172`, `args: 21`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 134`, `duplicate_logic: 4`, `orphaned_logic: 4`
* *Architecture:* `api: 6`, `concurrency: 12`, `import: 4`
* *Defense:* `safety: 16`, `test: 2`, `sync_locks: 3`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core::slice::SliceIndex, std::sync::Barrier, core::num::Wrapping, IndexMut, core::ops::Index
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/exports.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.79%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.588 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.001 IQR)
- **Top Global Matches:** file_cluster_8: 13.588, file_cluster_13: 13.758, file_cluster_0: 13.788
- **Magnitude:** 777.96 | **LOC:** 621 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (85.0794%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `blst_uint64_from_fr` (Impact: 18.3 | O(N^3) | DB: 4)
  * `blst_uint64_from_fp` (Impact: 18.2 | O(N^3) | DB: 4)
  * `blst_sk_inverse` (Impact: 15.2 | O(N^6) | DB: 2)
  * `blst_fr_from_scalar` (Impact: 14.8 | O(N^6) | DB: 1)
  * `blst_uint32_from_fp` (Impact: 14.7 | O(N^3) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 85`, `args: 10`, `func_start: 64`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 313`
* *Architecture:* `api: 209`, `import: 3`
* *Defense:* `safety: 23`, `immutability_locks: 100`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.503
  * `Choke Point (Betweenness):` 0.00038 | `Ripple Effect (Closeness):` 0.031683
  * `Imports (Out-Degree: 3):` bytes.h, sha256.h, fields.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/asm/sha256-portable-x86_64.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.959 IQR)
- **Top Global Matches:** file_cluster_8: 10.959, file_cluster_0: 11.424, file_cluster_7: 11.585
- **Magnitude:** 651.63 | **LOC:** 343 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (70.5603%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 4`, `args: 5`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 15`, `state_mutation: 90`
* *Architecture:* `io: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/aggregate.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.069 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.499 IQR)
- **Top Global Matches:** file_cluster_8: 13.069, file_cluster_0: 13.13, file_cluster_9: 13.281
- **Magnitude:** 649.06 | **LOC:** 674 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (84.7965%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `PAIRING_Aggregate_PK_in_G2` (Impact: 92.1 | O(N^6) | DB: 10)
  * `blst_pairing_merge` (Impact: 83.0 | O(N^6) | DB: 4)
  * `PAIRING_FinalVerify` (Impact: 44.0 | O(N^6))
  * `blst_aggregate_in_g1` (Impact: 25.9 | O(N^6) | DB: 1)
  * `blst_aggregate_in_g2` (Impact: 25.9 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 69`, `args: 1`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 117`, `dead_code: 2`
* *Architecture:* `api: 150`
* *Defense:* `safety: 30`, `immutability_locks: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.438
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.013201
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/asm/sha256-x86_64.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.091 IQR)
- **Top Global Matches:** file_cluster_8: 12.091, file_cluster_0: 12.577, file_cluster_7: 12.583
- **Magnitude:** 648.16 | **LOC:** 808 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 139
- **Risk Profile:** Cognitive Load (58.7902%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `body_00_15` (Impact: 329.0 | O(2^N) | DB: 139)
  * `AUTOLOAD` (Impact: 7.2 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 24`, `args: 115`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 109`, `high_risk_execution: 3`, `state_mutation: 298`, `dead_code: 1`
* *Architecture:* `io: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` scalar
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/e2.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.48 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.899 IQR)
- **Top Global Matches:** file_cluster_8: 11.48, file_cluster_13: 11.841, file_cluster_7: 11.959
- **Magnitude:** 590.54 | **LOC:** 639 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (52.446%), Tech Debt (95.8783%)
**Top Internal Functions/Classes:**
  * `blst_p2_mult` (Impact: 36.5 | O(N^6) | DB: 8)
  * `blst_sign_pk2_in_g1` (Impact: 24.2 | O(N^6) | DB: 3)
  * `POINTonE2_Deserialize_BE` (Impact: 23.1 | O(N^6) | DB: 1)
  * `POINTonE2_Uncompress_Z` (Impact: 22.4 | O(N^6) | DB: 3)
  * `blst_sk_to_pk2_in_g2` (Impact: 21.7 | O(N^6) | DB: 3)
    * *Intent:* #ifndef FUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION flt_reciprocal_fp2(Z, out->Z); /* 1/Z */ #else reci...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 73`, `args: 15`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `state_mutation: 112`, `fragile_debt: 18`
* *Architecture:* `api: 137`, `import: 5`
* *Defense:* `safety: 7`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.503
  * `Choke Point (Betweenness):` 0.000738 | `Ripple Effect (Closeness):` 0.031683
  * `Imports (Out-Degree: 5):` fields.h, ec_ops.h, errors.h, point.h, ec_mult.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/e1.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.779 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.978 IQR)
- **Top Global Matches:** file_cluster_8: 11.779, file_cluster_13: 12.067, file_cluster_7: 12.239
- **Magnitude:** 580.8 | **LOC:** 565 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (63.4704%), Tech Debt (96.5555%)
**Top Internal Functions/Classes:**
  * `blst_p1_mult` (Impact: 36.5 | O(N^6) | DB: 8)
  * `POINTonE1_Uncompress_Z` (Impact: 26.1 | O(N^6) | DB: 3)
  * `blst_sign_pk2_in_g2` (Impact: 24.2 | O(N^6) | DB: 3)
  * `blst_sk_to_pk2_in_g1` (Impact: 21.7 | O(N^6) | DB: 3)
    * *Intent:* mul_fp(out->Y, out->Y, ZZ); /* Y = Y/Z^3 */
  * `POINTonE1_Deserialize_BE` (Impact: 19.1 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 70`, `args: 15`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `state_mutation: 111`, `fragile_debt: 16`
* *Architecture:* `api: 136`, `import: 5`
* *Defense:* `safety: 7`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.503
  * `Choke Point (Betweenness):` 0.000738 | `Ripple Effect (Closeness):` 0.031683
  * `Imports (Out-Degree: 5):` fields.h, ec_ops.h, errors.h, point.h, ec_mult.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/multi_scalar.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.1%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.362 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.584 IQR)
- **Top Global Matches:** file_cluster_8: 15.362, file_cluster_0: 15.442, file_cluster_13: 15.45
- **Magnitude:** 565.54 | **LOC:** 475 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (70.4375%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pippenger_window_size` (Impact: 12.8 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 25`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 464`
* *Architecture:* `api: 81`, `import: 2`
* *Defense:* `safety: 62`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.438
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.013201
  * `Imports (Out-Degree: 2):` point.h, fields.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/asm/add_mod_384-x86_64.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.894 IQR)
- **Top Global Matches:** file_cluster_8: 10.894, file_cluster_7: 11.507, file_cluster_1: 11.744
- **Magnitude:** 524.28 | **LOC:** 1567 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (26.695%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ret` (Impact: 177.7 | O(2^N) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 13`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 319`
* *Architecture:* `io: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/vect.h` (C | Tier 0 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.805 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.179 IQR)
- **Top Global Matches:** file_cluster_13: 13.805, file_cluster_8: 13.815, file_cluster_0: 13.912
- **Magnitude:** 517.9 | **LOC:** 432 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (62.5554%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `vec_select` (Impact: 138.7 | O(N^6) | DB: 10)
  * `vec_cswap` (Impact: 16.6 | O(N^6) | DB: 11)
    * *Intent:* # elif defined(_MSC_VER) # define restrict __restrict # else # define restrict # endif # endif #endi...
  * `vec_zero` (Impact: 10.9 | O(N^2) | DB: 5)
  * `vec_is_equal` (Impact: 10.0 | O(N^2) | DB: 7)
  * `vec_is_zero` (Impact: 8.7 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 114`, `args: 18`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 162`
* *Architecture:* `api: 137`, `import: 4`
* *Defense:* `safety: 28`, `immutability_locks: 168`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 100.931
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.150371
  * `Imports (Out-Degree: 0):` stdlib.h, malloc.h, stddef.h, alloca.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/asm/mulx_mont_384-x86_64.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.668 IQR)
- **Top Global Matches:** file_cluster_8: 10.668, file_cluster_7: 11.363, file_cluster_1: 11.584
- **Magnitude:** 438.78 | **LOC:** 2487 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (19.6422%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 32`, `args: 5`
* *Risk/State:* `state_mutation: 382`
* *Architecture:* `io: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/asm/mulq_mont_384-x86_64.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.531 IQR)
- **Top Global Matches:** file_cluster_8: 10.531, file_cluster_7: 11.212, file_cluster_1: 11.452
- **Magnitude:** 431.46 | **LOC:** 2755 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.2507%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 31`, `args: 14`
* *Risk/State:* `state_mutation: 370`
* *Architecture:* `io: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/blst_t.hpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.27 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.439 IQR)
- **Top Global Matches:** file_cluster_8: 13.27, file_cluster_13: 13.48, file_cluster_11: 13.614
- **Magnitude:** 428.86 | **LOC:** 673 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (78.8232%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `operator^` (Impact: 31.2 | O(N^5) | DB: 10)
  * `operator^=` (Impact: 14.4 | O(N^3) | DB: 3)
  * `vec_left_align` (Impact: 11.0 | O(N^3) | DB: 12)
    * *Intent:* #include "bytes.h" #undef launder // avoid conflict with C++ >=17 #ifdef __GNUC__
  * `to_scalar` (Impact: 8.8 | O(N^3) | DB: 4)
  * `one` (Impact: 7.3 | O(N^3) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 115`, `args: 12`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 259`, `duplicate_logic: 17`, `orphaned_logic: 20`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bytes.h, cstdint, vect.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/keygen.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.91%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.468 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.24 IQR)
- **Top Global Matches:** file_cluster_8: 13.468, file_cluster_13: 13.574, file_cluster_0: 13.706
- **Magnitude:** 387.1 | **LOC:** 320 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (85.8933%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `HKDF_Expand` (Impact: 81.2 | O(N^6) | DB: 8)
  * `keygen` (Impact: 41.9 | O(N^6) | DB: 8)
  * `HKDF_Extract` (Impact: 30.7 | O(N^6) | DB: 1)
  * `parent_SK_to_lamport_PK` (Impact: 21.0 | O(N^6) | DB: 16)
  * `HMAC_init` (Impact: 12.5 | O(N^2) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 38`, `args: 3`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 120`
* *Architecture:* `api: 50`, `import: 3`
* *Defense:* `safety: 22`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.503
  * `Choke Point (Betweenness):` 0.000462 | `Ripple Effect (Closeness):` 0.031683
  * `Imports (Out-Degree: 3):` bytes.h, consts.h, sha256.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/asm/sha256-armv8.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.437 IQR)
- **Top Global Matches:** file_cluster_8: 12.437, file_cluster_0: 12.828, file_cluster_17: 12.898
- **Magnitude:** 384.48 | **LOC:** 555 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 92
- **Risk Profile:** Cognitive Load (64.0193%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `body_00_15` (Impact: 82.5 | O(2^N) | DB: 2)
  * `AUTOLOAD` (Impact: 38.4 | O(2^N) | DB: 92)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 25`, `args: 89`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 77`, `high_risk_execution: 1`, `state_mutation: 254`
* *Architecture:* `io: 6`, `import: 2`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` integer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/rust/benches/blst_benches.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.504 IQR)
- **Top Global Matches:** file_cluster_17: 11.504, file_cluster_8: 11.507, file_cluster_13: 11.858
- **Magnitude:** 380.32 | **LOC:** 479 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (26.8941%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bench_serdes` (Impact: 72.3 | O(N^3) | DB: 12)
  * `bench_verify_multi_aggregate` (Impact: 67.3 | O(N^6) | DB: 12)
  * `bench_fast_aggregate_verify` (Impact: 66.1 | O(N^6) | DB: 6)
  * `bench_aggregate_verify` (Impact: 36.2 | O(N^5) | DB: 4)
  * `bench_aggregate` (Impact: 24.5 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 154`, `args: 77`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 74`
* *Architecture:* `import: 5`
* *Defense:* `safety: 15`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Criterion, criterion::criterion_group, rand_chacha::ChaCha20Rng, SeedableRng, blst::min_pk::*, blst::*, rand::RngCore, BenchmarkId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ec_mult.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.213 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.228 IQR)
- **Top Global Matches:** file_cluster_8: 14.213, file_cluster_13: 14.462, file_cluster_0: 14.478
- **Magnitude:** 316.92 | **LOC:** 316 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (57.4156%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_wval_limb` (Impact: 3.9 | O(N^2) | DB: 10)
  * `booth_encode` (Impact: 1.6 | O(N^1) | DB: 3)
  * `get_wval` (Impact: 1.4 | O(N^1) | DB: 2)
    * *Intent:* /* * Copyright Supranational LLC * Licensed under the Apache License, Version 2.0, see LICENSE for d...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 11`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 266`
* *Architecture:* `api: 39`, `import: 1`
* *Defense:* `safety: 17`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.032403
  * `Imports (Out-Degree: 1):` point.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/bytes.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.012 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.416 IQR)
- **Top Global Matches:** file_cluster_8: 15.012, file_cluster_0: 15.12, file_cluster_9: 15.205
- **Magnitude:** 266.68 | **LOC:** 153 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (63.4303%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `le_bytes_from_limbs` (Impact: 50.2 | O(N^6) | DB: 15)
    * *Intent:* /*
  * `bytes_from_hexascii` (Impact: 33.0 | O(N^3) | DB: 8)
  * `limbs_from_hexascii` (Impact: 16.9 | O(N^3) | DB: 8)
  * `limbs_from_be_bytes` (Impact: 7.6 | O(N^6) | DB: 5)
  * `bytes_zero` (Impact: 5.5 | O(N^2) | DB: 3)
    * *Intent:* /* * Copyright Supranational LLC * Licensed under the Apache License, Version 2.0, see LICENSE for d...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 10`, `args: 5`, `func_start: 7`
* *Risk/State:* `state_mutation: 127`
* *Architecture:* `api: 20`
* *Defense:* `safety: 9`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 35.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.09538
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/hash_to_field.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.908 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.702 IQR)
- **Top Global Matches:** file_cluster_13: 14.908, file_cluster_8: 14.97, file_cluster_0: 15.007
- **Magnitude:** 265.8 | **LOC:** 178 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (62.5811%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `blst_expand_message_xmd` (Impact: 47.4 | O(N^6) | DB: 8)
  * `hash_to_field` (Impact: 29.6 | O(N^6) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 15`, `args: 4`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 154`
* *Architecture:* `api: 32`, `import: 2`
* *Defense:* `safety: 22`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.503
  * `Choke Point (Betweenness):` 0.000264 | `Ripple Effect (Closeness):` 0.031683
  * `Imports (Out-Degree: 2):` consts.h, sha256.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/asm/ct_is_square_mod_384-x86_64.pl` (PERL) | Magnitude: 90.12 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 254, state_mutation: 67, indent_spaces: 39, branch: 38
- `bindings/rust/src/lib.rs` (RUST) | Magnitude: 3762.34 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1975, structural_boundaries: 514, state_mutation: 312, branch: 240
- `src/asm/arm-xlate.pl` (PERL) | Magnitude: 8186.14 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 699, branch: 171, regex_execution: 167, indent_spaces: 142

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `bindings/go/blst.go` (GO) | Magnitude: 2402.6 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 1438, state_mutation: 1043, pointers: 616, encapsulation: 416

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/vect.h` (C) | Magnitude: 517.9 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: immutability_locks: 168, state_mutation: 162, api: 137, structural_boundaries: 114
- `src/server.c` (C) | Magnitude: 15.52 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: import: 20, macros: 3, scientific: 2, ownership: 1
- `src/rb_tree.c` (C) | Magnitude: 239.36 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 98, indent_spaces: 64, pointers: 56, api: 28
- `bindings/node.js/runnable.js` (JAVASCRIPT) | Magnitude: 14.64 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 2, args: 1, state_mutation: 1
- `src/hash_to_field.c` (C) | Magnitude: 265.8 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 154, indent_spaces: 114, pointers: 71, api: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `bindings/rust/benches/blst_benches.rs` (RUST) | Magnitude: 380.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 347, structural_boundaries: 154, args: 77, state_mutation: 74

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/pentaroot.c` (C) | Magnitude: 36.64 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, state_mutation: 16, macros: 12, immutability_locks: 11
- `bindings/zig/tests.zig` (ZIG) | Magnitude: 35.1 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, branch: 33, safety: 30, bitwise_ops: 30
- `bindings/go/cgo_server.c` (C) | Magnitude: 10.52 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 1
- `src/cpuid.c` (C) | Magnitude: 117.98 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 79, indent_spaces: 44, branch: 41, macros: 33
- `src/exp.c` (C) | Magnitude: 70.42 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 21, branch: 9, api: 8

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `bindings/go/blst.go` -> Churn: **100.0%** | Cog Load: 49.9024% | Debt: 100.0%
- `src/multi_scalar.c` -> Churn: **71.35%** | Cog Load: 70.4375% | Debt: 0.0%
- `src/keygen.c` -> Churn: **63.09%** | Cog Load: 85.8933% | Debt: 0.0%
- `bindings/go/rb_tree.go` -> Churn: **63.09%** | Cog Load: 73.3214% | Debt: 19.7642%
- `bindings/blst.hpp` -> Churn: **58.86%** | Cog Load: 74.1741% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/asm/arm-xlate.pl` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 8186.14
- `bindings/rust/src/lib.rs` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 3762.34
- `bindings/go/blst.go` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 2402.6
- `bindings/blst.hpp` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 1255.78
- `bindings/rust/src/pippenger.rs` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 935.44

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/e1.c` -> **Severity: 0.073** (Bridge: 0.0007 * Flux: 99.4226%)
- `src/e2.c` -> **Severity: 0.073** (Bridge: 0.0007 * Flux: 98.4747%)
- `src/vect.c` -> **Severity: 0.059** (Bridge: 0.0006 * Flux: 99.9811%)
- `src/keygen.c` -> **Severity: 0.046** (Bridge: 0.0005 * Flux: 100.0%)
- `src/exports.c` -> **Severity: 0.038** (Bridge: 0.0004 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/bytes.h` -> **Severity: 9.221** (Embedded: 0.0954 * Error Risk: 96.6715%)
- `src/vect.h` -> **Severity: 6.861** (Embedded: 0.1504 * Error Risk: 45.625%)
- `src/ec_mult.h` -> **Severity: 2.972** (Embedded: 0.0324 * Error Risk: 91.7164%)
- `src/hash_to_field.c` -> **Severity: 2.742** (Embedded: 0.0317 * Error Risk: 86.5297%)
- `src/sha256.h` -> **Severity: 2.615** (Embedded: 0.0404 * Error Risk: 64.6712%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/vect.h` -> **Severity: 10093.1** (Blast Radius: 100.931 * Doc Risk: 100.0%)
- `src/fields.h` -> **Severity: 4516.196** (Blast Radius: 45.163 * Doc Risk: 99.9977%)
- `src/consts.h` -> **Severity: 3933.892** (Blast Radius: 39.339 * Doc Risk: 99.9998%)
- `src/bytes.h` -> **Severity: 3510.893** (Blast Radius: 35.109 * Doc Risk: 99.9998%)
- `src/point.h` -> **Severity: 3435.087** (Blast Radius: 34.362 * Doc Risk: 99.9676%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
