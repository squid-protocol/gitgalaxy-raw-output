# ARCHITECTURAL_BRIEF: serde
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/serde-rs/serde.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 226 analyzed artifact(s), 33303 LOC.
- **Load-bearing artifact:** `serde_derive/src/dummy.rs` -- 2 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `serde_core/src/crate_root.rs` -- pulls in 90 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `serde_derive/src/internals/attr.rs` at magnitude 1064.14 (structural weight, not risk).
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
| Total Artifacts | 359 |
| Analyzed Artifacts (Scanned) | 226 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 133 |
| Total LOC | 33303 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 63.0% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4062 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 1.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 208 | 33303 | 92.0% |
| PLAINTEXT | 10 | 0 | 4.4% |
| MARKDOWN | 8 | 0 | 3.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `2.032`
> **Composition Archetype:** `Mid Flat Project` (z +2.03; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 36%, State Mutators Files 28%, Generic / Templated Code Files 13%, Declarative / Non-Code 8%, Large Core Modules 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 208 | 92.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 18 | 8.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 133*

**Composition by Extension & Reason:**
- `.stderr`: 118x Excluded (Unsupported Extension: '.stderr')
- `.toml`: 7x Unsupported Format (.toml)
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 21.1 | 2.0 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 86.2 | 12.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 12.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 70.5 | 4.9 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 28.2 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 96.1 | 4.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.9 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 85.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1532 | 72 | 9 | `serde/src/private/de.rs` |
| cleanup | 1 | 1 | 0 | `serde/src/private/de.rs` |
| guards | 399 | 42 | 2 | `serde_derive/src/internals/attr.rs` |
| danger | 134 | 32 | 1 | `test_suite/tests/test_de.rs` |
| concurrency | 30 | 6 | 0 | `serde_core/src/crate_root.rs` |
| connectivity | 677 | 87 | 6 | `test_suite/tests/test_gen.rs` |
| io | 7 | 6 | 0 | `serde_core/src/crate_root.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2 | 2 | 0 | `serde/build.rs` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 1258 | 25 | 1 | `test_suite/tests/test_de.rs` |
| docs | 6690 | 51 | 18 | `serde_core/src/ser/mod.rs` |
| debt | 299 | 28 | 2 | `serde/src/private/de.rs` |
| mutation | 1978 | 68 | 22 | `serde_derive/src/ser.rs` |
| dead_code | 1001 | 165 | 4 | `serde_core/src/ser/mod.rs` |
| credential | 0 | 0 | 0 | - |
| threat | 276 | 36 | 2 | `serde_core/src/de/impls.rs` |
| ml_ai | 132 | 23 | 0 | `serde_core/src/de/value.rs` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `serde_core/src/crate_root.rs` (Hits: 2)
- `serde/build.rs` (Hits: 1)
- `serde_core/build.rs` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **dummy.rs** (`serde_derive/src/dummy.rs`) — 2 inbound connections
2. **pretend.rs** (`serde_derive/src/pretend.rs`) — 2 inbound connections
3. **this.rs** (`serde_derive/src/this.rs`) — 2 inbound connections
4. **value.rs** (`serde_core/src/de/value.rs`) — 1 inbound connections
5. **check.rs** (`serde_derive/src/internals/check.rs`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **crate_root.rs** (`serde_core/src/crate_root.rs`) — 90 outbound dependencies
2. **test_de.rs** (`test_suite/tests/test_de.rs`) — 57 outbound dependencies
3. **test_ser.rs** (`test_suite/tests/test_ser.rs`) — 38 outbound dependencies
4. **lib.rs** (`serde/src/lib.rs`) — 36 outbound dependencies
5. **de.rs** (`serde/src/private/de.rs`) — 35 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `from_ast` **(Many-Argument Workhorses)** (@ `serde_derive/src/internals/attr.rs`) -> Impact: **216.1** | LOC: 248
  * *Intent:* /// Extract out the `#[serde(...)]` attributes from a struct field.
- `from_ast` **(Many-Argument Workhorses)** (@ `serde_derive/src/internals/attr.rs`) -> Impact: **180.0** | LOC: 309
  * *Intent:* /// Extract out the `#[serde(...)]` attributes from an item.
- `deserialize_map` **(Many-Argument Workhorses)** (@ `serde_derive/src/de/struct_.rs`) -> Impact: **113.9** | LOC: 221
- `deserialize` **(Many-Argument Workhorses)** (@ `serde_derive/src/de/enum_adjacently.rs`) -> Impact: **110.8** | LOC: 306
  * *Intent:* /// Generates `Deserialize::deserialize` body for an `enum Enum {...}` with `#[serde(tag, content)]` attributes
- `from_ast` **(Many-Argument Workhorses)** (@ `serde_derive/src/internals/attr.rs`) -> Impact: **105.4** | LOC: 168
- `deserialize_identifier` **(Many-Argument Workhorses)** (@ `serde_derive/src/de/identifier.rs`) -> Impact: **88.2** | LOC: 293
- `with_bound` **(Many-Argument Workhorses)** (@ `serde_derive/src/bound.rs`) -> Impact: **83.0** | LOC: 228
  * *Intent:* // Puts the given bound on any generic type parameters that are used in fields // for which filter returns true. // // For example, the following stru...
- `deserialize_map_in_place` **(Many-Argument Workhorses)** (@ `serde_derive/src/de/struct_.rs`) -> Impact: **59.9** | LOC: 158
- `serialize_adjacently_tagged_variant` **(Many-Argument Workhorses)** (@ `serde_derive/src/ser.rs`) -> Impact: **56.4** | LOC: 123
- `deserialize` **(Many-Argument Workhorses)** (@ `serde_derive/src/de/struct_.rs`) -> Impact: **51.5** | LOC: 181
  * *Intent:* /// Generates `Deserialize::deserialize` body for a `struct Struct {...}`

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `serde_derive/src/internals` | 10 | 1703.64 | 9.78% | 29.25% |
| `serde_core/src/de` | 4 | 1524.9 | 5.21% | 90.44% |
| `test_suite/tests` | 21 | 1392.36 | 1.38% | 0.0% |
| `serde/src/private` | 3 | 1348.56 | 4.35% | 46.49% |
| `serde_derive/src` | 9 | 1170.38 | 8.83% | 17.0% |
| `serde_derive/src/de` | 9 | 888.7 | 9.26% | 39.01% |
| `serde_core/src/ser` | 4 | 439.4 | 4.75% | 94.51% |
| `serde_core/src` | 5 | 127.32 | 2.64% | 45.56% |
| `test_suite/tests/regression` | 8 | 106.44 | 0.0% | 0.0% |
| `serde_core/src/private` | 6 | 72.66 | 2.43% | 39.03% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `serde_core/src/ser/impossible.rs` -> **100.0%** Exposure
- `serde_core/src/ser/mod.rs` -> **100.0%** Exposure
- `serde_core/src/de/mod.rs` -> **99.9997%** Exposure
- `serde_derive/src/lib.rs` -> **99.9993%** Exposure
- `serde_core/src/de/ignored_any.rs` -> **99.9991%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `serde_derive/src/internals/ctxt.rs` -> **96.0834%** Exposure
- `serde_derive/src/this.rs` -> **91.6827%** Exposure
- `serde_derive/src/internals/case.rs` -> **84.4693%** Exposure
- `serde_derive/src/bound.rs` -> **63.4749%** Exposure
- `serde_core/src/format.rs` -> **50.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test_suite/tests/test_de.rs` -> **97** Orphaned Functions | **0** Duplicates
- `serde_core/src/de/mod.rs` -> **68** Orphaned Functions | **4** Duplicates
- `test_suite/tests/test_de_error.rs` -> **66** Orphaned Functions | **0** Duplicates
- `test_suite/tests/test_ser.rs` -> **63** Orphaned Functions | **0** Duplicates
- `serde/src/private/de.rs` -> **2** Orphaned Functions | **56** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1102` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `serde_derive/src/internals/attr.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1064.14 | **LOC:** 1819 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (86.4%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (49.7%), Guard Balance (formerly Safety Score) (45.6%)
- **Documentation Coverage:** 90.3448% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_ast` **(Many-Argument Workhorses)** (Impact: 216.1)
    * *Intent:* /// Extract out the `#[serde(...)]` attributes from a struct field.
  * `from_ast` **(Many-Argument Workhorses)** (Impact: 180.0)
    * *Intent:* /// Extract out the `#[serde(...)]` attributes from an item.
  * `from_ast` **(Many-Argument Workhorses)** (Impact: 105.4)
  * `get_ser_and_de` **(Many-Argument Workhorses)** (Impact: 38.0)
  * `parse_lit_into_lifetimes` **(Compute Cores)** (Impact: 20.9)
    * *Intent:* // Parses a string literal like "'a + 'b + 'c" containing a nonempty list of // lifetimes separated ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 328`, `structural_boundaries: 329`, `args: 108`, `func_start: 91`, `class_start: 11`
* *Risk/State:* `state_mutation: 40`, `dead_code: 9`, `duplicate_logic: 25`, `unreferenced_by_name: 3`
* *Architecture:* `api: 66`, `import: 13`
* *Defense:* `safety: 63`, `doc: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ctxt, Ident, Lifetime, Name, Span, Token, TokenStream, TokenTree...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde/src/private/de.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 965.92 | **LOC:** 3502 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (47.6%), Mutation Surface (formerly State Flux) (12.8%)
- **Documentation Coverage:** 93.8567% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize_enum` **(Many-Argument Workhorses)** (Impact: 11.2)
  * `deserialize_enum` **(Many-Argument Workhorses)** (Impact: 11.0)
  * `borrow_cow_str` **(Generic / Templated Code)** (Impact: 10.7)
  * `visit_map` **(Generic / Templated Code)** (Impact: 10.1)
  * `deserialize_unit_struct` **(Generic / Templated Code)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 630`, `args: 262`, `func_start: 258`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 12`, `dead_code: 1`, `fragile_debt: 2`, `duplicate_logic: 56`, `unreferenced_by_name: 2`
* *Architecture:* `api: 44`, `import: 10`
* *Defense:* `safety: 41`, `doc: 72`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BytesDeserializer, Content, ContentDeserializer, ContentRefDeserializer, ContentVisitor, Deserialize, DeserializeSeed, Deserializer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_core/src/de/impls.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 829.2 | **LOC:** 3174 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (62.1%), Guard Balance (formerly Safety Score) (38.9%), Mutation Surface (formerly State Flux) (15.0%)
- **Documentation Coverage:** 99.505% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize` **(Generic / Templated Code)** (Impact: 29.6)
  * `deserialize` **(Generic / Templated Code)** (Impact: 28.0)
  * `deserialize` **(Generic / Templated Code)** (Impact: 17.7)
  * `deserialize` **(Generic / Templated Code)** (Impact: 17.7)
  * `visit_map` **(Generic / Templated Code)** (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 608`, `args: 191`, `func_start: 180`, `class_start: 49`
* *Risk/State:* `state_mutation: 19`, `dead_code: 4`, `fragile_debt: 2`, `duplicate_logic: 18`, `unreferenced_by_name: 5`
* *Architecture:* `api: 12`, `import: 17`
* *Defense:* `safety: 45`, `doc: 802`, `sync_locks: 4`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Deserializer, EnumAccess, Error, InPlaceSeed, MapAccess, SeqAccess, Unexpected, VariantAccess...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_derive/src/ser.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 490.78 | **LOC:** 1370 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 4.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.5%), Mutation Surface (formerly State Flux) (19.8%)
- **Documentation Coverage:** 95.7447% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `serialize_adjacently_tagged_variant` **(Many-Argument Workhorses)** (Impact: 56.4)
  * `serialize_struct_visitor` **(Many-Argument Workhorses)** (Impact: 43.6)
  * `serialize_struct_variant` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `serialize_tuple_struct_visitor` **(Many-Argument Workhorses)** (Impact: 24.8)
  * `serialize_struct_variant_with_flatten` **(Many-Argument Workhorses)** (Impact: 20.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 10 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 266`, `args: 71`, `func_start: 40`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 4`, `state_mutation: 10`, `dead_code: 1`
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 23`, `doc: 15`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Ctxt, Data, Derive, Field, Ident, Index, Match, Member...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_core/src/de/value.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 369.92 | **LOC:** 1896 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 8.065; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (56.7%), Guard Balance (formerly Safety Score) (40.0%)
- **Documentation Coverage:** 83.5366% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `next_element_seed` **(Generic / Templated Code)** (Impact: 9.3)
  * `size_hint` **(Compute Cores)** (Impact: 7.5)
  * `deserialize_tuple` **(Generic / Templated Code)** (Impact: 6.6)
  * `deserialize_seq` **(Generic / Templated Code)** (Impact: 5.9)
  * `fmt` **(Compute Cores)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 414`, `args: 126`, `func_start: 126`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `fragile_debt: 1`, `duplicate_logic: 33`
* *Architecture:* `api: 42`, `import: 7`
* *Defense:* `safety: 8`, `doc: 524`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004444
  * `Imports (Out-Degree: 0):` Deserialize, DeserializeSeed, Deserializer, Expected, IntoDeserializer, MapAccess, Second, SeqAccess...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `serde/src/private/ser.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 355.34 | **LOC:** 1383 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (53.5%), Guard Balance (formerly Safety Score) (49.5%), Debt Markers (formerly Tech Debt) (40.3%)
- **Documentation Coverage:** 97.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `serialize` **(Many-Argument Workhorses)** (Impact: 17.8)
  * `fmt` **(Parameter Forwarders)** (Impact: 4.3)
  * `serialize_tagged_newtype` **(Generic / Templated Code)** (Impact: 3.6)
    * *Intent:* /// Not public API.
  * `serialize_tuple_variant` **(Generic / Templated Code)** (Impact: 3.3)
  * `serialize_struct_variant` **(Generic / Templated Code)** (Impact: 3.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 253`, `args: 131`, `func_start: 130`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`, `duplicate_logic: 10`
* *Architecture:* `api: 29`, `import: 11`
* *Defense:* `safety: 3`, `doc: 69`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ContentSerializer, Impossible, Serialize, SerializeMap, SerializeStruct, SerializeStructVariantAsMapValue, SerializeTupleVariantAsMapValue, Serializer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_derive/src/de.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 317.2 | **LOC:** 977 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 4.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (45.8%), Mutation Surface (formerly State Flux) (22.3%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize_seq` **(Many-Argument Workhorses)** (Impact: 39.5)
  * `deserialize_seq_in_place` **(Many-Argument Workhorses)** (Impact: 26.8)
  * `deserialize_body` **(Defensive Guards)** (Impact: 20.3)
  * `deserialize_in_place_body` **(Compute Cores)** (Impact: 16.1)
  * `deserialize_transparent` **(Defensive Guards)** (Impact: 12.4)
    * *Intent:* /// Generates `Deserialize::deserialize` body for a type with `#[serde(transparent)]` attribute
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 202`, `args: 67`, `func_start: 40`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 11`, `dead_code: 1`, `unreferenced_by_name: 7`
* *Architecture:* `api: 2`, `import: 13`
* *Defense:* `safety: 28`, `doc: 30`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Ctxt, Data, Derive, Field, Fragment, Ident, Index, Member...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test_suite/tests/test_annotations.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 291.54 | **LOC:** 3577 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (48.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (3.9%), Complexity Load (formerly Cognitive Load) (2.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize_string_as_variant` **(Generic / Templated Code)** (Impact: 8.1)
  * `flatten_any_after_flatten_struct` **(Annotated & Test Methods)** (Impact: 8.0)
  * `test_partially_untagged_enum_desugared` **(Annotated & Test Methods)** (Impact: 7.2)
  * `deserialize` **(Generic / Templated Code)** (Impact: 6.9)
  * `deserialize_with` **(Generic / Templated Code)** (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 233`, `args: 88`, `func_start: 88`, `class_start: 95`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 8`, `planned_debt: 6`, `fragile_debt: 1`, `unreferenced_by_name: 52`
* *Architecture:* `api: 2`, `import: 21`
* *Defense:* `safety: 1`, `test: 61`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Deserialize, Deserializer, E::*, Exp::*, HashMap, IgnoredAny, MapAccess, Serialize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_core/src/de/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 285.22 | **LOC:** 2393 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 4.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Dead Code Surface (formerly Dead Code) (41.3%), Mutation Surface (formerly State Flux) (10.8%)
- **Documentation Coverage:** 16.1017% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fmt` **(Generic / Templated Code)** (Impact: 10.3)
  * `fmt` **(Compute Cores)** (Impact: 7.8)
  * `unknown_variant` **(Generic / Templated Code)** (Impact: 5.9)
    * *Intent:* /// Raised when a `Deserialize` enum type received a variant with an /// unrecognized name.
  * `unknown_field` **(Generic / Templated Code)** (Impact: 5.9)
    * *Intent:* /// Raised when a `Deserialize` struct type received a field with an /// unrecognized name.
  * `next_entry_seed` **(Generic / Templated Code)** (Impact: 4.9)
    * *Intent:* /// This returns `Ok(Some((key, value)))` for the next (key-value) pair in /// the map, or `Ok(None)...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 209`, `args: 111`, `func_start: 111`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 4`, `dead_code: 60`, `planned_debt: 12`, `duplicate_logic: 4`, `unreferenced_by_name: 68`
* *Architecture:* `api: 18`, `import: 6`
* *Defense:* `safety: 1`, `doc: 1654`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Deserialize, DeserializeOwned, DeserializeSeed, Deserializer, IntoDeserializer, Result, SeqAccess, Unexpected...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_derive/src/de/struct_.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 284.68 | **LOC:** 698 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (89.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (44.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.5%)
- **Documentation Coverage:** 47.619% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize_map` **(Many-Argument Workhorses)** (Impact: 113.9)
  * `deserialize_map_in_place` **(Many-Argument Workhorses)** (Impact: 59.9)
  * `deserialize` **(Many-Argument Workhorses)** (Impact: 51.5)
    * *Intent:* /// Generates `Deserialize::deserialize` body for a `struct Struct {...}`
  * `deserialize_in_place` **(Many-Argument Workhorses)** (Impact: 14.4)
    * *Intent:* /// Generates `Deserialize::deserialize_in_place` body for a `struct Struct {...}`
  * `deserialize_field_identifier` **(Many-Argument Workhorses)** (Impact: 11.2)
    * *Intent:* /// Generates enum and its `Deserialize` implementation that represents each /// non-skipped field o...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 160`, `args: 41`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `state_mutation: 2`, `dead_code: 3`, `fragile_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 2`, `import: 10`
* *Defense:* `safety: 12`, `doc: 8`, `test: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FieldWithAliases, Fragment, Match, Parameters, Stmts, StructForm, crate::de::
    deserialize_seq, crate::de::deserialize_seq_in_place...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_derive/src/bound.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 227.68 | **LOC:** 426 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (63.5%), Guard Balance (formerly Safety Score) (59.8%), Debt Markers (formerly Tech Debt) (36.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `with_bound` **(Many-Argument Workhorses)** (Impact: 83.0)
    * *Intent:* // Puts the given bound on any generic type parameters that are used in fields // for which filter r...
  * `visit_type` **(Many-Argument Workhorses)** (Impact: 14.3)
    * *Intent:* // Everything below is simply traversing the syntax tree.
  * `with_where_predicates_from_variants` **(Compute Cores)** (Impact: 13.2)
  * `visit_path` **(Defensive Guards)** (Impact: 13.0)
  * `with_where_predicates_from_fields` **(Compute Cores)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 58`, `args: 20`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 11`, `dead_code: 3`, `unreferenced_by_name: 7`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `safety: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Data, Punctuated, crate::internals::ast::Container, crate::internals::attr, proc_macro2::Span, std::collections::HashSet, syn::Token, syn::punctuated::Pair...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test_suite/tests/test_de.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 222.98 | **LOC:** 2388 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **57**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (15.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (2.9%), Connectivity (formerly Api Exposure) (1.8%)
- **Documentation Coverage:** 98.1132% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test` **(Generic / Templated Code)** (Impact: 5.9)
  * `test_atomics` **(Annotated & Test Methods)** (Impact: 4.7)
  * `deserialize` **(Generic / Templated Code)** (Impact: 3.2)
  * `assert_de_tokens_ignore` **(Annotated & Test Methods)** (Impact: 2.6)
  * `test` **(Generic / Templated Code)** (Impact: 2.3)
    * *Intent:* //////////////////////////////////////////////////////////////////////////
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 86`, `args: 118`, `func_start: 106`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 1`, `unreferenced_by_name: 97`
* *Architecture:* `io: 1`, `api: 1`, `import: 20`
* *Defense:* `doc: 72`, `test: 689`, `sync_locks: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AtomicI16, AtomicI32, AtomicI8, AtomicIsize, AtomicU16, AtomicU32, AtomicU64, AtomicU8...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_derive/src/de/identifier.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 222.9 | **LOC:** 478 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (48.9%), Guard Balance (formerly Safety Score) (47.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize_identifier` **(Many-Argument Workhorses)** (Impact: 88.2)
  * `deserialize_custom` **(Many-Argument Workhorses)** (Impact: 31.5)
    * *Intent:* // Generates `Deserialize::deserialize` body for an enum with // `serde(field_identifier)` or `serde...
  * `deserialize_generated` **(Many-Argument Workhorses)** (Impact: 20.1)
  * `visit_borrowed_str` **(Generic / Templated Code)** (Impact: 4.1)
  * `visit_borrowed_bytes` **(Generic / Templated Code)** (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 91`, `args: 31`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`
* *Architecture:* `api: 18`, `import: 7`
* *Defense:* `safety: 6`, `doc: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Parameters, Stmts, ToTokens, TokenStream, Variant, crate::de::FieldWithAliases, crate::fragment::Fragment, crate::internals::ast::Style...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_core/src/ser/impls.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 210.68 | **LOC:** 1046 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (78.0%), Guard Balance (formerly Safety Score) (31.6%), Mutation Surface (formerly State Flux) (21.5%)
- **Documentation Coverage:** 84.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `serialize` **(Generic / Templated Code)** (Impact: 9.7)
  * `format_u8` **(Type Conversions)** (Impact: 9.7)
  * `serialize` **(Generic / Templated Code)** (Impact: 9.7)
  * `serialize` **(Generic / Templated Code)** (Impact: 7.9)
  * `serialize` **(Generic / Templated Code)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 190`, `args: 49`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 9`, `duplicate_logic: 13`, `unreferenced_by_name: 1`
* *Architecture:* `import: 10`
* *Defense:* `safety: 3`, `doc: 676`, `test: 6`, `sync_locks: 5`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Serialize, SerializeTuple, Serializer, crate::lib::*, crate::ser::Error, std::os::unix::ffi::OsStrExt, std::os::windows::ffi::OsStrExt, super::SerializeStruct
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_derive/src/internals/check.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 191.74 | **LOC:** 478 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 8.065; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (46.0%), Mutation Surface (formerly State Flux) (14.4%), Connectivity (formerly Api Exposure) (12.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_internal_tag_field_name_conflict` **(Compute Cores)** (Impact: 30.2)
    * *Intent:* // The tag of an internally-tagged struct variant must not be the same as either // one of its field...
  * `check_transparent` **(Many-Argument Workhorses)** (Impact: 25.9)
    * *Intent:* // Enums and unit structs cannot be transparent.
  * `check_variant_skip_attrs` **(Many-Argument Workhorses)** (Impact: 24.3)
    * *Intent:* // Skip-(de)serializing attributes are not allowed on variants marked // (de)serialize_with.
  * `check_default_on_tuple` **(Defensive Guards)** (Impact: 18.6)
    * *Intent:* // If some field of a tuple struct is marked #[serde(default)] then all fields // after it must also...
  * `check_identifier` **(Many-Argument Workhorses)** (Impact: 14.3)
    * *Intent:* // The `other` attribute must be used at most once and it must be the last // variant of an enum. //...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 54`, `args: 15`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`, `dead_code: 2`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004444
  * `Imports (Out-Degree: 0):` Ctxt, Data, Derive, Field, Identifier, Style, TagType, Type...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test_suite/tests/test_gen.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 159.74 | **LOC:** 961 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.0%), Connectivity (formerly Api Exposure) (12.2%), Complexity Load (formerly Cognitive Load) (1.8%)
- **Documentation Coverage:** 68.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_gen` **(Annotated & Test Methods)** (Impact: 40.4)
    * *Intent:* //////////////////////////////////////////////////////////////////////////
  * `serialize_some_other_variant` **(Generic / Templated Code)** (Impact: 2.3)
  * `vec_first_element` **(Generic / Templated Code)** (Impact: 2.1)
  * `ser_x` **(Generic / Templated Code)** (Impact: 1.9)
  * `serialize_with` **(Generic / Templated Code)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 136`, `args: 18`, `func_start: 18`, `class_start: 105`
* *Risk/State:* `high_risk_execution: 8`, `state_mutation: 6`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 69`, `import: 10`
* *Defense:* `doc: 96`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DeserializeOwned, Deserializer, Serialize, Serializer, ser_x, serde::de::Deserialize, serde::ser::Serialize, serde_derive::Deserialize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_derive/src/de/enum_adjacently.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 158.72 | **LOC:** 325 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 54.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.6%), Guard Balance (formerly Safety Score) (51.1%), Mutation Surface (formerly State Flux) (49.4%)
- **Documentation Coverage:** 34.7826% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize` **(Many-Argument Workhorses)** (Impact: 110.8)
    * *Intent:* /// Generates `Deserialize::deserialize` body for an `enum Enum {...}` with `#[serde(tag, content)]`...
  * `visit_map` **(Many-Argument Workhorses)** (Impact: 13.2)
  * `visit_seq` **(Generic / Templated Code)** (Impact: 6.7)
  * `deserialize` **(Generic / Templated Code)** (Impact: 3.9)
  * `expecting` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 70`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 3`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 6`, `doc: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Match, Parameters, Variant, crate::de::enum_, crate::de::enum_untagged, crate::de::field_i, crate::fragment::Fragment, crate::internals::ast::Style...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_derive/src/internals/receiver.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 137.56 | **LOC:** 294 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.7%), Mutation Surface (formerly State Flux) (36.0%), Complexity Load (formerly Cognitive Load) (12.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_generics_mut` **(Compute Cores)** (Impact: 15.2)
  * `visit_type_mut_impl` **(Compute Cores)** (Impact: 14.4)
    * *Intent:* // Everything below is simply traversing the syntax tree.
  * `self_to_expr_path` **(Defensive Guards)** (Impact: 11.1)
  * `visit_type_mut` **(Defensive Guards)** (Impact: 11.1)
    * *Intent:* // `Self` -> `Receiver`
  * `visit_path_arguments_mut` **(Defensive Guards)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 123`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Data, DeriveInput, Expr, ExprPath, GenericArgument, GenericParam, Generics, Macro...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test_suite/tests/test_de_error.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 135.56 | **LOC:** 1569 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (24.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (2.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_u64` **(Annotated & Test Methods)** (Impact: 2.5)
  * `test_u128` **(Annotated & Test Methods)** (Impact: 2.5)
  * `test_i8` **(I/O & Config Routines)** (Impact: 2.0)
  * `test_i16` **(Annotated & Test Methods)** (Impact: 2.0)
  * `test_i32` **(Annotated & Test Methods)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 67`, `args: 66`, `func_start: 66`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `unreferenced_by_name: 66`
* *Architecture:* `import: 7`
* *Defense:* `test: 281`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BTreeSet, CString, HashMap, HashSet, IntoDeserializer, NonZeroI16, NonZeroI32, NonZeroI64...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_core/src/ser/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 132.78 | **LOC:** 2011 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Dead Code Surface (formerly Dead Code) (99.2%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (11.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `iterator_len_hint` **(Generic / Templated Code)** (Impact: 4.7)
  * `serialize_newtype_variant` **(Generic / Templated Code)** (Impact: 2.9)
    * *Intent:* /// } /// /// impl Serialize for E { /// fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::E...
  * `serialize_tuple_variant` **(Generic / Templated Code)** (Impact: 2.8)
    * *Intent:* /// tv.serialize_field(b)?; /// tv.end() /// } /// E::U(ref a, ref b, ref c) => { /// let mut tv = s...
  * `serialize_struct_variant` **(Generic / Templated Code)** (Impact: 2.8)
    * *Intent:* /// ref r, /// ref g, /// ref b, /// } => { /// let mut sv = serializer.serialize_struct_variant("E"...
  * `serialize_unit_variant` **(Generic / Templated Code)** (Impact: 2.5)
    * *Intent:* /// } /// /// impl Serialize for E { /// fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::E...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 94`, `args: 58`, `func_start: 56`, `class_start: 10`
* *Risk/State:* `state_mutation: 1`, `dead_code: 167`, `planned_debt: 3`, `duplicate_logic: 15`, `unreferenced_by_name: 31`
* *Architecture:* `api: 14`, `import: 5`
* *Defense:* `doc: 1694`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Display, None, Serialize, SerializeMap, SerializeSeq, SerializeStruct, SerializeStructVariant, SerializeTuple...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test_suite/tests/test_ser.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 106.76 | **LOC:** 920 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **38**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (41.8%)
- **Documentation Coverage:** 98.4127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_enum_skipped` **(Annotated & Test Methods)** (Impact: 2.2)
  * `test_system_time` **(Annotated & Test Methods)** (Impact: 1.9)
  * `test_cannot_serialize_paths` **(Annotated & Test Methods)** (Impact: 1.6)
  * `test_result` **(I/O & Config Routines)** (Impact: 1.5)
  * `test_slice` **(Annotated & Test Methods)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 33`, `args: 63`, `func_start: 63`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1`, `unreferenced_by_name: 63`
* *Architecture:* `io: 1`, `import: 17`
* *Defense:* `doc: 48`, `test: 63`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AtomicI16, AtomicI32, AtomicI8, AtomicIsize, AtomicU16, AtomicU32, AtomicU64, AtomicU8...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_derive/src/de/tuple.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 88.08 | **LOC:** 284 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 57.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (85.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (46.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.6%)
- **Documentation Coverage:** 41.1765% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize` **(Many-Argument Workhorses)** (Impact: 32.9)
    * *Intent:* /// Generates `Deserialize::deserialize` body for a `struct Tuple(...);` including `struct Newtype(T...
  * `deserialize_in_place` **(Many-Argument Workhorses)** (Impact: 20.9)
    * *Intent:* /// Generates `Deserialize::deserialize_in_place` body for a `struct Tuple(...);` including `struct ...
  * `deserialize_newtype_struct` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `visit_seq` **(Generic / Templated Code)** (Impact: 2.1)
    * *Intent:* #visit_newtype_struct
  * `visit_newtype_struct` **(Generic / Templated Code)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 72`, `args: 11`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `state_mutation: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 3`, `doc: 4`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Parameters, Stmts, TupleForm, crate::de::deserialize_seq, crate::de::deserialize_seq_in_place, crate::fragment::Fragment, crate::internals::ast::Field, crate::internals::attr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_derive/src/internals/ast.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 80.1 | **LOC:** 226 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 4.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (46.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.1%), Mutation Surface (formerly State Flux) (14.6%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_ast` **(Many-Argument Workhorses)** (Impact: 18.4)
    * *Intent:* /// Convert the raw Syn ast into a parsed container object, collecting errors in `cx`.
  * `enum_from_ast` **(Many-Argument Workhorses)** (Impact: 10.9)
  * `fields_from_ast` **(Many-Argument Workhorses)** (Impact: 8.7)
  * `struct_from_ast` **(Many-Argument Workhorses)** (Impact: 8.5)
  * `all_fields` **(Generic / Templated Code)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 29`, `args: 10`, `func_start: 6`, `class_start: 5`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 22`, `import: 4`
* *Defense:* `safety: 2`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Ctxt, Derive, check, crate::internals::attr, proc_macro2::Ident, syn::Token, syn::punctuated::Punctuated
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_derive/src/internals/case.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 79.72 | **LOC:** 201 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (84.5%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (46.0%), Guard Balance (formerly Safety Score) (44.8%)
- **Documentation Coverage:** 45.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fmt` **(Compute Cores)** (Impact: 14.5)
  * `apply_to_field` **(Compute Cores)** (Impact: 13.5)
    * *Intent:* /// Apply a renaming rule to a struct field, returning the version expected in the source.
  * `apply_to_variant` **(Compute Cores)** (Impact: 9.8)
    * *Intent:* /// Apply a renaming rule to an enum variant, returning the version expected in the source.
  * `from_str` **(Generic / Templated Code)** (Impact: 4.7)
  * `or` **(Defensive Guards)** (Impact: 3.8)
    * *Intent:* /// Returns the `RenameRule` if it is not `None`, `rule_b` otherwise.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 15`, `args: 7`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 1`, `doc: 18`, `test: 19`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Debug, Display, self::RenameRule::*, std::fmt::self
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `serde_core/src/crate_root.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 75.72 | **LOC:** 172 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **90**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.2%), Connectivity (formerly Api Exposure) (15.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.3%), Mutation Surface (formerly State Flux) (10.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 66`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 2`, `api: 57`, `import: 54`
* *Defense:* `doc: 9`, `sync_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AtomicI16, AtomicI32, AtomicI8, AtomicIsize, AtomicU16, AtomicU32, AtomicU64, AtomicU8...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `test_suite/tests/test_annotations.rs` -> **David Tolnay** (100.0% isolated ownership) | Magnitude: 291.54
- `serde_core/src/de/mod.rs` -> **David Tolnay** (100.0% isolated ownership) | Magnitude: 285.22
- `serde_derive/src/bound.rs` -> **dishmaker** (100.0% isolated ownership) | Magnitude: 227.68
- `test_suite/tests/test_de.rs` -> **David Tolnay** (100.0% isolated ownership) | Magnitude: 222.98
- `test_suite/tests/test_de_error.rs` -> **David Tolnay** (100.0% isolated ownership) | Magnitude: 135.56

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `serde_derive/src/pretend.rs` -> **Severity: 0.455** (Embedded: 0.0089 * Error Risk: 51.1362%)
- `serde_derive/src/this.rs` -> **Severity: 0.406** (Embedded: 0.0089 * Error Risk: 45.7248%)
- `serde_derive/src/internals/check.rs` -> **Severity: 0.204** (Embedded: 0.0044 * Error Risk: 45.9548%)
- `serde_core/src/de/value.rs` -> **Severity: 0.178** (Embedded: 0.0044 * Error Risk: 40.0334%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `serde_derive/src/internals/check.rs` -> **Severity: 806.5** (Blast Radius: 8.065 * Doc Risk: 100.0%)
- `serde_derive/src/dummy.rs` -> **Severity: 682.9** (Blast Radius: 6.829 * Doc Risk: 100.0%)
- `serde_derive/src/pretend.rs` -> **Severity: 682.9** (Blast Radius: 6.829 * Doc Risk: 100.0%)
- `serde_derive/src/this.rs` -> **Severity: 682.9** (Blast Radius: 6.829 * Doc Risk: 100.0%)
- `serde_core/src/de/value.rs` -> **Severity: 673.723** (Blast Radius: 8.065 * Doc Risk: 83.5366%)

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
