# ARCHITECTURAL_BRIEF: redox
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/redox` |
| **Timestamp** | `2026-08-07T04:05:28.911575+00:00` |
| **Scan Duration** | `2.05s` |
| **Git Branch** | `master` |
| **Git Commit** | `79fb42097d2d91ed85aac7c0f20d75e50c9ad9fb` |
| **Git Remote** | `https://github.com/redox-os/redox.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 69 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
| Dominant Lang | MAKEFILE |

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
| Cognitive Load Exposure | 0.0 | 100.0 | 43.7 | 25.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 58.9 | 78.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 54.2 | 57.8 | 100.0 |
| Testing Exposure | 0.0 | 80.0 | 15.1 | 2.3 | 0.0 |
| API Exposure | 0.0 | 12.2 | 3.6 | 2.5 | 0.0 |
| Concurrency Exposure | 0.0 | 95.4 | 3.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 59.1 | 88.7 | 0.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 2.9 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 92.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.1 | 0.5 | 0.2 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 22.0 | 8.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 49.9 | 51.0 | 66.3 |
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

- `parse_args` (@ `src/bin/repo.rs`) -> Impact: **541.1** | LOC: 1103
- `Anonymous_Block_[Truncated]` (@ `native_bootstrap.sh`) -> Impact: **380.9** | LOC: 689
- `Anonymous_Block_[Truncated]` (@ `podman_bootstrap.sh`) -> Impact: **290.8** | LOC: 413
- `run_tui_cook` (@ `src/bin/repo.rs`) -> Impact: **256.6** | LOC: 491
- `fetch_offline` (@ `src/cook/fetch.rs`) -> Impact: **180.2** | LOC: 383
- `build` (@ `src/cook/cook_build.rs`) -> Impact: **170.5** | LOC: 242
- `publish_packages` (@ `src/bin/repo_builder.rs`) -> Impact: **133.6** | LOC: 231
  * *Intent:* // TODO: Make this callable from repo bin
- `auto_deps_from_dynamic_linking` (@ `src/cook/cook_build.rs`) -> Impact: **120.5** | LOC: 130
- `Anonymous_Block_[Truncated]` (@ `recipes/wip/dev/lang/perl5/configure_tool.sh`) -> Impact: **95.4** | LOC: 240
- `main` (@ `recipes/demos/sdl2-gears/gears.c`) -> Impact: **77.5** | LOC: 200

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `mk` | 10 | 5201.16 | 35.98% | 8.75% |
| `src/cook` | 9 | 1682.08 | 21.61% | 51.49% |
| `src/bin` | 3 | 1550.44 | 42.46% | 18.41% |
| `__monolith__` | 7 | 1540.48 | 23.85% | 24.49% |
| `recipes/demos/osdemo` | 1 | 518.74 | 63.61% | 10.37% |
| `src` | 6 | 518.34 | 10.42% | 37.5% |
| `recipes/demos/sdl2-gears` | 1 | 317.94 | 84.35% | 10.37% |
| `bin` | 7 | 189.62 | 8.93% | 71.43% |
| `recipes/wip/dev/lang/perl5` | 1 | 181.42 | 38.74% | 81.34% |
| `recipes/shells/bash/etc/skel` | 2 | 95.7 | 52.5% | 100.0% |

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `41` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `375` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `podman/rustinstall.sh` (SHELL) -> Cumulative Risk: **607.73**
- **Archetype:** `file_cluster_12` (Distance: 14.418 IQR)
- **Magnitude:** 14.3 | **LOC:** 21 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9996%)
- **Heaviest Functions:** `__global_context__` (Impact: 6.0)

### 2. `scripts/network-boot.sh` (SHELL) -> Cumulative Risk: **606.83**
- **Archetype:** `file_cluster_8` (Distance: 11.697 IQR)
- **Magnitude:** 1.73 | **LOC:** 53 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.4875%), Cognitive Load (98.8723%), Tech Debt (96.8356%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 5.3), `__global_context__` (Impact: 3.2)

