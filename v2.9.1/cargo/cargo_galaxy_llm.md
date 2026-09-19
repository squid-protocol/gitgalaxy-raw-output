# ARCHITECTURAL_BRIEF: cargo
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/rust-lang/cargo.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1995 analyzed artifact(s), 268527 LOC.
- **Load-bearing artifact:** `src/doc/src/reference/manifest.md` -- 12 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/cargo/core/compiler/mod.rs` -- pulls in 101 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tests/testsuite/package.rs` at magnitude 2476.06 (structural weight, not risk).
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
| Total Artifacts | 2942 |
| Analyzed Artifacts (Scanned) | 1995 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 947 |
| Total LOC | 268527 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 67.8% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5104 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3272 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.4133 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 15 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1217 | 265439 | 61.0% |
| XML | 382 | 3 | 19.1% |
| MARKDOWN | 240 | 0 | 12.0% |
| PLAINTEXT | 127 | 0 | 6.4% |
| JSON | 16 | 1950 | 0.8% |
| SHELL | 6 | 349 | 0.3% |
| PYTHON | 2 | 94 | 0.1% |
| DOCKERFILE | 2 | 44 | 0.1% |
| JAVASCRIPT | 1 | 637 | 0.1% |
| CSS | 1 | 6 | 0.1% |
| HTML | 1 | 5 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Flat Modular Platform`
> **Architectural Drift Z-Score:** `5.061`
> **Composition Archetype:** `Flat Modular Platform` (z +5.06; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 55%, Large Core Modules 18%, Declarative / Non-Code 7%, Large Core Modules (3) 6%, State Mutators Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1627 | 81.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 367 | 18.4% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 947*

**Composition by Extension & Reason:**
- `.toml`: 380x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 285x Unsupported Format (.toml), 7x Excluded (Unsupported Extension: '.toml')
- `.rs`: 128x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1121 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1213 LOC)
- `no_extension`: 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected), 1x Unsupported Format (.undeterminable)
- `.lock`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 12x Excluded (Unsupported Extension: '.lock')
- `.stderr`: 19x Excluded (Unsupported Extension: '.stderr')
- `.stdout`: 14x Excluded (Unsupported Extension: '.stdout')
- `.tgz`: 10x Excluded (Explicitly Denied Extension: '.tgz')
- `.yml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 7x Excluded (Explicitly Denied Extension: '.png')
- `.svg`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 74 LOC)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 12 LOC)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1481 LOC)
- `.json5`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.conf`: 1x Excluded (Unsupported Extension: '.conf')
- `.1`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 92.8 | 3.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 18.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 95.4 | 5.1 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.9 | 1.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 85.9 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 13.6 | 1.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 50.7 | 60.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 65.7 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5397 | 457 | 7 | `crates/cargo-util-schemas/src/manifest/mod.rs` |
| cleanup | 112 | 45 | 0 | `tests/testsuite/global_cache_tracker.rs` |
| guards | 2951 | 352 | 3 | `src/cargo/util/toml/mod.rs` |
| danger | 4798 | 347 | 4 | `tests/testsuite/config.rs` |
| concurrency | 1312 | 152 | 0 | `tests/testsuite/package.rs` |
| connectivity | 6311 | 436 | 7 | `crates/cargo-util-schemas/src/manifest/mod.rs` |
| io | 631 | 178 | 0 | `tests/testsuite/package.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 77 | 48 | 0 | `tests/testsuite/profile_trim_paths.rs` |
| time | 34 | 28 | 0 | `src/etc/cargo.bashcomp.sh` |
| serialization | 106 | 39 | 0 | `credential/cargo-credential/src/lib.rs` |
| regex | 15 | 9 | 0 | `src/etc/cargo.bashcomp.sh` |
| events | 510 | 83 | 0 | `src/cargo/core/global_cache_tracker.rs` |
| tests | 3432 | 263 | 2 | `tests/testsuite/test.rs` |
| docs | 14428 | 428 | 10 | `src/cargo/core/compiler/fingerprint/mod.rs` |
| debt | 1356 | 223 | 1 | `tests/testsuite/build_script.rs` |
| mutation | 57662 | 821 | 48 | `tests/testsuite/package.rs` |
| dead_code | 3920 | 860 | 4 | `tests/testsuite/test.rs` |
| credential | 15 | 7 | 0 | `tests/testsuite/login.rs` |
| threat | 79 | 42 | 0 | `tests/testsuite/test.rs` |
| ml_ai | 72 | 16 | 0 | `src/cargo/core/compiler/timings/report.rs` |
| ui | 13 | 2 | 0 | `src/cargo/core/compiler/timings/timings.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/testsuite/package.rs` (Hits: 55)
- `src/etc/cargo.bashcomp.sh` (Hits: 22)
- `crates/cargo-util/src/paths.rs` (Hits: 20)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **manifest.md** (`src/doc/src/reference/manifest.md`) — 12 inbound connections
2. **config.md** (`src/doc/src/reference/config.md`) — 11 inbound connections
3. **resolver.md** (`src/doc/src/reference/resolver.md`) — 9 inbound connections
4. **process.rs** (`src/cargo/util/credential/process.rs`) — 9 inbound connections
5. **build-scripts.md** (`src/doc/src/reference/build-scripts.md`) — 7 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`src/cargo/core/compiler/mod.rs`) — 101 outbound dependencies
2. **SUMMARY.md** (`src/doc/src/SUMMARY.md`) — 98 outbound dependencies
3. **mod.rs** (`src/cargo/util/context/mod.rs`) — 90 outbound dependencies
4. **mod.rs** (`src/cargo/ops/mod.rs`) — 84 outbound dependencies
5. **mod.rs** (`src/cargo/util/toml/mod.rs`) — 83 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `to_real_manifest` **(Many-Argument Workhorses)** (@ `src/cargo/util/toml/mod.rs`) -> Impact: **330.2** | LOC: 619
- `new` **(Many-Argument Workhorses)** (@ `src/cargo/ops/cargo_install.rs`) -> Impact: **209.0** | LOC: 213
  * *Intent:* // Returns pkg to install. None if pkg is already installed
