# ARCHITECTURAL_BRIEF: redox
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/redox-os/redox.git` |
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
- **Scope:** 110 analyzed artifact(s), 12358 LOC.
- **Load-bearing artifact:** `src/recipe.rs` -- 9 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/bin/repo.rs` -- pulls in 87 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/bin/repo.rs` at magnitude 1130.44 (structural weight, not risk).
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
| Total Artifacts | 3191 |
| Analyzed Artifacts (Scanned) | 110 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3081 |
| Total LOC | 12358 |
| Volatility Index | 0.027 |
| % Scanned of codebase = | 3.4% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2997 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1469 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 10.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9381 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| SHELL | 33 | 2536 | 30.0% |
| PLAINTEXT | 22 | 0 | 20.0% |
| RUST | 20 | 6541 | 18.2% |
| MAKEFILE | 11 | 1446 | 10.0% |
| MARKDOWN | 7 | 0 | 6.4% |
| C | 5 | 1207 | 4.5% |
| PYTHON | 3 | 147 | 2.7% |
| YAML | 1 | 39 | 0.9% |
| NIX | 1 | 176 | 0.9% |
| CPP | 1 | 5 | 0.9% |
| GO | 1 | 5 | 0.9% |
| JAVA | 1 | 5 | 0.9% |
| JAVASCRIPT | 1 | 1 | 0.9% |
| LUA | 1 | 1 | 0.9% |
| ZIG | 1 | 4 | 0.9% |
| CSS | 1 | 245 | 0.9% |

## 4.1 SOURCE ENCODINGS
All 110 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 39%, Declarative / Non-Code 22%, Large Core Modules 14%, Large Core Modules (3) 11%, Large Core Modules (2) 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 81 | 73.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 29 | 26.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3081*

**Composition by Extension & Reason:**
- `.toml`: 2611x Excluded (Unsupported Extension: '.toml'), 303x Unsupported Format (.toml), 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 109x Excluded (Unsupported Extension: '.patch'), 8x Unsupported Format (.patch), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 9x Unsupported Format (.undeterminable), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sha`: 4x Excluded (Unsupported Extension: '.sha')
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.lock`: 2x Excluded (Unsupported Extension: '.lock')
- `.ttf`: 1x Excluded (Explicitly Denied Extension: '.ttf')
- `.wav`: 1x Excluded (Explicitly Denied Extension: '.wav')
- `.ion`: 1x Excluded (Unsupported Extension: '.ion')
- `.bashrc`: 1x Excluded (Unsupported Extension: '.bashrc')
- `.site`: 1x Excluded (Unsupported Extension: '.site')
- `.ipxe`: 1x Excluded (Unsupported Extension: '.ipxe')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 23.3 | 14.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 89.5 | 47.0 | 55.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 11.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.8 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 73.3 | 15.1 | 0.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 51.1 | 1.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 53.1 | 67.2 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 1.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.1 | 0.4 | 0.1 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 19.2 | 6.2 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 56.1 | 85.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 40 | 11 | 0 | `recipes/demos/osdemo/osdemo.c` |
| cleanup | 82 | 15 | 1 | `mk/prefix.mk` |
| guards | 323 | 37 | 8 | `src/bin/repo.rs` |
| danger | 573 | 54 | 13 | `native_bootstrap.sh` |
| concurrency | 32 | 9 | 0 | `src/bin/repo.rs` |
| connectivity | 374 | 43 | 9 | `src/recipe.rs` |
| io | 534 | 47 | 10 | `mk/prefix.mk` |
| crypto | 0 | 0 | 0 | - |
| ipc | 75 | 16 | 2 | `native_bootstrap.sh` |
| time | 7 | 4 | 0 | `mk/disk.mk` |
| serialization | 26 | 9 | 0 | `mk/prefix.mk` |
| regex | 32 | 11 | 0 | `native_bootstrap.sh` |
| events | 15 | 8 | 0 | `mk/config.mk` |
| tests | 65 | 11 | 0 | `native_bootstrap.sh` |
| docs | 138 | 18 | 1 | `src/recipe.rs` |
| debt | 686 | 56 | 9 | `native_bootstrap.sh` |
| mutation | 2427 | 66 | 75 | `src/bin/repo.rs` |
| dead_code | 47 | 24 | 1 | `Makefile` |
| credential | 6 | 2 | 0 | `mk/prefix.mk` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 157 | 8 | 0 | `recipes/demos/gears/gears.c` |
| ui | 21 | 4 | 0 | `src/web/style.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `mk/prefix.mk` (Hits: 110)
- `native_bootstrap.sh` (Hits: 75)
- `podman_bootstrap.sh` (Hits: 57)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **recipe.rs** (`src/recipe.rs`) — 9 inbound connections
2. **lib.rs** (`src/lib.rs`) — 8 inbound connections
3. **config.rs** (`src/config.rs`) — 6 inbound connections
4. **package.rs** (`src/cook/package.rs`) — 6 inbound connections
5. **pty.rs** (`src/cook/pty.rs`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **repo.rs** (`src/bin/repo.rs`) — 87 outbound dependencies
2. **fetch.rs** (`src/cook/fetch.rs`) — 29 outbound dependencies
3. **cook_build.rs** (`src/cook/cook_build.rs`) — 26 outbound dependencies
4. **repo_builder.rs** (`src/bin/repo_builder.rs`) — 24 outbound dependencies
5. **fs.rs** (`src/cook/fs.rs`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `run_tui_cook` **(Many-Argument Workhorses)** (@ `src/bin/repo.rs`) -> Impact: **225.5** | LOC: 491
- `build` **(Many-Argument Workhorses)** (@ `src/cook/cook_build.rs`) -> Impact: **225.3** | LOC: 326
- `fetch` **(Many-Argument Workhorses)** (@ `src/cook/fetch.rs`) -> Impact: **184.5** | LOC: 290
- `parse_args` **(Compute Cores)** (@ `src/bin/repo.rs`) -> Impact: **167.9** | LOC: 275
- `auto_deps_from_dynamic_linking` **(Many-Argument Workhorses)** (@ `src/cook/cook_build.rs`) -> Impact: **108.5** | LOC: 130
- `publish_packages` **(Compute Cores)** (@ `src/bin/repo_builder.rs`) -> Impact: **97.8** | LOC: 231
  * *Intent:* // TODO: Make this callable from repo bin
- `walk_tree_entry` **(Many-Argument Workhorses)** (@ `src/cook/tree.rs`) -> Impact: **70.7** | LOC: 86
- `main` **(Many-Argument Workhorses)** (@ `recipes/demos/sdl2-gears/gears.c`) -> Impact: **68.9** | LOC: 200
- `fetch_remote` **(Many-Argument Workhorses)** (@ `src/cook/fetch.rs`) -> Impact: **66.1** | LOC: 97
- `package` **(Many-Argument Workhorses)** (@ `src/cook/package.rs`) -> Impact: **65.6** | LOC: 105

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/cook` | 9 | 2096.24 | 23.58% | 10.52% |
| `src/bin` | 3 | 1273.76 | 36.82% | 26.96% |
| `__monolith__` | 10 | 870.68 | 14.0% | 11.75% |
| `src` | 6 | 682.64 | 13.39% | 27.23% |
| `mk` | 10 | 588.96 | 23.77% | 3.98% |
| `recipes/demos/osdemo` | 1 | 392.34 | 62.15% | 9.35% |
| `bin` | 7 | 291.32 | 26.72% | 0.0% |
| `recipes/demos/sdl2-gears` | 1 | 251.86 | 70.61% | 9.47% |
| `recipes/demos/gears` | 1 | 149.72 | 78.42% | 0.0% |
| `recipes/wip/dev/lang/perl5` | 1 | 124.5 | 15.91% | 21.31% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `recipes/wip/vice/recipe.sh` -> **100.0%** Exposure
- `Makefile` -> **99.956%** Exposure
- `recipes/wip/demos/rust-cairo/recipe.sh` -> **85.8453%** Exposure
- `src/lib.rs` -> **79.1704%** Exposure
- `scripts/include-recipes.sh` -> **62.2459%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `mk/qemu.mk` -> **100.0%** Exposure
- `bin/aarch64-unknown-redox-llvm-config` -> **100.0%** Exposure
- `bin/x86_64-unknown-redox-llvm-config` -> **100.0%** Exposure
- `scripts/changelog.sh` -> **100.0%** Exposure
- `scripts/executables.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Makefile` -> **9** Orphaned Functions | **0** Duplicates
- `recipes/wip/vice/recipe.sh` -> **4** Orphaned Functions | **0** Duplicates
- `src/lib.rs` -> **3** Orphaned Functions | **0** Duplicates
- `recipes/wip/demos/rust-cairo/recipe.sh` -> **2** Orphaned Functions | **0** Duplicates
- `src/bin/repo.rs` -> **2** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `11` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `376` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/bin/repo.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.795)
- **Top Global Matches:** file_cluster_4: 6.795, file_cluster_6: 9.843, file_cluster_0: 12.987
- **Magnitude:** 1130.44 | **LOC:** 1951 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 93.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **87**; blast radius 6.917; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (95.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.5%)
- **Documentation Coverage:** 97.9167% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_tui_cook` **(Many-Argument Workhorses)** (Impact: 225.5)
  * `parse_args` **(Compute Cores)** (Impact: 167.9)
  * `repo_inner` **(Many-Argument Workhorses)** (Impact: 41.9)
  * `handle_cook` **(Many-Argument Workhorses)** (Impact: 31.0)
  * `main_inner` **(I/O & Config Routines)** (Impact: 29.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 85 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 389`, `structural_boundaries: 392`, `args: 100`, `func_start: 40`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 12`, `state_mutation: 121`, `planned_debt: 5`, `fragile_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 8`, `concurrency: 14`, `import: 38`
* *Defense:* `safety: 59`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` ansi_to_tui::IntoText, anyhow::Context, anyhow::anyhow, anyhow::bail, cookbook::config::CookConfig, cookbook::config::get_config, cookbook::config::init_config, cookbook::cook::cook_build::build...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cook/cook_build.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.47)
- **Top Global Matches:** file_cluster_8: 7.47, file_cluster_6: 17.542, file_cluster_3: 20.244
- **Magnitude:** 613.58 | **LOC:** 760 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **26**; blast radius 11.798; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (86.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.6%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build` **(Many-Argument Workhorses)** (Impact: 225.3)
  * `auto_deps_from_dynamic_linking` **(Many-Argument Workhorses)** (Impact: 108.5)
  * `build_remote` **(Many-Argument Workhorses)** (Impact: 50.0)
  * `build_deps_dir` **(Many-Argument Workhorses)** (Impact: 47.4)
  * `build_auto_deps` **(Many-Argument Workhorses)** (Impact: 30.1)
    * *Intent:* /// Calculate automatic dependencies
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 29 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 166`, `args: 40`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 3`, `state_mutation: 33`, `planned_debt: 7`
* *Architecture:* `io: 3`, `api: 14`, `import: 14`
* *Defense:* `safety: 15`, `doc: 1`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.798
  * `Choke Point (Betweenness):` 0.000268 | `Ripple Effect (Closeness):` 0.052844
  * `Imports (Out-Degree: 8):` crate::config::CookConfig, crate::cook::fetch, crate::cook::fs::*, crate::cook::package::package_source_paths, crate::cook::package::package_target, crate::cook::pty::PtyOut, crate::cook::script::*, crate::is_redox...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/cook/fetch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.497)
- **Top Global Matches:** file_cluster_6: 5.497, file_cluster_4: 11.107, file_cluster_8: 14.054
- **Magnitude:** 448.76 | **LOC:** 748 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **29**; blast radius 12.603; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.7%), Guard Balance (formerly Safety Score) (50.9%), Connectivity (formerly Api Exposure) (35.0%)
- **Documentation Coverage:** 96.875% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetch` **(Many-Argument Workhorses)** (Impact: 184.5)
  * `fetch_remote` **(Many-Argument Workhorses)** (Impact: 66.1)
  * `fetch_offline` **(Many-Argument Workhorses)** (Impact: 40.2)
  * `fetch_apply_patches` **(Many-Argument Workhorses)** (Impact: 19.0)
  * `fetch_extract_tar` **(Stateful Encapsulated Methods)** (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 10 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 164`, `args: 31`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 13`, `state_mutation: 7`, `planned_debt: 6`
* *Architecture:* `io: 7`, `api: 19`, `import: 28`
* *Defense:* `safety: 20`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.603
  * `Choke Point (Betweenness):` 0.001018 | `Ripple Effect (Closeness):` 0.055046
  * `Imports (Out-Degree: 9):` crate::Error, crate::Result, crate::bail_other_err, crate::config::translate_mirror, crate::cook::cook_build, crate::cook::fetch_repo, crate::cook::fetch_repo::PlainPtyCallback, crate::cook::fs::*...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `native_bootstrap.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.723)