### 3. `native_bootstrap.sh` (SHELL) -> Cumulative Risk: **596.63**
- **Archetype:** `file_cluster_8` (Distance: 11.493 IQR)
- **Magnitude:** 678.54 | **LOC:** 1193 | **CtrlFlow:** 84.9% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (93.4923%), Safety Score (89.526%), Verification (80.0%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 380.9), `Anonymous_Block` (Impact: 54.3), `Anonymous_Block` (Impact: 21.8)

### 4. `scripts/commit-hash.sh` (SHELL) -> Cumulative Risk: **592.24**
- **Archetype:** `file_cluster_8` (Distance: 12.318 IQR)
- **Magnitude:** 3.06 | **LOC:** 28 | **CtrlFlow:** 85.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.6047%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 13.7), `Anonymous_Block` (Impact: 6.2), `__global_context__` (Impact: 1.4)

### 5. `podman_bootstrap.sh` (SHELL) -> Cumulative Risk: **570.03**
- **Archetype:** `file_cluster_0` (Distance: 12.828 IQR)
- **Magnitude:** 498.9 | **LOC:** 664 | **CtrlFlow:** 84.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (98.8192%), State Flux (97.4667%), Safety Score (94.1363%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 290.8), `Anonymous_Block` (Impact: 32.9), `Anonymous_Block` (Impact: 16.4)

### 6. `scripts/find-recipe.sh` (SHELL) -> Cumulative Risk: **565.77**
- **Archetype:** `file_cluster_12` (Distance: 10.334 IQR)
- **Magnitude:** 2.67 | **LOC:** 45 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Cognitive Load (99.88%), Tech Debt (99.4824%), Safety Score (92.7779%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 17.1), `__global_context__` (Impact: 4.0)

### 7. `recipes/shells/bash/etc/skel/.bashrc` (SHELL) -> Cumulative Risk: **558.95**
- **Archetype:** `file_cluster_11` (Distance: 15.409 IQR)
- **Magnitude:** 69.78 | **LOC:** 100 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 24.4), `Anonymous_Block` (Impact: 11.5), `__global_context__` (Impact: 5.7)

### 8. `scripts/include-recipes.sh` (SHELL) -> Cumulative Risk: **558.81**
- **Archetype:** `file_cluster_11` (Distance: 13.794 IQR)
- **Magnitude:** 2.9 | **LOC:** 27 | **CtrlFlow:** 90.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.8778%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 10.3), `Anonymous_Block` (Impact: 4.3), `__global_context__` (Impact: 2.1)

### 9. `scripts/dual-boot.sh` (SHELL) -> Cumulative Risk: **556.41**
- **Archetype:** `file_cluster_12` (Distance: 13.471 IQR)
- **Magnitude:** 4.12 | **LOC:** 53 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9998%), Cognitive Load (99.9975%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 10.2), `Anonymous_Block` (Impact: 6.2), `Anonymous_Block` (Impact: 6.2)

