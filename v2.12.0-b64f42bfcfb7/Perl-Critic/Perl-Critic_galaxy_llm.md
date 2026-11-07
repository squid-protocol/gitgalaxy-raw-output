# ARCHITECTURAL_BRIEF: Perl-Critic
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Perl-Critic/Perl-Critic.git` |
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
- **Scope:** 279 analyzed artifact(s), 36253 LOC.
- **Load-bearing artifact:** `lib/Perl/Critic/Utils.pm` -- 190 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `t/05_utils_ppi.t` -- pulls in 21 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/Perl/Critic/Utils.pm` at magnitude 21996.88 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 279 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 160 |
| Total LOC | 36253 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 63.6% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4623 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5319 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4601 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 12 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 264 | 36088 | 94.6% |
| PLAINTEXT | 9 | 0 | 3.2% |
| MARKDOWN | 3 | 0 | 1.1% |
| YAML | 1 | 109 | 0.4% |
| HTML | 1 | 30 | 0.4% |
| DOCKERFILE | 1 | 26 | 0.4% |

## 4.1 SOURCE ENCODINGS
All 279 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Interface Declarations Files 40%, Declarative / Non-Code 16%, Large Core Modules (3) 13%, Large Core Modules (2) 9%, Parameter Forwarders Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 267 | 95.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 12 | 4.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 160*