- **Top Global Matches:** file_cluster_12: 8.723, file_cluster_7: 8.878, file_cluster_5: 10.759
- **Magnitude:** 422.34 | **LOC:** 1193 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 57.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 6.917; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.8%)
- **Documentation Coverage:** 26.087% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ubuntu` **(Many-Argument Workhorses)** (Impact: 36.2)
    * *Intent:* ############################################################################### # This function take...
  * `fedora` **(Many-Argument Workhorses)** (Impact: 27.3)
    * *Intent:* ############################################################################### # This function take...
  * `suse` **(Compute Cores)** (Impact: 25.8)
    * *Intent:* ############################################################################### # This function take...
  * `gentoo` **(Compute Cores)** (Impact: 22.0)
    * *Intent:* ############################################################################### # This function take...
  * `rustInstall` **(Compute Cores)** (Impact: 21.2)
    * *Intent:* ############################################################################# # This function takes ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 342`, `args: 55`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 58`, `high_risk_execution: 26`, `state_mutation: 38`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 75`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 1`, `doc: 11`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` env
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `recipes/demos/osdemo/osdemo.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.381)
- **Top Global Matches:** file_cluster_4: 7.381, file_cluster_6: 10.654, file_cluster_12: 12.07
- **Magnitude:** 392.34 | **LOC:** 548 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 6.917; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.5%), Complexity Load (formerly Cognitive Load) (62.2%)
- **Documentation Coverage:** 91.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test` **(Many-Argument Workhorses)** (Impact: 62.1)
  * `display_image` **(Many-Argument Workhorses)** (Impact: 24.3)
  * `write_ppm` **(Many-Argument Workhorses)** (Impact: 22.3)
  * `main` **(Compute Cores)** (Impact: 13.2)
  * `init_context` **(I/O & Config Routines)** (Impact: 11.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 12 instances
* *Amplified Cascading Flux:* 74 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 227
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 23`, `args: 64`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 79`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 8`
* *Defense:* `safety: 6`, `doc: 1`, `immutability_locks: 21`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` glu.h, osmesa.h, assert.h, math.h, orbital.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/recipe.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.104)
- **Top Global Matches:** file_cluster_0: 8.104, file_cluster_12: 9.007, file_cluster_5: 9.106
- **Magnitude:** 331.12 | **LOC:** 717 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **18**; blast radius 47.723; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.6%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.7%), Connectivity (formerly Api Exposure) (69.1%)
- **Documentation Coverage:** 96.0784% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new_recursive` **(Many-Argument Workhorses)** (Impact: 59.0)
  * `guess_version` **(Defensive Guards)** (Impact: 19.7)
  * `new` **(Many-Argument Workhorses)** (Impact: 17.8)
  * `from_path` **(Compute Cores)** (Impact: 12.7)
  * `extract_cargo_ver` **(Defensive Guards)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 105`, `args: 43`, `func_start: 27`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 38`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 53`, `import: 9`
