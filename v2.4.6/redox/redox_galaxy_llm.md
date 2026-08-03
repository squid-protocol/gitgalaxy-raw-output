# ARCHITECTURAL_BRIEF: redox
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/redox` |
| **Timestamp** | `2026-08-03T19:44:29.735003+00:00` |
| **Scan Duration** | `2.28s` |
| **Git Branch** | `master` |
| **Git Commit** | `79fb42097d2d91ed85aac7c0f20d75e50c9ad9fb` |
| **Git Remote** | `https://github.com/redox-os/redox.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 69 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
| Total Artifacts | 3191 |
| Analyzed Artifacts (Scanned) | 93 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3098 |
| Total LOC | 10436 |
| Volatility Index | 0.032 |
| % Scanned of codebase = | 2.9% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.518 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.7763 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8182 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| SHELL | 32 | 2431 | 34.4% |
| PLAINTEXT | 20 | 0 | 21.5% |
| RUST | 19 | 4959 | 20.4% |
| MAKEFILE | 11 | 1446 | 11.8% |
| C | 4 | 1033 | 4.3% |
| MARKDOWN | 3 | 0 | 3.2% |
| PYTHON | 2 | 146 | 2.2% |
| NIX | 1 | 176 | 1.1% |
| CSS | 1 | 245 | 1.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.394`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 49 | 52.7% |
| file_cluster_13 | 7 | 7.5% |
| file_cluster_12 | 5 | 5.4% |
| file_cluster_0 | 3 | 3.2% |
| file_cluster_11 | 3 | 3.2% |
| file_cluster_17 | 2 | 2.2% |
| file_cluster_16 | 1 | 1.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 23 | 24.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3098*

**Composition by Extension & Reason:**
- `.toml`: 2558x Excluded (Unsupported Extension: '.toml'), 304x Unsupported Format (.toml), 69x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 107x Excluded (Unsupported Extension: '.patch'), 8x Unsupported Format (.patch), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 10x Unsupported Format (.undeterminable), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 279 LOC)
- `.sha`: 4x Excluded (Unsupported Extension: '.sha')
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.lock`: 2x Excluded (Unsupported Extension: '.lock')
- `.cmake`: 2x Excluded (Unsupported Extension: '.cmake')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 1x Excluded (Explicitly Denied Extension: '.ttf')
- `.wav`: 1x Excluded (Explicitly Denied Extension: '.wav')
- `.ion`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bashrc`: 1x Excluded (Unsupported Extension: '.bashrc')
- `.c`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 45.0 | 29.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.3 | 42.9 | 40.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 54.0 | 57.8 | 100.0 |
| Testing Exposure | 0.0 | 80.0 | 23.9 | 2.3 | 80.0 |
| API Exposure | 0.0 | 12.2 | 3.5 | 2.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 59.0 | 87.8 | 0.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 2.9 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 92.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.1 | 0.5 | 0.2 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 22.0 | 8.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 68.1 | 76.9 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 41.9 | 1.3 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 7.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 17.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `mk/prefix.mk` (Hits: 106)
- `native_bootstrap.sh` (Hits: 70)
- `podman_bootstrap.sh` (Hits: 52)

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

- `parse_args` (@ `src/bin/repo.rs`) -> Impact: **1784.2** | LOC: 1103
- `build` (@ `src/cook/cook_build.rs`) -> Impact: **1140.6** | LOC: 242
- `fetch_offline` (@ `src/cook/fetch.rs`) -> Impact: **667.8** | LOC: 383
- `Anonymous_Block_[Truncated]` (@ `native_bootstrap.sh`) -> Impact: **603.7** | LOC: 689
- `auto_deps_from_dynamic_linking` (@ `src/cook/cook_build.rs`) -> Impact: **469.5** | LOC: 130
- `Anonymous_Block_[Truncated]` (@ `podman_bootstrap.sh`) -> Impact: **448.4** | LOC: 413
- `publish_packages` (@ `src/bin/repo_builder.rs`) -> Impact: **445.6** | LOC: 231
  * *Intent:* // TODO: Make this callable from repo bin
- `walk_tree_entry` (@ `src/cook/tree.rs`) -> Impact: **411.0** | LOC: 86
- `new_recursive` (@ `src/recipe.rs`) -> Impact: **403.4** | LOC: 99
- `main` (@ `recipes/demos/sdl2-gears/gears.c`) -> Impact: **246.4** | LOC: 200

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `build` (@ `src/cook/cook_build.rs`) -> **O(2^N) [Recursive]**
- `new_recursive` (@ `src/recipe.rs`) -> **O(2^N) [Recursive]**
- `new_recursive_nonstop` (@ `src/staged_pkg.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// List ordered success packages and map of failed packages. /// A package can be both success and failed if dependencies aren't satistied.
- `fmt` (@ `src/lib.rs`) -> **O(2^N) [Recursive]**
- `main` (@ `src/bin/cookbook_redoxer.rs`) -> **O(2^N) [Recursive]**
- `parse_args` (@ `src/bin/repo_builder.rs`) -> **O(2^N) [Recursive]**
- `move_dir_all_inner_fn` (@ `src/cook/fs.rs`) -> **O(2^N) [Recursive]**
- `new` (@ `src/cook/ident.rs`) -> **O(2^N) [Recursive]**
- `package` (@ `src/cook/package.rs`) -> **O(2^N) [Recursive]**
- `read` (@ `src/cook/pty.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `Anonymous_Block_[Truncated]` (@ `native_bootstrap.sh`) -> DB Complexity: **155**
- `Anonymous_Block_[Truncated]` (@ `podman_bootstrap.sh`) -> DB Complexity: **117**
- `Anonymous_Block_[Truncated]` (@ `recipes/wip/dev/lang/perl5/configure_tool.sh`) -> DB Complexity: **80**
- `parse_args` (@ `src/bin/repo.rs`) -> DB Complexity: **61**
- `main` (@ `bin/aarch64-unknown-redox-llvm-config`) -> DB Complexity: **45**
- `main` (@ `bin/x86_64-unknown-redox-llvm-config`) -> DB Complexity: **45**
- `Anonymous_Block_[Truncated]` (@ `scripts/category.sh`) -> DB Complexity: **42**
  * *Intent:* #!/usr/bin/env bash # This script run the recipe command options on some Cookbook category
- `gear` (@ `recipes/demos/sdl2-gears/gears.c`) -> DB Complexity: **31**
- `write_ppm` (@ `recipes/demos/osdemo/osdemo.c`) -> DB Complexity: **28**
- `fetch_offline` (@ `src/cook/fetch.rs`) -> DB Complexity: **28**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `mk` | 10 | 5321.16 | 44.1% | 8.75% |
| `src/cook` | 9 | 4528.88 | 22.29% | 51.49% |
| `src/bin` | 3 | 3058.34 | 43.86% | 15.32% |
| `__monolith__` | 7 | 1919.28 | 25.82% | 24.49% |
| `src` | 6 | 1292.54 | 10.75% | 37.5% |
| `recipes/demos/osdemo` | 1 | 618.84 | 63.61% | 10.37% |
| `recipes/demos/sdl2-gears` | 1 | 500.64 | 84.35% | 10.37% |
| `bin` | 7 | 277.22 | 8.93% | 71.43% |
| `src/web` | 2 | 169.54 | 6.5% | 32.52% |
| `recipes/wip/dev/lang/perl5` | 1 | 152.02 | 30.45% | 81.34% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `bin/aarch64-unknown-redox-pkg-config` -> **100.0%** Exposure
- `bin/i586-unknown-redox-pkg-config` -> **100.0%** Exposure
- `bin/i686-unknown-redox-pkg-config` -> **100.0%** Exposure
- `bin/riscv64-unknown-redox-pkg-config` -> **100.0%** Exposure
- `bin/x86_64-unknown-redox-pkg-config` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `mk/qemu.mk` -> **100.0%** Exposure
- `podman/rustinstall.sh` -> **100.0%** Exposure
- `recipes/shells/bash/etc/skel/.bashrc` -> **100.0%** Exposure
- `recipes/shells/bash/etc/skel/.profile` -> **100.0%** Exposure
- `scripts/changelog.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `native_bootstrap.sh` -> **2** Orphaned Functions | **12** Duplicates
- `podman_bootstrap.sh` -> **2** Orphaned Functions | **12** Duplicates
- `src/cook/pty.rs` -> **4** Orphaned Functions | **8** Duplicates
- `src/cook/fetch_repo.rs` -> **10** Orphaned Functions | **0** Duplicates
- `src/lib.rs` -> **3** Orphaned Functions | **6** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`Makefile`** -> AI Confidence: **99.48%**
2. **`recipes/demos/gears/gears.c`** -> AI Confidence: **99.39%**
3. **`recipes/demos/osdemo/osdemo.c`** -> AI Confidence: **99.39%**
4. **`src/bin/repo.rs`** -> AI Confidence: **99.31%**
5. **`src/bin/repo_builder.rs`** -> AI Confidence: **99.31%**
6. **`src/config.rs`** -> AI Confidence: **99.31%**
7. **`src/cook/cook_build.rs`** -> AI Confidence: **99.31%**
8. **`mk/depends.mk`** -> AI Confidence: **99.29%**
9. **`mk/disk.mk`** -> AI Confidence: **99.29%**
10. **`mk/fstools.mk`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `bin/aarch64-unknown-redox-llvm-config` -> **100.0%** Exposure
- `bin/x86_64-unknown-redox-llvm-config` -> **100.0%** Exposure
- `recipes/demos/cairo-demo/cairo-demo.c` -> **20.0%** Exposure
- `recipes/demos/osdemo/osdemo.c` -> **20.0%** Exposure
- `recipes/demos/sdl2-gears/gears.c` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `Makefile` -> **100.0%** Exposure
- `mk/ci.mk` -> **100.0%** Exposure
- `mk/disk.mk` -> **100.0%** Exposure
- `mk/fstools.mk` -> **100.0%** Exposure
- `mk/prefix.mk` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `bin/aarch64-unknown-redox-llvm-config` -> **100.0%** Exposure
- `bin/x86_64-unknown-redox-llvm-config` -> **100.0%** Exposure
- `native_bootstrap.sh` -> **100.0%** Exposure
- `podman_bootstrap.sh` -> **100.0%** Exposure
- `scripts/find-recipe.sh` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `41` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `375` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `native_bootstrap.sh` (SHELL) -> Cumulative Risk: **774.55**
- **Archetype:** `file_cluster_8` (Distance: 11.231 IQR)
- **Magnitude:** 900.94 | **LOC:** 1193 | **CtrlFlow:** 77.5% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%), State Flux (87.1304%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 603.7), `Anonymous_Block` (Impact: 84.0), `Anonymous_Block` (Impact: 18.2)

