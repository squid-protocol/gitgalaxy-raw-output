# ARCHITECTURAL_BRIEF: cargo
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/rust-lang/cargo.git` |
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
- **Scope:** 2011 analyzed artifact(s), 271928 LOC.
- **Load-bearing artifact:** `crates/cargo-test-support/src/lib.rs` -- 536 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tests/testsuite/main.rs` -- pulls in 202 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tests/testsuite/package.rs` at magnitude 2447.56 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 2011 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 931 |
| Total LOC | 271928 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 68.4% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4983 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.312 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 13.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.7774 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 12 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1220 | 268150 | 60.7% |
| XML | 383 | 3 | 19.0% |
| MARKDOWN | 242 | 0 | 12.0% |
| PLAINTEXT | 127 | 0 | 6.3% |
| JSON | 17 | 2070 | 0.8% |
| YAML | 9 | 570 | 0.4% |
| SHELL | 6 | 349 | 0.3% |
| PYTHON | 2 | 94 | 0.1% |
| DOCKERFILE | 2 | 44 | 0.1% |
| JAVASCRIPT | 1 | 637 | 0.0% |
| CSS | 1 | 6 | 0.0% |
| HTML | 1 | 5 | 0.0% |

## 4.1 SOURCE ENCODINGS
All 2011 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 55%, Large Core Modules 18%, Declarative / Non-Code 7%, Large Core Modules (3) 6%, State Mutators Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1641 | 81.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 369 | 18.3% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 931*

**Composition by Extension & Reason:**
- `.toml`: 380x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 285x Unsupported Format (.toml), 7x Excluded (Unsupported Extension: '.toml')
- `.rs`: 128x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1213 LOC)
- `no_extension`: 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected), 1x Unsupported Format (.undeterminable)
- `.lock`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 12x Excluded (Unsupported Extension: '.lock')
- `.stderr`: 19x Excluded (Unsupported Extension: '.stderr')
- `.stdout`: 14x Excluded (Unsupported Extension: '.stdout')
- `.tgz`: 10x Excluded (Explicitly Denied Extension: '.tgz')
- `.png`: 7x Excluded (Explicitly Denied Extension: '.png')
- `.svg`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1481 LOC)
- `.conf`: 1x Excluded (Unsupported Extension: '.conf')
- `.1`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 92.8 | 3.0 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.4 | 16.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 91.2 | 13.2 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.9 | 1.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 10.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 11.4 | 0.9 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 6.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 50.8 | 63.2 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 303 | 115 | 0 | `src/cargo/util/cpu.rs` |
| cleanup | 112 | 45 | 0 | `tests/testsuite/global_cache_tracker.rs` |
| guards | 2987 | 359 | 3 | `src/cargo/util/toml/mod.rs` |
| danger | 4844 | 350 | 4 | `tests/testsuite/config.rs` |
| concurrency | 1381 | 157 | 0 | `tests/testsuite/package.rs` |
| connectivity | 8730 | 536 | 13 | `crates/cargo-util-schemas/src/manifest/mod.rs` |
| io | 636 | 181 | 0 | `tests/testsuite/package.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 77 | 48 | 0 | `tests/testsuite/profile_trim_paths.rs` |
| time | 34 | 28 | 0 | `src/etc/cargo.bashcomp.sh` |
| serialization | 107 | 40 | 0 | `credential/cargo-credential/src/lib.rs` |
| regex | 15 | 9 | 0 | `src/etc/cargo.bashcomp.sh` |
| events | 514 | 85 | 0 | `src/cargo/core/global_cache_tracker.rs` |
| tests | 3503 | 266 | 2 | `tests/testsuite/test.rs` |
| docs | 14676 | 439 | 10 | `src/cargo/core/compiler/fingerprint/mod.rs` |
| debt | 1376 | 229 | 1 | `tests/testsuite/build_script.rs` |
| mutation | 58505 | 827 | 48 | `tests/testsuite/package.rs` |
| dead_code | 749 | 489 | 1 | `src/cargo/util/context/mod.rs` |
| credential | 34 | 8 | 0 | `src/cargo/sources/git/known_hosts.rs` |
| threat | 5 | 3 | 0 | `src/cargo/sources/git/known_hosts.rs` |
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

1. **lib.rs** (`crates/cargo-test-support/src/lib.rs`) — 536 inbound connections
2. **lib.rs** (`tests/testsuite/mock-std/library/std/src/lib.rs`) — 359 inbound connections
3. **compare.rs** (`crates/cargo-test-support/src/compare.rs`) — 292 inbound connections
4. **errors.rs** (`src/cargo/util/errors.rs`) — 167 inbound connections
5. **mod.rs** (`src/cargo/util/context/mod.rs`) — 117 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **main.rs** (`tests/testsuite/main.rs`) — 202 outbound dependencies
2. **mod.rs** (`tests/testsuite/cargo_add/mod.rs`) — 165 outbound dependencies
3. **mod.rs** (`src/cargo/core/compiler/mod.rs`) — 124 outbound dependencies
4. **mod.rs** (`src/cargo/ops/mod.rs`) — 109 outbound dependencies
5. **mod.rs** (`src/cargo/util/mod.rs`) — 100 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `to_real_manifest` **(Many-Argument Workhorses)** (@ `src/cargo/util/toml/mod.rs`) -> Impact: **312.2** | LOC: 619
- `resolve_dependency` **(Many-Argument Workhorses)** (@ `src/cargo/ops/cargo_add/mod.rs`) -> Impact: **207.2** | LOC: 184
- `create_bcx` **(Many-Argument Workhorses)** (@ `src/cargo/ops/cargo_compile/mod.rs`) -> Impact: **195.0** | LOC: 456
  * *Intent:* /// Prepares all required information for the actual compilation. /// /// For how it works and what data it collects, /// please see the [module-level...
- `new` **(Many-Argument Workhorses)** (@ `src/cargo/ops/cargo_install.rs`) -> Impact: **190.9** | LOC: 213
  * *Intent:* // Returns pkg to install. None if pkg is already installed
- `normalize_package_toml` **(Many-Argument Workhorses)** (@ `src/cargo/util/toml/mod.rs`) -> Impact: **174.7** | LOC: 213
- `sync` **(Many-Argument Workhorses)** (@ `src/cargo/ops/vendor.rs`) -> Impact: **169.2** | LOC: 304
- `clean_specs` **(Many-Argument Workhorses)** (@ `src/cargo/ops/cargo_clean.rs`) -> Impact: **166.4** | LOC: 258
- `from_toml` **(Many-Argument Workhorses)** (@ `src/cargo/util/toml_mut/dependency.rs`) -> Impact: **164.0** | LOC: 159
  * *Intent:* /// Create a dependency from a TOML table entry.
- `parse` **(Many-Argument Workhorses)** (@ `src/cargo/core/compiler/custom_build.rs`) -> Impact: **149.3** | LOC: 346
  * *Intent:* /// Parses the output instructions of a build script. /// /// * `pkg_descr` --- for error messages /// * `library_name` --- for determining if `RUSTC_...
