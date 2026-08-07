# ARCHITECTURAL_BRIEF: Perl-Critic
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/Perl-Critic` |
| **Timestamp** | `2026-08-07T03:51:34.840198+00:00` |
| **Scan Duration** | `0.39s` |
| **Git Branch** | `dev` |
| **Git Commit** | `c437d557ec903c99c5114bac738a484dfedb1f9f` |
| **Git Remote** | `https://github.com/Perl-Critic/Perl-Critic.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1 malicious artifacts.

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
| Total Artifacts | 439 |
| Analyzed Artifacts (Scanned) | 82 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 357 |
| Total LOC | 9053 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 18.7% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 67 | 8997 | 81.7% |
| PLAINTEXT | 10 | 0 | 12.2% |
| MARKDOWN | 3 | 0 | 3.7% |
| HTML | 1 | 30 | 1.2% |
| DOCKERFILE | 1 | 26 | 1.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.72`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 59 | 72.0% |
| file_cluster_8 | 7 | 8.5% |
| file_cluster_13 | 2 | 2.4% |
| file_cluster_17 | 1 | 1.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 13 | 15.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 357*

**Composition by Extension & Reason:**
- `.pm`: 194x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.run`: 131x Excluded (Unsupported Extension: '.run'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 8x Unsupported Format (.undeterminable), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.pl`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 306 LOC), 1x Excluded (Machine-Generated Source Code Signature: 848 LOC)
- `.pdf`: 2x Excluded (Explicitly Denied Extension: '.pdf')
- `.pod`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')
- `.developer`: 1x Excluded (Unsupported Extension: '.developer')
- `.release`: 1x Excluded (Unsupported Extension: '.release')
- `.graffle`: 1x Excluded (Unsupported Extension: '.graffle')
- `.el`: 1x Excluded (Unsupported Extension: '.el')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 87.2 | 40.9 | 42.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.7 | 72.3 | 77.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 11.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.2 | 0.0 | 0.0 |
| API Exposure | 0.0 | 5.0 | 0.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 18.5 | 0.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 86.6 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 15.0 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 97.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 57.0 | 24.3 | 19.6 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lib/Perl/Critic/Utils/POD.pm` (Hits: 25)
- `doc/links.html` (Hits: 22)
- `t/05_utils.t` (Hits: 21)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
2. **README-prologue.md** (`README-prologue.md`) — 0 inbound connections
3. **README.md** (`README.md`) — 0 inbound connections
4. **Changes** (`Changes`) — 0 inbound connections
5. **INSTALL** (`INSTALL`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **05_utils_ppi.t** (`t/05_utils_ppi.t`) — 22 outbound dependencies
2. **perlcritic** (`bin/perlcritic`) — 20 outbound dependencies
3. **01_config.t** (`t/01_config.t`) — 18 outbound dependencies
4. **05_utils.t** (`t/05_utils.t`) — 18 outbound dependencies
5. **06_violation.t** (`t/06_violation.t`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `count_matches` (@ `t/05_utils.t`) -> Impact: **93.6** | LOC: 542
  * *Intent:* #-----------------------------------------------------------------------------
- `print_header` (@ `t/Variables/RequireLocalizedPunctuationVars.run.PL`) -> Impact: **90.7** | LOC: 293
- `test_find_keywords` (@ `t/05_utils.t`) -> Impact: **71.6** | LOC: 532
- `foo` (@ `t/05_utils.t`) -> Impact: **71.0** | LOC: 519
- `print_pass_local_deref` (@ `t/Variables/RequireLocalizedPunctuationVars.run.PL`) -> Impact: **51.7** | LOC: 134
- `_get_module_abstract_from_filehandle` (@ `lib/Perl/Critic/Utils/POD.pm`) -> Impact: **48.0** | LOC: 81
  * *Intent:* #-----------------------------------------------------------------------------
- `_test_exception_from_get_module_abstract` (@ `t/05_utils_pod.t`) -> Impact: **23.8** | LOC: 29
- `prepare_insert_statement` (@ `examples/loadanalysisdb`) -> Impact: **23.1** | LOC: 38
- `_count_main_logic_operators_and_keywords` (@ `lib/Perl/Critic/Utils/McCabe.pm`) -> Impact: **20.3** | LOC: 35
  * *Intent:* #-----------------------------------------------------------------------------
- `generate_policy_summary` (@ `inc/Perl/Critic/PolicySummaryGenerator.pm`) -> Impact: **18.6** | LOC: 111
  * *Intent:* #-----------------------------------------------------------------------------

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `t` | 40 | 3378.66 | 46.79% | 6.17% |
| `inc/Devel` | 2 | 1033.59 | 19.58% | 83.57% |
| `bin` | 1 | 913.5 | 39.55% | 14.52% |
| `lib/Perl/Critic/Utils` | 5 | 574.4 | 26.1% | 12.26% |
| `xt` | 11 | 307.28 | 45.94% | 17.09% |
| `t/Variables` | 1 | 243.86 | 72.99% | 0.0% |
| `extras` | 1 | 163.52 | 44.26% | 0.0% |
| `examples` | 2 | 98.33 | 16.15% | 0.0% |
| `__monolith__` | 7 | 91.66 | 0.0% | 0.0% |
| `inc/Perl/Critic` | 2 | 61.82 | 10.79% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `xt/99_pod_coverage.t` -> **99.9935%** Exposure
- `t/20_policy_prohibit_hard_tabs.t` -> **99.9099%** Exposure
- `inc/Devel/AssertOS.pm` -> **99.8264%** Exposure
- `doc/PolicyParameter_Notes.pod` -> **98.961%** Exposure
- `xt/81_ppi_problems.t` -> **87.9444%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bin/perlcritic` -> **100.0%** Exposure
- `lib/Perl/Critic/Utils/McCabe.pm` -> **100.0%** Exposure
- `lib/Perl/Critic/Utils/POD.pm` -> **100.0%** Exposure
- `lib/Perl/Critic/Utils/PPI.pm` -> **100.0%** Exposure
- `lib/Perl/Critic/Utils/Perl.pm` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `doc/PolicyParameter_Notes.pod` -> **0** Orphaned Functions | **3** Duplicates
- `t/05_utils_pod.t` -> **3** Orphaned Functions | **0** Duplicates
- `t/20_policy_prohibit_hard_tabs.t` -> **0** Orphaned Functions | **3** Duplicates
- `lib/Perl/Critic/Utils/PPI.pm` -> **2** Orphaned Functions | **0** Duplicates
- `t/05_utils.t` -> **0** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`extras/Dockerfile`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `566` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `t/Variables/RequireLocalizedPunctuationVars.run.PL` (PERL) -> Cumulative Risk: **478.93**
- **Archetype:** `file_cluster_0` (Distance: 12.22 IQR)
- **Magnitude:** 243.86 | **LOC:** 360 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (85.0015%), Verification (80.0%)
- **Heaviest Functions:** `print_header` (Impact: 90.7), `print_pass_local_deref` (Impact: 51.7), `print_fail_non_local_deref` (Impact: 12.4)

### 2. `xt/99_pod_coverage.t` (PERL) -> Cumulative Risk: **478.75**
- **Archetype:** `file_cluster_0` (Distance: 13.14 IQR)
- **Magnitude:** 12.6 | **LOC:** 71 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9935%), State Flux (99.9911%), Safety Score (82.5569%)
- **Heaviest Functions:** `get_trusted_methods` (Impact: 1.9)

### 3. `xt/81_ppi_problems.t` (PERL) -> Cumulative Risk: **472.48**
- **Archetype:** `file_cluster_0` (Distance: 11.654 IQR)
- **Magnitude:** 29.78 | **LOC:** 64 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9995%), Tech Debt (87.9444%), Safety Score (76.121%)

### 4. `t/14_policy_parameter_behavior_boolean.t` (PERL) -> Cumulative Risk: **464.13**
- **Archetype:** `file_cluster_0` (Distance: 12.625 IQR)
- **Magnitude:** 67.32 | **LOC:** 101 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (93.1235%), Cognitive Load (73.6975%)

### 5. `lib/Perl/Critic/Utils/PPI.pm` (PERL) -> Cumulative Risk: **451.57**
- **Archetype:** `file_cluster_0` (Distance: 12.397 IQR)
- **Magnitude:** 181.66 | **LOC:** 416 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Verification (80.0%), Safety Score (73.162%)
- **Heaviest Functions:** `is_ppi_constant_element` (Impact: 16.5), `get_constant_name_element_from_declaring` (Impact: 14.7), `is_in_subroutine` (Impact: 11.8)

### 6. `lib/Perl/Critic/Utils/POD.pm` (PERL) -> Cumulative Risk: **410.61**
- **Archetype:** `file_cluster_0` (Distance: 11.172 IQR)
- **Magnitude:** 259.62 | **LOC:** 724 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Verification (80.0%), Safety Score (72.7613%)
- **Heaviest Functions:** `_get_module_abstract_from_filehandle` (Impact: 48.0), `_get_pod_section_from_filehandle` (Impact: 8.8), `_get_pod_section_from_file` (Impact: 7.1)

### 7. `xt/94_includes.t` (PERL) -> Cumulative Risk: **408.83**
- **Archetype:** `file_cluster_0` (Distance: 12.909 IQR)
- **Magnitude:** 70.12 | **LOC:** 104 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.06%), Cognitive Load (87.1635%)
- **Heaviest Functions:** `match` (Impact: 7.7)

### 8. `t/00_versions.t` (PERL) -> Cumulative Risk: **405.3**
- **Archetype:** `file_cluster_0` (Distance: 13.807 IQR)
- **Magnitude:** 58.98 | **LOC:** 82 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.1826%), Cognitive Load (79.635%)
- **Heaviest Functions:** `check_version` (Impact: 18.1)

### 9. `xt/80_policysummary.t` (PERL) -> Cumulative Risk: **404.21**
- **Archetype:** `file_cluster_0` (Distance: 12.631 IQR)
- **Magnitude:** 68.34 | **LOC:** 96 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (92.7225%), Cognitive Load (83.3681%)

### 10. `t/13_bundled_policies.t` (PERL) -> Cumulative Risk: **403.1**
- **Archetype:** `file_cluster_0` (Distance: 12.155 IQR)
- **Magnitude:** 20.32 | **LOC:** 34 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.997%), Safety Score (78.1597%), Cognitive Load (67.9179%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `inc/Devel/CheckOS.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.315 IQR)
- **Top Global Matches:** file_cluster_0: 11.315, file_cluster_13: 11.447, file_cluster_17: 11.759
- **Magnitude:** 1025.53 | **LOC:** 333 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.722%), Tech Debt (67.3096%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 62`, `args: 1`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 54`, `fragile_debt: 4`
* *Architecture:* `io: 1`, `api: 6`, `import: 16`
* *Defense:* `safety: 1`, `doc: 31`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, warnings, this, match, File::Find::Rule, Devel::CheckOS, Devel::AssertOS, vars...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/perlcritic` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.659 IQR)
- **Top Global Matches:** file_cluster_0: 14.659, file_cluster_13: 14.831, file_cluster_17: 14.875
- **Magnitude:** 913.5 | **LOC:** 1049 | **CtrlFlow:** 83.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.5531%), Tech Debt (14.5246%)
**Top Internal Functions/Classes:**
  * `complicated_function` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 42`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 898`, `planned_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 13`, `concurrency: 1`, `import: 26`
* *Defense:* `safety: 4`, `doc: 90`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` quotes, strict, parentheses, the, of, with, just, errors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/03_pragmas.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.319 IQR)
- **Top Global Matches:** file_cluster_13: 12.319, file_cluster_8: 12.541, file_cluster_0: 12.646
- **Magnitude:** 787.3 | **LOC:** 969 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.5343%), Tech Debt (19.627%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 212`, `func_start: 4`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 279`, `fragile_debt: 4`
* *Architecture:* `import: 69`
* *Defense:* `safety: 62`, `doc: 6`, `test: 33`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, warnings, Test::More, Perl::Critic::TestUtils, Perl::Critic::PolicyFactory, critic
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/05_utils.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.706 IQR)
- **Top Global Matches:** file_cluster_0: 11.706, file_cluster_13: 12.012, file_cluster_8: 12.196
- **Magnitude:** 448.48 | **LOC:** 633 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.8177%), Tech Debt (23.9938%)
**Top Internal Functions/Classes:**
  * `count_matches` (Impact: 93.6)
    * *Intent:* #-----------------------------------------------------------------------------
  * `test_find_keywords` (Impact: 71.6)
  * `foo` (Impact: 71.0)
  * `make_doc` (Impact: 4.5)
  * `test_export` (Impact: 2.4)
    * *Intent:* #-----------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 216`, `args: 2`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 2`, `state_mutation: 195`, `duplicate_logic: 2`