* *Defense:* `safety: 12`, `doc: 39`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 47.723
  * `Choke Point (Betweenness):` 0.003223 | `Ripple Effect (Closeness):` 0.088073
  * `Imports (Out-Degree: 3):` crate::WALK_DEPTH, crate::cook::package, crate::recipe::BuildKind, crate::recipe::BuildRecipe, crate::recipe::PackageRecipe, crate::recipe::Recipe, crate::recipe::SourceRecipe, crate::staged_pkg...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/cook/fs.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.792)
- **Top Global Matches:** file_cluster_0: 7.792, file_cluster_4: 9.334, file_cluster_15: 10.113
- **Magnitude:** 326.94 | **LOC:** 451 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **21**; blast radius 12.288; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (80.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (59.1%), Guard Balance (formerly Safety Score) (53.5%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_git_remote_tracking` **(Compute Cores)** (Impact: 42.6)
    * *Intent:* /// (local_branch_name, remote_branch, remote_name, remote_url) /// -> ("fix_stuff", "master", "orig...
  * `move_dir_all_inner_fn` **(Generic / Templated Code)** (Impact: 29.4)
  * `check_files_present` **(Compute Cores)** (Impact: 20.2)
  * `copy_dir_all` **(Generic / Templated Code)** (Impact: 18.0)
  * `run_command_stdin` **(Many-Argument Workhorses)** (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 105`, `args: 37`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 12`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 26`, `import: 4`
* *Defense:* `safety: 9`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.288
  * `Choke Point (Betweenness):` 8.2e-05 | `Ripple Effect (Closeness):` 0.057439
  * `Imports (Out-Degree: 3):` crate::Error, crate::Result, crate::bail_other_err, crate::config::translate_mirror, crate::cook::pty::PtyOut, crate::cook::pty::spawn_to_pipe, crate::wrap_io_err, crate::wrap_other_err...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `podman_bootstrap.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.907)
- **Top Global Matches:** file_cluster_7: 8.907, file_cluster_12: 9.479, file_cluster_5: 11.015
- **Magnitude:** 283.2 | **LOC:** 664 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 6.917; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (20.6%)
- **Documentation Coverage:** 21.0526% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `suse` **(Compute Cores)** (Impact: 24.2)
    * *Intent:* ############################################################################### # This function take...
  * `gentoo` **(Compute Cores)** (Impact: 20.5)
    * *Intent:* ############################################################################### # This function take...
  * `rustInstall` **(Compute Cores)** (Impact: 19.6)
    * *Intent:* ############################################################################# # This function takes ...
  * `ubuntu` **(Compute Cores)** (Impact: 19.1)
    * *Intent:* ############################################################################### # This function take...
  * `fedora` **(Compute Cores)** (Impact: 18.8)
    * *Intent:* ############################################################################### # This function take...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 275`, `args: 47`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 20`, `state_mutation: 23`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 57`, `import: 1`
* *Defense:* `safety: 1`, `doc: 11`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` env
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `recipes/demos/sdl2-gears/gears.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.863)
- **Top Global Matches:** file_cluster_4: 7.863, file_cluster_6: 8.098, file_cluster_16: 14.129
- **Magnitude:** 251.86 | **LOC:** 524 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 6.917; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.6%), Guard Balance (formerly Safety Score) (64.1%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 68.9)
  * `gear` **(Many-Argument Workhorses)** (Impact: 23.1)
    * *Intent:* **/
  * `cleanup` **(I/O & Config Routines)** (Impact: 7.8)
  * `CheckSDLError` **(Compute Cores)** (Impact: 4.9)
  * `draw` **(I/O & Config Routines)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 27`, `args: 71`, `func_start: 8`
* *Risk/State:* `state_mutation: 52`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `doc: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SDL.h, SDL_image.h, SDL_mixer.h, SDL_opengl.h, SDL_ttf.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mk/qemu.mk` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.917)
- **Top Global Matches:** file_cluster_12: 6.917, file_cluster_7: 7.678, file_cluster_5: 9.869
- **Magnitude:** 193.18 | **LOC:** 379 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 7.505; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.5%), Guard Balance (formerly Safety Score) (76.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `qemu-deps` **(I/O & Config Routines)** (Impact: 4.2)
  * `qemu-deps` **(I/O & Config Routines)** (Impact: 2.1)
  * `qemu-deps` **(I/O & Config Routines)** (Impact: 2.1)
  * `qemu-deps` **(I/O & Config Routines)** (Impact: 2.0)
  * `qemu-deps` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 116`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 57`, `dead_code: 4`
* *Architecture:* `io: 24`, `api: 1`
* *Defense:* `safety: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.505
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009174
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cook/package.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.017)
- **Top Global Matches:** file_cluster_6: 8.017, file_cluster_8: 10.528, file_cluster_4: 15.432
- **Magnitude:** 184.58 | **LOC:** 311 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **21**; blast radius 25.568; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.5%), Mutation Surface (formerly State Flux) (67.3%), Guard Balance (formerly Safety Score) (52.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `package` **(Many-Argument Workhorses)** (Impact: 65.6)
  * `package_toml` **(Many-Argument Workhorses)** (Impact: 46.8)
  * `package_handle_push` **(Many-Argument Workhorses)** (Impact: 17.9)
  * `package_target` **(Generic / Templated Code)** (Impact: 4.6)
  * `package_stage_paths` **(Defensive Guards)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 53`, `args: 22`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 7`, `planned_debt: 6`
* *Architecture:* `io: 1`, `api: 9`, `import: 6`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.568
  * `Choke Point (Betweenness):` 0.002194 | `Ripple Effect (Closeness):` 0.066055
  * `Imports (Out-Degree: 7):` crate::Error, crate::config::CookConfig, crate::cook::cook_build::BuildResult, crate::cook::fetch, crate::cook::fs::*, crate::cook::pty::PtyOut, crate::log_to_pty, crate::recipe::BuildKind...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/cook/tree.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.771)
