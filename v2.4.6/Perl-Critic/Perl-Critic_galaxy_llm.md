# ARCHITECTURAL_BRIEF: Perl-Critic
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/Perl-Critic` |
| **Timestamp** | `2026-08-03T19:29:28.453928+00:00` |
| **Scan Duration** | `0.47s` |
| **Git Branch** | `dev` |
| **Git Commit** | `c437d557ec903c99c5114bac738a484dfedb1f9f` |
| **Git Remote** | `https://github.com/Perl-Critic/Perl-Critic.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1 malicious artifacts.

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
> **Assigned Ecosystem Baseline:** `Cluster 4`
> **Architectural Drift Z-Score:** `9.692`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 60 | 73.2% |
| file_cluster_8 | 6 | 7.3% |
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
| Cognitive Load Exposure | 5.0 | 96.3 | 64.0 | 84.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 38.2 | 35.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.7 | 0.0 | 0.0 |
| API Exposure | 0.0 | 5.0 | 0.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 18.5 | 0.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 90.3 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 15.0 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 97.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 95.8 | 36.0 | 28.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 14.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 23.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 5.6 | 0.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `count_matches` (@ `t/05_utils.t`) -> Impact: **1647.8** | LOC: 542
  * *Intent:* #-----------------------------------------------------------------------------
- `get_constant_name_element_from_declaring` (@ `lib/Perl/Critic/Utils/PPI.pm`) -> Impact: **251.7** | LOC: 26
  * *Intent:* #-----------------------------------------------------------------------------
- `foo` (@ `t/05_utils_ppi.t`) -> Impact: **219.2** | LOC: 65
- `print_header` (@ `t/Variables/RequireLocalizedPunctuationVars.run.PL`) -> Impact: **166.7** | LOC: 293
- `is_ppi_constant_element` (@ `lib/Perl/Critic/Utils/PPI.pm`) -> Impact: **160.0** | LOC: 18
  * *Intent:* #-----------------------------------------------------------------------------
- `_get_module_abstract_from_filehandle` (@ `lib/Perl/Critic/Utils/POD.pm`) -> Impact: **148.1** | LOC: 81
  * *Intent:* #-----------------------------------------------------------------------------
- `required_module_versions` (@ `inc/Perl/Critic/BuildUtilities.pm`) -> Impact: **124.0** | LOC: 49
- `_count_main_logic_operators_and_keywords` (@ `lib/Perl/Critic/Utils/McCabe.pm`) -> Impact: **102.3** | LOC: 35
  * *Intent:* #-----------------------------------------------------------------------------
- `_test_exception_from_get_module_abstract` (@ `t/05_utils_pod.t`) -> Impact: **102.1** | LOC: 29
- `generate_policy_summary` (@ `inc/Perl/Critic/PolicySummaryGenerator.pm`) -> Impact: **93.0** | LOC: 111
  * *Intent:* #-----------------------------------------------------------------------------

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `count_matches` (@ `t/05_utils.t`) -> **O(2^N) [Recursive]**
  * *Intent:* #-----------------------------------------------------------------------------
- `get_constant_name_element_from_declaring` (@ `lib/Perl/Critic/Utils/PPI.pm`) -> **O(2^N) [Recursive]**
  * *Intent:* #-----------------------------------------------------------------------------
- `foo` (@ `t/05_utils_ppi.t`) -> **O(2^N) [Recursive]**
- `os_is` (@ `inc/Devel/AssertOS/Solaris.pm`) -> **O(2^N) [Recursive]**
- `default_maximum_violations_per_document` (@ `t/02_policy.t`) -> **O(2^N) [Recursive]**
- `can_podspell` (@ `t/20_policy_pod_spelling.t`) -> **O(2^N) [Recursive]**
- `foo` (@ `t/20_policy_require_tidy_code.t`) -> **O(2^N) [Recursive]**
- `match` (@ `xt/94_includes.t`) -> **O(2^N) [Recursive]**
- `_get_module_abstract_from_filehandle` (@ `lib/Perl/Critic/Utils/POD.pm`) -> **O(N^5)**
  * *Intent:* #-----------------------------------------------------------------------------