### 10. `recipes/demos/osdemo/osdemo.c` (C) -> Cumulative Risk: **550.38**
- **Archetype:** `file_cluster_8` (Distance: 12.982 IQR)
- **Magnitude:** 518.74 | **LOC:** 548 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.3183%), Documentation (91.3317%)
- **Heaviest Functions:** `test` (Impact: 34.1), `display_image` (Impact: 28.7), `write_ppm` (Impact: 22.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `mk/qemu.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.972 IQR)
- **Top Global Matches:** file_cluster_17: 12.972, file_cluster_8: 13.317, file_cluster_0: 13.371
- **Magnitude:** 1657.88 | **LOC:** 379 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 55.6%
- **Risk Profile:** Cognitive Load (86.9145%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 73`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 171`, `dead_code: 5`
* *Architecture:* `io: 24`, `api: 1`
* *Defense:* `safety: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.833
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01087
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/bin/repo.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.679 IQR)
- **Top Global Matches:** file_cluster_8: 13.679, file_cluster_13: 13.694, file_cluster_17: 13.733
- **Magnitude:** 1364.52 | **LOC:** 1951 | **CtrlFlow:** 48.7% | **Authorship Centralization:** 93.8%
- **Risk Profile:** Cognitive Load (58.0535%), Tech Debt (27.0854%)
**Top Internal Functions/Classes:**
  * `parse_args` (Impact: 541.1)
  * `run_tui_cook` (Impact: 256.6)
  * `main_inner` (Impact: 50.5)
  * `repo_inner` (Impact: 46.3)
  * `draw_prompt` (Impact: 29.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 331`, `args: 77`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 171`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 3`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 4`, `api: 6`, `concurrency: 54`, `import: 39`
* *Defense:* `safety: 195`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` get_config, fetch_offline, std::path::PathBuf, Write, Position, MouseEvent, Key, env...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mk/prefix.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.563 IQR)
- **Top Global Matches:** file_cluster_8: 10.563, file_cluster_0: 10.929, file_cluster_6: 10.957
- **Magnitude:** 1186.92 | **LOC:** 411 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (14.0729%), Tech Debt (17.3547%)
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

### `mk/repo.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.02 IQR)
- **Top Global Matches:** file_cluster_8: 8.02, file_cluster_7: 8.899, file_cluster_17: 8.957
- **Magnitude:** 1168.04 | **LOC:** 261 | **CtrlFlow:** 98.1% | **Authorship Centralization:** 90.9%
- **Risk Profile:** Cognitive Load (33.1154%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 2`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 6`
* *Architecture:* `io: 1`, `api: 13`
* *Defense:* `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.833
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01087
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `native_bootstrap.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.493 IQR)
- **Top Global Matches:** file_cluster_8: 11.493, file_cluster_12: 11.865, file_cluster_7: 11.899
- **Magnitude:** 678.54 | **LOC:** 1193 | **CtrlFlow:** 84.9% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (77.8963%), Tech Debt (72.5995%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 380.9)
  * `Anonymous_Block` (Impact: 54.3)
  * `Anonymous_Block` (Impact: 21.8)
  * `Anonymous_Block` (Impact: 16.4)
  * `Anonymous_Block` (Impact: 15.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 59`, `args: 55`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 54`, `high_risk_execution: 25`, `state_mutation: 114`, `dead_code: 4`, `duplicate_logic: 12`, `orphaned_logic: 2`
* *Architecture:* `io: 70`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 3`, `doc: 11`, `test: 17`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` env, the
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `recipes/demos/osdemo/osdemo.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.982 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.271 IQR)
- **Top Global Matches:** file_cluster_8: 12.982, file_cluster_13: 13.035, file_cluster_0: 13.306
- **Magnitude:** 518.74 | **LOC:** 548 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.6069%), Tech Debt (10.3702%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 34.1)
  * `display_image` (Impact: 28.7)
  * `write_ppm` (Impact: 22.3)
  * `init_context` (Impact: 14.8)
  * `main` (Impact: 13.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 21`, `args: 10`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 317`, `orphaned_logic: 1`
* *Architecture:* `io: 5`, `api: 51`, `import: 8`
* *Defense:* `safety: 6`, `doc: 1`, `test: 5`, `immutability_locks: 22`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` string.h, math.h, stdio.h, osmesa.h, orbital.h, stdlib.h, glu.h, assert.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `podman_bootstrap.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.828 IQR)
- **Top Global Matches:** file_cluster_0: 12.828, file_cluster_8: 12.875, file_cluster_17: 12.876
- **Magnitude:** 498.9 | **LOC:** 664 | **CtrlFlow:** 84.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.2962%), Tech Debt (98.8192%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 290.8)
  * `Anonymous_Block` (Impact: 32.9)
  * `Anonymous_Block` (Impact: 16.4)
  * `Anonymous_Block` (Impact: 14.8)
  * `Anonymous_Block` (Impact: 13.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 48`, `args: 47`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 19`, `state_mutation: 69`, `dead_code: 7`, `duplicate_logic: 12`, `orphaned_logic: 2`
* *Architecture:* `io: 52`, `import: 1`
* *Defense:* `safety: 3`, `doc: 11`, `test: 15`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` env, the
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mk/disk.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.37 IQR)
- **Top Global Matches:** file_cluster_8: 7.37, file_cluster_7: 8.442, file_cluster_1: 8.617
- **Magnitude:** 458.36 | **LOC:** 102 | **CtrlFlow:** 87.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.6671%), Tech Debt (0.0%)
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

