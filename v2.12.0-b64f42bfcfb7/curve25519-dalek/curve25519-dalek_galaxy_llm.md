# ARCHITECTURAL_BRIEF: curve25519-dalek
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/dalek-cryptography/curve25519-dalek.git` |
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
- **Scope:** 103 analyzed artifact(s), 31962 LOC.
- **Load-bearing artifact:** `curve25519-dalek/src/edwards.rs` -- 32 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `curve25519-dalek/src/edwards.rs` -- pulls in 72 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `curve25519-dalek/src/edwards.rs` at magnitude 567.38 (structural weight, not risk).
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
| Total Artifacts | 133 |
| Analyzed Artifacts (Scanned) | 103 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 30 |
| Total LOC | 31962 |
| Volatility Index | 0.019 |
| % Scanned of codebase = | 77.4% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4598 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0412 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 47.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5703 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 80 | 31539 | 77.7% |
| MARKDOWN | 12 | 0 | 11.7% |
| YAML | 7 | 352 | 6.8% |
| PLAINTEXT | 2 | 0 | 1.9% |
| MAKEFILE | 1 | 8 | 1.0% |
| SHELL | 1 | 63 | 1.0% |

## 4.1 SOURCE ENCODINGS
All 103 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 28%, State Mutators Files 17%, Large Core Modules (3) 15%, Declarative / Non-Code 14%, Generic / Templated Code Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 89 | 86.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 14 | 13.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 30*

**Composition by Extension & Reason:**
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 46 exceeds 500 chars), 1x Unresolved Ambiguity (No Retainable Structure)
- `.toml`: 5x Unsupported Format (.toml), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.der`: 3x Excluded (Explicitly Denied Extension: '.der')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.sage`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpeg`: 1x Excluded (Explicitly Denied Extension: '.jpeg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 43.4 | 7.1 | 3.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 32.6 | 47.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 8.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.9 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 73.0 | 33.9 | 37.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 3.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 28.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.1 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.6 | 1.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 12.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 45.9 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.8 | 1.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 379 | 29 | 7 | `curve25519-dalek/src/backend/serial/u32/field.rs` |
| cleanup | 0 | 0 | 0 | - |
| guards | 408 | 53 | 10 | `curve25519-dalek/src/backend/serial/u32/constants.rs` |
| danger | 169 | 21 | 5 | `ed25519-dalek/tests/ed25519.rs` |
| concurrency | 10 | 4 | 0 | `ed25519-dalek/tests/ed25519.rs` |
| connectivity | 990 | 79 | 27 | `curve25519-dalek/src/edwards.rs` |
| io | 76 | 3 | 0 | `curve25519-dalek/tests/build_tests.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 28 | 6 | 0 | `ed25519-dalek/tests/ed25519.rs` |
| regex | 1 | 1 | 0 | `curve25519-dalek/tests/build_tests.sh` |
| events | 3 | 1 | 0 | `curve25519-dalek-derive/src/lib.rs` |
| tests | 805 | 38 | 19 | `curve25519-dalek/src/scalar.rs` |
| docs | 4322 | 82 | 136 | `curve25519-dalek/src/scalar.rs` |
| debt | 131 | 30 | 3 | `curve25519-dalek/src/backend/vector/avx2/edwards.rs` |
| mutation | 3718 | 74 | 131 | `curve25519-dalek/src/backend/vector/ifma/field.rs` |
| dead_code | 48 | 11 | 1 | `x25519-dalek/tests/x25519_tests.rs` |
| credential | 1 | 1 | 0 | `ed25519-dalek/src/lib.rs` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 2 | 1 | 0 | `curve25519-dalek/benches/dalek_benchmarks.rs` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.125**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `curve25519-dalek/tests/build_tests.sh` (Hits: 74)
- `ed25519-dalek/tests/ed25519.rs` (Hits: 1)
- `ed25519-dalek/tests/validation_criteria.rs` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **edwards.rs** (`curve25519-dalek/src/edwards.rs`) — 32 inbound connections
2. **scalar.rs** (`curve25519-dalek/src/scalar.rs`) — 29 inbound connections
3. **traits.rs** (`curve25519-dalek/src/traits.rs`) — 25 inbound connections
4. **constants.rs** (`curve25519-dalek/src/constants.rs`) — 23 inbound connections
5. **window.rs** (`curve25519-dalek/src/window.rs`) — 16 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **edwards.rs** (`curve25519-dalek/src/edwards.rs`) — 72 outbound dependencies
2. **ristretto.rs** (`curve25519-dalek/src/ristretto.rs`) — 51 outbound dependencies
3. **scalar.rs** (`curve25519-dalek/src/scalar.rs`) — 42 outbound dependencies
4. **signing.rs** (`ed25519-dalek/src/signing.rs`) — 34 outbound dependencies
5. **montgomery.rs** (`curve25519-dalek/src/montgomery.rs`) — 28 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `process_function` **(Many-Argument Workhorses)** (@ `curve25519-dalek-derive/src/lib.rs`) -> Impact: **48.9** | LOC: 177
- `process_mod` **(Many-Argument Workhorses)** (@ `curve25519-dalek-derive/src/lib.rs`) -> Impact: **31.9** | LOC: 77
- `verify_batch` **(Many-Argument Workhorses)** (@ `ed25519-dalek/src/batch.rs`) -> Impact: **25.4** | LOC: 107
  * *Intent:* /// use getrandom::{SysRng, rand_core::{TryRng, UnwrapErr}}; /// /// # fn main() { /// let mut csprng = UnwrapErr(SysRng); /// let signing_keys: Vec<_...
- `mul` **(Many-Argument Workhorses)** (@ `curve25519-dalek/src/backend/vector/scalar_mul/vartime_double_base.rs`) -> Impact: **22.9** | LOC: 59
  * *Intent:* /// Compute \\(aA + bB\\) in variable time, where \\(B\\) is the Ed25519 basepoint.
- `mul` **(Many-Argument Workhorses)** (@ `curve25519-dalek/src/backend/serial/scalar_mul/vartime_double_base.rs`) -> Impact: **22.5** | LOC: 50
  * *Intent:* /// Compute \\(aA + bB\\) in variable time, where \\(B\\) is the Ed25519 basepoint.
- `optional_multiscalar_mul` **(Many-Argument Workhorses)** (@ `curve25519-dalek/src/backend/vector/scalar_mul/pippenger.rs`) -> Impact: **22.1** | LOC: 95
- `optional_multiscalar_mul` **(Many-Argument Workhorses)** (@ `curve25519-dalek/src/backend/serial/scalar_mul/pippenger.rs`) -> Impact: **22.0** | LOC: 94
- `verify_prehashed_strict` **(Many-Argument Workhorses)** (@ `ed25519-dalek/src/verifying.rs`) -> Impact: **19.8** | LOC: 38
  * *Intent:* /// set, this will default to an empty string. /// * `signature` is a purported Ed25519ph signature on the `prehashed_message`. /// /// # Returns /// ...
- `optional_mixed_multiscalar_mul` **(Many-Argument Workhorses)** (@ `curve25519-dalek/src/backend/serial/scalar_mul/precomputed_straus.rs`) -> Impact: **19.2** | LOC: 71
- `optional_mixed_multiscalar_mul` **(Many-Argument Workhorses)** (@ `curve25519-dalek/src/backend/vector/scalar_mul/precomputed_straus.rs`) -> Impact: **19.1** | LOC: 69

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `curve25519-dalek/src` | 13 | 2019.72 | 4.49% | 8.33% |
| `curve25519-dalek/src/backend/serial/u32` | 3 | 609.48 | 19.77% | 20.47% |
| `curve25519-dalek/src/backend/serial/u64` | 3 | 588.94 | 17.43% | 13.3% |
| `ed25519-dalek/src` | 9 | 586.98 | 2.95% | 5.0% |
| `curve25519-dalek/src/backend/vector/ifma` | 3 | 442.34 | 20.64% | 3.08% |
| `curve25519-dalek/src/backend/vector/avx2` | 3 | 329.78 | 4.76% | 25.32% |
| `ed25519-dalek/tests` | 4 | 202.9 | 1.92% | 0.0% |
| `curve25519-dalek-derive/src` | 1 | 197.36 | 19.43% | 9.44% |
| `curve25519-dalek/src/backend/vector/scalar_mul` | 5 | 183.18 | 18.86% | 0.0% |
| `curve25519-dalek/src/backend/serial/scalar_mul` | 5 | 175.0 | 21.16% | 2.62% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `x25519-dalek/src/x25519.rs` -> **100.0%** Exposure
- `curve25519-dalek/build.rs` -> **73.8413%** Exposure
- `.github/workflows/workspace.yml` -> **54.4525%** Exposure
- `.github/workflows/curve25519-dalek.yml` -> **53.864%** Exposure
- `curve25519-dalek/src/backend/serial/u32/field.rs` -> **50.9764%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `curve25519-dalek/src/backend/serial/scalar_mul/variable_base.rs` -> **99.9994%** Exposure
- `curve25519-dalek/src/backend/serial/u32/field.rs` -> **99.9954%** Exposure
- `curve25519-dalek/src/backend/vector/scalar_mul/vartime_double_base.rs` -> **99.9905%** Exposure
- `curve25519-dalek/src/backend/serial/u64/field.rs` -> **99.9887%** Exposure
- `curve25519-dalek/src/backend/serial/u32/scalar.rs` -> **99.9812%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `x25519-dalek/tests/x25519_tests.rs` -> **18** Orphaned Functions | **0** Duplicates
- `x25519-dalek/src/x25519.rs` -> **0** Orphaned Functions | **13** Duplicates
- `curve25519-dalek-derive/tests/tests.rs` -> **9** Orphaned Functions | **0** Duplicates
- `ed25519-dalek/tests/pkcs8.rs` -> **6** Orphaned Functions | **0** Duplicates
- `curve25519-dalek/src/backend/vector/avx2/field.rs` -> **0** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `ed25519-dalek/src/lib.rs` -> **99.7549%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `883` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `curve25519-dalek/src/edwards.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.04)
- **Top Global Matches:** file_cluster_0: 7.04, file_cluster_5: 8.699, file_cluster_13: 9.112
- **Magnitude:** 567.38 | **LOC:** 2601 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **32** in-repo importer(s); it depends on **72**; blast radius 59.57; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.7%), Connectivity (formerly Api Exposure) (61.9%), Guard Balance (formerly Safety Score) (47.5%), Mutation Surface (formerly State Flux) (32.1%)
- **Documentation Coverage:** 53.211% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize` **(Generic / Templated Code)** (Impact: 11.5)
  * `visit_seq` **(Generic / Templated Code)** (Impact: 11.1)
  * `deserialize` **(Generic / Templated Code)** (Impact: 10.0)
  * `visit_seq` **(Generic / Templated Code)** (Impact: 9.3)
  * `try_from_rng` **(Defensive Guards)** (Impact: 9.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 455`, `args: 176`, `func_start: 153`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 41`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 82`, `import: 48`
