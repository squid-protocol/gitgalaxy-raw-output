# ARCHITECTURAL_BRIEF: blst
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/supranational/blst.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 116 analyzed artifact(s), 38655 LOC.
- **Load-bearing artifact:** `src/vect.h` -- 22 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `bindings/rust/src/lib.rs` -- pulls in 23 dependencies, the widest assembly point in the scan.
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
| Analyzed Artifacts (Scanned) | 116 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 131 |
| Total LOC | 38655 |
| Volatility Index | 0.009 |
| % Scanned of codebase = | 47.0% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2865 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3269 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7753 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 37 | 9166 | 31.9% |
| PERL | 25 | 18261 | 21.6% |
| JSON | 7 | 573 | 6.0% |
| MARKDOWN | 6 | 0 | 5.2% |
| GO | 6 | 3717 | 5.2% |
| RUST | 6 | 3321 | 5.2% |
| PYTHON | 5 | 484 | 4.3% |
| YAML | 4 | 399 | 3.4% |
| CPP | 4 | 1910 | 3.4% |
| SHELL | 3 | 180 | 2.6% |
| ZIG | 3 | 136 | 2.6% |
| JAVASCRIPT | 2 | 49 | 1.7% |
| TYPESCRIPT | 2 | 230 | 1.7% |
| CSHARP | 1 | 60 | 0.9% |
| HTML | 1 | 38 | 0.9% |
| ASSEMBLY | 1 | 0 | 0.9% |
| MAKEFILE | 1 | 19 | 0.9% |
| JAVA | 1 | 50 | 0.9% |
| BATCH | 1 | 62 | 0.9% |

## 4.1 SOURCE ENCODINGS
All 116 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 37%, Data / Markup / Trivial 18%, Large Core Modules (3) 12%, Compute Cores Files 7%, Encapsulated Accessors Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 110 | 94.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 5.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 131*

**Composition by Extension & Reason:**
- `.s`: 79x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.asm`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.me`: 5x Excluded (Unsupported Extension: '.me')
- `.tgo`: 4x Unsupported Format (.tgo)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
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
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.9 | 26.0 | 13.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.1 | 42.3 | 54.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 15.7 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 85.4 | 9.0 | 1.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 56.6 | 0.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 55.5 | 83.2 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.8 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 48.2 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 454 | 50 | 6 | `bindings/go/blst.go` |
| cleanup | 83 | 34 | 2 | `src/asm/x86_64-xlate.pl` |
| guards | 2896 | 51 | 87 | `bindings/blst.hpp` |
| danger | 601 | 58 | 12 | `src/asm/sha256-x86_64.pl` |
| concurrency | 143 | 5 | 0 | `bindings/go/blst.go` |
| connectivity | 845 | 59 | 21 | `bindings/go/blst.go` |
| io | 172 | 35 | 2 | `build.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 38 | 9 | 0 | `src/asm/sha256-portable-x86_64.pl` |
| time | 0 | 0 | 0 | - |
| serialization | 4 | 2 | 0 | `bindings/go/blst_htoc_test.go` |
| regex | 545 | 31 | 6 | `src/asm/x86_64-xlate.pl` |
| events | 2 | 1 | 0 | `bindings/c#/poc.cs` |
| tests | 126 | 11 | 0 | `bindings/rust/src/lib.rs` |
| docs | 281 | 10 | 0 | `bindings/emscripten/build.py` |
| debt | 341 | 48 | 13 | `.github/workflows/ci.yml` |
| mutation | 5684 | 87 | 101 | `src/no_asm.h` |
| dead_code | 1128 | 25 | 2 | `src/recip-addchain.h` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 51 | 12 | 1 | `src/ec_ops.h` |
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