### `src/cook/fetch.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.365 IQR)
- **Top Global Matches:** file_cluster_13: 12.365, file_cluster_8: 12.625, file_cluster_11: 12.691
- **Magnitude:** 416.3 | **LOC:** 748 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (50.4364%), Tech Debt (15.0489%)
**Top Internal Functions/Classes:**
  * `fetch_offline` (Impact: 180.2)
  * `fetch_remote` (Impact: 71.0)
  * `fetch_extract_tar` (Impact: 16.8)
    * *Intent:* //TODO: set upstream URL (is this needed?) // git remote set-url upstream "$GIT_UPSTREAM" &> /dev/nu...
  * `fetch_cargo` (Impact: 14.7)
  * `get_blake3` (Impact: 10.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 111`, `args: 22`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 61`, `planned_debt: 6`
* *Architecture:* `io: 7`, `api: 19`, `import: 28`
* *Defense:* `safety: 50`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.198
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.024457
  * `Imports (Out-Degree: 0):` crate::cook::fs::*, crate::recipe::BuildKind, crate::wrap_other_err, crate::recipe::SourceRecipe, crate::cook::package::get_package_name, crate::recipe::CookRecipe, std::process::Command, PathBuf...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/cook/fs.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.129 IQR)
- **Top Global Matches:** file_cluster_16: 13.129, file_cluster_8: 13.21, file_cluster_13: 13.327
- **Magnitude:** 395.66 | **LOC:** 451 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (30.1616%), Tech Debt (9.6612%)
**Top Internal Functions/Classes:**
  * `get_git_remote_tracking` (Impact: 60.4)
    * *Intent:* /// (local_branch_name, remote_branch, remote_name, remote_url) /// -> ("fix_stuff", "master", "orig...
  * `move_dir_all_inner_fn` (Impact: 32.8)
  * `check_files_present` (Impact: 20.2)
  * `copy_dir_all` (Impact: 18.0)
  * `get_git_fetch_rev` (Impact: 17.1)
    * *Intent:* /// get commit rev after fetch
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 106`, `args: 36`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 52`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 42`, `import: 4`
* *Defense:* `safety: 76`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.054348
  * `Imports (Out-Degree: 0):` config::translate_mirror, Stdio, Write, Result, PathBuf, walkdir::DirEntry, process::self, io::self...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/cook/cook_build.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.585 IQR)
- **Top Global Matches:** file_cluster_8: 11.585, file_cluster_13: 11.646, file_cluster_11: 11.82
- **Magnitude:** 351.72 | **LOC:** 760 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.9211%), Tech Debt (40.3711%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 170.5)
  * `auto_deps_from_dynamic_linking` (Impact: 120.5)
  * `auto_deps_from_static_package_deps` (Impact: 4.7)
  * `new` (Impact: 2.1)
  * `cached` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 100`, `args: 13`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 36`, `planned_debt: 7`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 8`, `import: 13`