### 2. `scripts/mount-redoxfs.sh` (SHELL) -> Cumulative Risk: **755.36**
- **Archetype:** `file_cluster_8` (Distance: 11.837 IQR)
- **Magnitude:** 10.73 | **LOC:** 120 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Tech Debt (99.996%), State Flux (99.9948%)
- **Heaviest Functions:** `check_dependencies` (Impact: 31.6), `Anonymous_Block` (Impact: 18.0), `unmount_fs` (Impact: 8.0)

### 3. `podman_bootstrap.sh` (SHELL) -> Cumulative Risk: **755.21**
- **Archetype:** `file_cluster_0` (Distance: 12.638 IQR)
- **Magnitude:** 655.3 | **LOC:** 664 | **CtrlFlow:** 76.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%), Tech Debt (98.8192%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 448.4), `Anonymous_Block` (Impact: 51.3), `Anonymous_Block` (Impact: 15.6)

### 4. `src/bin/repo.rs` (RUST) -> Cumulative Risk: **749.52**
- **Archetype:** `file_cluster_8` (Distance: 13.719 IQR)
- **Magnitude:** 2520.52 | **LOC:** 1951 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 93.8%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9995%), Churn (95.05%)
- **Heaviest Functions:** `parse_args` (Impact: 1784.2), `main_inner` (Impact: 179.6), `repo_inner` (Impact: 160.4)