1. **vect.h** (`src/vect.h`) — 22 inbound connections
2. **fields.h** (`src/fields.h`) — 12 inbound connections
3. **bytes.h** (`src/bytes.h`) — 9 inbound connections
4. **vect.c** (`src/vect.c`) — 9 inbound connections
5. **point.h** (`src/point.h`) — 8 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`bindings/rust/src/lib.rs`) — 23 outbound dependencies
2. **server.c** (`src/server.c`) — 20 outbound dependencies
3. **README.md** (`README.md`) — 14 outbound dependencies
4. **client_min_pk.c** (`src/client_min_pk.c`) — 11 outbound dependencies
5. **client_min_sig.c** (`src/client_min_sig.c`) — 11 outbound dependencies

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
| `src` | 37 | 6656.74 | 31.07% | 7.87% |
| `src/asm` | 25 | 5362.72 | 31.94% | 1.25% |
| `bindings/go` | 10 | 4070.22 | 26.78% | 20.85% |
| `bindings/rust/src` | 4 | 1214.38 | 20.38% | 47.3% |
| `bindings` | 3 | 556.66 | 2.52% | 15.02% |
| `bindings/node.js` | 6 | 307.7 | 17.36% | 22.96% |
| `__monolith__` | 7 | 209.0 | 15.81% | 5.39% |
| `bindings/java` | 3 | 161.0 | 54.61% | 32.36% |
| `bindings/vectors/hash_to_curve` | 7 | 102.32 | 0.0% | 0.0% |
| `bindings/rust/benches` | 1 | 102.02 | 8.2% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `bindings/node.js/blst.hpp.ts` -> **100.0%** Exposure
- `src/blst_t.hpp` -> **99.5028%** Exposure
- `bindings/java/runnable.java` -> **97.0688%** Exposure
- `src/e1.c` -> **96.1368%** Exposure
- `src/e2.c` -> **95.4529%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `bindings/go/generate.py` -> **100.0%** Exposure
- `bindings/node.js/blst_wrap.py` -> **100.0%** Exposure
- `bindings/zig/generate.py` -> **100.0%** Exposure
- `bindings/go/blst.go` -> **100.0%** Exposure
- `bindings/go/rb_tree.go` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `bindings/node.js/blst.hpp.ts` -> **0** Orphaned Functions | **42** Duplicates
- `bindings/go/blst.go` -> **30** Orphaned Functions | **0** Duplicates
- `bindings/rust/src/lib.rs` -> **26** Orphaned Functions | **4** Duplicates
- `bindings/go/blst_minpk_test.go` -> **21** Orphaned Functions | **0** Duplicates
- `src/blst_t.hpp` -> **0** Orphaned Functions | **18** Duplicates

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
- **Unknown Dependencies:** `243` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `bindings/go/blst.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.619)
- **Top Global Matches:** file_cluster_4: 7.619, file_cluster_15: 10.192, file_cluster_10: 10.628
- **Magnitude:** 3296.72 | **LOC:** 3631 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 19.999; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.3%), Complexity Load (formerly Cognitive Load) (63.6%)
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
* *Risk/State:* `high_risk_execution: 23`, `state_mutation: 397`, `dead_code: 16`, `planned_debt: 2`, `unreferenced_by_name: 30`
* *Architecture:* `api: 179`, `concurrency: 34`, `import: 2`
* *Defense:* `safety: 1`, `doc: 101`, `sync_locks: 83`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.999
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.026087
  * `Imports (Out-Degree: 0):` C, fmt, bits, runtime, sync, atomic, unsafe
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/asm/x86_64-xlate.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.575)
- **Top Global Matches:** file_cluster_8: 7.575, file_cluster_6: 11.217, file_cluster_4: 19.534
- **Magnitude:** 2201.74 | **LOC:** 1974 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 5.633; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.8%), Complexity Load (formerly Cognitive Load) (87.0%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 3`, `state_mutation: 424`, `dead_code: 5`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 34`, `import: 5`
* *Defense:* `safety: 1`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.633
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assembler, integer, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/no_asm.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.947)
- **Top Global Matches:** file_cluster_16: 6.947, file_cluster_15: 7.005, file_cluster_17: 8.343
- **Magnitude:** 1820.7 | **LOC:** 1346 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); blast radius 20.879; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (59.4%)
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
* *Structure:* `branch: 82`, `structural_boundaries: 78`, `args: 66`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `state_mutation: 598`
* *Architecture:* `api: 17`
* *Defense:* `safety: 63`, `immutability_locks: 119`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.879
  * `Choke Point (Betweenness):` 0.000496 | `Ripple Effect (Closeness):` 0.09821
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `bindings/rust/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.002)
- **Top Global Matches:** file_cluster_12: 8.002, file_cluster_0: 8.326, file_cluster_5: 8.386
- **Magnitude:** 893.96 | **LOC:** 2386 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **23**; blast radius 15.21; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (62.0%), Guard Balance (formerly Safety Score) (53.3%), Mutation Surface (formerly State Flux) (25.9%)
- **Documentation Coverage:** 99.0476% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `verify_multiple_aggregate_signatures` **(Many-Argument Workhorses)** (Impact: 54.9)
    * *Intent:* // https://ethresear.ch/t/fast-verification-of-multiple-bls-signatures/5407
  * `aggregate_verify` **(Many-Argument Workhorses)** (Impact: 54.2)
  * `mul_n_aggregate` **(Many-Argument Workhorses)** (Impact: 31.5)
  * `verify_multiple_aggregate_signatures` **(Many-Argument Workhorses)** (Impact: 29.4)
  * `aggregate` **(Many-Argument Workhorses)** (Impact: 28.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 20 instances
* *High Risk Execution (weighted view):* 6
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 514`, `args: 173`, `func_start: 131`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 8`, `state_mutation: 31`, `dead_code: 2`, `planned_debt: 9`, `duplicate_logic: 4`, `unreferenced_by_name: 26`
* *Architecture:* `api: 89`, `concurrency: 5`, `import: 24`
* *Defense:* `safety: 9`, `doc: 2`, `test: 53`, `sync_locks: 5`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.21
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.017391
  * `Imports (Out-Degree: 0):` alloc, alloc::boxed::Box, alloc::vec, alloc::vec::Vec, core::any::Any, core::mem::MaybeUninit, core::mem::transmute, core::ptr...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/exports.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.532)
