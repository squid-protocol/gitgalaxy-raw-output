# ARCHITECTURAL_BRIEF: eeglab
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/sccn/eeglab` |
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
| Total Artifacts | 826 |
| Analyzed Artifacts (Scanned) | 677 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 149 |
| Total LOC | 84580 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 82.0% |
| Dominant Lang | MATLAB |

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
| MATLAB | 650 | 84452 | 96.0% |
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
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +2.88; from the repo's file-archetype mix)
> **File Composition:** Many-Argument Workhorses Files 43%, Defensive Guards Files 20%, Compute Cores Files 14%, Data / Markup / Trivial 13%, Large Core Modules 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 662 | 97.8% |
| Unknown | 2 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 13 | 1.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 149*

**Composition by Extension & Reason:**
- `.sfp`: 45x Excluded (Unsupported Extension: '.sfp')
- `.ced`: 12x Excluded (Unsupported Extension: '.ced')
- `.locs`: 12x Excluded (Unsupported Extension: '.locs')
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Binary Format Detected)
- `.m`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 17 LOC), 1x Excluded (Machine-Generated Source Code Signature: 31 LOC)
- `.elp`: 7x Excluded (Unsupported Extension: '.elp')
- `.dat`: 4x Excluded (Unsupported Extension: '.dat'), 3x Excluded (Unsupported Extension: '.DAT')
- `.xyz`: 3x Excluded (Unsupported Extension: '.xyz')
- `.loc`: 3x Excluded (Unsupported Extension: '.loc')
- `.map`: 3x Excluded (Unsupported Extension: '.map')
- `.mat`: 3x Excluded (Unsupported Extension: '.mat')
- `.fdt`: 3x Excluded (Unsupported Extension: '.fdt')
- `.set`: 3x Excluded (Unsupported Extension: '.set')
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.1 | 61.2 | 72.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 82.5 | 95.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 37.7 | 40.4 | 62.2 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 31.6 | 2.7 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 9.0 | 3.3 | 3.2 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 81.9 | 0.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 88.1 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 13.9 | 10.4 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 92.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.1 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 92.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1410 | 311 | 5 | `functions/studyfunc/std_serialize.m` |
| cleanup | 438 | 159 | 2 | `functions/sigprocfunc/eegplot.m` |
| guards | 7236 | 479 | 29 | `functions/adminfunc/eeg_checkset.m` |
| danger | 1813 | 364 | 7 | `functions/sigprocfunc/runica.m` |
| concurrency | 21 | 13 | 0 | `functions/miscfunc/runicalowmem.m` |
| connectivity | 1082 | 624 | 3 | `functions/studyfunc/std_serialize.m` |
| io | 486 | 125 | 2 | `functions/studyfunc/std_limoresults.m` |
| crypto | 0 | 0 | 0 | - |
| ipc | 19 | 11 | 0 | `functions/sigprocfunc/coregister.m` |
| time | 75 | 35 | 0 | `functions/miscfunc/icademo.m` |
| serialization | 222 | 63 | 0 | `functions/studyfunc/std_limoresults.m` |
| regex | 16 | 7 | 0 | `functions/popfunc/pop_topochansel.m` |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 51 | 21 | 0 | `functions/studyfunc/std_lm_getvars.m` |
| debt | 3104 | 371 | 11 | `eeglab.m` |
| mutation | 53530 | 627 | 184 | `eeglab.m` |
| dead_code | 2071 | 637 | 5 | `functions/miscfunc/runicalowmem.m` |
| credential | 2 | 2 | 0 | `functions/adminfunc/eeg_checkset.m` |
| threat | 133 | 55 | 0 | `functions/timefreqfunc/timefreq.m` |
| ml_ai | 1024 | 179 | 4 | `functions/timefreqfunc/newcrossf.m` |
| ui | 920 | 159 | 4 | `functions/sigprocfunc/eegplot.m` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.4**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `functions/studyfunc/std_limoresults.m` (Hits: 37)
- `functions/sigprocfunc/readegihdr.m` (Hits: 21)
- `functions/timefreqfunc/crossf.m` (Hits: 21)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
No file in this repository declares an import that GitGalaxy resolved, so there is no coupling ranking to report. See the note above -- the same caveat applies.


## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `toporeplot` **(Many-Argument Workhorses)** (@ `functions/studyfunc/toporeplot.m`) -> Impact: **1025.4** | LOC: 714
  * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" % AND ANY EXP...
- `runica` **(Many-Argument Workhorses)** (@ `functions/sigprocfunc/runica_ml.m`) -> Impact: **881.3** | LOC: 538
  * *Intent:* % 02-27-98 use PINV instead of INV to rank order comps if ncomps < chans -sm % 04-28-98 added 'posact' and 'pca' flags -sm % 07-16-98 reduced length o...
- `runica` **(Many-Argument Workhorses)** (@ `functions/sigprocfunc/runica_ml2.m`) -> Impact: **881.3** | LOC: 538
  * *Intent:* % 02-27-98 use PINV instead of INV to rank order comps if ncomps < chans -sm % 04-28-98 added 'posact' and 'pca' flags -sm % 07-16-98 reduced length o...
- `runica` **(Many-Argument Workhorses)** (@ `functions/sigprocfunc/runica_mlb.m`) -> Impact: **881.3** | LOC: 537
  * *Intent:* % 02-27-98 use PINV instead of INV to rank order comps if ncomps < chans -sm % 04-28-98 added 'posact' and 'pca' flags -sm % 07-16-98 reduced length o...
- `runica` **(Many-Argument Workhorses)** (@ `functions/miscfunc/runicatest.m`) -> Impact: **864.0** | LOC: 520
  * *Intent:* % 02-27-98 use PINV instead of INV to rank order comps if ncomps < chans -sm % 04-28-98 added 'posact' and 'pca' flags -sm % 07-16-98 reduced length o...
- `Anonymous_Block` **(Many-Argument Workhorses)** (@ `functions/timefreqfunc/newcrossf.m`) -> Impact: **609.8** | LOC: 733
- `topoplot` **(Many-Argument Workhorses)** (@ `functions/sigprocfunc/topoplot.m`) -> Impact: **584.5** | LOC: 890
  * *Intent:* % 2-26-98 Revised by Colin % -changed image back to surface command % -added fill and blank styles % -removed extra background colormap entry (now use...
- `Anonymous_Block_[Truncated]` **(Many-Argument Workhorses)** (@ `functions/popfunc/pop_chanedit.m`) -> Impact: **540.0** | LOC: 880
- `binica` **(Many-Argument Workhorses)** (@ `functions/sigprocfunc/binica.m`) -> Impact: **467.3** | LOC: 372
  * *Intent:* % SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS % INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN %...
- `crossf` **(Many-Argument Workhorses)** (@ `functions/miscfunc/crossfold.m`) -> Impact: **438.7** | LOC: 330
  * *Intent:* % THE POSSIBILITY OF SUCH DAMAGE. % 11-20-98 defined LINEWIDTH constant -sm % 04-01-99 made number of frequencies consistent -se % 06-29-99 fixed cons...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `functions/studyfunc` | 132 | 31920.18 | 66.45% | 36.12% |
| `functions/sigprocfunc` | 114 | 31857.68 | 64.57% | 41.91% |
| `functions/popfunc` | 130 | 31496.62 | 71.74% | 28.82% |
| `functions/miscfunc` | 110 | 19404.1 | 62.81% | 44.2% |
| `functions/timefreqfunc` | 24 | 8677.14 | 64.12% | 40.21% |
| `functions/adminfunc` | 66 | 6565.18 | 47.01% | 35.03% |
| `functions/supportfiles/channel_location_files/neuroscan` | 2 | 5001.0 | 0.0% | 0.0% |
| `functions/statistics` | 16 | 2808.4 | 72.63% | 47.02% |
| `__monolith__` | 5 | 1972.04 | 14.94% | 2.08% |
| `functions/guifunc` | 10 | 1655.36 | 55.9% | 34.75% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `functions/adminfunc/eeglab_error.m` -> **99.9983%** Exposure
- `functions/sigprocfunc/textsc.m` -> **99.8499%** Exposure
- `functions/studyfunc/std_savedat.m` -> **99.8499%** Exposure
- `functions/statistics/anova1_cell.m` -> **99.0462%** Exposure
- `functions/popfunc/eeg_insertboundold.m` -> **98.3591%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `eeglab.m` -> **100.0%** Exposure
- `functions/@eegobj/subsasgn.m` -> **100.0%** Exposure
- `functions/@memmapdata/size.m` -> **100.0%** Exposure
- `functions/@memmapdata/subsref.m` -> **100.0%** Exposure
- `functions/@memmapdata/sum.m` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `functions/timefreqfunc/newcrossf.m` -> **5** Orphaned Functions | **0** Duplicates
- `functions/studyfunc/pop_addindepvar.m` -> **4** Orphaned Functions | **0** Duplicates
- `functions/studyfunc/std_readeegfield.m` -> **4** Orphaned Functions | **0** Duplicates
- `functions/miscfunc/corrimage.m` -> **3** Orphaned Functions | **0** Duplicates
- `functions/popfunc/eeg_topoplot.m` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `7` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `0` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `functions/studyfunc/std_precomp.m` (MATLAB) -> Cumulative Risk: **700.55**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.47)
- **Magnitude:** 770.2 | **LOC:** 611 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.2636%)
- **Heaviest Functions:** `std_precomp` (Many-Argument Workhorses, Impact: 273.7), `getchansandopts` (Many-Argument Workhorses, Impact: 34.0), `getclustcomps` (Many-Argument Workhorses, Impact: 33.0)

### 2. `functions/adminfunc/eeg_eval.m` (MATLAB) -> Cumulative Risk: **683.96**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +2.30)
- **Magnitude:** 210.7 | **LOC:** 193 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.5792%)
- **Heaviest Functions:** `eeg_eval` (Many-Argument Workhorses, Impact: 73.2), `update_datafield` (I/O & Config Routines, Impact: 3.2)

### 3. `functions/studyfunc/std_createclust.m` (MATLAB) -> Cumulative Risk: **671.7**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.08)
- **Magnitude:** 187.36 | **LOC:** 273 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.7102%)
- **Heaviest Functions:** `std_createclust` (Many-Argument Workhorses, Impact: 28.4), `__global_context__` (I/O & Config Routines, Impact: 5.0), `Anonymous_Block` (I/O & Config Routines, Impact: 4.8)

### 4. `functions/sigprocfunc/movav.m` (MATLAB) -> Cumulative Risk: **671.68**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.83)
- **Magnitude:** 411.86 | **LOC:** 281 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.3342%)
- **Heaviest Functions:** `movav` (Many-Argument Workhorses, Impact: 217.8), `nan_mean` (Compute Cores, Impact: 8.6), `nan_sum` (Interface Declarations, Impact: 2.0)

### 5. `functions/adminfunc/getkeyval.m` (MATLAB) -> Cumulative Risk: **668.48**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.18)
- **Magnitude:** 136.08 | **LOC:** 147 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.3457%)
- **Heaviest Functions:** `getkeyval` (Many-Argument Workhorses, Impact: 38.8), `Anonymous_Block` (Defensive Guards, Impact: 15.3), `__global_context__` (I/O & Config Routines, Impact: 4.5)

### 6. `functions/popfunc/eeg_insertboundold.m` (MATLAB) -> Cumulative Risk: **667.88**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +0.20)
- **Magnitude:** 186.02 | **LOC:** 196 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.5762%)
- **Heaviest Functions:** `eeg_insertboundold` (Many-Argument Workhorses, Impact: 26.4), `findnested` (Compute Cores, Impact: 15.9), `Anonymous_Block` (Defensive Guards, Impact: 9.1)

### 7. `functions/studyfunc/std_limo.m` (MATLAB) -> Cumulative Risk: **667.85**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +0.69)
- **Magnitude:** 892.28 | **LOC:** 755 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.3899%)
- **Heaviest Functions:** `std_limo` (Many-Argument Workhorses, Impact: 65.5), `Anonymous_Block` (Compute Cores, Impact: 48.5), `__global_context__` (Compute Cores, Impact: 28.6)

### 8. `functions/studyfunc/std_readtopo.m` (MATLAB) -> Cumulative Risk: **664.7**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.31)
- **Magnitude:** 148.8 | **LOC:** 176 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.7705%)
- **Heaviest Functions:** `Anonymous_Block` (Defensive Guards, Impact: 47.4), `std_readtopo` (Many-Argument Workhorses, Impact: 7.9), `Anonymous_Block` (I/O & Config Routines, Impact: 4.5)

### 9. `functions/miscfunc/fieldtrip2eeglab.m` (MATLAB) -> Cumulative Risk: **664.24**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.22)
- **Magnitude:** 168.64 | **LOC:** 141 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.5809%)
- **Heaviest Functions:** `fieldtrip2eeglab` (Many-Argument Workhorses, Impact: 58.5), `__global_context__` (I/O & Config Routines, Impact: 2.5)

### 10. `functions/popfunc/pop_resample.m` (MATLAB) -> Cumulative Risk: **657.69**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +0.59)
- **Magnitude:** 427.36 | **LOC:** 462 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.3614%)
- **Heaviest Functions:** `pop_resample` (Many-Argument Workhorses, Impact: 160.9), `firfiltdcpadded` (Defensive Guards, Impact: 17.4), `myresample` (Many-Argument Workhorses, Impact: 12.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `functions/supportfiles/channel_location_files/neuroscan/cap128.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/timefreqfunc/crossf.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 2402.06 | **LOC:** 1458 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.8499%), Tech Debt (8.8137%)
**Top Internal Functions/Classes:**
  * `crossf` **(Many-Argument Workhorses)** (Impact: 421.7)
    * *Intent:* % Note: 3 "objects" (Tf, Coher and Boot) are handled by specific functions under Matlab % (Tf) funct...
  * `tfitc` **(Many-Argument Workhorses)** (Impact: 159.4)
    * *Intent:* % function for itc % ----------------
  * `bootinit` **(Many-Argument Workhorses)** (Impact: 127.3)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% BOOTSTRAP %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %%%%%%%%%%%%%%%%%...
  * `tfcomp` **(Many-Argument Workhorses)** (Impact: 123.0)
    * *Intent:* % function for time freq decomposition % ------------------------------------ % tf is an structure c...
  * `tfitcpost` **(Many-Argument Workhorses)** (Impact: 120.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 235 instances
* *Memory Alloc (weighted view):* 22
* *State Mutation (weighted view):* 769
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 197`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 299`, `dead_code: 28`, `unreferenced_by_name: 1`
* *Architecture:* `io: 21`, `api: 14`
* *Defense:* `safety: 97`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/topoplot.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1958.1 | **LOC:** 1804 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.4136%), Tech Debt (8.4979%)
**Top Internal Functions/Classes:**
  * `topoplot` **(Many-Argument Workhorses)** (Impact: 584.5)
    * *Intent:* % 2-26-98 Revised by Colin % -changed image back to surface command % -added fill and blank styles %...
  * `Anonymous_Block` **(Compute Cores)** (Impact: 118.5)
    * *Intent:* % %%%%%%%%%%%%%%%%%%% Plot filled ring to mask jagged grid boundary %%%%%%%%%%%%%%%%%%%%%%%%%%% % hw...
  * `__global_context__` **(I/O & Config Routines)** (Impact: 19.5)
    * *Intent:* % (looking down at the top of the head) using interpolation on a fine % cartesian grid. Can also sho...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 9.1)
    * *Intent:* % %%%%%%%%%%% reset color limits for grid plot %%%%%%%%%%%%%%%%%%%%%%%%% %
  * `disk` **(Many-Argument Workhorses)** (Impact: 8.8)
    * *Intent:* % %%%%%%%%%%%%% Draw circle %%%%%%%%%%%%%%%%%%%%%%%% %
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 328 instances
* *Memory Alloc (weighted view):* 32
* *State Mutation (weighted view):* 1116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 429`, `structural_boundaries: 243`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 460`, `dead_code: 25`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`
* *Defense:* `safety: 79`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `eeglab.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1947.28 | **LOC:** 2293 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.7161%), Tech Debt (10.4147%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Compute Cores)** (Impact: 126.2)
  * `eeg_mainfig` **(Compute Cores)** (Impact: 81.5)
    * *Intent:* % REMOVED MENUS %eegmenu( false, tools_m, 'Label', 'Automatic comp. reject', 'enable', 'off', 'CallB...
  * `__global_context__` **(Compute Cores)** (Impact: 64.1)
    * *Intent:* % electrophysiological data analysis incorporating the ICA/EEG toolbox % (Makeig et al.) developed a...
  * `popask` **(Defensive Guards)** (Impact: 55.9)
  * `Anonymous_Block` **(Defensive Guards)** (Impact: 36.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 314 instances
* *State Mutation (weighted view):* 1139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 442`, `structural_boundaries: 348`, `args: 26`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 2`, `state_mutation: 511`, `dead_code: 9`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 7`, `api: 13`
* *Defense:* `safety: 171`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/timefreqfunc/newcrossf.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1800.24 | **LOC:** 1468 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.2953%), Tech Debt (12.8995%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Many-Argument Workhorses)** (Impact: 609.8)
  * `newcrossf` **(Many-Argument Workhorses)** (Impact: 120.6)
    * *Intent:* % There are 3 "objects" Tf, Coher and Boot which are handled % - by specific functions under Matlab ...
  * `ampcorr` **(Many-Argument Workhorses)** (Impact: 104.9)
    * *Intent:* % *********************************************************************** % ------------------------...
  * `plotall` **(Many-Argument Workhorses)** (Impact: 62.4)
    * *Intent:* % ------------------ % plotting functions % ------------------
  * `coherinit` **(Many-Argument Workhorses)** (Impact: 44.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% COHERENCE OBSOLETE %%%%%%%%%%%%%%%%%%%%%%%%% %%%%%%%%%%%%%%%%%%%%%%...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 209 instances
* *State Mutation (weighted view):* 642
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 353`, `structural_boundaries: 233`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 224`, `dead_code: 14`, `unreferenced_by_name: 5`
* *Architecture:* `api: 10`
* *Defense:* `safety: 129`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/runica_ml2.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1699.14 | **LOC:** 1113 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.5334%), Tech Debt (11.1888%)
**Top Internal Functions/Classes:**
  * `runica` **(Many-Argument Workhorses)** (Impact: 881.3)
    * *Intent:* % 02-27-98 use PINV instead of INV to rank order comps if ncomps < chans -sm % 04-28-98 added 'posac...
  * `Anonymous_Block` **(Compute Cores)** (Impact: 68.5)
    * *Intent:* % a position dependent on the system clock
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 21.8)
    * *Intent:* % %%%%%%%%%%%%%%%%%%% Perform sphering %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %
  * `Anonymous_Block` **(Compute Cores)** (Impact: 5.3)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 204 instances
* *Memory Alloc (weighted view):* 21
* *State Mutation (weighted view):* 668
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 198`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 260`, `dead_code: 23`, `fragile_debt: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/runica_ml.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1695.1 | **LOC:** 1113 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.7565%), Tech Debt (11.1992%)
**Top Internal Functions/Classes:**
  * `runica` **(Many-Argument Workhorses)** (Impact: 881.3)
    * *Intent:* % 02-27-98 use PINV instead of INV to rank order comps if ncomps < chans -sm % 04-28-98 added 'posac...
  * `Anonymous_Block` **(Compute Cores)** (Impact: 70.5)
    * *Intent:* % a position dependent on the system clock
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 21.8)
    * *Intent:* % %%%%%%%%%%%%%%%%%%% Perform sphering %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %
  * `Anonymous_Block` **(Compute Cores)** (Impact: 5.3)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 202 instances