* *Defense:* `safety: 5`, `doc: 375`, `test: 116`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 59.57
  * `Choke Point (Betweenness):` 0.039857 | `Ripple Effect (Closeness):` 0.401687
  * `Imports (Out-Degree: 8):` affine, affine::AffinePoint, alloc::vec::Vec, bincode, cfg_if::cfg_if, constants::ED25519_SQRTAM2, core::array::TryFromSliceError, core::borrow::Borrow...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `curve25519-dalek/src/scalar.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.197)
- **Top Global Matches:** file_cluster_0: 7.197, file_cluster_13: 8.496, file_cluster_12: 9.051
- **Magnitude:** 488.04 | **LOC:** 2160 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **42**; blast radius 109.348; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (64.0%), Mutation Surface (formerly State Flux) (53.6%), Guard Balance (formerly Safety Score) (45.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.4%)
- **Documentation Coverage:** 70.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `non_adjacent_form` **(Many-Argument Workhorses)** (Impact: 16.5)
    * *Intent:* /// The quantity \\( k - n_0 \\) is /// $$ /// \begin{aligned} /// k - n_0 &= \sum\_{i=0}^{w-1} k\_i...
  * `as_radix_2w` **(Many-Argument Workhorses)** (Impact: 15.1)
    * *Intent:* /// For radix 16, `Self` must be less than \\(2^{255}\\). This is because most integers larger /// t...
  * `deserialize` **(Generic / Templated Code)** (Impact: 11.6)
  * `visit_seq` **(Generic / Templated Code)** (Impact: 11.1)
  * `test_pippenger_radix_iter` **(Type Conversions)** (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 394`, `args: 114`, `func_start: 104`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 42`, `planned_debt: 1`
* *Architecture:* `api: 74`, `import: 30`
* *Defense:* `safety: 2`, `doc: 524`, `test: 130`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 109.348
  * `Choke Point (Betweenness):` 0.093681 | `Ripple Effect (Closeness):` 0.364835
  * `Imports (Out-Degree: 2):` alloc::vec::Vec, bincode, cfg_if::cfg_if, core::borrow::Borrow, core::fmt::Debug, core::iter, core::iter::Product, core::iter::Sum...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `curve25519-dalek/src/ristretto.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.938)
