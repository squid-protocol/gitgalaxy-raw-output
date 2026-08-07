# ARCHITECTURAL_BRIEF: blst
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/blst` |
| **Timestamp** | `2026-08-07T03:49:10.881259+00:00` |
| **Scan Duration** | `0.65s` |
| **Git Branch** | `master` |
| **Git Commit** | `f62244ef50ad1a603decdb8f215e982d2a467bb6` |
| **Git Remote** | `https://github.com/supranational/blst.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 62 malicious artifacts.

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
> **Architectural Drift Z-Score:** `7.27`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 85 | 83.3% |
| file_cluster_13 | 7 | 6.9% |
| file_cluster_0 | 3 | 2.9% |
| file_cluster_11 | 1 | 1.0% |

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
| Cognitive Load Exposure | 0.0 | 96.9 | 34.0 | 21.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 55.9 | 66.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.0 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 16.8 | 2.3 | 2.3 |
| API Exposure | 0.0 | 17.3 | 4.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 30.9 | 0.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 61.5 | 94.6 | 0.0 |
| Commented Logic Exposure | 0.0 | 20.6 | 1.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 10.6 | 1.6 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 44.0 | 20.7 | 100.0 |
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

- `joined_execute` (@ `bindings/rust/src/lib.rs`) -> Impact: **427.7** | LOC: 1556
- `re` (@ `src/asm/x86_64-xlate.pl`) -> Impact: **275.4** | LOC: 346
- `size` (@ `src/asm/x86_64-xlate.pl`) -> Impact: **240.1** | LOC: 559
- `coreAggregateVerifyPkInG1` (@ `bindings/go/blst.go`) -> Impact: **87.4** | LOC: 108
- `coreAggregateVerifyPkInG2` (@ `bindings/go/blst.go`) -> Impact: **87.4** | LOC: 108
- `out` (@ `src/asm/x86_64-xlate.pl`) -> Impact: **74.6** | LOC: 72
- `mult` (@ `bindings/rust/src/pippenger.rs`) -> Impact: **69.7** | LOC: 193
- `body_00_15` (@ `src/asm/sha256-x86_64.pl`) -> Impact: **68.5** | LOC: 523
- `verify_multiple_aggregate_signatures` (@ `bindings/rust/src/lib.rs`) -> Impact: **63.9** | LOC: 77
- `aggregate_verify` (@ `bindings/rust/src/lib.rs`) -> Impact: **60.5** | LOC: 79

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/asm` | 25 | 14792.7 | 37.05% | 4.89% |
| `src` | 37 | 7309.74 | 43.5% | 7.9% |
| `bindings/go` | 7 | 2527.62 | 21.25% | 17.11% |
| `bindings/rust/src` | 4 | 2076.46 | 44.52% | 79.85% |
| `bindings` | 3 | 1170.6 | 27.39% | 33.33% |
| `bindings/rust/benches` | 1 | 199.52 | 25.05% | 0.0% |
| `bindings/vectors/hash_to_curve` | 7 | 102.32 | 0.0% | 0.0% |
| `bindings/node.js` | 6 | 69.25 | 11.61% | 16.53% |
| `bindings/java` | 2 | 56.98 | 34.19% | 48.53% |
| `bindings/zig` | 3 | 52.4 | 30.76% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `bindings/blst.hpp` -> **100.0%** Exposure
- `src/blst_t.hpp` -> **100.0%** Exposure
- `bindings/go/blst.go` -> **100.0%** Exposure
- `bindings/rust/publish.sh` -> **100.0%** Exposure
- `bindings/rust/src/lib.rs` -> **99.9999%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/bulk_addition.c` -> **100.0%** Exposure
- `src/bytes.h` -> **100.0%** Exposure
- `src/cpuid.c` -> **100.0%** Exposure
- `src/ec_mult.h` -> **100.0%** Exposure
- `src/exp.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `bindings/blst.hpp` -> **0** Orphaned Functions | **184** Duplicates
- `bindings/rust/src/lib.rs` -> **25** Orphaned Functions | **76** Duplicates
- `bindings/go/blst.go` -> **0** Orphaned Functions | **80** Duplicates
- `src/blst_t.hpp` -> **20** Orphaned Functions | **17** Duplicates
- `src/asm/x86_64-xlate.pl` -> **0** Orphaned Functions | **10** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`bindings/go/blst.go`** -> AI Confidence: **99.25%**
2. **`src/exp.c`** -> AI Confidence: **99.23%**
3. **`src/pentaroot-addchain.h`** -> AI Confidence: **99.23%**
4. **`src/recip-addchain.h`** -> AI Confidence: **99.23%**
5. **`src/sqrt-addchain.h`** -> AI Confidence: **99.23%**
6. **`bindings/rust/publish.sh`** -> AI Confidence: **99.17%**
7. **`bindings/rust/src/lib.rs`** -> AI Confidence: **99.16%**
8. **`bindings/go/generate.py`** -> AI Confidence: **99.13%**
9. **`bindings/node.js/blst_wrap.py`** -> AI Confidence: **99.13%**
10. **`src/bulk_addition.c`** -> AI Confidence: **99.1%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `202` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `bindings/go/blst.go` (GO) -> Cumulative Risk: **674.21**
- **Archetype:** `file_cluster_11` (Distance: 15.048 IQR)
- **Magnitude:** 2294.3 | **LOC:** 3631 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Churn (100.0%)
- **Heaviest Functions:** `coreAggregateVerifyPkInG1` (Impact: 87.4), `coreAggregateVerifyPkInG2` (Impact: 87.4), `multipleAggregateVerifyPkInG1` (Impact: 55.0)

### 2. `bindings/blst.hpp` (CPP) -> Cumulative Risk: **664.65**
- **Archetype:** `file_cluster_8` (Distance: 13.185 IQR)
- **Magnitude:** 943.98 | **LOC:** 959 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9997%), Safety Score (94.3142%)
- **Heaviest Functions:** `aggregate` (Impact: 6.3), `aggregate` (Impact: 6.3), `P1` (Impact: 5.5)

### 3. `src/e1.c` (C) -> Cumulative Risk: **626.27**
- **Archetype:** `file_cluster_8` (Distance: 11.779 IQR)
- **Magnitude:** 393.0 | **LOC:** 565 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9965%), State Flux (99.4226%), Tech Debt (96.5555%)
- **Heaviest Functions:** `blst_p1_mult` (Impact: 11.4), `POINTonE1_Uncompress_Z` (Impact: 8.6), `blst_sign_pk2_in_g2` (Impact: 7.4)

### 4. `src/keygen.c` (C) -> Cumulative Risk: **620.98**
- **Archetype:** `file_cluster_8` (Distance: 13.468 IQR)
- **Magnitude:** 250.8 | **LOC:** 320 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (85.8933%)
- **Heaviest Functions:** `HKDF_Expand` (Impact: 24.7), `keygen` (Impact: 14.3), `HKDF_Extract` (Impact: 9.5)

### 5. `src/exports.c` (C) -> Cumulative Risk: **614.16**
- **Archetype:** `file_cluster_8` (Distance: 13.588 IQR)
- **Magnitude:** 696.86 | **LOC:** 621 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (92.9612%)
- **Heaviest Functions:** `blst_uint64_from_fp` (Impact: 9.6), `blst_uint64_from_fr` (Impact: 9.6), `blst_uint64_from_scalar` (Impact: 8.1)

### 6. `src/e2.c` (C) -> Cumulative Risk: **610.79**
- **Archetype:** `file_cluster_8` (Distance: 11.48 IQR)
- **Magnitude:** 400.04 | **LOC:** 639 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9837%), State Flux (98.4747%), Tech Debt (95.8783%)
- **Heaviest Functions:** `blst_p2_mult` (Impact: 11.4), `POINTonE2_Deserialize_BE` (Impact: 8.1), `POINTonE2_Uncompress_Z` (Impact: 7.5)

### 7. `src/blst_t.hpp` (CPP) -> Cumulative Risk: **609.68**
- **Archetype:** `file_cluster_8` (Distance: 13.471 IQR)
- **Magnitude:** 403.56 | **LOC:** 673 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (98.7053%)
- **Heaviest Functions:** `operator^` (Impact: 18.6), `vec_left_align` (Impact: 11.0), `to_scalar` (Impact: 7.7)

### 8. `bindings/rust/src/pippenger.rs` (RUST) -> Cumulative Risk: **597.18**
- **Archetype:** `file_cluster_8` (Distance: 11.396 IQR)
- **Magnitude:** 342.74 | **LOC:** 549 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9788%), Safety Score (83.1117%), Verification (80.0%)
- **Heaviest Functions:** `mult` (Impact: 69.7), `validate` (Impact: 30.7), `add` (Impact: 20.1)

### 9. `src/vect.h` (C) -> Cumulative Risk: **567.7**
- **Archetype:** `file_cluster_13` (Distance: 13.805 IQR)
- **Magnitude:** 391.5 | **LOC:** 432 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.943%), Safety Score (85.2471%)
- **Heaviest Functions:** `vec_select` (Impact: 40.7), `vec_zero` (Impact: 7.5), `vec_is_equal` (Impact: 7.0)

### 10. `src/asm/x86_64-xlate.pl` (PERL) -> Cumulative Risk: **560.95**
- **Archetype:** `file_cluster_8` (Distance: 14.598 IQR)
- **Magnitude:** 2210.92 | **LOC:** 1974 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.3354%), Cognitive Load (96.9416%)
- **Heaviest Functions:** `re` (Impact: 275.4), `size` (Impact: 240.1), `out` (Impact: 74.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/asm/arm-xlate.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.76 IQR)
- **Top Global Matches:** file_cluster_0: 14.76, file_cluster_11: 14.84, file_cluster_8: 14.921
- **Magnitude:** 8101.29 | **LOC:** 516 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (87.0665%), Tech Debt (20.8232%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 139`, `args: 17`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 699`, `dead_code: 3`, `fragile_debt: 2`
* *Architecture:* `io: 4`, `import: 1`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/go/blst.go` (GO | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.048 IQR)
- **Top Global Matches:** file_cluster_11: 15.048, file_cluster_4: 15.059, file_cluster_12: 15.102
- **Magnitude:** 2294.3 | **LOC:** 3631 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.9024%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `coreAggregateVerifyPkInG1` (Impact: 87.4)
  * `coreAggregateVerifyPkInG2` (Impact: 87.4)
  * `multipleAggregateVerifyPkInG1` (Impact: 55.0)
  * `multipleAggregateVerifyPkInG2` (Impact: 55.0)
  * `coreAggregate` (Impact: 42.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 381`, `structural_boundaries: 319`, `args: 132`, `func_start: 132`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1043`, `dead_code: 24`, `planned_debt: 2`, `duplicate_logic: 80`
* *Architecture:* `api: 171`, `concurrency: 96`, `import: 2`
* *Defense:* `safety: 3`, `doc: 89`, `sync_locks: 67`, `immutability_locks: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unsafe, bits, C, fmt, atomic, sync, runtime
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/asm/x86_64-xlate.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.598 IQR)
- **Top Global Matches:** file_cluster_8: 14.598, file_cluster_0: 14.712, file_cluster_11: 14.718
- **Magnitude:** 2210.92 | **LOC:** 1974 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.9416%), Tech Debt (63.9307%)
**Top Internal Functions/Classes:**
  * `re` (Impact: 275.4)
  * `size` (Impact: 240.1)
  * `out` (Impact: 74.6)
  * `out` (Impact: 40.3)
  * `out` (Impact: 31.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 524`, `structural_boundaries: 332`, `args: 44`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 2`, `state_mutation: 1421`, `dead_code: 6`, `planned_debt: 1`, `duplicate_logic: 10`
* *Architecture:* `io: 4`, `import: 5`
* *Defense:* `safety: 1`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` occasion, dynamic, following, strict, even, warnings, multiple, DWP_OP_reg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/rust/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.476 IQR)
- **Top Global Matches:** file_cluster_0: 12.476, file_cluster_8: 12.565, file_cluster_17: 12.634
- **Magnitude:** 1651.94 | **LOC:** 2386 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (34.5838%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `joined_execute` (Impact: 427.7)
  * `verify_multiple_aggregate_signatures` (Impact: 63.9)
  * `aggregate_verify` (Impact: 60.5)
  * `mul_n_aggregate` (Impact: 36.2)
  * `verify_multiple_aggregate_signatures` (Impact: 34.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 514`, `args: 170`, `func_start: 128`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 3`, `state_mutation: 294`, `dead_code: 2`, `planned_debt: 9`, `duplicate_logic: 76`, `orphaned_logic: 25`
* *Architecture:* `api: 86`, `concurrency: 5`, `import: 23`
* *Defense:* `safety: 155`, `doc: 2`, `test: 53`, `sync_locks: 5`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MaybeUninit, alloc::boxed::Box, SeedableRng, rand_chacha::ChaCha20Rng, alloc::vec, alloc::vec::Vec, Arc, zeroize::Zeroize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/no_asm.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.14 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 4.515 IQR)
- **Top Global Matches:** file_cluster_8: 15.14, file_cluster_11: 15.271, file_cluster_0: 15.28
- **Magnitude:** 1414.28 | **LOC:** 1346 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.6514%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sqr_mont_382x` (Impact: 39.4)
  * `mul_mont_n` (Impact: 12.7)
    * *Intent:* #if !defined(__STDC_VERSION__) || __STDC_VERSION__<199901 || defined(__STDC_NO_VLA__) # error "unsup...
  * `blst_sha256_block_data_order` (Impact: 12.2)
  * `mul_mont_nonred_n` (Impact: 10.0)
  * `mul_by_3_mod_n` (Impact: 9.2)
    * *Intent:* #define SUB_MOD_IMPL(bits) \
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 52`, `args: 5`, `func_start: 30`
* *Risk/State:* `state_mutation: 1076`, `dead_code: 1`
* *Architecture:* `api: 149`
* *Defense:* `safety: 42`, `immutability_locks: 96`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.509
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.024752
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bindings/blst.hpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.185 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 6.895 IQR)
- **Top Global Matches:** file_cluster_8: 13.185, file_cluster_13: 13.49, file_cluster_0: 13.605
- **Magnitude:** 943.98 | **LOC:** 959 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (72.104%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `aggregate` (Impact: 6.3)
  * `aggregate` (Impact: 6.3)
  * `P1` (Impact: 5.5)
  * `P2` (Impact: 5.5)
  * `P1_Affine` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 244`, `args: 143`, `func_start: 209`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 6`, `state_mutation: 512`, `duplicate_logic: 184`
* *Architecture:* `api: 27`, `import: 5`
* *Defense:* `safety: 8`, `immutability_locks: 368`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` blst.h, cstring, memory, string, vector
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/exports.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.79%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.588 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.001 IQR)
- **Top Global Matches:** file_cluster_8: 13.588, file_cluster_13: 13.758, file_cluster_0: 13.788
- **Magnitude:** 696.86 | **LOC:** 621 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (85.0794%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `blst_uint64_from_fp` (Impact: 9.6)
  * `blst_uint64_from_fr` (Impact: 9.6)
  * `blst_uint64_from_scalar` (Impact: 8.1)
  * `blst_uint32_from_scalar` (Impact: 7.9)
  * `blst_uint32_from_fp` (Impact: 7.7)
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
- **Global Archetype:** `file_cluster_8` (Drift: 10.871 IQR)
- **Top Global Matches:** file_cluster_8: 10.871, file_cluster_0: 11.327, file_cluster_7: 11.509
- **Magnitude:** 651.63 | **LOC:** 343 | **CtrlFlow:** 68.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.6405%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 8`, `args: 5`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 15`, `state_mutation: 90`
* *Architecture:* `io: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/multi_scalar.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.1%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.362 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.584 IQR)
- **Top Global Matches:** file_cluster_8: 15.362, file_cluster_0: 15.442, file_cluster_13: 15.45
- **Magnitude:** 561.54 | **LOC:** 475 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (70.4375%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pippenger_window_size` (Impact: 8.8)
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

### `src/asm/sha256-x86_64.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.03 IQR)
- **Top Global Matches:** file_cluster_8: 12.03, file_cluster_0: 12.512, file_cluster_7: 12.529
- **Magnitude:** 440.76 | **LOC:** 808 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.6931%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `body_00_15` (Impact: 68.5)
  * `SSSE3_256_00_47` (Impact: 52.5)
  * `Xupdate_256_SSSE3` (Impact: 4.0)
  * `AUTOLOAD` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 33`, `args: 115`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 109`, `high_risk_execution: 3`, `state_mutation: 298`, `dead_code: 1`