- **Top Global Matches:** file_cluster_15: 6.532, file_cluster_12: 7.094, file_cluster_16: 8.809
- **Magnitude:** 565.16 | **LOC:** 621 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 7.855; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.8%), Connectivity (formerly Api Exposure) (82.9%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.855
  * `Choke Point (Betweenness):` 0.000534 | `Ripple Effect (Closeness):` 0.042609
  * `Imports (Out-Degree: 5):` bytes.h, fields.h, sha256.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/aggregate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.663)
- **Top Global Matches:** file_cluster_4: 6.663, file_cluster_6: 9.263, file_cluster_12: 12.9
- **Magnitude:** 526.06 | **LOC:** 674 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 6.984; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.9%), Guard Balance (formerly Safety Score) (54.0%)
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
* *Structure:* `branch: 104`, `structural_boundaries: 94`, `args: 81`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 44`
* *Architecture:* `api: 25`
* *Defense:* `safety: 49`, `immutability_locks: 88`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.984
  * `Choke Point (Betweenness):` 3.3e-05 | `Ripple Effect (Closeness):` 0.027174
  * `Imports (Out-Degree: 7):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `bindings/blst.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.69)
- **Top Global Matches:** file_cluster_15: 7.69, file_cluster_11: 8.281, file_cluster_12: 9.282
- **Magnitude:** 517.38 | **LOC:** 959 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 12.816; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.3%), Debt Markers (formerly Tech Debt) (45.1%), Connectivity (formerly Api Exposure) (44.4%)
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
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 244`, `args: 143`, `func_start: 227`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 30`, `duplicate_logic: 8`
* *Architecture:* `api: 36`, `import: 5`
* *Defense:* `safety: 8`, `immutability_locks: 368`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.816
  * `Choke Point (Betweenness):` 0.004424 | `Ripple Effect (Closeness):` 0.017391
  * `Imports (Out-Degree: 12):` blst.h, cstring, memory, string, vector
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/blst_t.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.542)
- **Top Global Matches:** file_cluster_15: 6.542, file_cluster_11: 7.76, file_cluster_16: 8.58
- **Magnitude:** 486.74 | **LOC:** 673 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.633; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Debt Markers (formerly Tech Debt) (99.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.2%)
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
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 236`, `args: 81`, `func_start: 99`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 67`, `duplicate_logic: 18`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `immutability_locks: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.633
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` bytes.h, cstdint, vect.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/go/blst_minpk_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.506)
- **Top Global Matches:** file_cluster_15: 7.506, file_cluster_10: 7.874, file_cluster_16: 8.628
- **Magnitude:** 403.16 | **LOC:** 723 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 5.633; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (94.3%), Guard Balance (formerly Safety Score) (61.3%), Complexity Load (formerly Cognitive Load) (28.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.633
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` rand, fmt, runtime, testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/asm/sha256-x86_64.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.726)
- **Top Global Matches:** file_cluster_7: 7.726, file_cluster_14: 8.341, file_cluster_12: 10.561
- **Magnitude:** 319.26 | **LOC:** 808 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.3%), Complexity Load (formerly Cognitive Load) (56.6%), Debt Markers (formerly Tech Debt) (8.7%)
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
* *Risk/State:* `safety_bypasses: 106`, `high_risk_execution: 2`, `state_mutation: 166`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 5`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.633
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/e1.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.457)
- **Top Global Matches:** file_cluster_16: 6.457, file_cluster_15: 6.885, file_cluster_11: 8.574
- **Magnitude:** 311.9 | **LOC:** 565 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **5**; blast radius 9.707; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (96.1%), Mutation Surface (formerly State Flux) (90.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.7%)
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
* *Structure:* `branch: 43`, `structural_boundaries: 70`, `args: 90`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `state_mutation: 28`, `fragile_debt: 16`
* *Architecture:* `api: 33`, `import: 5`
* *Defense:* `safety: 7`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.707
  * `Choke Point (Betweenness):` 0.002379 | `Ripple Effect (Closeness):` 0.058696
  * `Imports (Out-Degree: 11):` ec_mult.h, ec_ops.h, errors.h, fields.h, point.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/e2.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.359)
- **Top Global Matches:** file_cluster_16: 6.359, file_cluster_15: 6.695, file_cluster_11: 8.443
- **Magnitude:** 310.74 | **LOC:** 639 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **5**; blast radius 9.707; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (95.5%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (74.9%), Guard Balance (formerly Safety Score) (56.1%)
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
* *Structure:* `branch: 44`, `structural_boundaries: 73`, `args: 90`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `state_mutation: 26`, `fragile_debt: 18`
* *Architecture:* `api: 32`, `import: 5`
* *Defense:* `safety: 7`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.707
  * `Choke Point (Betweenness):` 0.002379 | `Ripple Effect (Closeness):` 0.058696
  * `Imports (Out-Degree: 11):` ec_mult.h, ec_ops.h, errors.h, fields.h, point.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/vect.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.917)
- **Top Global Matches:** file_cluster_12: 8.917, file_cluster_16: 9.668, file_cluster_7: 10.421
- **Magnitude:** 301.74 | **LOC:** 432 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **4**; blast radius 122.604; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.8%), Connectivity (formerly Api Exposure) (85.4%), Guard Balance (formerly Safety Score) (64.6%), Complexity Load (formerly Cognitive Load) (57.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vec_select` **(Stateful Encapsulated Methods)** (Impact: 38.2)
  * `vec_is_equal` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `vec_is_zero` **(Stateful Encapsulated Methods)** (Impact: 6.1)
  * `vec_cswap` **(Stateful Encapsulated Methods)** (Impact: 5.4)
  * `vec_czero` **(Stateful Encapsulated Methods)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 121`, `args: 94`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 45`