* *Architecture:* `io: 21`, `import: 24`
* *Defense:* `safety: 10`, `test: 64`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Temp, Carp, Fatal, warnings, strict, of, autodie, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Utils/POD.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.172 IQR)
- **Top Global Matches:** file_cluster_0: 11.172, file_cluster_8: 11.421, file_cluster_13: 11.43
- **Magnitude:** 259.62 | **LOC:** 724 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.8991%), Tech Debt (10.7939%)
**Top Internal Functions/Classes:**
  * `_get_module_abstract_from_filehandle` (Impact: 48.0)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_get_pod_section_from_filehandle` (Impact: 8.8)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_get_pod_section_from_file` (Impact: 7.1)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_get_module_abstract_from_file` (Impact: 7.1)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_get_pod_section_from_string` (Impact: 6.7)
    * *Intent:* #-----------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 125`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 101`, `planned_debt: 1`
* *Architecture:* `io: 25`, `api: 3`, `import: 14`
* *Defense:* `safety: 2`, `doc: 31`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Pod::Select, strict, warnings, abstract, hyphen, English, Perl::Critic::Exception::Fatal::Generic, Perl::Critic::Utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/Variables/RequireLocalizedPunctuationVars.run.PL` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.22 IQR)
- **Top Global Matches:** file_cluster_0: 12.22, file_cluster_8: 12.244, file_cluster_13: 12.262
- **Magnitude:** 243.86 | **LOC:** 360 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.9921%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `print_header` (Impact: 90.7)
  * `print_pass_local_deref` (Impact: 51.7)
  * `print_fail_non_local_deref` (Impact: 12.4)
  * `print_pass_local` (Impact: 11.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 64`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 74`
* *Architecture:* `io: 5`, `import: 6`
* *Defense:* `safety: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, strict, warnings, English, List::SomeUtils, space, B::Keywords, critic
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/06_violation.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.028 IQR)
- **Top Global Matches:** file_cluster_0: 11.028, file_cluster_13: 11.554, file_cluster_8: 11.784
- **Magnitude:** 233.18 | **LOC:** 291 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.2374%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 72`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 71`, `dead_code: 1`
* *Architecture:* `import: 15`
* *Defense:* `safety: 4`, `test: 46`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, warnings, diagnostics, Perl::Critic::Policy::Test, Test::More, English, Perl::Critic::TestUtils, lib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Utils/PPI.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.397 IQR)
- **Top Global Matches:** file_cluster_0: 12.397, file_cluster_13: 12.945, file_cluster_17: 13.234
- **Magnitude:** 181.66 | **LOC:** 416 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.8973%), Tech Debt (50.4941%)
**Top Internal Functions/Classes:**
  * `is_ppi_constant_element` (Impact: 16.5)
    * *Intent:* #-----------------------------------------------------------------------------
  * `get_constant_name_element_from_declaring` (Impact: 14.7)
    * *Intent:* #-----------------------------------------------------------------------------
  * `is_in_subroutine` (Impact: 11.8)
    * *Intent:* #-----------------------------------------------------------------------------
  * `is_subroutine_declaration` (Impact: 8.0)
    * *Intent:* #-----------------------------------------------------------------------------
  * `get_previous_module_used_on_same_line` (Impact: 7.9)
    * *Intent:* #-----------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 110`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 83`, `planned_debt: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `import: 13`