- `prepare_insert_statement` (@ `examples/loadanalysisdb`) -> **O(N^4)**

### Highest Data Gravity (Database Complexity)
- `count_matches` (@ `t/05_utils.t`) -> DB Complexity: **171**
  * *Intent:* #-----------------------------------------------------------------------------
- `check_version` (@ `t/00_versions.t`) -> DB Complexity: **21**
- `print_header` (@ `t/Variables/RequireLocalizedPunctuationVars.run.PL`) -> DB Complexity: **20**
- `generate_policy_summary` (@ `inc/Perl/Critic/PolicySummaryGenerator.pm`) -> DB Complexity: **19**
  * *Intent:* #-----------------------------------------------------------------------------
- `test_supported_parameters` (@ `t/14_policy_parameters.t`) -> DB Complexity: **17**
  * *Intent:* #-----------------------------------------------------------------------------
- `summarize` (@ `examples/generatestats`) -> DB Complexity: **14**
- `_get_pod_section_from_file` (@ `lib/Perl/Critic/Utils/POD.pm`) -> DB Complexity: **13**
  * *Intent:* #-----------------------------------------------------------------------------
- `_get_module_abstract_from_file` (@ `lib/Perl/Critic/Utils/POD.pm`) -> DB Complexity: **13**
  * *Intent:* #-----------------------------------------------------------------------------
- `trim_raw_pod_section` (@ `lib/Perl/Critic/Utils/POD.pm`) -> DB Complexity: **12**
  * *Intent:* #-----------------------------------------------------------------------------
