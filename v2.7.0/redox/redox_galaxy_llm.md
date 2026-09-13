# ARCHITECTURAL_BRIEF: redox
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/redox-os/redox.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 3191 |
| Analyzed Artifacts (Scanned) | 104 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3087 |
| Total LOC | 12319 |
| Volatility Index | 0.029 |
| % Scanned of codebase = | 3.3% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5521 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.7006 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8182 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| SHELL | 33 | 2536 | 31.7% |
| PLAINTEXT | 20 | 0 | 19.2% |
| RUST | 20 | 6541 | 19.2% |
| MAKEFILE | 11 | 1446 | 10.6% |
| C | 5 | 1207 | 4.8% |
| MARKDOWN | 4 | 0 | 3.8% |
| PYTHON | 3 | 147 | 2.9% |
| NIX | 1 | 176 | 1.0% |
| CPP | 1 | 5 | 1.0% |
| GO | 1 | 5 | 1.0% |
| JAVA | 1 | 5 | 1.0% |
| JAVASCRIPT | 1 | 1 | 1.0% |
| LUA | 1 | 1 | 1.0% |
| ZIG | 1 | 4 | 1.0% |
| CSS | 1 | 245 | 1.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 80 | 76.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 24 | 23.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3087*

**Composition by Extension & Reason:**
- `.toml`: 2618x Excluded (Unsupported Extension: '.toml'), 304x Unsupported Format (.toml), 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 111x Excluded (Unsupported Extension: '.patch'), 8x Unsupported Format (.patch)
- `no_extension`: 10x Unsupported Format (.undeterminable), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sha`: 4x Excluded (Unsupported Extension: '.sha')
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 279 LOC)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.lock`: 2x Excluded (Unsupported Extension: '.lock')
- `.cmake`: 2x Excluded (Unsupported Extension: '.cmake')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 1x Excluded (Explicitly Denied Extension: '.ttf')
- `.wav`: 1x Excluded (Explicitly Denied Extension: '.wav')
- `.ion`: 1x Excluded (Unsupported Extension: '.ion')
- `.bashrc`: 1x Excluded (Unsupported Extension: '.bashrc')
- `.site`: 1x Excluded (Unsupported Extension: '.site')
- `.ipxe`: 1x Excluded (Unsupported Extension: '.ipxe')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 23.4 | 13.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 57.8 | 68.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 15.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 20.0 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 74.0 | 13.0 | 3.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 51.1 | 1.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 52.6 | 58.6 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 64.6 | 2.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 61.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.1 | 0.4 | 0.1 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 19.2 | 3.1 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 56.1 | 85.4 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 270 | 24 | 10 | `src/bin/repo.rs` |
| cleanup | 82 | 15 | 1 | `mk/prefix.mk` |
| guards | 324 | 38 | 9 | `src/bin/repo.rs` |
| danger | 572 | 53 | 14 | `native_bootstrap.sh` |
| concurrency | 32 | 9 | 0 | `src/bin/repo.rs` |
| connectivity | 372 | 45 | 9 | `src/recipe.rs` |
| io | 533 | 46 | 10 | `mk/prefix.mk` |
| crypto | 0 | 0 | 0 | - |
| ipc | 75 | 16 | 3 | `native_bootstrap.sh` |
| time | 7 | 4 | 0 | `mk/disk.mk` |
| serialization | 26 | 9 | 0 | `mk/prefix.mk` |
| regex | 32 | 11 | 1 | `native_bootstrap.sh` |
| events | 15 | 8 | 0 | `mk/config.mk` |
| tests | 64 | 10 | 0 | `native_bootstrap.sh` |
| docs | 138 | 18 | 2 | `src/recipe.rs` |
| debt | 686 | 56 | 14 | `native_bootstrap.sh` |
| mutation | 2418 | 65 | 80 | `src/bin/repo.rs` |
| dead_code | 74 | 29 | 2 | `src/cook/fetch_repo.rs` |
| credential | 6 | 2 | 0 | `mk/prefix.mk` |
| threat | 33 | 14 | 1 | `mk/config.mk` |
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