- **Top Global Matches:** file_cluster_6: 6.771, file_cluster_8: 11.987, file_cluster_4: 13.555
- **Magnitude:** 157.38 | **LOC:** 197 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 11.719; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `walk_tree_entry` **(Many-Argument Workhorses)** (Impact: 70.7)
  * `walk_file_tree` **(Many-Argument Workhorses)** (Impact: 30.0)
  * `display_pkg_fn` **(Many-Argument Workhorses)** (Impact: 9.8)
  * `display_tree_entry` **(Many-Argument Workhorses)** (Impact: 4.1)
  * `format_size` **(Type Conversions)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 47`, `args: 8`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 6`, `import: 5`
* *Defense:* `safety: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.719
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.047182
  * `Imports (Out-Degree: 1):` anyhow::Context, crate::recipe::CookRecipe, pkg::Package, pkg::PackageName, std::collections::HashMap, std::collections::HashSet, std::fmt::Write, std::fs::read_to_string...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/cook/script.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.295)
- **Top Global Matches:** file_cluster_2: 4.295, file_cluster_17: 5.469, file_cluster_15: 6.467
- **Magnitude:** 152.2 | **LOC:** 418 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 92.9%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 9.889; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.6%), Guard Balance (formerly Safety Score) (65.9%), Complexity Load (formerly Cognitive Load) (53.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 6`, `args: 1`
* *Risk/State:* `state_mutation: 57`, `planned_debt: 4`
* *Architecture:* `api: 5`
* *Defense:* `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.889
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.050015
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `recipes/demos/gears/gears.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.253)
- **Top Global Matches:** file_cluster_16: 6.253, file_cluster_15: 8.581, file_cluster_2: 8.725
- **Magnitude:** 149.72 | **LOC:** 345 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 6.917; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (78.4%), Guard Balance (formerly Safety Score) (70.8%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `gear` **(Many-Argument Workhorses)** (Impact: 22.8)
    * *Intent:* **/
  * `draw` **(I/O & Config Routines)** (Impact: 3.9)
  * `sync` **(Stateful Encapsulated Methods)** (Impact: 2.8)
  * `init` **(Encapsulated Accessors)** (Impact: 2.5)
  * `reshape` **(Stateful Encapsulated Methods)** (Impact: 2.4)
    * *Intent:* /* new window size or exposure */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 31 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 19`, `args: 60`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 47`
* *Architecture:* `import: 7`
* *Defense:* `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` gl.h, glu.h, osmesa.h, math.h, orbital.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mk/repo.mk` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.294)
- **Top Global Matches:** file_cluster_12: 8.294, file_cluster_7: 9.498, file_cluster_4: 10.112
- **Magnitude:** 147.64 | **LOC:** 261 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 90.9%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 7.505; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.8%), Guard Balance (formerly Safety Score) (54.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `debug.%` **(Compute Cores)** (Impact: 21.2)
    * *Intent:* # Debug a statically linked program with gdbgui, for example: debug.drivers-initfs DEBUG_BIN=pcid # ...
  * `p.%` **(I/O & Config Routines)** (Impact: 9.9)
    * *Intent:* # Push compiled package into existing image # DO NOT RUN THIS WHILE QEMU ALIVE, THE DISK MIGHT CORRU...
  * `push` **(I/O & Config Routines)** (Impact: 9.9)
    * *Intent:* # Push all recipes specified by the filesystem config
  * `fetch` **(I/O & Config Routines)** (Impact: 5.4)
    * *Intent:* # Fetch all recipes source or binary from filesystem config
  * `f.%` **(I/O & Config Routines)** (Impact: 5.4)
    * *Intent:* # Invoke fetch for one or more targets separated by comma
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 27`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 6`
* *Architecture:* `io: 1`, `api: 35`
* *Defense:* `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.505
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009174
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/config.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.456)
- **Top Global Matches:** file_cluster_5: 7.456, file_cluster_7: 8.208, file_cluster_12: 9.152
- **Magnitude:** 130.3 | **LOC:** 255 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **8**; blast radius 20.957; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Guard Balance (formerly Safety Score) (75.2%), Connectivity (formerly Api Exposure) (72.4%), Concurrency Surface (formerly Concurrency) (51.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init_config` **(I/O & Config Routines)** (Impact: 18.1)
  * `translate_mirror` **(Defensive Guards)** (Impact: 11.5)
  * `extract_env` **(Defensive Guards)** (Impact: 5.5)
  * `from` **(State Mutators)** (Impact: 2.1)
  * `setup_test_config` **(Interface Declarations)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 25`, `args: 16`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 14`
* *Architecture:* `api: 33`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 8`, `doc: 13`, `test: 15`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 20.957
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.067411
  * `Imports (Out-Degree: 0):` self::*, serde::Deserialize, serde::Serialize, std::collections::HashMap, std::env, std::fs, std::str::FromStr, std::sync::OnceLock
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/bin/repo_builder.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.945)
- **Top Global Matches:** file_cluster_8: 9.945, file_cluster_6: 11.121, file_cluster_4: 18.585
- **Magnitude:** 127.2 | **LOC:** 291 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 6.917; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.8%), Guard Balance (formerly Safety Score) (51.5%), Mutation Surface (formerly State Flux) (48.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `publish_packages` **(Compute Cores)** (Impact: 97.8)
    * *Intent:* // TODO: Make this callable from repo bin
  * `is_newer` **(State Mutators)** (Impact: 5.7)
  * `main` **(Interface Declarations)** (Impact: 3.2)
  * `parse_args` **(Generic / Templated Code)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 70`, `args: 16`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 6`, `planned_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `import: 14`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` cookbook::WALK_DEPTH, cookbook::cook::fetch, cookbook::cook::ident::get_ident, cookbook::cook::ident::init_ident, cookbook::cook::package, cookbook::recipe::CookRecipe, cookbook::staged_pkg, cookbook::web::CliWebConfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `recipes/wip/dev/lang/perl5/configure_tool.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.784)
- **Top Global Matches:** file_cluster_7: 7.784, file_cluster_14: 8.738, file_cluster_12: 9.745
- **Magnitude:** 124.5 | **LOC:** 352 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (46.6%), Debt Markers (formerly Tech Debt) (21.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `whichprog` **(Compute Cores)** (Impact: 25.1)
    * *Intent:* # whichprog symbol VAR prog1 prog2
  * `tryfromenv` **(Compute Cores)** (Impact: 9.4)
  * `tryprog` **(Defensive Guards)** (Impact: 5.7)
    * *Intent:* # Toolchain detection
  * `detect_cc_version` **(I/O & Config Routines)** (Impact: 4.3)
    * *Intent:* # This is only a function for easy access to return-s # try.out contains `$cc --version` output. # #...
  * `setfromenv` **(State Mutators)** (Impact: 3.7)
    * *Intent:* # setfromvar what SHELLVAR
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 94`, `args: 23`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 5`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `io: 47`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/aarch64-unknown-redox-llvm-config` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.39)
- **Top Global Matches:** file_cluster_3: 8.39, file_cluster_8: 21.604, file_cluster_6: 34.26
- **Magnitude:** 123.16 | **LOC:** 104 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 6.917; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Complexity Load (formerly Cognitive Load) (79.7%), Dead Code Surface (formerly Dead Code) (10.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 21.0)
  * `is_unwanted_arch` **(Compute Cores)** (Impact: 18.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 9`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 30`, `dead_code: 1`
* *Architecture:* `io: 10`, `api: 2`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, subprocess, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/x86_64-unknown-redox-llvm-config` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.39)
- **Top Global Matches:** file_cluster_3: 8.39, file_cluster_8: 21.604, file_cluster_6: 34.26
- **Magnitude:** 123.16 | **LOC:** 104 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 6.917; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Complexity Load (formerly Cognitive Load) (79.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 21.0)
  * `is_unwanted_arch` **(Compute Cores)** (Impact: 18.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 9`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 30`, `dead_code: 1`
* *Architecture:* `io: 10`, `api: 2`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.917
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, subprocess, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cook/pty.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.056)
- **Top Global Matches:** file_cluster_12: 7.056, file_cluster_5: 7.503, file_cluster_0: 8.199
- **Magnitude:** 101.6 | **LOC:** 344 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **20**; blast radius 15.351; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (57.4%), Guard Balance (formerly Safety Score) (52.1%), Concurrency Surface (formerly Concurrency) (35.5%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `spawn_command` **(Compute Cores)** (Impact: 14.4)
  * `openpty` **(Compute Cores)** (Impact: 7.8)
  * `read` **(Compute Cores)** (Impact: 5.8)
  * `spawn_to_pipe` **(Defensive Guards)** (Impact: 5.5)
  * `cloexec` **(Compute Cores)** (Impact: 4.8)
    * *Intent:* /// Helper function to set the close-on-exec flag for a raw descriptor
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 83`, `args: 19`, `func_start: 18`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 7`, `api: 18`, `concurrency: 5`, `import: 13`
* *Defense:* `safety: 1`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.351
  * `Choke Point (Betweenness):` 6e-05 | `Ripple Effect (Closeness):` 0.06291
  * `Imports (Out-Degree: 1):` crate::Error, crate::Result, crate::wrap_io_err, libc, libc::winsize, std::fs::File, std::io, std::io::PipeReader...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/cook/fetch_repo.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.09)
- **Top Global Matches:** file_cluster_12: 7.09, file_cluster_5: 7.154, file_cluster_7: 8.528
- **Magnitude:** 101.0 | **LOC:** 205 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 9.51; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.6%), Connectivity (formerly Api Exposure) (54.8%)
- **Documentation Coverage:** 88.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load_cached_repo` **(Compute Cores)** (Impact: 10.6)
  * `download_increment` **(Type Conversions)** (Impact: 6.5)
  * `fetch_end` **(Compute Cores)** (Impact: 4.6)
  * `download_start` **(Parameter Forwarders)** (Impact: 4.5)
  * `format_size` **(Type Conversions)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 45`, `args: 19`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 14`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 12`, `import: 2`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.51
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.046984
  * `Imports (Out-Degree: 0):` pkg::PackageName, pkg::RemotePackage, pkg::RepoManager, pkg::Repository, pkg::callback::Callback, pkg::callback::SilentCallback, pkg::net_backend::CurlBackend, pkg::net_backend::DownloadBackend...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/web/html.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.483)
- **Top Global Matches:** file_cluster_12: 7.483, file_cluster_9: 7.678, file_cluster_15: 8.404
- **Magnitude:** 92.72 | **LOC:** 330 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 16.968; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.6%), Mutation Surface (formerly State Flux) (46.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_html_pkg` **(Many-Argument Workhorses)** (Impact: 33.7)
  * `get_tree_url` **(Many-Argument Workhorses)** (Impact: 21.3)
  * `generate_html_index` **(Many-Argument Workhorses)** (Impact: 8.1)
  * `get_hostname` **(Defensive Guards)** (Impact: 2.0)
  * `get_short_commit` **(Defensive Guards)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 45`, `args: 13`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 13`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.968
  * `Choke Point (Betweenness):` 0.000212 | `Ripple Effect (Closeness):` 0.038856
  * `Imports (Out-Degree: 4):` crate::cook::ident, crate::cook::tree::format_size, crate::recipe::CookRecipe, crate::recipe::SourceRecipe, crate::web::get_category, pkg::Package, std::collections::BTreeMap, std::fs...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/staged_pkg.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.376)