- `trim_pod_section` (@ `lib/Perl/Critic/Utils/POD.pm`) -> DB Complexity: **12**
  * *Intent:* #-----------------------------------------------------------------------------

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `t` | 40 | 9861.38 | 75.86% | 5.57% |
| `inc/Devel` | 2 | 2520.87 | 34.76% | 83.57% |
| `lib/Perl/Critic/Utils` | 5 | 1459.4 | 43.44% | 12.26% |
| `bin` | 1 | 995.5 | 44.29% | 14.52% |
| `xt` | 11 | 336.78 | 66.23% | 17.09% |
| `inc/Perl/Critic` | 2 | 287.22 | 37.32% | 0.0% |
| `t/Variables` | 1 | 248.16 | 81.1% | 0.0% |
| `examples` | 2 | 171.4 | 24.79% | 0.0% |
| `extras` | 1 | 163.52 | 44.26% | 0.0% |
| `doc` | 2 | 104.48 | 9.25% | 49.48% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `xt/99_pod_coverage.t` -> **99.9935%** Exposure
- `t/20_policy_prohibit_hard_tabs.t` -> **99.9099%** Exposure
- `inc/Devel/AssertOS.pm` -> **99.8264%** Exposure
- `doc/PolicyParameter_Notes.pod` -> **98.961%** Exposure
- `xt/81_ppi_problems.t` -> **87.9444%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bin/perlcritic` -> **100.0%** Exposure
- `lib/Perl/Critic/Utils/Constants.pm` -> **100.0%** Exposure
- `lib/Perl/Critic/Utils/McCabe.pm` -> **100.0%** Exposure
- `lib/Perl/Critic/Utils/POD.pm` -> **100.0%** Exposure
- `lib/Perl/Critic/Utils/PPI.pm` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `doc/PolicyParameter_Notes.pod` -> **0** Orphaned Functions | **3** Duplicates
- `t/05_utils_pod.t` -> **3** Orphaned Functions | **0** Duplicates
- `t/20_policy_prohibit_hard_tabs.t` -> **0** Orphaned Functions | **3** Duplicates
- `lib/Perl/Critic/Utils/PPI.pm` -> **2** Orphaned Functions | **0** Duplicates
- `bin/perlcritic` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`extras/Dockerfile`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `examples/loadanalysisdb` -> **100.0%** Exposure
- `inc/Perl/Critic/PolicySummaryGenerator.pm` -> **100.0%** Exposure
- `lib/Perl/Critic/Utils/POD.pm` -> **100.0%** Exposure
- `lib/Perl/Critic/Utils/PPI.pm` -> **100.0%** Exposure
- `t/03_annotations.t` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `t/05_utils.t` -> **5.5823%** Exposure
### Algorithmic DoS Exposure
- `inc/Perl/Critic/PolicySummaryGenerator.pm` -> **100.0%** Exposure
- `lib/Perl/Critic/Utils/McCabe.pm` -> **100.0%** Exposure
- `lib/Perl/Critic/Utils/POD.pm` -> **100.0%** Exposure
- `lib/Perl/Critic/Utils/PPI.pm` -> **100.0%** Exposure
- `t/05_utils.t` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `566` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `t/Variables/RequireLocalizedPunctuationVars.run.PL` (PERL) -> Cumulative Risk: **629.11**
- **Archetype:** `file_cluster_0` (Distance: 12.416 IQR)
- **Magnitude:** 248.16 | **LOC:** 360 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `print_header` (Impact: 166.7)

### 2. `lib/Perl/Critic/Utils/PPI.pm` (PERL) -> Cumulative Risk: **609.87**
- **Archetype:** `file_cluster_0` (Distance: 12.8 IQR)
- **Magnitude:** 670.16 | **LOC:** 416 | **CtrlFlow:** 80.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `get_constant_name_element_from_declaring` (Impact: 251.7), `is_ppi_constant_element` (Impact: 160.0), `is_subroutine_declaration` (Impact: 46.9)

### 3. `t/14_policy_parameters.t` (PERL) -> Cumulative Risk: **586.67**
- **Archetype:** `file_cluster_0` (Distance: 12.84 IQR)
- **Magnitude:** 145.4 | **LOC:** 124 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9999%)
- **Heaviest Functions:** `test_supported_parameters` (Impact: 80.9)

### 4. `lib/Perl/Critic/Utils/McCabe.pm` (PERL) -> Cumulative Risk: **575.58**
- **Archetype:** `file_cluster_0` (Distance: 12.557 IQR)
- **Magnitude:** 202.56 | **LOC:** 204 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9872%)
- **Heaviest Functions:** `_count_main_logic_operators_and_keywords` (Impact: 102.3), `_count_logic_keywords` (Impact: 24.6), `_count_logic_operators` (Impact: 24.6)

### 5. `t/05_utils.t` (PERL) -> Cumulative Risk: **571.93**
- **Archetype:** `file_cluster_0` (Distance: 12.865 IQR)
- **Magnitude:** 1968.38 | **LOC:** 633 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `count_matches` (Impact: 1647.8), `test_export` (Impact: 6.3)

### 6. `lib/Perl/Critic/Utils/POD.pm` (PERL) -> Cumulative Risk: **562.32**
- **Archetype:** `file_cluster_0` (Distance: 11.519 IQR)
- **Magnitude:** 507.12 | **LOC:** 724 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_get_module_abstract_from_filehandle` (Impact: 148.1), `get_raw_module_abstract_from_file` (Impact: 13.9), `get_raw_module_abstract_from_filehandle` (Impact: 13.9)

### 7. `inc/Perl/Critic/PolicySummaryGenerator.pm` (PERL) -> Cumulative Risk: **545.45**
- **Archetype:** `file_cluster_0` (Distance: 12.082 IQR)
- **Magnitude:** 124.32 | **LOC:** 211 | **CtrlFlow:** 75.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9262%)
- **Heaviest Functions:** `generate_policy_summary` (Impact: 93.0)

### 8. `t/00_versions.t` (PERL) -> Cumulative Risk: **518.73**
- **Archetype:** `file_cluster_0` (Distance: 14.199 IQR)
- **Magnitude:** 87.48 | **LOC:** 82 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (97.5407%), Cognitive Load (92.0893%)
- **Heaviest Functions:** `check_version` (Impact: 38.6)

### 9. `t/08_document.t` (PERL) -> Cumulative Risk: **486.01**
- **Archetype:** `file_cluster_0` (Distance: 12.128 IQR)
- **Magnitude:** 106.62 | **LOC:** 194 | **CtrlFlow:** 72.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Cognitive Load (89.6482%)
- **Heaviest Functions:** `test_version` (Impact: 32.1)