* *Memory Alloc (weighted view):* 21
* *State Mutation (weighted view):* 662
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 198`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 258`, `dead_code: 23`, `fragile_debt: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/runica.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1679.74 | **LOC:** 1582 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (73.8667%), Tech Debt (8.9084%)
**Top Internal Functions/Classes:**
  * `runica` **(Many-Argument Workhorses)** (Impact: 343.8)
    * *Intent:* % 02-27-98 use PINV instead of INV to rank order comps if ncomps < chans -sm % 04-28-98 added 'posac...
  * `Anonymous_Block` **(Compute Cores)** (Impact: 47.0)
    * *Intent:* %% Compute ICA Weights
  * `Anonymous_Block` **(Compute Cores)** (Impact: 46.6)
    * *Intent:* %% Compute ICA Weights
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 33.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %% Compute ICA Weights
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 33.4)
    * *Intent:* %% Compute ICA Weights
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 322 instances
* *State Mutation (weighted view):* 1081
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 349`, `structural_boundaries: 226`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 437`, `dead_code: 40`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 2`
* *Defense:* `safety: 42`, `doc: 5`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/runica_mlb.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1673.06 | **LOC:** 1098 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.3481%), Tech Debt (11.2905%)
**Top Internal Functions/Classes:**
  * `runica` **(Many-Argument Workhorses)** (Impact: 881.3)
    * *Intent:* % 02-27-98 use PINV instead of INV to rank order comps if ncomps < chans -sm % 04-28-98 added 'posac...
  * `Anonymous_Block` **(Compute Cores)** (Impact: 59.8)
    * *Intent:* % a position dependent on the system clock
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 21.8)
    * *Intent:* % %%%%%%%%%%%%%%%%%%% Perform sphering %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %
  * `Anonymous_Block` **(Compute Cores)** (Impact: 5.3)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 4.5)
    * *Intent:* % %%%%%%%%%%%%%%%%%% return nonlinearly-transformed data %%%%%%%%%%%%%%%% %
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 198 instances
* *Memory Alloc (weighted view):* 17
* *State Mutation (weighted view):* 651
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 192`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 255`, `dead_code: 23`, `fragile_debt: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/eegplot.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1671.02 | **LOC:** 2222 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.8288%), Tech Debt (8.5311%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Compute Cores)** (Impact: 407.4)
  * `eegplot` **(Defensive Guards)** (Impact: 28.8)
    * *Intent:* % 1 - winlength % 2 - srate % 3 - children % 'backeeg' axis % 1 - trialtag % 2 - g.winrej % 3 - nest...
  * `defmotion` **(Compute Cores)** (Impact: 26.4)
    * *Intent:* % Function to show the value and electrode at mouse position
  * `Anonymous_Block` **(Compute Cores)** (Impact: 25.6)
  * `__global_context__` **(I/O & Config Routines)** (Impact: 22.1)
    * *Intent:* % Allows vertical scrolling through channels and manual marking % and unmarking of data stretches or...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 333 instances
* *State Mutation (weighted view):* 1118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 381`, `structural_boundaries: 388`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 452`, `dead_code: 17`, `fragile_debt: 1`
* *Architecture:* `api: 3`
* *Defense:* `safety: 185`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/eegplotlegacy.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1634.94 | **LOC:** 2187 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.2874%), Tech Debt (8.5401%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Compute Cores)** (Impact: 404.1)
  * `Anonymous_Block` **(Compute Cores)** (Impact: 25.6)
  * `defmotion` **(Compute Cores)** (Impact: 24.9)
    * *Intent:* % Function to show the value and electrode at mouse position
  * `__global_context__` **(I/O & Config Routines)** (Impact: 22.0)
    * *Intent:* % Allows vertical scrolling through channels and manual marking % and unmarking of data stretches or...
  * `eegplotlegacy` **(Defensive Guards)** (Impact: 18.9)
    * *Intent:* % 1 - winlength % 2 - srate % 3 - children % 'backeeg' axis % 1 - trialtag % 2 - g.winrej % 3 - nest...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 324 instances
* *State Mutation (weighted view):* 1097
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 372`, `structural_boundaries: 375`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 449`, `dead_code: 15`, `fragile_debt: 1`
* *Architecture:* `api: 3`
* *Defense:* `safety: 178`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/miscfunc/runicatest.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1599.66 | **LOC:** 1062 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.7189%), Tech Debt (9.5961%)
**Top Internal Functions/Classes:**
  * `runica` **(Many-Argument Workhorses)** (Impact: 864.0)
    * *Intent:* % 02-27-98 use PINV instead of INV to rank order comps if ncomps < chans -sm % 04-28-98 added 'posac...
  * `Anonymous_Block` **(Compute Cores)** (Impact: 58.1)
    * *Intent:* % permute=randperm(datalength); % shuffle data order at each step bootstrap = round(datalength*rand(...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 21.8)
    * *Intent:* % %%%%%%%%%%%%%%%%%%% Perform sphering %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 13.3)
    * *Intent:* % %%%%%%%%%%%%%%%%%%%% Find mean variances %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % meanvar = zeros(ncomps...
  * `Anonymous_Block` **(Compute Cores)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 180 instances
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 597
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 191`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 237`, `dead_code: 20`, `fragile_debt: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/miscfunc/runicalowmem.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1576.4 | **LOC:** 1504 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.6981%), Tech Debt (8.9765%)
**Top Internal Functions/Classes:**
  * `runica` **(Many-Argument Workhorses)** (Impact: 311.9)
    * *Intent:* % 02-27-98 use PINV instead of INV to rank order comps if ncomps < chans -sm % 04-28-98 added 'posac...
  * `Anonymous_Block` **(Compute Cores)** (Impact: 44.5)
    * *Intent:* % a position dependent on the system clock %% Compute ICA Weights
  * `Anonymous_Block` **(Compute Cores)** (Impact: 43.0)
    * *Intent:* %% Compute ICA Weights
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 29.9)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %% Compute ICA Weights
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 29.8)
    * *Intent:* %% Compute ICA Weights
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 306 instances
* *Memory Alloc (weighted view):* 32
* *State Mutation (weighted view):* 1024
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 247`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 412`, `dead_code: 40`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 3`
* *Defense:* `safety: 33`, `doc: 5`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/studyfunc/toporeplot.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1540.92 | **LOC:** 849 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.5191%), Tech Debt (9.6653%)
**Top Internal Functions/Classes:**
  * `toporeplot` **(Many-Argument Workhorses)** (Impact: 1025.4)
    * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRI...
  * `__global_context__` **(I/O & Config Routines)** (Impact: 2.0)
    * *Intent:* % in a 2-D circular scalp map view (as looking down at the top % of the head). May also be used to r...
  * `Anonymous_Block` **(Defensive Guards)** (Impact: 1.2)
    * *Intent:* % %%%%%%%%%%%%% Set EEGLAB background color to match head border %%%%%%%%%%%%%%%%%%%%%%%% %
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 151 instances
* *Memory Alloc (weighted view):* 10
* *State Mutation (weighted view):* 500
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 97`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 198`, `dead_code: 7`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 32`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/adminfunc/eeg_checkset.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1416.02 | **LOC:** 1444 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.26%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `eeg_checkset` **(Many-Argument Workhorses)** (Impact: 300.4)
    * *Intent:* % THE POSSIBILITY OF SUCH DAMAGE. % 01-25-02 reformated help & license -ad % 01-26-02 chandeg events...
  * `__global_context__` **(I/O & Config Routines)** (Impact: 79.2)
    * *Intent:* % Also: See EEG dataset structure field descriptions below. % % Usage: >> [EEGOUT,changes] = eeg_che...
  * `Anonymous_Block` **(Defensive Guards)** (Impact: 51.8)
  * `Anonymous_Block` **(Defensive Guards)** (Impact: 29.2)
    * *Intent:* % reference (use EEG structure) % --------- if ~isfield(EEG, 'ref') EEG.ref = ''; end if isequal(EEG...
  * `popask` **(Defensive Guards)** (Impact: 18.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 222 instances
* *State Mutation (weighted view):* 708
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 438`, `structural_boundaries: 351`, `args: 7`, `func_start: 3`
* *Risk/State:* `state_mutation: 264`, `dead_code: 7`
* *Architecture:* `io: 2`, `api: 3`
* *Defense:* `safety: 234`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/popfunc/pop_chanedit.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1384.62 | **LOC:** 1170 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.1363%), Tech Debt (12.0962%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` **(Many-Argument Workhorses)** (Impact: 540.0)
  * `Anonymous_Block` **(Defensive Guards)** (Impact: 27.0)
    * *Intent:* % in case an EEG structure was given as input % ------------------------------------------- if isfie...
  * `pop_chanedit` **(Defensive Guards)** (Impact: 11.1)
    * *Intent:* % AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE % IMPLIED WARRANTIES OF ...
  * `add_locfiles` **(Many-Argument Workhorses)** (Impact: 10.0)
    * *Intent:* % adding channel location file % ----------------------------
  * `popask` **(Compute Cores)** (Impact: 9.2)
    * *Intent:* % ask for confirmation % --------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 222 instances
* *State Mutation (weighted view):* 731
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 214`, `args: 8`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 287`, `dead_code: 5`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 6`
* *Defense:* `safety: 122`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/coregister.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1257.7 | **LOC:** 941 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.5013%), Tech Debt (10.8789%)
**Top Internal Functions/Classes:**
  * `coregister` **(Many-Argument Workhorses)** (Impact: 257.4)
    * *Intent:* % LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR % CONSEQUENTIAL DAMAGES (INCLU...
  * `plotelec` **(Many-Argument Workhorses)** (Impact: 79.9)
    * *Intent:* % plot electrodes % ---------------
  * `plotlabels` **(Many-Argument Workhorses)** (Impact: 65.4)
    * *Intent:* % plot electrode labels % ---------------------
  * `align_fiducials` **(Many-Argument Workhorses)** (Impact: 58.2)
    * *Intent:* % align fiducials % --------------- % rename fiducials % ---------------- ind1 = strmatch(fidnames1{...
  * `decodelabels` **(Many-Argument Workhorses)** (Impact: 56.8)
    * *Intent:* % decode labels for electrode caps % -------------------------------- % 86 channels
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 151 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 583
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 80`, `args: 9`, `func_start: 9`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 281`, `dead_code: 4`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 9`
* *Defense:* `safety: 55`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/timefreqfunc/timef.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1178.48 | **LOC:** 1130 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.8105%), Tech Debt (13.4919%)
**Top Internal Functions/Classes:**
  * `timef` **(Many-Argument Workhorses)** (Impact: 422.5)
    * *Intent:* % 02-28-00 added NOTE on formula derivation below -sm % 03-16-00 added AXCOPY feature -sm & tpj % 04...
  * `Anonymous_Block` **(Compute Cores)** (Impact: 38.7)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 17.6)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 16.1)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 11.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 171 instances