**Composition by Extension & Reason:**
- `.run`: 136x Excluded (Unsupported Extension: '.run')
- `no_extension`: 8x Unsupported Format (.undeterminable), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unresolved Ambiguity (No Retainable Structure)
- `.pdf`: 2x Excluded (Explicitly Denied Extension: '.pdf')
- `.pl`: 1x Excluded (Machine-Generated Source Code Signature: 306 LOC), 1x Excluded (Machine-Generated Source Code Signature: 848 LOC)
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')
- `.developer`: 1x Excluded (Unsupported Extension: '.developer')
- `.release`: 1x Excluded (Unsupported Extension: '.release')
- `.graffle`: 1x Excluded (Unsupported Extension: '.graffle')
- `.el`: 1x Excluded (Unsupported Extension: '.el')
- `.pm`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 90.0 | 23.5 | 16.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 81.1 | 35.6 | 48.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 52.7 | 65.4 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 15.6 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 47.0 | 6.4 | 7.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 97.8 | 0.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 40.9 | 32.4 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.6 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 79.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 520 | 199 | 5 | `lib/Perl/Critic/Document.pm` |
| cleanup | 113 | 26 | 0 | `lib/Perl/Critic/Utils.pm` |
| guards | 2200 | 260 | 15 | `lib/Perl/Critic/Utils.pm` |
| danger | 311 | 71 | 3 | `lib/Perl/Critic/Policy/ControlStructures/ProhibitUnreachableCode.pm` |
| concurrency | 18 | 7 | 0 | `lib/Perl/Critic/Utils.pm` |
| connectivity | 1468 | 228 | 8 | `lib/Perl/Critic/Utils.pm` |
| io | 383 | 73 | 3 | `lib/Perl/Critic/Utils.pm` |
| crypto | 0 | 0 | 0 | - |
| ipc | 34 | 10 | 0 | `lib/Perl/Critic/Policy/InputOutput/ProhibitBacktickOperators.pm` |
| time | 53 | 31 | 1 | `lib/Perl/Critic/Policy/BuiltinFunctions/ProhibitSleepViaSelect.pm` |
| serialization | 0 | 0 | 0 | - |
| regex | 913 | 132 | 8 | `lib/Perl/Critic/Utils.pm` |
| events | 31 | 22 | 0 | `TODO.pod` |
| tests | 925 | 55 | 7 | `t/01_config.t` |
| docs | 240 | 217 | 1 | `inc/Devel/CheckOS.pm` |
| debt | 362 | 95 | 4 | `t/Variables/RequireLocalizedPunctuationVars.run.PL` |
| mutation | 2915 | 216 | 27 | `lib/Perl/Critic/Config.pm` |
| dead_code | 786 | 157 | 6 | `lib/Perl/Critic/Policy/InputOutput/RequireEncodingWithUTF8Layer.pm` |
| credential | 1 | 1 | 0 | `doc/links.html` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 25 | 7 | 0 | `lib/Perl/Critic/Policy/BuiltinFunctions/ProhibitUselessTopic.pm` |
| ui | 14 | 11 | 0 | `bin/perlcritic` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **5.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lib/Perl/Critic/Utils.pm` (Hits: 49)
- `doc/links.html` (Hits: 22)
- `t/05_utils.t` (Hits: 21)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Utils.pm** (`lib/Perl/Critic/Utils.pm`) — 190 inbound connections
2. **TestUtils.pm** (`lib/Perl/Critic/TestUtils.pm`) — 51 inbound connections
3. **PolicyFactory.pm** (`lib/Perl/Critic/PolicyFactory.pm`) — 22 inbound connections
4. **Constants.pm** (`lib/Perl/Critic/Utils/Constants.pm`) — 10 inbound connections
5. **Internal.pm** (`lib/Perl/Critic/Exception/Fatal/Internal.pm`) — 9 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **05_utils_ppi.t** (`t/05_utils_ppi.t`) — 21 outbound dependencies
2. **TestUtils.pm** (`lib/Perl/Critic/TestUtils.pm`) — 20 outbound dependencies
3. **Command.pm** (`lib/Perl/Critic/Command.pm`) — 19 outbound dependencies
4. **Policy.pm** (`lib/Perl/Critic/Policy.pm`) — 18 outbound dependencies
5. **05_utils.t** (`t/05_utils.t`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `violates` **(Many-Argument Workhorses)** (@ `lib/Perl/Critic/Policy/BuiltinFunctions/ProhibitShiftRef.pm`) -> Impact: **123.7** | LOC: 150
  * *Intent:* #-----------------------------------------------------------------------------
- `supported_parameters` **(I/O & Config Routines)** (@ `lib/Perl/Critic/Policy/NamingConventions/Capitalization.pm`) -> Impact: **67.7** | LOC: 114
  * *Intent:* #----------------------------------------------------------------------------- # Can't handle named parameters yet.
- `initialize_parameter` **(Many-Argument Workhorses)** (@ `lib/Perl/Critic/PolicyParameter/Behavior/Enumeration.pm`) -> Impact: **65.1** | LOC: 101
  * *Intent:* #-----------------------------------------------------------------------------
- `print_fail_non_local` **(Many-Argument Workhorses)** (@ `t/Variables/RequireLocalizedPunctuationVars.run.PL`) -> Impact: **53.3** | LOC: 83
- `_validate_fully_qualified_symbols` **(Many-Argument Workhorses)** (@ `lib/Perl/Critic/Policy/ValuesAndExpressions/ProhibitComplexVersion.pm`) -> Impact: **52.2** | LOC: 61
  * *Intent:* #-----------------------------------------------------------------------------
- `supported_parameters` **(Many-Argument Workhorses)** (@ `lib/Perl/Critic/Policy/ValuesAndExpressions/ProhibitInterpolationOfLiterals.pm`) -> Impact: **49.2** | LOC: 79
  * *Intent:* #-----------------------------------------------------------------------------
- `_get_module_abstract_from_filehandle` **(Many-Argument Workhorses)** (@ `lib/Perl/Critic/Utils/POD.pm`) -> Impact: **48.0** | LOC: 81
  * *Intent:* #-----------------------------------------------------------------------------
- `violates` **(Many-Argument Workhorses)** (@ `lib/Perl/Critic/Policy/InputOutput/ProhibitBarewordDirHandles.pm`) -> Impact: **46.8** | LOC: 95
  * *Intent:* #-----------------------------------------------------------------------------
- `_init` **(Many-Argument Workhorses)** (@ `lib/Perl/Critic/Annotation.pm`) -> Impact: **43.6** | LOC: 76
  * *Intent:* #============================================================================= # OBJECT methods
- `_validate_word_version` **(Defensive Guards)** (@ `lib/Perl/Critic/Policy/ValuesAndExpressions/RequireConstantVersion.pm`) -> Impact: **43.6** | LOC: 33
  * *Intent:* #----------------------------------------------------------------------------- # Validate $VERSION = version->new();

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib/Perl/Critic` | 21 | 31430.71 | 32.42% | 7.66% |
| `bin` | 1 | 2718.64 | 28.0% | 8.68% |
| `t` | 40 | 2137.46 | 22.25% | 5.23% |
| `__monolith__` | 8 | 1524.58 | 4.78% | 4.39% |
| `lib/Perl/Critic/Policy/ValuesAndExpressions` | 21 | 1477.56 | 29.93% | 85.04% |
| `lib/Perl/Critic/Policy/RegularExpressions` | 13 | 1034.2 | 32.96% | 87.58% |
| `lib/Perl/Critic/Policy/Subroutines` | 12 | 941.06 | 30.31% | 76.22% |
| `lib/Perl/Critic/Policy/Variables` | 15 | 906.78 | 18.54% | 86.62% |
| `lib/Perl/Critic/Policy/BuiltinFunctions` | 17 | 761.26 | 35.69% | 96.34% |
| `lib/Perl/Critic/Policy/InputOutput` | 15 | 651.04 | 24.37% | 93.85% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/workflows/testsuite.yml` -> **100.0%** Exposure
- `lib/Perl/Critic/Policy/BuiltinFunctions/ProhibitShiftRef.pm` -> **100.0%** Exposure
- `lib/Perl/Critic/Policy/InputOutput/ProhibitExplicitStdin.pm` -> **100.0%** Exposure
- `lib/Perl/Critic/Policy/InputOutput/ProhibitJoinedReadline.pm` -> **99.9995%** Exposure
- `lib/Perl/Critic/Policy/InputOutput/ProhibitBarewordFileHandles.pm` -> **99.9981%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `lib/Perl/Critic/OptionsProcessor.pm` -> **100.0%** Exposure
- `lib/Perl/Critic/ProfilePrototype.pm` -> **100.0%** Exposure
- `t/09_theme.t` -> **100.0%** Exposure
- `t/14_policy_parameter_behavior_boolean.t` -> **100.0%** Exposure
- `t/14_policy_parameter_behavior_enumeration.t` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `.github/workflows/testsuite.yml` -> **0** Orphaned Functions | **8** Duplicates
- `lib/Perl/Critic/Policy/Modules/RequireExplicitPackage.pm` -> **7** Orphaned Functions | **0** Duplicates
- `lib/Perl/Critic/Policy/ValuesAndExpressions/ProhibitMagicNumbers.pm` -> **7** Orphaned Functions | **0** Duplicates
- `lib/Perl/Critic/Policy/BuiltinFunctions/ProhibitLvalueSubstr.pm` -> **6** Orphaned Functions | **0** Duplicates
- `lib/Perl/Critic/Policy/BuiltinFunctions/ProhibitShiftRef.pm` -> **6** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1666` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/Perl/Critic/Utils.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.042)
- **Top Global Matches:** file_cluster_2: 5.042, file_cluster_13: 5.344, file_cluster_17: 5.481
- **Magnitude:** 21996.88 | **LOC:** 2011 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **190** in-repo importer(s); it depends on **16**; blast radius 224.65; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.3%), Mutation Surface (formerly State Flux) (17.2%), Concurrency Surface (formerly Concurrency) (16.5%), Complexity Load (formerly Cognitive Load) (14.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 301`, `structural_boundaries: 435`, `args: 48`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `fragile_debt: 1`
* *Architecture:* `io: 49`, `api: 44`, `concurrency: 7`, `import: 22`
* *Defense:* `safety: 39`, `doc: 1`, `immutability_locks: 50`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 224.65
  * `Choke Point (Betweenness):` 0.005255 | `Ripple Effect (Closeness):` 0.705397
  * `Imports (Out-Degree: 2):` B::Keywords, Carp, English, Exporter, File::Find, File::Spec, List::SomeUtils, PPI::Token::Quote::Single...
  * `Imported By (In-Degree: 190):` (Excluded from Brief to save tokens)

### `lib/Perl/Critic/DEVELOPER.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.003)
- **Top Global Matches:** file_cluster_2: 4.003, file_cluster_13: 4.887, file_cluster_17: 5.272
- **Magnitude:** 5513.95 | **LOC:** 1104 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.2%), Mutation Surface (formerly State Flux) (40.5%), Complexity Load (formerly Cognitive Load) (13.9%), Debt Markers (formerly Tech Debt) (10.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 177`, `args: 10`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 19`, `planned_debt: 5`
* *Architecture:* `io: 10`, `api: 24`, `import: 38`
* *Defense:* `safety: 11`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/perlcritic` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.349)
- **Top Global Matches:** file_cluster_2: 4.349, file_cluster_13: 5.702, file_cluster_17: 5.994
- **Magnitude:** 2718.64 | **LOC:** 1049 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.393; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (76.5%), Guard Balance (formerly Safety Score) (54.0%), Complexity Load (formerly Cognitive Load) (28.0%), Concurrency Surface (formerly Concurrency) (13.2%)
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
* *Defense:* `safety: 5`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Perl::Critic::Command, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `TODO.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.854)
- **Top Global Matches:** file_cluster_2: 4.854, file_cluster_13: 5.456, file_cluster_17: 5.987
- **Magnitude:** 1430.0 | **LOC:** 672 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (62.6%), Guard Balance (formerly Safety Score) (53.3%), Complexity Load (formerly Cognitive Load) (29.1%), Debt Markers (formerly Tech Debt) (20.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 56`, `func_start: 2`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 10`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `api: 2`, `import: 23`
* *Defense:* `safety: 6`, `doc: 1`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/CORE_DEVELOPER.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.292)
- **Top Global Matches:** file_cluster_2: 3.292, file_cluster_13: 4.701, file_cluster_17: 4.995
- **Magnitude:** 858.16 | **LOC:** 315 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.5%), Debt Markers (formerly Tech Debt) (30.6%), Mutation Surface (formerly State Flux) (25.8%), Complexity Load (formerly Cognitive Load) (11.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 33`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 3`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 3`, `import: 4`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Config.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.514)
- **Top Global Matches:** file_cluster_15: 5.514, file_cluster_11: 7.775, file_cluster_16: 7.868
- **Magnitude:** 593.74 | **LOC:** 1395 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **16**; blast radius 8.969; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.0%), Complexity Load (formerly Cognitive Load) (50.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_load_policies` **(Compute Cores)** (Impact: 36.8)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_validate_and_save_regex` **(Many-Argument Workhorses)** (Impact: 32.4)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_init` **(Many-Argument Workhorses)** (Impact: 24.1)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_validate_and_save_color_severity` **(Many-Argument Workhorses)** (Impact: 22.4)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_validate_and_save_severity` **(Many-Argument Workhorses)** (Impact: 20.8)
    * *Intent:* #-----------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 253
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 248`, `args: 47`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 87`
* *Architecture:* `io: 1`, `api: 26`, `import: 17`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.969
  * `Choke Point (Betweenness):` 0.003266 | `Ripple Effect (Closeness):` 0.113991
  * `Imports (Out-Degree: 9):` English, List::SomeUtils, Perl::Critic::Exception::AggregateConfiguration, Perl::Critic::Exception::Configuration, Perl::Critic::Exception::Configuration::Option::Global::ParameterValue, Perl::Critic::Exception::Fatal::Internal, Perl::Critic::PolicyFactory, Perl::Critic::Theme...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `lib/Perl/Critic/Policy/RegularExpressions/ProhibitUnusedCapture.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.303)
- **Top Global Matches:** file_cluster_4: 6.303, file_cluster_15: 9.959, file_cluster_9: 10.79
- **Magnitude:** 433.36 | **LOC:** 878 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.393; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.4%), Complexity Load (formerly Cognitive Load) (40.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_enough_assignments` **(Defensive Guards)** (Impact: 42.9)
  * `_mark_magic_in_content` **(Many-Argument Workhorses)** (Impact: 40.9)
    * *Intent:* # Find capture variables in the content of a double-quotish thing, and # record their use. RT #38942...
  * `_mark_magic` **(Many-Argument Workhorses)** (Impact: 37.0)
  * `violates` **(Many-Argument Workhorses)** (Impact: 24.2)
  * `_enough_uses_in_regexp` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* # Find uses of both numbered and named capture variables in the regexp itself. # Return true if all ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 27 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 244`, `args: 25`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 33`, `dead_code: 3`, `planned_debt: 3`, `unreferenced_by_name: 5`
* *Architecture:* `api: 6`, `import: 16`
* *Defense:* `safety: 36`, `doc: 1`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` List::SomeUtils, Perl::Critic::Utils, Readonly, Scalar::Util, a, parent, strict, the...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Document.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.334)
- **Top Global Matches:** file_cluster_15: 6.334, file_cluster_12: 8.119, file_cluster_16: 8.431
- **Magnitude:** 391.36 | **LOC:** 970 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 3.594; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.6%), Complexity Load (formerly Cognitive Load) (34.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_inner_element_is_in_outer_scope_really` **(Defensive Guards)** (Impact: 21.8)
    * *Intent:* # Helper for element_is_in_lexical_scope_after_statement_containing(). # Given that the outer elemen...
  * `_init_from_external_source` **(Compute Cores)** (Impact: 21.3)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_find_use_re_modifiers_in_scope_from_element` **(Defensive Guards)** (Impact: 20.2)
  * `_determine_is_module` **(Type Conversions)** (Impact: 16.7)
    * *Intent:* #-----------------------------------------------------------------------------
  * `find` **(Many-Argument Workhorses)** (Impact: 13.6)
    * *Intent:* #-----------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 268`, `args: 38`, `func_start: 36`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 35`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `api: 22`, `import: 22`
* *Defense:* `safety: 17`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.594
  * `Choke Point (Betweenness):` 0.001451 | `Ripple Effect (Closeness):` 0.072782
  * `Imports (Out-Degree: 3):` List::Util, PPI::Document, PPI::Document::File, PPIx::Regexp, PPIx::Utils::Traversal, Perl::Critic::Annotation, Perl::Critic::Document, Perl::Critic::Exception::Parse...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `t/05_utils_pod.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.513)