- **Top Global Matches:** file_cluster_12: 8.376, file_cluster_0: 8.697, file_cluster_5: 8.728
- **Magnitude:** 92.26 | **LOC:** 161 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **11**; blast radius 33.269; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.2%), Connectivity (formerly Api Exposure) (43.6%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new_recursive_nonstop` **(Many-Argument Workhorses)** (Impact: 29.0)
    * *Intent:* /// List ordered success packages and map of failed packages. /// A package can be both success and ...
  * `new_recursive` **(Compute Cores)** (Impact: 16.9)
  * `from_path` **(Defensive Guards)** (Impact: 7.8)
  * `new` **(Defensive Guards)** (Impact: 4.4)
  * `list` **(Generic / Templated Code)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 34`, `args: 13`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 8`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 6`, `import: 6`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 33.269
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.070475
  * `Imports (Out-Degree: 0):` pkg::Package, pkg::PackageError, pkg::PackageName, std::borrow::Cow, std::collections::BTreeMap, std::collections::BTreeSet, std::collections::HashMap, std::ffi::OsStr...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `mk/prefix.mk` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.208)
- **Top Global Matches:** file_cluster_8: 9.208, file_cluster_6: 18.302, file_cluster_3: 21.029
- **Magnitude:** 84.62 | **LOC:** 411 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 7.505; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (56.7%), Debt Markers (formerly Tech Debt) (12.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `static_clean` **(I/O & Config Routines)** (Impact: 56.5)
    * *Intent:* # Remove relibc in sysroot and all statically linked recipes
  * `prefix` **(State Mutators)** (Impact: 1.1)
  * `prefix_clean` **(I/O & Config Routines)** (Impact: 1.1)
    * *Intent:* # Remove prefix builds and downloads
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 48`, `func_start: 3`
* *Risk/State:* `planned_debt: 4`
* *Architecture:* `io: 110`, `api: 19`
* *Defense:* `cleanup: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.505
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009174
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/cook/fetch_repo.rs` (RUST) | Magnitude: 101.0 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 150, structural_boundaries: 45, core_var_decl: 24, args: 19
- `native_bootstrap.sh` (SHELL) | Magnitude: 422.34 | Delta: **0.155** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 859, structural_boundaries: 342, debug_prints: 187, branch: 137

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/cook.rs` (RUST) | Magnitude: 23.68 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `recipes/shells/bash/etc/skel/.profile` (SHELL) | Magnitude: 13.72 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 19, globals: 10, indent_spaces: 5, branch: 4

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/bin/repo.rs` -> Churn: **95.05%** | Cog Load: 55.2113% | Debt: 14.9823%
- `src/cook/script.rs` -> Churn: **68.6%** | Cog Load: 53.8811% | Debt: 12.516%
- `mk/qemu.mk` -> Churn: **61.33%** | Cog Load: 94.5175% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/bin/repo.rs` -> **Wildan M** (93.8% isolated ownership) | Magnitude: 1130.44
- `src/cook/cook_build.rs` -> **Wildan M** (100.0% isolated ownership) | Magnitude: 613.58
- `src/cook/fetch.rs` -> **Wildan M** (100.0% isolated ownership) | Magnitude: 448.76
- `src/recipe.rs` -> **Wildan M** (100.0% isolated ownership) | Magnitude: 331.12
- `src/cook/fs.rs` -> **Wildan M** (100.0% isolated ownership) | Magnitude: 326.94

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/recipe.rs` -> **Severity: 0.298** (Bridge: 0.0032 * Flux: 92.5884%)
- `src/cook/package.rs` -> **Severity: 0.148** (Bridge: 0.0022 * Flux: 67.3196%)
- `src/web.rs` -> **Severity: 0.098** (Bridge: 0.001 * Flux: 96.1987%)
- `src/cook/cook_build.rs` -> **Severity: 0.026** (Bridge: 0.0003 * Flux: 95.439%)
- `src/cook/fetch.rs` -> **Severity: 0.021** (Bridge: 0.001 * Flux: 20.3175%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/config.rs` -> **Severity: 5.072** (Embedded: 0.0674 * Error Risk: 75.2381%)
- `src/recipe.rs` -> **Severity: 4.78** (Embedded: 0.0881 * Error Risk: 54.273%)
- `src/lib.rs` -> **Severity: 4.128** (Embedded: 0.0826 * Error Risk: 50.0%)
- `src/staged_pkg.rs` -> **Severity: 3.959** (Embedded: 0.0705 * Error Risk: 56.1709%)
- `src/cook/ident.rs` -> **Severity: 3.618** (Embedded: 0.0517 * Error Risk: 70.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/recipe.rs` -> **Severity: 4585.149** (Blast Radius: 47.723 * Doc Risk: 96.0784%)
- `src/lib.rs` -> **Severity: 4282.893** (Blast Radius: 50.616 * Doc Risk: 84.6154%)
- `src/staged_pkg.rs` -> **Severity: 2772.416** (Blast Radius: 33.269 * Doc Risk: 83.3333%)
- `src/cook/package.rs` -> **Severity: 2556.8** (Blast Radius: 25.568 * Doc Risk: 100.0%)
- `src/config.rs` -> **Severity: 2095.7** (Blast Radius: 20.957 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2411 call pairs -- scoped 14.6%, unique 0.0%, ambiguous 0.0%, external 85.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 1812 | 14.3% | 0.0% | 0.1% | 85.7% |
| shell | 353 | 19.3% | 0.0% | 0.0% | 80.7% |
| c | 215 | 10.2% | 0.0% | 0.0% | 89.8% |
| python | 27 | 14.8% | 0.0% | 0.0% | 85.2% |
| go | 1 | 0.0% | 0.0% | 0.0% | 100.0% |
| java | 1 | 0.0% | 0.0% | 0.0% | 100.0% |
| lua | 1 | 0.0% | 0.0% | 0.0% | 100.0% |
| zig | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