* *Defense:* `safety: 33`, `doc: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` package_target, crate::recipe::BuildKind, PackageName, pkg::Package, PathBuf, crate::recipe::AutoDeps, crate::config::CookConfig, std::os::unix...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.505 IQR)
- **Top Global Matches:** file_cluster_8: 8.505, file_cluster_13: 8.725, file_cluster_7: 9.299
- **Magnitude:** 339.76 | **LOC:** 136 | **CtrlFlow:** 93.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (12.7698%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 2`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 5`
* *Architecture:* `io: 2`, `api: 4`, `import: 10`
* *Defense:* `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` podman.mk, prefix.mk, qemu.mk, depends.mk, fstools.mk, ci.mk, repo.mk, disk.mk...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `recipes/demos/sdl2-gears/gears.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.826 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.494 IQR)
- **Top Global Matches:** file_cluster_8: 11.826, file_cluster_13: 12.218, file_cluster_7: 12.25
- **Magnitude:** 317.94 | **LOC:** 524 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.35%), Tech Debt (10.3702%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 77.5)
  * `gear` (Impact: 11.0)
  * `cleanup` (Impact: 7.8)
  * `CheckSDLError` (Impact: 5.8)
  * `idle` (Impact: 3.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 22`, `args: 6`, `func_start: 8`
* *Risk/State:* `state_mutation: 164`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 31`, `import: 5`
* *Defense:* `doc: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SDL_opengl.h, SDL_ttf.h, SDL_image.h, SDL.h, SDL_mixer.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mk/podman.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.86 IQR)
- **Top Global Matches:** file_cluster_8: 10.86, file_cluster_0: 11.177, file_cluster_6: 11.182
- **Magnitude:** 256.04 | **LOC:** 102 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 54.5%
- **Risk Profile:** Cognitive Load (13.5193%), Tech Debt (44.3425%)
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

### `mk/fstools.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.025 IQR)
- **Top Global Matches:** file_cluster_8: 7.025, file_cluster_7: 8.078, file_cluster_1: 8.324
- **Magnitude:** 203.88 | **LOC:** 57 | **CtrlFlow:** 85.0% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (26.8941%), Tech Debt (0.0%)
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

### `recipes/wip/dev/lang/perl5/configure_tool.sh` (SHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.524 IQR)
- **Top Global Matches:** file_cluster_8: 9.524, file_cluster_0: 10.097, file_cluster_7: 10.171
- **Magnitude:** 181.42 | **LOC:** 352 | **CtrlFlow:** 82.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.7375%), Tech Debt (81.3438%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 95.4)
  * `whichprog` (Impact: 22.3)
    * *Intent:* # whichprog symbol VAR prog1 prog2
  * `tryfromenv` (Impact: 16.3)
  * `detect_cc_version` (Impact: 10.3)
    * *Intent:* # This is only a function for easy access to return-s # try.out contains `$cc --version` output. # #...
  * `__global_context__` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 22`, `args: 23`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 15`, `dead_code: 2`, `fragile_debt: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 42`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` |
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bin/repo_builder.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.009 IQR)
- **Top Global Matches:** file_cluster_13: 12.009, file_cluster_8: 12.108, file_cluster_17: 12.134
- **Magnitude:** 174.9 | **LOC:** 291 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.2353%), Tech Debt (28.1406%)
**Top Internal Functions/Classes:**
  * `publish_packages` (Impact: 133.6)
    * *Intent:* // TODO: Make this callable from repo bin
  * `is_newer` (Impact: 5.7)
  * `main` (Impact: 5.4)
  * `parse_args` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 70`, `args: 16`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 23`, `planned_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 5`, `import: 14`
* *Defense:* `safety: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pkg::Repository, Write, BTreeSet, std::env, init_ident, std::process::Command, File, PathBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/recipe.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.97 IQR)
- **Top Global Matches:** file_cluster_0: 11.97, file_cluster_16: 12.171, file_cluster_8: 12.246
- **Magnitude:** 163.4 | **LOC:** 717 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.2786%), Tech Debt (11.4512%)
**Top Internal Functions/Classes:**
  * `new_recursive` (Impact: 61.9)
  * `apply_filesystem_config` (Impact: 6.0)
  * `get_package_deps_recursive` (Impact: 4.9)
  * `get_build_deps_recursive` (Impact: 4.8)
  * `get_all_deps_names_recursive` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 35`, `args: 17`, `func_start: 11`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 25`, `planned_debt: 3`
