# ARCHITECTURAL_BRIEF: quote
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/dtolnay/quote.git` |
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
- **Scope:** 26 analyzed artifact(s), 2412 LOC.
- **Load-bearing artifact:** `src/lib.rs` -- 9 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/runtime.rs` -- pulls in 26 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/runtime.rs` at magnitude 175.62 (structural weight, not risk).
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
| Total Artifacts | 37 |
| Analyzed Artifacts (Scanned) | 26 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11 |
| Total LOC | 2412 |
| Volatility Index | 0.077 |
| % Scanned of codebase = | 70.3% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2348 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6254 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7791 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 20 | 2309 | 76.9% |
| YAML | 2 | 103 | 7.7% |
| PLAINTEXT | 2 | 0 | 7.7% |
| MARKDOWN | 2 | 0 | 7.7% |

## 4.1 SOURCE ENCODINGS
All 26 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 54%, Generic / Templated Code Files 15%, Declarative / Non-Code 8%, Large Core Modules (3) 8%, State Mutators Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 22 | 84.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 15.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11*

**Composition by Extension & Reason:**
- `.stderr`: 7x Excluded (Unsupported Extension: '.stderr')
- `.toml`: 2x Unsupported Format (.toml), 1x Excluded (Unsupported Extension: '.toml')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 21.6 | 4.3 | 4.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 55.7 | 18.0 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 17.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 12.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 66.5 | 11.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 15.8 | 0.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 95.8 | 11.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.7 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 15.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 77.4 | 95.9 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 11 | 4 | 1 | `src/to_tokens.rs` |
| cleanup | 0 | 0 | 0 | - |
| guards | 21 | 9 | 1 | `src/runtime.rs` |
| danger | 8 | 5 | 1 | `src/runtime.rs` |
| concurrency | 2 | 1 | 0 | `tests/test.rs` |
| connectivity | 69 | 10 | 2 | `src/runtime.rs` |
| io | 2 | 2 | 0 | `benches/timer.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `build.rs` |
| time | 1 | 1 | 0 | `benches/timer.rs` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 1 | 1 | 0 | `.github/workflows/ci.yml` |
| tests | 94 | 3 | 0 | `tests/test.rs` |
| docs | 811 | 8 | 47 | `src/lib.rs` |
| debt | 34 | 7 | 3 | `src/to_tokens.rs` |
| mutation | 309 | 18 | 19 | `tests/test.rs` |
| dead_code | 51 | 11 | 1 | `tests/test.rs` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 2 | 1 | 0 | `src/to_tokens.rs` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `benches/timer.rs` (Hits: 1)
- `tests/ui/not-quotable.rs` (Hits: 1)
- `.github/FUNDING.yml` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lib.rs** (`src/lib.rs`) — 9 inbound connections
2. **ext.rs** (`src/ext.rs`) — 4 inbound connections
3. **to_tokens.rs** (`src/to_tokens.rs`) — 4 inbound connections
4. **timer.rs** (`benches/timer.rs`) — 2 inbound connections
5. **ident_fragment.rs** (`src/ident_fragment.rs`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **runtime.rs** (`src/runtime.rs`) — 26 outbound dependencies
2. **to_tokens.rs** (`src/to_tokens.rs`) — 17 outbound dependencies
3. **test.rs** (`tests/test.rs`) — 14 outbound dependencies
4. **lib.rs** (`src/lib.rs`) — 12 outbound dependencies
5. **ci.yml** (`.github/workflows/ci.yml`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `deserialize` **(Generic / Templated Code)** (@ `benches/lib.rs`) -> Impact: **30.0** | LOC: 176
- `visit_map` **(Defensive Guards)** (@ `benches/lib.rs`) -> Impact: **14.8** | LOC: 54
- `append_separated` **(Generic / Templated Code)** (@ `src/ext.rs`) -> Impact: **7.2** | LOC: 24
- `visit_seq` **(Generic / Templated Code)** (@ `benches/lib.rs`) -> Impact: **6.8** | LOC: 33
- `do_append_separated` **(Generic / Templated Code)** (@ `src/ext.rs`) -> Impact: **6.8** | LOC: 15
- `rustc_minor_version` **(Compute Cores)** (@ `build.rs`) -> Impact: **6.5** | LOC: 10
- `respan_token_tree` **(Compute Cores)** (@ `src/runtime.rs`) -> Impact: **5.9** | LOC: 14
  * *Intent:* // Token tree with every span replaced by the given one.
- `fmt` **(Defensive Guards)** (@ `src/ident_fragment.rs`) -> Impact: **5.6** | LOC: 8
- `ident_maybe_raw` **(Defensive Guards)** (@ `src/runtime.rs`) -> Impact: **5.5** | LOC: 7
- `to_tokens` **(Compute Cores)** (@ `src/to_tokens.rs`) -> Impact: **5.4** | LOC: 4

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 7 | 425.5 | 8.67% | 43.66% |
| `tests` | 2 | 99.64 | 1.93% | 0.0% |
| `benches` | 4 | 97.02 | 3.94% | 9.44% |
| `.github/workflows` | 1 | 22.14 | 6.53% | 0.0% |
| `__monolith__` | 4 | 21.76 | 2.16% | 9.44% |
| `.github` | 1 | 10.52 | 0.0% | 0.0% |
| `tests/ui` | 7 | 9.32 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/to_tokens.rs` -> **99.9999%** Exposure
- `src/ident_fragment.rs` -> **99.9998%** Exposure
- `src/runtime.rs` -> **97.4855%** Exposure
- `benches/main.rs` -> **37.7541%** Exposure
- `build.rs` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/to_tokens.rs` -> **95.8452%** Exposure
- `src/runtime.rs` -> **62.3963%** Exposure
- `.github/workflows/ci.yml` -> **39.1928%** Exposure
- `src/ext.rs` -> **33.6357%** Exposure
- `src/lib.rs` -> **11.4141%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test.rs` -> **41** Orphaned Functions | **2** Duplicates
- `src/to_tokens.rs` -> **0** Orphaned Functions | **13** Duplicates
- `src/runtime.rs` -> **0** Orphaned Functions | **10** Duplicates
- `src/ident_fragment.rs` -> **0** Orphaned Functions | **4** Duplicates
- `benches/main.rs` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `113` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/runtime.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.495)
- **Top Global Matches:** file_cluster_0: 6.495, file_cluster_13: 9.727, file_cluster_5: 9.81
- **Magnitude:** 175.62 | **LOC:** 507 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **26**; blast radius 19.895; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (66.5%), Mutation Surface (formerly State Flux) (62.4%)
- **Documentation Coverage:** 50.7937% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `respan_token_tree` **(Compute Cores)** (Impact: 5.9)
    * *Intent:* // Token tree with every span replaced by the given one.
  * `ident_maybe_raw` **(Defensive Guards)** (Impact: 5.5)
  * `parse_spanned` **(Parameter Forwarders)** (Impact: 4.3)
  * `push_group_spanned` **(Parameter Forwarders)** (Impact: 2.8)
  * `push_lifetime_spanned` **(Parameter Forwarders)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 124`, `args: 44`, `func_start: 44`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 25`, `duplicate_logic: 10`
* *Architecture:* `api: 47`, `import: 17`
* *Defense:* `safety: 2`, `doc: 47`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.22
  * `Imports (Out-Degree: 3):` alloc::collections::btree_set, alloc::collections::btree_set::BTreeSet, alloc::format, alloc::vec::Vec, core::fmt, core::iter, core::ops::BitOr, core::ops::Deref...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/to_tokens.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.58)
- **Top Global Matches:** file_cluster_0: 6.58, file_cluster_15: 8.755, file_cluster_11: 10.262
- **Magnitude:** 106.7 | **LOC:** 282 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **17**; blast radius 296.309; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (95.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.5%)
- **Documentation Coverage:** 91.8919% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_tokens` **(Compute Cores)** (Impact: 5.4)
  * `to_tokens` **(Defensive Guards)** (Impact: 3.7)
  * `to_tokens` **(Parameter Forwarders)** (Impact: 1.9)
  * `to_tokens` **(Parameter Forwarders)** (Impact: 1.9)
  * `to_tokens` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 85`, `args: 37`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`, `duplicate_logic: 13`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 1`, `doc: 49`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 296.309
  * `Choke Point (Betweenness):` 0.001667 | `Ripple Effect (Closeness):` 0.3136
  * `Imports (Out-Degree: 1):` alloc::borrow::Cow, alloc::borrow::ToOwned, alloc::boxed::Box, alloc::ffi::CString, alloc::rc::Rc, alloc::string::String, core::ffi::CStr, core::iter...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `tests/test.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.997)
- **Top Global Matches:** file_cluster_0: 6.997, file_cluster_13: 8.287, file_cluster_15: 10.064
- **Magnitude:** 98.1 | **LOC:** 576 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 11.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (41.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.5%), Concurrency Surface (formerly Concurrency) (15.8%), Complexity Load (formerly Cognitive Load) (3.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_advanced` **(Generic / Templated Code)** (Impact: 4.7)
  * `test_type_inference_for_span` **(Annotated & Test Methods)** (Impact: 4.3)
  * `test_quote_impl` **(Annotated & Test Methods)** (Impact: 3.0)
  * `test_quote_spanned_impl` **(Annotated & Test Methods)** (Impact: 3.0)
  * `test_array` **(Annotated & Test Methods)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 191`, `args: 52`, `func_start: 48`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`, `duplicate_logic: 2`, `unreferenced_by_name: 41`
* *Architecture:* `concurrency: 2`, `import: 5`
* *Defense:* `doc: 2`, `test: 92`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` proc_macro, proc_macro2::Delimiter, proc_macro2::Group, proc_macro2::Ident, proc_macro2::Span, proc_macro2::TokenStream, quote::TokenStreamExt, quote::format_ident...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `benches/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.048)
- **Top Global Matches:** file_cluster_0: 6.048, file_cluster_5: 9.371, file_cluster_15: 9.482
- **Magnitude:** 85.92 | **LOC:** 213 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 15.983; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.9%), Connectivity (formerly Api Exposure) (44.1%), Mutation Surface (formerly State Flux) (10.8%)
- **Documentation Coverage:** 88.1% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize` **(Generic / Templated Code)** (Impact: 30.0)
  * `visit_map` **(Defensive Guards)** (Impact: 14.8)
  * `visit_seq` **(Generic / Templated Code)** (Impact: 6.8)
  * `visit_u64` **(Generic / Templated Code)** (Impact: 4.1)
  * `visit_bytes` **(Generic / Templated Code)** (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 51`, `args: 13`, `func_start: 10`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `api: 7`, `import: 4`
* *Defense:* `safety: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.983
  * `Choke Point (Betweenness):` 0.011667 | `Ripple Effect (Closeness):` 0.04
  * `Imports (Out-Degree: 2):` timer, benchmark, proc_macro2::Ident, proc_macro::TokenStream, quote::quote
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ext.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 4.232)
- **Top Global Matches:** file_cluster_0: 4.232, file_cluster_13: 10.02, file_cluster_2: 10.053
- **Magnitude:** 49.76 | **LOC:** 139 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 288.467; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.0%), Mutation Surface (formerly State Flux) (33.6%), Connectivity (formerly Api Exposure) (25.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.6%)
- **Documentation Coverage:** 63.6364% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `append_separated` **(Generic / Templated Code)** (Impact: 7.2)
  * `do_append_separated` **(Generic / Templated Code)** (Impact: 6.8)
  * `append_terminated` **(Generic / Templated Code)** (Impact: 5.0)
  * `do_append_terminated` **(Generic / Templated Code)** (Impact: 4.5)
  * `append_all` **(Generic / Templated Code)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 33`, `args: 11`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 288.467
  * `Choke Point (Betweenness):` 0.000833 | `Ripple Effect (Closeness):` 0.3136
  * `Imports (Out-Degree: 1):` core::iter, proc_macro2::TokenStream, proc_macro2::TokenTree, super::ToTokens
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.915)
- **Top Global Matches:** file_cluster_2: 3.915, file_cluster_17: 4.272, file_cluster_13: 4.402
- **Magnitude:** 39.68 | **LOC:** 1478 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **12**; blast radius 91.895; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (86.7%), Guard Balance (formerly Safety Score) (42.5%), Connectivity (formerly Api Exposure) (28.0%), Mutation Surface (formerly State Flux) (11.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 152`, `args: 4`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 1`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 1`, `doc: 552`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 91.895
  * `Choke Point (Betweenness):` 0.0975 | `Ripple Effect (Closeness):` 0.363636
  * `Imports (Out-Degree: 6):` ext, format, ident_fragment, runtime.rs, spanned, to_tokens, alloc, crate::ext::TokenStreamExt...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/ident_fragment.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.19)