- **Top Global Matches:** file_cluster_0: 6.938, file_cluster_5: 8.562, file_cluster_12: 9.507
- **Magnitude:** 368.66 | **LOC:** 1741 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **51**; blast radius 21.213; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (58.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.3%), Guard Balance (formerly Safety Score) (47.9%)
- **Documentation Coverage:** 76.259% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize` **(Generic / Templated Code)** (Impact: 11.5)
  * `visit_seq` **(Generic / Templated Code)** (Impact: 11.1)
  * `deserialize` **(Generic / Templated Code)** (Impact: 10.0)
  * `visit_seq` **(Generic / Templated Code)** (Impact: 9.3)
  * `double_and_compress_batch` **(Generic / Templated Code)** (Impact: 8.1)
    * *Intent:* /// Double-and-compress a batch of points. The Ristretto encoding /// is not batchable, since it req...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 377`, `args: 118`, `func_start: 89`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 16`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 59`, `import: 38`
* *Defense:* `safety: 3`, `doc: 330`, `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.213
  * `Choke Point (Betweenness):` 0.006284 | `Ripple Effect (Closeness):` 0.245475
  * `Imports (Out-Degree: 6):` elligator, alloc::vec::Vec, bincode, core::array::TryFromSliceError, core::borrow::Borrow, core::convert::Infallible, core::fmt::Debug, core::iter::Sum...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `curve25519-dalek/src/backend/vector/ifma/field.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.411)
- **Top Global Matches:** file_cluster_13: 6.411, file_cluster_15: 7.414, file_cluster_0: 7.924
- **Magnitude:** 296.38 | **LOC:** 847 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 6.761; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Connectivity (formerly Api Exposure) (68.4%), Guard Balance (formerly Safety Score) (58.7%), Complexity Load (formerly Cognitive Load) (42.9%)
- **Documentation Coverage:** 96.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mul` **(Many-Argument Workhorses)** (Impact: 8.7)
  * `square` **(Compute Cores)** (Impact: 7.1)
  * `iterated_mul_matches_serial` **(Annotated & Test Methods)** (Impact: 5.2)
  * `iterated_u32_mul_matches_serial` **(Annotated & Test Methods)** (Impact: 5.2)
  * `blend_lanes` **(Many-Argument Workhorses)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 244`, `args: 32`, `func_start: 32`, `class_start: 4`
* *Risk/State:* `state_mutation: 136`
* *Architecture:* `api: 31`, `import: 11`
* *Defense:* `doc: 4`, `test: 29`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.761
  * `Choke Point (Betweenness):` 0.000524 | `Ripple Effect (Closeness):` 0.128992
  * `Imports (Out-Degree: 3):` core::arch::x86_64::_mm256_blend_epi32, core::arch::x86_64::_mm256_madd52hi_epu64, core::arch::x86_64::_mm256_madd52lo_epu64, core::arch::x86_64::_mm256_permute4x64_epi64, core::ops::Add, core::ops::Mul, core::ops::Neg, crate::backend::serial::u64::field::FieldElement51...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `curve25519-dalek/src/backend/serial/u32/scalar.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.043)
- **Top Global Matches:** file_cluster_13: 7.043, file_cluster_15: 7.542, file_cluster_0: 8.471
- **Magnitude:** 245.46 | **LOC:** 559 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 7.627; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (70.1%), Guard Balance (formerly Safety Score) (60.4%), Complexity Load (formerly Cognitive Load) (20.8%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_bytes_wide` **(Compute Cores)** (Impact: 6.1)
    * *Intent:* /// Reduce a 64 byte / 512 bit scalar mod l.
  * `from_bytes` **(Compute Cores)** (Impact: 5.5)
    * *Intent:* /// Unpack a 32 byte / 256 bit scalar into 9 29-bit limbs.
  * `add` **(Compute Cores)** (Impact: 4.2)
    * *Intent:* /// Compute `a + b` (mod l).
  * `sub` **(Type Conversions)** (Impact: 4.2)
    * *Intent:* /// Compute `a - b` (mod l).
  * `conditional_add_l` **(Stateful Encapsulated Methods)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 95`, `args: 32`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 103`, `fragile_debt: 1`
* *Architecture:* `api: 34`, `import: 6`
* *Defense:* `doc: 47`, `test: 19`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.627
  * `Choke Point (Betweenness):` 0.00435 | `Ripple Effect (Closeness):` 0.17596
  * `Imports (Out-Degree: 1):` core::fmt::Debug, core::ops::Index, core::ops::IndexMut, crate::constants, self::*, subtle::Choice, subtle::ConditionallySelectable, zeroize::Zeroize
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `curve25519-dalek/src/backend/serial/u32/field.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.874)
- **Top Global Matches:** file_cluster_0: 6.874, file_cluster_15: 8.595, file_cluster_13: 8.843
- **Magnitude:** 233.38 | **LOC:** 608 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 11.952; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.8%), Connectivity (formerly Api Exposure) (62.3%)
- **Documentation Coverage:** 57.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_bytes` **(Type Conversions)** (Impact: 9.7)
    * *Intent:* /// Serialize this `FieldElement51` to a 32-byte array. The /// encoding is canonical.
  * `reduce` **(Type Conversions)** (Impact: 7.0)
    * *Intent:* /// Given unreduced coefficients `z[0], ..., z[9]` of any size, /// carry and reduce them mod p to o...
  * `mul` **(Many-Argument Workhorses)** (Impact: 6.8)
  * `carry` **(Annotated & Test Methods)** (Impact: 5.8)
    * *Intent:* /// Carry the value from limb i = 0..8 to limb i+1
  * `pow2k` **(Parameter Forwarders)** (Impact: 3.9)
    * *Intent:* /// Given `k > 0`, return `self^(2^k)`.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 131`, `args: 27`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 91`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 21`, `import: 8`