### 5. `scripts/network-boot.sh` (SHELL) -> Cumulative Risk: **725.39**
- **Archetype:** `file_cluster_8` (Distance: 11.697 IQR)
- **Magnitude:** 1.73 | **LOC:** 53 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Cognitive Load (99.6035%), State Flux (99.4875%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 5.3), `__global_context__` (Impact: 3.2)

### 6. `src/cook/pty.rs` (RUST) -> Cumulative Risk: **715.18**
- **Archetype:** `file_cluster_13` (Distance: 13.023 IQR)
- **Magnitude:** 254.48 | **LOC:** 344 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `spawn_command` (Impact: 44.7), `read` (Impact: 26.6), `resize` (Impact: 18.4)

### 7. `src/web.rs` (RUST) -> Cumulative Risk: **701.2**
- **Archetype:** `file_cluster_13` (Distance: 11.4 IQR)
- **Magnitude:** 109.16 | **LOC:** 132 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.1687%)
- **Heaviest Functions:** `generate_web` (Impact: 64.2), `parse_args` (Impact: 16.6), `get_category` (Impact: 6.3)

### 8. `src/cook/fetch_repo.rs` (RUST) -> Cumulative Risk: **677.59**
- **Archetype:** `file_cluster_8` (Distance: 11.747 IQR)
- **Magnitude:** 156.3 | **LOC:** 205 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.8848%)
- **Heaviest Functions:** `load_cached_repo` (Impact: 28.8), `fetch_end` (Impact: 12.3), `download_increment` (Impact: 11.7)

### 9. `scripts/find-recipe.sh` (SHELL) -> Cumulative Risk: **671.04**
- **Archetype:** `file_cluster_12` (Distance: 10.291 IQR)
- **Magnitude:** 2.87 | **LOC:** 45 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Cognitive Load (99.8524%), Tech Debt (99.4824%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 19.1), `__global_context__` (Impact: 4.0)