* *Architecture:* `io: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` scalar
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/asm/mulx_mont_384-x86_64.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.537 IQR)
- **Top Global Matches:** file_cluster_8: 10.537, file_cluster_7: 11.248, file_cluster_1: 11.464
- **Magnitude:** 438.78 | **LOC:** 2487 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.6422%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 52`, `args: 5`
* *Risk/State:* `state_mutation: 382`
* *Architecture:* `io: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/asm/mulq_mont_384-x86_64.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.34 IQR)
- **Top Global Matches:** file_cluster_8: 10.34, file_cluster_7: 11.042, file_cluster_1: 11.276
- **Magnitude:** 431.46 | **LOC:** 2755 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.2507%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 56`, `args: 14`
* *Risk/State:* `state_mutation: 370`
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
- **Magnitude:** 403.56 | **LOC:** 674 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.7965%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `PAIRING_Aggregate_PK_in_G2` (Impact: 29.6)
  * `blst_pairing_merge` (Impact: 25.4)
  * `PAIRING_FinalVerify` (Impact: 13.9)
  * `blst_aggregate_in_g1` (Impact: 8.4)
  * `blst_aggregate_in_g2` (Impact: 8.4)
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

### `src/blst_t.hpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.471 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.468 IQR)
- **Top Global Matches:** file_cluster_8: 13.471, file_cluster_13: 13.675, file_cluster_11: 13.806
- **Magnitude:** 403.56 | **LOC:** 673 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (76.8298%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `operator^` (Impact: 18.6)
  * `vec_left_align` (Impact: 11.0)
    * *Intent:* #include "bytes.h" #undef launder // avoid conflict with C++ >=17 #ifdef __GNUC__
  * `to_scalar` (Impact: 7.7)
  * `operator^=` (Impact: 7.4)
  * `operator*=` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 115`, `args: 39`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 259`, `duplicate_logic: 17`, `orphaned_logic: 20`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` vect.h, bytes.h, cstdint
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/asm/add_mod_384-x86_64.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.669 IQR)
- **Top Global Matches:** file_cluster_8: 10.669, file_cluster_7: 11.307, file_cluster_1: 11.536
- **Magnitude:** 402.68 | **LOC:** 1567 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.0194%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ret` (Impact: 33.5)
  * `vec_select` (Impact: 28.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 33`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 313`
* *Architecture:* `io: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/e2.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.48 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.899 IQR)
- **Top Global Matches:** file_cluster_8: 11.48, file_cluster_13: 11.841, file_cluster_7: 11.959
- **Magnitude:** 400.04 | **LOC:** 639 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.446%), Tech Debt (95.8783%)
**Top Internal Functions/Classes:**
  * `blst_p2_mult` (Impact: 11.4)
  * `POINTonE2_Deserialize_BE` (Impact: 8.1)
  * `POINTonE2_Uncompress_Z` (Impact: 7.5)
  * `blst_sign_pk2_in_g1` (Impact: 7.4)
  * `blst_sk_to_pk2_in_g2` (Impact: 6.7)
    * *Intent:* #ifndef FUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION flt_reciprocal_fp2(Z, out->Z); /* 1/Z */ #else reci...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 73`, `args: 15`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `state_mutation: 112`, `fragile_debt: 18`
* *Architecture:* `api: 137`, `import: 5`
* *Defense:* `safety: 7`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.503
  * `Choke Point (Betweenness):` 0.000738 | `Ripple Effect (Closeness):` 0.031683
  * `Imports (Out-Degree: 5):` ec_mult.h, fields.h, errors.h, point.h, ec_ops.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/e1.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.779 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.978 IQR)
- **Top Global Matches:** file_cluster_8: 11.779, file_cluster_13: 12.067, file_cluster_7: 12.239
- **Magnitude:** 393.0 | **LOC:** 565 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.4704%), Tech Debt (96.5555%)
**Top Internal Functions/Classes:**
  * `blst_p1_mult` (Impact: 11.4)
  * `POINTonE1_Uncompress_Z` (Impact: 8.6)
  * `blst_sign_pk2_in_g2` (Impact: 7.4)
  * `blst_sk_to_pk2_in_g1` (Impact: 6.7)
    * *Intent:* mul_fp(out->Y, out->Y, ZZ); /* Y = Y/Z^3 */
  * `POINTonE1_Deserialize_BE` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 70`, `args: 15`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `state_mutation: 111`, `fragile_debt: 16`
* *Architecture:* `api: 136`, `import: 5`
* *Defense:* `safety: 7`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.503
  * `Choke Point (Betweenness):` 0.000738 | `Ripple Effect (Closeness):` 0.031683
  * `Imports (Out-Degree: 5):` ec_mult.h, fields.h, errors.h, point.h, ec_ops.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/vect.h` (C | Tier 0 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.805 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.179 IQR)