* *Architecture:* `api: 33`, `import: 5`
* *Defense:* `safety: 34`, `doc: 39`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` crate::recipe::BuildKind, cook::package, PackageName, SourceRecipe, PathBuf, regex::Regex, pkg::PackageName, staged_pkg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cook/tree.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.496 IQR)
- **Top Global Matches:** file_cluster_8: 11.496, file_cluster_13: 11.604, file_cluster_17: 11.779
- **Magnitude:** 152.78 | **LOC:** 197 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.6202%), Tech Debt (23.0251%)
**Top Internal Functions/Classes:**
  * `walk_tree_entry` (Impact: 73.9)
  * `walk_file_tree` (Impact: 30.0)
  * `display_pkg_fn` (Impact: 10.6)
  * `format_size` (Impact: 4.5)
  * `display_tree_entry` (Impact: 4.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 47`, `args: 8`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 6`, `import: 5`
* *Defense:* `safety: 22`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::fmt::Write, PackageName, path::PathBuf, std::
    collections::HashMap, pkg::Package, fs::read_to_string, crate::recipe::CookRecipe, HashSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mk/ci.mk` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.35 IQR)
- **Top Global Matches:** file_cluster_8: 7.35, file_cluster_7: 8.332, file_cluster_1: 8.577
- **Magnitude:** 152.68 | **LOC:** 72 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 62.5%
- **Risk Profile:** Cognitive Load (17.1324%), Tech Debt (0.0%)
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

### `src/cook/pty.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.023 IQR)
- **Top Global Matches:** file_cluster_13: 13.023, file_cluster_4: 13.219, file_cluster_0: 13.282
- **Magnitude:** 139.38 | **LOC:** 344 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (23.0182%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `spawn_command` (Impact: 14.4)
  * `cloexec` (Impact: 6.5)
  * `read` (Impact: 5.8)
  * `spawn_to_pipe` (Impact: 5.5)
  * `flush_pty` (Impact: 4.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 67`, `args: 17`, `func_start: 16`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 39`, `planned_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 4`
* *Architecture:* `io: 5`, `api: 11`, `concurrency: 15`, `import: 13`
* *Defense:* `safety: 41`, `doc: 12`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::os::fd::FromRawFd, Write, Result, std::io, mem, PipeWriter, std::os::unix::process::CommandExt, crate::Error...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/config.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.093 IQR)
- **Top Global Matches:** file_cluster_0: 11.093, file_cluster_8: 11.248, file_cluster_13: 11.431
- **Magnitude:** 114.3 | **LOC:** 255 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.257%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init_config` (Impact: 29.1)
  * `translate_mirror` (Impact: 15.7)
  * `extract_env` (Impact: 5.5)
  * `from` (Impact: 2.7)
  * `setup_test_config` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 25`, `args: 16`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 6`
* *Architecture:* `api: 35`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 33`, `doc: 13`, `test: 15`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` env, fs, serde::Deserialize, str::FromStr, std::collections::HashMap, super::*, Serialize, sync::OnceLock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cook/fetch_repo.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.747 IQR)
- **Top Global Matches:** file_cluster_8: 11.747, file_cluster_13: 11.976, file_cluster_11: 12.064
- **Magnitude:** 102.5 | **LOC:** 205 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (20.0637%), Tech Debt (99.8848%)
**Top Internal Functions/Classes:**
  * `load_cached_repo` (Impact: 14.8)
  * `download_increment` (Impact: 6.5)
  * `fetch_end` (Impact: 6.3)
  * `init_binary_repo` (Impact: 4.5)
  * `format_size` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 45`, `args: 19`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 28`, `planned_debt: 1`, `orphaned_logic: 10`
* *Architecture:* `io: 4`, `api: 5`, `import: 2`
* *Defense:* `safety: 16`, `doc: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rc::Rc, time::Duration, RepoManager, io::PipeWriter, net_backend::CurlBackend, Write, pkg::
    PackageName, std::
    cell::RefCell...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/staged_pkg.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.262 IQR)