* *State Mutation (weighted view):* 551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 177`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 209`, `dead_code: 3`, `fragile_debt: 3`
* *Architecture:* `api: 3`
* *Defense:* `safety: 103`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/envtopo.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1144.92 | **LOC:** 1284 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.5804%), Tech Debt (20.2556%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` **(Many-Argument Workhorses)** (Impact: 262.2)
  * `envtopo` **(Many-Argument Workhorses)** (Impact: 75.5)
    * *Intent:* % 01-21-00 added 'bold' option for colorfile arg -sm % 02-28-00 added fill_comp_env arg -sm % 03-16-...
  * `envelope` **(Compute Cores)** (Impact: 15.2)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 7.7)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 196 instances
* *State Mutation (weighted view):* 621
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 173`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 229`, `dead_code: 16`, `fragile_debt: 6`
* *Architecture:* `io: 5`, `api: 2`
* *Defense:* `safety: 31`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/headplot.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1125.3 | **LOC:** 896 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.1059%), Tech Debt (10.5001%)
**Top Internal Functions/Classes:**
  * `fastcalcgx` **(Many-Argument Workhorses)** (Impact: 162.6)
    * *Intent:* %%%%%%%%%%%%%%%%%%%
  * `plotelec` **(Many-Argument Workhorses)** (Impact: 127.5)
    * *Intent:* % %%%%%%%%%%%%%%% % plot electrodes % %%%%%%%%%%%%%%%
  * `headplot` **(Many-Argument Workhorses)** (Impact: 123.3)
    * *Intent:* % CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) % ARISING IN ANY WAY OUT O...
  * `distance` **(Compute Cores)** (Impact: 102.9)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % DISTANCE - function used in 'setup' %%%%%%%%%%%%%%%%%%%%%%...
  * `calcgx` **(Compute Cores)** (Impact: 83.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % CALCGX - function used in 'setup' %%%%%%%%%%%%%%%%%%%%%%%%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 129 instances
* *Memory Alloc (weighted view):* 12
* *State Mutation (weighted view):* 438
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 91`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 180`, `dead_code: 4`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 6`
* *Defense:* `safety: 40`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/spectopo.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1071.4 | **LOC:** 994 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.5662%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `spectopo` **(Many-Argument Workhorses)** (Impact: 239.4)
    * *Intent:* % CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) % ARISING IN ANY WAY OUT O...
  * `spectcomp` **(Many-Argument Workhorses)** (Impact: 92.1)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%% % function computing spectrum %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  * `closestplot` **(Many-Argument Workhorses)** (Impact: 73.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%% % function closest plot %%%%%%%%%%%%%%%%%%%%%%%
  * `Anonymous_Block` **(Compute Cores)** (Impact: 49.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % plot vertical lines through ch...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 166 instances
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 514
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 146`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 182`, `dead_code: 9`
* *Architecture:* `api: 4`
* *Defense:* `safety: 60`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/studyfunc/std_dipplot.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1058.64 | **LOC:** 839 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.5524%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `std_plotcompdip` **(Many-Argument Workhorses)** (Impact: 119.7)
    * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRI...
  * `std_centroid` **(Many-Argument Workhorses)** (Impact: 71.5)
    * *Intent:* % ----------------------- % load all dipoles and % compute dipole centroid % DEVELOPMENT: this funct...
  * `std_dipplot` **(Many-Argument Workhorses)** (Impact: 42.5)
    * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRI...
  * `computecentroid` **(Compute Cores)** (Impact: 31.6)
    * *Intent:* % -------------------------------- % new function to compute centroid % was programmed to debug the ...
  * `dipgroups` **(Many-Argument Workhorses)** (Impact: 29.5)
    * *Intent:* % first, extract the subject number for n = 1:length(comp_to_disp) subjectnum(n,1) = str2num(comp_to...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 171 instances
* *State Mutation (weighted view):* 621
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 155`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 279`, `dead_code: 7`
* *Architecture:* `io: 5`, `api: 6`
* *Defense:* `safety: 34`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/studyfunc/pop_clustedit.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 962.76 | **LOC:** 969 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.7542%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pop_clustedit` **(Compute Cores)** (Impact: 180.6)
    * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRI...
  * `__global_context__` **(I/O & Config Routines)** (Impact: 25.0)
    * *Intent:* % options for visualizing and manipulating an input STUDY structure. % Only component measures (e.g....
  * `Anonymous_Block` **(Compute Cores)** (Impact: 10.9)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 8.9)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 177 instances
* *State Mutation (weighted view):* 652
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 136`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 298`, `dead_code: 12`
* *Architecture:* `io: 1`, `api: 2`
* *Defense:* `safety: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/studyfunc/std_readdata.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 933.2 | **LOC:** 624 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.5921%), Tech Debt (12.6549%)
**Top Internal Functions/Classes:**
  * `std_readdata` **(Many-Argument Workhorses)** (Impact: 240.1)
    * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRI...
  * `reorganizedata` **(Defensive Guards)** (Impact: 69.4)
    * *Intent:* % reorganize data % ---------------
  * `reorganizedata2` **(Defensive Guards)** (Impact: 66.1)
    * *Intent:* % reorganize data 2 % -----------------
  * `processtf` **(Many-Argument Workhorses)** (Impact: 63.9)
    * *Intent:* % call newtimef (duplicate function in std_erspplot) % -------------- % compute ITC or ERSP if strcm...
  * `getfilename` **(Many-Argument Workhorses)** (Impact: 18.1)
    * *Intent:* % get file base name: filepath and sess are cell array (in case 2 files per subject) % -------------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 131 instances
* *State Mutation (weighted view):* 399
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 149`, `args: 18`, `func_start: 8`
* *Risk/State:* `state_mutation: 137`, `dead_code: 6`, `unreferenced_by_name: 2`
* *Architecture:* `api: 8`
* *Defense:* `safety: 59`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/studyfunc/std_limo.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 892.28 | **LOC:** 755 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.568%), Tech Debt (9.7372%)
**Top Internal Functions/Classes:**
  * `std_limo` **(Many-Argument Workhorses)** (Impact: 65.5)
    * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRI...
  * `Anonymous_Block` **(Compute Cores)** (Impact: 48.5)
  * `__global_context__` **(Compute Cores)** (Impact: 28.6)
    * *Intent:* % call limo_batch to create all 1st level LIMO_EEG analysis % % Usage: % [STUDY LIMO_files] = std_li...
  * `Anonymous_Block` **(Callbacks & Closures)** (Impact: 15.7)
    * *Intent:* % further split that list per regressor and group
  * `Anonymous_Block` **(Defensive Guards)** (Impact: 13.3)
    * *Intent:* % computing channel neighbour matrix % ---------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 169 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 550
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 119`, `args: 16`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 212`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 3`, `concurrency: 4`
* *Defense:* `safety: 37`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `functions/adminfunc/eeg_getversion.m` -> Churn: **100.0%** | Cog Load: 39.1741% | Debt: 62.2459%
- `functions/sigprocfunc/readeetraklocs.m` -> Churn: **93.94%** | Cog Load: 76.8525% | Debt: 62.2459%
- `functions/adminfunc/plugin_askinstall.m` -> Churn: **72.7%** | Cog Load: 80.8455% | Debt: 62.2459%
- `functions/adminfunc/eeglab_update.m` -> Churn: **66.41%** | Cog Load: 73.1716% | Debt: 0.0%
- `functions/timefreqfunc/tf_cycle_calc.m` -> Churn: **59.16%** | Cog Load: 79.5365% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `functions/sigprocfunc/runica.m` -> **Arnaud Delorme** (100.0% isolated ownership) | Magnitude: 1679.74
- `functions/popfunc/pop_select.m` -> **Arnaud Delorme** (100.0% isolated ownership) | Magnitude: 734.9
- `functions/popfunc/pop_epoch.m` -> **Arnaud Delorme** (100.0% isolated ownership) | Magnitude: 533.52
- `functions/studyfunc/pop_chanplot.m` -> **Arnaud Delorme** (100.0% isolated ownership) | Magnitude: 523.64
- `functions/popfunc/pop_topoplot.m` -> **Arnaud Delorme** (100.0% isolated ownership) | Magnitude: 495.82

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `functions/@eegobj/length.m` -> **Severity: 147.7** (Blast Radius: 1.477 * Doc Risk: 100.0%)
- `functions/@eegobj/subsasgn.m` -> **Severity: 147.7** (Blast Radius: 1.477 * Doc Risk: 100.0%)
- `functions/@eegobj/subsref.m` -> **Severity: 147.7** (Blast Radius: 1.477 * Doc Risk: 100.0%)
- `functions/@memmapdata/display.m` -> **Severity: 147.7** (Blast Radius: 1.477 * Doc Risk: 100.0%)
- `functions/@memmapdata/isnumeric.m` -> **Severity: 147.7** (Blast Radius: 1.477 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
