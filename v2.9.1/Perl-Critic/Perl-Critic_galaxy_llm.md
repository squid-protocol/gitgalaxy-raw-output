# ARCHITECTURAL_BRIEF: Perl-Critic
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Perl-Critic/Perl-Critic.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 82 analyzed artifact(s), 9457 LOC.
- **Load-bearing artifact:** none identifiable. No file in this repository is imported by another that GitGalaxy could resolve, so there is no dependency hierarchy to report. That is itself a finding: either this is a collection of independent scripts/documents rather than a coupled system, or the import style is one the engine does not resolve for these languages.
- **Top orchestrator:** `t/05_utils_ppi.t` -- pulls in 22 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `bin/perlcritic` at magnitude 2718.64 (structural weight, not risk).
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
| Total Artifacts | 439 |
| Analyzed Artifacts (Scanned) | 82 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 357 |
| Total LOC | 9457 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 18.7% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | n/a (not computed) | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 68 | 9401 | 82.9% |
| PLAINTEXT | 9 | 0 | 11.0% |
| MARKDOWN | 3 | 0 | 3.7% |
| HTML | 1 | 30 | 1.2% |
| DOCKERFILE | 1 | 26 | 1.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo`
> **Architectural Drift Z-Score:** `3.036`
> **Composition Archetype:** `Small Flat Repo` (z +3.04; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 41%, Data / Markup / Trivial 17%, Compute Cores Files 10%, Interface Declarations Files 9%, Large Core Modules (3) 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 70 | 85.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 12 | 14.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 357*

**Composition by Extension & Reason:**
- `.pm`: 194x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.run`: 136x Excluded (Unsupported Extension: '.run')
- `no_extension`: 8x Unsupported Format (.undeterminable), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unresolved Ambiguity (No Retainable Structure)
- `.pl`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 306 LOC), 1x Excluded (Machine-Generated Source Code Signature: 848 LOC)
- `.pdf`: 2x Excluded (Explicitly Denied Extension: '.pdf')
- `.pod`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')
- `.developer`: 1x Excluded (Unsupported Extension: '.developer')
- `.release`: 1x Excluded (Unsupported Extension: '.release')
- `.graffle`: 1x Excluded (Unsupported Extension: '.graffle')
- `.el`: 1x Excluded (Unsupported Extension: '.el')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 78.5 | 18.3 | 8.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.6 | 44.9 | 51.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.3 | 9.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 9.9 | 2.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 13.2 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 43.2 | 38.5 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 15.0 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 41.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 116 | 32 | 5 | `t/05_utils_pod.t` |
| cleanup | 31 | 9 | 1 | `lib/Perl/Critic/Utils/POD.pm` |
| guards | 361 | 65 | 9 | `t/03_pragmas.t` |
| danger | 102 | 31 | 4 | `t/00_modules.t` |
| concurrency | 1 | 1 | 0 | `bin/perlcritic` |
| connectivity | 157 | 34 | 4 | `t/05_utils.t` |
| io | 97 | 19 | 2 | `doc/links.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 3 | 2 | 0 | `extras/Dockerfile` |
| time | 6 | 2 | 0 | `TODO.pod` |
| serialization | 0 | 0 | 0 | - |
| regex | 197 | 32 | 7 | `lib/Perl/Critic/Utils/POD.pm` |
| events | 11 | 8 | 0 | `TODO.pod` |
| tests | 832 | 51 | 38 | `t/01_config.t` |
| docs | 124 | 22 | 1 | `bin/perlcritic` |
| debt | 140 | 25 | 6 | `t/Variables/RequireLocalizedPunctuationVars.run.PL` |
| mutation | 902 | 63 | 37 | `t/05_utils.t` |
| dead_code | 9 | 4 | 0 | `t/01_config.t` |
| credential | 1 | 1 | 0 | `doc/links.html` |
| threat | 8 | 3 | 0 | `TODO.pod` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 4 | 3 | 0 | `bin/perlcritic` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.75**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `doc/links.html` (Hits: 22)
- `t/05_utils.t` (Hits: 21)
- `lib/Perl/Critic/Utils/POD.pm` (Hits: 15)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **05_utils_ppi.t** (`t/05_utils_ppi.t`) — 22 outbound dependencies
2. **perlcritic** (`bin/perlcritic`) — 20 outbound dependencies
3. **01_config.t** (`t/01_config.t`) — 18 outbound dependencies
4. **05_utils.t** (`t/05_utils.t`) — 18 outbound dependencies
5. **06_violation.t** (`t/06_violation.t`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `print_fail_non_local` **(Many-Argument Workhorses)** (@ `t/Variables/RequireLocalizedPunctuationVars.run.PL`) -> Impact: **53.3** | LOC: 83
- `_get_module_abstract_from_filehandle` **(Many-Argument Workhorses)** (@ `lib/Perl/Critic/Utils/POD.pm`) -> Impact: **48.0** | LOC: 81
  * *Intent:* #-----------------------------------------------------------------------------
- `generate_policy_summary` **(I/O & Config Routines)** (@ `inc/Perl/Critic/PolicySummaryGenerator.pm`) -> Impact: **17.6** | LOC: 111
  * *Intent:* #-----------------------------------------------------------------------------
- `is_ppi_constant_element` **(Defensive Guards)** (@ `lib/Perl/Critic/Utils/PPI.pm`) -> Impact: **16.5** | LOC: 18
  * *Intent:* #-----------------------------------------------------------------------------
- `test_is_unchecked_call` **(I/O & Config Routines)** (@ `t/05_utils.t`) -> Impact: **16.2** | LOC: 85
  * *Intent:* #-----------------------------------------------------------------------------
- `test_is_perl_and_shebang_line` **(I/O & Config Routines)** (@ `t/05_utils.t`) -> Impact: **16.1** | LOC: 62
  * *Intent:* #-----------------------------------------------------------------------------
- `_count_main_logic_operators_and_keywords` **(Defensive Guards)** (@ `lib/Perl/Critic/Utils/McCabe.pm`) -> Impact: **15.8** | LOC: 35
  * *Intent:* #-----------------------------------------------------------------------------
- `summarize` **(Compute Cores)** (@ `examples/generatestats`) -> Impact: **14.6** | LOC: 50
- `RUN` **(I/O & Config Routines)** (@ `extras/Dockerfile`) -> Impact: **13.8** | LOC: 17
- `list_platforms` **(I/O & Config Routines)** (@ `inc/Devel/CheckOS.pm`) -> Impact: **13.6** | LOC: 31

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `bin` | 1 | 2718.64 | 14.21% | 9.59% |
| `t` | 40 | 2137.46 | 22.21% | 6.9% |
| `__monolith__` | 7 | 1508.22 | 2.14% | 3.45% |
| `lib/Perl/Critic/Utils` | 5 | 362.96 | 12.94% | 4.76% |
| `xt` | 11 | 175.18 | 14.36% | 13.58% |
| `doc` | 2 | 171.08 | 2.87% | 0.0% |
| `examples` | 2 | 155.18 | 16.62% | 0.0% |
| `t/Variables` | 1 | 129.56 | 28.51% | 0.0% |
| `inc/Devel` | 2 | 84.98 | 11.31% | 80.63% |
| `inc/Perl/Critic` | 2 | 42.84 | 6.76% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `inc/Devel/AssertOS.pm` -> **99.3307%** Exposure
- `xt/99_pod_coverage.t` -> **99.3307%** Exposure
- `t/20_policy_prohibit_hard_tabs.t` -> **96.8563%** Exposure
- `inc/Devel/CheckOS.pm` -> **61.9335%** Exposure
- `t/15_statistics.t` -> **59.1182%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `t/09_theme.t` -> **100.0%** Exposure
- `t/14_policy_parameter_behavior_boolean.t` -> **100.0%** Exposure
- `t/14_policy_parameter_behavior_enumeration.t` -> **100.0%** Exposure
- `t/14_policy_parameter_behavior_integer.t` -> **100.0%** Exposure
- `t/14_policy_parameter_behavior_list_string.t` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/03_pragmas.t` -> **0** Orphaned Functions | **2** Duplicates
- `t/20_policy_prohibit_hard_tabs.t` -> **0** Orphaned Functions | **2** Duplicates
- `t/15_statistics.t` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `581` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `bin/perlcritic` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2718.64 | **LOC:** 1049 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (76.5%), Guard Balance (formerly Safety Score) (60.9%), Complexity Load (formerly Cognitive Load) (14.2%), Concurrency Surface (formerly Concurrency) (13.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 16 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 45`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 29`, `planned_debt: 2`
* *Architecture:* `io: 13`, `api: 2`, `concurrency: 1`, `import: 37`
* *Defense:* `safety: 5`, `doc: 55`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic, Perl::Critic::Command, a, about, additional, arguments, critic, errors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `TODO.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1430.0 | **LOC:** 672 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (62.6%), Guard Balance (formerly Safety Score) (60.9%), Debt Markers (formerly Tech Debt) (24.2%), Complexity Load (formerly Cognitive Load) (15.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 56`, `func_start: 2`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 10`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `api: 2`, `import: 23`
* *Defense:* `safety: 6`, `doc: 18`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` C, L, Optional::Module, PPI::Cache, Perl::Critic, case, critic, feature...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/05_utils_pod.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 380.38 | **LOC:** 691 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (49.7%), Guard Balance (formerly Safety Score) (45.0%), Complexity Load (formerly Cognitive Load) (5.5%), Connectivity (formerly Api Exposure) (3.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 92`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `api: 2`, `import: 16`
* *Defense:* `safety: 5`, `doc: 16`, `test: 38`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, English, Perl::Critic::TestUtils, Perl::Critic::Utils::POD, Readonly, Test::More, a, abstract...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/05_utils.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 193.4 | **LOC:** 633 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.5%), Guard Balance (formerly Safety Score) (48.5%), Complexity Load (formerly Cognitive Load) (18.2%), Connectivity (formerly Api Exposure) (9.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_is_unchecked_call` **(I/O & Config Routines)** (Impact: 16.2)
    * *Intent:* #-----------------------------------------------------------------------------
  * `test_is_perl_and_shebang_line` **(I/O & Config Routines)** (Impact: 16.1)
    * *Intent:* #-----------------------------------------------------------------------------
  * `test_is_assignment_operator` **(I/O & Config Routines)** (Impact: 6.5)
    * *Intent:* #-----------------------------------------------------------------------------
  * `test_is_perl_bareword` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* #-----------------------------------------------------------------------------
  * `test_is_script` **(I/O & Config Routines)** (Impact: 5.5)
    * *Intent:* #-----------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 8 instances
* *Memory Alloc (weighted view):* 12
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 225`, `args: 2`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 45`
* *Architecture:* `io: 21`, `api: 23`, `import: 26`
* *Defense:* `safety: 10`, `test: 64`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, English, Fatal, Fatal::Exception, File::Temp, List::SomeUtils, PPI::Document, PPI::Document::File...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Utils/POD.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 177.52 | **LOC:** 724 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.7%), Mutation Surface (formerly State Flux) (25.7%), Complexity Load (formerly Cognitive Load) (12.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_module_abstract_from_filehandle` **(Many-Argument Workhorses)** (Impact: 48.0)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_get_pod_section_from_filehandle` **(Compute Cores)** (Impact: 8.8)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_get_pod_section_from_file` **(Compute Cores)** (Impact: 7.1)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_get_module_abstract_from_file` **(Compute Cores)** (Impact: 7.1)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_get_pod_section_from_string` **(Compute Cores)** (Impact: 6.7)
    * *Intent:* #-----------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 125`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `planned_debt: 1`
* *Architecture:* `io: 15`, `api: 22`, `import: 14`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` English, Exporter, Perl::Critic::Exception::Fatal::Generic, Perl::Critic::Exception::IO, Perl::Critic::Utils, Perl::Critic::Utils::POD, Pod::PlainText, Pod::Select...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/PolicyParameter_Notes.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 155.48 | **LOC:** 157 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (5.7%), Connectivity (formerly Api Exposure) (5.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 26`, `func_start: 3`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 11`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` any, configuration, for, hash, need, the
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/14_policy_parameter_behavior_enumeration.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 138.4 | **LOC:** 163 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.6%), Complexity Load (formerly Cognitive Load) (68.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 15`
* *Risk/State:* `state_mutation: 47`
* *Architecture:* `import: 21`
* *Defense:* `safety: 8`, `test: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` English, Perl::Critic::Policy, Perl::Critic::PolicyParameter, Perl::Critic::TestUtils, Test::More, default, strict, value...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/03_pragmas.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 138.0 | **LOC:** 969 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Debt Markers (formerly Tech Debt) (53.8%), Guard Balance (formerly Safety Score) (47.5%), Complexity Load (formerly Cognitive Load) (19.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `foo` **(Interface Declarations)** (Impact: 1.4)
  * `grep` **(Interface Declarations)** (Impact: 1.1)
  * `grep` **(Interface Declarations)** (Impact: 1.1)
  * `grep` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 212`, `func_start: 4`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 60`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 4`, `import: 71`
* *Defense:* `safety: 62`, `doc: 2`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::PolicyFactory, Perl::Critic::TestUtils, Test::More, critic, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/09_theme.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 135.78 | **LOC:** 319 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.7%), Complexity Load (formerly Cognitive Load) (78.5%), Connectivity (formerly Api Exposure) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `has_theme` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* #-----------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 31`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 50`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 4`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` English, List::SomeUtils, Perl::Critic::PolicyFactory, Perl::Critic::TestUtils, Perl::Critic::Theme, Perl::Critic::UserProfile, Test::More, critic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/Variables/RequireLocalizedPunctuationVars.run.PL` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 129.56 | **LOC:** 360 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.1%), Complexity Load (formerly Cognitive Load) (28.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `print_fail_non_local` **(Many-Argument Workhorses)** (Impact: 53.3)
  * `print_pass_local` **(Compute Cores)** (Impact: 11.6)
  * `print_pass_non_local_exception` **(Compute Cores)** (Impact: 7.9)
  * `print_fail_non_local_deref` **(Compute Cores)** (Impact: 6.6)
  * `print_footer` **(Compute Cores)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 64`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `io: 3`, `api: 7`, `import: 6`
* *Defense:* `safety: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` B::Keywords, Carp, English, List::SomeUtils, critic, space, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/14_policy_parameter_behavior_integer.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 122.38 | **LOC:** 169 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.1%), Complexity Load (formerly Cognitive Load) (59.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 14`
* *Risk/State:* `state_mutation: 55`
* *Architecture:* `import: 17`
* *Defense:* `safety: 7`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` English, Perl::Critic::Policy, Perl::Critic::PolicyParameter, Perl::Critic::TestUtils, Test::More, default, strict, value...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Utils/PPI.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 115.98 | **LOC:** 416 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (51.9%), Guard Balance (formerly Safety Score) (43.4%), Complexity Load (formerly Cognitive Load) (17.6%), Debt Markers (formerly Tech Debt) (14.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is_ppi_constant_element` **(Defensive Guards)** (Impact: 16.5)
    * *Intent:* #-----------------------------------------------------------------------------
  * `get_constant_name_element_from_declaring_statement` **(Defensive Guards)** (Impact: 9.8)
    * *Intent:* #-----------------------------------------------------------------------------
  * `is_subroutine_declaration` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* #-----------------------------------------------------------------------------
  * `get_previous_module_used_on_same_line` **(Defensive Guards)** (Impact: 7.9)
    * *Intent:* #-----------------------------------------------------------------------------
  * `get_next_element_in_same_simple_statement` **(Defensive Guards)** (Impact: 7.8)
    * *Intent:* #-----------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 112`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 2`
* *Architecture:* `api: 13`, `import: 13`
* *Defense:* `safety: 18`, `doc: 1`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Exporter, L, Readonly, Scalar::Util, constant, hashify, next, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/14_policy_parameter_behavior_list_string.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 108.72 | **LOC:** 168 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.1%), Complexity Load (formerly Cognitive Load) (70.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 13`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `import: 21`
* *Defense:* `safety: 2`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::Policy, Perl::Critic::PolicyParameter, Perl::Critic::TestUtils, Test::More, default, strict, value, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/generatestats` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 96.28 | **LOC:** 301 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (71.8%), Complexity Load (formerly Cognitive Load) (25.0%), Connectivity (formerly Api Exposure) (7.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `summarize` **(Compute Cores)** (Impact: 14.6)
  * `report_types` **(Compute Cores)** (Impact: 11.0)
  * `report_files` **(Compute Cores)** (Impact: 6.5)
  * `report_policies` **(Compute Cores)** (Impact: 6.2)
  * `report_totals` **(Compute Cores)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 56`, `args: 7`, `func_start: 8`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 14`
* *Architecture:* `api: 8`, `import: 11`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, English, File::Spec, Perl6::Say, Perl::Critic, Perl::Critic::Utils, Readonly, means...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/07_command.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 87.06 | **LOC:** 281 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (56.7%), Complexity Load (formerly Cognitive Load) (45.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 54`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`
* *Architecture:* `import: 11`
* *Defense:* `safety: 14`, `test: 39`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, English, File::Spec, Perl::Critic::Command, Perl::Critic::TestUtils, Perl::Critic::Utils, Test::More, arguments...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/03_annotations.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 85.92 | **LOC:** 244 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.9%), Complexity Load (formerly Cognitive Load) (65.1%), Connectivity (formerly Api Exposure) (4.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `annotate` **(Compute Cores)** (Impact: 6.7)
  * `choose_annotation` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 41`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 24`
* *Architecture:* `api: 2`, `import: 10`
* *Defense:* `safety: 2`, `doc: 1`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PPI::Document, Perl::Critic::Annotation, Perl::Critic::TestUtils, Test::More, critic, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/14_policy_parameter_behavior_boolean.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 85.32 | **LOC:** 101 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.6%), Complexity Load (formerly Cognitive Load) (67.4%), Debt Markers (formerly Tech Debt) (53.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 17`
* *Risk/State:* `state_mutation: 23`, `planned_debt: 2`
* *Architecture:* `import: 14`
* *Defense:* `safety: 2`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` English, Perl::Critic::Policy, Perl::Critic::PolicyParameter, Perl::Critic::TestUtils, Perl::Critic::Utils, Test::More, default, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `inc/Devel/CheckOS.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 78.92 | **LOC:** 333 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (81.7%), Guard Balance (formerly Safety Score) (70.8%), Debt Markers (formerly Tech Debt) (61.9%), Complexity Load (formerly Cognitive Load) (15.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `list_platforms` **(I/O & Config Routines)** (Impact: 13.6)
  * `os_is` **(Compute Cores)** (Impact: 9.2)
  * `list_family_members` **(I/O & Config Routines)** (Impact: 4.7)
  * `os_isnt` **(Compute Cores)** (Impact: 4.6)
  * `die_if_os_isnt` **(Annotated & Test Methods)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 62`, `args: 2`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 10`, `fragile_debt: 4`
* *Architecture:* `io: 1`, `api: 13`, `import: 16`
* *Defense:* `safety: 1`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Devel::AssertOS, Devel::CheckOS, Exporter, File::Find::Rule, File::Spec, match, strict, the...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/loadanalysisdb` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 58.9 | **LOC:** 345 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.0%), Complexity Load (formerly Cognitive Load) (8.2%), Connectivity (formerly Api Exposure) (7.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepare_insert_statement` **(Compute Cores)** (Impact: 13.2)
  * `load` **(Many-Argument Workhorses)** (Impact: 11.9)
  * `execute_insert_statement` **(Many-Argument Workhorses)** (Impact: 4.2)
  * `connect_to_database` **(I/O & Config Routines)** (Impact: 4.0)
  * `main` **(I/O & Config Routines)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 47`, `args: 5`, `func_start: 7`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`
* *Architecture:* `io: 2`, `api: 7`, `import: 11`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, DBI, English, File::Spec, Perl6::Say, Perl::Critic, Perl::Critic::Utils, Readonly...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Changes` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 51.58 | **LOC:** 2579 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/01_config.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 49.42 | **LOC:** 555 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (62.5%), Guard Balance (formerly Safety Score) (28.8%), Complexity Load (formerly Cognitive Load) (12.9%), Dead Code Surface (formerly Dead Code) (10.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 101`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`, `dead_code: 5`
* *Architecture:* `io: 1`, `import: 13`
* *Defense:* `safety: 7`, `test: 81`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` English, File::Spec, IO::Interactive, List::SomeUtils, Perl::Critic::Config, Perl::Critic::Exception::AggregateConfiguration, Perl::Critic::PolicyFactory, Perl::Critic::TestUtils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/14_policy_parameter_behavior_string.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 48.76 | **LOC:** 64 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.9%), Complexity Load (formerly Cognitive Load) (59.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 13`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `import: 10`
* *Defense:* `safety: 2`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::Policy, Perl::Critic::PolicyParameter, Perl::Critic::TestUtils, Test::More, default, strict, value, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Utils/McCabe.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 41.66 | **LOC:** 204 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (70.4%), Guard Balance (formerly Safety Score) (56.1%), Complexity Load (formerly Cognitive Load) (22.4%), Connectivity (formerly Api Exposure) (6.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_count_main_logic_operators_and_keywords` **(Defensive Guards)** (Impact: 15.8)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_count_logic_keywords` **(Parameter Forwarders)** (Impact: 3.6)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_count_logic_operators` **(Parameter Forwarders)** (Impact: 3.6)
    * *Intent:* #-----------------------------------------------------------------------------
  * `calculate_mccabe_of_sub` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* #-----------------------------------------------------------------------------
  * `calculate_mccabe_of_main` **(Parameter Forwarders)** (Impact: 1.8)
    * *Intent:* #-----------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 52`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Exporter, Perl::Critic::Utils, Readonly, critic, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/05_utils_ppi.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 34.4 | **LOC:** 380 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (34.6%), Mutation Surface (formerly State Flux) (31.5%), Complexity Load (formerly Cognitive Load) (7.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 69`, `args: 5`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `import: 21`
* *Defense:* `safety: 2`, `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PPI::Document, PPI::Statement, PPI::Statement::Break, PPI::Statement::Compound, PPI::Statement::Data, PPI::Statement::End, PPI::Statement::Expression, PPI::Statement::Include...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/80_policysummary.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 34.34 | **LOC:** 96 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 12.048; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (64.2%), Guard Balance (formerly Safety Score) (63.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 32`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 2`, `import: 9`
* *Defense:* `safety: 4`, `test: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, English, File::Spec, Perl::Critic::PolicyFactory, Perl::Critic::TestUtils, Test::More, extra, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `examples/generatestats` -> **Severity: 1204.8** (Blast Radius: 12.048 * Doc Risk: 100.0%)
- `examples/loadanalysisdb` -> **Severity: 1204.8** (Blast Radius: 12.048 * Doc Risk: 100.0%)
- `inc/Devel/AssertOS/Solaris.pm` -> **Severity: 1204.8** (Blast Radius: 12.048 * Doc Risk: 100.0%)
- `inc/Perl/Critic/BuildUtilities.pm` -> **Severity: 1204.8** (Blast Radius: 12.048 * Doc Risk: 100.0%)
- `inc/Perl/Critic/PolicySummaryGenerator.pm` -> **Severity: 1204.8** (Blast Radius: 12.048 * Doc Risk: 100.0%)

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