- `install_one` **(Many-Argument Workhorses)** (@ `src/cargo/ops/cargo_install.rs`) -> Impact: **148.6** | LOC: 304

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/testsuite` | 152 | 35067.06 | 5.33% | 0.0% |
| `src/cargo/core` | 13 | 5229.3 | 8.24% | 5.74% |
| `src/cargo/ops` | 19 | 4895.74 | 15.83% | 6.97% |
| `src/cargo/core/compiler` | 19 | 4172.64 | 8.39% | 9.74% |
| `src/cargo/util` | 37 | 3557.3 | 8.57% | 12.86% |
| `src/cargo/util/toml` | 3 | 2656.98 | 13.1% | 15.21% |
| `src/cargo/core/resolver` | 10 | 2341.38 | 11.31% | 7.87% |
| `src/cargo/util/context` | 10 | 2285.38 | 8.85% | 8.97% |
| `crates/cargo-test-support/src` | 9 | 2016.56 | 6.23% | 8.16% |
| `src/bin/cargo/commands` | 40 | 1673.72 | 9.29% | 1.7% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/cargo/util/errors.rs` -> **100.0%** Exposure
- `src/cargo/util/once.rs` -> **100.0%** Exposure
- `.github/ISSUE_TEMPLATE/bug_report.yml` -> **99.9999%** Exposure
- `src/cargo/sources/path.rs` -> **99.9745%** Exposure
- `crates/mdman/src/format/mod.rs` -> **99.9447%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/cargo/util/dependency_queue.rs` -> **100.0%** Exposure
- `src/cargo/util/edit_distance.rs` -> **100.0%** Exposure
- `src/cargo/util/graph.rs` -> **100.0%** Exposure
- `src/cargo/util/network/http.rs` -> **100.0%** Exposure
- `src/cargo/util/network/http_async.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/cargo-util-schemas/src/manifest/mod.rs` -> **34** Orphaned Functions | **14** Duplicates
- `src/cargo/util/context/mod.rs` -> **35** Orphaned Functions | **0** Duplicates
- `crates/resolver-tests/tests/pubgrub.rs` -> **28** Orphaned Functions | **0** Duplicates
- `src/cargo/sources/path.rs` -> **0** Orphaned Functions | **24** Duplicates
- `tests/testsuite/build_script.rs` -> **0** Orphaned Functions | **22** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `src/cargo/sources/git/known_hosts.rs` -> **100.0%** Exposure
- `tests/testsuite/ssh.rs` -> **65.6928%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `7` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `9542` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tests/testsuite/package.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.452)
- **Top Global Matches:** file_cluster_12: 7.452, file_cluster_13: 9.316, file_cluster_2: 9.375
- **Magnitude:** 2447.56 | **LOC:** 8033 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **29**; blast radius 0.263; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.8%), Connectivity (formerly Api Exposure) (59.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (55.9%), Complexity Load (formerly Cognitive Load) (26.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `workspace_noconflict_readme` **(I/O & Config Routines)** (Impact: 143.0)
  * `git_dependency_no_version` **(I/O & Config Routines)** (Impact: 64.0)
  * `long_file_names` **(I/O & Config Routines)** (Impact: 6.4)
  * `include_exclude_test` **(Many-Argument Workhorses)** (Impact: 6.1)
  * `repackage_smaller_local_dep_tmp_registry_checksum_match` **(I/O & Config Routines)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 182 instances
* *State Mutation (weighted view):* 1912
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 357`, `args: 150`, `func_start: 141`
* *Risk/State:* `safety_bypasses: 106`, `high_risk_execution: 1`, `state_mutation: 1548`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 55`, `api: 58`, `import: 25`
* *Defense:* `safety: 1`, `doc: 26`, `test: 25`, `sync_locks: 104`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.263
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.000895
  * `Imports (Out-Degree: 11):` aux, con, bar, cargo::util::HumanBytes, cargo_test_support::Project, cargo_test_support::ProjectBuilder, cargo_test_support::basic_manifest, cargo_test_support::git...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cargo/util/toml/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.29)
- **Top Global Matches:** file_cluster_4: 8.29, file_cluster_6: 8.546, file_cluster_12: 14.57
- **Magnitude:** 1889.62 | **LOC:** 3335 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 41.7%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **85**; blast radius 0.584; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.6%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (67.3%), Guard Balance (formerly Safety Score) (52.7%)
- **Documentation Coverage:** 68.8312% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_real_manifest` **(Many-Argument Workhorses)** (Impact: 312.2)
  * `normalize_package_toml` **(Many-Argument Workhorses)** (Impact: 174.7)
  * `prepare_toml_for_publish` **(Many-Argument Workhorses)** (Impact: 129.0)
    * *Intent:* /// Prepares the manifest for publishing. // - Path and git components of dependency specifications ...
  * `normalize_toml` **(Many-Argument Workhorses)** (Impact: 119.5)
    * *Intent:* /// See [`Manifest::normalized_toml`] for more details
  * `dep_to_dependency` **(Many-Argument Workhorses)** (Impact: 90.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 65 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 517`, `structural_boundaries: 562`, `args: 191`, `func_start: 65`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 54`, `high_risk_execution: 6`, `state_mutation: 79`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 14`, `import: 41`
* *Defense:* `safety: 103`, `doc: 35`, `test: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.584
  * `Choke Point (Betweenness):` 0.0007 | `Ripple Effect (Closeness):` 0.095392
  * `Imports (Out-Degree: 30):` embedded, targets, anyhow::Context, anyhow::anyhow, anyhow::bail, cargo_platform::Platform, cargo_util::paths, cargo_util_schemas::manifest...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `tests/testsuite/build_script.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.624)
- **Top Global Matches:** file_cluster_12: 7.624, file_cluster_13: 9.516, file_cluster_11: 9.85
- **Magnitude:** 1549.88 | **LOC:** 6815 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 46.2%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **35**; blast radius 0.263; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.5%), Connectivity (formerly Api Exposure) (60.6%), Guard Balance (formerly Safety Score) (60.3%), Concurrency Surface (formerly Concurrency) (12.2%)
- **Documentation Coverage:** 95.7806% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_rename_with_link_search_path` **(Many-Argument Workhorses)** (Impact: 27.8)
  * `code_generation` **(I/O & Config Routines)** (Impact: 27.0)
  * `rerun_if_directory` **(I/O & Config Routines)** (Impact: 15.5)
  * `generate_good_d_files` **(I/O & Config Routines)** (Impact: 9.5)
  * `custom_build_env_vars` **(I/O & Config Routines)** (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 936
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 338`, `args: 338`, `func_start: 250`
* *Risk/State:* `safety_bypasses: 104`, `high_risk_execution: 14`, `state_mutation: 926`, `fragile_debt: 4`, `duplicate_logic: 22`
* *Architecture:* `io: 17`, `api: 109`, `concurrency: 2`, `import: 67`
* *Defense:* `safety: 1`, `doc: 29`, `test: 89`, `immutability_locks: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.263
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000895
  * `Imports (Out-Degree: 13):` a, aaaaa, b, bar, cargo_test_support::basic_manifest, cargo_test_support::compare::assert_e2e, cargo_test_support::cross_compile, cargo_test_support::git...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cargo/core/compiler/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.12)
- **Top Global Matches:** file_cluster_6: 8.12, file_cluster_8: 10.662, file_cluster_4: 15.41
- **Magnitude:** 1404.0 | **LOC:** 2639 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 40.9%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **124**; blast radius 0.454; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (89.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.1%)
- **Documentation Coverage:** 26.3158% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_base_args` **(Many-Argument Workhorses)** (Impact: 130.9)
    * *Intent:* /// Adds essential rustc flags and environment variables to the command to execute.
  * `rustc` **(Many-Argument Workhorses)** (Impact: 129.6)
    * *Intent:* /// Creates a unit of work invoking `rustc` for building the `unit`.
  * `on_stderr_line_inner` **(Many-Argument Workhorses)** (Impact: 125.7)
    * *Intent:* /// Returns true if the line should be cached.
  * `compile` **(Many-Argument Workhorses)** (Impact: 77.7)
    * *Intent:* /// Builds up and enqueue a list of pending jobs onto the `job` queue. /// /// Starting from the `un...
  * `rustdoc` **(Many-Argument Workhorses)** (Impact: 52.5)
    * *Intent:* /// Creates a unit of work invoking `rustdoc` for documenting the `unit`.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 69 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 220
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 417`, `structural_boundaries: 520`, `args: 126`, `func_start: 54`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 82`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 3`, `api: 38`, `concurrency: 2`, `import: 61`
* *Defense:* `safety: 57`, `doc: 184`, `test: 5`, `sync_locks: 13`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.454
  * `Choke Point (Betweenness):` 0.004518 | `Ripple Effect (Closeness):` 0.09254
  * `Imports (Out-Degree: 49):` artifact, build_config, build_context, build_runner, compilation, compile_kind, crate_type, custom_build...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/cargo/util/context/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.519)
- **Top Global Matches:** file_cluster_4: 8.519, file_cluster_0: 8.935, file_cluster_12: 9.411
- **Magnitude:** 1238.2 | **LOC:** 2585 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **117** in-repo importer(s); it depends on **99**; blast radius 3.905; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (72.8%), Debt Markers (formerly Tech Debt) (59.3%), Mutation Surface (formerly State Flux) (50.4%)
- **Documentation Coverage:** 30.8081% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `save_credentials` **(Many-Argument Workhorses)** (Impact: 93.3)
  * `configure` **(Many-Argument Workhorses)** (Impact: 63.7)
    * *Intent:* /// Update the instance based on settings typically passed in on /// the command-line. /// /// This ...
  * `get_cv_with_env` **(Many-Argument Workhorses)** (Impact: 38.4)
    * *Intent:* /// This is a helper for getting a CV from a file or env var.
  * `cli_args_as_table` **(Compute Cores)** (Impact: 34.7)
    * *Intent:* /// Parses the CLI config args and returns them as a table.
  * `include_paths` **(Many-Argument Workhorses)** (Impact: 32.5)
    * *Intent:* /// Converts the `include` config value to a list of absolute paths.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 41 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 379`, `structural_boundaries: 398`, `args: 203`, `func_start: 119`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 4`, `state_mutation: 48`, `planned_debt: 1`, `unreferenced_by_name: 35`
* *Architecture:* `io: 4`, `api: 97`, `concurrency: 1`, `import: 62`
* *Defense:* `safety: 65`, `doc: 369`, `test: 10`, `sync_locks: 23`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.905
  * `Choke Point (Betweenness):` 0.006026 | `Ripple Effect (Closeness):` 0.10166
  * `Imports (Out-Degree: 37):` config_value, de, environment, error, key, path, schema, target...
  * `Imported By (In-Degree: 117):` (Excluded from Brief to save tokens)

### `tests/testsuite/publish.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.011)
- **Top Global Matches:** file_cluster_4: 8.011, file_cluster_2: 9.202, file_cluster_13: 9.419
- **Magnitude:** 1182.3 | **LOC:** 4764 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **17**; blast radius 0.263; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.6%), Connectivity (formerly Api Exposure) (47.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.7%), Complexity Load (formerly Cognitive Load) (18.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `publish_git_with_version` **(I/O & Config Routines)** (Impact: 122.0)
    * *Intent:* // A dependency with both `git` and `version`.
  * `git_deps` **(I/O & Config Routines)** (Impact: 38.5)
  * `old_token_location` **(I/O & Config Routines)** (Impact: 3.5)
  * `publish_checks_for_token_before_verify` **(I/O & Config Routines)** (Impact: 3.0)
  * `publish_with_bad_source` **(I/O & Config Routines)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 12 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 881
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 201`, `args: 104`, `func_start: 82`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 1`, `state_mutation: 857`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 20`, `import: 14`
* *Defense:* `doc: 4`, `test: 9`, `sync_locks: 45`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.263
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000895
  * `Imports (Out-Degree: 7):` bar, cargo_test_support::Project, cargo_test_support::basic_manifest, cargo_test_support::git, cargo_test_support::git::repo, cargo_test_support::paths, cargo_test_support::project, cargo_test_support::publish...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/testsuite/build.rs` (RUST | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.988)
- **Top Global Matches:** file_cluster_12: 7.988, file_cluster_13: 9.076, file_cluster_15: 9.72
- **Magnitude:** 1126.68 | **LOC:** 6531 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **58**; blast radius 0.263; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (76.9%), Guard Balance (formerly Safety Score) (57.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.1%), Concurrency Surface (formerly Concurrency) (13.0%)
- **Documentation Coverage:** 98.7879% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `crate_env_vars` **(I/O & Config Routines)** (Impact: 81.0)
  * `repro` **(Compute Cores)** (Impact: 7.2)
  * `main` **(I/O & Config Routines)** (Impact: 5.5)
  * `build_with_symlink_to_path_dependency_with_build_script_in_git` **(I/O & Config Routines)** (Impact: 4.2)
  * `cargo_compile_api_exposes_artifact_paths` **(I/O & Config Routines)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *High Risk Execution (weighted view):* 25
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 610
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 407`, `args: 282`, `func_start: 250`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 74`, `high_risk_execution: 27`, `state_mutation: 608`, `fragile_debt: 2`, `duplicate_logic: 12`
* *Architecture:* `io: 17`, `api: 128`, `concurrency: 8`, `import: 41`
* *Defense:* `safety: 3`, `doc: 8`, `test: 173`, `sync_locks: 4`, `immutability_locks: 21`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.263
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.000895
  * `Imports (Out-Degree: 18):` a, aaaaa, bar, baz, bbbbb, build, cargo::GlobalContext, cargo::core::Workspace...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cargo/core/workspace.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.315)