### 10. `xt/99_pod_coverage.t` (PERL) -> Cumulative Risk: **484.06**
- **Archetype:** `file_cluster_0` (Distance: 13.537 IQR)
- **Magnitude:** 15.1 | **LOC:** 71 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9991%), Tech Debt (99.9935%), Cognitive Load (91.0053%)
- **Heaviest Functions:** `get_trusted_methods` (Impact: 2.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `t/06_violation.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.596 IQR)
- **Top Global Matches:** file_cluster_0: 12.596, file_cluster_13: 13.079, file_cluster_17: 13.339
- **Magnitude:** 3551.3 | **LOC:** 291 | **CtrlFlow:** 76.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.0807%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 71`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 137`, `dead_code: 1`
* *Architecture:* `import: 15`
* *Defense:* `safety: 4`, `test: 46`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::TestUtils, warnings, PPI::Document, ViolationTest, File::Spec::Functions, diagnostics, English, Perl::Critic::Utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `inc/Devel/CheckOS.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.605 IQR)
- **Top Global Matches:** file_cluster_0: 11.605, file_cluster_13: 11.74, file_cluster_17: 12.04
- **Magnitude:** 2502.31 | **LOC:** 333 | **CtrlFlow:** 74.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (39.385%), Tech Debt (67.3096%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 55`, `args: 1`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 60`, `fragile_debt: 4`
* *Architecture:* `io: 1`, `api: 6`, `import: 16`
* *Defense:* `safety: 1`, `doc: 31`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vars, warnings, match, the, Exporter, Devel::CheckOS, Devel::AssertOS, File::Spec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/05_utils.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.865 IQR)
- **Top Global Matches:** file_cluster_0: 12.865, file_cluster_13: 13.141, file_cluster_11: 13.385
- **Magnitude:** 1968.38 | **LOC:** 633 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 171
- **Risk Profile:** Cognitive Load (89.0399%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `count_matches` (Impact: 1647.8 | O(2^N) | DB: 171)
    * *Intent:* #-----------------------------------------------------------------------------
  * `test_export` (Impact: 6.3 | O(N^1))
    * *Intent:* #-----------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 154`, `args: 2`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 2`, `state_mutation: 305`
* *Architecture:* `io: 21`, `import: 24`
* *Defense:* `safety: 10`, `test: 64`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::TestUtils, warnings, PPI::Document, File::Temp, strict, autodie, doc, Perl::Critic::Utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/03_pragmas.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.544 IQR)
- **Top Global Matches:** file_cluster_13: 12.544, file_cluster_8: 12.779, file_cluster_0: 12.86
- **Magnitude:** 1338.8 | **LOC:** 969 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (57.7836%), Tech Debt (19.627%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 206`, `func_start: 4`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 283`, `fragile_debt: 4`
* *Architecture:* `import: 69`
* *Defense:* `safety: 62`, `doc: 6`, `test: 33`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::TestUtils, warnings, Test::More, Perl::Critic::PolicyFactory, strict, critic
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/perlcritic` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.828 IQR)
- **Top Global Matches:** file_cluster_0: 14.828, file_cluster_13: 15.003, file_cluster_17: 15.037
- **Magnitude:** 995.5 | **LOC:** 1049 | **CtrlFlow:** 91.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (44.2861%), Tech Debt (14.5246%)
**Top Internal Functions/Classes:**
  * `complicated_function` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 437`, `structural_boundaries: 40`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 980`, `planned_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 13`, `concurrency: 1`, `import: 26`
* *Defense:* `safety: 4`, `doc: 90`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` arguments, errors, it, strict, critic, warnings, about, quotes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Utils/PPI.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.8 IQR)
- **Top Global Matches:** file_cluster_0: 12.8, file_cluster_13: 13.332, file_cluster_11: 13.535
- **Magnitude:** 670.16 | **LOC:** 416 | **CtrlFlow:** 80.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (45.4216%), Tech Debt (50.4941%)
**Top Internal Functions/Classes:**
  * `get_constant_name_element_from_declaring` (Impact: 251.7 | O(2^N) | DB: 1)
    * *Intent:* #-----------------------------------------------------------------------------
  * `is_ppi_constant_element` (Impact: 160.0 | O(N^4) | DB: 2)
    * *Intent:* #-----------------------------------------------------------------------------
  * `is_subroutine_declaration` (Impact: 46.9 | O(N^4) | DB: 3)
    * *Intent:* #-----------------------------------------------------------------------------
  * `get_previous_module_used_on_same_line` (Impact: 26.3 | O(N^3) | DB: 4)
    * *Intent:* #-----------------------------------------------------------------------------
  * `get_next_element_in_same_simple_statemen` (Impact: 26.2 | O(N^3) | DB: 4)
    * *Intent:* #-----------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 404`, `structural_boundaries: 98`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 87`, `planned_debt: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `import: 13`
