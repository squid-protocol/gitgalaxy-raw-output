# ARCHITECTURAL_BRIEF: bootloader
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/rust-osdev/bootloader.git` |
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
- **Scope:** 124 analyzed artifact(s), 8132 LOC.
- **Load-bearing artifact:** `api/src/info.rs` -- 41 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `uefi/src/main.rs` -- pulls in 48 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `common/src/load_kernel.rs` at magnitude 240.9 (structural weight, not risk).
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
| Total Artifacts | 175 |
| Analyzed Artifacts (Scanned) | 124 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 51 |
| Total LOC | 8132 |
| Volatility Index | 0.016 |
| % Scanned of codebase = | 70.9% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5947 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2323 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 9.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7422 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 16 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 105 | 7782 | 84.7% |
| MARKDOWN | 6 | 0 | 4.8% |
| PLAINTEXT | 4 | 0 | 3.2% |
| JSON | 4 | 85 | 3.2% |
| YAML | 3 | 197 | 2.4% |
| PYTHON | 1 | 31 | 0.8% |
| ASSEMBLY | 1 | 37 | 0.8% |

## 4.1 SOURCE ENCODINGS
All 124 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 18%, Data / Markup / Trivial 17%, Type Conversions Files 16%, State Mutators Files 11%, Large Core Modules (3) 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 114 | 91.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 10 | 8.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 51*

**Composition by Extension & Reason:**
- `.toml`: 26x Unsupported Format (.toml), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.toml')
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ld`: 4x Excluded (Unsupported Extension: '.ld')
- `.lock`: 3x Excluded (Unsupported Extension: '.lock')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 51.0 | 4.6 | 2.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 32.1 | 50.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.9 | 7.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.4 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 76.5 | 15.1 | 7.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 90.6 | 3.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 12.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 18.7 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.8 | 1.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 12.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 68.8 | 79.2 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 118 | 40 | 2 | `bios/stage-2/src/fat.rs` |
| cleanup | 2 | 1 | 0 | `src/lib.rs` |
| guards | 203 | 48 | 6 | `common/src/level_4_entries.rs` |
| danger | 332 | 53 | 5 | `build.rs` |
| concurrency | 40 | 16 | 1 | `build.rs` |
| connectivity | 445 | 70 | 8 | `api/src/info.rs` |
| io | 29 | 10 | 0 | `build.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 5 | 2 | 0 | `.github/workflows/trigger-release/trigger-release.py` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 46 | 13 | 1 | `uefi/src/main.rs` |
| tests | 155 | 42 | 4 | `common/src/legacy_memory_region.rs` |
| docs | 730 | 63 | 10 | `api/src/info.rs` |
| debt | 46 | 16 | 1 | `build.rs` |
| mutation | 1195 | 93 | 24 | `common/src/load_kernel.rs` |
| dead_code | 115 | 59 | 2 | `src/lib.rs` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `build.rs` (Hits: 10)
- `src/disk_image.rs` (Hits: 4)
- `tests/runner/src/lib.rs` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **info.rs** (`api/src/info.rs`) — 41 inbound connections
2. **lib.rs** (`api/src/lib.rs`) — 30 inbound connections
3. **config.rs** (`api/src/config.rs`) — 13 inbound connections
4. **lib.rs** (`tests/runner/src/lib.rs`) — 12 inbound connections
5. **lib.rs** (`bios/common/src/lib.rs`) — 8 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **main.rs** (`uefi/src/main.rs`) — 48 outbound dependencies
2. **lib.rs** (`common/src/lib.rs`) — 43 outbound dependencies
3. **main.rs** (`bios/stage-4/src/main.rs`) — 32 outbound dependencies
4. **load_kernel.rs** (`common/src/load_kernel.rs`) — 30 outbound dependencies
5. **main.rs** (`bios/stage-2/src/main.rs`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `set_up_mappings` **(Many-Argument Workhorses)** (@ `common/src/lib.rs`) -> Impact: **74.2** | LOC: 266
  * *Intent:* /// Sets up mappings for a kernel stack and the framebuffer. /// /// The `kernel_bytes` slice should contain the raw bytes of the kernel ELF executabl...
- `create_disk_image` **(Many-Argument Workhorses)** (@ `src/disk_image.rs`) -> Impact: **53.0** | LOC: 99
  * *Intent:* /// Creates a bootable disk image from the given bootloader executable.
- `new` **(Many-Argument Workhorses)** (@ `common/src/level_4_entries.rs`) -> Impact: **46.7** | LOC: 102
  * *Intent:* /// Initializes a new instance. /// /// Marks the statically configured virtual address ranges from the config as used.
- `handle_dynamic_segment` **(Many-Argument Workhorses)** (@ `common/src/load_kernel.rs`) -> Impact: **45.6** | LOC: 73
- `deserialize` **(Compute Cores)** (@ `api/src/config.rs`) -> Impact: **41.3** | LOC: 119
  * *Intent:* /// Tries to deserialize a config byte array that was created using [`Self::serialize`]. /// /// This is used by the bootloader to deserialize the con...
- `create_mbr_disk` **(Many-Argument Workhorses)** (@ `src/mbr.rs`) -> Impact: **38.0** | LOC: 90
- `get_best_mode` **(Many-Argument Workhorses)** (@ `bios/stage-2/src/vesa.rs`) -> Impact: **34.3** | LOC: 46
- `create_gpt_disk` **(Compute Cores)** (@ `src/gpt.rs`) -> Impact: **29.1** | LOC: 63
- `main_inner` **(Many-Argument Workhorses)** (@ `uefi/src/main.rs`) -> Impact: **26.3** | LOC: 111
- `load_segments` **(Defensive Guards)** (@ `common/src/load_kernel.rs`) -> Impact: **23.5** | LOC: 45

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `common/src` | 9 | 813.3 | 5.07% | 2.3% |
| `bios/stage-2/src` | 8 | 421.02 | 9.8% | 4.8% |
| `src` | 6 | 329.26 | 13.48% | 24.46% |
| `api/src` | 3 | 267.56 | 3.58% | 36.45% |
| `uefi/src` | 2 | 172.1 | 8.62% | 4.6% |
| `__monolith__` | 9 | 160.84 | 1.0% | 0.0% |
| `bios/stage-3/src` | 4 | 102.96 | 16.67% | 7.88% |
| `bios/boot_sector/src` | 5 | 80.9 | 6.26% | 26.86% |
| `bios/stage-4/src` | 2 | 71.78 | 5.23% | 36.97% |
| `.github/workflows` | 3 | 69.14 | 1.68% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/uefi/mod.rs` -> **99.9447%** Exposure
- `bios/boot_sector/src/boot.s` -> **99.9447%** Exposure
- `src/bios/mod.rs` -> **99.593%** Exposure
- `src/lib.rs` -> **84.1131%** Exposure
- `bios/stage-4/src/main.rs` -> **73.9488%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/workflows/trigger-release/trigger-release.py` -> **99.9994%** Exposure
- `.github/workflows/release.yml` -> **99.6316%** Exposure
- `bios/stage-2/src/disk.rs` -> **97.7472%** Exposure
- `bios/stage-3/src/paging.rs` -> **97.3403%** Exposure
- `bios/boot_sector/src/main.rs` -> **97.1417%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/lib.rs` -> **7** Orphaned Functions | **0** Duplicates
- `src/uefi/mod.rs` -> **5** Orphaned Functions | **0** Duplicates
- `bios/boot_sector/src/boot.s` -> **5** Orphaned Functions | **0** Duplicates
- `bios/stage-4/src/main.rs` -> **4** Orphaned Functions | **0** Duplicates
- `src/bios/mod.rs` -> **4** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `626` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `common/src/load_kernel.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.935)
- **Top Global Matches:** file_cluster_5: 8.935, file_cluster_12: 9.176, file_cluster_4: 9.382
- **Magnitude:** 240.9 | **LOC:** 827 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **30**; blast radius 3.805; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.8%), Connectivity (formerly Api Exposure) (40.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.4%)
- **Documentation Coverage:** 57.6923% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle_dynamic_segment` **(Many-Argument Workhorses)** (Impact: 45.6)
  * `load_segments` **(Defensive Guards)** (Impact: 23.5)
  * `new` **(Many-Argument Workhorses)** (Impact: 21.3)
  * `remove_copied_flags` **(Compute Cores)** (Impact: 17.6)
    * *Intent:* /// Cleans up the custom flags set by [`Inner::make_mut`].
  * `handle_load_segment` **(Compute Cores)** (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 188`, `args: 31`, `func_start: 21`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 11`, `state_mutation: 3`
* *Architecture:* `api: 10`, `import: 6`
* *Defense:* `safety: 13`, `doc: 49`, `test: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.805
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.02168
  * `Imports (Out-Degree: 4):` bootloader_api::config::Mapping, bootloader_api::info::TlsTemplate, core::cmp, core::iter::Step, core::mem::size_of, core::ops::Add, crate::PAGE_SIZE, crate::level_4_entries::UsedLevel4Entries...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `common/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.643)