### 10. `recipes/demos/osdemo/osdemo.c` (C) -> Cumulative Risk: **661.75**
- **Archetype:** `file_cluster_8` (Distance: 12.982 IQR)
- **Magnitude:** 618.84 | **LOC:** 548 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (98.5437%)
- **Heaviest Functions:** `test` (Impact: 62.1), `write_ppm` (Impact: 52.5), `display_image` (Impact: 42.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/bin/repo.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.719 IQR)
- **Top Global Matches:** file_cluster_8: 13.719, file_cluster_13: 13.733, file_cluster_17: 13.772
- **Magnitude:** 2520.52 | **LOC:** 1951 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 93.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (61.7174%), Tech Debt (17.807%)
**Top Internal Functions/Classes:**
  * `parse_args` (Impact: 1784.2 | O(N^6) | DB: 61)
  * `main_inner` (Impact: 179.6 | O(N^6))
  * `repo_inner` (Impact: 160.4 | O(N^6) | DB: 7)
  * `new` (Impact: 27.2 | O(N^4) | DB: 3)
  * `publish_packages` (Impact: 18.1 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 322`, `structural_boundaries: 331`, `args: 90`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 171`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 3`, `orphaned_logic: 2`
* *Architecture:* `io: 4`, `api: 6`, `concurrency: 64`, `import: 39`
* *Defense:* `safety: 195`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` env, Direction, std::cmp, cookbook::cook::package::package, cookbook::cook::fetch::FetchResult, style, staged_pkg, std::path::PathBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mk/qemu.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.98 IQR)
- **Top Global Matches:** file_cluster_17: 12.98, file_cluster_8: 13.327, file_cluster_0: 13.38
- **Magnitude:** 1757.88 | **LOC:** 379 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 55.6%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (88.2758%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 73`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 171`, `dead_code: 5`
* *Architecture:* `io: 24`, `api: 1`
* *Defense:* `safety: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.833
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01087
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cook/cook_build.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.613 IQR)
- **Top Global Matches:** file_cluster_8: 11.613, file_cluster_13: 11.672, file_cluster_11: 11.844
- **Magnitude:** 1680.42 | **LOC:** 760 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (23.6462%), Tech Debt (40.3711%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 1140.6 | O(2^N) | DB: 6)
  * `auto_deps_from_dynamic_linking` (Impact: 469.5 | O(N^6) | DB: 11)
  * `auto_deps_from_static_package_deps` (Impact: 7.4 | O(N^2))
  * `cached` (Impact: 7.3 | O(2^N))
  * `new` (Impact: 3.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 100`, `args: 14`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 36`, `planned_debt: 7`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 8`, `import: 13`
* *Defense:* `safety: 33`, `doc: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` str, pkg::PackageError, crate::cook::script::*, crate::cook::package::package_source_paths, PackageName, crate::recipe::AutoDeps, crate::recipe::BuildKind, std::os::unix...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mk/repo.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.02 IQR)
- **Top Global Matches:** file_cluster_8: 8.02, file_cluster_7: 8.899, file_cluster_17: 8.956
- **Magnitude:** 1188.04 | **LOC:** 261 | **CtrlFlow:** 98.1% | **Authorship Centralization:** 90.9%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (47.2799%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 2`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 6`
* *Architecture:* `io: 1`, `api: 13`
* *Defense:* `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.833
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01087
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mk/prefix.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.563 IQR)
- **Top Global Matches:** file_cluster_8: 10.563, file_cluster_0: 10.929, file_cluster_6: 10.957
- **Magnitude:** 1186.92 | **LOC:** 411 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (17.9427%), Tech Debt (17.3547%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 21`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 5`, `dead_code: 5`, `planned_debt: 4`
* *Architecture:* `io: 106`, `api: 17`
* *Defense:* `cleanup: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.833
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01087
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `native_bootstrap.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.231 IQR)
- **Top Global Matches:** file_cluster_8: 11.231, file_cluster_12: 11.643, file_cluster_7: 11.659
- **Magnitude:** 900.94 | **LOC:** 1193 | **CtrlFlow:** 77.5% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(N^4) | **DB Complexity:** 155
- **Risk Profile:** Cognitive Load (75.6609%), Tech Debt (72.5995%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 603.7 | O(N^4) | DB: 155)
  * `Anonymous_Block` (Impact: 84.0 | O(N^4) | DB: 26)
  * `Anonymous_Block` (Impact: 18.2 | O(N^2) | DB: 14)
  * `Anonymous_Block` (Impact: 15.6 | O(N^2) | DB: 11)
  * `Anonymous_Block` (Impact: 13.7 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 61`, `args: 55`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 54`, `high_risk_execution: 25`, `state_mutation: 96`, `dead_code: 4`, `duplicate_logic: 12`, `orphaned_logic: 2`
* *Architecture:* `io: 70`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 3`, `doc: 11`, `test: 17`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` the, env
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cook/fs.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.138 IQR)
- **Top Global Matches:** file_cluster_16: 13.138, file_cluster_8: 13.221, file_cluster_13: 13.336
- **Magnitude:** 835.36 | **LOC:** 451 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (31.211%), Tech Debt (9.6612%)
**Top Internal Functions/Classes:**
  * `move_dir_all_inner_fn` (Impact: 158.0 | O(2^N) | DB: 4)
  * `get_git_remote_tracking` (Impact: 154.4 | O(N^4) | DB: 6)
    * *Intent:* /// (local_branch_name, remote_branch, remote_name, remote_url) /// -> ("fix_stuff", "master", "orig...
  * `copy_dir_all` (Impact: 69.9 | O(2^N))
  * `get_git_fetch_rev` (Impact: 41.1 | O(N^4))
    * *Intent:* /// get commit rev after fetch
  * `check_files_present` (Impact: 39.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 106`, `args: 36`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 52`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 42`, `import: 4`
* *Defense:* `safety: 76`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.054348
  * `Imports (Out-Degree: 0):` walkdir::DirEntry, time::SystemTime, io::self, Stdio, Write, wrap_io_err, serde::Serialize, spawn_to_pipe...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/cook/fetch.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.376 IQR)