* *Defense:* `doc: 59`, `test: 5`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.952
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.248772
  * `Imports (Out-Degree: 0):` core::fmt::Debug, core::ops::Add, core::ops::AddAssign, core::ops::Mul, core::ops::MulAssign, core::ops::Neg, core::ops::Sub, core::ops::SubAssign...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `curve25519-dalek/src/backend/serial/u64/scalar.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.003)
- **Top Global Matches:** file_cluster_13: 7.003, file_cluster_15: 7.728, file_cluster_0: 8.401
- **Magnitude:** 209.96 | **LOC:** 519 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 7.627; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Connectivity (formerly Api Exposure) (71.0%), Guard Balance (formerly Safety Score) (57.3%), Complexity Load (formerly Cognitive Load) (15.2%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_bytes_wide` **(Compute Cores)** (Impact: 5.7)
    * *Intent:* /// Reduce a 64 byte / 512 bit scalar mod l
  * `from_bytes` **(Type Conversions)** (Impact: 5.3)
    * *Intent:* /// Unpack a 32 byte / 256 bit scalar into 5 52-bit limbs.
  * `add` **(Compute Cores)** (Impact: 4.2)
    * *Intent:* /// Compute `a + b` (mod l)
  * `sub` **(Type Conversions)** (Impact: 4.2)
    * *Intent:* /// Compute `a - b` (mod l)
  * `conditional_add_l` **(Stateful Encapsulated Methods)** (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 85`, `args: 32`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 69`, `fragile_debt: 1`
* *Architecture:* `api: 34`, `import: 6`
* *Defense:* `doc: 46`, `test: 19`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.627
  * `Choke Point (Betweenness):` 0.00435 | `Ripple Effect (Closeness):` 0.17596
  * `Imports (Out-Degree: 1):` core::fmt::Debug, core::ops::Index, core::ops::IndexMut, crate::constants, self::*, subtle::Choice, subtle::ConditionallySelectable, zeroize::Zeroize
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ed25519-dalek/src/verifying.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.755)
- **Top Global Matches:** file_cluster_0: 5.755, file_cluster_13: 9.681, file_cluster_16: 9.772
- **Magnitude:** 201.08 | **LOC:** 752 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **28**; blast radius 7.637; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (45.4%), Guard Balance (formerly Safety Score) (43.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.9%)
- **Documentation Coverage:** 51.5152% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `verify_prehashed_strict` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* /// set, this will default to an empty string. /// * `signature` is a purported Ed25519ph signature ...
  * `verify_strict` **(Many-Argument Workhorses)** (Impact: 17.2)
    * *Intent:* /// /// # "Strict" Verification /// /// This method performs *both* of the above signature malleabil...
  * `deserialize` **(Generic / Templated Code)** (Impact: 12.3)
  * `visit_seq` **(Generic / Templated Code)** (Impact: 11.7)
  * `raw_verify_prehashed` **(Stateful Encapsulated Methods)** (Impact: 10.4)
    * *Intent:* /// The prehashed non-batched Ed25519 verification check, rejecting non-canonical R values. /// (see...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 103`, `args: 49`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 30`, `import: 12`
* *Defense:* `safety: 7`, `doc: 221`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.637
  * `Choke Point (Betweenness):` 0.010168 | `Ripple Effect (Closeness):` 0.087379
  * `Imports (Out-Degree: 11):` stream, core::fmt::Debug, core::hash::Hash, core::hash::Hasher, crate::constants::PUBLIC_KEY_LENGTH, crate::context::Context, crate::errors::InternalError, crate::errors::SignatureError...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `curve25519-dalek-derive/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.585)
- **Top Global Matches:** file_cluster_4: 6.585, file_cluster_15: 11.119, file_cluster_6: 11.205
- **Magnitude:** 197.36 | **LOC:** 464 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **3**; blast radius 16.965; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.6%), Complexity Load (formerly Cognitive Load) (19.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_function` **(Many-Argument Workhorses)** (Impact: 48.9)
  * `process_mod` **(Many-Argument Workhorses)** (Impact: 31.9)
  * `parse` **(Compute Cores)** (Impact: 9.2)
  * `process_item` **(State Mutators)** (Impact: 8.7)
  * `unsafe_target_feature_specialize` **(Many-Argument Workhorses)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 112`, `args: 23`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `state_mutation: 27`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 5`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.965
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.147191
  * `Imports (Out-Degree: 0):` proc_macro2::TokenStream, proc_macro::TokenStream, syn::spanned::Spanned
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `curve25519-dalek/src/backend/serial/u64/constants.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.377)
- **Top Global Matches:** file_cluster_2: 3.377, file_cluster_17: 5.435, file_cluster_13: 6.671
- **Magnitude:** 190.18 | **LOC:** 7782 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 11.393; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (27.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `api: 21`, `import: 4`
* *Defense:* `doc: 39`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.393
  * `Choke Point (Betweenness):` 0.007637 | `Ripple Effect (Closeness):` 0.236708
  * `Imports (Out-Degree: 5):` crate::backend::serial::curve_models::AffineNielsPoint, crate::edwards::EdwardsBasepointTable, crate::edwards::EdwardsPoint, crate::window::LookupTable, crate::window::NafLookupTable8, super::field::FieldElement51, super::scalar::Scalar52
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `curve25519-dalek/src/backend/serial/u64/field.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.188)
- **Top Global Matches:** file_cluster_0: 7.188, file_cluster_15: 8.706, file_cluster_13: 9.448
- **Magnitude:** 188.8 | **LOC:** 576 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **11**; blast radius 15.258; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (62.9%), Guard Balance (formerly Safety Score) (60.0%)
- **Documentation Coverage:** 56.4103% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pow2k` **(Type Conversions)** (Impact: 12.3)
    * *Intent:* /// Given `k > 0`, return `self^(2^k)`.
  * `mul` **(Type Conversions)** (Impact: 6.7)
  * `to_bytes` **(Type Conversions)** (Impact: 5.6)
    * *Intent:* /// Serialize this `FieldElement51` to a 32-byte array. The /// encoding is canonical.
  * `add_assign` **(Generic / Templated Code)** (Impact: 3.7)
  * `reduce` **(Compute Cores)** (Impact: 3.2)
    * *Intent:* /// Given 64-bit input limbs, reduce to enforce the bound 2^(51 + epsilon).
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 99`, `args: 26`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 82`, `duplicate_logic: 2`
* *Architecture:* `api: 21`, `import: 8`
* *Defense:* `doc: 42`, `test: 17`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.258
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.275839
  * `Imports (Out-Degree: 0):` core::fmt::Debug, core::ops::Add, core::ops::AddAssign, core::ops::Mul, core::ops::MulAssign, core::ops::Neg, core::ops::Sub, core::ops::SubAssign...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `ed25519-dalek/src/signing.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.035)