- **Top Global Matches:** file_cluster_4: 9.643, file_cluster_5: 10.487, file_cluster_12: 11.149
- **Magnitude:** 197.0 | **LOC:** 700 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **43**; blast radius 5.687; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.2%), Mutation Surface (formerly State Flux) (22.1%)
- **Documentation Coverage:** 38.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_up_mappings` **(Many-Argument Workhorses)** (Impact: 74.2)
    * *Intent:* /// Sets up mappings for a kernel stack and the framebuffer. /// /// The `kernel_bytes` slice should...
  * `create_boot_info` **(Many-Argument Workhorses)** (Impact: 16.5)
    * *Intent:* /// Allocates and initializes the boot info struct and the memory map. /// /// The boot info and mem...
  * `mapping_addr` **(Many-Argument Workhorses)** (Impact: 9.7)
  * `init_logger` **(Many-Argument Workhorses)** (Impact: 5.8)
    * *Intent:* /// Initialize a text-based logger using the given pixel-based framebuffer as output.
  * `mapping_addr_page_aligned` **(Many-Argument Workhorses)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *High Risk Execution (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 147`, `args: 19`, `func_start: 12`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 12`, `state_mutation: 14`, `unreferenced_by_name: 3`
* *Architecture:* `api: 44`, `import: 10`
* *Defense:* `safety: 4`, `doc: 62`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.687
  * `Choke Point (Betweenness):` 0.001899 | `Ripple Effect (Closeness):` 0.03252
  * `Imports (Out-Degree: 11):` entropy, framebuffer, gdt, legacy_memory_region, level_4_entries, load_kernel, logger, serial...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `bios/stage-2/src/fat.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.842)