- **Top Global Matches:** file_cluster_4: 7.315, file_cluster_0: 11.505, file_cluster_12: 11.542
- **Magnitude:** 1091.38 | **LOC:** 2493 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 47.4%
- **Blast Radius:** changing it is visible to **68** in-repo importer(s); it depends on **79**; blast radius 2.434; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (96.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.1%), Mutation Surface (formerly State Flux) (67.0%)
- **Documentation Coverage:** 52.2989% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emit_pkg_lints` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `report_unknown_features_error` **(Many-Argument Workhorses)** (Impact: 39.8)
  * `find_path_deps` **(Many-Argument Workhorses)** (Impact: 38.5)
  * `find_members` **(Defensive Guards)** (Impact: 36.5)
    * *Intent:* /// After the root of a workspace has been located, probes for all members /// of a workspace. /// /...
  * `set_resolve_behavior` **(Defensive Guards)** (Impact: 32.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 337`, `structural_boundaries: 399`, `args: 210`, `func_start: 106`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 4`, `state_mutation: 62`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 72`, `import: 51`
* *Defense:* `safety: 60`, `doc: 198`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.434
  * `Choke Point (Betweenness):` 0.013129 | `Ripple Effect (Closeness):` 0.118804
  * `Imports (Out-Degree: 46):` anyhow::Context, anyhow::anyhow, anyhow::bail, cargo_util::paths, cargo_util::paths::normalize_path, cargo_util_schemas::manifest, cargo_util_schemas::manifest::RustVersion, cargo_util_schemas::manifest::TomlDependency...
  * `Imported By (In-Degree: 68):` (Excluded from Brief to save tokens)