- **Top Global Matches:** file_cluster_0: 6.035, file_cluster_13: 9.538, file_cluster_15: 10.245
- **Magnitude:** 186.1 | **LOC:** 978 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **34**; blast radius 6.096; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (50.0%), Guard Balance (formerly Safety Score) (43.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.4%)
- **Documentation Coverage:** 46.3768% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize` **(Generic / Templated Code)** (Impact: 12.2)
  * `visit_seq` **(Generic / Templated Code)** (Impact: 11.7)
  * `raw_sign_prehashed` **(Many-Argument Workhorses)** (Impact: 7.6)
    * *Intent:* /// The prehashed signing function for Ed25519 (i.e., Ed25519ph). `CtxDigest` is the digest /// func...
  * `raw_sign_byupdate` **(Stateful Encapsulated Methods)** (Impact: 7.5)
    * *Intent:* /// Sign a message provided in parts. The `msg_update` closure will be called twice to hash the /// ...
  * `try_from` **(Defensive Guards)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 121`, `args: 52`, `func_start: 44`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `planned_debt: 1`
* *Architecture:* `api: 32`, `import: 14`
* *Defense:* `safety: 3`, `doc: 372`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.096
  * `Choke Point (Betweenness):` 0.006899 | `Ripple Effect (Closeness):` 0.073582
  * `Imports (Out-Degree: 11):` core::fmt::Debug, crate::Signature, crate::constants::KEYPAIR_LENGTH, crate::constants::SECRET_KEY_LENGTH, crate::context::Context, crate::errors::InternalError, crate::errors::SignatureError, crate::hazmat::ExpandedSecretKey...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `curve25519-dalek/src/backend/vector/avx2/field.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.835)
- **Top Global Matches:** file_cluster_13: 6.835, file_cluster_15: 7.213, file_cluster_11: 8.763
- **Magnitude:** 173.38 | **LOC:** 989 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **21**; blast radius 6.726; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (63.4%), Guard Balance (formerly Safety Score) (48.2%), Mutation Surface (formerly State Flux) (46.6%)
- **Documentation Coverage:** 36.7347% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reduce64` **(Compute Cores)** (Impact: 7.6)
    * *Intent:* /// Given an array of wide coefficients, reduce them to a `FieldElement2625x4`. /// /// # Postcondit...
  * `blend` **(Many-Argument Workhorses)** (Impact: 7.0)
    * *Intent:* /// Blend `self` with `other`, taking lanes specified in `control` from `other`. /// /// The `contro...
  * `blend_lanes` **(Type Conversions)** (Impact: 6.6)
  * `reduce` **(I/O & Config Routines)** (Impact: 6.5)
    * *Intent:* /// Reduce this vector of field elements \\(\mathrm{mod} p\\). /// /// # Postconditions /// /// The ...
  * `mul` **(Compute Cores)** (Impact: 6.4)
    * *Intent:* /// Multiply `self` by `rhs`. /// /// # Preconditions /// /// The coefficients of `self` must be bou...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 227`, `args: 34`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `state_mutation: 29`, `dead_code: 5`, `duplicate_logic: 4`
* *Architecture:* `api: 24`, `import: 20`
* *Defense:* `doc: 136`, `test: 31`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.726
  * `Choke Point (Betweenness):` 0.000397 | `Ripple Effect (Closeness):` 0.131679
  * `Imports (Out-Degree: 4):` core::arch::x86_64::_mm256_blend_epi32, core::arch::x86_64::_mm256_mul_epu32, core::arch::x86_64::_mm256_permutevar8x32_epi32, core::arch::x86_64::_mm256_shuffle_epi32, core::arch::x86_64::_mm256_srlv_epi32, core::arch::x86_64::_mm256_unpackhi_epi32, core::arch::x86_64::_mm256_unpacklo_epi32, core::ops::Add...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ed25519-dalek/tests/ed25519.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.13)
- **Top Global Matches:** file_cluster_7: 7.13, file_cluster_5: 7.541, file_cluster_12: 8.895
- **Magnitude:** 136.54 | **LOC:** 731 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 2.602; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (77.6%), Connectivity (formerly Api Exposure) (55.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.4%), Concurrency Surface (formerly Concurrency) (18.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `against_reference_implementation` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* // TESTVECTORS is taken from sign.input.gz in agl's ed25519 Golang // package. It is a selection of ...
  * `compute_challenge` **(Many-Argument Workhorses)** (Impact: 5.4)
    * *Intent:* // Computes the prehashed or non-prehashed challenge, depending on whether context is given
  * `repudiation_prehash` **(Annotated & Test Methods)** (Impact: 5.3)
    * *Intent:* // Identical to repudiation() above, but testing verify_prehashed against // verify_prehashed_strict...
  * `repudiation` **(Annotated & Test Methods)** (Impact: 5.0)
    * *Intent:* // Tests that verify_strict() rejects small-order pubkeys. We test this by explicitly // constructin...
  * `ed25519ph_sign_verify` **(Annotated & Test Methods)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 187`, `args: 31`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 53`, `high_risk_execution: 1`, `state_mutation: 12`
* *Architecture:* `io: 1`, `api: 24`, `concurrency: 4`, `import: 12`
* *Defense:* `safety: 1`, `doc: 2`, `test: 86`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.602
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` curve25519_dalek::constants::ED25519_BASEPOINT_POINT, curve25519_dalek::edwards::CompressedEdwardsY, curve25519_dalek::edwards::EdwardsPoint, curve25519_dalek::scalar::Scalar, curve25519_dalek::traits::IsIdentity, ed25519_dalek::*, getrandom::SysRng, getrandom::rand_core::UnwrapErr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `curve25519-dalek/src/field.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.138)
- **Top Global Matches:** file_cluster_12: 7.138, file_cluster_5: 7.68, file_cluster_13: 8.438
- **Magnitude:** 135.68 | **LOC:** 940 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **18**; blast radius 21.848; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.7%), Connectivity (formerly Api Exposure) (46.5%), Mutation Surface (formerly State Flux) (13.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.1%)
- **Documentation Coverage:** 57.4074% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expand_msg_xmd` **(Many-Argument Workhorses)** (Impact: 8.4)
    * *Intent:* /// Hashes the concatenation of the elements of `msg` with domain separator equal to the /// concate...
  * `hash_to_field` **(Generic / Templated Code)** (Impact: 7.4)
  * `internal_invert_batch` **(Compute Cores)** (Impact: 6.9)
    * *Intent:* /// Given a slice of pub(crate)lic `FieldElements`, replace each with its inverse. `scratch` can ///...
  * `from_bytes_wide` **(Annotated & Test Methods)** (Impact: 4.5)
  * `sqrt_ratio_i` **(Stateful Encapsulated Methods)** (Impact: 4.1)
    * *Intent:* /// Given `FieldElements` `u` and `v`, compute either `sqrt(u/v)` /// or `sqrt(i*u/v)` in constant t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 179`, `args: 37`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 10`
* *Architecture:* `api: 27`, `import: 12`
* *Defense:* `doc: 137`, `test: 56`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.848
  * `Choke Point (Betweenness):` 0.04169 | `Ripple Effect (Closeness):` 0.286093
  * `Imports (Out-Degree: 2):` cfg_if::cfg_if, core::iter::once, crate::backend, crate::constants, crate::field::*, digest::Digest, digest::FixedOutput, digest::HashMarker...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `curve25519-dalek/src/montgomery.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.656)