- **Top Global Matches:** file_cluster_2: 3.513, file_cluster_17: 4.968, file_cluster_13: 5.427
- **Magnitude:** 380.38 | **LOC:** 691 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.393; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (49.7%), Guard Balance (formerly Safety Score) (47.9%), Complexity Load (formerly Cognitive Load) (7.2%), Connectivity (formerly Api Exposure) (3.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 92`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `api: 2`, `import: 16`
* *Defense:* `safety: 5`, `doc: 6`, `test: 38`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Carp, English, Perl::Critic::TestUtils, Perl::Critic::Utils::POD, Readonly, Test::More, abstract, hyphen...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Command.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.647)
- **Top Global Matches:** file_cluster_4: 5.647, file_cluster_6: 10.384, file_cluster_15: 10.644
- **Magnitude:** 295.06 | **LOC:** 732 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **19**; blast radius 2.972; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.7%), Complexity Load (formerly Cognitive Load) (28.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_render_report` **(Many-Argument Workhorses)** (Impact: 36.2)
    * *Intent:* #------------------------------------------------------------------------------
  * `_critique` **(Compute Cores)** (Impact: 27.0)
    * *Intent:* #------------------------------------------------------------------------------
  * `_validate_options` **(Compute Cores)** (Impact: 26.0)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_report_statistics` **(Many-Argument Workhorses)** (Impact: 22.9)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_get_input` **(Compute Cores)** (Impact: 17.2)
    * *Intent:* #-----------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 169`, `args: 12`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 6`, `state_mutation: 27`, `fragile_debt: 2`
* *Architecture:* `io: 4`, `api: 4`, `import: 25`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.972
  * `Choke Point (Betweenness):` 0.000593 | `Ripple Effect (Closeness):` 0.007168
  * `Imports (Out-Degree: 9):` English, Exporter, Getopt::Long, List::Util, Perl::Critic, Perl::Critic::Exception::Parse, Perl::Critic::PolicyFactory, Perl::Critic::PolicyListing...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Perl/Critic/Policy/NamingConventions/Capitalization.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.209)