### `tests/testsuite/test.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.296)
- **Top Global Matches:** file_cluster_13: 7.296, file_cluster_2: 8.132, file_cluster_15: 8.704
- **Magnitude:** 1082.32 | **LOC:** 5656 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **34**; blast radius 0.263; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (91.2%), Guard Balance (formerly Safety Score) (57.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.2%), Concurrency Surface (formerly Concurrency) (12.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cargo_test_doctest_xcompile_runner` **(I/O & Config Routines)** (Impact: 6.1)
  * `cargo_test_env` **(Annotated & Test Methods)** (Impact: 4.0)
  * `cargo_test_doctest_xcompile_no_runner` **(I/O & Config Routines)** (Impact: 4.0)
  * `test_filtered_excludes_compiling_examples` **(I/O & Config Routines)** (Impact: 3.5)
  * `no_fail_fast` **(Annotated & Test Methods)** (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 196`, `args: 386`, `func_start: 269`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 49`, `state_mutation: 515`
* *Architecture:* `io: 5`, `api: 192`, `concurrency: 1`, `import: 16`
* *Defense:* `doc: 136`, `test: 237`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.263
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000895
  * `Imports (Out-Degree: 12):` a, b, bar, baz, c, cargo_test_support::basic_bin_manifest, cargo_test_support::basic_lib_manifest, cargo_test_support::basic_manifest...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/testsuite/registry.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.449)
- **Top Global Matches:** file_cluster_12: 7.449, file_cluster_5: 8.898, file_cluster_13: 9.18
- **Magnitude:** 1081.78 | **LOC:** 4791 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 45.5%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **32**; blast radius 0.263; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (65.2%), Guard Balance (formerly Safety Score) (58.1%), Complexity Load (formerly Cognitive Load) (8.2%)
- **Documentation Coverage:** 99.6441% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `registry_index_rejected` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `sparse_retry_multiple` **(I/O & Config Routines)** (Impact: 12.6)
  * `dl_retry_multiple` **(I/O & Config Routines)** (Impact: 12.4)
  * `chmod_readonly` **(Compute Cores)** (Impact: 7.5)
  * `inaccessible_registry_cache_still_works` **(I/O & Config Routines)** (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 460
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 335`, `args: 253`, `func_start: 175`
* *Risk/State:* `safety_bypasses: 69`, `high_risk_execution: 2`, `state_mutation: 446`
* *Architecture:* `io: 3`, `api: 119`, `import: 23`
* *Defense:* `doc: 4`, `test: 19`, `sync_locks: 24`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.263
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.000895
  * `Imports (Out-Degree: 10):` bar, cargo::core::SourceId, cargo_test_support::assert_deterministic_mtime, cargo_test_support::basic_manifest, cargo_test_support::git, cargo_test_support::paths, cargo_test_support::project, cargo_test_support::registry...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/testsuite/artifact_dep.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.71)
- **Top Global Matches:** file_cluster_12: 6.71, file_cluster_2: 7.232, file_cluster_13: 7.394
- **Magnitude:** 994.42 | **LOC:** 3593 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **24**; blast radius 0.263; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (64.7%), Guard Balance (formerly Safety Score) (60.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.4%), Complexity Load (formerly Cognitive Load) (8.9%)
- **Documentation Coverage:** 94.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assert_artifact_executable_output` **(Many-Argument Workhorses)** (Impact: 10.7)
  * `build_script_with_bin_artifacts` **(I/O & Config Routines)** (Impact: 8.7)
  * `cross_doctests_works_with_artifacts` **(I/O & Config Routines)** (Impact: 7.0)
  * `env_vars_and_build_products_for_various_build_targets` **(Annotated & Test Methods)** (Impact: 7.0)
  * `build_script_with_selected_dashed_bin_artifact_and_lib_true` **(I/O & Config Routines)** (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 189`, `args: 190`, `func_start: 107`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 6`, `state_mutation: 621`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 104`, `import: 11`
* *Defense:* `safety: 1`, `doc: 27`, `test: 58`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.263
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000895
  * `Imports (Out-Degree: 8):` a::Trait, arch, b::Trait, bar, builder, cargo_test_support::Project, cargo_test_support::basic_bin_manifest, cargo_test_support::basic_manifest...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/testsuite/git.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.526)