- **Top Global Matches:** file_cluster_5: 6.842, file_cluster_12: 8.606, file_cluster_0: 9.897
- **Magnitude:** 165.38 | **LOC:** 506 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 2.682; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.7%), Connectivity (formerly Api Exposure) (61.4%), Guard Balance (formerly Safety Score) (56.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `classify_fat_entry` **(Many-Argument Workhorses)** (Impact: 17.1)
  * `find_file_in_root_dir` **(Many-Argument Workhorses)** (Impact: 14.3)
  * `parse` **(Type Conversions)** (Impact: 10.7)
  * `fat_entry_of_nth_cluster` **(Type Conversions)** (Impact: 10.5)
  * `fat_type` **(Compute Cores)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 96`, `args: 35`, `func_start: 25`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 3`, `state_mutation: 5`
* *Architecture:* `api: 22`, `import: 2`
* *Defense:* `safety: 3`, `test: 3`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.682
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01084
  * `Imports (Out-Degree: 1):` core::char::DecodeUtf16Error, crate::disk::AlignedBuffer, crate::disk::Read, crate::disk::Seek, crate::disk::SeekFrom
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `api/src/config.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 8.275)
- **Top Global Matches:** file_cluster_13: 8.275, file_cluster_15: 8.458, file_cluster_0: 8.466
- **Magnitude:** 156.76 | **LOC:** 614 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **3**; blast radius 209.625; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (71.6%), Connectivity (formerly Api Exposure) (59.1%), Guard Balance (formerly Safety Score) (45.1%)
- **Documentation Coverage:** 35.1351% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize` **(Compute Cores)** (Impact: 41.3)
    * *Intent:* /// Tries to deserialize a config byte array that was created using [`Self::serialize`]. /// /// Thi...
  * `serialize` **(Defensive Guards)** (Impact: 14.5)
    * *Intent:* /// Serializes the configuration to a byte array. /// /// This is used by the [`crate::entry_point`]...
  * `random` **(I/O & Config Routines)** (Impact: 10.7)
  * `deserialize` **(Generic / Templated Code)** (Impact: 6.3)
  * `random` **(I/O & Config Routines)** (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 89`, `args: 24`, `func_start: 24`, `class_start: 5`
* *Risk/State:* `state_mutation: 1`, `planned_debt: 5`, `duplicate_logic: 3`
* *Architecture:* `api: 36`, `import: 2`
* *Defense:* `safety: 6`, `doc: 118`, `test: 10`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 209.625
  * `Choke Point (Betweenness):` 0.001466 | `Ripple Effect (Closeness):` 0.217811
  * `Imports (Out-Degree: 1):` crate::concat::*, crate::version_info, self::*
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `uefi/src/main.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.879)
- **Top Global Matches:** file_cluster_5: 5.879, file_cluster_12: 8.315, file_cluster_7: 9.284
- **Magnitude:** 155.28 | **LOC:** 567 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **48**; blast radius 2.527; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.9%), Mutation Surface (formerly State Flux) (50.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.9%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main_inner` **(Many-Argument Workhorses)** (Impact: 26.3)
  * `init_logger` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `create_page_tables` **(Many-Argument Workhorses)** (Impact: 11.9)
    * *Intent:* /// Creates page table abstraction types for both the bootloader and kernel page tables.
  * `load_file_from_disk` **(Many-Argument Workhorses)** (Impact: 10.1)
  * `locate_and_open_protocol` **(Generic / Templated Code)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 154`, `args: 25`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 2`, `state_mutation: 11`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 10`
* *Defense:* `safety: 8`, `doc: 2`, `test: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.527
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` memory_descriptor, bootloader_api::info::FrameBufferInfo, bootloader_boot_config::BootConfig, bootloader_x86_64_common::Kernel, bootloader_x86_64_common::RawFrameBufferInfo, bootloader_x86_64_common::SystemInfo, bootloader_x86_64_common::legacy_memory_region::LegacyFrameAllocator, core::arch::asm...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `common/src/legacy_memory_region.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.602)
- **Top Global Matches:** file_cluster_0: 6.602, file_cluster_15: 7.146, file_cluster_12: 7.835
- **Magnitude:** 143.0 | **LOC:** 596 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **11**; blast radius 5.763; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (50.5%), Guard Balance (formerly Safety Score) (47.9%), Mutation Surface (formerly State Flux) (28.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.9%)
- **Documentation Coverage:** 41.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `construct_memory_map` **(Many-Argument Workhorses)** (Impact: 18.8)
    * *Intent:* /// Converts this type to a boot info memory map. /// /// The memory map is placed in the given `reg...
  * `split_and_add_region` **(Many-Argument Workhorses)** (Impact: 14.0)
  * `allocate_frame` **(Defensive Guards)** (Impact: 11.0)
  * `allocate_frame_from_descriptor` **(Compute Cores)** (Impact: 7.9)
  * `test_multiple_regions` **(I/O & Config Routines)** (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 95`, `args: 31`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`, `planned_debt: 1`
* *Architecture:* `api: 16`, `import: 4`
* *Defense:* `safety: 5`, `doc: 37`, `test: 25`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.763
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.044264
  * `Imports (Out-Degree: 1):` bootloader_api::info::MemoryRegion, bootloader_api::info::MemoryRegionKind, core::cmp, core::mem::MaybeUninit, self::*, x86_64::PhysAddr, x86_64::align_down, x86_64::align_up...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `api/src/info.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.548)
- **Top Global Matches:** file_cluster_0: 5.548, file_cluster_13: 9.096, file_cluster_15: 9.691
- **Magnitude:** 98.96 | **LOC:** 382 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **41** in-repo importer(s); it depends on **3**; blast radius 118.04; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (76.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.4%), Concurrency Surface (formerly Concurrency) (21.4%), Complexity Load (formerly Cognitive Load) (3.8%)
- **Documentation Coverage:** 26.4706% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `as_ref` **(Defensive Guards)** (Impact: 3.1)
    * *Intent:* /// Converts from `&Optional<T>` to `Option<&T>`. /// /// For convenience, this method directly perf...
  * `as_mut` **(Defensive Guards)** (Impact: 3.1)
    * *Intent:* /// Converts from `&mut Optional<T>` to `Option<&mut T>`. /// /// For convenience, this method direc...
  * `from` **(Defensive Guards)** (Impact: 3.1)
  * `from` **(Generic / Templated Code)** (Impact: 3.1)
  * `new` **(State Mutators)** (Impact: 2.4)
    * *Intent:* /// Create a new boot info structure with the given memory map. /// /// The other fields are initial...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 39`, `args: 20`, `func_start: 20`, `class_start: 9`
* *Risk/State:* None
* *Architecture:* `api: 54`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 4`, `doc: 146`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 118.04
  * `Choke Point (Betweenness):` 0.00191 | `Ripple Effect (Closeness):` 0.312195
  * `Imports (Out-Degree: 1):` core::ops, core::slice, crate::config::ApiVersion
  * `Imported By (In-Degree: 41):` (Excluded from Brief to save tokens)

### `src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.643)
- **Top Global Matches:** file_cluster_15: 6.643, file_cluster_12: 7.852, file_cluster_13: 8.214
- **Magnitude:** 96.86 | **LOC:** 236 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **19**; blast radius 21.142; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (84.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.3%)
- **Documentation Coverage:** 29.1667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_uefi_tftp_folder` **(Compute Cores)** (Impact: 15.5)
  * `create_fat_filesystem_image` **(Many-Argument Workhorses)** (Impact: 11.2)
  * `create_bios_image` **(Compute Cores)** (Impact: 10.1)
  * `create_uefi_image` **(Compute Cores)** (Impact: 9.4)
  * `create_uefi_fat_partition` **(Parameter Forwarders)** (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 47`, `args: 15`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`, `unreferenced_by_name: 7`
* *Architecture:* `api: 15`, `import: 8`
* *Defense:* `doc: 21`, `immutability_locks: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.142
  * `Choke Point (Betweenness):` 0.006198 | `Ripple Effect (Closeness):` 0.074332
  * `Imports (Out-Degree: 7):` bios, fat, file_data_source, gpt, mbr, uefi, alloc, anyhow::Context...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `common/src/level_4_entries.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.517)
- **Top Global Matches:** file_cluster_6: 8.517, file_cluster_4: 11.912, file_cluster_8: 16.432
- **Magnitude:** 90.26 | **LOC:** 230 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **24**; blast radius 3.657; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (45.4%), Connectivity (formerly Api Exposure) (37.5%), Mutation Surface (formerly State Flux) (35.5%)
- **Documentation Coverage:** 10.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new` **(Many-Argument Workhorses)** (Impact: 46.7)
    * *Intent:* /// Initializes a new instance. /// /// Marks the statically configured virtual address ranges from ...
  * `get_free_entries` **(Defensive Guards)** (Impact: 10.1)
    * *Intent:* /// Returns the first index of a `num` contiguous unused level 4 entries and marks them as /// used....
  * `get_free_address` **(Many-Argument Workhorses)** (Impact: 7.2)
    * *Intent:* /// Returns a virtual address in one or more unused level 4 entries and marks them as used. /// /// ...
  * `mark_segments` **(Generic / Templated Code)** (Impact: 4.6)
    * *Intent:* /// Marks the virtual address range of all segments as used.
  * `mark_range_as_used` **(Generic / Templated Code)** (Impact: 4.5)
    * *Intent:* /// Marks all p4 entries in the range `[address..address+size)` as used.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 57`, `args: 10`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 3`
* *Architecture:* `api: 5`, `import: 8`
* *Defense:* `safety: 14`, `doc: 20`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.657
  * `Choke Point (Betweenness):` 3.3e-05 | `Ripple Effect (Closeness):` 0.02168
  * `Imports (Out-Degree: 5):` bootloader_api::BootloaderConfig, bootloader_api::config, bootloader_api::info::MemoryRegion, core::alloc::Layout, core::iter::Step, crate::BootInfo, crate::RawFrameBufferInfo, crate::entropy...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `build.rs` (RUST | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.928)
- **Top Global Matches:** file_cluster_7: 6.928, file_cluster_12: 8.515, file_cluster_5: 9.366
- **Magnitude:** 82.78 | **LOC:** 420 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 3.064; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.0%), Concurrency Surface (formerly Concurrency) (62.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_bios_stage_2` **(I/O & Config Routines)** (Impact: 7.3)
  * `build_bios_boot_sector` **(I/O & Config Routines)** (Impact: 7.2)
  * `build_bios_stage_3` **(Annotated & Test Methods)** (Impact: 7.2)
  * `build_bios_stage_4` **(I/O & Config Routines)** (Impact: 7.2)
  * `build_uefi_bootloader` **(Annotated & Test Methods)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *High Risk Execution (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 72`, `args: 21`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 17`
* *Architecture:* `io: 10`, `api: 1`, `concurrency: 12`, `import: 7`
* *Defense:* `safety: 5`, `test: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00813
  * `Imports (Out-Degree: 0):` std::fs::File, std::path::Path, std::path::PathBuf, std::process::Command
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/disk_image.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.597)
- **Top Global Matches:** file_cluster_8: 6.597, file_cluster_6: 17.066, file_cluster_3: 20.086
- **Magnitude:** 75.62 | **LOC:** 184 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 2.527; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.2%), Debt Markers (formerly Tech Debt) (49.6%), Mutation Surface (formerly State Flux) (23.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_disk_image` **(Many-Argument Workhorses)** (Impact: 53.0)
    * *Intent:* /// Creates a bootable disk image from the given bootloader executable.
  * `pad_to_nearest_block_size` **(Compute Cores)** (Impact: 8.5)
  * `from` **(State Mutators)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 37`, `args: 10`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 2`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 2`, `import: 5`
* *Defense:* `safety: 1`, `doc: 10`, `test: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.527
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` anyhow::Context, std::fs, std::fs::OpenOptions, std::io, std::io::Seek, std::io::Write, std::path::Path, std::process::Command...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `common/src/framebuffer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.457)
- **Top Global Matches:** file_cluster_15: 7.457, file_cluster_0: 7.538, file_cluster_12: 7.806
- **Magnitude:** 69.8 | **LOC:** 155 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 3.553; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.7%), Guard Balance (formerly Safety Score) (57.6%), Connectivity (formerly Api Exposure) (49.5%), Concurrency Surface (formerly Concurrency) (29.8%)
- **Documentation Coverage:** 46.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_pixel` **(Many-Argument Workhorses)** (Impact: 9.9)
  * `write_char` **(Compute Cores)** (Impact: 7.8)
    * *Intent:* /// Writes a single char to the framebuffer. Takes care of special control characters, such as /// n...
  * `write_rendered_char` **(Compute Cores)** (Impact: 5.6)
    * *Intent:* /// Prints a rendered char into the framebuffer. /// Updates `self.x_pos`.
  * `write_str` **(Parameter Forwarders)** (Impact: 3.8)
  * `get_char_raster` **(Defensive Guards)** (Impact: 3.3)
    * *Intent:* /// Returns the raster of the given char or the raster of [`font_constants::BACKUP_CHAR`].
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 29`, `args: 13`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 9`
* *Architecture:* `api: 8`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 1`, `doc: 17`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.553
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.029268
  * `Imports (Out-Degree: 1):` bootloader_api::info::FrameBufferInfo, bootloader_api::info::PixelFormat, core::fmt, core::ptr, font_constants::BACKUP_CHAR, noto_sans_mono_bitmap::FontWeight, noto_sans_mono_bitmap::RasterHeight, noto_sans_mono_bitmap::RasterizedChar...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `bios/stage-2/src/vesa.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.559)