- **Top Global Matches:** file_cluster_13: 12.262, file_cluster_17: 12.42, file_cluster_8: 12.422
- **Magnitude:** 95.3 | **LOC:** 161 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.1019%), Tech Debt (14.3599%)
**Top Internal Functions/Classes:**
  * `new_recursive_nonstop` (Impact: 33.0)
    * *Intent:* /// List ordered success packages and map of failed packages. /// A package can be both success and ...
  * `new_recursive` (Impact: 18.8)
  * `from_path` (Impact: 7.8)
  * `new` (Impact: 6.2)
  * `list` (Impact: 2.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 34`, `args: 13`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 15`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 7`, `import: 6`
* *Defense:* `safety: 31`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.835
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.043478
  * `Imports (Out-Degree: 0):` HashMap, std::ffi::OsStr, std::borrow::Cow, std::sync::LazyLock, PackageName, std::collections::BTreeMap, BTreeSet, std::path::Path...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/web/html.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.309 IQR)
- **Top Global Matches:** file_cluster_8: 9.309, file_cluster_17: 9.852, file_cluster_13: 9.915
- **Magnitude:** 92.32 | **LOC:** 330 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.5278%), Tech Debt (13.7579%)
**Top Internal Functions/Classes:**
  * `generate_html_pkg` (Impact: 35.3)
  * `get_tree_url` (Impact: 23.6)
  * `generate_html_index` (Impact: 10.8)
  * `get_hostname` (Impact: 2.5)
  * `get_short_commit` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 45`, `args: 13`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 9`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.984
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::collections::BTreeMap, crate::cook::ident, crate::recipe::SourceRecipe, crate::web::get_category, pkg::Package, std::fs, recipe::CookRecipe, crate::cook::tree::format_size...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `podman_bootstrap.sh` (SHELL) | Magnitude: 498.9 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 401, branch: 263, debug_prints: 148, state_mutation: 69
- `src/config.rs` (RUST) | Magnitude: 114.3 | Delta: **0.155 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 183, api: 35, safety: 33, encapsulation: 28
- `src/recipe.rs` (RUST) | Magnitude: 163.4 | Delta: **0.201 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 296, doc: 39, structural_boundaries: 35, safety: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `scripts/check-ci-config.sh` (SHELL) | Magnitude: 5.13 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: branch: 21, state_mutation: 21, reflection_metaprogramming: 10, indent_spaces: 10
- `recipes/shells/bash/etc/skel/.bashrc` (SHELL) | Magnitude: 69.78 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: branch: 38, state_mutation: 21, indent_spaces: 17, structural_boundaries: 9
- `scripts/include-recipes.sh` (SHELL) | Magnitude: 2.9 | Delta: **0.15 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 12, branch: 9, indent_spaces: 8, safety_bypasses: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/ventoy.sh` (SHELL) | Magnitude: 2.92 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 12, state_mutation: 12, indent_spaces: 12, reflection_metaprogramming: 11
- `scripts/find-recipe.sh` (SHELL) | Magnitude: 2.67 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 18, branch: 17, indent_spaces: 17, structural_boundaries: 11
- `scripts/dual-boot.sh` (SHELL) | Magnitude: 4.12 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 17, branch: 16, state_mutation: 15, safety: 8
- `scripts/changelog.sh` (SHELL) | Magnitude: 11.89 | Delta: **0.132 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 55, state_mutation: 50, indent_spaces: 48, reflection_metaprogramming: 36
- `podman/rustinstall.sh` (SHELL) | Magnitude: 14.3 | Delta: **0.199 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 10, state_mutation: 8, reflection_metaprogramming: 7, debug_prints: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/web.rs` (RUST) | Magnitude: 60.36 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 31, branch: 16, state_mutation: 15
- `recipes/shells/bash/etc/skel/.profile` (SHELL) | Magnitude: 25.92 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: branch: 16, globals: 10, state_mutation: 6, indent_spaces: 5
- `src/bin/repo_builder.rs` (RUST) | Magnitude: 174.9 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 215, structural_boundaries: 70, branch: 64, safety: 34
- `src/staged_pkg.rs` (RUST) | Magnitude: 95.3 | Delta: **0.158 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 115, branch: 38, structural_boundaries: 34, safety: 31
- `src/cook/pty.rs` (RUST) | Magnitude: 139.38 | Delta: **0.196 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 168, structural_boundaries: 67, safety: 41, state_mutation: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/cook/fs.rs` (RUST) | Magnitude: 395.66 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 306, branch: 120, structural_boundaries: 106, safety: 76

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/bin/cookbook_redoxer.rs` (RUST) | Magnitude: 11.02 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 4, branch: 3, state_mutation: 3
- `mk/qemu.mk` (MAKEFILE) | Magnitude: 1657.88 | Delta: **0.345 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 220, state_mutation: 171, branch: 131, structural_boundaries: 73

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/bin/repo.rs` (RUST) | Magnitude: 1364.52 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1290, structural_boundaries: 331, branch: 314, safety: 195
- `src/cook/package.rs` (RUST) | Magnitude: 87.34 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 26, safety: 19, branch: 11
- `recipes/demos/osdemo/osdemo.c` (C) | Magnitude: 518.74 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 377, state_mutation: 317, branch: 65, api: 51
- `src/cook/cook_build.rs` (RUST) | Magnitude: 351.72 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 364, branch: 106, structural_boundaries: 100, state_mutation: 36
- `scripts/recipe-path.sh` (SHELL) | Magnitude: 1.02 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: branch: 3, state_mutation: 3, reflection_metaprogramming: 2, args: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/bin/repo.rs` -> Churn: **95.05%** | Cog Load: 58.0535% | Debt: 27.0854%
- `src/cook/fetch.rs` -> Churn: **71.74%** | Cog Load: 50.4364% | Debt: 15.0489%
- `src/cook/package.rs` -> Churn: **67.55%** | Cog Load: 12.2489% | Debt: 64.4004%
- `mk/qemu.mk` -> Churn: **61.33%** | Cog Load: 86.9145% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/bin/repo.rs` -> **Wildan M** (93.8% isolated ownership) | Magnitude: 1364.52
- `mk/repo.mk` -> **Wildan M** (90.9% isolated ownership) | Magnitude: 1168.04
- `mk/disk.mk` -> **Wildan M** (100.0% isolated ownership) | Magnitude: 458.36
- `src/cook/fetch.rs` -> **Wildan M** (100.0% isolated ownership) | Magnitude: 416.3
- `src/cook/fs.rs` -> **Wildan M** (100.0% isolated ownership) | Magnitude: 395.66

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/cook/package.rs` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 61.9305%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `mk/podman.mk` -> **Severity: 1.027** (Embedded: 0.0109 * Error Risk: 94.4368%)
- `mk/qemu.mk` -> **Severity: 1.022** (Embedded: 0.0109 * Error Risk: 94.0386%)
- `mk/disk.mk` -> **Severity: 1.019** (Embedded: 0.0109 * Error Risk: 93.7495%)
- `src/cook/fs.rs` -> **Severity: 1.01** (Embedded: 0.0543 * Error Risk: 18.5822%)
- `mk/fstools.mk` -> **Severity: 0.996** (Embedded: 0.0109 * Error Risk: 91.611%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/cook/fs.rs` -> **Severity: 3756.5** (Blast Radius: 37.565 * Doc Risk: 100.0%)
- `src/staged_pkg.rs` -> **Severity: 1443.83** (Blast Radius: 24.835 * Doc Risk: 58.1369%)
- `podman/rustinstall.sh` -> **Severity: 998.4** (Blast Radius: 9.984 * Doc Risk: 100.0%)
- `recipes/wip/vice/recipe.sh` -> **Severity: 998.4** (Blast Radius: 9.984 * Doc Risk: 100.0%)
- `recipes/demos/cairo-demo/cairo-demo.c` -> **Severity: 998.4** (Blast Radius: 9.984 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