- **Top Global Matches:** file_cluster_4: 7.209, file_cluster_15: 10.033, file_cluster_9: 10.368
- **Magnitude:** 294.64 | **LOC:** 770 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.393; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.9%), Debt Markers (formerly Tech Debt) (46.0%), Mutation Surface (formerly State Flux) (38.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `supported_parameters` **(I/O & Config Routines)** (Impact: 67.7)
    * *Intent:* #----------------------------------------------------------------------------- # Can't handle named ...
  * `_variable_capitalization` **(Many-Argument Workhorses)** (Impact: 27.8)
  * `_is_directly_in_scope_block` **(Defensive Guards)** (Impact: 19.8)
    * *Intent:* # { my $x } parses as # PPI::Document # PPI::Statement::Compound # PPI::Structure::Block { ... } # P...
  * `_foreach_variable_capitalization` **(Compute Cores)** (Impact: 19.4)
  * `initialize_if_enabled` **(Many-Argument Workhorses)** (Impact: 18.1)
    * *Intent:* #-----------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 188`, `args: 14`, `func_start: 24`, `class_start: 6`
* *Risk/State:* `state_mutation: 13`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 6`
* *Architecture:* `io: 1`, `api: 18`, `import: 14`
* *Defense:* `safety: 19`, `doc: 1`, `immutability_locks: 18`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` English, List::SomeUtils, PPIx::Utils::Traversal, Perl::Critic::Exception::AggregateConfiguration, Perl::Critic::Exception::Configuration::Option::Policy::ParameterValue, Perl::Critic::Utils, Perl::Critic::Utils::PPI, Perl::Critic::Utils::Perl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Policy/ValuesAndExpressions/ProhibitMagicNumbers.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.498)
- **Top Global Matches:** file_cluster_4: 6.498, file_cluster_15: 9.099, file_cluster_11: 10.004
- **Magnitude:** 244.2 | **LOC:** 680 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.393; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.1%), Complexity Load (formerly Cognitive Load) (36.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_element_is_in_a_constant_subroutine` **(Defensive Guards)** (Impact: 25.8)
  * `_determine_allowed_values` **(Compute Cores)** (Impact: 23.9)
  * `violates` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `_element_is_in_an_include_readonly_or_version_statement` **(Defensive Guards)** (Impact: 19.2)
  * `_element_is_in_a_plan_statement` **(Defensive Guards)** (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 157`, `args: 11`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 38`, `unreferenced_by_name: 7`
* *Architecture:* `io: 9`, `api: 8`, `import: 16`
* *Defense:* `safety: 21`, `doc: 1`, `test: 3`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Perl::Critic::Utils, Readonly, parent, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Policy/ValuesAndExpressions/RequireConstantVersion.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.049)
- **Top Global Matches:** file_cluster_4: 7.049, file_cluster_6: 10.506, file_cluster_9: 11.906
- **Magnitude:** 241.32 | **LOC:** 434 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.393; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.7%), Debt Markers (formerly Tech Debt) (74.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_validate_word_version` **(Defensive Guards)** (Impact: 43.6)
    * *Intent:* #----------------------------------------------------------------------------- # Validate $VERSION =...
  * `_validate_word_qv` **(Defensive Guards)** (Impact: 27.5)
    * *Intent:* #----------------------------------------------------------------------------- # Validate $VERSION =...
  * `_validate_operator_bind_regex` **(Defensive Guards)** (Impact: 27.2)
    * *Intent:* #----------------------------------------------------------------------------- # Validate a bind_reg...
  * `violates` **(Many-Argument Workhorses)** (Impact: 24.8)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_validate_word_vstring` **(Defensive Guards)** (Impact: 12.7)
    * *Intent:* #----------------------------------------------------------------------------- # Validate $VERSION =...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 102`, `args: 7`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 26`, `planned_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 6`, `import: 10`
* *Defense:* `safety: 20`, `doc: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Perl::Critic::Utils, Perl::Critic::Utils::PPI, Readonly, parent, strict, version, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/OptionsProcessor.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.329)
- **Top Global Matches:** file_cluster_15: 6.329, file_cluster_4: 7.703, file_cluster_11: 8.294
- **Magnitude:** 221.6 | **LOC:** 455 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 3.215; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_init` **(Many-Argument Workhorses)** (Impact: 33.3)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_check_for_extra_options` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* #-----------------------------------------------------------------------------
  * `new` **(Type Conversions)** (Impact: 2.0)
    * *Intent:* #-----------------------------------------------------------------------------
  * `severity` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* #----------------------------------------------------------------------------- # Public ACCESSOR met...
  * `theme` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* #-----------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 91`, `args: 22`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 56`