* *Architecture:* `api: 80`, `import: 4`
* *Defense:* `safety: 28`, `immutability_locks: 168`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 122.604
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.20148
  * `Imports (Out-Degree: 0):` alloca.h, malloc.h, stddef.h, stdlib.h
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `src/asm/sha256-armv8.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.744)
- **Top Global Matches:** file_cluster_7: 7.744, file_cluster_14: 8.027, file_cluster_12: 10.686
- **Magnitude:** 296.88 | **LOC:** 555 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 5.633; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.9%), Complexity Load (formerly Cognitive Load) (63.1%), Debt Markers (formerly Tech Debt) (9.2%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.633
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` integer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/rust/src/pippenger.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.377)
- **Top Global Matches:** file_cluster_6: 7.377, file_cluster_4: 9.181, file_cluster_12: 15.811
- **Magnitude:** 278.04 | **LOC:** 549 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 5.633; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.6%), Complexity Load (formerly Cognitive Load) (54.5%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.633
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core::num::Wrapping, core::ops::Index, core::ops::IndexMut, core::slice::SliceIndex, std::sync::Barrier
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/asm/arm-xlate.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.754)
- **Top Global Matches:** file_cluster_3: 8.754, file_cluster_8: 21.222, file_cluster_6: 33.785
- **Magnitude:** 238.7 | **LOC:** 516 | **CtrlFlow:** 50.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 5.633; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.1%), Guard Balance (formerly Safety Score) (73.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expand_line` **(Compute Cores)** (Impact: 37.9)
  * `range` **(Parameter Forwarders)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 139`, `args: 17`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 63`, `dead_code: 1`
* *Architecture:* `io: 3`, `api: 2`, `import: 1`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.633
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/asm/mulq_mont_384-x86_64.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.271)
- **Top Global Matches:** file_cluster_2: 3.271, file_cluster_17: 5.249, file_cluster_13: 6.107
- **Magnitude:** 229.46 | **LOC:** 2755 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (62.1%), Guard Balance (formerly Safety Score) (53.6%), Complexity Load (formerly Cognitive Load) (8.8%), Test Surface (formerly Verification) (2.3%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.633
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/keygen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.198)
- **Top Global Matches:** file_cluster_16: 6.198, file_cluster_15: 7.282, file_cluster_12: 8.168
- **Magnitude:** 227.9 | **LOC:** 320 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 7.855; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.0%), Guard Balance (formerly Safety Score) (63.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `keygen` **(Many-Argument Workhorses)** (Impact: 33.9)
    * *Intent:* #ifndef __BLST_HKDF_TESTMODE__
  * `HMAC_init` **(Stateful Encapsulated Methods)** (Impact: 16.0)
  * `parent_SK_to_lamport_PK` **(Many-Argument Workhorses)** (Impact: 13.7)
  * `HKDF_Expand` **(Many-Argument Workhorses)** (Impact: 13.4)
  * `HKDF_Extract` **(Stateful Encapsulated Methods)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 39`, `args: 27`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 40`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `safety: 22`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.855
  * `Choke Point (Betweenness):` 0.000536 | `Ripple Effect (Closeness):` 0.042609
  * `Imports (Out-Degree: 4):` bytes.h, consts.h, sha256.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/bytes.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.248)
- **Top Global Matches:** file_cluster_16: 5.248, file_cluster_15: 8.074, file_cluster_17: 8.459
- **Magnitude:** 226.96 | **LOC:** 153 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); blast radius 33.682; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.2%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 33.682
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.126087
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `bindings/node.js/blst.hpp.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.239)
- **Top Global Matches:** file_cluster_15: 6.239, file_cluster_11: 7.262, file_cluster_2: 7.662
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.633
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pairing.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.082)
- **Top Global Matches:** file_cluster_16: 6.082, file_cluster_15: 7.313, file_cluster_12: 8.208
- **Magnitude:** 198.28 | **LOC:** 494 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 7.832; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.2%), Complexity Load (formerly Cognitive Load) (39.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `blst_miller_loop_n` **(Many-Argument Workhorses)** (Impact: 20.1)
    * *Intent:* #ifndef MILLER_LOOP_N_MAX # define MILLER_LOOP_N_MAX 16 #endif
  * `add_n_dbl_n` **(Stateful Encapsulated Methods)** (Impact: 11.6)
  * `miller_loop_n` **(Many-Argument Workhorses)** (Impact: 11.0)
  * `blst_miller_loop` **(Compute Cores)** (Impact: 6.2)
  * `start_dbl_n` **(Stateful Encapsulated Methods)** (Impact: 5.3)
    * *Intent:* #endif
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 24`, `args: 90`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `safety: 12`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.832
  * `Choke Point (Betweenness):` 0.000184 | `Ripple Effect (Closeness):` 0.034783
  * `Imports (Out-Degree: 4):` fields.h, point.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/multi_scalar.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.0)
- **Top Global Matches:** file_cluster_9: 8.0, file_cluster_16: 12.138, file_cluster_12: 12.969
- **Magnitude:** 194.72 | **LOC:** 475 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 6.076; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (58.5%), Guard Balance (formerly Safety Score) (55.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pippenger_window_size` **(Stateful Encapsulated Methods)** (Impact: 12.1)
    * *Intent:* /* * Pippenger algorithm implementation, fastest option for larger amount * of points... */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 28`, `args: 30`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 167`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 70`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.076
  * `Choke Point (Betweenness):` 3.5e-05 | `Ripple Effect (Closeness):` 0.011594
  * `Imports (Out-Degree: 2):` fields.h, point.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/asm/ctx_inverse_mod_384-x86_64.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.59)
- **Top Global Matches:** file_cluster_2: 3.59, file_cluster_13: 5.33, file_cluster_17: 5.391
- **Magnitude:** 182.7 | **LOC:** 1070 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Guard Balance (formerly Safety Score) (58.2%), Complexity Load (formerly Cognitive Load) (20.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 48 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 50`, `args: 2`
* *Risk/State:* `state_mutation: 54`
* *Architecture:* `io: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.633
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/asm/mulx_mont_384-x86_64.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.833)
- **Top Global Matches:** file_cluster_2: 2.833, file_cluster_17: 5.047, file_cluster_13: 5.599
- **Magnitude:** 181.78 | **LOC:** 2487 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.0%), Mutation Surface (formerly State Flux) (49.8%), Complexity Load (formerly Cognitive Load) (8.3%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 34 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 53`, `args: 2`
* *Risk/State:* `state_mutation: 57`
* *Architecture:* `io: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.633
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/asm/ct_inverse_mod_256-x86_64.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.328)
- **Top Global Matches:** file_cluster_2: 3.328, file_cluster_13: 5.027, file_cluster_17: 5.254
- **Magnitude:** 169.64 | **LOC:** 845 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (59.9%), Complexity Load (formerly Cognitive Load) (26.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 46 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 141
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 39`, `args: 2`
* *Risk/State:* `state_mutation: 49`
* *Architecture:* `io: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.633
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `bindings/emscripten/runnable.js` (JAVASCRIPT) | Magnitude: 12.16 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 18, core_var_decl: 11, design_snake_case: 9, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `bindings/zig/tests.zig` (ZIG) | Magnitude: 13.54 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 67, safety: 30, core_var_decl: 27, design_snake_case: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/no_asm.h` (C) | Magnitude: 1820.7 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 782, state_mutation: 598, core_var_decl: 258, design_snake_case: 246

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `bindings/go/blst.go` -> Churn: **56.46%** | Cog Load: 63.5937% | Debt: 30.4081%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `bindings/go/blst.go` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 3296.72
- `bindings/blst.hpp` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 517.38
- `src/asm/arm-xlate.pl` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 238.7
- `src/keygen.c` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 227.9
- `src/multi_scalar.c` -> **Andy Polyakov** (100.0% isolated ownership) | Magnitude: 194.72

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/e1.c` -> **Severity: 0.216** (Bridge: 0.0024 * Flux: 90.6079%)
- `src/e2.c` -> **Severity: 0.178** (Bridge: 0.0024 * Flux: 74.8525%)
- `src/vect.c` -> **Severity: 0.115** (Bridge: 0.0011 * Flux: 99.7458%)
- `src/hash_to_field.c` -> **Severity: 0.09** (Bridge: 0.0009 * Flux: 100.0%)
- `src/keygen.c` -> **Severity: 0.054** (Bridge: 0.0005 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/vect.h` -> **Severity: 13.006** (Embedded: 0.2015 * Error Risk: 64.5528%)
- `src/bytes.h` -> **Severity: 11.043** (Embedded: 0.1261 * Error Risk: 87.5787%)
- `src/no_asm.h` -> **Severity: 9.083** (Embedded: 0.0982 * Error Risk: 92.4873%)
- `src/vect.c` -> **Severity: 7.22** (Embedded: 0.1179 * Error Risk: 61.2154%)
- `src/hash_to_field.c` -> **Severity: 4.319** (Embedded: 0.0621 * Error Risk: 69.5297%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/vect.h` -> **Severity: 12260.4** (Blast Radius: 122.604 * Doc Risk: 100.0%)
- `src/bytes.h` -> **Severity: 3368.2** (Blast Radius: 33.682 * Doc Risk: 100.0%)
- `src/fields.h` -> **Severity: 2484.3** (Blast Radius: 24.843 * Doc Risk: 100.0%)
- `src/vect.c` -> **Severity: 2343.5** (Blast Radius: 23.435 * Doc Risk: 100.0%)
- `src/no_asm.h` -> **Severity: 2087.9** (Blast Radius: 20.879 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 220 literal sites + 5 sites through wrappers = 225
- **`memory_alloc`:** 223 literal sites + 2 sites through wrappers = 225

- `PrintBytes` (function, debug_prints, primitive): 5 call sites in 1 files -- `bindings/go/blst.go`
- `init` (function, memory_alloc, primitive): 2 call sites in 1 files -- `bindings/blst.hpp`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 3829 call pairs -- scoped 24.7%, unique 12.8%, ambiguous 1.4%, external 61.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 1163 | 47.3% | 28.0% | 0.2% | 24.5% |
| go | 932 | 26.6% | 2.3% | 0.0% | 71.1% |
| rust | 846 | 6.1% | 0.0% | 0.8% | 93.0% |
| cpp | 449 | 16.0% | 31.8% | 10.2% | 41.9% |
| perl | 198 | 9.1% | 0.0% | 0.0% | 90.9% |
| python | 94 | 3.2% | 0.0% | 0.0% | 96.8% |
| shell | 39 | 0.0% | 0.0% | 0.0% | 100.0% |
| csharp | 34 | 5.9% | 0.0% | 0.0% | 94.1% |
| java | 23 | 4.3% | 0.0% | 0.0% | 95.7% |
| html | 19 | 0.0% | 0.0% | 0.0% | 100.0% |

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