- **Top Global Matches:** file_cluster_13: 13.805, file_cluster_8: 13.815, file_cluster_0: 13.912
- **Magnitude:** 391.5 | **LOC:** 432 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (62.5554%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `vec_select` (Impact: 40.7)
  * `vec_zero` (Impact: 7.5)
  * `vec_is_equal` (Impact: 7.0)
  * `vec_is_zero` (Impact: 6.1)
  * `vec_cswap` (Impact: 5.4)
    * *Intent:* # elif defined(_MSC_VER) # define restrict __restrict # else # define restrict # endif # endif #endi...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 114`, `args: 18`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 162`
* *Architecture:* `api: 137`, `import: 4`
* *Defense:* `safety: 28`, `immutability_locks: 168`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 100.931
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.150371
  * `Imports (Out-Degree: 0):` malloc.h, stdlib.h, alloca.h, stddef.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `bindings/rust/src/pippenger.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.94%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.396 IQR)
- **Top Global Matches:** file_cluster_8: 11.396, file_cluster_0: 11.535, file_cluster_13: 11.674
- **Magnitude:** 342.74 | **LOC:** 549 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (79.403%), Tech Debt (60.7069%)
**Top Internal Functions/Classes:**
  * `mult` (Impact: 69.7)
  * `validate` (Impact: 30.7)
  * `add` (Impact: 20.1)
  * `breakdown` (Impact: 19.7)
  * `from` (Impact: 14.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 172`, `args: 19`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 134`, `duplicate_logic: 4`, `orphaned_logic: 4`
* *Architecture:* `api: 6`, `concurrency: 12`, `import: 4`
* *Defense:* `safety: 16`, `test: 2`, `sync_locks: 3`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core::slice::SliceIndex, core::ops::Index, std::sync::Barrier, IndexMut, core::num::Wrapping
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/asm/sha256-armv8.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.379 IQR)
- **Top Global Matches:** file_cluster_8: 12.379, file_cluster_0: 12.763, file_cluster_17: 12.822
- **Magnitude:** 332.88 | **LOC:** 555 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.052%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `body_00_15` (Impact: 46.5)
  * `AUTOLOAD` (Impact: 22.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 37`, `args: 89`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 77`, `high_risk_execution: 1`, `state_mutation: 254`
* *Architecture:* `io: 6`, `import: 2`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` integer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ec_mult.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.213 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.228 IQR)
- **Top Global Matches:** file_cluster_8: 14.213, file_cluster_13: 14.462, file_cluster_0: 14.478
- **Magnitude:** 315.92 | **LOC:** 316 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (57.4156%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_wval_limb` (Impact: 2.9)
  * `booth_encode` (Impact: 1.6)
  * `get_wval` (Impact: 1.4)
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

### `src/keygen.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.91%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.468 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.24 IQR)
- **Top Global Matches:** file_cluster_8: 13.468, file_cluster_13: 13.574, file_cluster_0: 13.706
- **Magnitude:** 250.8 | **LOC:** 320 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (85.8933%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `HKDF_Expand` (Impact: 24.7)
  * `keygen` (Impact: 14.3)
  * `HKDF_Extract` (Impact: 9.5)
  * `HMAC_init` (Impact: 9.0)
  * `parent_SK_to_lamport_PK` (Impact: 8.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 38`, `args: 3`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 120`
* *Architecture:* `api: 50`, `import: 3`
* *Defense:* `safety: 22`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.503
  * `Choke Point (Betweenness):` 0.000462 | `Ripple Effect (Closeness):` 0.031683
  * `Imports (Out-Degree: 3):` consts.h, bytes.h, sha256.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/hash_to_field.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.908 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.702 IQR)
- **Top Global Matches:** file_cluster_13: 14.908, file_cluster_8: 14.97, file_cluster_0: 15.007
- **Magnitude:** 212.8 | **LOC:** 178 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.5811%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `blst_expand_message_xmd` (Impact: 14.3)
  * `hash_to_field` (Impact: 9.7)
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

### `src/bytes.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.012 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.416 IQR)
- **Top Global Matches:** file_cluster_8: 15.012, file_cluster_0: 15.12, file_cluster_9: 15.205
- **Magnitude:** 200.88 | **LOC:** 153 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.4303%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bytes_from_hexascii` (Impact: 16.9)
  * `le_bytes_from_limbs` (Impact: 15.2)
    * *Intent:* /*
  * `limbs_from_hexascii` (Impact: 8.9)
  * `bytes_zero` (Impact: 3.8)
    * *Intent:* /* * Copyright Supranational LLC * Licensed under the Apache License, Version 2.0, see LICENSE for d...
  * `limbs_from_be_bytes` (Impact: 2.6)
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

### `bindings/rust/benches/blst_benches.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.441 IQR)
- **Top Global Matches:** file_cluster_8: 11.441, file_cluster_17: 11.447, file_cluster_13: 11.801
- **Magnitude:** 199.52 | **LOC:** 479 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.0538%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bench_serdes` (Impact: 38.8)
  * `bench_verify_multi_aggregate` (Impact: 18.1)
  * `bench_fast_aggregate_verify` (Impact: 16.9)
  * `bench_aggregate_verify` (Impact: 11.6)
  * `bench_aggregate` (Impact: 11.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 154`, `args: 77`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 72`
* *Architecture:* `import: 5`
* *Defense:* `safety: 15`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BenchmarkId, blst::min_pk::*, blst::*, SeedableRng, rand_chacha::ChaCha20Rng, Criterion, criterion_main, criterion::criterion_group...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/asm/ct_is_square_mod_384-x86_64.pl` (PERL) | Magnitude: 96.12 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 254, state_mutation: 67, indent_spaces: 39, branch: 38
- `src/asm/arm-xlate.pl` (PERL) | Magnitude: 8101.29 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 699, branch: 169, regex_execution: 167, indent_spaces: 142
- `bindings/rust/src/lib.rs` (RUST) | Magnitude: 1651.94 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1975, structural_boundaries: 514, state_mutation: 294, branch: 234

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `bindings/go/blst.go` (GO) | Magnitude: 2294.3 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 1438, state_mutation: 1043, pointers: 616, encapsulation: 416

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/vect.h` (C) | Magnitude: 391.5 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: immutability_locks: 168, state_mutation: 162, api: 137, structural_boundaries: 114
- `src/server.c` (C) | Magnitude: 15.52 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: import: 20, macros: 3, scientific: 2, ownership: 1
- `src/rb_tree.c` (C) | Magnitude: 174.26 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 98, indent_spaces: 64, pointers: 56, api: 28
- `bindings/node.js/runnable.js` (JAVASCRIPT) | Magnitude: 14.64 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 2, args: 1, state_mutation: 1
- `src/hash_to_field.c` (C) | Magnitude: 212.8 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 154, indent_spaces: 114, pointers: 71, api: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `bindings/rust/benches/blst_benches.rs` (RUST) | Magnitude: 199.52 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 347, structural_boundaries: 154, args: 77, state_mutation: 72
- `src/pentaroot.c` (C) | Magnitude: 33.64 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, state_mutation: 16, macros: 12, immutability_locks: 11
- `bindings/zig/tests.zig` (ZIG) | Magnitude: 35.1 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, branch: 33, safety: 30, bitwise_ops: 30
- `bindings/go/cgo_server.c` (C) | Magnitude: 10.52 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 1
- `src/cpuid.c` (C) | Magnitude: 115.68 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 79, indent_spaces: 44, branch: 41, macros: 33

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `bindings/go/blst.go` -> Churn: **100.0%** | Cog Load: 49.9024% | Debt: 100.0%
- `src/multi_scalar.c` -> Churn: **71.35%** | Cog Load: 70.4375% | Debt: 0.0%
- `src/keygen.c` -> Churn: **63.09%** | Cog Load: 85.8933% | Debt: 0.0%
- `bindings/go/rb_tree.go` -> Churn: **63.09%** | Cog Load: 73.3214% | Debt: 19.7642%
- `bindings/blst.hpp` -> Churn: **58.86%** | Cog Load: 72.104% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/asm/arm-xlate.pl` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 8101.29
- `bindings/go/blst.go` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 2294.3
- `bindings/rust/src/lib.rs` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 1651.94
- `bindings/blst.hpp` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 943.98
- `src/exports.c` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 696.86

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

- `src/vect.h` -> **Severity: 12.819** (Embedded: 0.1504 * Error Risk: 85.2471%)
- `src/bytes.h` -> **Severity: 9.44** (Embedded: 0.0954 * Error Risk: 98.9708%)
- `src/consts.h` -> **Severity: 7.093** (Embedded: 0.107 * Error Risk: 66.2622%)
- `src/sha256.h` -> **Severity: 3.754** (Embedded: 0.0404 * Error Risk: 92.8651%)
- `src/ec_mult.h` -> **Severity: 3.176** (Embedded: 0.0324 * Error Risk: 98.003%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/vect.h` -> **Severity: 10093.1** (Blast Radius: 100.931 * Doc Risk: 100.0%)
- `src/fields.h` -> **Severity: 4514.819** (Blast Radius: 45.163 * Doc Risk: 99.9672%)
- `src/consts.h` -> **Severity: 3918.562** (Blast Radius: 39.339 * Doc Risk: 99.6101%)
- `src/bytes.h` -> **Severity: 3480.517** (Blast Radius: 35.109 * Doc Risk: 99.1346%)
- `src/point.h` -> **Severity: 3416.727** (Blast Radius: 34.362 * Doc Risk: 99.4333%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