- **Top Global Matches:** file_cluster_12: 7.656, file_cluster_5: 7.867, file_cluster_0: 8.299
- **Magnitude:** 133.86 | **LOC:** 771 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **28**; blast radius 13.812; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (55.7%), Guard Balance (formerly Safety Score) (47.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.4%), Mutation Surface (formerly State Flux) (19.0%)
- **Documentation Coverage:** 52.459% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mul_bits_be` **(Type Conversions)** (Impact: 6.6)
    * *Intent:* /// Given `self` \\( = u\_0(P) \\), and a big-endian bit representation of an integer /// \\(n\\), r...
  * `elligator_encode` **(Compute Cores)** (Impact: 6.1)
  * `to_edwards` **(Compute Cores)** (Impact: 5.0)
    * *Intent:* /// /// # Inputs /// /// * `sign`: a `u8` donating the desired sign of the resulting /// `EdwardsPoi...
  * `differential_add_and_double` **(Many-Argument Workhorses)** (Impact: 4.0)
    * *Intent:* /// Perform the double-and-add step of the Montgomery ladder. /// /// Given projective points /// \\...
  * `montgomery_mul_bits_be_twist` **(Annotated & Test Methods)** (Impact: 3.5)
    * *Intent:* // Tests that MontgomeryPoint::mul_bits_be is consistent on any point, even ones that might be // on...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 199`, `args: 39`, `func_start: 38`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 10`
* *Architecture:* `api: 28`, `import: 18`
* *Defense:* `doc: 103`, `test: 35`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.812
  * `Choke Point (Betweenness):` 0.005886 | `Ripple Effect (Closeness):` 0.282035
  * `Imports (Out-Degree: 5):` alloc::vec::Vec, bincode, core::hash::Hash, core::hash::Hasher, core::ops::Mul, core::ops::MulAssign, core::ops::Neg, crate::constants...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `curve25519-dalek/src/backend/serial/u32/constants.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.183)
- **Top Global Matches:** file_cluster_2: 3.183, file_cluster_17: 5.244, file_cluster_13: 6.472
- **Magnitude:** 130.64 | **LOC:** 4811 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 11.393; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (28.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `api: 21`, `import: 4`
* *Defense:* `doc: 45`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.393
  * `Choke Point (Betweenness):` 0.007637 | `Ripple Effect (Closeness):` 0.236708
  * `Imports (Out-Degree: 5):` crate::backend::serial::curve_models::AffineNielsPoint, crate::edwards::EdwardsBasepointTable, crate::edwards::EdwardsPoint, crate::window::LookupTable, crate::window::NafLookupTable8, super::field::FieldElement2625, super::scalar::Scalar29
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `curve25519-dalek/benches/dalek_benchmarks.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.221)
- **Top Global Matches:** file_cluster_0: 6.221, file_cluster_5: 8.164, file_cluster_12: 9.201
- **Magnitude:** 115.3 | **LOC:** 420 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 2.602; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.4%), Complexity Load (formerly Cognitive Load) (7.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vartime_precomputed_helper` **(Compute Cores)** (Impact: 9.2)
  * `scalar_arith` **(Callbacks & Closures)** (Impact: 8.5)
  * `vartime_precomputed_pure_static` **(Generic / Templated Code)** (Impact: 7.0)
  * `vartime_multiscalar_mul` **(Generic / Templated Code)** (Impact: 6.8)
  * `consttime_multiscalar_mul` **(Generic / Templated Code)** (Impact: 6.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 163`, `args: 83`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `api: 5`, `import: 19`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.602
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` criterion::BatchSize, criterion::BenchmarkGroup, criterion::BenchmarkId, criterion::Criterion, criterion::criterion_main, criterion::measurement::Measurement, curve25519_dalek::constants, curve25519_dalek::edwards::EdwardsPoint...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `curve25519-dalek/src/backend/vector/avx2/edwards.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.353)
- **Top Global Matches:** file_cluster_0: 7.353, file_cluster_13: 7.476, file_cluster_15: 7.679
- **Magnitude:** 111.4 | **LOC:** 571 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **20**; blast radius 11.124; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (66.1%), Guard Balance (formerly Safety Score) (50.6%), Connectivity (formerly Api Exposure) (44.2%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `serial_add` **(Compute Cores)** (Impact: 5.0)
  * `double` **(I/O & Config Routines)** (Impact: 4.4)
    * *Intent:* /// Compute the double of this point.
  * `mul_by_pow_2` **(Parameter Forwarders)** (Impact: 3.8)
  * `serial_double` **(Compute Cores)** (Impact: 3.8)
  * `add` **(Compute Cores)** (Impact: 3.3)
    * *Intent:* /// Add an `ExtendedPoint` and a `CachedPoint`.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 128`, `args: 26`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `state_mutation: 20`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 12`, `import: 18`
* *Defense:* `doc: 53`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.124
  * `Choke Point (Betweenness):` 0.015482 | `Ripple Effect (Closeness):` 0.135262
  * `Imports (Out-Degree: 9):` core::ops::Add, core::ops::Neg, core::ops::Sub, crate::backend::serial::u64::field::FieldElement51, crate::backend::vector::avx2::constants::BASEPOINT_ODD_LOOKUP_TABLE, crate::constants, crate::edwards, crate::scalar::Scalar...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `curve25519-dalek/src/lizard/lizard_ristretto.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.74)
- **Top Global Matches:** file_cluster_5: 6.74, file_cluster_12: 7.326, file_cluster_7: 9.201
- **Magnitude:** 109.78 | **LOC:** 405 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 3.109; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.4%), Guard Balance (formerly Safety Score) (60.9%), Connectivity (formerly Api Exposure) (39.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.9%)
- **Documentation Coverage:** 20.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `elligator_inv` **(I/O & Config Routines)** (Impact: 12.2)
    * *Intent:* // Test that // elligator_ristretto_flavor ○ elligator_ristretto_flavor_inverse ○ elligator_ristrett...
  * `map_pos_felem_to_curve_inverse` **(I/O & Config Routines)** (Impact: 9.8)
    * *Intent:* // Tests that map_to_curve_inverse ○ map_to_curve_restricted is the identity and has a non-None // r...
  * `lizard_decode` **(Generic / Templated Code)** (Impact: 8.5)
    * *Intent:* /// Decode 16 bytes of data from a RistrettoPoint, using the Lizard method. Returns `None` if /// th...
  * `to_jacobi_quartic_ristretto` **(Compute Cores)** (Impact: 5.0)
    * *Intent:* /// Find a point on the Jacobi quartic associated to each of the four /// points Ristretto equivalen...
  * `map_to_curve_inverse` **(Annotated & Test Methods)** (Impact: 4.0)
    * *Intent:* // Tests that map_to_curve ○ map_to_curve_inverse is the identity
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 107`, `args: 19`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 3`, `state_mutation: 15`
* *Architecture:* `api: 7`, `import: 14`
* *Defense:* `safety: 1`, `doc: 30`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.109
  * `Choke Point (Betweenness):` 0.001843 | `Ripple Effect (Closeness):` 0.044581
  * `Imports (Out-Degree: 6):` crate::constants, crate::edwards::EdwardsPoint, crate::field::FieldElement, crate::ristretto::CompressedRistretto, crate::ristretto::RistrettoPoint, digest::Digest, digest::HashMarker, digest::array::Array...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `curve25519-dalek/src/window.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.381)