- **Top Global Matches:** file_cluster_13: 12.376, file_cluster_8: 12.633, file_cluster_11: 12.694
- **Magnitude:** 779.6 | **LOC:** 748 | **CtrlFlow:** 49.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (54.7801%), Tech Debt (15.0489%)
**Top Internal Functions/Classes:**
  * `fetch_offline` (Impact: 667.8 | O(N^6) | DB: 28)
  * `get_blake3` (Impact: 15.4 | O(N^2) | DB: 5)
  * `cached` (Impact: 7.3 | O(2^N))
  * `new` (Impact: 4.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 111`, `args: 23`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 61`, `planned_debt: 6`
* *Architecture:* `io: 7`, `api: 16`, `import: 28`
* *Defense:* `safety: 50`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.198
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.024457
  * `Imports (Out-Degree: 0):` crate::config::translate_mirror, pkg::SourceIdentifier, crate::wrap_io_err, crate::cook::script::*, std::fs, crate::cook::package::package_source_paths, std::path::Path, crate::cook::cook_build...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `podman_bootstrap.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.638 IQR)
- **Top Global Matches:** file_cluster_0: 12.638, file_cluster_8: 12.654, file_cluster_17: 12.692
- **Magnitude:** 655.3 | **LOC:** 664 | **CtrlFlow:** 76.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 117
- **Risk Profile:** Cognitive Load (76.3476%), Tech Debt (98.8192%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 448.4 | O(N^4) | DB: 117)
  * `Anonymous_Block` (Impact: 51.3 | O(N^4) | DB: 9)
  * `Anonymous_Block` (Impact: 15.6 | O(N^2) | DB: 11)
  * `Anonymous_Block` (Impact: 13.4 | O(N^2))
  * `Anonymous_Block` (Impact: 11.7 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 50`, `args: 47`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 19`, `state_mutation: 60`, `dead_code: 7`, `duplicate_logic: 12`, `orphaned_logic: 2`
* *Architecture:* `io: 52`, `import: 1`
* *Defense:* `safety: 3`, `doc: 11`, `test: 15`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` the, env
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `recipes/demos/osdemo/osdemo.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.982 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.271 IQR)
- **Top Global Matches:** file_cluster_8: 12.982, file_cluster_13: 13.035, file_cluster_0: 13.306
- **Magnitude:** 618.84 | **LOC:** 548 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (63.6069%), Tech Debt (10.3702%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 62.1 | O(N^3) | DB: 26)
  * `write_ppm` (Impact: 52.5 | O(N^4) | DB: 28)
  * `display_image` (Impact: 42.1 | O(N^2) | DB: 12)
  * `init_context` (Impact: 33.9 | O(N^4) | DB: 20)
  * `main` (Impact: 19.3 | O(N^2) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 21`, `args: 10`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 317`, `orphaned_logic: 1`
* *Architecture:* `io: 5`, `api: 51`, `import: 8`
* *Defense:* `safety: 6`, `doc: 1`, `test: 5`, `immutability_locks: 22`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` math.h, string.h, orbital.h, osmesa.h, glu.h, assert.h, stdlib.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cook/tree.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.534 IQR)
- **Top Global Matches:** file_cluster_8: 11.534, file_cluster_13: 11.641, file_cluster_17: 11.816
- **Magnitude:** 610.58 | **LOC:** 197 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (22.6202%), Tech Debt (23.0251%)
**Top Internal Functions/Classes:**
  * `walk_tree_entry` (Impact: 411.0 | O(2^N) | DB: 9)
  * `walk_file_tree` (Impact: 142.0 | O(2^N) | DB: 12)
  * `display_pkg_fn` (Impact: 15.5 | O(N^2))
  * `format_size` (Impact: 6.5 | O(N^2))
  * `display_tree_entry` (Impact: 6.1 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 47`, `args: 9`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 6`, `import: 5`
* *Defense:* `safety: 22`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs::read_to_string, pkg::Package, HashSet, crate::recipe::CookRecipe, anyhow::Context, std::
    collections::HashMap, path::PathBuf, PackageName...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/recipe.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.97 IQR)