- `resolve_dependency` **(Many-Argument Workhorses)** (@ `src/cargo/ops/cargo_add/mod.rs`) -> Impact: **207.2** | LOC: 184
- `create_bcx` **(Many-Argument Workhorses)** (@ `src/cargo/ops/cargo_compile/mod.rs`) -> Impact: **195.0** | LOC: 456
  * *Intent:* /// Prepares all required information for the actual compilation. /// /// For how it works and what data it collects, /// please see the [module-level...
- `sync` **(Many-Argument Workhorses)** (@ `src/cargo/ops/vendor.rs`) -> Impact: **179.2** | LOC: 304
- `normalize_package_toml` **(Many-Argument Workhorses)** (@ `src/cargo/util/toml/mod.rs`) -> Impact: **174.7** | LOC: 213
- `parse` **(Many-Argument Workhorses)** (@ `src/cargo/core/compiler/custom_build.rs`) -> Impact: **173.3** | LOC: 346
  * *Intent:* /// Parses the output instructions of a build script. /// /// * `pkg_descr` --- for error messages /// * `library_name` --- for determining if `RUSTC_...
- `clean_specs` **(Many-Argument Workhorses)** (@ `src/cargo/ops/cargo_clean.rs`) -> Impact: **169.0** | LOC: 258
- `from_toml` **(Many-Argument Workhorses)** (@ `src/cargo/util/toml_mut/dependency.rs`) -> Impact: **166.7** | LOC: 159
  * *Intent:* /// Create a dependency from a TOML table entry.
- `build_work` **(Many-Argument Workhorses)** (@ `src/cargo/core/compiler/custom_build.rs`) -> Impact: **152.1** | LOC: 409
  * *Intent:* /// Constructs the unit of work of running a build script. /// /// The construction includes: /// /// * Set environment variables for the build script...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/testsuite` | 151 | 34225.0 | 6.69% | 0.0% |