- **Top Global Matches:** file_cluster_0: 5.381, file_cluster_13: 9.864, file_cluster_15: 10.273
- **Magnitude:** 87.42 | **LOC:** 277 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **11**; blast radius 28.473; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.7%), Guard Balance (formerly Safety Score) (53.7%), Debt Markers (formerly Tech Debt) (32.9%), Connectivity (formerly Api Exposure) (32.5%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fmt` **(Generic / Templated Code)** (Impact: 7.4)
  * `fmt` **(Generic / Templated Code)** (Impact: 7.3)
  * `select` **(Type Conversions)** (Impact: 4.6)
    * *Intent:* /// Given \\(-8 \leq x \leq 8\\), return \\(xP\\) in constant time.
  * `from` **(Generic / Templated Code)** (Impact: 3.3)
  * `from` **(Generic / Templated Code)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 57`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `state_mutation: 11`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 11`, `import: 11`
* *Defense:* `doc: 16`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.473
  * `Choke Point (Betweenness):` 0.001735 | `Ripple Effect (Closeness):` 0.303565
  * `Imports (Out-Degree: 3):` cfg_if::cfg_if, core::fmt::Debug, crate::backend::serial::curve_models::AffineNielsPoint, crate::backend::serial::curve_models::ProjectiveNielsPoint, crate::edwards::EdwardsPoint, crate::traits::Identity, subtle::Choice, subtle::ConditionallyNegatable...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `curve25519-dalek/src/backend/vector/ifma/edwards.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.357)
- **Top Global Matches:** file_cluster_0: 6.357, file_cluster_13: 8.801, file_cluster_15: 9.411
- **Magnitude:** 87.06 | **LOC:** 338 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **19**; blast radius 9.09; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.5%), Guard Balance (formerly Safety Score) (53.3%), Connectivity (formerly Api Exposure) (50.1%), Complexity Load (formerly Cognitive Load) (19.0%)
- **Documentation Coverage:** 86.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mul_by_pow_2` **(Parameter Forwarders)** (Impact: 3.8)
  * `double` **(Compute Cores)** (Impact: 3.4)
  * `from` **(Generic / Templated Code)** (Impact: 3.3)
  * `from` **(Generic / Templated Code)** (Impact: 3.3)
  * `from` **(Generic / Templated Code)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 84`, `args: 21`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `state_mutation: 15`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 13`, `import: 15`
* *Defense:* `doc: 2`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.09
  * `Choke Point (Betweenness):` 0.01066 | `Ripple Effect (Closeness):` 0.127868
  * `Imports (Out-Degree: 9):` core::ops::Add, core::ops::Neg, core::ops::Sub, crate::constants, crate::edwards, crate::scalar::Scalar, crate::traits::Identity, crate::window::LookupTable...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `x25519-dalek/src/x25519.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.838)
- **Top Global Matches:** file_cluster_0: 7.838, file_cluster_5: 8.159, file_cluster_13: 9.684
- **Magnitude:** 81.06 | **LOC:** 400 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 8.933; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (55.1%), Guard Balance (formerly Safety Score) (45.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.4%)
- **Documentation Coverage:** 10.6383% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `x25519` **(State Mutators)** (Impact: 3.2)
    * *Intent:* /// The bare, byte-oriented x25519 function, exactly as specified in RFC7748. /// /// This can be us...
  * `diffie_hellman` **(State Mutators)** (Impact: 1.9)
    * *Intent:* /// Perform a Diffie-Hellman key agreement between `self` and /// `their_public` key to produce a [`...
  * `diffie_hellman` **(State Mutators)** (Impact: 1.9)
    * *Intent:* /// Perform a Diffie-Hellman key agreement between `self` and /// `their_public` key to produce a [`...
  * `diffie_hellman` **(State Mutators)** (Impact: 1.9)
    * *Intent:* /// Perform a Diffie-Hellman key agreement between `self` and /// `their_public` key to produce a `S...
  * `random_from_rng` **(Generic / Templated Code)** (Impact: 1.7)
    * *Intent:* /// Generate a new [`EphemeralSecret`] with the supplied RNG.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 56`, `args: 30`, `func_start: 30`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `planned_debt: 1`, `duplicate_logic: 13`
* *Architecture:* `api: 27`, `import: 3`
* *Defense:* `doc: 146`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.933
  * `Choke Point (Betweenness):` 0.009604 | `Ripple Effect (Closeness):` 0.038835
  * `Imports (Out-Degree: 3):` curve25519_dalek::edwards::EdwardsPoint, curve25519_dalek::montgomery::MontgomeryPoint, curve25519_dalek::traits::IsIdentity, rand_core::CryptoRng, zeroize::Zeroize, zeroize::ZeroizeOnDrop
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `curve25519-dalek/src/backend/serial/curve_models.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.097)
- **Top Global Matches:** file_cluster_0: 5.097, file_cluster_13: 8.354, file_cluster_15: 8.619
- **Magnitude:** 79.98 | **LOC:** 568 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **12**; blast radius 31.141; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (57.0%), Debt Markers (formerly Tech Debt) (11.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.2%)
- **Documentation Coverage:** 61.2903% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add` **(Generic / Templated Code)** (Impact: 2.5)
  * `sub` **(Generic / Templated Code)** (Impact: 2.5)
  * `add` **(Generic / Templated Code)** (Impact: 2.5)
  * `sub` **(Generic / Templated Code)** (Impact: 2.5)
  * `conditional_select` **(State Mutators)** (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 90`, `args: 26`, `func_start: 26`, `class_start: 4`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `api: 23`, `import: 10`
* *Defense:* `doc: 152`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.141
  * `Choke Point (Betweenness):` 0.010208 | `Ripple Effect (Closeness):` 0.278091
  * `Imports (Out-Degree: 4):` core::fmt::Debug, core::ops::Add, core::ops::Neg, core::ops::Sub, crate::constants, crate::edwards::EdwardsPoint, crate::field::FieldElement, crate::traits::Identity...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `curve25519-dalek/src/backend/vector/packed_simd.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.926)
