# ARCHITECTURAL_BRIEF: alire
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/alire-project/alire.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 559 analyzed artifact(s), 48183 LOC.
- **Load-bearing artifact:** `src/alr/os_linux/os.c` -- 12 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/alr/alr-commands.adb` -- pulls in 56 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/alire/alire-solver.adb` at magnitude 701.8 (structural weight, not risk).
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
| Total Artifacts | 1828 |
| Analyzed Artifacts (Scanned) | 559 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1269 |
| Total LOC | 48183 |
| Volatility Index | 0.932 |
| % Scanned of codebase = | 30.6% |
| Dominant Lang | ADA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4912 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.107 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.2881 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ADA | 472 | 45811 | 84.4% |
| SHELL | 26 | 725 | 4.7% |
| MARKDOWN | 25 | 0 | 4.5% |
| PYTHON | 19 | 1435 | 3.4% |
| PLAINTEXT | 5 | 0 | 0.9% |
| XML | 3 | 0 | 0.5% |
| YAML | 3 | 66 | 0.5% |
| JAVASCRIPT | 2 | 87 | 0.4% |
| C | 2 | 25 | 0.4% |
| POWERSHELL | 1 | 18 | 0.2% |
| DOCKERFILE | 1 | 16 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `1.694`
> **Composition Archetype:** `Mid Flat Project` (z +1.69; from the repo's file-archetype mix)
> **File Composition:** Parameter Forwarders Files 27%, Data / Markup / Trivial 20%, Declarative / Non-Code 18%, Large Core Modules (3) 11%, Compute Cores Files 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 529 | 94.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 30 | 5.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1269*

**Composition by Extension & Reason:**
- `.yaml`: 369x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 811 LOC)
- `.py`: 368x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 346x Excluded (Unsupported Extension: '.toml'), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 48x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 13x Unsupported Format (.undeterminable), 5x Unresolved Ambiguity (No Retainable Structure)
- `.gpr`: 34x Excluded (Unsupported Extension: '.gpr'), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tgz`: 17x Excluded (Explicitly Denied Extension: '.tgz')
- `.yml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 5x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ads`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 21 LOC)
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.adb`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 21 LOC)
- `.sh`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.0 | 9.8 | 5.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 18.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 27.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 13.8 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 68.3 | 2.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 2.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 4.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 93.2 | 100.0 | 100.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 69.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1072 | 255 | 4 | `src/alire/alire-reserved.adb` |
| cleanup | 93 | 27 | 0 | `trash/stress/selftest.sh` |
| guards | 2181 | 348 | 9 | `src/alire/alire-toml_keys.ads` |
| danger | 471 | 135 | 2 | `scripts/alr-completion.bash` |
| concurrency | 91 | 39 | 0 | `src/alire/alire-directories.adb` |
| connectivity | 410 | 261 | 1 | `testsuite/drivers/helpers.py` |
| io | 680 | 92 | 3 | `testsuite/drivers/helpers.py` |
| crypto | 2 | 2 | 0 | `testsuite/drivers/driver/docker_wrapper.py` |
| ipc | 20 | 7 | 0 | `testsuite/run.py` |
| time | 62 | 14 | 0 | `src/alire/alire-test-runner.adb` |
| serialization | 27 | 5 | 0 | `src/alire/alire-github.adb` |
| regex | 73 | 24 | 0 | `scripts/alr-completion.bash` |
| events | 28 | 23 | 0 | `trash/stress/selftest.sh` |
| tests | 158 | 47 | 0 | `testsuite/tests_ada/src/alr_tests-format_duration.adb` |
| docs | 95 | 11 | 0 | `testsuite/drivers/helpers.py` |
| debt | 596 | 128 | 2 | `src/alire/alire-crate_configuration.adb` |
| mutation | 4425 | 290 | 22 | `testsuite/drivers/alr.py` |
| dead_code | 852 | 294 | 4 | `src/alire/alire-solver.adb` |
| credential | 0 | 0 | 0 | - |
| threat | 257 | 78 | 1 | `src/alire/alire-conditional_trees.ads` |
| ml_ai | 10 | 7 | 0 | `scripts/alr-completion.bash` |
| ui | 3 | 1 | 0 | `scripts/alr-completion.bash` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `testsuite/drivers/helpers.py` (Hits: 74)
- `scripts/installer/make-alire-installer` (Hits: 56)
- `scripts/alr-completion.bash` (Hits: 45)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **os.c** (`src/alr/os_linux/os.c`) — 12 inbound connections
2. **alr.py** (`testsuite/drivers/alr.py`) — 6 inbound connections
3. **helpers.py** (`testsuite/drivers/helpers.py`) — 5 inbound connections
4. **functions.sh** (`dev/functions.sh`) — 4 inbound connections
5. **settings.md** (`doc/settings.md`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **alr-commands.adb** (`src/alr/alr-commands.adb`) — 56 outbound dependencies
2. **alire-publish.adb** (`src/alire/alire-publish.adb`) — 35 outbound dependencies
3. **alire-roots.adb** (`src/alire/alire-roots.adb`) — 27 outbound dependencies
4. **alire-test-runner.adb** (`src/alire/alire-test-runner.adb`) — 26 outbound dependencies
5. **alire-releases.ads** (`src/alire/alire-releases.ads`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Preferred_Version` **(Compute Cores)** (@ `src/alire/alire-solver.adb`) -> Impact: **107.3** | LOC: 171
  * *Intent:* ----------------------- -- Preferred_Version -- -----------------------
- `alr_with` **(Many-Argument Workhorses)** (@ `testsuite/drivers/alr.py`) -> Impact: **101.3** | LOC: 66
- `alr_pin` **(Many-Argument Workhorses)** (@ `testsuite/drivers/alr.py`) -> Impact: **86.1** | LOC: 64
- `Load_Source_Archive` **(Many-Argument Workhorses)** (@ `src/alire/alire-origins.adb`) -> Impact: **83.8** | LOC: 155
  * *Intent:* ------------------------- -- Load_Source_Archive -- -------------------------
- `Load_Crate_Section` **(Many-Argument Workhorses)** (@ `src/alire/alire-toml_load.adb`) -> Impact: **73.2** | LOC: 135
  * *Intent:* ------------------------ -- Load_Crate_Section -- ------------------------
- `Update_Dependencies` **(Many-Argument Workhorses)** (@ `src/alire/alire-roots.adb`) -> Impact: **72.3** | LOC: 124
  * *Intent:* ------------------------- -- Update_Dependencies -- -------------------------
- `Report` **(Many-Argument Workhorses)** (@ `src/alr/alr-commands-show.adb`) -> Impact: **71.6** | LOC: 91
  * *Intent:* ------------ -- Report -- ------------
- `Create_One` **(Many-Argument Workhorses)** (@ `src/alire/alire-properties-configurations.adb`) -> Impact: **66.8** | LOC: 123
  * *Intent:* ---------------- -- Create_One -- ----------------
- `Right` **(Compute Cores)** (@ `src/alire/alire-solver.adb`) -> Impact: **66.3** | LOC: 139
- `From_TOML` **(Many-Argument Workhorses)** (@ `src/alire/alire-properties-build_switches.adb`) -> Impact: **62.2** | LOC: 125
  * *Intent:* --------------- -- From_TOML -- ---------------

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/alire` | 296 | 14789.78 | 10.07% | 25.06% |
| `src/alr` | 92 | 2961.32 | 6.87% | 49.85% |
| `testsuite/drivers` | 6 | 1140.56 | 21.76% | 53.0% |
| `testsuite/drivers/driver` | 5 | 316.94 | 50.91% | 7.02% |
| `scripts/python` | 4 | 308.6 | 54.91% | 0.0% |
| `src/templates` | 16 | 258.52 | 0.4% | 0.0% |
| `testsuite/tests_ada/src` | 13 | 147.24 | 3.39% | 33.59% |
| `scripts/installer` | 3 | 132.44 | 58.8% | 33.33% |
| `src/alire/os_windows` | 3 | 129.12 | 8.41% | 37.87% |
| `testsuite` | 9 | 93.86 | 10.61% | 8.82% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `trash/stress/selftest.sh` -> **100.0%** Exposure
- `testsuite/drivers/builds.py` -> **99.9996%** Exposure
- `testsuite/tests_ada/src/alr_tests-string_utils.adb` -> **99.9955%** Exposure
- `src/alire/alire-properties-platform.ads` -> **99.9934%** Exposure
- `src/alire/alire-roots-optional.ads` -> **99.9915%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `scripts/alr-completion.bash` -> **100.0%** Exposure
- `scripts/python/check_finalize_exceptions.py` -> **100.0%** Exposure
- `scripts/python/separate-origins.py` -> **100.0%** Exposure
- `scripts/python/split-crates.py` -> **100.0%** Exposure
- `testsuite/drivers/alr.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/alire/alire-origins.ads` -> **14** Orphaned Functions | **0** Duplicates
- `src/alire/alire-properties-platform.ads` -> **12** Orphaned Functions | **0** Duplicates
- `src/alire/alire-solutions.adb` -> **12** Orphaned Functions | **0** Duplicates
- `testsuite/drivers/asserts.py` -> **9** Orphaned Functions | **0** Duplicates
- `testsuite/drivers/builds.py` -> **7** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `1850` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/alire/alire-solver.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 701.8 | **LOC:** 2325 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.1%), Mutation Surface (formerly State Flux) (36.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Preferred_Version` **(Compute Cores)** (Impact: 107.3)
    * *Intent:* ----------------------- -- Preferred_Version -- -----------------------
  * `Right` **(Compute Cores)** (Impact: 66.3)
  * `Compare_Attempted_Dependencies` **(I/O & Config Routines)** (Impact: 35.1)
    * *Intent:* ------------------------------------ -- Compare_Attempted_Dependencies -- --------------------------...
  * `Include` **(Compute Cores)** (Impact: 29.3)
    * *Intent:* ------------- -- Include -- -------------
  * `Check_Release` **(Many-Argument Workhorses)** (Impact: 28.1)
    * *Intent:* ------------------- -- Check_Release -- -------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 366`, `structural_boundaries: 454`, `args: 34`, `func_start: 53`
* *Risk/State:* `state_mutation: 34`, `dead_code: 17`, `planned_debt: 8`, `fragile_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 2`, `import: 15`
* *Defense:* `safety: 6`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Containers, Ada.Containers.Indefinite_Ordered_Sets, Alire.Containers, Alire.Dependencies.States, Alire.Milestones, Alire.Optional, Alire.Platforms.Current, Alire.Releases.Containers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `testsuite/drivers/alr.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 643.98 | **LOC:** 767 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **13**; blast radius 6.666; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (96.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 36.7647% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `alr_with` **(Many-Argument Workhorses)** (Impact: 101.3)
  * `alr_pin` **(Many-Argument Workhorses)** (Impact: 86.1)
  * `init_local_crate` **(Many-Argument Workhorses)** (Impact: 20.0)
  * `prepare_indexes` **(Many-Argument Workhorses)** (Impact: 19.6)
    * *Intent:* """ Populate alr's config directory with the provided indexes. :param str config_dir: Configuration ...
  * `run_alr` **(Many-Argument Workhorses)** (Impact: 18.5)
    * *Intent:* """ Run "alr" with the given arguments. :param bool complain_on_error: If true and the subprocess ex...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 67 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 223
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 113`, `args: 35`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 89`, `fragile_debt: 1`
* *Architecture:* `io: 41`, `api: 34`, `import: 13`
* *Defense:* `safety: 4`, `doc: 30`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.666
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011989
  * `Imports (Out-Degree: 1):` e3.fs, e3.os.process, e3.testsuite.driver.classic, json, os, os.path, pexpect, platform...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/alire/alire-roots.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 578.56 | **LOC:** 2181 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.3%), Complexity Load (formerly Cognitive Load) (13.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Update_Dependencies` **(Many-Argument Workhorses)** (Impact: 72.3)
    * *Intent:* ------------------------- -- Update_Dependencies -- -------------------------
  * `Call_Gprbuild` **(Compute Cores)** (Impact: 38.5)
    * *Intent:* ------------------- -- Call_Gprbuild -- -------------------
  * `Sync_From_Manifest` **(Many-Argument Workhorses)** (Impact: 25.3)
    * *Intent:* ------------------------ -- Sync_From_Manifest -- ------------------------
  * `Add_Link_Pin` **(Compute Cores)** (Impact: 25.1)
    * *Intent:* ------------------ -- Add_Link_Pin -- ------------------
  * `Direct_Withs` **(Compute Cores)** (Impact: 19.8)
    * *Intent:* ------------------ -- Direct_Withs -- ------------------
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 433`, `args: 78`, `func_start: 75`
* *Risk/State:* `state_mutation: 11`, `dead_code: 9`, `unreferenced_by_name: 7`
* *Architecture:* `io: 13`, `concurrency: 1`, `import: 34`
* *Defense:* `safety: 7`, `test: 2`, `immutability_locks: 30`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Directories, Ada.Unchecked_Deallocation, Alire.Conditional, Alire.Dependencies.Containers, Alire.Environment.Loading, Alire.Errors, Alire.Flags, Alire.Install...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-properties-configurations.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 443.98 | **LOC:** 946 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (91.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Create_One` **(Many-Argument Workhorses)** (Impact: 66.8)
    * *Intent:* ---------------- -- Create_One -- ----------------
  * `Valid` **(Compute Cores)** (Impact: 50.7)
    * *Intent:* ----------- -- Valid -- -----------
  * `To_C_Declaration` **(Compute Cores)** (Impact: 23.5)
    * *Intent:* ---------------------- -- To_C_Declaration -- ----------------------
  * `To_TOML` **(Compute Cores)** (Impact: 20.0)
  * `To_Ada_Declaration` **(Compute Cores)** (Impact: 18.3)
    * *Intent:* ------------------------ -- To_Ada_Declaration -- ------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 251`, `args: 24`, `func_start: 25`
* *Risk/State:* `state_mutation: 35`, `dead_code: 5`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 1`, `import: 6`
* *Defense:* `safety: 6`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AAA.Enum_Tools, Ada.Characters.Handling, Ada.Strings.Unbounded, Alire.Utils.Did_You_Mean, Alire.Utils.YAML, TOML
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-solutions.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 437.1 | **LOC:** 1562 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.8%), Debt Markers (formerly Tech Debt) (33.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Print_Versions` **(Many-Argument Workhorses)** (Impact: 38.6)
    * *Intent:* -------------------- -- Print_Versions -- --------------------
  * `Visit` **(Compute Cores)** (Impact: 37.8)
    * *Intent:* ----------- -- Visit -- -----------
  * `Print_Pins` **(Compute Cores)** (Impact: 20.1)
    * *Intent:* ---------------- -- Print_Pins -- ----------------
  * `Print_Tree` **(Many-Argument Workhorses)** (Impact: 18.0)
    * *Intent:* ---------------- -- Print_Tree -- ----------------
  * `Composition` **(Compute Cores)** (Impact: 16.3)
    * *Intent:* ----------------- -- Composition -- -----------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 357`, `args: 69`, `func_start: 71`
* *Risk/State:* `state_mutation: 16`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `api: 1`, `import: 12`
* *Defense:* `safety: 1`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Alire.Crates, Alire.Dependencies.Diffs, Alire.Dependencies.Graphs, Alire.Errors, Alire.Index, Alire.Root, Alire.Settings.Builtins, Alire.Solutions.Diffs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-origins.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 424.94 | **LOC:** 980 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.3%), Mutation Surface (formerly State Flux) (37.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Load_Source_Archive` **(Many-Argument Workhorses)** (Impact: 83.8)
    * *Intent:* ------------------------- -- Load_Source_Archive -- -------------------------
  * `Image` **(Compute Cores)** (Impact: 24.1)
    * *Intent:* ----------- -- Image -- ----------- -- Note: for a conditional origin this falls back to -- Bin_Arch...
  * `New_VCS` **(Many-Argument Workhorses)** (Impact: 22.0)
    * *Intent:* ------------- -- New_VCS -- -------------
  * `To_TOML` **(Compute Cores)** (Impact: 19.4)
    * *Intent:* ------------- -- To_TOML -- -------------
  * `From_TOML` **(Compute Cores)** (Impact: 17.8)
    * *Intent:* --------------- -- From_TOML -- ---------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 215`, `args: 50`, `func_start: 47`
* *Risk/State:* `state_mutation: 15`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 3`, `import: 11`
* *Defense:* `safety: 8`, `test: 1`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AAA.Strings, Ada.Directories, Alire.Features, Alire.Loading, Alire.Origins.Deployers.System, Alire.Platforms.Current, Alire.Root, Alire.URI...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-publish.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 398.78 | **LOC:** 1510 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.4%), Debt Markers (formerly Tech Debt) (10.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Check_Release` **(Many-Argument Workhorses)** (Impact: 48.7)
    * *Intent:* ------------------- -- Check_Release -- ------------------- -- Checks the presence of recommended/ma...
  * `Remote_Origin` **(Many-Argument Workhorses)** (Impact: 40.6)
    * *Intent:* ------------------- -- Remote_Origin -- -------------------
  * `Generate_Index_Manifest` **(Compute Cores)** (Impact: 31.0)
    * *Intent:* -- Bind the user manifest with the origin TOML object and create the index -- manifest.
  * `Infer_Remote` **(Many-Argument Workhorses)** (Impact: 30.9)
    * *Intent:* -- Return the name of the remote to use as the published origin. -- -- Raises Checked_Error if the c...
  * `Step_Description` **(Compute Cores)** (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 229`, `args: 41`, `func_start: 36`
* *Risk/State:* `state_mutation: 4`, `dead_code: 8`, `unreferenced_by_name: 4`
* *Architecture:* `io: 13`, `import: 36`
* *Defense:* `safety: 7`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AAA.Strings, Ada.Directories, Ada.Text_IO, Alire.Crates, Alire.Environment, Alire.Errors, Alire.GitHub, Alire.Hashes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-releases.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 382.2 | **LOC:** 1440 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.5%), Complexity Load (formerly Cognitive Load) (19.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `To_TOML` **(Compute Cores)** (Impact: 37.5)
    * *Intent:* ------------- -- To_TOML -- -------------
  * `Create_Authoritative_Manifest` **(Compute Cores)** (Impact: 33.5)
    * *Intent:* ----------------------------------- -- Create_Authoritative_Manifest -- ----------------------------...
  * `From_TOML` **(Many-Argument Workhorses)** (Impact: 22.1)
    * *Intent:* --------------- -- From_TOML -- ---------------
  * `Project_Files` **(Many-Argument Workhorses)** (Impact: 15.8)
    * *Intent:* ------------------- -- Project_Files -- -------------------
  * `Release_Path` **(I/O & Config Routines)** (Impact: 15.4)
    * *Intent:* ------------------ -- Release_Path -- ------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 376`, `args: 51`, `func_start: 55`
* *Risk/State:* `state_mutation: 17`, `dead_code: 3`, `unreferenced_by_name: 5`
* *Architecture:* `io: 6`, `import: 23`
* *Defense:* `safety: 5`, `test: 2`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Directories, Ada.Strings.Fixed, Ada.Text_IO, Alire.Crates, Alire.Defaults, Alire.Directories, Alire.Errors, Alire.Flags...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-crate_configuration.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 379.3 | **LOC:** 1064 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.6%), Mutation Surface (formerly State Flux) (17.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Generate_GPR_Config` **(Many-Argument Workhorses)** (Impact: 33.2)
    * *Intent:* ------------------------- -- Generate_GPR_Config -- -------------------------
  * `Set_Profile` **(Compute Cores)** (Impact: 31.5)
    * *Intent:* ----------------- -- Set_Profile -- -----------------
  * `Make_Switches_Map` **(Many-Argument Workhorses)** (Impact: 28.4)
    * *Intent:* ----------------------- -- Make_Switches_Map -- -----------------------
  * `Generate_Ada_Config` **(Many-Argument Workhorses)** (Impact: 25.5)
    * *Intent:* ------------------------- -- Generate_Ada_Config -- -------------------------
  * `Generate_C_Config` **(Many-Argument Workhorses)** (Impact: 25.4)
    * *Intent:* ----------------------- -- Generate_C_Config -- -----------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 216`, `args: 31`, `func_start: 32`
* *Risk/State:* `state_mutation: 16`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 2`, `import: 20`
* *Defense:* `safety: 2`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AAA.Enum_Tools, AAA.Strings, Ada.Directories, Ada.Strings.Unbounded, Ada.Text_IO, Alire.Containers, Alire.Directories, Alire.Origins...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-directories.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 361.34 | **LOC:** 1198 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.8%), Mutation Surface (formerly State Flux) (44.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Report_Remaining` **(I/O & Config Routines)** (Impact: 17.3)
    * *Intent:* ---------------------- -- Report_Remaining -- ----------------------
  * `Next_Name` **(Compute Cores)** (Impact: 17.2)
    * *Intent:* --------------- -- Next_Name -- ---------------
  * `Copy` **(Compute Cores)** (Impact: 15.9)
    * *Intent:* ---------- -- Copy -- ----------
  * `Check` **(Compute Cores)** (Impact: 15.2)
    * *Intent:* ----------- -- Check -- -----------
  * `Ensure_Deletable_Item` **(Compute Cores)** (Impact: 13.7)
    * *Intent:* --------------------------- -- Ensure_Deletable_Item -- ---------------------------
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 18 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 273`, `args: 45`, `func_start: 47`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 20`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 18`, `concurrency: 5`, `import: 16`
* *Defense:* `safety: 12`, `sync_locks: 4`, `immutability_locks: 20`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Numerics.Discrete_Random, Ada.Real_Time, Ada.Unchecked_Conversion, Ada.Unchecked_Deallocation, Alire.OS_Lib.Subprocess, Alire.Paths, Alire.Platforms.Current, Alire.Platforms.Folders...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-vcss-git.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 329.66 | **LOC:** 921 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.6%), Mutation Surface (formerly State Flux) (10.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Push` **(Many-Argument Workhorses)** (Impact: 34.8)
    * *Intent:* ---------- -- Push -- ----------
  * `Clone_Branch` **(Many-Argument Workhorses)** (Impact: 34.1)
    * *Intent:* ------------------ -- Clone_Branch -- ------------------
  * `Branch_Remote` **(Many-Argument Workhorses)** (Impact: 25.4)
  * `Dirty_Files` **(Many-Argument Workhorses)** (Impact: 24.4)
    * *Intent:* ----------------- -- Dirty_Files -- -----------------
  * `Remote_Commit` **(Many-Argument Workhorses)** (Impact: 22.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 222`, `args: 32`, `func_start: 33`
* *Risk/State:* `state_mutation: 10`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `import: 13`
* *Defense:* `safety: 7`, `test: 5`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Containers, Ada.Directories, Alire.Directories, Alire.Errors, Alire.OS_Lib.Subprocess, Alire.URI, Alire.Utils.Tools, Alire.Utils.User_Input.Query_Config...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `testsuite/drivers/helpers.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 319.92 | **LOC:** 616 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **15**; blast radius 5.186; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 43.5294% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `distribution` **(Compute Cores)** (Impact: 16.8)
  * `contents` **(Defensive Guards)** (Impact: 12.6)
    * *Intent:* # Return the entries (sorted) under a given folder, both folders and files # Optionally, return only...
  * `check_line_in` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* # Check line appears in file """ Assert that the `filename` text file contains at least one line tha...
  * `testing_find_test` **(Generic / Templated Code)** (Impact: 7.5)
    * *Intent:* """ Return the test entry named `name` from a list of JSON test entries, or raise AssertionError lis...
  * `enable` **(Stateful Encapsulated Methods)** (Impact: 5.7)
    * *Intent:* """ Enable mocking for the command. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 147`, `args: 46`, `func_start: 46`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 7`, `state_mutation: 58`, `fragile_debt: 1`
* *Architecture:* `io: 74`, `api: 42`, `import: 15`
* *Defense:* `safety: 8`, `doc: 35`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.186
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.00967
  * `Imports (Out-Degree: 2):` drivers.alr, fcntl, hashlib, json, os, pathlib, platform, re...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/alire/alire-toolchains.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 316.12 | **LOC:** 873 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.2%), Concurrency Surface (formerly Concurrency) (34.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Detect` **(Compute Cores)** (Impact: 51.6)
    * *Intent:* ------------ -- Detect -- ------------
  * `Set_Up` **(Compute Cores)** (Impact: 48.3)
    * *Intent:* ------------ -- Set_Up -- ------------
  * `Add_Choice` **(Many-Argument Workhorses)** (Impact: 36.3)
    * *Intent:* ---------------- -- Add_Choice -- ----------------
  * `Pick_Up_Tool` **(Compute Cores)** (Impact: 18.0)
    * *Intent:* ------------------ -- Pick_Up_Tool -- ------------------
  * `Remove` **(Compute Cores)** (Impact: 14.7)
    * *Intent:* ------------ -- Remove -- ------------
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 11
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 164`, `args: 21`, `func_start: 27`
* *Risk/State:* `state_mutation: 6`, `dead_code: 4`, `unreferenced_by_name: 3`
* *Architecture:* `io: 5`, `concurrency: 6`, `import: 17`
* *Defense:* `safety: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AAA.Text_IO, Ada.Containers.Indefinite_Vectors, Ada.Directories, Alire.Cache, Alire.Directories, Alire.Index, Alire.Manifest, Alire.Origins.Deployers.System...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-conditional_trees.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 279.3 | **LOC:** 689 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.6%), Debt Markers (formerly Tech Debt) (18.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Print` **(Many-Argument Workhorses)** (Impact: 40.0)
  * `Flatten` **(Compute Cores)** (Impact: 29.9)
    * *Intent:* ------------- -- Flatten -- ------------- -- Remove redundant and/or subtrees by merging upwards.
  * `Visit` **(Compute Cores)** (Impact: 15.5)
  * `Tree_TOML_Add` **(Many-Argument Workhorses)** (Impact: 15.5)
    * *Intent:* ------------------- -- Tree_TOML_Add -- -------------------
  * `Enumerate` **(Compute Cores)** (Impact: 13.9)
    * *Intent:* --------------- -- Enumerate -- ---------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 210`, `args: 43`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 5`
* *Architecture:* `import: 2`
* *Defense:* `safety: 1`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Containers.Indefinite_Ordered_Maps, Alire.TOML_Adapters
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-test-runner.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 253.04 | **LOC:** 1024 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.8%), Mutation Surface (formerly State Flux) (44.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Run` **(Many-Argument Workhorses)** (Impact: 24.5)
    * *Intent:* --------- -- Run -- ---------
  * `Text` **(Compute Cores)** (Impact: 15.1)
  * `Put_Progress` **(I/O & Config Routines)** (Impact: 13.2)
    * *Intent:* ------------------ -- Put_Progress -- ------------------
  * `Fail` **(Compute Cores)** (Impact: 12.3)
    * *Intent:* ---------- -- Fail -- ----------
  * `Diagnose` **(Compute Cores)** (Impact: 9.7)
    * *Intent:* -------------- -- Diagnose -- --------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 212`, `args: 34`, `func_start: 37`
* *Risk/State:* `state_mutation: 21`, `dead_code: 1`, `planned_debt: 4`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 26`
* *Defense:* `safety: 2`, `immutability_locks: 35`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AAA.Enum_Tools, Ada.Calendar, Ada.Containers.Indefinite_Ordered_Maps, Ada.Containers.Indefinite_Vectors, Ada.Exceptions, Ada.Strings.Fixed, Ada.Strings.Unbounded, Ada.Text_IO...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-properties-build_switches.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 232.42 | **LOC:** 397 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `From_TOML` **(Many-Argument Workhorses)** (Impact: 62.2)
    * *Intent:* --------------- -- From_TOML -- ---------------
  * `From_TOML` **(Compute Cores)** (Impact: 20.9)
    * *Intent:* --------------- -- From_TOML -- ---------------
  * `Apply` **(Compute Cores)** (Impact: 18.7)
    * *Intent:* ----------- -- Apply -- -----------
  * `From_TOML` **(Defensive Guards)** (Impact: 10.0)
    * *Intent:* --------------- -- From_TOML -- ---------------
  * `Apply` **(Compute Cores)** (Impact: 5.8)
    * *Intent:* ----------- -- Apply -- -----------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 109`, `args: 12`, `func_start: 12`
* *Risk/State:* `state_mutation: 33`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `import: 3`
* *Defense:* `safety: 3`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Alire.TOML_Keys, Alire.Utils.Did_You_Mean, TOML
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alr/alr-commands-show.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 211.8 | **LOC:** 484 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.1%), Debt Markers (formerly Tech Debt) (14.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Report` **(Many-Argument Workhorses)** (Impact: 71.6)
    * *Intent:* ------------ -- Report -- ------------
  * `Report_Externals` **(Compute Cores)** (Impact: 42.7)
    * *Intent:* ---------------------- -- Report_Externals -- ----------------------
  * `Validate` **(Compute Cores)** (Impact: 33.7)
    * *Intent:* -------------- -- Validate -- --------------
  * `Execute` **(Compute Cores)** (Impact: 15.8)
  * `Find_Target_Release` **(Many-Argument Workhorses)** (Impact: 12.5)
    * *Intent:* ------------------------- -- Find_Target_Release -- ------------------------- -- May raise Alire.Que...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 77`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 3`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `import: 15`
* *Defense:* `safety: 3`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Containers, Alire.Conditional, Alire.Dependencies, Alire.Formatting, Alire.Index.Search, Alire.Milestones, Alire.Platforms.Current, Alire.Releases.Containers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-index_on_disk-loading.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 211.1 | **LOC:** 652 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.6%), Mutation Surface (formerly State Flux) (58.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Adjust_Priorities` **(Compute Cores)** (Impact: 36.7)
    * *Intent:* ----------------------- -- Adjust_Priorities -- -----------------------
  * `Load` **(Many-Argument Workhorses)** (Impact: 31.8)
    * *Intent:* ---------- -- Load -- ----------
  * `Load_All` **(Many-Argument Workhorses)** (Impact: 20.4)
    * *Intent:* -------------- -- Load_All -- --------------
  * `Check_One` **(Compute Cores)** (Impact: 19.0)
    * *Intent:* --------------- -- Check_One -- ---------------
  * `Actually_Add` **(Compute Cores)** (Impact: 14.9)
    * *Intent:* ------------------ -- Actually_Add -- ------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 169`, `args: 17`, `func_start: 17`
* *Risk/State:* `state_mutation: 15`, `dead_code: 3`, `unreferenced_by_name: 3`
* *Architecture:* `io: 7`, `import: 15`
* *Defense:* `safety: 4`, `test: 3`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Directories, Ada.Text_IO, Alire.Containers, Alire.Index, Alire.Index_On_Disk.Updates, Alire.Platforms.Current, Alire.Provides, Alire.Settings.Builtins...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-os_lib-subprocess.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 210.12 | **LOC:** 541 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (86.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Token_Finish` **(I/O & Config Routines)** (Impact: 37.6)
  * `Checked_Spawn` **(Many-Argument Workhorses)** (Impact: 23.5)
    * *Intent:* ------------------- -- Checked_Spawn -- -------------------
  * `Dim` **(Compute Cores)** (Impact: 16.6)
    * *Intent:* --------- -- Dim -- ---------
  * `Spawn_Raw` **(Compute Cores)** (Impact: 10.2)
    * *Intent:* --------------- -- Spawn_Raw -- ---------------
  * `Read_Output` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* ----------------- -- Read_Output -- -----------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 118`, `args: 20`, `func_start: 18`
* *Risk/State:* `state_mutation: 18`, `unreferenced_by_name: 4`
* *Architecture:* `import: 8`
* *Defense:* `safety: 3`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Strings.Maps, Ada.Text_IO, Alire.Directories, Alire.Platforms.Current, AnsiAda, CLIC.TTY, GNAT.IO, GNAT.OS_Lib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/python/split-crates.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 206.22 | **LOC:** 185 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.69; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (94.8%), Complexity Load (formerly Cognitive Load) (83.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_release` **(Many-Argument Workhorses)** (Impact: 33.7)
  * `fix_ver` **(Compute Cores)** (Impact: 14.7)
    * *Intent:* # Ensure the version has major.minor.patch numbers, for regularity, and that pre-release/build info ...
  * `fix_order` **(Defensive Guards)** (Impact: 10.6)
  * `is_index` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* # Look for an "index.toml" file that contains a matching 'version = "x.x"' target = os.path.join(pat...
  * `migrate` **(Compute Cores)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 36`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 31`
* *Architecture:* `io: 18`, `api: 9`, `import: 5`
* *Defense:* `safety: 11`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` copy, os, pathlib, re, rtoml
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-toml_adapters.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 204.72 | **LOC:** 503 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.9%), Concurrency Surface (formerly Concurrency) (43.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Print` **(Compute Cores)** (Impact: 37.2)
  * `Report_Extra_Keys` **(Compute Cores)** (Impact: 14.0)
    * *Intent:* ----------------------- -- Report_Extra_Keys -- -----------------------
  * `Pop_Expr` **(Compute Cores)** (Impact: 11.1)
    * *Intent:* -------------- -- Pop_Expr -- --------------
  * `Pop` **(Compute Cores)** (Impact: 10.8)
    * *Intent:* --------- -- Pop -- ---------
  * `Image` **(Defensive Guards)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 174`, `args: 28`, `func_start: 28`
* *Risk/State:* `state_mutation: 7`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `concurrency: 3`, `import: 1`
* *Defense:* `safety: 4`, `test: 1`, `immutability_locks: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Alire.Utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-settings-edit.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 202.74 | **LOC:** 431 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (77.8%), Guard Balance (formerly Safety Score) (63.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Valid_Builtin` **(Many-Argument Workhorses)** (Impact: 61.9)
    * *Intent:* ------------------- -- Valid_Builtin -- -------------------
  * `Location` **(Compute Cores)** (Impact: 21.1)
    * *Intent:* -------------- -- Location -- --------------
  * `Set_Globally` **(Compute Cores)** (Impact: 11.1)
    * *Intent:* ------------------ -- Set_Globally -- ------------------
  * `Set_Locally` **(Compute Cores)** (Impact: 11.0)
    * *Intent:* ----------------- -- Set_Locally -- -----------------
  * `Set` **(Compute Cores)** (Impact: 9.5)
    * *Intent:* --------- -- Set -- ---------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 100`, `args: 12`, `func_start: 17`
* *Risk/State:* `state_mutation: 11`, `planned_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 2`, `import: 12`
* *Defense:* `safety: 1`, `test: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Directories, Ada.Text_IO, Alire.Environment, Alire.Features, Alire.Paths, Alire.Platforms.Current, Alire.Platforms.Folders, Alire.Settings.Builtins...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-user_pins.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 197.22 | **LOC:** 742 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.6%), Mutation Surface (formerly State Flux) (29.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Update` **(Compute Cores)** (Impact: 37.9)
    * *Intent:* ------------ -- Update -- ------------
  * `Image` **(Compute Cores)** (Impact: 21.5)
    * *Intent:* ----------- -- Image -- -----------
  * `Load_Remote` **(I/O & Config Routines)** (Impact: 18.1)
    * *Intent:* ----------------- -- Load_Remote -- -----------------
  * `To_TOML` **(Compute Cores)** (Impact: 15.0)
    * *Intent:* ------------- -- To_TOML -- -------------
  * `Path` **(Compute Cores)** (Impact: 10.6)
    * *Intent:* ---------- -- Path -- ----------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 133`, `args: 18`, `func_start: 20`
* *Risk/State:* `state_mutation: 12`, `dead_code: 1`, `unreferenced_by_name: 6`
* *Architecture:* `io: 8`, `api: 1`, `import: 11`
* *Defense:* `safety: 3`, `test: 3`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AAA.Strings, Ada.Directories, Alire.Directories, Alire.Errors, Alire.Origins, Alire.Roots.Optional, Alire.Utils.TTY, Alire.Utils.User_Input...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-solutions-diffs.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 189.58 | **LOC:** 571 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.3%), Debt Markers (formerly Tech Debt) (43.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Icon` **(Compute Cores)** (Impact: 37.0)
    * *Intent:* ---------- -- Icon -- ----------
  * `Warn_Unsatisfiable_GNAT_External` **(I/O & Config Routines)** (Impact: 36.9)
    * *Intent:* -------------------------------------- -- Warn_Unsatisfiable_GNAT_External -- ----------------------...
  * `Pinned_Or_Unpinned` **(Compute Cores)** (Impact: 15.2)
    * *Intent:* ------------------------ -- Pinned_Or_Unpinned -- ------------------------
  * `Missing_Releases` **(I/O & Config Routines)** (Impact: 10.6)
    * *Intent:* ---------------------- -- Missing_Releases -- ----------------------
  * `Transitivity_Changed` **(I/O & Config Routines)** (Impact: 9.9)
    * *Intent:* -------------------------- -- transitivity_changed -- --------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 97`, `args: 9`, `func_start: 22`
* *Risk/State:* `state_mutation: 5`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `concurrency: 2`, `import: 6`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AAA.Strings, Alire.Origins, Alire.Toolchains, Alire.User_Pins, Alire.Utils.TTY, Alire.Utils.Tables
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/alire/alire-index.adb` (ADA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 182.98 | **LOC:** 452 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.69; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.7%), Debt Markers (formerly Tech Debt) (24.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Releases_Satisfying` **(Many-Argument Workhorses)** (Impact: 44.3)
    * *Intent:* ------------------------- -- Releases_Satisfying -- -------------------------
  * `Detect_Externals` **(Compute Cores)** (Impact: 32.6)
    * *Intent:* ---------------------- -- Detect_Externals -- ----------------------
  * `Add` **(Compute Cores)** (Impact: 17.0)
    * *Intent:* -- During on-demand crate loading, we need to know which crates also -- provide the requested crate....
  * `Exists` **(Compute Cores)** (Impact: 12.7)
    * *Intent:* ------------ -- Exists -- ------------
  * `Find` **(Compute Cores)** (Impact: 12.7)
    * *Intent:* ---------- -- Find -- ----------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 119`, `args: 12`, `func_start: 15`
* *Risk/State:* `state_mutation: 2`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `import: 6`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.69
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ada.Containers.Indefinite_Ordered_Maps, Ada.Containers.Indefinite_Ordered_Sets, Alire.Containers, Alire.Index_On_Disk.Loading, Alire.Publish, Alire.Utils.TTY
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `scripts/alr-completion.bash` -> Churn: **100.0%** | Cog Load: 85.5422% | Debt: 0.0%
- `scripts/aptdetect` -> Churn: **100.0%** | Cog Load: 69.8465% | Debt: 0.0%
- `scripts/installer/make-alire-installer` -> Churn: **100.0%** | Cog Load: 94.4634% | Debt: 0.0%
- `scripts/verify-pins.sh` -> Churn: **100.0%** | Cog Load: 54.9834% | Debt: 0.0%
- `support/embedder/embedder.sh` -> Churn: **100.0%** | Cog Load: 68.5201% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/alire/alire-solver.adb` -> **Seb M'Caw** (100.0% isolated ownership) | Magnitude: 701.8
- `testsuite/drivers/alr.py` -> **Seb M'Caw** (100.0% isolated ownership) | Magnitude: 643.98
- `src/alire/alire-roots.adb` -> **Seb M'Caw** (100.0% isolated ownership) | Magnitude: 578.56
- `src/alire/alire-properties-configurations.adb` -> **Seb M'Caw** (100.0% isolated ownership) | Magnitude: 443.98
- `src/alire/alire-solutions.adb` -> **Seb M'Caw** (100.0% isolated ownership) | Magnitude: 437.1

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `testsuite/drivers/driver/base_driver.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `testsuite/drivers/helpers.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9995%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `testsuite/drivers/alr.py` -> **Severity: 1.151** (Embedded: 0.012 * Error Risk: 95.9841%)
- `testsuite/drivers/helpers.py` -> **Severity: 0.908** (Embedded: 0.0097 * Error Risk: 93.9479%)
- `dev/functions.sh` -> **Severity: 0.567** (Embedded: 0.0071 * Error Risk: 79.873%)
- `testsuite/drivers/driver/base_driver.py` -> **Severity: 0.539** (Embedded: 0.0057 * Error Risk: 94.7705%)
- `testsuite/drivers/driver/python_script.py` -> **Severity: 0.169** (Embedded: 0.0018 * Error Risk: 94.9925%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/alr/os_linux/os.c` -> **Severity: 1799.3** (Blast Radius: 17.993 * Doc Risk: 100.0%)
- `dev/functions.sh` -> **Severity: 743.7** (Blast Radius: 7.437 * Doc Risk: 100.0%)
- `testsuite/drivers/driver/base_driver.py` -> **Severity: 339.8** (Blast Radius: 3.398 * Doc Risk: 100.0%)
- `testsuite/drivers/alr.py` -> **Severity: 245.073** (Blast Radius: 6.666 * Doc Risk: 36.7647%)
- `scripts/python/alire/index.py` -> **Severity: 240.8** (Blast Radius: 2.408 * Doc Risk: 100.0%)

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