| `src/cargo/core` | 13 | 5355.9 | 8.69% | 23.84% |
| `src/cargo/ops` | 19 | 4971.94 | 16.07% | 20.91% |
| `src/cargo/core/compiler` | 19 | 4256.64 | 8.65% | 35.34% |
| `src/cargo/util` | 37 | 3552.4 | 8.89% | 42.6% |
| `src/cargo/util/toml` | 3 | 2737.88 | 14.91% | 40.62% |
| `src/cargo/core/resolver` | 10 | 2396.88 | 11.9% | 27.89% |
| `src/cargo/util/context` | 10 | 2309.98 | 8.95% | 23.54% |
| `crates/cargo-test-support/src` | 9 | 2071.06 | 6.84% | 28.59% |
| `src/bin/cargo/commands` | 40 | 1810.92 | 10.34% | 35.26% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/cargo/util/errors.rs` -> **100.0%** Exposure
- `src/cargo/util/once.rs` -> **100.0%** Exposure
- `src/cargo/core/compiler/job_queue/job_state.rs` -> **99.9999%** Exposure
- `crates/build-rs/src/input.rs` -> **99.9998%** Exposure
- `src/cargo/util/context/environment.rs` -> **99.9955%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/cargo/util/dependency_queue.rs` -> **100.0%** Exposure
- `src/cargo/util/edit_distance.rs` -> **100.0%** Exposure
- `src/cargo/util/graph.rs` -> **100.0%** Exposure
- `src/cargo/util/network/http.rs` -> **100.0%** Exposure
- `src/cargo/util/network/http_async.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/testsuite/test.rs` -> **123** Orphaned Functions | **0** Duplicates
- `tests/testsuite/build_script.rs` -> **93** Orphaned Functions | **22** Duplicates
- `tests/testsuite/script/cargo.rs` -> **80** Orphaned Functions | **0** Duplicates
- `tests/testsuite/build.rs` -> **62** Orphaned Functions | **12** Duplicates
- `tests/testsuite/workspaces.rs` -> **70** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/testsuite/ssh.rs` -> **65.6928%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `9340` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tests/testsuite/package.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2476.06 | **LOC:** 8033 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 31.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (86.3%), Connectivity (formerly Api Exposure) (80.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.4%), Complexity Load (formerly Cognitive Load) (25.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `git_dependency_no_version` **(I/O & Config Routines)** (Impact: 92.5)
  * `workspace_noconflict_readme` **(I/O & Config Routines)** (Impact: 92.5)
  * `package_verbose` **(I/O & Config Routines)** (Impact: 7.5)
  * `checksum_changed` **(I/O & Config Routines)** (Impact: 7.5)
    * *Intent:* // This is a companion to `publish::checksum_changed`, but because this one // is packaging without ...
  * `long_file_names` **(I/O & Config Routines)** (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 191 instances
* *State Mutation (weighted view):* 1930
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 357`, `args: 150`, `func_start: 141`
* *Risk/State:* `safety_bypasses: 106`, `high_risk_execution: 1`, `state_mutation: 1548`, `dead_code: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 55`, `api: 58`, `import: 25`
* *Defense:* `safety: 1`, `doc: 26`, `test: 25`, `sync_locks: 104`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File, Package, ProjectBuilder, basic_manifest, cargo::util::HumanBytes, cargo_test_support::
    Project, cargo_test_support::publish::validate_crate_contents, cargo_test_support::registry::self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cargo/util/toml/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1947.02 | **LOC:** 3335 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 48.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **83**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (85.1%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (68.8%), Guard Balance (formerly Safety Score) (58.2%)
- **Documentation Coverage:** 68.8312% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_real_manifest` **(Many-Argument Workhorses)** (Impact: 330.2)
  * `normalize_package_toml` **(Many-Argument Workhorses)** (Impact: 174.7)
  * `prepare_toml_for_publish` **(Many-Argument Workhorses)** (Impact: 129.0)
    * *Intent:* /// Prepares the manifest for publishing. // - Path and git components of dependency specifications ...
  * `normalize_toml` **(Many-Argument Workhorses)** (Impact: 119.5)
    * *Intent:* /// See [`Manifest::normalized_toml`] for more details
  * `dep_to_dependency` **(Many-Argument Workhorses)** (Impact: 95.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 67 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 538`, `structural_boundaries: 562`, `args: 191`, `func_start: 65`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 54`, `high_risk_execution: 6`, `state_mutation: 79`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 14`, `import: 41`
* *Defense:* `safety: 103`, `doc: 35`, `test: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ArtifactTarget, BTreeSet, CRATES_IO_REGISTRY, CompileTarget, DepKind, EitherManifest, Feature, FeatureValue...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/testsuite/build_script.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1505.68 | **LOC:** 6815 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 42.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **30**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (77.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.7%), Concurrency Surface (formerly Concurrency) (12.2%), Complexity Load (formerly Cognitive Load) (11.5%)
- **Documentation Coverage:** 93.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_rename_with_link_search_path` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `code_generation` **(I/O & Config Routines)** (Impact: 27.0)
  * `rerun_if_directory` **(I/O & Config Routines)** (Impact: 15.5)
  * `generate_good_d_files` **(I/O & Config Routines)** (Impact: 9.5)
  * `custom_build_env_vars` **(I/O & Config Routines)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 936
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 338`, `args: 338`, `func_start: 250`
* *Risk/State:* `safety_bypasses: 104`, `high_risk_execution: 14`, `state_mutation: 926`, `dead_code: 3`, `fragile_debt: 4`, `duplicate_logic: 22`, `unreferenced_by_name: 93`
* *Architecture:* `io: 17`, `api: 16`, `concurrency: 2`, `import: 67`
* *Defense:* `safety: 1`, `doc: 29`, `test: 89`, `immutability_locks: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cargo_test_support::basic_manifest, cargo_test_support::compare::assert_e2e, cargo_test_support::git, cargo_test_support::paths::cargo_home, cargo_test_support::registry::Package, cargo_test_support::str, cargo_util::paths::self, crate::prelude::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cargo/core/compiler/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1425.5 | **LOC:** 2639 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 37.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **101**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (96.7%), Mutation Surface (formerly State Flux) (89.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.3%)
- **Documentation Coverage:** 26.3158% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rustc` **(Many-Argument Workhorses)** (Impact: 135.6)
    * *Intent:* /// Creates a unit of work invoking `rustc` for building the `unit`.
  * `build_base_args` **(Many-Argument Workhorses)** (Impact: 134.9)
    * *Intent:* /// Adds essential rustc flags and environment variables to the command to execute.
  * `on_stderr_line_inner` **(Many-Argument Workhorses)** (Impact: 125.7)
    * *Intent:* /// Returns true if the line should be cached.
  * `compile` **(Many-Argument Workhorses)** (Impact: 77.7)
    * *Intent:* /// Builds up and enqueue a list of pending jobs onto the `job` queue. /// /// Starting from the `un...
  * `add_native_deps` **(Many-Argument Workhorses)** (Impact: 54.2)
    * *Intent:* // Add all relevant `-L` and `-l` flags from dependencies (now calculated and // present in `state`)...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 69 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 220
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 425`, `structural_boundaries: 520`, `args: 126`, `func_start: 54`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 82`, `dead_code: 3`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 3`, `api: 38`, `concurrency: 2`, `import: 61`
* *Defense:* `safety: 57`, `doc: 184`, `test: 5`, `sync_locks: 13`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BufWriter, BuildScriptOutputs, BuildScripts, CompileKindFallback, CompileMode, CompileTarget, Doctest, Error...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cargo/util/context/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1257.3 | **LOC:** 2585 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 62.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **90**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (59.3%), Mutation Surface (formerly State Flux) (50.4%)
- **Documentation Coverage:** 30.8081% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `save_credentials` **(Many-Argument Workhorses)** (Impact: 95.3)
  * `configure` **(Many-Argument Workhorses)** (Impact: 63.7)
    * *Intent:* /// Update the instance based on settings typically passed in on /// the command-line. /// /// This ...
  * `cli_args_as_table` **(Compute Cores)** (Impact: 40.3)
    * *Intent:* /// Parses the CLI config args and returns them as a table.
  * `get_cv_with_env` **(Many-Argument Workhorses)** (Impact: 40.2)
    * *Intent:* /// This is a helper for getting a CV from a file or env var.
  * `include_paths` **(Many-Argument Workhorses)** (Impact: 32.5)
    * *Intent:* /// Converts the `include` config value to a list of absolute paths.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 41 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 390`, `structural_boundaries: 398`, `args: 203`, `func_start: 119`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 4`, `state_mutation: 48`, `dead_code: 6`, `planned_debt: 1`, `unreferenced_by_name: 35`
* *Architecture:* `io: 4`, `api: 97`, `concurrency: 1`, `import: 62`
* *Defense:* `safety: 65`, `doc: 369`, `test: 10`, `sync_locks: 23`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CacheLockMode, CacheLocker, File, GlobalCacheTracker, HashSet, IntoUrl, IntoUrlWithBase, Mutex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/testsuite/publish.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1216.2 | **LOC:** 4764 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 22.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (79.2%), Connectivity (formerly Api Exposure) (49.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.1%), Complexity Load (formerly Cognitive Load) (18.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `publish_git_with_version` **(I/O & Config Routines)** (Impact: 89.5)
    * *Intent:* // A dependency with both `git` and `version`.
  * `git_deps` **(I/O & Config Routines)** (Impact: 53.5)
  * `old_token_location` **(I/O & Config Routines)** (Impact: 6.0)
  * `simple` **(I/O & Config Routines)** (Impact: 5.0)
  * `duplicate_version` **(I/O & Config Routines)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 30 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 917
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 201`, `args: 104`, `func_start: 82`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 1`, `state_mutation: 857`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 20`, `import: 14`
* *Defense:* `doc: 4`, `test: 9`, `sync_locks: 45`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mutex, Package, RegistryBuilder, Response, cargo_test_support::Project, cargo_test_support::basic_manifest, cargo_test_support::git::self, cargo_test_support::registry::self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/testsuite/registry.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1136.18 | **LOC:** 4791 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 45.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (88.5%), Guard Balance (formerly Safety Score) (73.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.9%), Complexity Load (formerly Cognitive Load) (8.6%)
- **Documentation Coverage:** 99.6441% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `registry_index_rejected` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `sparse_retry_multiple` **(I/O & Config Routines)** (Impact: 12.6)
  * `dl_retry_multiple` **(I/O & Config Routines)** (Impact: 12.4)
  * `wrong_version_http` **(I/O & Config Routines)** (Impact: 8.2)
  * `wrong_version_git` **(I/O & Config Routines)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 468
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 335`, `args: 253`, `func_start: 175`
* *Risk/State:* `safety_bypasses: 69`, `high_risk_execution: 2`, `state_mutation: 446`
* *Architecture:* `io: 3`, `api: 119`, `import: 23`
* *Defense:* `doc: 4`, `test: 19`, `sync_locks: 24`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dependency, File, Package, PathBuf, RegistryBuilder, Response, TestRegistry, cargo::core::SourceId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/testsuite/build.rs` (RUST | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1115.78 | **LOC:** 6531 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 28.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 0.473; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (71.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.2%), Concurrency Surface (formerly Concurrency) (13.0%), Connectivity (formerly Api Exposure) (9.6%)
- **Documentation Coverage:** 99.0476% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `crate_env_vars` **(I/O & Config Routines)** (Impact: 103.5)
  * `repro` **(Compute Cores)** (Impact: 7.2)
  * `primary_package_env_var` **(I/O & Config Routines)** (Impact: 6.0)
  * `main` **(I/O & Config Routines)** (Impact: 5.5)
  * `incompatible_dependencies` **(I/O & Config Routines)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 7 instances
* *High Risk Execution (weighted view):* 25
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 622
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 407`, `args: 282`, `func_start: 250`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 74`, `high_risk_execution: 27`, `state_mutation: 608`, `fragile_debt: 2`, `duplicate_logic: 12`, `unreferenced_by_name: 62`
* *Architecture:* `io: 17`, `api: 68`, `concurrency: 8`, `import: 41`
* *Defense:* `safety: 3`, `doc: 8`, `test: 173`, `sync_locks: 4`, `immutability_locks: 21`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ProjectBuilder, basic_bin_manifest, basic_lib_manifest, basic_manifest, cargo::GlobalContext, cargo::core::Workspace, cargo::core::compiler::UserIntent, cargo::ops::CompileOptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cargo/core/workspace.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1113.58 | **LOC:** 2493 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 51.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **79**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (95.8%), Connectivity (formerly Api Exposure) (94.5%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (67.0%)
- **Documentation Coverage:** 52.2989% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emit_pkg_lints` **(Many-Argument Workhorses)** (Impact: 45.5)
  * `find_path_deps` **(Many-Argument Workhorses)** (Impact: 40.8)
  * `report_unknown_features_error` **(Many-Argument Workhorses)** (Impact: 39.8)
  * `find_members` **(Defensive Guards)** (Impact: 39.3)
    * *Intent:* /// After the root of a workspace has been located, probes for all members /// of a workspace. /// /...
  * `emit_ws_lints` **(Compute Cores)** (Impact: 32.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 350`, `structural_boundaries: 399`, `args: 210`, `func_start: 106`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 4`, `state_mutation: 62`, `dead_code: 3`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 72`, `import: 51`
* *Defense:* `safety: 60`, `doc: 198`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BTreeSet, CRATES_IO_REGISTRY, Edition, FeatureValue, GlobalContext, HashMap, HashSet, IntoUrl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/testsuite/git.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1004.78 | **LOC:** 4490 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 18.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (89.0%), Guard Balance (formerly Safety Score) (80.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.5%), Complexity Load (formerly Cognitive Load) (10.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `git_worktree_with_original_repo_renamed` **(I/O & Config Routines)** (Impact: 28.2)
  * `dirty_submodule` **(I/O & Config Routines)** (Impact: 10.8)
  * `failed_submodule_checkout` **(I/O & Config Routines)** (Impact: 8.4)
  * `git_with_force_push` **(I/O & Config Routines)** (Impact: 8.4)
  * `metadata_master_consistency` **(I/O & Config Routines)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 20 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 553
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 331`, `args: 239`, `func_start: 86`
* *Risk/State:* `safety_bypasses: 129`, `high_risk_execution: 1`, `state_mutation: 513`, `dead_code: 2`
* *Architecture:* `io: 4`, `api: 110`, `concurrency: 2`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `test: 25`, `sync_locks: 11`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ordering, TcpStream, basic_manifest, cargo_test_support::Project, cargo_test_support::basic_lib_manifest, cargo_test_support::git::add_submodule, cargo_test_support::paths, cargo_test_support::registry::Package...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/testsuite/artifact_dep.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 990.42 | **LOC:** 3593 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (79.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.1%), Connectivity (formerly Api Exposure) (9.7%), Complexity Load (formerly Cognitive Load) (9.5%)
- **Documentation Coverage:** 94.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assert_artifact_executable_output` **(Many-Argument Workhorses)** (Impact: 10.7)
  * `build_script_with_bin_artifacts` **(I/O & Config Routines)** (Impact: 8.7)
  * `build_script_features_for_shared_dependency` **(I/O & Config Routines)** (Impact: 8.5)
  * `features_are_not_unified_among_lib_and_bin_dep_of_different_target` **(I/O & Config Routines)** (Impact: 7.5)
  * `cross_doctests_works_with_artifacts` **(I/O & Config Routines)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 649
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 189`, `args: 190`, `func_start: 107`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 6`, `state_mutation: 621`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 51`
* *Architecture:* `io: 2`, `api: 53`, `import: 11`
* *Defense:* `safety: 1`, `doc: 27`, `test: 58`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RegistryBuilder, a::Trait, b::Trait, basic_bin_manifest, basic_manifest, cargo_test_support::
    Project, cargo_test_support::compare::assert_e2e, cargo_test_support::registry::Package...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/testsuite/test.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 968.72 | **LOC:** 5656 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 80.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.4%), Concurrency Surface (formerly Concurrency) (12.1%), Connectivity (formerly Api Exposure) (9.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cargo_test_doctest_xcompile_runner` **(I/O & Config Routines)** (Impact: 6.1)
  * `cargo_doc_test_quiet` **(I/O & Config Routines)** (Impact: 6.0)
  * `cyclical_dep_with_missing_feature` **(I/O & Config Routines)** (Impact: 4.7)
  * `doctest_skip_staticlib` **(I/O & Config Routines)** (Impact: 4.2)
  * `cargo_test_env` **(Annotated & Test Methods)** (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 196`, `args: 386`, `func_start: 269`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 49`, `state_mutation: 515`, `dead_code: 5`, `unreferenced_by_name: 123`
* *Architecture:* `io: 5`, `api: 69`, `concurrency: 1`, `import: 16`
* *Defense:* `doc: 136`, `test: 237`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` basic_lib_manifest, basic_manifest, cargo_test_support::basic_bin_manifest, cargo_test_support::cross_compile, cargo_test_support::registry::Package, cargo_test_support::rustc_host, cargo_util::paths::dylib_path_envvar, crate::prelude::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cargo/sources/git/utils.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 958.5 | **LOC:** 1786 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 43.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 0.473; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.4%), Guard Balance (formerly Safety Score) (53.0%)
- **Documentation Coverage:** 12.2807% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `github_fast_path` **(Many-Argument Workhorses)** (Impact: 89.0)
    * *Intent:* /// Attempts GitHub's special fast path for testing if we've already got an /// up-to-date copy of t...
  * `with_authentication` **(Many-Argument Workhorses)** (Impact: 79.1)
    * *Intent:* /// we fall back to the generic user of `git`. /// /// * If a username/password is allowed, then we ...
  * `fetch` **(Many-Argument Workhorses)** (Impact: 68.7)
    * *Intent:* /// Attempts to fetch the given git `reference` for a Git repository. /// /// This is the main entry...
  * `update_submodule` **(Many-Argument Workhorses)** (Impact: 68.3)
    * *Intent:* /// Update a single Git submodule, and recurse into its submodules.
  * `update_submodules` **(Many-Argument Workhorses)** (Impact: 68.0)
    * *Intent:* /// Like `git submodule update --recursive` but for this git checkout. /// /// This function respect...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 43 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 299`, `args: 88`, `func_start: 42`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 49`, `dead_code: 10`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 19`, `concurrency: 1`, `import: 24`
* *Defense:* `safety: 42`, `doc: 233`, `test: 7`, `sync_locks: 2`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` GitCliError, Instant, IntoUrl, MetricsCounter, ObjectType, Oid, Ordering, PathBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cargo/ops/cargo_add/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 947.38 | **LOC:** 1377 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 71.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.2%)
- **Documentation Coverage:** 59.2593% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve_dependency` **(Many-Argument Workhorses)** (Impact: 207.2)
  * `add` **(Many-Argument Workhorses)** (Impact: 110.1)
    * *Intent:* /// Add dependencies to a manifest
  * `get_public_dependency` **(Many-Argument Workhorses)** (Impact: 76.8)
  * `get_latest_dependency` **(Many-Argument Workhorses)** (Impact: 54.3)
  * `print_action_msg` **(Defensive Guards)** (Impact: 42.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 278`, `structural_boundaries: 292`, `args: 94`, `func_start: 26`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 3`, `state_mutation: 63`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 23`, `import: 43`
* *Defense:* `safety: 57`, `doc: 56`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` anyhow::Context, cargo_util::paths, cargo_util_schemas::core::PartialVersion, cargo_util_schemas::manifest::PathBaseName, cargo_util_schemas::manifest::RustVersion, cargo_util_terminal::Shell, crate::CargoResult, crate::GlobalContext...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/testsuite/bad_config.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 866.5 | **LOC:** 4189 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 47.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (74.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.3%), Complexity Load (formerly Cognitive Load) (15.9%), Connectivity (formerly Api Exposure) (6.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `redefined_sources` **(I/O & Config Routines)** (Impact: 76.5)
  * `duplicate_packages_in_cargo_lock` **(I/O & Config Routines)** (Impact: 5.0)
  * `bad1` **(I/O & Config Routines)** (Impact: 3.0)
  * `unsupported_float` **(I/O & Config Routines)** (Impact: 2.5)
  * `unsupported_datetime` **(I/O & Config Routines)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 669
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 195`, `args: 60`, `func_start: 122`
* *Risk/State:* `state_mutation: 657`, `duplicate_logic: 6`, `unreferenced_by_name: 12`
* *Architecture:* `api: 13`, `import: 32`
* *Defense:* `doc: 5`, `test: 3`, `sync_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Package, basic_bin_manifest, basic_manifest, cargo_test_support::Project, cargo_test_support::git::cargo_uses_gitoxide, cargo_test_support::registry::self, crate::prelude::*, project...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cargo/core/global_cache_tracker.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 836.9 | **LOC:** 1840 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (65.3%), Guard Balance (formerly Safety Score) (48.8%), Debt Markers (formerly Tech Debt) (36.9%)
- **Documentation Coverage:** 8.642% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `populate_untracked` **(Many-Argument Workhorses)** (Impact: 65.8)
    * *Intent:* /// Updates the database to add any files that are currently not tracked /// (such as when they are ...
  * `clean_inner` **(Many-Argument Workhorses)** (Impact: 59.5)
  * `get_git_items_to_clean_size` **(Many-Argument Workhorses)** (Impact: 53.3)
    * *Intent:* /// Adds paths to delete from the git cache, keeping the total size under /// the give value. /// //...
  * `sync_db_with_files` **(Many-Argument Workhorses)** (Impact: 41.9)
    * *Intent:* /// 2. Adds missing entries to the database that are on disk (such as when /// files are added by ol...
  * `get_registry_items_to_clean_size_both` **(Many-Argument Workhorses)** (Impact: 32.1)
    * *Intent:* /// Adds paths to delete from both `registry_crate` and `registry_src` in /// order to keep the tota...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 327`, `args: 89`, `func_start: 58`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 46`, `dead_code: 1`, `planned_debt: 4`, `unreferenced_by_name: 15`
* *Architecture:* `io: 2`, `api: 41`, `import: 19`
* *Defense:* `safety: 27`, `doc: 348`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ErrorCode, GlobalContext, Migration, PathBuf, Progress, ProgressStyle, SystemTime, anyhow::Context...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/testsuite/patch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 798.18 | **LOC:** 3433 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 64.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (76.9%), Guard Balance (formerly Safety Score) (76.7%), Connectivity (formerly Api Exposure) (64.6%), Complexity Load (formerly Cognitive Load) (15.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `patch_to_git_pull_request` **(I/O & Config Routines)** (Impact: 52.5)
  * `perform_old_git_patch` **(I/O & Config Routines)** (Impact: 12.8)
  * `mismatched_version_with_prerelease` **(I/O & Config Routines)** (Impact: 8.2)
  * `patch_eq_conflict_panic` **(I/O & Config Routines)** (Impact: 5.0)
    * *Intent:* // From https://github.com/rust-lang/cargo/issues/7463
  * `mismatched_version2` **(I/O & Config Routines)** (Impact: 5.0)
    * *Intent:* // From https://github.com/rust-lang/cargo/issues/11336
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 561
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 112`, `args: 38`, `func_start: 63`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 547`
* *Architecture:* `io: 2`, `api: 47`, `import: 17`
* *Defense:* `doc: 1`, `test: 15`, `sync_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Package, bar::hello, cargo_test_support::basic_manifest, cargo_test_support::git, cargo_test_support::paths, cargo_test_support::registry::self, crate::prelude::*, project...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/cargo-util-schemas/src/manifest/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 784.72 | **LOC:** 1840 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (88.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.1%), Mutation Surface (formerly State Flux) (31.4%)
- **Documentation Coverage:** 89.1192% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `merge` **(Defensive Guards)** (Impact: 46.2)
    * *Intent:* /// Overwrite self's values with the given profile.
  * `deserialize` **(Generic / Templated Code)** (Impact: 15.0)
  * `visit_map` **(Defensive Guards)** (Impact: 15.0)
    * *Intent:* // Deserialize MyMap from an abstract "map" provided by the // Deserializer. The MapAccess input is ...
  * `fmt` **(Defensive Guards)** (Impact: 12.9)
  * `deserialize` **(Generic / Templated Code)** (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 284`, `args: 189`, `func_start: 129`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 22`, `duplicate_logic: 14`, `unreferenced_by_name: 34`
* *Architecture:* `api: 269`, `import: 22`
* *Defense:* `safety: 36`, `doc: 58`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Display, IntoDeserializer, Serialize, Unexpected, Write, crate::core::PackageIdSpec, crate::restricted_names, crate::restricted_names::NameValidationError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/testsuite/vendor.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 780.58 | **LOC:** 2259 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 44.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (84.0%), Connectivity (formerly Api Exposure) (56.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.7%), Complexity Load (formerly Cognitive Load) (26.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `git_deterministic` **(I/O & Config Routines)** (Impact: 7.0)
  * `discovery_inferred_build_rs_included` **(I/O & Config Routines)** (Impact: 6.0)
  * `discovery_inferred_build_rs_excluded` **(I/O & Config Routines)** (Impact: 6.0)
  * `discovery_inferred_lib_included` **(I/O & Config Routines)** (Impact: 6.0)
  * `discovery_inferred_lib_excluded` **(I/O & Config Routines)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 545
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 124`, `args: 93`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 439`
* *Architecture:* `io: 2`, `api: 46`, `import: 11`
* *Defense:* `doc: 5`, `test: 38`, `sync_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Package, RegistryBuilder, basic_lib_manifest, basic_manifest, cargo_test_support::Project, cargo_test_support::assert_deterministic_mtime, cargo_test_support::compare::assert_e2e, cargo_test_support::git...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/testsuite/doc.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 779.62 | **LOC:** 4032 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 58.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (70.0%), Guard Balance (formerly Safety Score) (61.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.5%), Complexity Load (formerly Cognitive Load) (5.1%)
- **Documentation Coverage:** 97.6331% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mergeable_info_rebuild_detection` **(I/O & Config Routines)** (Impact: 9.5)
  * `mergeable_info_rebuild_with_depinfo` **(I/O & Config Routines)** (Impact: 9.5)
  * `doc_fingerprint_is_versioning_consistent` **(I/O & Config Routines)** (Impact: 8.5)
  * `mergeable_info_multi_targets` **(I/O & Config Routines)** (Impact: 8.0)
  * `mergeable_info_additive` **(I/O & Config Routines)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 306
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 185`, `args: 114`, `func_start: 123`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 38`, `high_risk_execution: 2`, `state_mutation: 304`, `dead_code: 1`, `fragile_debt: 4`
* *Architecture:* `io: 1`, `api: 164`, `import: 17`
* *Defense:* `doc: 66`, `test: 159`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` a::fun, basic_manifest, cargo_test_support::basic_lib_manifest, cargo_test_support::compare::assert_e2e, cargo_test_support::cross_compile, cargo_test_support::registry::Package, cargo_test_support::rustc_host, cargo_test_support::str...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cargo/util/toml_mut/dependency.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 768.4 | **LOC:** 1321 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (81.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%)
- **Documentation Coverage:** 37.2881% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_toml` **(Many-Argument Workhorses)** (Impact: 166.7)
    * *Intent:* /// Create a dependency from a TOML table entry.
  * `update_toml` **(Many-Argument Workhorses)** (Impact: 113.0)
    * *Intent:* /// Modify existing entry to match this dependency.
  * `to_toml` **(Many-Argument Workhorses)** (Impact: 46.9)
    * *Intent:* /// Convert dependency to TOML. /// /// Returns a tuple with the dependency's name and either the ve...
  * `path_field` **(Many-Argument Workhorses)** (Impact: 15.8)
  * `source_id` **(Defensive Guards)** (Impact: 14.7)
    * *Intent:* /// Get the `SourceID` for this dependency.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 42 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 259`, `args: 95`, `func_start: 68`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 67`, `high_risk_execution: 1`, `state_mutation: 64`, `duplicate_logic: 2`
* *Architecture:* `api: 75`, `import: 17`
* *Defense:* `safety: 68`, `doc: 82`, `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Formatter, GitReference, PathBuf, cargo_util::paths, cargo_util_schemas::manifest::PathBaseName, crate::CargoResult, crate::GlobalContext, crate::core::Features...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cargo/util/toml/targets.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 759.84 | **LOC:** 1259 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.7%), Complexity Load (formerly Cognitive Load) (15.8%)
- **Documentation Coverage:** 89.5833% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalize_lib` **(Many-Argument Workhorses)** (Impact: 61.8)
  * `normalize_targets_with_legacy_path` **(Many-Argument Workhorses)** (Impact: 55.6)
  * `toml_targets_and_inferred` **(Many-Argument Workhorses)** (Impact: 55.3)
  * `normalize_bins` **(Many-Argument Workhorses)** (Impact: 51.9)
  * `to_targets` **(Many-Argument Workhorses)** (Impact: 50.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 37 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 243`, `args: 82`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 3`, `state_mutation: 50`, `unreferenced_by_name: 7`
* *Architecture:* `io: 1`, `api: 7`, `import: 13`
* *Defense:* `safety: 46`, `doc: 25`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DirEntry, Feature, Features, HashSet, PathBuf, StringOrVec, Target, TomlBenchTarget...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cargo/ops/fix/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 747.74 | **LOC:** 1453 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **58**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.8%), Debt Markers (formerly Tech Debt) (32.1%)
- **Documentation Coverage:** 63.6364% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rustfix_and_fix` **(Many-Argument Workhorses)** (Impact: 76.1)
    * *Intent:* /// Executes `rustc` to apply one round of suggestions to the crate in question. /// /// This will f...
  * `migrate_manifests` **(Many-Argument Workhorses)** (Impact: 71.5)
  * `rustfix_crate` **(Many-Argument Workhorses)** (Impact: 65.3)
    * *Intent:* /// Attempts to apply fixes to a single crate. /// /// This runs `rustc` (possibly multiple times) t...
  * `check_resolver_change` **(Many-Argument Workhorses)** (Impact: 45.9)
  * `fix` **(Many-Argument Workhorses)** (Impact: 43.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 42 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 154
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 287`, `args: 89`, `func_start: 29`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 3`, `state_mutation: 70`, `planned_debt: 2`, `fragile_debt: 5`, `unreferenced_by_name: 4`
* *Architecture:* `io: 5`, `api: 14`, `import: 35`
* *Defense:* `safety: 36`, `doc: 110`, `test: 8`, `sync_locks: 2`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CompileOptions, ExitStatus, FeatureOpts, FeatureResolver, FeaturesFor, HashMap, HashSet, LockServerClient...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/cargo-test-support/src/registry.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 732.9 | **LOC:** 1879 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 0.473; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (95.4%), Mutation Surface (formerly State Flux) (80.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.2%)
- **Documentation Coverage:** 22.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_authorized` **(Many-Argument Workhorses)** (Impact: 54.0)
  * `build` **(Compute Cores)** (Impact: 47.2)
    * *Intent:* /// Initializes the registry.
  * `append_manifest` **(Many-Argument Workhorses)** (Impact: 40.6)
  * `start` **(Compute Cores)** (Impact: 26.7)
  * `index` **(Compute Cores)** (Impact: 23.2)
    * *Intent:* /// Serve the registry index
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 29 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 11
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 321`, `args: 110`, `func_start: 96`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 51`, `high_risk_execution: 3`, `state_mutation: 78`, `planned_debt: 2`
* *Architecture:* `io: 4`, `api: 102`, `concurrency: 6`, `import: 21`
* *Defense:* `safety: 29`, `doc: 249`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AsymmetricSecretKey, BufReader, File, HashMap, Header, JoinHandle, OffsetDateTime, PathBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cargo/ops/cargo_update.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 728.88 | **LOC:** 1258 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **40**; blast radius 0.473; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.3%), Guard Balance (formerly Safety Score) (53.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.0%)
- **Documentation Coverage:** 84.0909% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `upgrade_dependency` **(Many-Argument Workhorses)** (Impact: 73.3)
  * `update_lockfile` **(Many-Argument Workhorses)** (Impact: 67.7)
  * `write_manifest_upgrades` **(Many-Argument Workhorses)** (Impact: 59.6)
    * *Intent:* /// Update manifests with upgraded versions, and write to disk. Based on /// cargo-edit. Returns tru...
  * `print_lockfile_updates` **(Many-Argument Workhorses)** (Impact: 50.6)
  * `upgrade_manifests` **(Many-Argument Workhorses)** (Impact: 44.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 30 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 303`, `args: 87`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 37`, `planned_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 22`, `import: 26`
* *Defense:* `safety: 40`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HasDevUnits, HashMap, HashSet, IndexSet, PackageIdSpec, PackageIdSpecQuery, Source, SourceId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/cargo/util/context/mod.rs` -> Churn: **100.0%** | Cog Load: 14.0997% | Debt: 59.3482%
- `src/cargo/core/compiler/build_runner/compilation_files.rs` -> Churn: **78.64%** | Cog Load: 8.1075% | Debt: 87.2788%
- `src/cargo/core/resolver/errors.rs` -> Churn: **66.81%** | Cog Load: 40.6412% | Debt: 58.6157%
- `src/cargo/util/mod.rs` -> Churn: **59.98%** | Cog Load: 5.5347% | Debt: 70.4909%
- `src/cargo/sources/registry/mod.rs` -> Churn: **50.19%** | Cog Load: 13.3721% | Debt: 52.507%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/cargo/core/global_cache_tracker.rs` -> **Ed Page** (100.0% isolated ownership) | Magnitude: 836.9
- `src/cargo/util/toml_mut/dependency.rs` -> **Ed Page** (100.0% isolated ownership) | Magnitude: 768.4
- `src/cargo/util/toml/targets.rs` -> **Naman Garg** (100.0% isolated ownership) | Magnitude: 759.84
- `tests/testsuite/fix.rs` -> **Ed Page** (100.0% isolated ownership) | Magnitude: 706.0
- `tests/testsuite/features2.rs` -> **Joe Neeman** (100.0% isolated ownership) | Magnitude: 630.86

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/cargo/util/credential/process.rs` -> **Severity: 0.316** (Embedded: 0.0045 * Error Risk: 70.0836%)
- `crates/mdman/src/format/md.rs` -> **Severity: 0.164** (Embedded: 0.0019 * Error Risk: 84.7005%)
- `src/bin/cargo/commands/info.rs` -> **Severity: 0.144** (Embedded: 0.002 * Error Risk: 71.9676%)
- `src/cargo/util/io.rs` -> **Severity: 0.118** (Embedded: 0.0026 * Error Risk: 45.7248%)
- `src/cargo/core/resolver/context.rs` -> **Severity: 0.099** (Embedded: 0.002 * Error Risk: 49.2501%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/cargo/util/credential/process.rs` -> **Severity: 389.1** (Blast Radius: 3.891 * Doc Risk: 100.0%)
- `src/cargo/util/io.rs` -> **Severity: 282.6** (Blast Radius: 2.826 * Doc Risk: 100.0%)
- `src/bin/cargo/commands/info.rs` -> **Severity: 208.1** (Blast Radius: 2.081 * Doc Risk: 100.0%)
- `crates/mdman/src/format/md.rs` -> **Severity: 130.6** (Blast Radius: 1.306 * Doc Risk: 100.0%)
- `src/bin/cargo/commands/init.rs` -> **Severity: 107.6** (Blast Radius: 1.076 * Doc Risk: 100.0%)

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