- **Top Global Matches:** file_cluster_13: 6.926, file_cluster_0: 7.675, file_cluster_15: 9.249
- **Magnitude:** 75.3 | **LOC:** 351 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **8**; blast radius 9.757; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (60.0%), Guard Balance (formerly Safety Score) (49.6%), Mutation Surface (formerly State Flux) (9.0%), Complexity Load (formerly Cognitive Load) (3.8%)
- **Documentation Coverage:** 59.5238% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new_const` **(Many-Argument Workhorses)** (Impact: 4.1)
    * *Intent:* /// A constified variant of `new`. /// /// Should only be called from `const` contexts. At runtime `...
  * `new` **(Type Conversions)** (Impact: 3.6)
    * *Intent:* /// Constructs a new instance.
  * `eq` **(State Mutators)** (Impact: 3.1)
  * `new` **(Type Conversions)** (Impact: 2.7)
    * *Intent:* /// Constructs a new instance.
  * `new_const` **(State Mutators)** (Impact: 2.6)
    * *Intent:* /// A constified variant of `new`. /// /// Should only be called from `const` contexts. At runtime `...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 27`, `args: 23`, `func_start: 23`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 21`, `import: 2`
* *Defense:* `doc: 26`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.757
  * `Choke Point (Betweenness):` 0.005013 | `Ripple Effect (Closeness):` 0.165848
  * `Imports (Out-Degree: 1):` core::ops::Add, core::ops::AddAssign, core::ops::BitAnd, core::ops::BitAndAssign, core::ops::BitXor, core::ops::BitXorAssign, core::ops::Sub, curve25519_dalek_derive::unsafe_target_feature
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `ed25519-dalek/src/batch.rs` (RUST) | Magnitude: 39.34 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 79, doc: 78, structural_boundaries: 48, import: 16
- `curve25519-dalek/src/backend/vector/avx2/edwards.rs` (RUST) | Magnitude: 111.4 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 296, structural_boundaries: 128, core_var_decl: 94, design_upper_case: 56

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `curve25519-dalek/src/ristretto/elligator.rs` (RUST) | Magnitude: 24.9 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 338, structural_boundaries: 31, doc: 18, core_var_decl: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `ed25519-dalek/tests/validation_criteria.rs` (RUST) | Magnitude: 50.38 | Delta: **0.148** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 145, structural_boundaries: 36, branch: 19, core_var_decl: 19

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `curve25519-dalek/src/scalar.rs` -> **Tony Arcieri** (100.0% isolated ownership) | Magnitude: 488.04
- `ed25519-dalek/src/verifying.rs` -> **Tony Arcieri** (100.0% isolated ownership) | Magnitude: 201.08
- `ed25519-dalek/src/signing.rs` -> **Tony Arcieri** (100.0% isolated ownership) | Magnitude: 186.1
- `ed25519-dalek/tests/ed25519.rs` -> **Tony Arcieri** (100.0% isolated ownership) | Magnitude: 136.54
- `curve25519-dalek/src/field.rs` -> **daxpedda** (100.0% isolated ownership) | Magnitude: 135.68

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `curve25519-dalek/src/scalar.rs` -> **Severity: 5.025** (Bridge: 0.0937 * Flux: 53.6372%)
- `curve25519-dalek/src/edwards.rs` -> **Severity: 1.279** (Bridge: 0.0399 * Flux: 32.1002%)
- `curve25519-dalek/src/backend/vector/avx2/edwards.rs` -> **Severity: 1.024** (Bridge: 0.0155 * Flux: 66.1166%)
- `curve25519-dalek/src/backend/vector/ifma/edwards.rs` -> **Severity: 0.879** (Bridge: 0.0107 * Flux: 82.4697%)
- `curve25519-dalek/src/field.rs` -> **Severity: 0.57** (Bridge: 0.0417 * Flux: 13.6755%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `curve25519-dalek/src/edwards.rs` -> **Severity: 19.095** (Embedded: 0.4017 * Error Risk: 47.5372%)
- `curve25519-dalek/src/scalar.rs` -> **Severity: 16.564** (Embedded: 0.3648 * Error Risk: 45.4007%)
- `curve25519-dalek/src/backend/serial/u64/field.rs` -> **Severity: 16.538** (Embedded: 0.2758 * Error Risk: 59.9561%)
- `curve25519-dalek/src/window.rs` -> **Severity: 16.287** (Embedded: 0.3036 * Error Risk: 53.6509%)
- `curve25519-dalek/src/backend/serial/u32/field.rs` -> **Severity: 15.635** (Embedded: 0.2488 * Error Risk: 62.849%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `curve25519-dalek/src/scalar.rs` -> **Severity: 7745.48** (Blast Radius: 109.348 * Doc Risk: 70.8333%)
- `curve25519-dalek/src/constants.rs` -> **Severity: 6461.87** (Blast Radius: 96.928 * Doc Risk: 66.6667%)
- `curve25519-dalek/src/backend.rs` -> **Severity: 3400.735** (Blast Radius: 58.74 * Doc Risk: 57.8947%)
- `curve25519-dalek/src/edwards.rs` -> **Severity: 3169.779** (Blast Radius: 59.57 * Doc Risk: 53.211%)
- `curve25519-dalek/src/window.rs` -> **Severity: 2214.567** (Blast Radius: 28.473 * Doc Risk: 77.7778%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 71 literal sites + 2 sites through wrappers = 73

- `determine_curve25519_dalek_bits_warning` (function, debug_prints, primitive): 2 call sites in 1 files -- `curve25519-dalek/build.rs`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 3298 call pairs -- scoped 20.2%, unique 0.0%, ambiguous 10.0%, external 69.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 3293 | 20.2% | 0.0% | 10.0% | 69.8% |
| shell | 5 | 20.0% | 0.0% | 0.0% | 80.0% |

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