- **Top Global Matches:** file_cluster_12: 6.526, file_cluster_7: 7.721, file_cluster_5: 8.503
- **Magnitude:** 946.58 | **LOC:** 4490 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 21.4%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **29**; blast radius 0.263; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (74.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.6%), Guard Balance (formerly Safety Score) (61.4%), Complexity Load (formerly Cognitive Load) (10.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `git_worktree_with_original_repo_renamed` **(I/O & Config Routines)** (Impact: 20.5)
  * `failed_submodule_checkout` **(I/O & Config Routines)** (Impact: 8.4)
  * `git_with_force_push` **(I/O & Config Routines)** (Impact: 8.4)
  * `dep_with_changed_submodule` **(I/O & Config Routines)** (Impact: 7.6)
  * `metadata_master_consistency` **(I/O & Config Routines)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 525
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 331`, `args: 239`, `func_start: 86`
* *Risk/State:* `safety_bypasses: 129`, `high_risk_execution: 1`, `state_mutation: 513`
* *Architecture:* `io: 4`, `api: 110`, `concurrency: 2`, `import: 17`
* *Defense:* `safety: 1`, `doc: 1`, `test: 25`, `sync_locks: 11`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.263
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000895
  * `Imports (Out-Degree: 6):` a, bar, cargo_test_support::Project, cargo_test_support::basic_lib_manifest, cargo_test_support::basic_manifest, cargo_test_support::git, cargo_test_support::git::add_submodule, cargo_test_support::git::cargo_uses_gitoxide...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cargo/ops/cargo_add/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.121)
- **Top Global Matches:** file_cluster_6: 7.121, file_cluster_8: 13.094, file_cluster_4: 13.248
- **Magnitude:** 934.58 | **LOC:** 1377 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **44**; blast radius 0.346; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.1%)
- **Documentation Coverage:** 59.2593% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve_dependency` **(Many-Argument Workhorses)** (Impact: 207.2)
  * `add` **(Many-Argument Workhorses)** (Impact: 106.7)
    * *Intent:* /// Add dependencies to a manifest
  * `get_public_dependency` **(Many-Argument Workhorses)** (Impact: 76.8)
  * `get_latest_dependency` **(Many-Argument Workhorses)** (Impact: 54.3)
  * `print_action_msg` **(Defensive Guards)** (Impact: 40.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 273`, `structural_boundaries: 292`, `args: 94`, `func_start: 26`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 3`, `state_mutation: 63`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 23`, `import: 43`
* *Defense:* `safety: 57`, `doc: 56`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.346
  * `Choke Point (Betweenness):` 0.000294 | `Ripple Effect (Closeness):` 0.07747
  * `Imports (Out-Degree: 25):` crate_spec, anyhow::Context, cargo_util::paths, cargo_util_schemas::core::PartialVersion, cargo_util_schemas::manifest::PathBaseName, cargo_util_schemas::manifest::RustVersion, cargo_util_terminal::Shell, crate::CargoResult...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/cargo/sources/git/utils.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.769)
- **Top Global Matches:** file_cluster_6: 5.769, file_cluster_4: 10.228, file_cluster_8: 15.126
- **Magnitude:** 927.7 | **LOC:** 1786 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 41.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **37**; blast radius 0.44; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (86.4%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.4%), Guard Balance (formerly Safety Score) (50.7%)
- **Documentation Coverage:** 13.7931% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `github_fast_path` **(Many-Argument Workhorses)** (Impact: 86.7)
    * *Intent:* /// Attempts GitHub's special fast path for testing if we've already got an /// up-to-date copy of t...
  * `with_authentication` **(Many-Argument Workhorses)** (Impact: 74.7)
    * *Intent:* /// we fall back to the generic user of `git`. /// /// * If a username/password is allowed, then we ...
  * `fetch` **(Many-Argument Workhorses)** (Impact: 66.1)
    * *Intent:* /// Attempts to fetch the given git `reference` for a Git repository. /// /// This is the main entry...
  * `update_submodule` **(Many-Argument Workhorses)** (Impact: 63.4)
    * *Intent:* /// Update a single Git submodule, and recurse into its submodules.
  * `update_submodules` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* /// Like `git submodule update --recursive` but for this git checkout. /// /// This function respect...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 39 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 299`, `args: 88`, `func_start: 42`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 49`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 20`, `concurrency: 1`, `import: 24`
* *Defense:* `safety: 42`, `doc: 233`, `test: 7`, `sync_locks: 2`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.44
  * `Choke Point (Betweenness):` 0.000157 | `Ripple Effect (Closeness):` 0.066501
  * `Imports (Out-Degree: 16):` anyhow::Context, anyhow::anyhow, cargo_util::ProcessBuilder, cargo_util::paths, cargo_util_terminal::Verbosity, crate::core::GitReference, crate::core::SourceId, crate::sources::git::fetch::RemoteKind...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/testsuite/bad_config.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.597)
- **Top Global Matches:** file_cluster_4: 8.597, file_cluster_2: 9.111, file_cluster_13: 9.242
- **Magnitude:** 868.0 | **LOC:** 4189 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 61.5%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.263; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (58.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.2%), Connectivity (formerly Api Exposure) (44.5%), Complexity Load (formerly Cognitive Load) (15.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `redefined_sources` **(I/O & Config Routines)** (Impact: 76.5)
  * `duplicate_packages_in_cargo_lock` **(I/O & Config Routines)** (Impact: 3.5)
  * `unsupported_float` **(I/O & Config Routines)** (Impact: 2.5)
  * `unsupported_datetime` **(I/O & Config Routines)** (Impact: 2.5)
  * `unsupported_float_array` **(I/O & Config Routines)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 661
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 195`, `args: 60`, `func_start: 122`
* *Risk/State:* `state_mutation: 657`, `duplicate_logic: 6`
* *Architecture:* `api: 25`, `import: 32`
* *Defense:* `doc: 5`, `test: 3`, `sync_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.263
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000895
  * `Imports (Out-Degree: 3):` build, cargo_test_support::Project, cargo_test_support::basic_bin_manifest, cargo_test_support::basic_manifest, cargo_test_support::git::cargo_uses_gitoxide, cargo_test_support::project, cargo_test_support::registry, cargo_test_support::registry::Package...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cargo/core/global_cache_tracker.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.82)
- **Top Global Matches:** file_cluster_4: 6.82, file_cluster_15: 8.98, file_cluster_0: 9.233
- **Magnitude:** 826.1 | **LOC:** 1840 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **27**; blast radius 0.692; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (65.3%), Connectivity (formerly Api Exposure) (61.4%), Guard Balance (formerly Safety Score) (49.6%)
- **Documentation Coverage:** 9.6386% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `populate_untracked` **(Many-Argument Workhorses)** (Impact: 62.9)
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
* *Structure:* `branch: 243`, `structural_boundaries: 327`, `args: 89`, `func_start: 58`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 46`, `planned_debt: 4`
* *Architecture:* `io: 2`, `api: 43`, `import: 19`
* *Defense:* `safety: 27`, `doc: 348`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.692
  * `Choke Point (Betweenness):` 0.000161 | `Ripple Effect (Closeness):` 0.08212
  * `Imports (Out-Degree: 12):` anyhow::Context, anyhow::bail, cargo_util::paths, cargo_util_terminal::Verbosity, crate::CargoResult, crate::GlobalContext, crate::core::gc::GcOpts, crate::ops::CleanContext...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `crates/cargo-util-schemas/src/manifest/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.4)