- **Top Global Matches:** file_cluster_0: 6.19, file_cluster_15: 9.64, file_cluster_11: 10.703
- **Magnitude:** 25.26 | **LOC:** 90 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 34.211; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (17.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.9%), Complexity Load (formerly Cognitive Load) (6.6%)
- **Documentation Coverage:** 81.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fmt` **(Defensive Guards)** (Impact: 5.6)
  * `fmt` **(Parameter Forwarders)** (Impact: 1.9)
  * `fmt` **(Parameter Forwarders)** (Impact: 1.9)
  * `fmt` **(Parameter Forwarders)** (Impact: 1.9)
  * `fmt` **(Parameter Forwarders)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 20`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `duplicate_logic: 4`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 1`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.211
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.250435
  * `Imports (Out-Degree: 0):` alloc::borrow::Cow, alloc::borrow::ToOwned, alloc::string::String, alloc::string::ToString, core::fmt, proc_macro2::Ident, proc_macro2::Span
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `.github/workflows/ci.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.617)
- **Top Global Matches:** file_cluster_11: 6.617, file_cluster_12: 6.648, file_cluster_2: 7.097
- **Magnitude:** 22.14 | **LOC:** 113 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 11.216; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (51.4%), Mutation Surface (formerly State Flux) (39.2%), Complexity Load (formerly Cognitive Load) (6.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Enable type layout randomization` **(I/O & Config Routines)** (Impact: 2.1)
  * `run` **(I/O & Config Routines)** (Impact: 2.1)
  * `run` **(State Mutators)** (Impact: 1.1)
  * `run` **(State Mutators)** (Impact: 1.1)
  * `run` **(State Mutators)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 21`, `args: 6`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 16`
* *Defense:* `safety: 1`, `doc: 8`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checkout@v6, upload-artifact@v6, pre_ci.yml@master, install@cargo-docs-rs, install@cargo-outdated, rust-toolchain@master, rust-toolchain@miri, rust-toolchain@nightly...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/format.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.854)
- **Top Global Matches:** file_cluster_2: 3.854, file_cluster_17: 4.841, file_cluster_13: 5.578
- **Magnitude:** 16.0 | **LOC:** 169 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 19.895; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (29.2%), Complexity Load (formerly Cognitive Load) (5.8%), Test Surface (formerly Verification) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (2.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 110`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.22
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/spanned.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.185)
- **Top Global Matches:** file_cluster_0: 6.185, file_cluster_13: 9.237, file_cluster_15: 9.27
- **Magnitude:** 12.48 | **LOC:** 50 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 19.895; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (31.8%), Complexity Load (formerly Cognitive Load) (9.8%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `join_spans` **(Defensive Guards)** (Impact: 3.4)
  * `__span` **(State Mutators)** (Impact: 1.6)
  * `__span` **(State Mutators)** (Impact: 1.6)
  * `__span` **(State Mutators)** (Impact: 1.6)
  * `__span` **(State Mutators)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 19`, `args: 8`, `func_start: 5`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.22
  * `Imports (Out-Degree: 1):` crate::ToTokens, proc_macro2::Span, proc_macro2::TokenStream, proc_macro2::extra::DelimSpan
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `build.rs` (RUST | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.404)
- **Top Global Matches:** file_cluster_9: 7.404, file_cluster_15: 8.581, file_cluster_16: 9.27
- **Magnitude:** 11.8 | **LOC:** 33 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 11.216; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.7%), Debt Markers (formerly Tech Debt) (37.8%), Complexity Load (formerly Cognitive Load) (8.6%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rustc_minor_version` **(Compute Cores)** (Impact: 6.5)
  * `main` **(I/O & Config Routines)** (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 11`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `unreferenced_by_name: 1`
* *Architecture:* `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::env, std::process::Command, std::str
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/FUNDING.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 10.52 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 5.42 | **LOC:** 271 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `benches/timer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.216)
- **Top Global Matches:** file_cluster_0: 6.216, file_cluster_13: 10.595, file_cluster_15: 10.624
- **Magnitude:** 5.3 | **LOC:** 18 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 22.776; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (21.5%), Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 88.1% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `time` **(Generic / Templated Code)** (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 13`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.776
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.08
  * `Imports (Out-Degree: 0):` std::io::Write, std::time::Instant, termcolor::Color, termcolor::ColorChoice, termcolor::ColorSpec, termcolor::StandardStream, termcolor::WriteColor
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `benches/main.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.433)
- **Top Global Matches:** file_cluster_11: 5.433, file_cluster_13: 6.119, file_cluster_17: 7.134
- **Magnitude:** 4.8 | **LOC:** 33 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 11.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (37.8%), Connectivity (formerly Api Exposure) (3.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 88.1% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `quote` **(Interface Declarations)** (Impact: 1.2)
  * `main` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 3`, `func_start: 2`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` lib, timer, benchmark, benchmark::benchmark, proc_macro2::Ident, proc_macro2::Span
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `LICENSE-APACHE` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 3.54 | **LOC:** 177 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/compiletest.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 4.99)
- **Top Global Matches:** file_cluster_13: 4.99, file_cluster_2: 8.031, file_cluster_11: 8.629
- **Magnitude:** 1.54 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ui` **(Annotated & Test Methods)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ui/does-not-have-iter-interpolated-dup.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 3.431)
- **Top Global Matches:** file_cluster_11: 3.431, file_cluster_2: 6.273, file_cluster_15: 6.675
- **Magnitude:** 1.5 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 11.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Interface Declarations)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` quote::quote
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ui/does-not-have-iter-interpolated.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 3.431)
- **Top Global Matches:** file_cluster_11: 3.431, file_cluster_2: 6.273, file_cluster_15: 6.675
- **Magnitude:** 1.5 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 11.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Interface Declarations)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` quote::quote
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ui/not-quotable.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 4.432)
- **Top Global Matches:** file_cluster_11: 4.432, file_cluster_2: 6.926, file_cluster_15: 7.251
- **Magnitude:** 1.32 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 11.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Interface Declarations)** (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` quote::quote, std::net::Ipv4Addr
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ui/not-repeatable.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 3.488)
- **Top Global Matches:** file_cluster_11: 3.488, file_cluster_2: 6.529, file_cluster_13: 6.799
- **Magnitude:** 1.32 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 11.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Interface Declarations)** (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` quote::quote
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ui/wrong-type-span.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 3.37)
- **Top Global Matches:** file_cluster_11: 3.37, file_cluster_2: 6.235, file_cluster_15: 6.646
- **Magnitude:** 1.32 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 11.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Interface Declarations)** (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` quote::quote_spanned
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ui/does-not-have-iter-separated.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.116)
- **Top Global Matches:** file_cluster_2: 6.116, file_cluster_13: 6.327, file_cluster_11: 6.739
- **Magnitude:** 1.18 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 11.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` quote::quote
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ui/does-not-have-iter.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.116)
- **Top Global Matches:** file_cluster_2: 6.116, file_cluster_13: 6.327, file_cluster_11: 6.739
- **Magnitude:** 1.18 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 11.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` quote::quote
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `LICENSE-MIT` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 24 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `.github/workflows/ci.yml` (YAML) | Magnitude: 22.14 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 21, import: 16, func_start: 11

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/lib.rs` -> **Severity: 1.113** (Bridge: 0.0975 * Flux: 11.4141%)
- `src/to_tokens.rs` -> **Severity: 0.16** (Bridge: 0.0017 * Flux: 95.8452%)
- `benches/lib.rs` -> **Severity: 0.126** (Bridge: 0.0117 * Flux: 10.825%)
- `src/ext.rs` -> **Severity: 0.028** (Bridge: 0.0008 * Flux: 33.6357%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/to_tokens.rs` -> **Severity: 16.787** (Embedded: 0.3136 * Error Risk: 53.529%)
- `src/lib.rs` -> **Severity: 15.455** (Embedded: 0.3636 * Error Risk: 42.5002%)
- `src/ext.rs` -> **Severity: 15.375** (Embedded: 0.3136 * Error Risk: 49.0267%)
- `src/runtime.rs` -> **Severity: 11.814** (Embedded: 0.22 * Error Risk: 53.7021%)
- `benches/lib.rs` -> **Severity: 1.956** (Embedded: 0.04 * Error Risk: 48.894%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/to_tokens.rs` -> **Severity: 27228.397** (Blast Radius: 296.309 * Doc Risk: 91.8919%)
- `src/ext.rs` -> **Severity: 18357.001** (Blast Radius: 288.467 * Doc Risk: 63.6364%)
- `src/ident_fragment.rs` -> **Severity: 2799.082** (Blast Radius: 34.211 * Doc Risk: 81.8182%)
- `benches/timer.rs` -> **Severity: 2006.566** (Blast Radius: 22.776 * Doc Risk: 88.1%)
- `src/spanned.rs` -> **Severity: 1989.5** (Blast Radius: 19.895 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 363 call pairs -- scoped 15.7%, unique 0.0%, ambiguous 1.7%, external 82.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 363 | 15.7% | 0.0% | 1.7% | 82.6% |

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