* *Architecture:* `api: 21`, `import: 11`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.215
  * `Choke Point (Betweenness):` 0.000844 | `Ripple Effect (Closeness):` 0.077314
  * `Imports (Out-Degree: 4):` List::SomeUtils, Perl::Critic::Exception::AggregateConfiguration, Perl::Critic::Exception::Configuration::Option::Global::ExtraParameter, Perl::Critic::Utils, Perl::Critic::Utils::Constants, strict, warnings
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Perl/Critic/Policy/Subroutines/RequireArgUnpacking.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.733)
- **Top Global Matches:** file_cluster_4: 6.733, file_cluster_9: 9.336, file_cluster_15: 9.341
- **Magnitude:** 216.98 | **LOC:** 520 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.393; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (76.9%), Guard Balance (formerly Safety Score) (47.4%), Complexity Load (formerly Cognitive Load) (30.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `violates` **(Many-Argument Workhorses)** (Impact: 41.1)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_is_unpack` **(Defensive Guards)** (Impact: 20.3)
  * `_is_size_check` **(Compute Cores)** (Impact: 17.2)
  * `_is_cast_of_scalar` **(Defensive Guards)** (Impact: 13.3)
    * *Intent:* # This subroutine recognizes (e.g.) $$_[0]. This is a use of $_ (equivalent to # $_->[0]), not @_.
  * `_is_delegation` **(Defensive Guards)** (Impact: 12.3)
    * *Intent:* # A literal @_ is allowed as the argument for a delegation. # An example of the idiom we are looking...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 146`, `args: 14`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 13`, `unreferenced_by_name: 5`
* *Architecture:* `io: 2`, `api: 8`, `import: 6`
* *Defense:* `safety: 28`, `doc: 1`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Perl::Critic::Utils, Readonly, parent, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/TestUtils.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.478)
- **Top Global Matches:** file_cluster_4: 6.478, file_cluster_12: 9.15, file_cluster_15: 9.178
- **Magnitude:** 214.28 | **LOC:** 662 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **51** in-repo importer(s); it depends on **20**; blast radius 35.141; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.5%), Guard Balance (formerly Safety Score) (52.8%), Complexity Load (formerly Cognitive Load) (45.9%), Debt Markers (formerly Tech Debt) (17.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_subtests_from_file` **(Compute Cores)** (Impact: 41.7)
    * *Intent:* # The internal representation of a subtest is just a hash with some # named keys. It could be an obj...
  * `_finalize_subtest` **(Compute Cores)** (Impact: 18.9)
  * `subtests_in_tree` **(Compute Cores)** (Impact: 16.2)
    * *Intent:* # Note: $include_extras is not documented in the POD because I'm not # committing to the interface y...
  * `_globals_from_file` **(Compute Cores)** (Impact: 15.8)
  * `fcritique_with_violations` **(Many-Argument Workhorses)** (Impact: 14.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 20 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 140`, `args: 8`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 22`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `io: 6`, `api: 16`, `import: 23`
* *Defense:* `safety: 5`, `doc: 1`, `test: 36`, `immutability_locks: 3`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 35.141
  * `Choke Point (Betweenness):` 0.014612 | `Ripple Effect (Closeness):` 0.182796
  * `Imports (Out-Degree: 7):` Carp, English, Exporter, ExtUtils::Manifest, File::Find, File::Path, File::Spec, File::Spec::Unix...
  * `Imported By (In-Degree: 51):` (Excluded from Brief to save tokens)

### `lib/Perl/Critic/Policy/RegularExpressions/ProhibitCaptureWithoutTest.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.081)
- **Top Global Matches:** file_cluster_6: 7.081, file_cluster_4: 10.17, file_cluster_8: 16.477
- **Magnitude:** 201.66 | **LOC:** 408 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.393; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (87.4%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (65.4%), Guard Balance (formerly Safety Score) (46.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_unambiguous_goto` **(Compute Cores)** (Impact: 32.1)
    * *Intent:* # Determine whether the given goto represents an unambiguous transfer of # control around anything t...
  * `_get_method_name` **(Defensive Guards)** (Impact: 28.5)
    * *Intent:* # If the argument introduces a method call, return the method name; # otherwise just return.
  * `_is_in_conditional_structure` **(Defensive Guards)** (Impact: 28.0)
  * `_is_control_transfer_to_right` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* # This subroutine returns true if there is a control transfer to the right of # the match operation ...
  * `_is_control_transfer_to_left` **(Defensive Guards)** (Impact: 13.1)
    * *Intent:* # This subroutine returns true if there is a control transfer to the left of # the match operation w...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 130`, `args: 9`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`, `planned_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `safety: 27`, `doc: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Perl::Critic::Utils, Readonly, parent, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/05_utils.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.237)
- **Top Global Matches:** file_cluster_12: 7.237, file_cluster_11: 7.68, file_cluster_15: 8.298
- **Magnitude:** 193.4 | **LOC:** 633 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 1.393; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.5%), Guard Balance (formerly Safety Score) (48.9%), Complexity Load (formerly Cognitive Load) (18.2%), Connectivity (formerly Api Exposure) (9.9%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Carp, English, Fatal, Fatal::Exception, File::Temp, List::SomeUtils, PPI::Document, PPI::Document::File...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Policy.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.278)
- **Top Global Matches:** file_cluster_15: 5.278, file_cluster_11: 6.321, file_cluster_10: 7.381
- **Magnitude:** 191.4 | **LOC:** 910 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 1.393; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.4%), Mutation Surface (formerly State Flux) (50.6%), Debt Markers (formerly Tech Debt) (30.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new` **(Many-Argument Workhorses)** (Impact: 14.8)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_set_maximum_violations_per_document` **(Compute Cores)** (Impact: 9.1)
    * *Intent:* #-----------------------------------------------------------------------------
  * `__set_base_parameters` **(Compute Cores)** (Impact: 8.7)
    * *Intent:* #-----------------------------------------------------------------------------
  * `to_string` **(Callbacks & Closures)** (Impact: 7.9)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_format_parameters` **(Compute Cores)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 212`, `args: 29`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 6`, `api: 29`, `import: 20`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` English, Exception::Class, File::Spec, Perl::Critic::Exception::AggregateConfiguration, Perl::Critic::Exception::Configuration, Perl::Critic::Exception::Configuration::Option::Policy::ExtraParameter, Perl::Critic::Exception::Configuration::Option::Policy::ParameterValue, Perl::Critic::Exception::Fatal::PolicyDefinition...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Utils/POD.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.327)
- **Top Global Matches:** file_cluster_15: 6.327, file_cluster_4: 7.82, file_cluster_16: 8.508
- **Magnitude:** 177.52 | **LOC:** 724 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 4.765; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.9%), Mutation Surface (formerly State Flux) (25.7%), Complexity Load (formerly Cognitive Load) (12.7%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.765
  * `Choke Point (Betweenness):` 0.000847 | `Ripple Effect (Closeness):` 0.067037
  * `Imports (Out-Degree: 3):` English, Exporter, Perl::Critic::Exception::Fatal::Generic, Perl::Critic::Exception::IO, Perl::Critic::Utils, Pod::PlainText, Pod::Select, strict...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/Perl/Critic/Policy/ErrorHandling/RequireCheckingReturnValueOfEval.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.509)
- **Top Global Matches:** file_cluster_15: 7.509, file_cluster_9: 7.975, file_cluster_11: 8.063
- **Magnitude:** 175.06 | **LOC:** 454 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.393; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (47.0%), Complexity Load (formerly Cognitive Load) (39.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_is_in_correct_position_in_a_structure_condition` **(Many-Argument Workhorses)** (Impact: 28.1)
  * `violates` **(Compute Cores)** (Impact: 23.3)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_is_in_postfix_expression` **(Defensive Guards)** (Impact: 14.4)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_is_in_right_hand_side_of_assignment` **(Compute Cores)** (Impact: 14.1)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_is_in_correct_position_in_a_condition_or_foreach_loop_collection` **(Defensive Guards)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 126`, `args: 10`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 14`, `unreferenced_by_name: 5`
* *Architecture:* `api: 7`, `import: 14`
* *Defense:* `safety: 30`, `doc: 1`, `immutability_locks: 8`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Perl::Critic::Utils, Readonly, Scalar::Util, parent, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Policy/InputOutput/RequireBriefOpen.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.321)
- **Top Global Matches:** file_cluster_4: 8.321, file_cluster_6: 9.817, file_cluster_9: 13.814
- **Magnitude:** 174.78 | **LOC:** 365 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.393; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.0%), Debt Markers (formerly Tech Debt) (38.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `violates` **(Compute Cores)** (Impact: 38.2)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_find_close_invocations_or_return` **(Defensive Guards)** (Impact: 35.5)
  * `_get_scope` **(Compute Cores)** (Impact: 25.9)
  * `_get_opened_fh` **(Defensive Guards)** (Impact: 17.5)
  * `_unwrap_block` **(Defensive Guards)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 121`, `args: 8`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 5`
* *Architecture:* `io: 20`, `api: 7`, `import: 8`
* *Defense:* `safety: 11`, `doc: 1`, `immutability_locks: 11`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` List::SomeUtils, Perl::Critic::Utils, Readonly, parent, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Violation.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.591)
- **Top Global Matches:** file_cluster_15: 5.591, file_cluster_11: 6.948, file_cluster_10: 7.387
- **Magnitude:** 161.36 | **LOC:** 600 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **11**; blast radius 7.442; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.6%), Guard Balance (formerly Safety Score) (54.1%), Complexity Load (formerly Cognitive Load) (34.0%), Debt Markers (formerly Tech Debt) (9.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new` **(Many-Argument Workhorses)** (Impact: 19.3)
  * `sort_by_location` **(Type Conversions)** (Impact: 9.1)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_line_containing_violation` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* #-----------------------------------------------------------------------------
  * `explanation` **(Type Conversions)** (Impact: 7.7)
    * *Intent:* #-----------------------------------------------------------------------------
  * `diagnostics` **(Defensive Guards)** (Impact: 6.5)
    * *Intent:* #-----------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 134`, `args: 20`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 20`, `import: 17`
* *Defense:* `safety: 7`, `doc: 1`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.442
  * `Choke Point (Betweenness):` 0.001703 | `Ripple Effect (Closeness):` 0.082713
  * `Imports (Out-Degree: 3):` File::Basename, Perl::Critic::Exception::Fatal::Internal, Perl::Critic::Utils, Perl::Critic::Utils::POD, Readonly, Scalar::Util, String::Format, explanation...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `lib/Perl/Critic/Policy/Subroutines/RequireFinalReturn.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.079)
- **Top Global Matches:** file_cluster_15: 7.079, file_cluster_11: 8.195, file_cluster_9: 8.511
- **Magnitude:** 161.34 | **LOC:** 378 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.393; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (56.8%), Guard Balance (formerly Safety Score) (43.6%), Debt Markers (formerly Tech Debt) (38.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_is_given_when_return` **(Defensive Guards)** (Impact: 26.9)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_is_compound_return` **(Defensive Guards)** (Impact: 20.4)
    * *Intent:* #-----------------------------------------------------------------------------
  * `violates` **(Many-Argument Workhorses)** (Impact: 17.7)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_is_terminal_stmnt` **(Defensive Guards)** (Impact: 14.6)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_is_suffix_when_with_return` **(Defensive Guards)** (Impact: 12.7)
    * *Intent:* #-----------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 127`, `args: 13`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 6`, `unreferenced_by_name: 5`
* *Architecture:* `api: 8`, `import: 10`
* *Defense:* `safety: 30`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` List::SomeUtils, Perl::Critic::Exception::Fatal::Internal, Perl::Critic::Utils, Readonly, more, parent, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Annotation.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.317)
- **Top Global Matches:** file_cluster_4: 6.317, file_cluster_6: 10.351, file_cluster_15: 11.062
- **Magnitude:** 156.92 | **LOC:** 410 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 3.004; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.5%), Guard Balance (formerly Safety Score) (55.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_init` **(Many-Argument Workhorses)** (Impact: 43.6)
    * *Intent:* #============================================================================= # OBJECT methods
  * `_parse_annotation` **(Compute Cores)** (Impact: 15.2)
    * *Intent:* #-----------------------------------------------------------------------------
  * `create_annotations` **(Compute Cores)** (Impact: 12.7)
    * *Intent:* #============================================================================= # CLASS methods
  * `_is_single_line_annotation_on_simple_statement` **(Defensive Guards)** (Impact: 10.4)
    * *Intent:* #----------------------------------------------------------------------------- # Recognize a single-...
  * `disables_policy` **(Parameter Forwarders)** (Impact: 5.5)
    * *Intent:* #-----------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 97`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `api: 8`, `import: 12`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.004
  * `Choke Point (Betweenness):` 0.000187 | `Ripple Effect (Closeness):` 0.056081
  * `Imports (Out-Degree: 2):` Carp, Perl::Critic::PolicyFactory, Perl::Critic::Utils, Readonly, strict, warnings
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `lib/Perl/Critic/Policy/Variables/ProhibitLocalVars.pm` (PERL) | Magnitude: 28.52 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 46, indent_spaces: 18, branch: 14, import: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `xt/40_criticize-code.t` (PERL) | Magnitude: 15.68 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 13, import: 11, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `lib/Perl/Critic/Policy/Modules/RequireExplicitPackage.pm` (PERL) | Magnitude: 48.76 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 66, indent_spaces: 51, branch: 18, import: 12
- `lib/Perl/Critic/Policy/Variables/ProhibitPackageVars.pm` (PERL) | Magnitude: 55.94 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 82, indent_spaces: 62, branch: 27, import: 13
- `lib/Perl/Critic/Policy/ValuesAndExpressions/ProhibitMismatchedOperators.pm` (PERL) | Magnitude: 91.9 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 75, branch: 42, func_start: 10
- `lib/Perl/Critic/Policy/Modules/RequireFilenameMatchesPackage.pm` (PERL) | Magnitude: 62.08 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 52, indent_spaces: 33, branch: 25, api: 7
- `t/01_policy_config.t` (PERL) | Magnitude: 10.1 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 29, test: 20, import: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `xt/42_criticize-tests.t` (PERL) | Magnitude: 15.66 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 13, import: 10, branch: 3
- `t/92_memory_leaks.t` (PERL) | Magnitude: 15.6 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 13, import: 10, safety: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `lib/Perl/Critic/Policy/Variables/ProhibitUnusedVariables.pm` (PERL) | Magnitude: 86.14 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 63, branch: 38, import: 10

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/Perl/Critic/TestUtils.pm` -> **Severity: 1.41** (Bridge: 0.0146 * Flux: 96.4687%)
- `lib/Perl/Critic/PolicyFactory.pm` -> **Severity: 0.428** (Bridge: 0.0049 * Flux: 86.6512%)
- `lib/Perl/Critic.pm` -> **Severity: 0.387** (Bridge: 0.0062 * Flux: 62.3444%)
- `lib/Perl/Critic/Config.pm` -> **Severity: 0.327** (Bridge: 0.0033 * Flux: 99.9779%)
- `lib/Perl/Critic/UserProfile.pm` -> **Severity: 0.226** (Bridge: 0.003 * Flux: 75.8469%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/Perl/Critic/Utils.pm` -> **Severity: 34.783** (Embedded: 0.7054 * Error Risk: 49.3102%)
- `lib/Perl/Critic/Utils/PPI.pm` -> **Severity: 18.356** (Embedded: 0.3932 * Error Risk: 46.6837%)
- `lib/Perl/Critic/TestUtils.pm` -> **Severity: 9.65** (Embedded: 0.1828 * Error Risk: 52.7899%)
- `lib/Perl/Critic/Config.pm` -> **Severity: 7.184** (Embedded: 0.114 * Error Risk: 63.0228%)
- `lib/Perl/Critic/PolicyFactory.pm` -> **Severity: 7.132** (Embedded: 0.1347 * Error Risk: 52.9534%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/Perl/Critic/Utils/PPI.pm` -> **Severity: 10065.8** (Blast Radius: 100.658 * Doc Risk: 100.0%)
- `lib/Perl/Critic/TestUtils.pm` -> **Severity: 3514.1** (Blast Radius: 35.141 * Doc Risk: 100.0%)
- `lib/Perl/Critic/PolicyFactory.pm` -> **Severity: 1477.5** (Blast Radius: 14.775 * Doc Risk: 100.0%)
- `lib/Perl/Critic/UserProfile.pm` -> **Severity: 897.5** (Blast Radius: 8.975 * Doc Risk: 100.0%)
- `lib/Perl/Critic/Config.pm` -> **Severity: 896.9** (Blast Radius: 8.969 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 172 literal sites + 3 sites through wrappers = 175

- `die_unsupported` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `inc/Devel/CheckOS.pm`
- `_display_version` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `lib/Perl/Critic/Command.pm`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 3391 call pairs -- scoped 12.4%, unique 0.0%, ambiguous 1.5%, external 86.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| perl | 3391 | 12.4% | 0.0% | 1.5% | 86.1% |

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