- **Top Global Matches:** file_cluster_0: 7.4, file_cluster_13: 11.347, file_cluster_5: 11.934
- **Magnitude:** 783.32 | **LOC:** 1840 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **37** in-repo importer(s); it depends on **23**; blast radius 1.847; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (88.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.4%), Mutation Surface (formerly State Flux) (31.4%)
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
* *Structure:* `branch: 146`, `structural_boundaries: 284`, `args: 189`, `func_start: 129`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 22`, `duplicate_logic: 14`, `unreferenced_by_name: 34`
* *Architecture:* `api: 269`, `import: 22`
* *Defense:* `safety: 36`, `doc: 58`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.847
  * `Choke Point (Betweenness):` 0.000271 | `Ripple Effect (Closeness):` 0.099106
  * `Imports (Out-Degree: 6):` rust_version, crate::core::PackageIdSpec, crate::restricted_names, crate::restricted_names::NameValidationError, crate::schema::TomlValueWrapper, rust_version::RustVersion, rust_version::RustVersionError, serde::Deserialize...
  * `Imported By (In-Degree: 37):` (Excluded from Brief to save tokens)

### `tests/testsuite/patch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.24)
- **Top Global Matches:** file_cluster_2: 7.24, file_cluster_13: 7.469, file_cluster_12: 8.018
- **Magnitude:** 768.38 | **LOC:** 3433 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 69.6%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.263; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (81.6%), Guard Balance (formerly Safety Score) (59.6%), Connectivity (formerly Api Exposure) (54.1%), Complexity Load (formerly Cognitive Load) (15.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `patch_to_git_pull_request` **(I/O & Config Routines)** (Impact: 57.5)
  * `perform_old_git_patch` **(I/O & Config Routines)** (Impact: 7.2)
  * `patched_reexport_stays_locked` **(I/O & Config Routines)** (Impact: 3.0)
  * `patch_in_real_with_base` **(I/O & Config Routines)** (Impact: 3.0)
  * `patch_in_virtual_with_base` **(I/O & Config Routines)** (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 112`, `args: 38`, `func_start: 63`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 547`
* *Architecture:* `io: 2`, `api: 47`, `import: 17`
* *Defense:* `doc: 1`, `test: 15`, `sync_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.263
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000895
  * `Imports (Out-Degree: 6):` bar, bar::hello, baz, cargo_test_support::basic_manifest, cargo_test_support::git, cargo_test_support::paths, cargo_test_support::project, cargo_test_support::registry...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cargo/util/toml_mut/dependency.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.897)
- **Top Global Matches:** file_cluster_5: 7.897, file_cluster_12: 10.045, file_cluster_7: 10.652
- **Magnitude:** 759.5 | **LOC:** 1321 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **20**; blast radius 0.615; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.5%), Guard Balance (formerly Safety Score) (60.5%)
- **Documentation Coverage:** 37.2881% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_toml` **(Many-Argument Workhorses)** (Impact: 164.0)
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
* *Structure:* `branch: 160`, `structural_boundaries: 259`, `args: 95`, `func_start: 68`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 67`, `high_risk_execution: 1`, `state_mutation: 64`, `duplicate_logic: 2`
* *Architecture:* `api: 75`, `import: 17`
* *Defense:* `safety: 68`, `doc: 82`, `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.615
  * `Choke Point (Betweenness):` 6.4e-05 | `Ripple Effect (Closeness):` 0.067216
  * `Imports (Out-Degree: 11):` cargo_util::paths, cargo_util_schemas::manifest::PathBaseName, crate::CargoResult, crate::GlobalContext, crate::core::Features, crate::core::GitReference, crate::core::SourceId, crate::core::Summary...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `tests/testsuite/workspaces.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.69)
- **Top Global Matches:** file_cluster_13: 6.69, file_cluster_2: 7.112, file_cluster_15: 7.919
- **Magnitude:** 749.28 | **LOC:** 2932 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 0.263; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (63.7%), Guard Balance (formerly Safety Score) (57.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.2%), Complexity Load (formerly Cognitive Load) (14.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ws_err_unused` **(I/O & Config Routines)** (Impact: 4.0)
  * `dont_recurse_out_of_cargo_home` **(I/O & Config Routines)** (Impact: 3.7)
  * `lock_doesnt_change_depending_on_crate` **(I/O & Config Routines)** (Impact: 3.5)
  * `relative_rustc` **(I/O & Config Routines)** (Impact: 3.5)
  * `ws_warn_unused` **(I/O & Config Routines)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 443
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 153`, `args: 127`, `func_start: 79`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 4`, `state_mutation: 441`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 86`, `import: 11`
* *Defense:* `doc: 9`, `test: 102`, `sync_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.263
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000895
  * `Imports (Out-Degree: 7):` bar, baz, cargo_test_support::ProjectBuilder, cargo_test_support::basic_lib_manifest, cargo_test_support::basic_manifest, cargo_test_support::git, cargo_test_support::paths, cargo_test_support::project...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/testsuite/doc.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.418)
- **Top Global Matches:** file_cluster_12: 7.418, file_cluster_13: 7.637, file_cluster_2: 7.882
- **Magnitude:** 746.42 | **LOC:** 4032 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 63.6%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 0.263; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (75.0%), Guard Balance (formerly Safety Score) (53.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.9%), Complexity Load (formerly Cognitive Load) (5.0%)
- **Documentation Coverage:** 97.6331% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `doc_fingerprint_is_versioning_consistent` **(I/O & Config Routines)** (Impact: 8.5)
  * `mergeable_info_multi_targets` **(I/O & Config Routines)** (Impact: 6.0)
  * `doc_fingerprint_unusual_behavior` **(I/O & Config Routines)** (Impact: 5.0)
  * `rebuild_tracks_env_in_dep` **(I/O & Config Routines)** (Impact: 4.0)
  * `crate_versions_flag_is_overridden` **(Annotated & Test Methods)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 306
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 185`, `args: 114`, `func_start: 123`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 38`, `high_risk_execution: 2`, `state_mutation: 304`, `fragile_debt: 4`
* *Architecture:* `io: 1`, `api: 164`, `import: 17`
* *Defense:* `doc: 66`, `test: 159`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.263
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000895
  * `Imports (Out-Degree: 10):` bar.rs, fun, a, a::fun, b, bar, cargo_test_support::basic_lib_manifest, cargo_test_support::basic_manifest...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cargo/util/toml/targets.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.67)
