# ARCHITECTURAL_BRIEF: eeglab
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/eeglab` |
| **Timestamp** | `2026-08-03T20:11:07.420341+00:00` |
| **Scan Duration** | `2.44s` |
| **Git Branch** | `develop` |
| **Git Commit** | `514a923047228fe24bfd9564c587e8a6b1cf56bb` |
| **Git Remote** | `https://github.com/sccn/eeglab` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 648 malicious artifacts.

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
| Total Artifacts | 826 |
| Analyzed Artifacts (Scanned) | 670 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 156 |
| Total LOC | 83326 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 81.1% |
| Dominant Lang | MATLAB |

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
| MATLAB | 643 | 83198 | 96.0% |
| PLAINTEXT | 11 | 1 | 1.6% |
| XML | 7 | 0 | 1.0% |
| MARKDOWN | 3 | 0 | 0.4% |
| BATCH | 2 | 5 | 0.3% |
| SCALA | 1 | 78 | 0.1% |
| SHELL | 1 | 16 | 0.1% |
| CSV | 1 | 27 | 0.1% |
| BINARY_THREAT | 1 | 1 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.641`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_17 | 375 | 56.0% |
| file_cluster_9 | 153 | 22.8% |
| file_cluster_8 | 116 | 17.3% |
| file_cluster_0 | 4 | 0.6% |
| file_cluster_11 | 4 | 0.6% |
| file_cluster_4 | 2 | 0.3% |
| Unknown | 2 | 0.3% |
| file_cluster_6 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 13 | 1.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 156*

**Composition by Extension & Reason:**
- `.sfp`: 45x Excluded (Unsupported Extension: '.sfp')
- `.m`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 17 LOC), 1x Excluded (Machine-Generated Source Code Signature: 31 LOC)
- `.ced`: 12x Excluded (Unsupported Extension: '.ced')
- `.locs`: 8x Excluded (Unsupported Extension: '.locs'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Binary Format Detected)
- `.elp`: 7x Excluded (Unsupported Extension: '.elp')
- `.dat`: 4x Excluded (Unsupported Extension: '.dat'), 3x Excluded (Unsupported Extension: '.DAT')
- `.xyz`: 3x Excluded (Unsupported Extension: '.xyz')
- `.loc`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.map`: 3x Excluded (Unsupported Extension: '.map')
- `.mat`: 3x Excluded (Unsupported Extension: '.mat')
- `.fdt`: 3x Excluded (Unsupported Extension: '.fdt')
- `.set`: 3x Excluded (Unsupported Extension: '.set')
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.7 | 69.7 | 81.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 71.9 | 80.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 12.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 12.7 | 2.3 | 2.3 |
| API Exposure | 0.0 | 4.3 | 0.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 87.1 | 0.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 93.8 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 13.5 | 10.1 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 89.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.5 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 98.6 | 18.9 | 11.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 7.2 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 19.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `functions/studyfunc/std_limoresults.m` (Hits: 26)
- `functions/timefreqfunc/crossf.m` (Hits: 22)
- `functions/timefreqfunc/timefreq.m` (Hits: 22)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CLAUDE.md** (`CLAUDE.md`) — 0 inbound connections
2. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 0 inbound connections
3. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
4. **Contents.m** (`Contents.m`) — 0 inbound connections
5. **eeglab.m** (`eeglab.m`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **CLAUDE.md** (`CLAUDE.md`) — 0 outbound dependencies
2. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 0 outbound dependencies
3. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 outbound dependencies
4. **Contents.m** (`Contents.m`) — 0 outbound dependencies
5. **eeglab.m** (`eeglab.m`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `pop_topoplot` (@ `functions/popfunc/pop_topoplot.m`) -> Impact: **2334.3** | LOC: 386
  * *Intent:* % ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE % LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR % CO...
- `pop_jointprob` (@ `functions/popfunc/pop_jointprob.m`) -> Impact: **1229.5** | LOC: 190
  * *Intent:* % IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE % ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS ...
- `pop_rejkurt` (@ `functions/popfunc/pop_rejkurt.m`) -> Impact: **1229.3** | LOC: 187
  * *Intent:* % IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE % ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS ...
- `eeg_pvaf` (@ `functions/popfunc/eeg_pvaf.m`) -> Impact: **1039.7** | LOC: 219
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `pop_rejchan` (@ `functions/popfunc/pop_rejchan.m`) -> Impact: **970.7** | LOC: 211
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `pop_interp` (@ `functions/popfunc/pop_interp.m`) -> Impact: **760.1** | LOC: 176
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `pop_rejtrend` (@ `functions/popfunc/pop_rejtrend.m`) -> Impact: **703.6** | LOC: 143
  * *Intent:* % IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE % ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS ...
- `pop_autorej` (@ `functions/popfunc/pop_autorej.m`) -> Impact: **619.7** | LOC: 186
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `readneurolocs` (@ `functions/sigprocfunc/readneurolocs.m`) -> Impact: **582.0** | LOC: 159
  * *Intent:* % This program is free software; you can redistribute it and/or modify % it under the terms of the GNU General Public License as published by % the Fr...
- `pop_newset` (@ `functions/popfunc/pop_newset.m`) -> Impact: **343.1** | LOC: 73
  * *Intent:* % Dataset (modified) selected -> select study % Dataset (modified) selected -> select multiple datasets % Dataset (modified) selected -> select other ...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `eeg_eval` (@ `functions/adminfunc/eeg_eval.m`) -> **O(2^N) [Recursive]**
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `makehelpfiles` (@ `functions/miscfunc/makehelpfiles.m`) -> **O(2^N) [Recursive]**
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `vectdata` (@ `functions/miscfunc/vectdata.m`) -> **O(2^N) [Recursive]**
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `eeg_pvaf` (@ `functions/popfunc/eeg_pvaf.m`) -> **O(2^N) [Recursive]**
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `eeg_rereject` (@ `functions/popfunc/eeg_rereject.m`) -> **O(2^N) [Recursive]**
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `eeg_timeinterp` (@ `functions/popfunc/eeg_timeinterp.m`) -> **O(2^N) [Recursive]**
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `pop_autorej` (@ `functions/popfunc/pop_autorej.m`) -> **O(2^N) [Recursive]**
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `pop_fileio` (@ `functions/popfunc/pop_fileio.m`) -> **O(2^N) [Recursive]**
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `pop_importegimat` (@ `functions/popfunc/pop_importegimat.m`) -> **O(2^N) [Recursive]**
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `pop_interp` (@ `functions/popfunc/pop_interp.m`) -> **O(2^N) [Recursive]**
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...

### Highest Data Gravity (Database Complexity)
- `pop_topoplot` (@ `functions/popfunc/pop_topoplot.m`) -> DB Complexity: **105**
  * *Intent:* % ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE % LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR % CO...
- `pop_autorej` (@ `functions/popfunc/pop_autorej.m`) -> DB Complexity: **59**
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `readegihdr` (@ `functions/sigprocfunc/readegihdr.m`) -> DB Complexity: **59**
  * *Intent:* % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO...
- `readneurolocs` (@ `functions/sigprocfunc/readneurolocs.m`) -> DB Complexity: **58**
  * *Intent:* % This program is free software; you can redistribute it and/or modify % it under the terms of the GNU General Public License as published by % the Fr...
- `pop_jointprob` (@ `functions/popfunc/pop_jointprob.m`) -> DB Complexity: **57**
  * *Intent:* % IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE % ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS ...
- `eeg_pvaf` (@ `functions/popfunc/eeg_pvaf.m`) -> DB Complexity: **56**
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `pop_rejkurt` (@ `functions/popfunc/pop_rejkurt.m`) -> DB Complexity: **55**
  * *Intent:* % IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE % ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS ...
- `topoplot` (@ `functions/sigprocfunc/topoplot.m`) -> DB Complexity: **53**
  * *Intent:* % 2-26-98 Revised by Colin % -changed image back to surface command % -added fill and blank styles % -removed extra background colormap entry (now use...
- `pop_rejchan` (@ `functions/popfunc/pop_rejchan.m`) -> DB Complexity: **52**
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `pop_interp` (@ `functions/popfunc/pop_interp.m`) -> DB Complexity: **45**
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `functions/sigprocfunc` | 114 | 50614.09 | 73.35% | 5.77% |
| `functions/popfunc` | 128 | 47701.45 | 79.56% | 8.47% |
| `functions/miscfunc` | 107 | 41738.04 | 73.34% | 11.67% |
| `functions/studyfunc` | 131 | 27125.92 | 74.08% | 14.16% |
| `functions/timefreqfunc` | 24 | 20307.91 | 73.7% | 7.54% |
| `functions/adminfunc` | 66 | 8793.91 | 55.73% | 19.68% |
| `functions/supportfiles/channel_location_files/neuroscan` | 2 | 5001.0 | 0.0% | 0.0% |
| `functions/statistics` | 16 | 2274.02 | 79.65% | 40.08% |
| `functions/@mmo` | 24 | 1958.5 | 50.66% | 20.75% |
| `functions/guifunc` | 10 | 1337.38 | 59.18% | 1.86% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `functions/@memmapdata/display.m` -> **100.0%** Exposure
- `functions/@memmapdata/ndims.m` -> **100.0%** Exposure
- `functions/miscfunc/rotatematlab.m` -> **100.0%** Exposure
- `functions/studyfunc/std_readerpimage.m` -> **100.0%** Exposure
- `functions/studyfunc/std_readersp.m` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `eeglab.m` -> **100.0%** Exposure
- `functions/@eegobj/length.m` -> **100.0%** Exposure
- `functions/@eegobj/subsasgn.m` -> **100.0%** Exposure
- `functions/@eegobj/subsref.m` -> **100.0%** Exposure
- `functions/@memmapdata/display.m` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `functions/studyfunc/pop_studydesign.m` -> **3** Orphaned Functions | **0** Duplicates
- `functions/miscfunc/make_timewarp.m` -> **2** Orphaned Functions | **0** Duplicates
- `functions/miscfunc/replace_in_all_files.m` -> **2** Orphaned Functions | **0** Duplicates
- `functions/popfunc/eeg_topoplot.m` -> **2** Orphaned Functions | **0** Duplicates
- `functions/@memmapdata/display.m` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`functions/@mmo/display.m`** -> AI Confidence: **99.29%**
2. **`functions/@mmo/permute.m`** -> AI Confidence: **99.29%**
3. **`functions/adminfunc/abouteeglab.m`** -> AI Confidence: **99.29%**
4. **`functions/adminfunc/eeglab_new.m`** -> AI Confidence: **99.29%**
5. **`functions/miscfunc/makehtml.m`** -> AI Confidence: **99.29%**
6. **`functions/statistics/anova1rm_cell.m`** -> AI Confidence: **99.29%**
7. **`functions/studyfunc/pop_dipparams.m`** -> AI Confidence: **99.29%**
8. **`functions/studyfunc/pop_statparams.m`** -> AI Confidence: **99.29%**
9. **`functions/@eegobj/eegobj.m`** -> AI Confidence: **99.29%**
10. **`functions/@eegobj/orderfields.m`** -> AI Confidence: **99.29%**
11. **`functions/adminfunc/troubleshooting_data_formats.m`** -> AI Confidence: **99.29%**
12. **`functions/supportfiles/EEGLAB_verbose`** -> AI Confidence: **99.29%**
13. **`functions/@memmapdata/reshape.m`** -> AI Confidence: **99.17%**
14. **`functions/@memmapdata/subsasgn.m`** -> AI Confidence: **99.17%**
15. **`functions/@memmapdata/subsref.m`** -> AI Confidence: **99.17%**
16. **`functions/adminfunc/eeglab_options.m`** -> AI Confidence: **99.17%**
17. **`functions/adminfunc/pop_rejmenu.m`** -> AI Confidence: **99.17%**
18. **`functions/guifunc/warndlg2.m`** -> AI Confidence: **99.17%**
19. **`functions/miscfunc/compile_eeglab.m`** -> AI Confidence: **99.17%**
20. **`functions/popfunc/eeg_boundarytype.m`** -> AI Confidence: **99.17%**
21. **`functions/popfunc/eeg_import.m`** -> AI Confidence: **99.17%**
22. **`functions/popfunc/eeg_mergechan.m`** -> AI Confidence: **99.17%**
23. **`functions/popfunc/pop_editset.m`** -> AI Confidence: **99.17%**
24. **`functions/popfunc/pop_importdata.m`** -> AI Confidence: **99.17%**
25. **`functions/popfunc/pop_newtimef.m`** -> AI Confidence: **99.17%**
26. **`functions/sigprocfunc/copyaxis.m`** -> AI Confidence: **99.17%**
27. **`functions/sigprocfunc/loadtxt.m`** -> AI Confidence: **99.17%**
28. **`functions/sigprocfunc/plotsphere.m`** -> AI Confidence: **99.17%**
29. **`functions/sigprocfunc/writeeeg.m`** -> AI Confidence: **99.17%**
30. **`functions/studyfunc/pop_erspparams.m`** -> AI Confidence: **99.17%**
31. **`functions/studyfunc/pop_specparams.m`** -> AI Confidence: **99.17%**
32. **`functions/studyfunc/std_chaninds.m`** -> AI Confidence: **99.17%**
33. **`functions/studyfunc/std_chantopo.m`** -> AI Confidence: **99.17%**
34. **`functions/studyfunc/std_makedesign.m`** -> AI Confidence: **99.17%**
35. **`functions/studyfunc/std_plotcurve.m`** -> AI Confidence: **99.17%**
36. **`functions/studyfunc/std_readfilelimo.m`** -> AI Confidence: **99.17%**
37. **`functions/timefreqfunc/newcrossf.m`** -> AI Confidence: **99.17%**
38. **`functions/timefreqfunc/newtimefpowerunit.m`** -> AI Confidence: **99.17%**
39. **`functions/adminfunc/plugin_uiupdate.m`** -> AI Confidence: **99.11%**
40. **`functions/miscfunc/crossfreq.m`** -> AI Confidence: **99.11%**
41. **`functions/miscfunc/setfont.m`** -> AI Confidence: **99.11%**
42. **`functions/miscfunc/textgui.m`** -> AI Confidence: **99.11%**
43. **`functions/sigprocfunc/isscript.m`** -> AI Confidence: **99.11%**
44. **`functions/statistics/fdr.m`** -> AI Confidence: **99.11%**
45. **`functions/statistics/stat_surrogate_ci.m`** -> AI Confidence: **99.11%**
46. **`functions/studyfunc/std_plottf.m`** -> AI Confidence: **99.11%**
47. **`functions/studyfunc/std_precomp_worker.m`** -> AI Confidence: **99.11%**
48. **`functions/timefreqfunc/crossf.m`** -> AI Confidence: **99.11%**
49. **`functions/timefreqfunc/timef.m`** -> AI Confidence: **99.11%**
50. **`eeglab.m`** -> AI Confidence: **99.06%**
51. **`functions/@eegobj/length.m`** -> AI Confidence: **99.06%**
52. **`functions/@eegobj/subsasgn.m`** -> AI Confidence: **99.06%**
53. **`functions/@eegobj/subsref.m`** -> AI Confidence: **99.06%**
54. **`functions/@memmapdata/display.m`** -> AI Confidence: **99.06%**
55. **`functions/@memmapdata/memmapdata.m`** -> AI Confidence: **99.06%**
56. **`functions/@memmapdata/ndims.m`** -> AI Confidence: **99.06%**
57. **`functions/@memmapdata/size.m`** -> AI Confidence: **99.06%**
58. **`functions/@memmapdata/sum.m`** -> AI Confidence: **99.06%**
59. **`functions/@mmo/binaryopp.m`** -> AI Confidence: **99.06%**
60. **`functions/@mmo/checkcopies_local.m`** -> AI Confidence: **99.06%**
61. **`functions/@mmo/checkworkspace.m`** -> AI Confidence: **99.06%**
62. **`functions/@mmo/ctranspose.m`** -> AI Confidence: **99.06%**
63. **`functions/@mmo/ndims.m`** -> AI Confidence: **99.06%**
64. **`functions/@mmo/reshape.m`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `functions/@mmo/mmo.m` -> **100.0%** Exposure
- `functions/@mmo/subsasgn_old.m` -> **100.0%** Exposure
- `functions/adminfunc/eeg_checkset.m` -> **100.0%** Exposure
- `functions/adminfunc/eeg_eval.m` -> **100.0%** Exposure
- `functions/adminfunc/eeg_readoptions.m` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `functions/miscfunc/detectmalware.m` -> **100.0%** Exposure
- `functions/miscfunc/rmart.m` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `functions/@mmo/mmo.m` -> **100.0%** Exposure
- `functions/@mmo/subsasgn_old.m` -> **100.0%** Exposure
- `functions/adminfunc/eeg_readoptions.m` -> **100.0%** Exposure
- `functions/popfunc/eeg_pvaf.m` -> **100.0%** Exposure
- `functions/popfunc/pop_autorej.m` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `9` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `0` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `functions/@mmo/size.m` (MATLAB) -> Cumulative Risk: **805.75**
- **Archetype:** `file_cluster_9` (Distance: 15.134 IQR)
- **Magnitude:** 97.1 | **LOC:** 67 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (99.6659%), Tech Debt (99.3307%)
- **Heaviest Functions:** `size` (Impact: 66.5)

### 2. `functions/miscfunc/make_timewarp.m` (MATLAB) -> Cumulative Risk: **759.22**
- **Archetype:** `file_cluster_17` (Distance: 16.566 IQR)
- **Magnitude:** 209.04 | **LOC:** 227 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Safety Score (97.071%)
- **Heaviest Functions:** `eventIsOfType` (Impact: 30.9), `eventMeetsCondition` (Impact: 25.4), `eventsOfCertainTypeAfterCertainLatencyIn` (Impact: 18.2)

### 3. `functions/sigprocfunc/biosig2eeglab.m` (MATLAB) -> Cumulative Risk: **749.15**
- **Archetype:** `file_cluster_17` (Distance: 17.828 IQR)
- **Magnitude:** 503.32 | **LOC:** 277 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `biosig2eeglab` (Impact: 337.3)

### 4. `functions/@mmo/mmo.m` (MATLAB) -> Cumulative Risk: **741.06**
- **Archetype:** `file_cluster_0` (Distance: 14.021 IQR)
- **Magnitude:** 244.2 | **LOC:** 166 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `mmo` (Impact: 178.3)

### 5. `functions/adminfunc/plugin_urlreadwrite.m` (MATLAB) -> Cumulative Risk: **733.17**
- **Archetype:** `file_cluster_8` (Distance: 14.074 IQR)
- **Magnitude:** 150.36 | **LOC:** 100 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.8888%)
- **Heaviest Functions:** `plugin_urlreadwrite` (Impact: 74.9)

### 6. `functions/studyfunc/std_readtopoclust.m` (MATLAB) -> Cumulative Risk: **707.03**
- **Archetype:** `file_cluster_17` (Distance: 15.603 IQR)
- **Magnitude:** 138.82 | **LOC:** 132 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Safety Score (84.2164%)
- **Heaviest Functions:** `std_readtopoclust` (Impact: 74.5)

### 7. `functions/popfunc/pop_topoplot.m` (MATLAB) -> Cumulative Risk: **702.69**
- **Archetype:** `file_cluster_17` (Distance: 14.965 IQR)
- **Magnitude:** 2649.82 | **LOC:** 467 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `pop_topoplot` (Impact: 2334.3)

### 8. `functions/sigprocfunc/biosig2eeglabevent.m` (MATLAB) -> Cumulative Risk: **693.66**
- **Archetype:** `file_cluster_17` (Distance: 15.763 IQR)
- **Magnitude:** 168.3 | **LOC:** 145 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Cognitive Load (89.4101%)
- **Heaviest Functions:** `biosig2eeglabevent` (Impact: 79.5)

### 9. `functions/popfunc/pop_autorej.m` (MATLAB) -> Cumulative Risk: **687.9**
- **Archetype:** `file_cluster_17` (Distance: 16.187 IQR)
- **Magnitude:** 773.72 | **LOC:** 263 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `pop_autorej` (Impact: 619.7)

### 10. `functions/statistics/surrogdistrib.m` (MATLAB) -> Cumulative Risk: **683.95**
- **Archetype:** `file_cluster_17` (Distance: 15.054 IQR)
- **Magnitude:** 213.58 | **LOC:** 177 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9071%)
- **Heaviest Functions:** `surrogate` (Impact: 50.3), `supersurrogate` (Impact: 48.8), `surrogdistrib` (Impact: 12.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `functions/timefreqfunc/newcrossf.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.758 IQR)
- **Top Global Matches:** file_cluster_17: 14.758, file_cluster_11: 14.958, file_cluster_8: 15.011
- **Magnitude:** 14504.64 | **LOC:** 1468 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (85.4239%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 402`, `structural_boundaries: 167`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 654`, `dead_code: 13`
* *Architecture:* None
* *Defense:* `safety: 84`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/supportfiles/channel_location_files/neuroscan/cap128.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/runica_ml.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.746 IQR)
- **Top Global Matches:** file_cluster_17: 14.746, file_cluster_11: 14.796, file_cluster_8: 14.808
- **Magnitude:** 4727.19 | **LOC:** 1113 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (78.1781%), Tech Debt (12.1476%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 196`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 683`, `dead_code: 15`, `fragile_debt: 2`
* *Architecture:* None
* *Defense:* `safety: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/runica_ml2.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.749 IQR)
- **Top Global Matches:** file_cluster_17: 14.749, file_cluster_11: 14.8, file_cluster_8: 14.812
- **Magnitude:** 4705.94 | **LOC:** 1113 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (77.9569%), Tech Debt (12.134%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 196`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 689`, `dead_code: 15`, `fragile_debt: 2`
* *Architecture:* None
* *Defense:* `safety: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/runica_mlb.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.779 IQR)
- **Top Global Matches:** file_cluster_17: 14.779, file_cluster_11: 14.835, file_cluster_8: 14.847
- **Magnitude:** 4565.93 | **LOC:** 1098 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (77.7842%), Tech Debt (12.2666%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 190`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 672`, `dead_code: 15`, `fragile_debt: 2`
* *Architecture:* None
* *Defense:* `safety: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/popfunc/pop_runica.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.973 IQR)
- **Top Global Matches:** file_cluster_17: 13.973, file_cluster_8: 14.014, file_cluster_4: 14.119
- **Magnitude:** 4044.32 | **LOC:** 695 | **CtrlFlow:** 56.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (81.4666%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 126`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 490`, `dead_code: 3`
* *Architecture:* `concurrency: 6`
* *Defense:* `safety: 40`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/miscfunc/tftopo.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.392 IQR)
- **Top Global Matches:** file_cluster_17: 14.392, file_cluster_11: 14.637, file_cluster_0: 14.661
- **Magnitude:** 3423.12 | **LOC:** 681 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (80.5331%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 106`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 319`, `dead_code: 9`
* *Architecture:* None
* *Defense:* `safety: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/popfunc/pop_headplot.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.657 IQR)
- **Top Global Matches:** file_cluster_17: 13.657, file_cluster_8: 13.686, file_cluster_0: 13.873
- **Magnitude:** 2748.26 | **LOC:** 551 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (78.7064%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 79`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 370`, `dead_code: 1`
* *Architecture:* `io: 8`
* *Defense:* `safety: 37`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/popfunc/pop_topoplot.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.965 IQR)
- **Top Global Matches:** file_cluster_17: 14.965, file_cluster_11: 15.35, file_cluster_0: 15.387
- **Magnitude:** 2649.82 | **LOC:** 467 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 105
- **Risk Profile:** Cognitive Load (82.9604%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pop_topoplot` (Impact: 2334.3 | O(2^N) | DB: 105)
    * *Intent:* % ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE % LIABLE FOR ANY DIRECT,...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 71`, `args: 2`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 309`, `dead_code: 5`
* *Architecture:* None
* *Defense:* `safety: 44`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/miscfunc/topoimage.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.53 IQR)
- **Top Global Matches:** file_cluster_17: 13.53, file_cluster_8: 13.559, file_cluster_11: 13.757
- **Magnitude:** 2586.06 | **LOC:** 685 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (72.7236%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 89`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 439`, `dead_code: 5`
* *Architecture:* `io: 7`
* *Defense:* `safety: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/miscfunc/eegplotold.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.029 IQR)
- **Top Global Matches:** file_cluster_8: 13.029, file_cluster_17: 13.09, file_cluster_2: 13.249
- **Magnitude:** 2469.33 | **LOC:** 1026 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (63.8417%), Tech Debt (10.4529%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 70`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 550`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `io: 10`
* *Defense:* `safety: 27`, `cleanup: 41`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/miscfunc/crossfold.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.665 IQR)
- **Top Global Matches:** file_cluster_17: 13.665, file_cluster_8: 13.703, file_cluster_11: 13.901
- **Magnitude:** 2228.12 | **LOC:** 548 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (79.3755%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 56`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 324`, `dead_code: 3`
* *Architecture:* None
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/popfunc/pop_loadset.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.301 IQR)
- **Top Global Matches:** file_cluster_17: 14.301, file_cluster_8: 14.383, file_cluster_0: 14.444
- **Magnitude:** 2067.81 | **LOC:** 432 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (79.4381%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 70`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 270`, `dead_code: 2`
* *Architecture:* `io: 5`
* *Defense:* `safety: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/popfunc/eeg_eegrej.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.1 IQR)
- **Top Global Matches:** file_cluster_17: 16.1, file_cluster_11: 16.402, file_cluster_9: 16.428
- **Magnitude:** 2016.65 | **LOC:** 264 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (88.4906%), Tech Debt (78.7169%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 51`, `args: 5`, `func_start: 3`
* *Risk/State:* `state_mutation: 150`, `dead_code: 4`, `fragile_debt: 3`
* *Architecture:* None
* *Defense:* `safety: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/plotdata.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.044 IQR)
- **Top Global Matches:** file_cluster_17: 15.044, file_cluster_0: 15.338, file_cluster_11: 15.343
- **Magnitude:** 1931.0 | **LOC:** 581 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (75.2581%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 67`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 283`, `dead_code: 10`
* *Architecture:* `io: 2`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/movav.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.685 IQR)
- **Top Global Matches:** file_cluster_8: 13.685, file_cluster_17: 13.75, file_cluster_0: 13.851
- **Magnitude:** 1654.96 | **LOC:** 281 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (84.3943%), Tech Debt (84.4323%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 38`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 185`, `dead_code: 1`, `fragile_debt: 4`
* *Architecture:* None
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/popfunc/eeg_amplitudearea.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.665 IQR)
- **Top Global Matches:** file_cluster_8: 13.665, file_cluster_17: 14.008, file_cluster_11: 14.056
- **Magnitude:** 1604.13 | **LOC:** 245 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (75.3491%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 29`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 294`, `dead_code: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/miscfunc/hungarian.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.385 IQR)
- **Top Global Matches:** file_cluster_8: 13.385, file_cluster_13: 13.884, file_cluster_7: 13.907
- **Magnitude:** 1574.14 | **LOC:** 468 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (74.1072%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 34`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 322`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/phasecoher.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.837 IQR)
- **Top Global Matches:** file_cluster_17: 13.837, file_cluster_8: 13.938, file_cluster_11: 14.009
- **Magnitude:** 1435.4 | **LOC:** 408 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (74.5115%), Tech Debt (22.27%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 43`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 221`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* None
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/miscfunc/envproj.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.121 IQR)
- **Top Global Matches:** file_cluster_17: 13.121, file_cluster_8: 13.205, file_cluster_11: 13.404
- **Magnitude:** 1401.39 | **LOC:** 399 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (76.4641%), Tech Debt (43.2584%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 55`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 249`, `dead_code: 2`, `fragile_debt: 3`
* *Architecture:* `io: 4`
* *Defense:* `safety: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/studyfunc/pop_erspparams.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.298 IQR)
- **Top Global Matches:** file_cluster_17: 15.298, file_cluster_0: 15.43, file_cluster_11: 15.473
- **Magnitude:** 1392.76 | **LOC:** 237 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.0834%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 23`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 107`, `dead_code: 3`
* *Architecture:* None
* *Defense:* `safety: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/signalstat.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.974 IQR)
- **Top Global Matches:** file_cluster_8: 12.974, file_cluster_17: 12.974, file_cluster_2: 13.195
- **Magnitude:** 1378.07 | **LOC:** 469 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (71.1998%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 38`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 231`, `dead_code: 2`
* *Architecture:* None
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/popfunc/pop_jointprob.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.218 IQR)
- **Top Global Matches:** file_cluster_8: 13.218, file_cluster_17: 13.342, file_cluster_0: 13.403
- **Magnitude:** 1371.82 | **LOC:** 287 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (76.5078%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pop_jointprob` (Impact: 1229.5 | O(2^N) | DB: 57)
    * *Intent:* % IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE % ARE DISCLAIMED. IN NO...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 27`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 139`, `dead_code: 1`
* *Architecture:* None
* *Defense:* `safety: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/popfunc/pop_rejkurt.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.161 IQR)
- **Top Global Matches:** file_cluster_8: 13.161, file_cluster_17: 13.287, file_cluster_0: 13.349
- **Magnitude:** 1365.58 | **LOC:** 283 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 55
- **Risk Profile:** Cognitive Load (76.7656%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pop_rejkurt` (Impact: 1229.3 | O(2^N) | DB: 55)
    * *Intent:* % IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE % ARE DISCLAIMED. IN NO...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 27`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 133`, `dead_code: 1`
* *Architecture:* None
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/miscfunc/timefrq.m` (MATLAB | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.618 IQR)
- **Top Global Matches:** file_cluster_8: 13.618, file_cluster_17: 13.677, file_cluster_13: 13.878
- **Magnitude:** 1354.91 | **LOC:** 416 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (73.1743%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 64`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 244`, `dead_code: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `functions/@mmo/mmo.m` (MATLAB) | Magnitude: 244.2 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 93, state_mutation: 62, structural_boundaries: 34, branch: 25
- `functions/popfunc/pop_chanevent.m` (MATLAB) | Magnitude: 172.84 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 135, indent_spaces: 115, branch: 67, structural_boundaries: 65
- `functions/popfunc/pop_loadbci.m` (MATLAB) | Magnitude: 269.36 | Delta: **0.152 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 241, indent_spaces: 164, structural_boundaries: 59, branch: 45
- `functions/sigprocfunc/eegrej.m` (MATLAB) | Magnitude: 212.16 | Delta: **0.326 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 140, structural_boundaries: 70, indent_spaces: 67, branch: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `functions/popfunc/eeg_laplac.m` (MATLAB) | Magnitude: 505.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 123, indent_spaces: 36, scientific: 20, branch: 16
- `functions/statistics/ttest2_cell.m` (MATLAB) | Magnitude: 144.14 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 88, indent_spaces: 58, branch: 19, scientific: 15
- `functions/sigprocfunc/jader.m` (MATLAB) | Magnitude: 562.23 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 186, branch: 22, indent_tabs: 19, structural_boundaries: 11
- `functions/statistics/corrcoef_cell.m` (MATLAB) | Magnitude: 104.82 | Delta: **0.126 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 93, indent_spaces: 39, scientific: 15, branch: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `functions/popfunc/pop_interp.m` (MATLAB) | Magnitude: 896.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 160, state_mutation: 133, branch: 47, structural_boundaries: 32
- `functions/sigprocfunc/floatwrite.m` (MATLAB) | Magnitude: 323.14 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 37, state_mutation: 30, branch: 18, structural_boundaries: 12
- `functions/sigprocfunc/icaproj.m` (MATLAB) | Magnitude: 646.06 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 59, state_mutation: 42, branch: 38, structural_boundaries: 34
- `functions/studyfunc/std_editset.m` (MATLAB) | Magnitude: 331.98 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 294, indent_spaces: 227, branch: 88, structural_boundaries: 61
- `functions/sigprocfunc/plotcurve.m` (MATLAB) | Magnitude: 212.54 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 243, state_mutation: 178, branch: 83, structural_boundaries: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `functions/studyfunc/std_precomp.m` (MATLAB) | Magnitude: 457.2 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 402, indent_spaces: 308, branch: 125, structural_boundaries: 80
- `functions/adminfunc/eeg_eval.m` (MATLAB) | Magnitude: 170.2 | Delta: **0.282 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 130, indent_spaces: 113, branch: 32, structural_boundaries: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `functions/miscfunc/averef.m` (MATLAB) | Magnitude: 119.71 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 36, indent_tabs: 7, structural_boundaries: 6, indent_spaces: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `functions/sigprocfunc/signalstat.m` (MATLAB) | Magnitude: 1378.07 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 231, indent_spaces: 106, branch: 57, indent_tabs: 45
- `functions/sigprocfunc/timtopo.m` (MATLAB) | Magnitude: 316.32 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 293, indent_spaces: 191, branch: 86, structural_boundaries: 49
- `functions/miscfunc/headmovie.m` (MATLAB) | Magnitude: 864.11 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 165, indent_spaces: 83, branch: 42, structural_boundaries: 33
- `functions/sigprocfunc/binica.m` (MATLAB) | Magnitude: 267.8 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 237, indent_spaces: 207, branch: 95, structural_boundaries: 77
- `functions/miscfunc/caliper.m` (MATLAB) | Magnitude: 936.7 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 129, indent_spaces: 88, branch: 42, structural_boundaries: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `functions/statistics/anova2_cell.m` (MATLAB) | Magnitude: 73.1 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 67, indent_spaces: 62, branch: 20, structural_boundaries: 11
- `functions/statistics/anova1_cell.m` (MATLAB) | Magnitude: 90.36 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 83, indent_spaces: 59, branch: 14, structural_boundaries: 9
- `functions/@mmo/permute.m` (MATLAB) | Magnitude: 30.2 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 22, dead_code: 16, indent_spaces: 11, branch: 10
- `functions/adminfunc/pop_delset.m` (MATLAB) | Magnitude: 64.58 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 39, structural_boundaries: 13, branch: 12, indent_tabs: 12
- `functions/sigprocfunc/readeetraklocs.m` (MATLAB) | Magnitude: 74.42 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 41, indent_spaces: 40, branch: 15, structural_boundaries: 12

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `functions/sigprocfunc/readeetraklocs.m` -> Churn: **93.94%** | Cog Load: 87.558% | Debt: 0.0%
- `functions/adminfunc/plugin_askinstall.m` -> Churn: **72.7%** | Cog Load: 90.4651% | Debt: 89.9121%
- `functions/adminfunc/eeglab_update.m` -> Churn: **66.41%** | Cog Load: 77.86% | Debt: 0.0%
- `functions/timefreqfunc/tf_cycle_calc.m` -> Churn: **59.16%** | Cog Load: 81.4389% | Debt: 0.0%
- `functions/popfunc/pop_runica.m` -> Churn: **51.45%** | Cog Load: 81.4666% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `functions/popfunc/pop_runica.m` -> **Arnaud Delorme** (100.0% isolated ownership) | Magnitude: 4044.32
- `functions/popfunc/pop_topoplot.m` -> **Arnaud Delorme** (100.0% isolated ownership) | Magnitude: 2649.82
- `functions/popfunc/pop_loadset.m` -> **Arnaud Delorme** (100.0% isolated ownership) | Magnitude: 2067.81
- `eeglab.m` -> **Arnaud Delorme** (100.0% isolated ownership) | Magnitude: 1303.78
- `functions/adminfunc/plugin_menu.m` -> **Arnaud Delorme** (100.0% isolated ownership) | Magnitude: 1254.36

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `functions/adminfunc/troubleshooting_data_formats.m` -> **Severity: 147.2** (Blast Radius: 1.493 * Doc Risk: 98.5936%)
- `functions/@mmo/unitaryopp.m` -> **Severity: 146.632** (Blast Radius: 1.493 * Doc Risk: 98.2131%)
- `functions/supportfiles/EEGLAB_verbose` -> **Severity: 146.275** (Blast Radius: 1.493 * Doc Risk: 97.9742%)
- `functions/@eegobj/subsasgn.m` -> **Severity: 145.69** (Blast Radius: 1.493 * Doc Risk: 97.5821%)
- `functions/adminfunc/abouteeglab.m` -> **Severity: 143.218** (Blast Radius: 1.493 * Doc Risk: 95.926%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