* *Defense:* `safety: 18`, `doc: 21`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` next, warnings, L, Exporter, Scalar::Util, hashify, version, constant...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Utils/POD.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.519 IQR)
- **Top Global Matches:** file_cluster_0: 11.519, file_cluster_13: 11.776, file_cluster_8: 11.803
- **Magnitude:** 507.12 | **LOC:** 724 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (42.7498%), Tech Debt (10.7939%)
**Top Internal Functions/Classes:**
  * `_get_module_abstract_from_filehandle` (Impact: 148.1 | O(N^5) | DB: 11)
    * *Intent:* #-----------------------------------------------------------------------------
  * `get_raw_module_abstract_from_file` (Impact: 13.9 | O(N^3))
    * *Intent:* #-----------------------------------------------------------------------------
  * `get_raw_module_abstract_from_filehandle` (Impact: 13.9 | O(N^3))
    * *Intent:* #-----------------------------------------------------------------------------
  * `get_raw_module_abstract_from_string` (Impact: 13.9 | O(N^3))
    * *Intent:* #-----------------------------------------------------------------------------
  * `get_module_abstract_from_file` (Impact: 13.9 | O(N^3))
    * *Intent:* #-----------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 99`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 105`, `planned_debt: 1`
* *Architecture:* `io: 25`, `api: 3`, `import: 14`
* *Defense:* `safety: 2`, `doc: 31`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hyphen, such, warnings, Pod::Select, critic, English, Perl::Critic::Utils, Exporter...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/05_utils_ppi.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.667 IQR)
- **Top Global Matches:** file_cluster_0: 10.667, file_cluster_13: 11.276, file_cluster_8: 11.324
- **Magnitude:** 267.6 | **LOC:** 380 | **CtrlFlow:** 90.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (52.8095%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `foo` (Impact: 219.2 | O(2^N) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 529`, `structural_boundaries: 56`, `args: 5`
* *Risk/State:* `state_mutation: 42`
* *Architecture:* `import: 21`
* *Defense:* `safety: 2`, `test: 51`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PPI::Statement::Scheduled, PPI::Statement::Include, Test::More, PPI::Token::Word, PPI::Statement::Sub, PPI::Statement::Null, strict, PPI::Statement::End...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/05_utils_pod.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.658 IQR)
- **Top Global Matches:** file_cluster_8: 11.658, file_cluster_0: 11.697, file_cluster_13: 11.716
- **Magnitude:** 249.48 | **LOC:** 691 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (28.2817%), Tech Debt (16.8848%)
**Top Internal Functions/Classes:**
  * `_test_exception_from_get_module_abstract` (Impact: 102.1 | O(N^4) | DB: 2)
  * `test_exception_from_get_raw_module_abstr` (Impact: 6.0 | O(N^2) | DB: 3)
    * *Intent:* #-----------------------------------------------------------------------------
  * `test_exception_from_get_module_abstract_` (Impact: 6.0 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 89`, `args: 3`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 126`, `orphaned_logic: 3`
* *Architecture:* `import: 16`
* *Defense:* `safety: 5`, `doc: 34`, `test: 38`, `immutability_locks: 2`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hyphen, Perl::Critic::TestUtils, warnings, English, name, Test::More, a, abstract...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/Variables/RequireLocalizedPunctuationVars.run.PL` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.416 IQR)
- **Top Global Matches:** file_cluster_0: 12.416, file_cluster_8: 12.459, file_cluster_13: 12.46
- **Magnitude:** 248.16 | **LOC:** 360 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (81.1019%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `print_header` (Impact: 166.7 | O(N^3) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 56`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 78`
* *Architecture:* `io: 5`, `import: 6`
* *Defense:* `safety: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, space, B::Keywords, English, List::SomeUtils, Carp, strict, critic
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Perl/Critic/Utils/McCabe.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.557 IQR)
- **Top Global Matches:** file_cluster_0: 12.557, file_cluster_13: 12.89, file_cluster_17: 13.066
- **Magnitude:** 202.56 | **LOC:** 204 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (47.2823%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_count_main_logic_operators_and_keywords` (Impact: 102.3 | O(N^3) | DB: 3)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_count_logic_keywords` (Impact: 24.6 | O(N^2) | DB: 4)
    * *Intent:* #-----------------------------------------------------------------------------
  * `_count_logic_operators` (Impact: 24.6 | O(N^2) | DB: 3)
    * *Intent:* #-----------------------------------------------------------------------------
  * `calculate_mccabe_of_sub` (Impact: 3.1 | O(N^1) | DB: 3)
    * *Intent:* #-----------------------------------------------------------------------------
  * `calculate_mccabe_of_main` (Impact: 3.0 | O(N^1) | DB: 2)
    * *Intent:* #-----------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 38`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 41`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 5`, `doc: 13`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, Exporter, Perl::Critic::Utils, Readonly, strict, critic
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/09_theme.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.887 IQR)
- **Top Global Matches:** file_cluster_17: 12.887, file_cluster_0: 12.939, file_cluster_13: 13.309
- **Magnitude:** 192.78 | **LOC:** 319 | **CtrlFlow:** 87.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (88.9138%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `has_theme` (Impact: 1.9 | O(N^1))
    * *Intent:* #-----------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 30`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 186`
* *Architecture:* `import: 10`
* *Defense:* `safety: 4`, `test: 31`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::TestUtils, warnings, critic, English, List::SomeUtils, Test::More, Perl::Critic::UserProfile, Perl::Critic::PolicyFactory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/03_annotations.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.198 IQR)
- **Top Global Matches:** file_cluster_0: 12.198, file_cluster_13: 12.407, file_cluster_8: 12.526
- **Magnitude:** 184.52 | **LOC:** 244 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (85.8981%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `annotate` (Impact: 88.7 | O(N^3) | DB: 6)
  * `choose_annotation` (Impact: 4.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 34`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 88`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `doc: 2`, `test: 30`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::TestUtils, warnings, PPI::Document, Perl::Critic::Annotation, Test::More, strict, critic
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/01_config.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.722 IQR)
- **Top Global Matches:** file_cluster_0: 12.722, file_cluster_17: 13.169, file_cluster_13: 13.246
- **Magnitude:** 184.42 | **LOC:** 555 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (88.6342%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 99`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 162`, `dead_code: 5`
* *Architecture:* `io: 1`, `import: 13`
* *Defense:* `safety: 7`, `test: 81`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::TestUtils, warnings, enabled, the, English, Perl::Critic::Utils, List::SomeUtils, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extras/Dockerfile` (DOCKERFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.924 IQR)
- **Top Global Matches:** file_cluster_8: 6.924, file_cluster_7: 8.111, file_cluster_13: 8.144
- **Magnitude:** 163.52 | **LOC:** 32 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
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

### `inc/Perl/Critic/BuildUtilities.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.645 IQR)
- **Top Global Matches:** file_cluster_0: 9.645, file_cluster_13: 10.166, file_cluster_8: 10.331
- **Magnitude:** 162.9 | **LOC:** 197 | **CtrlFlow:** 87.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (37.7577%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `required_module_versions` (Impact: 124.0 | O(N^2))
  * `configure_required_module_versions` (Impact: 11.1 | O(N^2))
  * `emit_tar_warning_if_necessary` (Impact: 8.1 | O(N^2))
  * `test_required_module_versions` (Impact: 4.8 | O(N^2))
  * `get_PL_files` (Impact: 1.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 17`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 9`
* *Architecture:* `io: 2`, `api: 2`, `import: 7`
* *Defense:* `safety: 2`, `doc: 11`, `test: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, by, English, Exporter, Devel::CheckOS, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/loadanalysisdb` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.836 IQR)
- **Top Global Matches:** file_cluster_0: 10.836, file_cluster_13: 10.893, file_cluster_8: 10.937
- **Magnitude:** 153.1 | **LOC:** 345 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (17.6893%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `prepare_insert_statement` (Impact: 54.8 | O(N^4) | DB: 1)
  * `load` (Impact: 36.9 | O(N^4) | DB: 4)
  * `connect_to_database` (Impact: 8.4 | O(N^4) | DB: 8)
  * `main` (Impact: 7.6 | O(N^2) | DB: 4)
  * `execute_insert_statement` (Impact: 6.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 39`, `args: 5`, `func_start: 7`
* *Risk/State:* `state_mutation: 29`
* *Architecture:* `io: 2`, `import: 11`
* *Defense:* `safety: 4`, `doc: 17`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, English, Perl::Critic::Utils, Perl6::Say, execute, File::Spec, Carp, version...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/14_policy_parameters.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.84 IQR)
- **Top Global Matches:** file_cluster_0: 12.84, file_cluster_13: 12.999, file_cluster_17: 13.416
- **Magnitude:** 145.4 | **LOC:** 124 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (90.6079%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_supported_parameters` (Impact: 80.9 | O(N^4) | DB: 17)
    * *Intent:* #-----------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 33`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 63`
* *Architecture:* `import: 9`
* *Defense:* `safety: 4`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::TestUtils, warnings, Perl::Critic::PolicyParameter, English, Perl::Critic::Utils, Test::More, Perl::Critic::UserProfile, Perl::Critic::PolicyFactory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `inc/Perl/Critic/PolicySummaryGenerator.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.082 IQR)
- **Top Global Matches:** file_cluster_0: 12.082, file_cluster_13: 12.273, file_cluster_17: 12.77
- **Magnitude:** 124.32 | **LOC:** 211 | **CtrlFlow:** 75.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (36.8892%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generate_policy_summary` (Impact: 93.0 | O(N^4) | DB: 19)
    * *Intent:* #-----------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 28`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `io: 5`, `api: 2`, `import: 12`
* *Defense:* `safety: 7`, `doc: 19`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, Exception::Class, English, Exporter, Perl::Critic::Utils, Perl::Critic::Config, Perl::Critic::Exception::IO, Carp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/07_command.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.392 IQR)
- **Top Global Matches:** file_cluster_0: 12.392, file_cluster_13: 12.671, file_cluster_8: 12.835
- **Magnitude:** 117.56 | **LOC:** 281 | **CtrlFlow:** 59.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (86.8486%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 53`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 99`
* *Architecture:* `import: 11`
* *Defense:* `safety: 11`, `test: 39`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` arguments, Perl::Critic::TestUtils, warnings, Perl::Critic::Command, English, Perl::Critic::Utils, Test::More, File::Spec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/14_policy_parameter_behavior_enumeration.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.439 IQR)
- **Top Global Matches:** file_cluster_0: 13.439, file_cluster_13: 13.665, file_cluster_8: 14.022
- **Magnitude:** 113.4 | **LOC:** 163 | **CtrlFlow:** 88.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.7216%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 15`
* *Risk/State:* `state_mutation: 96`
* *Architecture:* `import: 16`
* *Defense:* `safety: 8`, `test: 25`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::TestUtils, warnings, Perl::Critic::Policy, value, Perl::Critic::PolicyParameter, English, Test::More, default...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/14_policy_parameter_behavior_integer.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.333 IQR)
- **Top Global Matches:** file_cluster_0: 13.333, file_cluster_13: 13.614, file_cluster_8: 14.006
- **Magnitude:** 110.38 | **LOC:** 169 | **CtrlFlow:** 90.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.7345%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 14`
* *Risk/State:* `state_mutation: 93`
* *Architecture:* `import: 17`
* *Defense:* `safety: 7`, `test: 23`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::TestUtils, warnings, Perl::Critic::Policy, value, Perl::Critic::PolicyParameter, English, Test::More, default...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/08_document.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.128 IQR)
- **Top Global Matches:** file_cluster_0: 12.128, file_cluster_13: 12.538, file_cluster_11: 12.753
- **Magnitude:** 106.62 | **LOC:** 194 | **CtrlFlow:** 72.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (89.6482%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_version` (Impact: 32.1 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 49`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 72`
* *Architecture:* `import: 9`
* *Defense:* `safety: 3`, `test: 23`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::TestUtils, warnings, Test::More, Perl::Critic::Document, include, Carp, Moose, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/11_policy_factory.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.312 IQR)
- **Top Global Matches:** file_cluster_0: 13.312, file_cluster_13: 13.707, file_cluster_11: 13.975
- **Magnitude:** 104.62 | **LOC:** 131 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (90.4384%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 32`, `args: 1`
* *Risk/State:* `state_mutation: 88`
* *Architecture:* `import: 7`
* *Defense:* `safety: 5`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::TestUtils, warnings, English, Test::More, Perl::Critic::UserProfile, Perl::Critic::PolicyFactory, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/14_policy_parameter_behavior_list_string.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.589 IQR)
- **Top Global Matches:** file_cluster_0: 12.589, file_cluster_13: 12.681, file_cluster_8: 12.891
- **Magnitude:** 92.72 | **LOC:** 168 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.5394%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 13`
* *Risk/State:* `state_mutation: 75`
* *Architecture:* `import: 16`
* *Defense:* `safety: 2`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Perl::Critic::TestUtils, warnings, Perl::Critic::Policy, value, Perl::Critic::PolicyParameter, Test::More, default, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `t/20_policy_require_consistent_newlines.t` (PERL) | Magnitude: 49.12 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 33, branch: 32, indent_spaces: 20, structural_boundaries: 18
- `t/00_versions.t` (PERL) | Magnitude: 87.48 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 48, branch: 30, structural_boundaries: 25, indent_spaces: 25
- `t/Variables/RequireLocalizedPunctuationVars.run.PL` (PERL) | Magnitude: 248.16 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 105, state_mutation: 78, branch: 58, structural_boundaries: 56
- `t/01_policy_config.t` (PERL) | Magnitude: 36.3 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 124, branch: 44, structural_boundaries: 28, test: 20
- `examples/loadanalysisdb` (PERL) | Magnitude: 153.1 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 121, branch: 63, structural_boundaries: 39, state_mutation: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `examples/generatestats` (PERL) | Magnitude: 18.3 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 98, branch: 59, state_mutation: 50, structural_boundaries: 47
- `t/03_pragmas.t` (PERL) | Magnitude: 1338.8 | Delta: **0.235 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 283, indent_spaces: 243, structural_boundaries: 206, encapsulation: 71

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `t/09_theme.t` (PERL) | Magnitude: 192.78 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 219, branch: 217, state_mutation: 186, decorators: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `t/05_utils_pod.t` (PERL) | Magnitude: 249.48 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 309, state_mutation: 126, branch: 90, structural_boundaries: 89
- `t/20_policy_prohibit_hard_tabs.t` (PERL) | Magnitude: 30.44 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 25, branch: 20, bitwise_ops: 12, structural_boundaries: 11
- `doc/PolicyParameter_Notes.pod` (PERL) | Magnitude: 88.88 | Delta: **0.378 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 88, branch: 49, structural_boundaries: 20, decorators: 20

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/13_bundled_policies.t` -> **Severity: 1154.637** (Blast Radius: 12.048 * Doc Risk: 95.8364%)
- `t/07_perlcritic.t` -> **Severity: 1101.504** (Blast Radius: 12.048 * Doc Risk: 91.4263%)
- `t/20_policy_prohibit_evil_modules.t` -> **Severity: 1062.444** (Blast Radius: 12.048 * Doc Risk: 88.1843%)
- `extras/Dockerfile` -> **Severity: 1040.556** (Blast Radius: 12.048 * Doc Risk: 86.3675%)
- `t/05_utils_perl.t` -> **Severity: 1035.65** (Blast Radius: 12.048 * Doc Risk: 85.9603%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
