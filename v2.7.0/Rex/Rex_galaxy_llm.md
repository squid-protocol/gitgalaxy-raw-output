# ARCHITECTURAL_BRIEF: Rex
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/RexOps/Rex.git` |
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
| Total Artifacts | 515 |
| Analyzed Artifacts (Scanned) | 108 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 407 |
| Total LOC | 6863 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 21.0% |
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
| PERL | 90 | 6609 | 83.3% |
| PLAINTEXT | 7 | 0 | 6.5% |
| YAML | 5 | 36 | 4.6% |
| SHELL | 3 | 218 | 2.8% |
| MARKDOWN | 2 | 0 | 1.9% |
| XML | 1 | 0 | 0.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 99 | 91.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 8.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 407*

**Composition by Extension & Reason:**
- `.pm`: 347x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 11x Unsupported Format (.undeterminable), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2047 LOC)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.out1`: 3x Excluded (Unsupported Extension: '.out1')
- `.out2`: 3x Excluded (Unsupported Extension: '.out2')
- `.out`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ex`: 2x Excluded (Unsupported Extension: '.ex')
- `.out3`: 2x Excluded (Unsupported Extension: '.out3')
- `.rex`: 2x Excluded (Unsupported Extension: '.rex')
- `.stderr`: 2x Excluded (Unsupported Extension: '.stderr')
- `.stdout`: 2x Excluded (Unsupported Extension: '.stdout')
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.9 | 17.5 | 7.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 35.3 | 41.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 7.8 | 0.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 41.4 | 21.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 6.0 | 0.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 20.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 14.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 102 | 24 | 2 | `bin/rexify` |
| cleanup | 27 | 11 | 0 | `bin/rexify` |
| guards | 222 | 89 | 4 | `t/network_linux.t` |
| danger | 202 | 26 | 2 | `bin/rexify` |
| concurrency | 14 | 6 | 0 | `misc/create_pod.sh` |
| connectivity | 56 | 13 | 1 | `bin/rexify` |
| io | 308 | 26 | 2 | `misc/create_pod.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 23 | 6 | 0 | `bin/rexify` |
| time | 4 | 2 | 0 | `t/shared.t` |
| serialization | 1 | 1 | 0 | `bin/rexify` |
| regex | 241 | 34 | 4 | `t/file.t` |
| events | 8 | 8 | 0 | `t/auth.t` |
| tests | 1167 | 87 | 19 | `t/cron.t` |
| docs | 7 | 6 | 0 | `t/cmdb/default/foo.yml` |
| debt | 134 | 14 | 1 | `bin/rexify` |
| mutation | 1154 | 89 | 26 | `bin/rexify` |
| dead_code | 8 | 2 | 0 | `bin/rexify` |
| credential | 2 | 1 | 0 | `t/url_encode.t` |
| threat | 11 | 11 | 0 | `bin/rex` |
| ml_ai | 13 | 5 | 0 | `bin/rexify` |
| ui | 112 | 8 | 0 | `t/template_ng.t` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `misc/create_pod.sh` (Hits: 195)
- `share/rex-tab-completion.zsh` (Hits: 30)
- `share/rex-tab-completion.bash` (Hits: 24)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **rexify** (`bin/rexify`) — 29 outbound dependencies
2. **file.t** (`t/file.t`) — 15 outbound dependencies
3. **load_rexfile.t** (`t/load_rexfile.t`) — 14 outbound dependencies
4. **git.t** (`t/scm/git.t`) — 14 outbound dependencies
5. **rsync.t** (`t/rsync.t`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `resolve_deps` (@ `bin/rexify`) -> Impact: **54.3** | LOC: 125
- `download_recipe` (@ `bin/rexify`) -> Impact: **28.4** | LOC: 58
- `install_perl_module` (@ `bin/rexify`) -> Impact: **20.7** | LOC: 47
- `_rex` (@ `share/rex-tab-completion.bash`) -> Impact: **20.7** | LOC: 46
  * *Intent:* # bash completion for rex
- `get` (@ `bin/rexify`) -> Impact: **19.6** | LOC: 24
- `_setup_test` (@ `t/load_rexfile.t`) -> Impact: **17.6** | LOC: 41
- `test_rsync` (@ `t/rsync.t`) -> Impact: **17.2** | LOC: 65
- `print_found` (@ `bin/rexify`) -> Impact: **16.2** | LOC: 12
- `Anonymous_Block` (@ `misc/create_pod.sh`) -> Impact: **12.0** | LOC: 98
- `download_recipe_git` (@ `bin/rexify`) -> Impact: **11.2** | LOC: 26

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `t` | 75 | 1836.36 | 17.98% | 1.3% |
| `bin` | 2 | 440.42 | 27.02% | 4.57% |
| `t/issue` | 8 | 152.78 | 8.59% | 12.5% |
| `share` | 2 | 110.68 | 66.08% | 0.0% |
| `misc` | 3 | 86.04 | 33.13% | 0.0% |
| `t/scm` | 1 | 40.06 | 7.2% | 0.0% |
| `xt/author` | 2 | 30.86 | 6.18% | 0.0% |
| `t/cmdb/default` | 2 | 29.42 | 0.0% | 0.0% |
| `t/cmdb` | 2 | 25.76 | 0.0% | 0.0% |
| `t/commands` | 1 | 16.6 | 4.97% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `t/issue/948.t` -> **99.9946%** Exposure
- `t/augeas.t` -> **75.566%** Exposure
- `t/db.t` -> **21.8486%** Exposure
- `bin/rexify` -> **9.1423%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `t/case.t` -> **100.0%** Exposure
- `t/helper_path.t` -> **100.0%** Exposure
- `t/hooks_in_rexfile_tasks_in_pkg.t` -> **100.0%** Exposure
- `share/rex-tab-completion.bash` -> **100.0%** Exposure
- `misc/sanitize_pod.pl` -> **99.9999%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/issue/948.t` -> **4** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `651` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `bin/rexify` (PERL) -> Cumulative Risk: **533.75**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 418.0 | **LOC:** 1402 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.5895%), Safety Score (96.742%)
- **Heaviest Functions:** `resolve_deps` (Impact: 54.3), `download_recipe` (Impact: 28.4), `install_perl_module` (Impact: 20.7)

### 2. `share/rex-tab-completion.bash` (SHELL) -> Cumulative Risk: **508.42**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 68.62 | **LOC:** 67 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.982%)
- **Heaviest Functions:** `_rex` (Impact: 20.7), `_rex_fix_colon_reply` (Impact: 2.4), `__global_context__` (Impact: 1.5)

### 3. `t/summary.t` (PERL) -> Cumulative Risk: **483.13**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 33.6 | **LOC:** 115 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (91.4012%), State Flux (86.2391%)
- **Heaviest Functions:** `test_summary` (Impact: 8.7), `create_tasks` (Impact: 6.2)

### 4. `t/load_rexfile.t` (PERL) -> Cumulative Risk: **463.3**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 45.0 | **LOC:** 100 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9996%), Safety Score (98.7327%)
- **Heaviest Functions:** `_setup_test` (Impact: 17.6)

### 5. `share/rex-tab-completion.zsh` (SHELL) -> Cumulative Risk: **456.84**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 42.06 | **LOC:** 77 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.988%), Safety Score (99.896%)
- **Heaviest Functions:** `__global_context__` (Impact: 10.7), `Anonymous_Block` (Impact: 4.5), `_rex_hosts` (Impact: 3.2)

### 6. `t/file_hooks.t` (PERL) -> Cumulative Risk: **442.4**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 54.3 | **LOC:** 141 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9824%), Safety Score (76.278%)
- **Heaviest Functions:** `expected_params` (Impact: 8.2), `before_hook` (Impact: 2.6), `after_change_hook` (Impact: 2.5)

### 7. `t/issue/948.t` (PERL) -> Cumulative Risk: **435.66**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 24.1 | **LOC:** 96 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9946%), State Flux (61.2336%)
- **Heaviest Functions:** `Rex::Helper::Run::i_run` (Impact: 5.0), `Rex::Commands::File::file` (Impact: 3.9), `Rex::Commands::Fs::unlink` (Impact: 1.6)

### 8. `t/rsync.t` (PERL) -> Cumulative Risk: **427.39**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 40.78 | **LOC:** 108 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9734%), Safety Score (81.0696%)
- **Heaviest Functions:** `test_rsync` (Impact: 17.2)

### 9. `t/write_utf8_files.t` (PERL) -> Cumulative Risk: **383.43**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 23.06 | **LOC:** 100 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (96.2349%), Safety Score (64.3781%)
- **Heaviest Functions:** `get_encoding` (Impact: 6.5), `write_file` (Impact: 2.0)

### 10. `t/hooks_in_rexfile_tasks_in_pkg.t` (PERL) -> Cumulative Risk: **381.23**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 54.86 | **LOC:** 58 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.9443%), Cognitive Load (84.2905%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `bin/rexify` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 418.0 | **LOC:** 1402 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.6076%), Tech Debt (9.1423%)
**Top Internal Functions/Classes:**
  * `resolve_deps` (Impact: 54.3)
  * `download_recipe` (Impact: 28.4)
  * `install_perl_module` (Impact: 20.7)
  * `get` (Impact: 19.6)
  * `print_found` (Impact: 16.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 14 instances
* *Amplified Cascading Flux:* 72 instances
* *Sec Tainted Injection (weighted view):* 14
* *State Mutation (weighted view):* 218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 181`, `args: 13`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 52`, `state_mutation: 74`, `dead_code: 4`, `fragile_debt: 1`
* *Architecture:* `io: 11`, `api: 10`, `import: 33`
* *Defense:* `safety: 5`, `doc: 1`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, Cwd, Data::Dumper, File::Basename, File::Spec, HTTP::Request, HTTP::Request::Common, JSON::MaybeXS...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/file.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 78.06 | **LOC:** 393 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.4665%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 45`
* *Risk/State:* `state_mutation: 43`
* *Architecture:* `import: 19`
* *Defense:* `safety: 2`, `test: 67`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cwd, File::Spec, File::Temp, Rex::Commands::File, Rex::Commands::Fs, Rex::Commands::Gather, Rex::Commands::Run, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/cron.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 71.86 | **LOC:** 539 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.655%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 25`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `io: 2`, `import: 5`
* *Defense:* `safety: 4`, `test: 287`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Cron::Base, Test::More, Test::Warnings, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `share/rex-tab-completion.bash` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 68.62 | **LOC:** 67 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.8147%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_rex` (Impact: 20.7)
    * *Intent:* # bash completion for rex
  * `_rex_fix_colon_reply` (Impact: 2.4)
  * `__global_context__` (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 33`, `args: 1`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 14`
* *Architecture:* `io: 24`, `concurrency: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/hooks_in_rexfile_tasks_in_pkg.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 54.86 | **LOC:** 58 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.2905%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `import: 10`
* *Defense:* `safety: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Temp, Rex::Commands, Rex::RunList, Rex::Shared::Var, Test::More, Test::Warnings, lib, t::tasks::alien...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/file_hooks.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 54.3 | **LOC:** 141 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.904%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expected_params` (Impact: 8.2)
  * `before_hook` (Impact: 2.6)
  * `after_change_hook` (Impact: 2.5)
  * `after_hook` (Impact: 2.5)
  * `before_change_hook` (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 45`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `safety: 2`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Temp, Rex::Commands::File, Rex::Hook, Test::Deep, Test::More, Test::Output, Test::Warnings, v5...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/template_ng.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 51.22 | **LOC:** 149 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.3931%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 19`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Commands, Rex::Config, Rex::Template::NG, Test::More, Test::Warnings, spaces, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dmi.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 50.34 | **LOC:** 196 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.8284%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 33`
* *Risk/State:* `state_mutation: 32`
* *Architecture:* `io: 3`, `import: 5`
* *Defense:* `safety: 5`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Inventory::DMIDecode, Test::More, Test::Warnings, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/shared.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 50.2 | **LOC:** 87 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.947%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 13`, `args: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 14`
* *Architecture:* `concurrency: 2`, `import: 7`
* *Defense:* `safety: 2`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Shared::Var, Test::Deep, Test::More, Test::Warnings, Time::HiRes, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/helper_path.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 49.86 | **LOC:** 60 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.8688%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 15`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cwd, File::Basename, Rex::Helper::Path, Test::More, Test::Warnings, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/load_rexfile.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 45.0 | **LOC:** 100 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.5656%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_setup_test` (Impact: 17.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 8 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 32`, `args: 1`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 10`
* *Architecture:* `io: 2`, `import: 13`
* *Defense:* `safety: 2`, `test: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` English, File::Spec, File::Temp, Rex::CLI, Rex::Commands::File, Sub::Override, Test::More, Test::Output...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/0.31.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 44.46 | **LOC:** 156 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.5223%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 26`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`
* *Architecture:* `import: 7`
* *Defense:* `safety: 5`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex, Test::More, Test::Warnings, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/network_linux.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 43.48 | **LOC:** 93 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.2018%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 17`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `io: 7`, `import: 6`
* *Defense:* `safety: 9`, `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Hardware::Network::Linux, Rex::Helper::Hash, Test::More, Test::Warnings, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `share/rex-tab-completion.zsh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 42.06 | **LOC:** 77 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.354%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__global_context__` (Impact: 10.7)
  * `Anonymous_Block` (Impact: 4.5)
  * `_rex_hosts` (Impact: 3.2)
    * *Intent:* # return hosts managed by rex or any other host availabe via zsh's _hosts function
  * `_hostgroups` (Impact: 2.2)
  * `_envs` (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 15`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 2`, `state_mutation: 6`
* *Architecture:* `io: 30`
* *Defense:* `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/rsync.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 40.78 | **LOC:** 108 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.3933%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_rsync` (Impact: 17.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 30`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`
* *Architecture:* `io: 1`, `api: 1`, `import: 13`
* *Defense:* `safety: 2`, `test: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cwd, File::Basename, File::Find, File::Temp, Rex::Commands::Rsync, Rex::Commands::Run, Rex::Task, Test::Deep...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/scm/git.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 40.06 | **LOC:** 353 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.1994%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `git_last_commit_message_ok` (Impact: 4.1)
  * `prepare_test_repo` (Impact: 3.1)
  * `init_test` (Impact: 2.9)
  * `git_branch_ok` (Impact: 2.3)
  * `git_repo_ok` (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 75`, `args: 5`, `func_start: 8`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 8`, `import: 13`
* *Defense:* `safety: 2`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` English, File::Spec, File::Temp, Rex::Commands, Rex::Commands::File, Rex::Commands::Run, Rex::Commands::SCM, Rex::Helper::Run...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/auth.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 39.92 | **LOC:** 181 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.0093%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 23`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Commands, Rex::Group, Test::More, Test::Warnings, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/case.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 39.88 | **LOC:** 65 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.3122%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 31`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Commands, Test::More, Test::Warnings, a, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/template.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 38.04 | **LOC:** 139 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.3803%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 22`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Commands, Rex::Config, Rex::Template, Symbol, Test::More, Test::Warnings, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `misc/sanitize_pod.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 36.78 | **LOC:** 51 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.9974%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 11`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `io: 2`, `import: 2`
* *Defense:* `safety: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `misc/create_pod.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 34.58 | **LOC:** 120 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.9787%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 12.0)
  * `__global_context__` (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 4 instances
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 52`, `args: 7`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 2`, `state_mutation: 5`
* *Architecture:* `io: 195`, `concurrency: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/report.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 34.2 | **LOC:** 82 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.0166%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 23`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 4`, `state_mutation: 6`
* *Architecture:* `io: 2`, `import: 10`
* *Defense:* `safety: 4`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Commands, Rex::Commands::File, Rex::Commands::Fs, Rex::Report::YAML, Test::More, Test::Warnings, YAML, v5...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/summary.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 33.6 | **LOC:** 115 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.3653%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_summary` (Impact: 8.7)
  * `create_tasks` (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 40`, `args: 1`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 12`
* *Defense:* `safety: 2`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` English, Module::Load::Conditional, Rex::Commands, Rex::Commands::Run, Rex::Config, Rex::Transaction, Test::Deep, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/hooks_in_rexfile.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 32.82 | **LOC:** 58 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.9834%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Temp, Rex::Commands, Rex::RunList, Rex::Shared::Var, Test::More, Test::Warnings, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/hooks.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 32.8 | **LOC:** 55 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.9834%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 20`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Temp, Rex::Commands, Rex::RunList, Rex::Shared::Var, Test::More, Test::Warnings, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `bin/rexify` -> **Severity: 925.9** (Blast Radius: 9.259 * Doc Risk: 100.0%)
- `t/cmdb_path.t` -> **Severity: 925.9** (Blast Radius: 9.259 * Doc Risk: 100.0%)
- `t/db.t` -> **Severity: 925.9** (Blast Radius: 9.259 * Doc Risk: 100.0%)
- `t/file_hooks.t` -> **Severity: 925.9** (Blast Radius: 9.259 * Doc Risk: 100.0%)
- `t/issue/948.t` -> **Severity: 925.9** (Blast Radius: 9.259 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