* *Defense:* `safety: 18`, `doc: 21`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Readonly, strict, warnings, next, Scalar::Util, version, L, hashify...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extras/Dockerfile` (DOCKERFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.924 IQR)
- **Top Global Matches:** file_cluster_8: 6.924, file_cluster_7: 8.111, file_cluster_13: 8.144
- **Magnitude:** 163.52 | **LOC:** 32 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.2562%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 6`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` alpine:latest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/09_theme.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.507 IQR)
- **Top Global Matches:** file_cluster_17: 12.507, file_cluster_0: 12.552, file_cluster_13: 12.926
- **Magnitude:** 158.78 | **LOC:** 319 | **CtrlFlow:** 71.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.8517%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `has_theme` (Impact: 1.9)
    * *Intent:* #-----------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 31`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 152`
* *Architecture:* `import: 10`
* *Defense:* `safety: 4`, `test: 31`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::UserProfile, strict, warnings, Test::More, English, Perl::Critic::TestUtils, Perl::Critic::PolicyFactory, List::SomeUtils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/05_utils_pod.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.712 IQR)
- **Top Global Matches:** file_cluster_8: 10.712, file_cluster_0: 10.867, file_cluster_13: 10.879
- **Magnitude:** 137.78 | **LOC:** 691 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.9042%), Tech Debt (16.8848%)
**Top Internal Functions/Classes:**
  * `_test_exception_from_get_module_abstract` (Impact: 23.8)
  * `test_exception_from_get_raw_module_abstr` (Impact: 4.3)
    * *Intent:* #-----------------------------------------------------------------------------
  * `test_exception_from_get_module_abstract_` (Impact: 4.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 92`, `args: 3`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 96`, `orphaned_logic: 3`
* *Architecture:* `import: 16`
* *Defense:* `safety: 5`, `doc: 34`, `test: 38`, `immutability_locks: 2`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, Readonly, strict, warnings, hyphen, Test::More, English, Perl::Critic::TestUtils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/01_config.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.958 IQR)
- **Top Global Matches:** file_cluster_0: 11.958, file_cluster_17: 12.44, file_cluster_13: 12.506
- **Magnitude:** 134.42 | **LOC:** 555 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.3936%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 100`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 112`, `dead_code: 5`
* *Architecture:* `io: 1`, `import: 13`
* *Defense:* `safety: 7`, `test: 81`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` enabled, IO::Interactive, strict, warnings, Perl::Critic::Utils::Constants, policies, Test::More, English...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/03_annotations.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.909 IQR)
- **Top Global Matches:** file_cluster_0: 11.909, file_cluster_13: 12.125, file_cluster_8: 12.18
- **Magnitude:** 103.12 | **LOC:** 244 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.7487%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `annotate` (Impact: 12.7)
  * `choose_annotation` (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 36`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 84`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `doc: 2`, `test: 30`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, warnings, Test::More, Perl::Critic::TestUtils, PPI::Document, Perl::Critic::Annotation, critic
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/07_command.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.515 IQR)
- **Top Global Matches:** file_cluster_0: 11.515, file_cluster_13: 11.792, file_cluster_8: 11.861
- **Magnitude:** 95.56 | **LOC:** 281 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.4823%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 54`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 77`
* *Architecture:* `import: 11`
* *Defense:* `safety: 11`, `test: 39`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, strict, warnings, Test::More, English, Perl::Critic::TestUtils, arguments, Perl::Critic::Utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/14_policy_parameter_behavior_enumeration.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.911 IQR)
- **Top Global Matches:** file_cluster_0: 12.911, file_cluster_13: 13.134, file_cluster_8: 13.439
- **Magnitude:** 91.4 | **LOC:** 163 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.5536%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 15`
* *Risk/State:* `state_mutation: 74`
* *Architecture:* `import: 16`
* *Defense:* `safety: 8`, `test: 25`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, warnings, Perl::Critic::Policy, Test::More, English, Perl::Critic::TestUtils, Perl::Critic::PolicyParameter, value...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/loadanalysisdb` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.612 IQR)
- **Top Global Matches:** file_cluster_0: 10.612, file_cluster_13: 10.663, file_cluster_8: 10.68
- **Magnitude:** 86.4 | **LOC:** 345 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.0047%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `prepare_insert_statement` (Impact: 23.1)
  * `load` (Impact: 11.9)
  * `execute_insert_statement` (Impact: 4.4)
  * `connect_to_database` (Impact: 4.0)
  * `main` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 46`, `args: 5`, `func_start: 7`
* *Risk/State:* `state_mutation: 29`
* *Architecture:* `io: 2`, `import: 11`
* *Defense:* `safety: 4`, `doc: 17`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DBI, Carp, Readonly, strict, warnings, version, English, Perl::Critic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Utils/McCabe.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.368 IQR)
- **Top Global Matches:** file_cluster_0: 12.368, file_cluster_13: 12.707, file_cluster_17: 12.871
- **Magnitude:** 83.56 | **LOC:** 204 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.3103%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_count_main_logic_operators_and_keywords` (Impact: 20.3)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_count_logic_keywords` (Impact: 6.1)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_count_logic_operators` (Impact: 6.1)
    * *Intent:* #-----------------------------------------------------------------------------
  * `calculate_mccabe_of_sub` (Impact: 3.1)
    * *Intent:* #-----------------------------------------------------------------------------
  * `calculate_mccabe_of_main` (Impact: 3.0)
    * *Intent:* #-----------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 52`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 41`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 5`, `doc: 13`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Readonly, strict, warnings, Perl::Critic::Utils, Exporter, critic
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/14_policy_parameter_behavior_list_string.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.198 IQR)
- **Top Global Matches:** file_cluster_0: 12.198, file_cluster_13: 12.284, file_cluster_8: 12.448
- **Magnitude:** 78.72 | **LOC:** 168 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.4985%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 13`
* *Risk/State:* `state_mutation: 61`
* *Architecture:* `import: 16`
* *Defense:* `safety: 2`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, warnings, Perl::Critic::Policy, Test::More, Perl::Critic::TestUtils, Perl::Critic::PolicyParameter, value, default
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/14_policy_parameter_behavior_integer.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.51 IQR)
- **Top Global Matches:** file_cluster_0: 12.51, file_cluster_13: 12.794, file_cluster_8: 13.112
- **Magnitude:** 78.38 | **LOC:** 169 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.1304%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 14`
* *Risk/State:* `state_mutation: 61`
* *Architecture:* `import: 17`
* *Defense:* `safety: 7`, `test: 23`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, warnings, Perl::Critic::Policy, Test::More, English, Perl::Critic::TestUtils, Perl::Critic::PolicyParameter, value...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/94_includes.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.909 IQR)
- **Top Global Matches:** file_cluster_0: 12.909, file_cluster_13: 13.1, file_cluster_8: 13.439
- **Magnitude:** 70.12 | **LOC:** 104 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.1635%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `match` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 35`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 61`
* *Architecture:* `import: 7`
* *Defense:* `safety: 5`, `test: 4`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, strict, warnings, Test::More, Perl::Critic::TestUtils, PPI::Document, File::Find
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/80_policysummary.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.631 IQR)
- **Top Global Matches:** file_cluster_0: 12.631, file_cluster_13: 12.736, file_cluster_8: 13.122
- **Magnitude:** 68.34 | **LOC:** 96 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.3681%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 32`
* *Risk/State:* `state_mutation: 52`
* *Architecture:* `io: 4`, `import: 8`
* *Defense:* `safety: 4`, `test: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, strict, warnings, Test::More, English, Perl::Critic::TestUtils, Perl::Critic::PolicyFactory, File::Spec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/14_policy_parameter_behavior_boolean.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.625 IQR)
- **Top Global Matches:** file_cluster_0: 12.625, file_cluster_13: 12.826, file_cluster_11: 13.216
- **Magnitude:** 67.32 | **LOC:** 101 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.6975%), Tech Debt (71.2814%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 17`
* *Risk/State:* `state_mutation: 51`, `planned_debt: 2`
* *Architecture:* `import: 14`
* *Defense:* `safety: 2`, `test: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, warnings, Perl::Critic::Policy, Test::More, English, Perl::Critic::TestUtils, Perl::Critic::Utils, Perl::Critic::PolicyParameter...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/16_roundtrip_defaults.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.617 IQR)
- **Top Global Matches:** file_cluster_0: 10.617, file_cluster_8: 10.788, file_cluster_13: 10.895
- **Magnitude:** 62.96 | **LOC:** 198 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.2999%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 49`, `args: 4`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* `import: 8`
* *Defense:* `safety: 4`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, warnings, Test::More, Perl::Critic::TestUtils, Perl::Critic::PolicyFactory, Perl::Critic::Utils, Perl::Critic::Config, Perl::Critic::ProfilePrototype...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/14_policy_parameters.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.941 IQR)
- **Top Global Matches:** file_cluster_0: 11.941, file_cluster_13: 12.109, file_cluster_8: 12.44
- **Magnitude:** 61.6 | **LOC:** 124 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.26%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_supported_parameters` (Impact: 11.6)
    * *Intent:* #-----------------------------------------------------------------------------
  * `test_invalid_parameters` (Impact: 5.5)
    * *Intent:* #-----------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 37`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 43`