- **Top Global Matches:** file_cluster_0: 11.97, file_cluster_16: 12.171, file_cluster_8: 12.246
- **Magnitude:** 534.0 | **LOC:** 717 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (7.2786%), Tech Debt (11.4512%)
**Top Internal Functions/Classes:**
  * `new_recursive` (Impact: 403.4 | O(2^N) | DB: 5)
  * `apply_filesystem_config` (Impact: 12.9 | O(N^5) | DB: 1)
  * `get_package_deps_recursive` (Impact: 8.9 | O(N^3))
  * `get_build_deps_recursive` (Impact: 8.8 | O(N^3))
  * `set_as_remote` (Impact: 8.4 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 35`, `args: 17`, `func_start: 11`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 25`, `planned_debt: 3`
* *Architecture:* `api: 33`, `import: 5`
* *Defense:* `safety: 34`, `doc: 39`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pkg::PackageError, SourceRecipe, PackageName, staged_pkg, crate::recipe::BuildKind, PackageRecipe, Serialize, crate::WALK_DEPTH...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `recipes/demos/sdl2-gears/gears.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.826 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.494 IQR)
- **Top Global Matches:** file_cluster_8: 11.826, file_cluster_13: 12.218, file_cluster_7: 12.25
- **Magnitude:** 500.64 | **LOC:** 524 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (84.35%), Tech Debt (10.3702%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 246.4 | O(N^6) | DB: 22)
  * `gear` (Impact: 14.5 | O(N^2) | DB: 31)
  * `CheckSDLError` (Impact: 11.0 | O(N^3) | DB: 1)
  * `cleanup` (Impact: 10.8 | O(N^2) | DB: 5)
  * `idle` (Impact: 4.8 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 22`, `args: 6`, `func_start: 8`
* *Risk/State:* `state_mutation: 164`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 31`, `import: 5`
* *Defense:* `doc: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SDL_mixer.h, SDL_ttf.h, SDL.h, SDL_opengl.h, SDL_image.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bin/repo_builder.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.019 IQR)
- **Top Global Matches:** file_cluster_13: 12.019, file_cluster_8: 12.118, file_cluster_17: 12.143
- **Magnitude:** 499.1 | **LOC:** 291 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (37.7789%), Tech Debt (28.1406%)
**Top Internal Functions/Classes:**
  * `publish_packages` (Impact: 445.6 | O(N^6) | DB: 18)
    * *Intent:* // TODO: Make this callable from repo bin
  * `is_newer` (Impact: 10.9 | O(N^3))
  * `parse_args` (Impact: 9.4 | O(2^N) | DB: 4)
  * `main` (Impact: 5.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 70`, `args: 17`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 23`, `planned_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 5`, `import: 14`
* *Defense:* `safety: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` File, SourceIdentifier, std::path::Path, staged_pkg, cookbook::cook::ident::get_ident, cookbook::cook::fetch, cookbook::web::CliWebConfig, std::env...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mk/disk.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.37 IQR)
- **Top Global Matches:** file_cluster_8: 7.37, file_cluster_7: 8.442, file_cluster_1: 8.617
- **Magnitude:** 458.36 | **LOC:** 102 | **CtrlFlow:** 87.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (50.2688%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 6`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 2`
* *Architecture:* `io: 11`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.833
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01087
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.505 IQR)
- **Top Global Matches:** file_cluster_8: 8.505, file_cluster_13: 8.725, file_cluster_7: 9.299
- **Magnitude:** 339.76 | **LOC:** 136 | **CtrlFlow:** 93.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (28.7056%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 2`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 5`
* *Architecture:* `io: 2`, `api: 4`, `import: 10`
* *Defense:* `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` depends.mk, fstools.mk, qemu.mk, config.mk, prefix.mk, virtualbox.mk, ci.mk, disk.mk...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/staged_pkg.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.274 IQR)
- **Top Global Matches:** file_cluster_13: 12.274, file_cluster_17: 12.432, file_cluster_8: 12.436
- **Magnitude:** 288.8 | **LOC:** 161 | **CtrlFlow:** 54.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (23.5368%), Tech Debt (14.3599%)
**Top Internal Functions/Classes:**
  * `new_recursive_nonstop` (Impact: 213.1 | O(2^N) | DB: 4)
    * *Intent:* /// List ordered success packages and map of failed packages. /// A package can be both success and ...
  * `new_recursive` (Impact: 27.7 | O(N^2))
  * `from_path` (Impact: 11.2 | O(N^2) | DB: 5)
  * `new` (Impact: 6.2 | O(N^1))
  * `list` (Impact: 3.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 34`, `args: 13`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 15`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 7`, `import: 6`
* *Defense:* `safety: 31`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.835
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.043478
  * `Imports (Out-Degree: 0):` BTreeSet, pkg::Package, std::borrow::Cow, PathBuf, PackageError, std::sync::LazyLock, std::ffi::OsStr, std::path::Path...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `mk/podman.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.86 IQR)
- **Top Global Matches:** file_cluster_8: 10.86, file_cluster_0: 11.177, file_cluster_6: 11.182
- **Magnitude:** 256.04 | **LOC:** 102 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 54.5%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (19.3769%), Tech Debt (44.3425%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 18`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 2`, `state_mutation: 6`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 2`
* *Defense:* `doc: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.833
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01087
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cook/pty.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.023 IQR)
- **Top Global Matches:** file_cluster_13: 13.023, file_cluster_4: 13.219, file_cluster_0: 13.282
- **Magnitude:** 254.48 | **LOC:** 344 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (23.0182%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `spawn_command` (Impact: 44.7 | O(N^6) | DB: 2)
  * `read` (Impact: 26.6 | O(2^N) | DB: 2)
  * `resize` (Impact: 18.4 | O(2^N))
  * `openpty` (Impact: 14.2 | O(2^N))
  * `spawn_command` (Impact: 10.5 | O(2^N) | DB: 1)
    * *Intent:* // Clean up a few things before we exec the program // Clear out any potentially problematic signal ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 67`, `args: 17`, `func_start: 16`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 39`, `planned_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 4`
* *Architecture:* `io: 5`, `api: 11`, `concurrency: 15`, `import: 13`
* *Defense:* `safety: 41`, `doc: 12`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::os::fd::FromRawFd, mem, std::
    io::PipeReader, ptr, std::os::unix::io::AsRawFd, winsize, process::Command, Write...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mk/fstools.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.025 IQR)