- **Top Global Matches:** file_cluster_6: 8.559, file_cluster_8: 13.472, file_cluster_4: 14.17
- **Magnitude:** 68.94 | **LOC:** 237 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 2.682; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (51.7%), Guard Balance (formerly Safety Score) (50.4%), Mutation Surface (formerly State Flux) (20.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_best_mode` **(Many-Argument Workhorses)** (Impact: 34.3)
  * `get_mode` **(Type Conversions)** (Impact: 5.8)
  * `query` **(Generic / Templated Code)** (Impact: 4.2)
  * `query` **(Generic / Templated Code)** (Impact: 1.9)
  * `enable` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 55`, `args: 16`, `func_start: 5`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`
* *Architecture:* `api: 11`, `import: 3`
* *Defense:* `safety: 2`, `doc: 5`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.682
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01084
  * `Imports (Out-Degree: 2):` bootloader_x86_64_bios_common::PixelFormat, core::arch::asm, crate::AlignedArrayBuffer, crate::disk::AlignedBuffer
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bios/stage-2/src/disk.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.829)
- **Top Global Matches:** file_cluster_12: 6.829, file_cluster_5: 7.54, file_cluster_7: 8.496
- **Magnitude:** 59.68 | **LOC:** 118 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 7.103; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (97.7%), Guard Balance (formerly Safety Score) (59.4%), Connectivity (formerly Api Exposure) (59.2%)
- **Documentation Coverage:** 90.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_exact_into` **(Type Conversions)** (Impact: 9.7)
  * `read_exact_at` **(Many-Argument Workhorses)** (Impact: 5.2)
  * `seek` **(Parameter Forwarders)** (Impact: 3.9)
  * `read_exact_at` **(Parameter Forwarders)** (Impact: 2.0)
  * `read_exact_into` **(Parameter Forwarders)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 39`, `args: 11`, `func_start: 10`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`
* *Architecture:* `api: 11`, `import: 1`
* *Defense:* `doc: 1`, `test: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.103
  * `Choke Point (Betweenness):` 0.000133 | `Ripple Effect (Closeness):` 0.026016
  * `Imports (Out-Degree: 1):` crate::dap
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `bios/stage-4/src/main.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.553)
- **Top Global Matches:** file_cluster_5: 6.553, file_cluster_12: 7.047, file_cluster_0: 9.027
- **Magnitude:** 58.38 | **LOC:** 308 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 2.527; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (73.9%), Guard Balance (formerly Safety Score) (55.1%), Mutation Surface (formerly State Flux) (35.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.9%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_start` **(Compute Cores)** (Impact: 18.7)
  * `init_logger` **(Many-Argument Workhorses)** (Impact: 6.7)
  * `detect_rsdp` **(Generic / Templated Code)** (Impact: 4.0)
  * `panic` **(State Mutators)** (Impact: 3.5)
  * `create_page_tables` **(Generic / Templated Code)** (Impact: 3.1)
    * *Intent:* /// Creates page table abstraction types for both the bootloader and kernel page tables.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 73`, `args: 12`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 4`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `safety: 2`, `doc: 1`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.527
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` memory_descriptor, bootloader_api::info::FrameBufferInfo, bootloader_api::info::PixelFormat, bootloader_boot_config::BootConfig, bootloader_boot_config::LevelFilter, bootloader_x86_64_bios_common::BiosFramebufferInfo, bootloader_x86_64_bios_common::BiosInfo, bootloader_x86_64_bios_common::E820MemoryRegion...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bios/stage-2/src/main.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.654)
- **Top Global Matches:** file_cluster_7: 7.654, file_cluster_12: 9.372, file_cluster_5: 9.583
- **Magnitude:** 57.84 | **LOC:** 271 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **24**; blast radius 3.287; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Debt Markers (formerly Tech Debt) (38.4%), Mutation Surface (formerly State Flux) (11.5%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_load_file` **(Many-Argument Workhorses)** (Impact: 19.7)
  * `start` **(Many-Argument Workhorses)** (Impact: 15.9)
  * `split_array_ref` **(Parameter Forwarders)** (Impact: 3.2)
    * *Intent:* /// Taken from https://github.com/rust-lang/rust/blob/e100ec5bc7cd768ec17d75448b29c9ab4a39272b/libra...
  * `load_file` **(Parameter Forwarders)** (Impact: 2.9)
  * `_start` **(State Mutators)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 93`, `args: 8`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 1`, `state_mutation: 4`, `planned_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `safety: 4`, `doc: 5`, `test: 3`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.287
  * `Choke Point (Betweenness):` 0.0004 | `Ripple Effect (Closeness):` 0.00813
  * `Imports (Out-Degree: 8):` dap, disk, fat, memory_map, protected_mode, screen, vesa, bootloader_x86_64_bios_common::BiosFramebufferInfo...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bios/stage-3/src/screen.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.976)