1. **fs.rs** (`src/cook/fs.rs`) — 5 inbound connections
2. **staged_pkg.rs** (`src/staged_pkg.rs`) — 4 inbound connections
3. **fetch.rs** (`src/cook/fetch.rs`) — 2 inbound connections
4. **ci.mk** (`mk/ci.mk`) — 1 inbound connections
5. **config.mk** (`mk/config.mk`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **repo.rs** (`src/bin/repo.rs`) — 87 outbound dependencies
2. **fetch.rs** (`src/cook/fetch.rs`) — 29 outbound dependencies
3. **cook_build.rs** (`src/cook/cook_build.rs`) — 26 outbound dependencies
4. **repo_builder.rs** (`src/bin/repo_builder.rs`) — 24 outbound dependencies
5. **fs.rs** (`src/cook/fs.rs`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `run_tui_cook` (@ `src/bin/repo.rs`) -> Impact: **225.5** | LOC: 491
- `build` (@ `src/cook/cook_build.rs`) -> Impact: **225.3** | LOC: 326
- `fetch` (@ `src/cook/fetch.rs`) -> Impact: **186.5** | LOC: 290
- `parse_args` (@ `src/bin/repo.rs`) -> Impact: **167.9** | LOC: 275
- `auto_deps_from_dynamic_linking` (@ `src/cook/cook_build.rs`) -> Impact: **108.5** | LOC: 130
- `publish_packages` (@ `src/bin/repo_builder.rs`) -> Impact: **97.8** | LOC: 231
  * *Intent:* // TODO: Make this callable from repo bin
- `walk_tree_entry` (@ `src/cook/tree.rs`) -> Impact: **70.7** | LOC: 86
- `main` (@ `recipes/demos/sdl2-gears/gears.c`) -> Impact: **68.9** | LOC: 200
- `fetch_remote` (@ `src/cook/fetch.rs`) -> Impact: **66.1** | LOC: 97
- `package` (@ `src/cook/package.rs`) -> Impact: **65.6** | LOC: 105

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/cook` | 9 | 2118.14 | 23.72% | 38.62% |
| `src/bin` | 3 | 1280.76 | 37.25% | 26.96% |
| `__monolith__` | 8 | 846.52 | 14.69% | 14.94% |
| `src` | 6 | 684.04 | 13.41% | 33.73% |
| `mk` | 10 | 588.96 | 23.77% | 6.49% |
| `recipes/demos/osdemo` | 1 | 395.34 | 62.56% | 10.37% |
| `bin` | 7 | 291.32 | 26.72% | 0.0% |
| `recipes/demos/sdl2-gears` | 1 | 251.86 | 70.61% | 10.56% |
| `recipes/demos/gears` | 1 | 149.72 | 78.42% | 0.0% |
| `recipes/wip/dev/lang/perl5` | 1 | 124.5 | 15.91% | 26.52% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Makefile` -> **99.9812%** Exposure
- `src/cook/fetch_repo.rs` -> **99.8848%** Exposure
- `src/web.rs` -> **99.1687%** Exposure
- `scripts/include-recipes.sh` -> **88.0797%** Exposure
- `src/cook/ident.rs` -> **81.7574%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `mk/qemu.mk` -> **100.0%** Exposure
- `bin/aarch64-unknown-redox-llvm-config` -> **100.0%** Exposure
- `bin/x86_64-unknown-redox-llvm-config` -> **100.0%** Exposure
- `scripts/changelog.sh` -> **100.0%** Exposure
- `scripts/executables.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/cook/fetch_repo.rs` -> **10** Orphaned Functions | **0** Duplicates
- `Makefile` -> **9** Orphaned Functions | **0** Duplicates
- `src/cook/pty.rs` -> **4** Orphaned Functions | **0** Duplicates
- `src/lib.rs` -> **3** Orphaned Functions | **0** Duplicates
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
- **Unknown Dependencies:** `377` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/bin/repo.rs` (RUST) -> Cumulative Risk: **648.23**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1137.44 | **LOC:** 1951 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 93.8%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.6471%), Documentation (97.9167%), Churn (95.05%)
- **Heaviest Functions:** `run_tui_cook` (Impact: 225.5), `parse_args` (Impact: 167.9), `repo_inner` (Impact: 41.9)

### 2. `src/recipe.rs` (RUST) -> Cumulative Risk: **595.22**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 331.12 | **LOC:** 717 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (96.0784%), State Flux (92.5884%), Verification (80.0%)
- **Heaviest Functions:** `new_recursive` (Impact: 59.0), `guess_version` (Impact: 19.7), `new` (Impact: 17.8)

### 3. `src/cook/fetch_repo.rs` (RUST) -> Cumulative Risk: **588.57**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 94.0 | **LOC:** 205 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.8848%), State Flux (99.1645%), Documentation (85.0%)
- **Heaviest Functions:** `load_cached_repo` (Impact: 10.6), `download_increment` (Impact: 6.5), `fetch_end` (Impact: 4.6)

### 4. `src/cook/cook_build.rs` (RUST) -> Cumulative Risk: **583.74**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 614.58 | **LOC:** 760 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (95.439%), Documentation (95.0%), Churn (86.4%)
- **Heaviest Functions:** `build` (Impact: 225.3), `auto_deps_from_dynamic_linking` (Impact: 108.5), `build_remote` (Impact: 50.0)

### 5. `mk/qemu.mk` (MAKEFILE) -> Cumulative Risk: **580.42**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 193.18 | **LOC:** 379 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 55.6%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.3219%)
- **Heaviest Functions:** `qemu-deps` (Impact: 4.2), `qemu-deps` (Impact: 2.1), `qemu-deps` (Impact: 2.1)

### 6. `src/cook/tree.rs` (RUST) -> Cumulative Risk: **578.72**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 157.38 | **LOC:** 197 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.7649%), Verification (80.0%)
- **Heaviest Functions:** `walk_tree_entry` (Impact: 70.7), `walk_file_tree` (Impact: 30.0), `display_pkg_fn` (Impact: 9.8)

### 7. `src/cook/package.rs` (RUST) -> Cumulative Risk: **566.63**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 184.58 | **LOC:** 311 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Verification (80.0%), Churn (67.55%)
- **Heaviest Functions:** `package` (Impact: 65.6), `package_toml` (Impact: 46.8), `package_handle_push` (Impact: 17.9)

### 8. `src/cook/fs.rs` (RUST) -> Cumulative Risk: **561.1**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 339.04 | **LOC:** 451 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (85.7143%), State Flux (80.528%), Verification (80.0%)
- **Heaviest Functions:** `get_git_remote_tracking` (Impact: 44.0), `move_dir_all_inner_fn` (Impact: 29.4), `check_files_present` (Impact: 20.2)

### 9. `src/config.rs` (RUST) -> Cumulative Risk: **560.87**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 130.3 | **LOC:** 255 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.4082%), Safety Score (83.9419%)
- **Heaviest Functions:** `init_config` (Impact: 18.1), `translate_mirror` (Impact: 11.5), `extract_env` (Impact: 5.5)

### 10. `src/staged_pkg.rs` (RUST) -> Cumulative Risk: **553.41**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 92.26 | **LOC:** 161 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (97.8791%), Documentation (83.3333%), Verification (80.0%)
- **Heaviest Functions:** `new_recursive_nonstop` (Impact: 29.0), `new_recursive` (Impact: 16.9), `from_path` (Impact: 7.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/bin/repo.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1137.44 | **LOC:** 1951 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 93.8%
- **Risk Profile:** Cognitive Load (56.5234%), Tech Debt (14.9823%)
**Top Internal Functions/Classes:**
  * `run_tui_cook` (Impact: 225.5)
  * `parse_args` (Impact: 167.9)
  * `repo_inner` (Impact: 41.9)
  * `handle_cook` (Impact: 31.0)
  * `main_inner` (Impact: 30.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 88 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 297
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 394`, `structural_boundaries: 392`, `args: 100`, `func_start: 40`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 12`, `state_mutation: 121`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 8`, `concurrency: 14`, `import: 38`
* *Defense:* `safety: 59`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` AtomicU32, Borders, Clear, Direction, HashMap, HashSet, Instant, Key...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cook/cook_build.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 614.58 | **LOC:** 760 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.4344%), Tech Debt (18.3767%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 225.3)
  * `auto_deps_from_dynamic_linking` (Impact: 108.5)
  * `build_remote` (Impact: 50.0)
  * `build_deps_dir` (Impact: 47.4)
  * `build_auto_deps` (Impact: 30.1)
    * *Intent:* /// Calculate automatic dependencies
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 29 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 166`, `args: 40`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 3`, `state_mutation: 33`, `planned_debt: 7`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 13`, `import: 14`
* *Defense:* `safety: 15`, `doc: 1`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CookRecipe, OptionalPackageRecipe, PackageName, PathBuf, crate::config::CookConfig, crate::cook::fetch, crate::cook::package::package_source_paths, crate::cook::pty::PtyOut...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cook/fetch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 459.56 | **LOC:** 748 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (14.8364%), Tech Debt (11.4653%)
**Top Internal Functions/Classes:**
  * `fetch` (Impact: 186.5)
  * `fetch_remote` (Impact: 66.1)
  * `fetch_offline` (Impact: 40.2)
  * `fetch_apply_patches` (Impact: 19.0)
  * `fetch_extract_tar` (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 10 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 164`, `args: 31`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 13`, `state_mutation: 7`, `planned_debt: 6`
* *Architecture:* `io: 7`, `api: 19`, `import: 28`
* *Defense:* `safety: 20`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021845
  * `Imports (Out-Degree: 0):` PathBuf, crate::Error, crate::Result, crate::bail_other_err, crate::config::translate_mirror, crate::cook::cook_build, crate::cook::fetch_repo, crate::cook::fetch_repo::PlainPtyCallback...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `native_bootstrap.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 422.34 | **LOC:** 1193 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (16.4304%), Tech Debt (8.9714%)
**Top Internal Functions/Classes:**
  * `ubuntu` (Impact: 36.2)
    * *Intent:* ############################################################################### # This function take...
  * `fedora` (Impact: 27.3)
    * *Intent:* ############################################################################### # This function take...
  * `suse` (Impact: 25.8)
    * *Intent:* ############################################################################### # This function take...
  * `gentoo` (Impact: 22.0)
    * *Intent:* ############################################################################### # This function take...
  * `rustInstall` (Impact: 21.2)
    * *Intent:* ############################################################################# # This function takes ...
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 11 instances
* *Amplified Cascading Flux:* 37 instances
* *Sec Tainted Injection (weighted view):* 11
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 342`, `args: 55`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 58`, `high_risk_execution: 26`, `state_mutation: 38`, `dead_code: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 75`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 1`, `doc: 11`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` env
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `recipes/demos/osdemo/osdemo.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 395.34 | **LOC:** 548 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.5646%), Tech Debt (10.3702%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 62.1)
  * `display_image` (Impact: 24.3)
  * `write_ppm` (Impact: 22.3)
  * `main` (Impact: 13.2)
  * `init_context` (Impact: 11.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 12 instances
* *Amplified Cascading Flux:* 74 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 227
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 23`, `args: 64`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 79`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 8`
* *Defense:* `safety: 6`, `doc: 1`, `immutability_locks: 21`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` glu.h, osmesa.h, assert.h, math.h, orbital.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cook/fs.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 339.04 | **LOC:** 451 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.7824%), Tech Debt (9.6673%)
**Top Internal Functions/Classes:**
  * `get_git_remote_tracking` (Impact: 44.0)
    * *Intent:* /// (local_branch_name, remote_branch, remote_name, remote_url) /// -> ("fix_stuff", "master", "orig...
  * `move_dir_all_inner_fn` (Impact: 29.4)
  * `check_files_present` (Impact: 20.2)
  * `copy_dir_all` (Impact: 18.0)
  * `get_git_fetch_rev` (Impact: 17.1)
    * *Intent:* /// get commit rev after fetch
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 105`, `args: 37`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 12`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 26`, `import: 4`
* *Defense:* `safety: 9`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 33.591
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.048544
  * `Imports (Out-Degree: 0):` Command, PathBuf, Result, Stdio, WalkDir, Write, bail_other_err, config::translate_mirror...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/recipe.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 331.12 | **LOC:** 717 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.5231%), Tech Debt (9.5314%)
**Top Internal Functions/Classes:**
  * `new_recursive` (Impact: 59.0)
  * `guess_version` (Impact: 19.7)
  * `new` (Impact: 17.8)
  * `from_path` (Impact: 12.7)
  * `extract_cargo_ver` (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 105`, `args: 43`, `func_start: 27`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 38`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 53`, `import: 9`
* *Defense:* `safety: 12`, `doc: 39`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` BuildRecipe, PackageName, PackageRecipe, PathBuf, Recipe, Serialize, SourceRecipe, convert::TryInto...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `podman_bootstrap.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 283.2 | **LOC:** 664 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.6048%), Tech Debt (10.5702%)
**Top Internal Functions/Classes:**
  * `suse` (Impact: 24.2)
    * *Intent:* ############################################################################### # This function take...
  * `gentoo` (Impact: 20.5)
    * *Intent:* ############################################################################### # This function take...
  * `rustInstall` (Impact: 19.6)
    * *Intent:* ############################################################################# # This function takes ...
  * `ubuntu` (Impact: 19.1)
    * *Intent:* ############################################################################### # This function take...
  * `fedora` (Impact: 18.8)
    * *Intent:* ############################################################################### # This function take...
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 10 instances
* *Amplified Cascading Flux:* 22 instances
* *Sec Tainted Injection (weighted view):* 10
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 275`, `args: 47`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 20`, `state_mutation: 23`, `dead_code: 7`, `unreferenced_by_name: 1`
* *Architecture:* `io: 57`, `import: 1`
* *Defense:* `safety: 1`, `doc: 11`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` env
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `recipes/demos/sdl2-gears/gears.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 251.86 | **LOC:** 524 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.6118%), Tech Debt (10.5571%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 68.9)
  * `gear` (Impact: 23.1)
    * *Intent:* **/
  * `cleanup` (Impact: 7.8)
  * `CheckSDLError` (Impact: 4.9)
  * `draw` (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 27`, `args: 71`, `func_start: 8`
* *Risk/State:* `state_mutation: 52`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `doc: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SDL.h, SDL_image.h, SDL_mixer.h, SDL_opengl.h, SDL_ttf.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mk/qemu.mk` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 193.18 | **LOC:** 379 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 55.6%
- **Risk Profile:** Cognitive Load (94.5175%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `qemu-deps` (Impact: 4.2)
  * `qemu-deps` (Impact: 2.1)
  * `qemu-deps` (Impact: 2.1)
  * `qemu-deps` (Impact: 2.0)
  * `qemu-deps` (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 116`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 57`, `dead_code: 4`
* *Architecture:* `io: 24`, `api: 1`
* *Defense:* `safety: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009709
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cook/package.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 184.58 | **LOC:** 311 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.4342%), Tech Debt (20.0246%)
**Top Internal Functions/Classes:**
  * `package` (Impact: 65.6)
  * `package_toml` (Impact: 46.8)
  * `package_handle_push` (Impact: 17.9)
  * `package_target` (Impact: 4.6)
  * `package_stage_paths` (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 53`, `args: 22`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 7`, `planned_debt: 6`
* *Architecture:* `io: 1`, `api: 9`, `import: 6`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.722
  * `Choke Point (Betweenness):` 9.5e-05 | `Ripple Effect (Closeness):` 0.009709
  * `Imports (Out-Degree: 1):` CookRecipe, OptionalPackageRecipe, Package, PackageName, PackagePrefix, PackageState, PathBuf, config::CookConfig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cook/script.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 158.2 | **LOC:** 418 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 92.9%
- **Risk Profile:** Cognitive Load (59.0653%), Tech Debt (12.516%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 6`, `args: 1`
* *Risk/State:* `state_mutation: 57`, `planned_debt: 4`
* *Architecture:* `api: 5`
* *Defense:* `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cook/tree.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 157.38 | **LOC:** 197 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.6454%), Tech Debt (41.4637%)
**Top Internal Functions/Classes:**
  * `walk_tree_entry` (Impact: 70.7)
  * `walk_file_tree` (Impact: 30.0)
  * `display_pkg_fn` (Impact: 9.8)
  * `display_tree_entry` (Impact: 4.1)
  * `format_size` (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 47`, `args: 8`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 6`, `import: 5`
* *Defense:* `safety: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HashSet, PackageName, anyhow::Context, crate::recipe::CookRecipe, fs::read_to_string, path::PathBuf, pkg::Package, std::
    collections::HashMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `recipes/demos/gears/gears.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 149.72 | **LOC:** 345 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.4156%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `gear` (Impact: 22.8)
    * *Intent:* **/
  * `draw` (Impact: 3.9)
  * `sync` (Impact: 2.8)
  * `init` (Impact: 2.5)
  * `reshape` (Impact: 2.4)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` gl.h, glu.h, osmesa.h, math.h, orbital.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mk/repo.mk` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 147.64 | **LOC:** 261 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 90.9%
- **Risk Profile:** Cognitive Load (22.485%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `debug.%` (Impact: 21.2)
    * *Intent:* # Debug a statically linked program with gdbgui, for example: debug.drivers-initfs DEBUG_BIN=pcid # ...
  * `p.%` (Impact: 9.9)
    * *Intent:* # Push compiled package into existing image # DO NOT RUN THIS WHILE QEMU ALIVE, THE DISK MIGHT CORRU...
  * `push` (Impact: 9.9)
    * *Intent:* # Push all recipes specified by the filesystem config
  * `fetch` (Impact: 5.4)
    * *Intent:* # Fetch all recipes source or binary from filesystem config
  * `f.%` (Impact: 5.4)
    * *Intent:* # Invoke fetch for one or more targets separated by comma
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 27`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 6`
* *Architecture:* `io: 1`, `api: 35`
* *Defense:* `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009709
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/config.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 130.3 | **LOC:** 255 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.7377%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init_config` (Impact: 18.1)
  * `translate_mirror` (Impact: 11.5)
  * `extract_env` (Impact: 5.5)
  * `from` (Impact: 2.1)
  * `setup_test_config` (Impact: 1.6)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Serialize, env, fs, serde::Deserialize, std::collections::HashMap, str::FromStr, super::*, sync::OnceLock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bin/repo_builder.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 127.2 | **LOC:** 291 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.3411%), Tech Debt (28.1406%)
**Top Internal Functions/Classes:**
  * `publish_packages` (Impact: 97.8)
    * *Intent:* // TODO: Make this callable from repo bin
  * `is_newer` (Impact: 5.7)
  * `main` (Impact: 3.2)
  * `parse_args` (Impact: 1.7)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` BTreeSet, File, HashMap, PathBuf, SourceIdentifier, Write, cookbook::WALK_DEPTH, cookbook::cook::fetch...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `recipes/wip/dev/lang/perl5/configure_tool.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 124.5 | **LOC:** 352 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.9093%), Tech Debt (26.5208%)
**Top Internal Functions/Classes:**
  * `whichprog` (Impact: 25.1)
    * *Intent:* # whichprog symbol VAR prog1 prog2
  * `__global_context__` (Impact: 9.5)
  * `tryfromenv` (Impact: 9.4)
  * `Anonymous_Block` (Impact: 7.1)
  * `Anonymous_Block` (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 94`, `args: 23`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 5`, `dead_code: 2`, `fragile_debt: 2`
* *Architecture:* `io: 47`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/aarch64-unknown-redox-llvm-config` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 123.16 | **LOC:** 104 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (79.7358%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 21.0)
  * `is_unwanted_arch` (Impact: 18.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Rce:* 4 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 4
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 9`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 30`, `dead_code: 1`
* *Architecture:* `io: 10`, `api: 2`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, subprocess, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/x86_64-unknown-redox-llvm-config` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 123.16 | **LOC:** 104 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (79.7358%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 21.0)
  * `is_unwanted_arch` (Impact: 18.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Rce:* 4 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 4
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 9`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 30`, `dead_code: 1`
* *Architecture:* `io: 10`, `api: 2`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, subprocess, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cook/pty.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 100.6 | **LOC:** 344 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (5.0809%), Tech Debt (52.402%)
**Top Internal Functions/Classes:**
  * `spawn_command` (Impact: 14.4)
  * `openpty` (Impact: 7.8)
  * `read` (Impact: 5.8)
  * `spawn_to_pipe` (Impact: 5.5)
  * `cloexec` (Impact: 4.8)
    * *Intent:* /// Helper function to set the close-on-exec flag for a raw descriptor
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 83`, `args: 19`, `func_start: 18`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1`, `planned_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 7`, `api: 17`, `concurrency: 5`, `import: 13`
* *Defense:* `safety: 1`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PipeWriter, Result, Write, crate::Error, libc::self, mem, process::Command, ptr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/web/html.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 97.02 | **LOC:** 330 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.1481%), Tech Debt (13.7579%)
**Top Internal Functions/Classes:**
  * `generate_html_pkg` (Impact: 33.7)
  * `get_tree_url` (Impact: 23.6)
  * `generate_html_index` (Impact: 10.1)
  * `get_hostname` (Impact: 2.0)
  * `get_short_commit` (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 45`, `args: 13`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 13`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::cook::ident, crate::cook::tree::format_size, crate::recipe::SourceRecipe, crate::web::get_category, path::Path, pkg::Package, recipe::CookRecipe, std::collections::BTreeMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cook/fetch_repo.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 94.0 | **LOC:** 205 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.1951%), Tech Debt (99.8848%)
**Top Internal Functions/Classes:**
  * `load_cached_repo` (Impact: 10.6)
  * `download_increment` (Impact: 6.5)
  * `fetch_end` (Impact: 4.6)
  * `download_start` (Impact: 4.5)
  * `format_size` (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 45`, `args: 19`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 14`, `planned_debt: 1`, `unreferenced_by_name: 10`
* *Architecture:* `io: 4`, `api: 5`, `import: 2`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DownloadBackend, PathBuf, RemotePackage, RepoManager, Repository, SilentCallback, Write, callback::Callback...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/staged_pkg.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 92.26 | **LOC:** 161 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (29.2862%), Tech Debt (14.4877%)
**Top Internal Functions/Classes:**
  * `new_recursive_nonstop` (Impact: 29.0)
    * *Intent:* /// List ordered success packages and map of failed packages. /// A package can be both success and ...
  * `new_recursive` (Impact: 16.9)
  * `from_path` (Impact: 7.8)
  * `new` (Impact: 4.4)
  * `list` (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 34`, `args: 13`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 8`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 6`, `import: 6`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.208
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.038835
  * `Imports (Out-Degree: 0):` BTreeSet, HashMap, PackageError, PackageName, PathBuf, pkg::Package, std::borrow::Cow, std::collections::BTreeMap...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `mk/prefix.mk` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 84.62 | **LOC:** 411 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (10.1635%), Tech Debt (15.3787%)
**Top Internal Functions/Classes:**
  * `static_clean` (Impact: 56.5)
    * *Intent:* # Remove relibc in sysroot and all statically linked recipes
  * `prefix` (Impact: 1.1)
  * `prefix_clean` (Impact: 1.1)
    * *Intent:* # Remove prefix builds and downloads
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 48`, `func_start: 3`
* *Risk/State:* `planned_debt: 4`
* *Architecture:* `io: 110`, `api: 19`
* *Defense:* `cleanup: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009709
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/bin/repo.rs` -> Churn: **95.05%** | Cog Load: 56.5234% | Debt: 14.9823%
- `src/cook/script.rs` -> Churn: **68.6%** | Cog Load: 59.0653% | Debt: 12.516%
- `mk/qemu.mk` -> Churn: **61.33%** | Cog Load: 94.5175% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/bin/repo.rs` -> **Wildan M** (93.8% isolated ownership) | Magnitude: 1137.44
- `src/cook/cook_build.rs` -> **Wildan M** (100.0% isolated ownership) | Magnitude: 614.58
- `src/cook/fetch.rs` -> **Wildan M** (100.0% isolated ownership) | Magnitude: 459.56
- `src/cook/fs.rs` -> **Wildan M** (100.0% isolated ownership) | Magnitude: 339.04
- `src/recipe.rs` -> **Wildan M** (100.0% isolated ownership) | Magnitude: 331.12

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/cook/package.rs` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 67.3196%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/cook/fs.rs` -> **Severity: 2.933** (Embedded: 0.0485 * Error Risk: 60.4242%)
- `src/staged_pkg.rs` -> **Severity: 2.633** (Embedded: 0.0388 * Error Risk: 67.7936%)
- `src/cook/fetch.rs` -> **Severity: 1.164** (Embedded: 0.0218 * Error Risk: 53.2697%)
- `mk/qemu.mk` -> **Severity: 0.945** (Embedded: 0.0097 * Error Risk: 97.3219%)
- `recipes/shells/bash/etc/skel/.bashrc` -> **Severity: 0.945** (Embedded: 0.0097 * Error Risk: 97.3403%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/cook/fs.rs` -> **Severity: 2879.229** (Blast Radius: 33.591 * Doc Risk: 85.7143%)
- `src/cook/fetch.rs` -> **Severity: 2096.181** (Blast Radius: 21.638 * Doc Risk: 96.875%)
- `src/staged_pkg.rs` -> **Severity: 1850.666** (Blast Radius: 22.208 * Doc Risk: 83.3333%)
- `src/cook/package.rs` -> **Severity: 1272.2** (Blast Radius: 12.722 * Doc Risk: 100.0%)
- `mk/ci.mk` -> **Severity: 968.7** (Blast Radius: 9.687 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