- **Top Global Matches:** file_cluster_8: 7.025, file_cluster_7: 8.078, file_cluster_1: 8.324
- **Magnitude:** 203.88 | **LOC:** 57 | **CtrlFlow:** 85.0% | **Authorship Centralization:** 85.7%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (58.992%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 3`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 3`
* *Architecture:* `io: 3`, `api: 1`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.833
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01087
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/config.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.119 IQR)
- **Top Global Matches:** file_cluster_0: 11.119, file_cluster_8: 11.278, file_cluster_13: 11.455
- **Magnitude:** 199.8 | **LOC:** 255 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (4.4727%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init_config` (Impact: 76.8 | O(N^4) | DB: 3)
  * `translate_mirror` (Impact: 43.6 | O(N^5) | DB: 1)
  * `extract_env` (Impact: 8.1 | O(N^2))
  * `from` (Impact: 4.7 | O(N^3))
  * `setup_test_config` (Impact: 4.1 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 25`, `args: 17`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 6`
* *Architecture:* `api: 35`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 33`, `doc: 13`, `test: 15`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` env, serde::Deserialize, Serialize, sync::OnceLock, std::collections::HashMap, super::*, fs, str::FromStr
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/web/html.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.354 IQR)
- **Top Global Matches:** file_cluster_8: 9.354, file_cluster_17: 9.891, file_cluster_13: 9.954
- **Magnitude:** 168.92 | **LOC:** 330 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (7.7149%), Tech Debt (13.7579%)
**Top Internal Functions/Classes:**
  * `generate_html_pkg` (Impact: 80.6 | O(N^4) | DB: 1)
  * `get_tree_url` (Impact: 34.7 | O(N^2) | DB: 1)
  * `generate_html_index` (Impact: 27.9 | O(N^5) | DB: 1)
  * `get_short_commit` (Impact: 4.2 | O(N^1))
  * `get_hostname` (Impact: 3.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 45`, `args: 13`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 9`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pkg::Package, crate::recipe::SourceRecipe, crate::web::get_category, crate::cook::tree::format_size, std::fs, recipe::CookRecipe, path::Path, crate::cook::ident...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cook/package.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.899 IQR)
- **Top Global Matches:** file_cluster_8: 11.899, file_cluster_13: 11.947, file_cluster_6: 12.174
- **Magnitude:** 167.24 | **LOC:** 311 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (12.2489%), Tech Debt (64.4004%)
**Top Internal Functions/Classes:**
  * `package` (Impact: 152.3 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 26`, `args: 8`, `func_start: 7`
* *Risk/State:* `state_mutation: 7`, `planned_debt: 6`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `safety: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.227
  * `Choke Point (Betweenness):` 0.000119 | `Ripple Effect (Closeness):` 0.01087
  * `Imports (Out-Degree: 1):` PackagePrefix, pkg::InstallState, Package, PackageName, pkgar_core::PackageSrc, CookRecipe, OptionalPackageRecipe, cook::cook_build::BuildResult...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cook/fetch_repo.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.747 IQR)
- **Top Global Matches:** file_cluster_8: 11.747, file_cluster_13: 11.976, file_cluster_11: 12.064
- **Magnitude:** 156.3 | **LOC:** 205 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (20.0637%), Tech Debt (99.8848%)
**Top Internal Functions/Classes:**
  * `load_cached_repo` (Impact: 28.8 | O(N^3) | DB: 9)
  * `fetch_end` (Impact: 12.3 | O(N^3) | DB: 1)
  * `download_increment` (Impact: 11.7 | O(N^3) | DB: 1)
  * `download_start` (Impact: 8.5 | O(N^3) | DB: 1)
  * `format_size` (Impact: 8.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 45`, `args: 19`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 28`, `planned_debt: 1`, `orphaned_logic: 10`
* *Architecture:* `io: 4`, `api: 5`, `import: 2`
* *Defense:* `safety: 16`, `doc: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Repository, PathBuf, time::Duration, SilentCallback, io::PipeWriter, std::
    cell::RefCell, pkg::
    PackageName, rc::Rc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mk/ci.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.35 IQR)