- **Top Global Matches:** file_cluster_12: 6.976, file_cluster_5: 6.977, file_cluster_0: 9.202
- **Magnitude:** 57.76 | **LOC:** 129 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 3.243; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.5%), Guard Balance (formerly Safety Score) (61.4%), Connectivity (formerly Api Exposure) (40.3%), Concurrency Surface (formerly Concurrency) (31.1%)
- **Documentation Coverage:** 86.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_char` **(Compute Cores)** (Impact: 7.7)
  * `write_rendered_char` **(Compute Cores)** (Impact: 5.6)
  * `write_pixel` **(Many-Argument Workhorses)** (Impact: 5.4)
  * `write_str` **(Parameter Forwarders)** (Impact: 3.8)
  * `new` **(Generic / Templated Code)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 32`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 9`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 3`
* *Defense:* `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.243
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.00813
  * `Imports (Out-Degree: 2):` bootloader_x86_64_bios_common::BiosFramebufferInfo, bootloader_x86_64_bios_common::PixelFormat, bootloader_x86_64_bios_common::racy_cell::RacyCell, core::fmt, core::ptr, noto_sans_mono_bitmap::BitmapChar, noto_sans_mono_bitmap::BitmapHeight, noto_sans_mono_bitmap::FontWeight...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/mbr.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 5.357)
- **Top Global Matches:** file_cluster_9: 5.357, file_cluster_16: 11.894, file_cluster_15: 12.077
- **Magnitude:** 49.66 | **LOC:** 101 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 4.324; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (84.5%), Guard Balance (formerly Safety Score) (53.9%), Complexity Load (formerly Cognitive Load) (18.9%), Connectivity (formerly Api Exposure) (18.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_mbr_disk` **(Many-Argument Workhorses)** (Impact: 38.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 25`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 3`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 4`
* *Defense:* `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.324
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.052213
  * `Imports (Out-Degree: 0):` anyhow::Context, mbrman::BOOT_ACTIVE, std::fs, std::fs::File, std::io, std::io::Cursor, std::io::Seek, std::io::SeekFrom...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/fat.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 9.074)
