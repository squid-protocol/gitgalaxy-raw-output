# ARCHITECTURAL_BRIEF: blst
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/supranational/blst.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 112 analyzed artifact(s), 38256 LOC.
- **Load-bearing artifact:** `src/fields.h` -- 12 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `bindings/rust/src/lib.rs` -- pulls in 22 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `bindings/go/blst.go` at magnitude 3296.72 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
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
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 247 |
| Analyzed Artifacts (Scanned) | 112 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 135 |
| Total LOC | 38256 |
| Volatility Index | 0.009 |
| % Scanned of codebase = | 45.3% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3933 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4777 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5915 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 39 | 9630 | 34.8% |
| PERL | 25 | 18261 | 22.3% |
| JSON | 7 | 573 | 6.2% |
| MARKDOWN | 6 | 0 | 5.4% |
| GO | 6 | 3717 | 5.4% |
| RUST | 6 | 3321 | 5.4% |
| PYTHON | 5 | 484 | 4.5% |
| SHELL | 3 | 180 | 2.7% |
| ZIG | 3 | 136 | 2.7% |
| CPP | 2 | 1446 | 1.8% |
| JAVASCRIPT | 2 | 49 | 1.8% |
| TYPESCRIPT | 2 | 230 | 1.8% |
| CSHARP | 1 | 60 | 0.9% |
| HTML | 1 | 38 | 0.9% |
| ASSEMBLY | 1 | 0 | 0.9% |
| MAKEFILE | 1 | 19 | 0.9% |
| JAVA | 1 | 50 | 0.9% |
| BATCH | 1 | 62 | 0.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `3.553`
> **Composition Archetype:** `Small Flat Repo (2)` (z +3.55; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 38%, Data / Markup / Trivial 15%, Large Core Modules (3) 12%, Compute Cores Files 7%, Encapsulated Accessors Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 106 | 94.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 5.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 135*

**Composition by Extension & Reason:**
- `.s`: 79x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.asm`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.me`: 5x Excluded (Unsupported Extension: '.me')
- `.tgo`: 4x Unsupported Format (.tgo)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.go`: 1x Excluded (Machine-Generated Source Code Signature: 727 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.zig`: 1x Excluded (Machine-Generated Source Code Signature: 608 LOC), 1x Excluded (Machine-Generated Source Code Signature: 508 LOC)
- `.swg`: 1x Excluded (Unsupported Extension: '.swg')
- `.csproj`: 1x Excluded (Unsupported Extension: '.csproj')
- `.cs`: 1x Excluded (Machine-Generated Source Code Signature: 1016 LOC)
- `.rs`: 1x Excluded (Machine-Generated Source Code Signature: 1416 LOC)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.pl`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.9 | 28.9 | 15.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 53.0 | 66.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 11.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 16.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.1 | 1.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 56.6 | 0.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 56.7 | 88.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 20.6 | 1.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 8.3 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 6.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 47.6 | 48.3 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5173 | 60 | 115 | `bindings/go/blst.go` |
| cleanup | 73 | 32 | 2 | `src/asm/x86_64-xlate.pl` |
| guards | 3026 | 51 | 87 | `bindings/blst.hpp` |
| danger | 596 | 56 | 12 | `src/asm/sha256-x86_64.pl` |
| concurrency | 142 | 4 | 0 | `bindings/go/blst.go` |
| connectivity | 1088 | 58 | 25 | `bindings/blst.h` |
| io | 165 | 34 | 2 | `build.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 38 | 9 | 0 | `src/asm/sha256-portable-x86_64.pl` |
| time | 0 | 0 | 0 | - |
| serialization | 4 | 2 | 0 | `bindings/go/blst_htoc_test.go` |
| regex | 545 | 31 | 6 | `src/asm/x86_64-xlate.pl` |
| events | 2 | 1 | 0 | `bindings/c#/poc.cs` |
| tests | 105 | 9 | 0 | `bindings/rust/src/lib.rs` |
| docs | 275 | 7 | 0 | `bindings/emscripten/build.py` |
| debt | 300 | 46 | 10 | `bindings/node.js/blst.hpp.ts` |
| mutation | 5654 | 85 | 101 | `src/no_asm.h` |
| dead_code | 181 | 30 | 3 | `bindings/go/blst.go` |
| credential | 0 | 0 | 0 | - |
| threat | 405 | 36 | 3 | `bindings/go/blst.go` |
| ml_ai | 52 | 13 | 1 | `src/ec_ops.h` |
| ui | 7 | 2 | 0 | `src/asm/x86_64-xlate.pl` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `build.sh` (Hits: 38)
- `bindings/emscripten/build.py` (Hits: 27)
- `bindings/go/generate.py` (Hits: 18)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **fields.h** (`src/fields.h`) — 12 inbound connections
2. **point.h** (`src/point.h`) — 8 inbound connections
3. **vect.h** (`src/vect.h`) — 7 inbound connections
4. **bytes.h** (`src/bytes.h`) — 6 inbound connections
5. **consts.h** (`src/consts.h`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`bindings/rust/src/lib.rs`) — 22 outbound dependencies
2. **server.c** (`src/server.c`) — 20 outbound dependencies
3. **README.md** (`README.md`) — 14 outbound dependencies
4. **x86_64-xlate.pl** (`src/asm/x86_64-xlate.pl`) — 13 outbound dependencies
5. **client_min_pk.c** (`src/client_min_pk.c`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `re` **(Many-Argument Workhorses)** (@ `src/asm/x86_64-xlate.pl`) -> Impact: **265.1** | LOC: 222
- `P1AffinesMult` **(Many-Argument Workhorses)** (@ `bindings/go/blst.go`) -> Impact: **185.3** | LOC: 307
  * *Intent:* // // Multi-scalar multiplication //
- `P2AffinesMult` **(Many-Argument Workhorses)** (@ `bindings/go/blst.go`) -> Impact: **185.3** | LOC: 307
  * *Intent:* // // Multi-scalar multiplication //
- `re` **(Compute Cores)** (@ `src/asm/x86_64-xlate.pl`) -> Impact: **114.3** | LOC: 139
- `PAIRING_Aggregate_PK_in_G1` **(Many-Argument Workhorses)** (@ `src/aggregate.c`) -> Impact: **91.6** | LOC: 99
- `PAIRING_Aggregate_PK_in_G2` **(Many-Argument Workhorses)** (@ `src/aggregate.c`) -> Impact: **91.3** | LOC: 93
  * *Intent:* /* * Optional |nbits|-wide |scalar| is used to facilitate multiple aggregated * signature verification as discussed at * https://ethresear.ch/t/fast-v...
- `coreAggregateVerifyPkInG1` **(Many-Argument Workhorses)** (@ `bindings/go/blst.go`) -> Impact: **78.9** | LOC: 108
- `coreAggregateVerifyPkInG2` **(Many-Argument Workhorses)** (@ `bindings/go/blst.go`) -> Impact: **78.9** | LOC: 108
- `out` **(Compute Cores)** (@ `src/asm/x86_64-xlate.pl`) -> Impact: **76.3** | LOC: 72
- `mult` **(Many-Argument Workhorses)** (@ `bindings/rust/src/pippenger.rs`) -> Impact: **69.7** | LOC: 193

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 37 | 7236.74 | 37.32% | 7.87% |
| `src/asm` | 25 | 5362.72 | 31.94% | 1.38% |
| `bindings/go` | 10 | 4070.22 | 26.78% | 22.84% |
| `bindings/rust/src` | 4 | 1221.98 | 20.4% | 47.3% |
| `bindings` | 3 | 792.06 | 5.63% | 7.19% |
| `bindings/node.js` | 6 | 307.7 | 17.36% | 28.85% |
| `__monolith__` | 6 | 189.5 | 15.49% | 8.33% |
| `bindings/java` | 3 | 161.0 | 54.61% | 32.36% |
| `bindings/vectors/hash_to_curve` | 7 | 102.32 | 0.0% | 0.0% |
| `bindings/rust/benches` | 1 | 102.02 | 8.2% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `bindings/node.js/blst.hpp.ts` -> **100.0%** Exposure
- `src/blst_t.hpp` -> **98.9218%** Exposure
- `bindings/java/runnable.java` -> **97.0688%** Exposure
- `src/e1.c` -> **96.5555%** Exposure
- `src/e2.c` -> **95.8783%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/bulk_addition.c` -> **100.0%** Exposure
- `src/bytes.h` -> **100.0%** Exposure
- `src/ec_mult.h` -> **100.0%** Exposure
- `src/exports.c` -> **100.0%** Exposure
- `src/hash_to_field.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `bindings/node.js/blst.hpp.ts` -> **0** Orphaned Functions | **42** Duplicates
- `bindings/go/blst.go` -> **30** Orphaned Functions | **0** Duplicates
- `bindings/rust/src/lib.rs` -> **26** Orphaned Functions | **4** Duplicates
- `bindings/go/blst_minpk_test.go` -> **21** Orphaned Functions | **0** Duplicates
- `src/blst_t.hpp` -> **0** Orphaned Functions | **16** Duplicates

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
- **Unknown Dependencies:** `240` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `bindings/go/blst.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3296.72 | **LOC:** 3631 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 6.226; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (94.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 42.9636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P1AffinesMult` **(Many-Argument Workhorses)** (Impact: 185.3)
    * *Intent:* // // Multi-scalar multiplication //
  * `P2AffinesMult` **(Many-Argument Workhorses)** (Impact: 185.3)
    * *Intent:* // // Multi-scalar multiplication //
  * `coreAggregateVerifyPkInG1` **(Many-Argument Workhorses)** (Impact: 78.9)
  * `coreAggregateVerifyPkInG2` **(Many-Argument Workhorses)** (Impact: 78.9)
  * `coreAggregate` **(Many-Argument Workhorses)** (Impact: 52.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 34 instances
* *Amplified Cascading Flux:* 394 instances
* *Concurrency (weighted view):* 204
* *State Mutation (weighted view):* 1185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 614`, `structural_boundaries: 510`, `args: 172`, `func_start: 172`, `class_start: 12`
* *Risk/State:* `high_risk_execution: 23`, `state_mutation: 397`, `dead_code: 38`, `planned_debt: 2`, `unreferenced_by_name: 30`
* *Architecture:* `api: 179`, `concurrency: 34`, `import: 2`
* *Defense:* `safety: 1`, `doc: 101`, `sync_locks: 83`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` C, fmt, bits, runtime, sync, atomic, unsafe
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/asm/x86_64-xlate.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2201.74 | **LOC:** 1974 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 6.226; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Complexity Load (formerly Cognitive Load) (87.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `re` **(Many-Argument Workhorses)** (Impact: 265.1)
  * `re` **(Compute Cores)** (Impact: 114.3)
  * `out` **(Compute Cores)** (Impact: 76.3)
  * `out` **(Compute Cores)** (Impact: 44.4)
  * `xdata` **(Compute Cores)** (Impact: 44.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 11 instances
* *Amplified Cascading Flux:* 423 instances
* *High Risk Execution (weighted view):* 2
* *Memory Alloc (weighted view):* 13
* *State Mutation (weighted view):* 1270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 582`, `structural_boundaries: 333`, `args: 44`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 3`, `state_mutation: 424`, `dead_code: 6`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 34`, `import: 5`
* *Defense:* `safety: 1`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DWP_OP_reg, DW_OP_bregX, assembler, dynamic, even, following, integer, multiple...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/no_asm.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 1820.7 | **LOC:** 1346 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 9.489; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mul_mont_n` **(Many-Argument Workhorses)** (Impact: 26.5)
    * *Intent:* #if defined(__clang__) # pragma GCC diagnostic ignored "-Wstatic-in-inline" #endif #if !defined(__cl...
  * `mul_mont_nonred_n` **(Many-Argument Workhorses)** (Impact: 20.5)
    * *Intent:* /* * mul_mont_n without final conditional subtraction, which implies * that modulus is one bit short...
  * `redc_mont_n` **(Many-Argument Workhorses)** (Impact: 19.1)
  * `mul_by_3_mod_n` **(Many-Argument Workhorses)** (Impact: 17.9)
  * `from_mont_n` **(Many-Argument Workhorses)** (Impact: 16.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 423 instances
* *State Mutation (weighted view):* 1444
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 78`, `args: 66`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `state_mutation: 598`, `dead_code: 1`
* *Architecture:* `api: 17`
* *Defense:* `safety: 63`, `immutability_locks: 119`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022523
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bindings/rust/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 901.56 | **LOC:** 2386 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 6.226; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (62.0%), Guard Balance (formerly Safety Score) (59.7%), Mutation Surface (formerly State Flux) (25.9%)
- **Documentation Coverage:** 99.0476% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `verify_multiple_aggregate_signatures` **(Many-Argument Workhorses)** (Impact: 54.9)
    * *Intent:* // https://ethresear.ch/t/fast-verification-of-multiple-bls-signatures/5407
  * `aggregate_verify` **(Many-Argument Workhorses)** (Impact: 54.2)
  * `mul_n_aggregate` **(Many-Argument Workhorses)** (Impact: 34.6)
  * `aggregate` **(Many-Argument Workhorses)** (Impact: 30.9)
  * `verify_multiple_aggregate_signatures` **(Many-Argument Workhorses)** (Impact: 29.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 20 instances
* *High Risk Execution (weighted view):* 6
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 514`, `args: 173`, `func_start: 131`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 8`, `state_mutation: 31`, `dead_code: 2`, `planned_debt: 9`, `duplicate_logic: 4`, `unreferenced_by_name: 26`
* *Architecture:* `api: 89`, `concurrency: 5`, `import: 24`
* *Defense:* `safety: 9`, `doc: 2`, `test: 53`, `sync_locks: 5`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Arc, Deserializer, MaybeUninit, Once, SeedableRng, Serialize, Serializer, alloc::boxed::Box...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/exports.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 565.16 | **LOC:** 621 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 7.678; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.2%), Complexity Load (formerly Cognitive Load) (84.8%), Connectivity (formerly Api Exposure) (82.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blst_uint64_from_fp` **(Compute Cores)** (Impact: 9.6)
  * `blst_uint64_from_fr` **(Compute Cores)** (Impact: 9.6)
  * `blst_sk_inverse` **(Defensive Guards)** (Impact: 8.1)
  * `blst_scalar_from_uint64` **(Compute Cores)** (Impact: 8.1)
  * `blst_uint64_from_scalar` **(Compute Cores)** (Impact: 8.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 253
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 85`, `args: 64`, `func_start: 64`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 105`
* *Architecture:* `api: 64`, `import: 3`
* *Defense:* `safety: 23`, `immutability_locks: 100`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.678
  * `Choke Point (Betweenness):` 0.000314 | `Ripple Effect (Closeness):` 0.028829
  * `Imports (Out-Degree: 3):` bytes.h, fields.h, sha256.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/aggregate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 526.06 | **LOC:** 674 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 6.716; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.3%), Guard Balance (formerly Safety Score) (63.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PAIRING_Aggregate_PK_in_G1` **(Many-Argument Workhorses)** (Impact: 91.6)
  * `PAIRING_Aggregate_PK_in_G2` **(Many-Argument Workhorses)** (Impact: 91.3)
    * *Intent:* /* * Optional |nbits|-wide |scalar| is used to facilitate multiple aggregated * signature verificati...
  * `blst_pairing_merge` **(Compute Cores)** (Impact: 37.1)
  * `PAIRING_FinalVerify` **(Stateful Encapsulated Methods)** (Impact: 19.4)
  * `blst_aggregate_in_g1` **(Many-Argument Workhorses)** (Impact: 15.4)
    * *Intent:* /* * PAIRING context-free entry points. * * To perform FastAggregateVerify, aggregate all public key...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 94`, `args: 81`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 44`, `dead_code: 2`
* *Architecture:* `api: 25`
* *Defense:* `safety: 49`, `immutability_locks: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012012
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bindings/blst.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 506.78 | **LOC:** 959 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 14.165; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.3%), Connectivity (formerly Api Exposure) (44.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P1` **(Compute Cores)** (Impact: 9.1)
    * *Intent:* #endif
  * `P2` **(Compute Cores)** (Impact: 9.1)
    * *Intent:* #endif
  * `P1_Affine` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* #endif
  * `P2_Affine` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* #endif
  * `mult` **(Defensive Guards)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 244`, `args: 143`, `func_start: 217`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 30`, `duplicate_logic: 4`
* *Architecture:* `api: 36`, `import: 5`
* *Defense:* `safety: 8`, `immutability_locks: 368`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.165
  * `Choke Point (Betweenness):` 0.000328 | `Ripple Effect (Closeness):` 0.018018
  * `Imports (Out-Degree: 1):` blst.h, cstring, memory, string, vector
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/blst_t.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 488.54 | **LOC:** 673 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 6.226; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (98.9%), Guard Balance (formerly Safety Score) (91.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `operator^` **(Compute Cores)** (Impact: 18.6)
    * *Intent:* // simplified exponentiation, but mind the ^ operator's precedence!
  * `operator^` **(Compute Cores)** (Impact: 18.6)
    * *Intent:* // simplified exponentiation, but mind the ^ operator's precedence!
  * `from` **(Compute Cores)** (Impact: 17.0)
  * `to` **(Many-Argument Workhorses)** (Impact: 11.6)
  * `vec_left_align` **(Many-Argument Workhorses)** (Impact: 11.0)
    * *Intent:* #include "bytes.h" #undef launder // avoid conflict with C++ >=17 #ifdef __GNUC__ # pragma GCC diagn...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 236`, `args: 81`, `func_start: 97`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 67`, `duplicate_logic: 16`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `immutability_locks: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bytes.h, cstdint, vect.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/multi_scalar.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 484.72 | **LOC:** 475 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 6.716; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.9%), Complexity Load (formerly Cognitive Load) (71.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pippenger_window_size` **(Stateful Encapsulated Methods)** (Impact: 12.1)
    * *Intent:* /* * Pippenger algorithm implementation, fastest option for larger amount * of points... */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 148 instances
* *State Mutation (weighted view):* 463
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 28`, `args: 30`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 167`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 70`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.716
  * `Choke Point (Betweenness):` 3.7e-05 | `Ripple Effect (Closeness):` 0.012012
  * `Imports (Out-Degree: 2):` fields.h, point.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bindings/go/blst_minpk_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 403.16 | **LOC:** 723 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 6.226; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (94.6%), Guard Balance (formerly Safety Score) (80.1%), Complexity Load (formerly Cognitive Load) (28.0%)
- **Documentation Coverage:** 46.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestSignMultipleVerifyAggregateMinPk` **(I/O & Config Routines)** (Impact: 19.5)
  * `TestSignVerifyMinPk` **(Compute Cores)** (Impact: 19.3)
  * `TestSignVerifyAggregateMinPk` **(Compute Cores)** (Impact: 18.2)
  * `TestSignVerifyAggregateValidatesInfinitePubkeyMinPk` **(Compute Cores)** (Impact: 12.1)
  * `BenchmarkBatchUncompressMinPk` **(I/O & Config Routines)** (Impact: 11.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 58 instances
* *State Mutation (weighted view):* 179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 36`, `args: 24`, `func_start: 24`
* *Risk/State:* `state_mutation: 63`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 21`
* *Architecture:* `api: 24`, `import: 1`
* *Defense:* `safety: 5`, `doc: 26`, `test: 20`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rand, fmt, runtime, testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/asm/sha256-x86_64.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 319.26 | **LOC:** 808 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 6.226; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Complexity Load (formerly Cognitive Load) (56.6%), Debt Markers (formerly Tech Debt) (9.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SSSE3_256_00_47` **(Many-Argument Workhorses)** (Impact: 16.5)
  * `sha256op38` **(Compute Cores)** (Impact: 6.5)
  * `AUTOLOAD` **(Interface Declarations)** (Impact: 3.3)
  * `body_00_15` **(I/O & Config Routines)** (Impact: 2.0)
  * `Xupdate_256_SSSE3` **(I/O & Config Routines)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 52 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 34`, `args: 9`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 106`, `high_risk_execution: 2`, `state_mutation: 166`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 5`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` scalar
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/e1.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 313.9 | **LOC:** 565 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 7.678; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (96.6%), Mutation Surface (formerly State Flux) (90.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blst_p1_mult` **(Many-Argument Workhorses)** (Impact: 23.8)
  * `POINTonE1_Uncompress_Z` **(Stateful Encapsulated Methods)** (Impact: 13.7)
  * `POINTonE1_Deserialize_BE` **(Stateful Encapsulated Methods)** (Impact: 10.2)
  * `POINTonE1_Deserialize_Z` **(Stateful Encapsulated Methods)** (Impact: 9.7)
  * `blst_sign_pk2_in_g2` **(Many-Argument Workhorses)** (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 70`, `args: 90`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `state_mutation: 28`, `fragile_debt: 16`
* *Architecture:* `api: 33`, `import: 5`
* *Defense:* `safety: 7`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.678
  * `Choke Point (Betweenness):` 0.00061 | `Ripple Effect (Closeness):` 0.028829
  * `Imports (Out-Degree: 5):` ec_mult.h, ec_ops.h, errors.h, fields.h, point.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/e2.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 312.74 | **LOC:** 639 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 7.678; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (95.9%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (74.9%), Guard Balance (formerly Safety Score) (68.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blst_p2_mult` **(Many-Argument Workhorses)** (Impact: 23.8)
  * `POINTonE2_Deserialize_BE` **(Stateful Encapsulated Methods)** (Impact: 12.4)
  * `POINTonE2_Uncompress_Z` **(Stateful Encapsulated Methods)** (Impact: 11.8)
  * `POINTonE2_Deserialize_Z` **(Stateful Encapsulated Methods)** (Impact: 9.7)
  * `POINTonE2_Uncompress_BE` **(Stateful Encapsulated Methods)** (Impact: 8.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 73`, `args: 90`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `state_mutation: 26`, `fragile_debt: 18`
* *Architecture:* `api: 32`, `import: 5`
* *Defense:* `safety: 7`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.678
  * `Choke Point (Betweenness):` 0.00061 | `Ripple Effect (Closeness):` 0.028829
  * `Imports (Out-Degree: 5):` ec_mult.h, ec_ops.h, errors.h, fields.h, point.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/vect.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 307.54 | **LOC:** 432 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **4**; blast radius 91.135; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.8%), Guard Balance (formerly Safety Score) (86.6%), Connectivity (formerly Api Exposure) (85.4%), Complexity Load (formerly Cognitive Load) (65.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vec_select` **(Stateful Encapsulated Methods)** (Impact: 40.7)
  * `vec_zero` **(Stateful Encapsulated Methods)** (Impact: 7.5)
  * `vec_is_equal` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `vec_is_zero` **(Stateful Encapsulated Methods)** (Impact: 6.1)
  * `vec_cswap` **(Stateful Encapsulated Methods)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 122`, `args: 94`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 45`
* *Architecture:* `api: 80`, `import: 4`
* *Defense:* `safety: 28`, `immutability_locks: 168`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 91.135
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.136824
  * `Imports (Out-Degree: 0):` alloca.h, malloc.h, stddef.h, stdlib.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/asm/sha256-armv8.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 296.88 | **LOC:** 555 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 6.226; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Complexity Load (formerly Cognitive Load) (63.1%), Debt Markers (formerly Tech Debt) (10.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unsha256` **(Compute Cores)** (Impact: 10.8)
  * `Xupdate` **(I/O & Config Routines)** (Impact: 6.8)
  * `Dscalar` **(Compute Cores)** (Impact: 4.3)
  * `Dlo` **(Compute Cores)** (Impact: 4.3)
  * `Dhi` **(Compute Cores)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 236
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 37`, `args: 12`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 76`, `high_risk_execution: 1`, `state_mutation: 126`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 9`, `import: 2`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` integer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/rust/src/pippenger.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 278.04 | **LOC:** 549 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 6.226; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (82.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (54.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mult` **(Many-Argument Workhorses)** (Impact: 69.7)
  * `validate` **(Compute Cores)** (Impact: 25.6)
  * `breakdown` **(Many-Argument Workhorses)** (Impact: 17.8)
  * `add` **(Compute Cores)** (Impact: 16.9)
  * `from` **(Compute Cores)** (Impact: 10.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 172`, `args: 19`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 36`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `concurrency: 2`, `import: 4`
* *Defense:* `test: 2`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IndexMut, core::num::Wrapping, core::ops::Index, core::slice::SliceIndex, std::sync::Barrier
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ec_mult.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 258.62 | **LOC:** 316 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 8.837; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Complexity Load (formerly Cognitive Load) (54.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_wval_limb` **(Stateful Encapsulated Methods)** (Impact: 4.8)
    * *Intent:* /* Works up to 25 bits. */
  * `get_wval` **(Stateful Encapsulated Methods)** (Impact: 2.5)
    * *Intent:* /* * Copyright Supranational LLC * Licensed under the Apache License, Version 2.0, see LICENSE for d...
  * `booth_encode` **(Stateful Encapsulated Methods)** (Impact: 2.3)
    * *Intent:* /* * Window value encoding that utilizes the fact that -P is trivially * calculated, which allows to...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 10`, `args: 9`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 91`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 16`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.837
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.029484
  * `Imports (Out-Degree: 1):` point.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/keygen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 239.2 | **LOC:** 320 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 7.678; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.2%), Complexity Load (formerly Cognitive Load) (84.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `keygen` **(Many-Argument Workhorses)** (Impact: 33.9)
    * *Intent:* #ifndef __BLST_HKDF_TESTMODE__
  * `HKDF_Expand` **(Many-Argument Workhorses)** (Impact: 24.7)
  * `HMAC_init` **(Stateful Encapsulated Methods)** (Impact: 16.0)
  * `parent_SK_to_lamport_PK` **(Many-Argument Workhorses)** (Impact: 13.7)
  * `HKDF_Extract` **(Stateful Encapsulated Methods)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 39`, `args: 27`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 40`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `safety: 22`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.678
  * `Choke Point (Betweenness):` 0.000382 | `Ripple Effect (Closeness):` 0.028829
  * `Imports (Out-Degree: 3):` bytes.h, consts.h, sha256.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/asm/arm-xlate.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 238.7 | **LOC:** 516 | **CtrlFlow:** 50.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 6.226; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.7%), Complexity Load (formerly Cognitive Load) (88.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expand_line` **(Compute Cores)** (Impact: 37.9)
  * `range` **(Parameter Forwarders)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 139`, `args: 17`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 63`, `dead_code: 3`
* *Architecture:* `io: 3`, `api: 2`, `import: 1`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/asm/mulq_mont_384-x86_64.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 229.46 | **LOC:** 2755 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (62.1%), Guard Balance (formerly Safety Score) (61.0%), Complexity Load (formerly Cognitive Load) (8.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 41 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 168
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 57`, `args: 2`
* *Risk/State:* `state_mutation: 86`
* *Architecture:* `io: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bytes.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 226.96 | **LOC:** 153 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); blast radius 36.994; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bytes_from_hexascii` **(Stateful Encapsulated Methods)** (Impact: 16.9)
  * `limbs_from_hexascii` **(Stateful Encapsulated Methods)** (Impact: 16.9)
  * `le_bytes_from_limbs` **(Stateful Encapsulated Methods)** (Impact: 15.2)
  * `limbs_from_be_bytes` **(Stateful Encapsulated Methods)** (Impact: 4.8)
  * `limbs_from_le_bytes` **(Stateful Encapsulated Methods)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 13`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 55`
* *Architecture:* `api: 7`
* *Defense:* `safety: 11`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.994
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.094159
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `bindings/blst.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 224.8 | **LOC:** 491 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 19.588; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.2%), Complexity Load (formerly Cognitive Load) (4.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 207`, `args: 185`, `class_start: 13`
* *Risk/State:* None
* *Architecture:* `api: 202`, `import: 4`
* *Defense:* `safety: 93`, `immutability_locks: 279`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.588
  * `Choke Point (Betweenness):` 0.000246 | `Ripple Effect (Closeness):` 0.024024
  * `Imports (Out-Degree: 1):` blst_aux.h, stdbool.h, stddef.h, stdint.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/pairing.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 214.18 | **LOC:** 494 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 6.716; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.7%), Complexity Load (formerly Cognitive Load) (42.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blst_miller_loop_n` **(Many-Argument Workhorses)** (Impact: 20.1)
    * *Intent:* #ifndef MILLER_LOOP_N_MAX # define MILLER_LOOP_N_MAX 16 #endif
  * `miller_loop_n` **(Many-Argument Workhorses)** (Impact: 20.0)
  * `line_add` **(Many-Argument Workhorses)** (Impact: 12.1)
    * *Intent:* /* * Copyright Supranational LLC * Licensed under the Apache License, Version 2.0, see LICENSE for d...
  * `add_n_dbl_n` **(Stateful Encapsulated Methods)** (Impact: 11.6)
  * `blst_miller_loop` **(Compute Cores)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 24`, `args: 90`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `safety: 12`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.716
  * `Choke Point (Betweenness):` 3.7e-05 | `Ripple Effect (Closeness):` 0.012012
  * `Imports (Out-Degree: 2):` fields.h, point.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bindings/node.js/blst.hpp.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 207.6 | **LOC:** 240 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.8%), Complexity Load (formerly Cognitive Load) (8.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `core_verify` **(State Mutators)** (Impact: 7.7)
  * `core_verify` **(State Mutators)** (Impact: 7.7)
  * `hash_to` **(Compute Cores)** (Impact: 6.0)
  * `encode_to` **(Compute Cores)** (Impact: 6.0)
  * `hash_to` **(Compute Cores)** (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 48`, `args: 93`, `func_start: 93`, `class_start: 18`
* *Risk/State:* `duplicate_logic: 42`
* *Architecture:* `api: 34`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.226
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/fp12_tower.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 184.14 | **LOC:** 790 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 6.716; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.5%), Connectivity (formerly Api Exposure) (13.4%), Complexity Load (formerly Cognitive Load) (8.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mul_fp2x2` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `sqr_fp12` **(Stateful Encapsulated Methods)** (Impact: 6.8)
    * *Intent:* #endif
  * `sqr_fp2x2` **(Stateful Encapsulated Methods)** (Impact: 6.0)
  * `blst_bendian_from_fp12` **(Defensive Guards)** (Impact: 5.9)
  * `mul_by_xy00z0_fp12` **(Stateful Encapsulated Methods)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 52`, `args: 51`, `func_start: 47`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 15`, `import: 1`
* *Defense:* `safety: 6`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.716
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.012012
  * `Imports (Out-Degree: 1):` fields.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `bindings/go/blst.go` -> Churn: **100.0%** | Cog Load: 63.5937% | Debt: 30.6942%
- `src/keygen.c` -> Churn: **63.09%** | Cog Load: 84.8479% | Debt: 0.0%
- `bindings/go/rb_tree.go` -> Churn: **63.09%** | Cog Load: 71.3623% | Debt: 24.2081%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `bindings/go/blst.go` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 3296.72
- `src/exports.c` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 565.16
- `bindings/blst.hpp` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 506.78
- `src/multi_scalar.c` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 484.72
- `bindings/go/blst_minpk_test.go` -> **radik878** (100.0% isolated ownership) | Magnitude: 403.16

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/e1.c` -> **Severity: 0.055** (Bridge: 0.0006 * Flux: 90.6079%)
- `src/vect.c` -> **Severity: 0.049** (Bridge: 0.0005 * Flux: 99.7458%)
- `src/e2.c` -> **Severity: 0.046** (Bridge: 0.0006 * Flux: 74.8525%)
- `src/keygen.c` -> **Severity: 0.038** (Bridge: 0.0004 * Flux: 100.0%)
- `src/exports.c` -> **Severity: 0.031** (Bridge: 0.0003 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/vect.h` -> **Severity: 11.848** (Embedded: 0.1368 * Error Risk: 86.5942%)
- `src/bytes.h` -> **Severity: 9.394** (Embedded: 0.0942 * Error Risk: 99.764%)
- `src/sha256.h` -> **Severity: 3.157** (Embedded: 0.0368 * Error Risk: 85.8149%)
- `src/ec_mult.h` -> **Severity: 2.925** (Embedded: 0.0295 * Error Risk: 99.205%)
- `src/exports.c` -> **Severity: 2.714** (Embedded: 0.0288 * Error Risk: 94.1513%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/vect.h` -> **Severity: 9113.5** (Blast Radius: 91.135 * Doc Risk: 100.0%)
- `src/fields.h` -> **Severity: 4078.1** (Blast Radius: 40.781 * Doc Risk: 100.0%)
- `src/bytes.h` -> **Severity: 3699.4** (Blast Radius: 36.994 * Doc Risk: 100.0%)
- `bindings/blst.hpp` -> **Severity: 1416.5** (Blast Radius: 14.165 * Doc Risk: 100.0%)
- `src/sha256.h` -> **Severity: 1384.0** (Blast Radius: 13.84 * Doc Risk: 100.0%)

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