- **Top Global Matches:** file_cluster_4: 7.67, file_cluster_0: 9.051, file_cluster_12: 9.333
- **Magnitude:** 735.74 | **LOC:** 1259 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **29**; blast radius 0.274; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.8%), Connectivity (formerly Api Exposure) (29.0%)
- **Documentation Coverage:** 89.5833% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalize_lib` **(Many-Argument Workhorses)** (Impact: 59.2)
  * `normalize_targets_with_legacy_path` **(Many-Argument Workhorses)** (Impact: 55.6)
  * `toml_targets_and_inferred` **(Many-Argument Workhorses)** (Impact: 52.2)
  * `to_targets` **(Many-Argument Workhorses)** (Impact: 50.2)
  * `normalize_bins` **(Many-Argument Workhorses)** (Impact: 48.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 36 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 243`, `args: 82`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 3`, `state_mutation: 50`
* *Architecture:* `io: 1`, `api: 7`, `import: 13`
* *Defense:* `safety: 46`, `doc: 25`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.274
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.077253
  * `Imports (Out-Degree: 11):` anyhow::Context, cargo_util::paths, cargo_util_schemas::manifest::PathValue, cargo_util_schemas::manifest::StringOrVec, cargo_util_schemas::manifest::TomlBenchTarget, cargo_util_schemas::manifest::TomlBinTarget, cargo_util_schemas::manifest::TomlExampleTarget, cargo_util_schemas::manifest::TomlLibTarget...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/cargo-test-support/src/registry.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.417)
- **Top Global Matches:** file_cluster_5: 7.417, file_cluster_12: 7.678, file_cluster_7: 9.801
- **Magnitude:** 728.6 | **LOC:** 1879 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **114** in-repo importer(s); it depends on **34**; blast radius 8.324; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (86.2%), Mutation Surface (formerly State Flux) (80.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.7%)
- **Documentation Coverage:** 22.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_authorized` **(Many-Argument Workhorses)** (Impact: 54.0)
  * `build` **(Compute Cores)** (Impact: 47.2)
    * *Intent:* /// Initializes the registry.
  * `append_manifest` **(Many-Argument Workhorses)** (Impact: 40.6)
  * `index` **(Compute Cores)** (Impact: 23.2)
    * *Intent:* /// Serve the registry index
  * `start` **(Compute Cores)** (Impact: 22.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 29 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 11
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 321`, `args: 110`, `func_start: 96`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 51`, `high_risk_execution: 3`, `state_mutation: 78`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 4`, `api: 102`, `concurrency: 6`, `import: 21`
* *Defense:* `safety: 29`, `doc: 249`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.324
  * `Choke Point (Betweenness):` 0.000204 | `Ripple Effect (Closeness):` 0.154212
  * `Imports (Out-Degree: 6):` cargo_util::Sha256, cargo_util::paths::append, crate::git::repo, crate::paths, crate::publish::create_index_line, crate::publish::write_to_index, flate2::Compression, flate2::write::GzEncoder...
  * `Imported By (In-Degree: 114):` (Excluded from Brief to save tokens)

### `src/cargo/ops/fix/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.361)
- **Top Global Matches:** file_cluster_8: 7.361, file_cluster_6: 12.294, file_cluster_4: 20.667
- **Magnitude:** 719.94 | **LOC:** 1453 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **58**; blast radius 0.445; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.6%), Debt Markers (formerly Tech Debt) (32.1%)
- **Documentation Coverage:** 63.6364% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `migrate_manifests` **(Many-Argument Workhorses)** (Impact: 71.5)
  * `rustfix_and_fix` **(Many-Argument Workhorses)** (Impact: 71.2)
    * *Intent:* /// Executes `rustc` to apply one round of suggestions to the crate in question. /// /// This will f...
  * `rustfix_crate` **(Many-Argument Workhorses)** (Impact: 62.9)
    * *Intent:* /// Attempts to apply fixes to a single crate. /// /// This runs `rustc` (possibly multiple times) t...
  * `check_resolver_change` **(Many-Argument Workhorses)** (Impact: 45.9)
  * `fix` **(Many-Argument Workhorses)** (Impact: 43.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 37 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 287`, `args: 89`, `func_start: 29`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 3`, `state_mutation: 70`, `planned_debt: 2`, `fragile_debt: 5`, `unreferenced_by_name: 4`
* *Architecture:* `io: 5`, `api: 14`, `import: 35`
* *Defense:* `safety: 36`, `doc: 110`, `test: 8`, `sync_locks: 2`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 0.000683 | `Ripple Effect (Closeness):` 0.077416
  * `Imports (Out-Degree: 28):` fix_edition, anyhow::Context, anyhow::bail, cargo_util::ProcessBuilder, cargo_util::exit_status_to_string, cargo_util::is_simple_exit_code, cargo_util::paths, cargo_util_schemas::manifest::TomlManifest...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/cargo/ops/cargo_update.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.13)