- **Top Global Matches:** file_cluster_9: 9.074, file_cluster_12: 11.873, file_cluster_7: 13.006
- **Magnitude:** 45.38 | **LOC:** 94 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 4.324; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.9%), Guard Balance (formerly Safety Score) (57.9%), Connectivity (formerly Api Exposure) (29.4%), Complexity Load (formerly Cognitive Load) (23.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_files_to_image` **(Compute Cores)** (Impact: 17.3)
  * `create_fat_filesystem` **(Many-Argument Workhorses)** (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 29`, `args: 5`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 4`
* *Architecture:* `io: 1`, `api: 2`, `import: 6`
* *Defense:* `safety: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.324
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.048402
  * `Imports (Out-Degree: 2):` anyhow::Context, crate::KERNEL_FILE_NAME, crate::file_data_source::FileDataSource, fatfs::Dir, std::collections::BTreeMap, std::fs, std::fs::File, std::path::Path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `.github/workflows/ci.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.184)
- **Top Global Matches:** file_cluster_2: 6.184, file_cluster_11: 6.242, file_cluster_15: 6.835
- **Magnitude:** 42.58 | **LOC:** 154 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.527; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.2%), Mutation Surface (formerly State Flux) (23.0%), Concurrency Surface (formerly Concurrency) (18.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.2%)
- **Documentation Coverage:** 91.3043% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Install QEMU (Linux)` **(I/O & Config Routines)** (Impact: 3.1)
    * *Intent:* # install QEMU
  * `Install QEMU (macOS)` **(I/O & Config Routines)** (Impact: 2.4)
  * `Install QEMU (Windows)` **(I/O & Config Routines)** (Impact: 2.3)
  * `Run bootloader common tests` **(I/O & Config Routines)** (Impact: 2.1)
  * `Test with only UEFI feature` **(I/O & Config Routines)** (Impact: 2.1)
    * *Intent:* # test feature gates (only on one OS is enough)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 18`, `args: 5`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 19`
* *Defense:* `doc: 8`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.527
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rust-cache@v2, checkout@v3, typos@v1.0.4, cargo-semver-checks-action@v2, rust-problem-matchers@v1.1.0
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/runner/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.12)
- **Top Global Matches:** file_cluster_5: 7.12, file_cluster_7: 7.662, file_cluster_12: 9.447
- **Magnitude:** 42.52 | **LOC:** 151 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **6**; blast radius 27.228; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Concurrency Surface (formerly Concurrency) (63.7%), Connectivity (formerly Api Exposure) (8.3%), Complexity Load (formerly Cognitive Load) (5.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_qemu` **(Generic / Templated Code)** (Impact: 8.7)
  * `run_test_kernel_internal` **(Defensive Guards)** (Impact: 7.7)
  * `run_test_kernel_on_uefi_pxe` **(Annotated & Test Methods)** (Impact: 2.2)
  * `run_test_kernel_with_config_file` **(State Mutators)** (Impact: 2.0)
  * `run_test_kernel_on_uefi` **(Annotated & Test Methods)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 38`, `args: 10`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 3`, `unreferenced_by_name: 3`
* *Architecture:* `io: 4`, `api: 7`, `concurrency: 5`, `import: 4`
* *Defense:* `safety: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 27.228
  * `Choke Point (Betweenness):` 0.006331 | `Ripple Effect (Closeness):` 0.097561
  * `Imports (Out-Degree: 2):` bootloader::BootConfig, bootloader::DiskImageBuilder, std::io::Read, std::path::Path, std::process::Command, std::process::Stdio
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/gpt.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 4.957)
- **Top Global Matches:** file_cluster_9: 4.957, file_cluster_15: 11.727, file_cluster_16: 11.933
- **Magnitude:** 34.18 | **LOC:** 71 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 4.324; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Mutation Surface (formerly State Flux) (45.6%), Connectivity (formerly Api Exposure) (18.5%), Complexity Load (formerly Cognitive Load) (18.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_gpt_disk` **(Compute Cores)** (Impact: 29.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 17`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.324
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.052213
  * `Imports (Out-Degree: 0):` anyhow::Context, std::fs, std::fs::File, std::io, std::io::Seek, std::path::Path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `.github/workflows/trigger-release/trigger-release.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.537)
- **Top Global Matches:** file_cluster_2: 5.537, file_cluster_17: 6.863, file_cluster_13: 7.34
- **Magnitude:** 33.62 | **LOC:** 39 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.527; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.2%), Complexity Load (formerly Cognitive Load) (51.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 6`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 8`
* *Architecture:* `io: 2`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.527
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` requests, subprocess, toml
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bios/common/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.217)
- **Top Global Matches:** file_cluster_13: 5.217, file_cluster_2: 7.153, file_cluster_0: 7.399
- **Magnitude:** 33.46 | **LOC:** 72 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **1**; blast radius 11.124; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (66.3%), Connectivity (formerly Api Exposure) (15.7%), Complexity Load (formerly Cognitive Load) (5.3%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is_unknown` **(State Mutators)** (Impact: 3.1)
  * `hlt` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`, `args: 2`, `func_start: 2`, `class_start: 5`
* *Risk/State:* `unreferenced_by_name: 2`
* *Architecture:* `api: 28`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.124
  * `Choke Point (Betweenness):` 0.000322 | `Ripple Effect (Closeness):` 0.065041
  * `Imports (Out-Degree: 1):` racy_cell
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `common/src/logger.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.377)
- **Top Global Matches:** file_cluster_5: 7.377, file_cluster_12: 8.317, file_cluster_7: 9.677
- **Magnitude:** 28.6 | **LOC:** 72 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 2.768; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (51.6%), Guard Balance (formerly Safety Score) (47.7%), Complexity Load (formerly Cognitive Load) (4.0%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 55.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new` **(Many-Argument Workhorses)** (Impact: 7.8)
    * *Intent:* /// Create a new instance that logs to the given framebuffer.
  * `log` **(Defensive Guards)** (Impact: 5.7)
  * `force_unlock` **(Defensive Guards)** (Impact: 4.6)
    * *Intent:* /// Force-unlocks the logger to prevent a deadlock. /// /// ## Safety /// This method is not memory ...
  * `enabled` **(State Mutators)** (Impact: 1.9)
  * `flush` **(State Mutators)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 19`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `safety: 4`, `doc: 7`, `sync_locks: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.768
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022584
  * `Imports (Out-Degree: 3):` bootloader_api::info::FrameBufferInfo, conquer_once::spin::OnceCell, core::fmt::Write, crate::framebuffer::FrameBufferWriter, crate::serial::SerialPort, spinning_top::Spinlock
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `bios/boot_sector/src/boot.s` (ASSEMBLY) | Magnitude: 14.74 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 17, args: 16, func_start: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `bios/stage-3/src/screen.rs` (RUST) | Magnitude: 57.76 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 90, structural_boundaries: 32, core_var_decl: 13, args: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/bios/mod.rs` (RUST) | Magnitude: 12.88 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 9, api: 5, doc: 5
- `common/src/framebuffer.rs` (RUST) | Magnitude: 69.8 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 95, structural_boundaries: 29, doc: 17, core_var_decl: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `.github/workflows/ci.yml` (YAML) | Magnitude: 42.58 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 130, func_start: 23, import: 19, structural_boundaries: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `common/src/serial.rs` (RUST) | Magnitude: 10.24 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 7, branch: 3, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `bios/stage-3/src/main.rs` (RUST) | Magnitude: 12.56 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 22, decorators: 8, args: 5

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/lib.rs` -> Churn: **52.29%** | Cog Load: 8.9936% | Debt: 84.1131%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `api/src/config.rs` -> **rezky_nightky** (100.0% isolated ownership) | Magnitude: 156.76
- `uefi/src/main.rs` -> **Spencer** (100.0% isolated ownership) | Magnitude: 155.28
- `common/src/legacy_memory_region.rs` -> **Spencer** (100.0% isolated ownership) | Magnitude: 143.0
- `api/src/info.rs` -> **Burkhard Mittelbach** (100.0% isolated ownership) | Magnitude: 98.96
- `common/src/framebuffer.rs` -> **Spencer** (100.0% isolated ownership) | Magnitude: 69.8

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/lib.rs` -> **Severity: 0.201** (Bridge: 0.0062 * Flux: 32.4464%)
- `common/src/lib.rs` -> **Severity: 0.042** (Bridge: 0.0019 * Flux: 22.1041%)
- `bios/stage-2/src/disk.rs` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 97.7472%)
- `bios/stage-2/src/main.rs` -> **Severity: 0.005** (Bridge: 0.0004 * Flux: 11.5103%)
- `bios/stage-2/src/memory_map.rs` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 71.7751%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `api/src/config.rs` -> **Severity: 9.833** (Embedded: 0.2178 * Error Risk: 45.1463%)
- `tests/runner/src/lib.rs` -> **Severity: 7.805** (Embedded: 0.0976 * Error Risk: 80.0%)
- `src/lib.rs` -> **Severity: 3.95** (Embedded: 0.0743 * Error Risk: 53.1342%)
- `src/mbr.rs` -> **Severity: 2.813** (Embedded: 0.0522 * Error Risk: 53.8757%)
- `src/fat.rs` -> **Severity: 2.803** (Embedded: 0.0484 * Error Risk: 57.9117%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `api/src/lib.rs` -> **Severity: 9670.55** (Blast Radius: 193.411 * Doc Risk: 50.0%)
- `api/src/config.rs` -> **Severity: 7365.195** (Blast Radius: 209.625 * Doc Risk: 35.1351%)
- `api/src/info.rs` -> **Severity: 3124.59** (Blast Radius: 118.04 * Doc Risk: 26.4706%)
- `tests/runner/src/lib.rs` -> **Severity: 2722.8** (Blast Radius: 27.228 * Doc Risk: 100.0%)
- `bios/common/src/lib.rs` -> **Severity: 1112.4** (Blast Radius: 11.124 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1956 call pairs -- scoped 14.4%, unique 0.0%, ambiguous 6.7%, external 78.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 1945 | 14.4% | 0.0% | 6.7% | 78.8% |
| python | 8 | 0.0% | 0.0% | 0.0% | 100.0% |
| assembly | 3 | 0.0% | 0.0% | 0.0% | 100.0% |

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