* *Architecture:* `import: 9`
* *Defense:* `safety: 4`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::UserProfile, strict, warnings, Test::More, English, Perl::Critic::TestUtils, Perl::Critic::PolicyFactory, Perl::Critic::Utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/00_versions.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.807 IQR)
- **Top Global Matches:** file_cluster_0: 13.807, file_cluster_13: 13.844, file_cluster_17: 13.982
- **Magnitude:** 58.98 | **LOC:** 82 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.635%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `check_version` (Impact: 18.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 28`, `args: 1`, `func_start: 3`
* *Risk/State:* `state_mutation: 40`
* *Architecture:* `io: 2`, `import: 7`
* *Defense:* `safety: 5`, `test: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, strict, warnings, Test::More, English, Perl::Critic::TestUtils, File::Find
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `t/20_policy_require_consistent_newlines.t` (PERL) | Magnitude: 43.12 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 27, indent_spaces: 20, structural_boundaries: 18, decorators: 12
- `t/Variables/RequireLocalizedPunctuationVars.run.PL` (PERL) | Magnitude: 243.86 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 105, state_mutation: 74, structural_boundaries: 64, encapsulation: 45
- `t/00_versions.t` (PERL) | Magnitude: 58.98 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 40, structural_boundaries: 28, indent_spaces: 25, regex_execution: 13
- `examples/loadanalysisdb` (PERL) | Magnitude: 86.4 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 121, structural_boundaries: 46, state_mutation: 29, decorators: 26
- `tools/ppidump` (PERL) | Magnitude: 0.04 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 24, branch: 10, structural_boundaries: 9, decorators: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `examples/generatestats` (PERL) | Magnitude: 11.93 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 98, structural_boundaries: 55, state_mutation: 48, encapsulation: 28
- `t/03_pragmas.t` (PERL) | Magnitude: 787.3 | Delta: **0.222 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 279, indent_spaces: 243, structural_boundaries: 212, encapsulation: 71

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `t/09_theme.t` (PERL) | Magnitude: 158.78 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 219, state_mutation: 152, branch: 79, decorators: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `t/01_policy_config.t` (PERL) | Magnitude: 23.6 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 29, test: 20, decorators: 18
- `t/05_utils_pod.t` (PERL) | Magnitude: 137.78 | Delta: **0.155 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 309, state_mutation: 96, structural_boundaries: 92, encapsulation: 57
- `t/20_policy_prohibit_hard_tabs.t` (PERL) | Magnitude: 24.44 | Delta: **0.256 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 19, structural_boundaries: 14, bitwise_ops: 12, test: 11
- `doc/PolicyParameter_Notes.pod` (PERL) | Magnitude: 15.88 | Delta: **0.506 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 26, decorators: 20, bitwise_ops: 13

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/13_bundled_policies.t` -> **Severity: 687.009** (Blast Radius: 12.048 * Doc Risk: 57.0227%)
- `t/07_perlcritic.t` -> **Severity: 677.813** (Blast Radius: 12.048 * Doc Risk: 56.2594%)
- `extras/Dockerfile` -> **Severity: 654.651** (Blast Radius: 12.048 * Doc Risk: 54.3369%)
- `t/20_policies.t` -> **Severity: 617.654** (Blast Radius: 12.048 * Doc Risk: 51.2661%)
- `t/20_policy_prohibit_evil_modules.t` -> **Severity: 603.906** (Blast Radius: 12.048 * Doc Risk: 50.125%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