- **Top Global Matches:** file_cluster_6: 7.13, file_cluster_4: 10.762, file_cluster_8: 15.971
- **Magnitude:** 719.18 | **LOC:** 1258 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **40**; blast radius 0.473; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.3%), Connectivity (formerly Api Exposure) (53.6%), Guard Balance (formerly Safety Score) (51.0%)
- **Documentation Coverage:** 84.0909% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `upgrade_dependency` **(Many-Argument Workhorses)** (Impact: 70.5)
  * `update_lockfile` **(Many-Argument Workhorses)** (Impact: 66.0)
  * `write_manifest_upgrades` **(Many-Argument Workhorses)** (Impact: 59.6)
    * *Intent:* /// Update manifests with upgraded versions, and write to disk. Based on /// cargo-edit. Returns tru...
  * `print_lockfile_updates` **(Many-Argument Workhorses)** (Impact: 50.6)
  * `upgrade_manifests` **(Many-Argument Workhorses)** (Impact: 39.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 30 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 303`, `args: 87`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 37`, `planned_debt: 2`
* *Architecture:* `api: 22`, `import: 26`
* *Defense:* `safety: 40`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.473
  * `Choke Point (Betweenness):` 0.00018 | `Ripple Effect (Closeness):` 0.077434
  * `Imports (Out-Degree: 23):` anyhow::Context, cargo_util_schemas::core::PartialVersion, cargo_util_terminal::Verbosity, crate::core::PackageId, crate::core::PackageIdSpec, crate::core::PackageIdSpecQuery, crate::core::Registry, crate::core::Resolve...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/bin/cargo/commands/doc.rs` (RUST) | Magnitude: 15.48 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 8, core_var_decl: 4, design_snake_case: 4
- `src/cargo/sources/registry/http_remote.rs` (RUST) | Magnitude: 292.38 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 460, structural_boundaries: 113, branch: 83, doc: 57
- `src/cargo/util/local_poll_adapter.rs` (RUST) | Magnitude: 54.7 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 119, structural_boundaries: 43, test: 23, generics: 19
- `src/cargo/core/compiler/fingerprint/rustdoc.rs` (RUST) | Magnitude: 90.54 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 180, structural_boundaries: 45, doc: 43, branch: 34
- `src/cargo/core/compiler/compile_kind.rs` (RUST) | Magnitude: 88.16 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 137, doc: 65, structural_boundaries: 36, branch: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/cargo/sources/git/mod.rs` (RUST) | Magnitude: 17.96 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 30, doc: 15, structural_boundaries: 14, api: 6
- `crates/cargo-test-support/containers/sshd/Dockerfile` (DOCKERFILE) | Magnitude: 19.74 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: branch: 9, func_start: 8, indent_spaces: 7, structural_boundaries: 4
- `tests/testsuite/cargo_env_config.rs` (RUST) | Magnitude: 64.06 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 281, structural_boundaries: 30, core_var_decl: 27, args: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/testsuite/warn_on_failure.rs` (RUST) | Magnitude: 26.46 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 66, core_var_decl: 13, design_snake_case: 13, state_mutation: 10
- `tests/testsuite/cargo_add/target_cfg/mod.rs` (RUST) | Magnitude: 5.3 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 9, import: 6, core_var_decl: 3
- `tests/testsuite/cargo_info/within_ws_with_alternative_registry/mod.rs` (RUST) | Magnitude: 2.96 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 8, import: 4, core_var_decl: 4
- `tests/testsuite/lto.rs` (RUST) | Magnitude: 197.4 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 576, core_var_decl: 91, design_snake_case: 91, state_mutation: 69
- `tests/testsuite/build_script_extra_link_arg.rs` (RUST) | Magnitude: 68.22 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 305, core_var_decl: 33, design_snake_case: 33, args: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `crates/xtask-stale-label/src/main.rs` (RUST) | Magnitude: 23.04 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 28, core_var_decl: 13, design_snake_case: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/testsuite/directory.rs` (RUST) | Magnitude: 198.46 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 569, core_var_decl: 121, design_snake_case: 119, state_mutation: 103
- `src/bin/cargo/commands/mod.rs` (RUST) | Magnitude: 51.18 | Delta: **0.151** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 44, api: 42, pointers: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/testsuite/cargo_info/mod.rs` (RUST) | Magnitude: 3.0 | Delta: **0.161** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 36, indent_spaces: 3, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/testsuite/cargo_add/mod.rs` (RUST) | Magnitude: 18.3 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 165
- `tests/testsuite/cargo_remove/mod.rs` (RUST) | Magnitude: 15.76 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 38
- `tests/testsuite/cargo_help/mod.rs` (RUST) | Magnitude: 15.24 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12
- `src/cargo/core/mod.rs` (RUST) | Magnitude: 40.62 | Delta: **0.195** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 28, api: 25, import: 13, indent_spaces: 2
- `tests/testsuite/cargo_new/mod.rs` (RUST) | Magnitude: 15.34 | Delta: **0.239** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/testsuite/cargo_add/git_tag/mod.rs` (RUST) | Magnitude: 3.16 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 12, import: 6, core_var_decl: 5
- `tests/testsuite/cargo_help/nested_cmd_with_extra_flags/mod.rs` (RUST) | Magnitude: 1.8 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 2, import: 2, args: 1
- `tests/testsuite/cargo_info/specify_empty_version_with_url/mod.rs` (RUST) | Magnitude: 2.44 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 4, import: 3, args: 1
- `tests/testsuite/cargo_info/specify_version_with_url_but_registry_is_not_matched/mod.rs` (RUST) | Magnitude: 2.44 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 4, import: 3, args: 1
- `tests/testsuite/cargo_add/overwrite_path_base_with_version/mod.rs` (RUST) | Magnitude: 2.6 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, import: 6, core_var_decl: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `crates/resolver-tests/src/sat.rs` (RUST) | Magnitude: 224.84 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 416, structural_boundaries: 99, branch: 64, generics: 53
- `tests/testsuite/utils/tools.rs` (RUST) | Magnitude: 31.62 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 42, core_var_decl: 18, design_snake_case: 18
- `crates/cargo-platform/examples/matches.rs` (RUST) | Magnitude: 12.88 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 14, core_var_decl: 8, design_snake_case: 8
- `src/bin/cargo/commands/config.rs` (RUST) | Magnitude: 15.14 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 5, branch: 4, generics: 4
- `crates/cargo-util/src/process_builder.rs` (RUST) | Magnitude: 365.16 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 487, structural_boundaries: 194, doc: 108, branch: 94

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/testsuite/config_include.rs` (RUST) | Magnitude: 137.46 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 383, core_var_decl: 90, design_snake_case: 89, state_mutation: 69
- `tests/testsuite/cargo_report_timings/mod.rs` (RUST) | Magnitude: 45.98 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 259, structural_boundaries: 34, core_var_decl: 29, design_snake_case: 26
- `tests/testsuite/cache_lock.rs` (RUST) | Magnitude: 92.34 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 172, core_var_decl: 53, design_snake_case: 53, structural_boundaries: 46
- `tests/testsuite/global_cache_tracker.rs` (RUST) | Magnitude: 375.78 | Delta: **0.145** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1443, core_var_decl: 277, design_snake_case: 277, structural_boundaries: 245

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/cargo/util/context/mod.rs` -> Churn: **72.84%** | Cog Load: 13.7635% | Debt: 59.3482%
- `src/cargo/core/resolver/errors.rs` -> Churn: **72.71%** | Cog Load: 35.7627% | Debt: 50.7911%
- `src/cargo/util/mod.rs` -> Churn: **54.63%** | Cog Load: 5.5347% | Debt: 70.4909%
- `src/cargo/sources/registry/mod.rs` -> Churn: **51.12%** | Cog Load: 13.1845% | Debt: 52.507%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/testsuite/test.rs` -> **Ed Page** (100.0% isolated ownership) | Magnitude: 1082.32
- `src/cargo/core/global_cache_tracker.rs` -> **Ed Page** (100.0% isolated ownership) | Magnitude: 826.1
- `tests/testsuite/fix.rs` -> **Ed Page** (100.0% isolated ownership) | Magnitude: 658.6
- `tests/testsuite/inheritable_workspace_fields.rs` -> **Ed Page** (100.0% isolated ownership) | Magnitude: 574.26
- `tests/testsuite/freshness_checksum.rs` -> **Weihang Lo** (100.0% isolated ownership) | Magnitude: 568.38

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `crates/cargo-test-support/src/lib.rs` -> **Severity: 1.885** (Bridge: 0.0352 * Flux: 53.5496%)
- `src/cargo/ops/tree/graph.rs` -> **Severity: 1.266** (Bridge: 0.0326 * Flux: 38.8559%)
- `src/cargo/core/workspace.rs` -> **Severity: 0.88** (Bridge: 0.0131 * Flux: 67.0494%)
- `src/cargo/core/compiler/build_context/target_info.rs` -> **Severity: 0.532** (Bridge: 0.0056 * Flux: 94.7173%)
- `src/cargo/core/compiler/mod.rs` -> **Severity: 0.402** (Bridge: 0.0045 * Flux: 89.0651%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/cargo-test-support/src/lib.rs` -> **Severity: 14.617** (Embedded: 0.268 * Error Risk: 54.5377%)
- `crates/cargo-test-support/src/containers.rs` -> **Severity: 11.152** (Embedded: 0.1394 * Error Risk: 80.0%)
- `crates/cargo-test-support/src/compare.rs` -> **Severity: 10.383** (Embedded: 0.1848 * Error Risk: 56.1786%)
- `crates/cargo-test-macro/src/lib.rs` -> **Severity: 9.821** (Embedded: 0.1395 * Error Risk: 70.3956%)
- `crates/cargo-test-support/src/publish.rs` -> **Severity: 9.532** (Embedded: 0.1406 * Error Risk: 67.8151%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/testsuite/mock-std/library/std/src/lib.rs` -> **Severity: 15075.1** (Blast Radius: 150.751 * Doc Risk: 100.0%)
- `crates/cargo-test-support/src/lib.rs` -> **Severity: 3925.234** (Blast Radius: 102.25 * Doc Risk: 38.3886%)
- `crates/cargo-test-support/src/compare.rs` -> **Severity: 960.268** (Blast Radius: 15.277 * Doc Risk: 62.8571%)
- `crates/cargo-test-support/src/paths.rs` -> **Severity: 671.939** (Blast Radius: 15.589 * Doc Risk: 43.1034%)
- `src/cargo/util/errors.rs` -> **Severity: 570.724** (Blast Radius: 6.706 * Doc Risk: 85.1064%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 961 literal sites + 24 sites through wrappers = 985
- **`panics_and_aborts`:** 459 literal sites + 2 sites through wrappers = 461

- `emit` (function, debug_prints, primitive): 22 call sites in 1 files -- `crates/build-rs/src/output.rs`
- `expand` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `src/cargo/util/toml/embedded.rs`
- `bar` (function, debug_prints, primitive): 1 call sites in 1 files -- `tests/testsuite/build_scripts_multiple.rs`
- `f` (function, debug_prints, primitive): 1 call sites in 1 files -- `tests/testsuite/features2.rs`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 74864 call pairs -- scoped 19.8%, unique 0.0%, ambiguous 11.8%, external 68.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 74779 | 19.8% | 0.0% | 11.8% | 68.4% |
| shell | 34 | 17.6% | 0.0% | 0.0% | 82.4% |
| javascript | 33 | 3.0% | 0.0% | 0.0% | 97.0% |
| python | 18 | 16.7% | 0.0% | 5.6% | 77.8% |

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