- **Top Global Matches:** file_cluster_8: 7.35, file_cluster_7: 8.332, file_cluster_1: 8.577
- **Magnitude:** 152.68 | **LOC:** 72 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 62.5%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (28.9399%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 6`, `func_start: 5`
* *Risk/State:* `high_risk_execution: 2`
* *Architecture:* `io: 28`, `api: 2`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.833
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01087
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `podman_bootstrap.sh` (SHELL) | Magnitude: 655.3 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 401, branch: 161, debug_prints: 148, state_mutation: 60
- `src/config.rs` (RUST) | Magnitude: 199.8 | Delta: **0.159 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 183, api: 35, safety: 33, encapsulation: 28
- `src/recipe.rs` (RUST) | Magnitude: 534.0 | Delta: **0.201 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 296, doc: 39, structural_boundaries: 35, safety: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `scripts/check-ci-config.sh` (SHELL) | Magnitude: 5.05 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 21, branch: 17, reflection_metaprogramming: 10, indent_spaces: 10
- `recipes/shells/bash/etc/skel/.bashrc` (SHELL) | Magnitude: 58.58 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: branch: 24, state_mutation: 21, indent_spaces: 17, structural_boundaries: 10
- `scripts/include-recipes.sh` (SHELL) | Magnitude: 2.62 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 12, indent_spaces: 8, branch: 7, safety_bypasses: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/ventoy.sh` (SHELL) | Magnitude: 3.06 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 12, indent_spaces: 12, reflection_metaprogramming: 11, branch: 10
- `scripts/find-recipe.sh` (SHELL) | Magnitude: 2.87 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 18, indent_spaces: 17, branch: 13, structural_boundaries: 13
- `scripts/dual-boot.sh` (SHELL) | Magnitude: 3.44 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 17, state_mutation: 15, branch: 10, safety: 8
- `scripts/changelog.sh` (SHELL) | Magnitude: 13.38 | Delta: **0.161 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 48, state_mutation: 44, branch: 37, reflection_metaprogramming: 36
- `podman/rustinstall.sh` (SHELL) | Magnitude: 12.3 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 10, state_mutation: 8, reflection_metaprogramming: 7, debug_prints: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/web.rs` (RUST) | Magnitude: 109.16 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 31, branch: 16, state_mutation: 15
- `recipes/shells/bash/etc/skel/.profile` (SHELL) | Magnitude: 20.22 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: globals: 10, branch: 8, state_mutation: 6, indent_spaces: 5
- `src/bin/repo_builder.rs` (RUST) | Magnitude: 499.1 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 215, structural_boundaries: 70, branch: 65, safety: 34
- `src/staged_pkg.rs` (RUST) | Magnitude: 288.8 | Delta: **0.158 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 115, branch: 41, structural_boundaries: 34, safety: 31
- `src/cook/pty.rs` (RUST) | Magnitude: 254.48 | Delta: **0.196 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 168, structural_boundaries: 67, safety: 41, state_mutation: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/cook/fs.rs` (RUST) | Magnitude: 835.36 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 306, branch: 125, structural_boundaries: 106, safety: 76

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/bin/cookbook_redoxer.rs` (RUST) | Magnitude: 38.72 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 4, branch: 3, state_mutation: 3
- `mk/qemu.mk` (MAKEFILE) | Magnitude: 1757.88 | Delta: **0.347 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 220, state_mutation: 171, branch: 141, structural_boundaries: 73

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/bin/repo.rs` (RUST) | Magnitude: 2520.52 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1290, structural_boundaries: 331, branch: 322, safety: 195
- `src/cook/package.rs` (RUST) | Magnitude: 167.24 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 26, safety: 19, branch: 11
- `recipes/demos/osdemo/osdemo.c` (C) | Magnitude: 618.84 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 377, state_mutation: 317, branch: 65, api: 51
- `src/cook/cook_build.rs` (RUST) | Magnitude: 1680.42 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 364, branch: 110, structural_boundaries: 100, state_mutation: 36
- `scripts/recipe-path.sh` (SHELL) | Magnitude: 1.02 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: branch: 3, state_mutation: 3, reflection_metaprogramming: 2, args: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/bin/repo.rs` -> Churn: **95.05%** | Cog Load: 61.7174% | Debt: 17.807%
- `src/cook/fetch.rs` -> Churn: **71.74%** | Cog Load: 54.7801% | Debt: 15.0489%
- `src/cook/package.rs` -> Churn: **67.55%** | Cog Load: 12.2489% | Debt: 64.4004%
- `mk/qemu.mk` -> Churn: **61.33%** | Cog Load: 88.2758% | Debt: 0.0%
- `mk/fstools.mk` -> Churn: **56.53%** | Cog Load: 58.992% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/bin/repo.rs` -> **Wildan M** (93.8% isolated ownership) | Magnitude: 2520.52
- `src/cook/cook_build.rs` -> **Wildan M** (100.0% isolated ownership) | Magnitude: 1680.42
- `mk/repo.mk` -> **Wildan M** (90.9% isolated ownership) | Magnitude: 1188.04
- `src/cook/fs.rs` -> **Wildan M** (100.0% isolated ownership) | Magnitude: 835.36
- `src/cook/fetch.rs` -> **Wildan M** (100.0% isolated ownership) | Magnitude: 779.6

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/cook/package.rs` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 61.9305%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/cook/fs.rs` -> **Severity: 1.01** (Embedded: 0.0543 * Error Risk: 18.5822%)
- `src/cook/fetch.rs` -> **Severity: 0.983** (Embedded: 0.0245 * Error Risk: 40.1781%)
- `mk/disk.mk` -> **Severity: 0.87** (Embedded: 0.0109 * Error Risk: 80.0%)
- `mk/podman.mk` -> **Severity: 0.87** (Embedded: 0.0109 * Error Risk: 80.0%)
- `src/staged_pkg.rs` -> **Severity: 0.76** (Embedded: 0.0435 * Error Risk: 17.4725%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/cook/fs.rs` -> **Severity: 3756.5** (Blast Radius: 37.565 * Doc Risk: 100.0%)
- `src/staged_pkg.rs` -> **Severity: 1642.8** (Blast Radius: 24.835 * Doc Risk: 66.1486%)
- `src/cook/fetch.rs` -> **Severity: 1084.213** (Blast Radius: 24.198 * Doc Risk: 44.8059%)
- `mk/config.mk` -> **Severity: 1083.3** (Blast Radius: 10.833 * Doc Risk: 100.0%)
- `mk/depends.mk` -> **Severity: 1083.3** (Blast Radius: 10.833 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
