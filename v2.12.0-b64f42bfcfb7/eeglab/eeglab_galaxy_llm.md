# ARCHITECTURAL_BRIEF: eeglab
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/sccn/eeglab` |
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
- **Scope:** 688 analyzed artifact(s), 85453 LOC.
- **Load-bearing artifact:** `functions/@eegobj/isfield.m` -- 174 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Heaviest artifact:** `functions/supportfiles/channel_location_files/neuroscan/cap128.asc` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 825 |
| Analyzed Artifacts (Scanned) | 688 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 137 |
| Total LOC | 85453 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 83.4% |
| Dominant Lang | MATLAB |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4115 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1283 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.205 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 66 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MATLAB | 653 | 85269 | 94.9% |
| PLAINTEXT | 12 | 1 | 1.7% |
| XML | 7 | 0 | 1.0% |
| MARKDOWN | 6 | 0 | 0.9% |
| JSON | 3 | 39 | 0.4% |
| CSV | 3 | 45 | 0.4% |
| BATCH | 2 | 5 | 0.3% |
| SCALA | 1 | 78 | 0.1% |
| SHELL | 1 | 16 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 687 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Many-Argument Workhorses Files 43%, Large Core Modules (2) 25%, Data / Markup / Trivial 14%, Compute Cores Files 14%, Declarative / Non-Code 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 670 | 97.4% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 17 | 2.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 137*

**Composition by Extension & Reason:**
- `.sfp`: 45x Excluded (Unsupported Extension: '.sfp')
- `.ced`: 12x Excluded (Unsupported Extension: '.ced')
- `.locs`: 12x Excluded (Unsupported Extension: '.locs')
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Binary Format Detected)
- `.elp`: 7x Excluded (Unsupported Extension: '.elp')
- `.dat`: 4x Excluded (Unsupported Extension: '.dat'), 3x Excluded (Unsupported Extension: '.DAT')
- `.m`: 1x Excluded (Machine-Generated Source Code Signature: 17 LOC), 1x Excluded (Machine-Generated Source Code Signature: 31 LOC), 1x Excluded (Saturation: Line 83 exceeds 500 chars)
- `.xyz`: 3x Excluded (Unsupported Extension: '.xyz')
- `.loc`: 3x Excluded (Unsupported Extension: '.loc')
- `.map`: 3x Excluded (Binary Format Detected)
- `.mat`: 3x Excluded (Unsupported Extension: '.mat')
- `.fdt`: 3x Excluded (Unsupported Extension: '.fdt')
- `.set`: 3x Excluded (Unsupported Extension: '.set')
- `.txt`: 1x Excluded (Machine-Generated Source Code Signature: 17 LOC), 1x Excluded (Machine-Generated Source Code Signature: 25 LOC)
- `.col`: 2x Excluded (Unsupported Extension: '.col')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.4 | 60.8 | 72.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.8 | 64.8 | 72.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 24.6 | 24.9 | 37.8 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 31.4 | 2.6 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 9.0 | 3.3 | 3.2 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 81.9 | 0.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 87.6 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 92.1 | 2.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.5 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 91.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1420 | 313 | 5 | `functions/studyfunc/std_serialize.m` |
| cleanup | 439 | 160 | 2 | `functions/sigprocfunc/eegplot.m` |
| guards | 7324 | 481 | 29 | `functions/adminfunc/eeg_checkset.m` |
| danger | 1844 | 366 | 7 | `functions/sigprocfunc/runica.m` |
| concurrency | 21 | 13 | 0 | `functions/miscfunc/runicalowmem.m` |
| connectivity | 1090 | 627 | 3 | `functions/studyfunc/std_serialize.m` |
| io | 486 | 125 | 2 | `functions/studyfunc/std_limoresults.m` |
| crypto | 0 | 0 | 0 | - |
| ipc | 19 | 11 | 0 | `functions/sigprocfunc/coregister.m` |
| time | 75 | 35 | 0 | `functions/miscfunc/icademo.m` |
| serialization | 222 | 63 | 0 | `functions/studyfunc/std_limoresults.m` |
| regex | 16 | 7 | 0 | `functions/popfunc/pop_topochansel.m` |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 51 | 21 | 0 | `functions/studyfunc/std_lm_getvars.m` |
| debt | 3127 | 373 | 11 | `eeglab.m` |
| mutation | 54008 | 629 | 185 | `eeglab.m` |
| dead_code | 852 | 555 | 2 | `functions/studyfunc/std_createclust.m` |
| credential | 2 | 2 | 0 | `functions/adminfunc/eeg_checkset.m` |
| threat | 3 | 1 | 0 | `functions/sigprocfunc/headplot.m` |
| ml_ai | 1035 | 181 | 4 | `functions/timefreqfunc/newcrossf.m` |
| ui | 933 | 162 | 4 | `functions/sigprocfunc/eegplot.m` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.3333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `functions/studyfunc/std_limoresults.m` (Hits: 37)
- `functions/sigprocfunc/readegihdr.m` (Hits: 21)
- `functions/timefreqfunc/crossf.m` (Hits: 21)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **isfield.m** (`functions/@eegobj/isfield.m`) — 174 inbound connections
2. **finputcheck.m** (`functions/guifunc/finputcheck.m`) — 104 inbound connections
3. **vararg2str.m** (`functions/adminfunc/vararg2str.m`) — 79 inbound connections
4. **fastif.m** (`functions/sigprocfunc/fastif.m`) — 70 inbound connections
5. **inputgui.m** (`functions/guifunc/inputgui.m`) — 69 inbound connections

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
- `topoplot` **(Many-Argument Workhorses)** (@ `functions/sigprocfunc/topoplot.m`) -> Impact: **584.5** | LOC: 890
  * *Intent:* % 2-26-98 Revised by Colin % -changed image back to surface command % -added fill and blank styles % -removed extra background colormap entry (now use...
- `Anonymous_Block_[Truncated]` **(Many-Argument Workhorses)** (@ `functions/popfunc/pop_chanedit.m`) -> Impact: **540.0** | LOC: 880
- `pop_erpimage` **(Many-Argument Workhorses)** (@ `functions/popfunc/pop_erpimage.m`) -> Impact: **480.1** | LOC: 526
  * *Intent:* % SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS % INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN %...
- `binica` **(Many-Argument Workhorses)** (@ `functions/sigprocfunc/binica.m`) -> Impact: **467.3** | LOC: 372
  * *Intent:* % SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS % INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN %...
- `crossf` **(Many-Argument Workhorses)** (@ `functions/miscfunc/crossfold.m`) -> Impact: **438.7** | LOC: 330
  * *Intent:* % THE POSSIBILITY OF SUCH DAMAGE. % 11-20-98 defined LINEWIDTH constant -sm % 04-01-99 made number of frequencies consistent -se % 06-29-99 fixed cons...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `functions/studyfunc` | 133 | 32833.9 | 66.13% | 23.75% |
| `functions/popfunc` | 131 | 32700.66 | 71.52% | 19.7% |
| `functions/sigprocfunc` | 115 | 32069.78 | 64.82% | 27.89% |
| `functions/miscfunc` | 110 | 19406.1 | 62.81% | 29.08% |
| `functions/timefreqfunc` | 24 | 8709.64 | 64.12% | 25.93% |
| `functions/adminfunc` | 66 | 6581.28 | 46.92% | 22.36% |
| `functions/supportfiles/channel_location_files/neuroscan` | 2 | 5001.0 | 0.0% | 0.0% |
| `functions/statistics` | 16 | 2867.8 | 72.63% | 32.52% |
| `__monolith__` | 5 | 2086.84 | 14.94% | 2.0% |
| `functions/guifunc` | 10 | 1638.96 | 57.18% | 22.53% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `functions/adminfunc/eeglab_error.m` -> **99.9925%** Exposure
- `functions/sigprocfunc/textsc.m` -> **99.3307%** Exposure
- `functions/studyfunc/std_savedat.m` -> **99.3307%** Exposure
- `functions/sigprocfunc/movav.m` -> **97.2598%** Exposure
- `functions/statistics/anova1_cell.m` -> **96.9302%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `eeglab.m` -> **100.0%** Exposure
- `functions/@eegobj/subsasgn.m` -> **100.0%** Exposure
- `functions/@memmapdata/size.m` -> **100.0%** Exposure
- `functions/@memmapdata/subsref.m` -> **100.0%** Exposure
- `functions/@memmapdata/sum.m` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `functions/timefreqfunc/newcrossf.m` -> **5** Orphaned Functions | **0** Duplicates
- `functions/sigprocfunc/coregister.m` -> **4** Orphaned Functions | **0** Duplicates
- `functions/studyfunc/pop_addindepvar.m` -> **4** Orphaned Functions | **0** Duplicates
- `functions/studyfunc/std_readeegfield.m` -> **4** Orphaned Functions | **0** Duplicates
- `functions/miscfunc/corrimage.m` -> **3** Orphaned Functions | **0** Duplicates

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

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `functions/supportfiles/channel_location_files/neuroscan/cap128.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.762
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/timefreqfunc/crossf.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 22.156)
- **Top Global Matches:** file_cluster_1: 22.156, file_cluster_3: 27.027, file_cluster_8: 48.637
- **Magnitude:** 2450.06 | **LOC:** 1458 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.8%), Guard Balance (formerly Safety Score) (77.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `crossf` **(Many-Argument Workhorses)** (Impact: 421.7)
    * *Intent:* % Note: 3 "objects" (Tf, Coher and Boot) are handled by specific functions under Matlab % (Tf) funct...
  * `tfitc` **(Many-Argument Workhorses)** (Impact: 159.4)
    * *Intent:* % function for itc % ----------------
  * `tfcomp` **(Many-Argument Workhorses)** (Impact: 139.0)
    * *Intent:* % function for time freq decomposition % ------------------------------------ % tf is an structure c...
  * `tfitcpost` **(Many-Argument Workhorses)** (Impact: 132.4)
  * `cohercomp` **(Many-Argument Workhorses)** (Impact: 127.3)
    * *Intent:* % function for coherence calculation % ------------------------------------- % function Coher = cohe...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 235 instances
* *Memory Alloc (weighted view):* 22
* *State Mutation (weighted view):* 769
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 197`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 299`, `dead_code: 12`, `unreferenced_by_name: 1`
* *Architecture:* `io: 21`, `api: 14`
* *Defense:* `safety: 97`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.762
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `eeglab.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.02)
- **Top Global Matches:** file_cluster_8: 11.02, file_cluster_3: 15.737, file_cluster_6: 22.582
- **Magnitude:** 2062.08 | **LOC:** 2293 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.925; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (74.7%), Guard Balance (formerly Safety Score) (74.4%), Debt Markers (formerly Tech Debt) (10.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `eeg_mainfig` **(Defensive Guards)** (Impact: 81.5)
    * *Intent:* % REMOVED MENUS %eegmenu( false, tools_m, 'Label', 'Automatic comp. reject', 'enable', 'off', 'CallB...
  * `popask` **(Defensive Guards)** (Impact: 55.9)
  * `myguihandles` **(Defensive Guards)** (Impact: 51.3)
  * `rmpathifpresent` **(Defensive Guards)** (Impact: 45.6)
  * `updatemenu` **(Defensive Guards)** (Impact: 35.4)
    * *Intent:* % Update EEGLAB GUI (list of datasets) % -----------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 315 instances
* *State Mutation (weighted view):* 1141
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 442`, `structural_boundaries: 348`, `args: 26`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 2`, `state_mutation: 511`, `dead_code: 4`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 7`, `api: 13`
* *Defense:* `safety: 171`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.000155 | `Ripple Effect (Closeness):` 0.001456
  * `Imports (Out-Degree: 22):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `functions/sigprocfunc/topoplot.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.272)
- **Top Global Matches:** file_cluster_8: 7.272, file_cluster_6: 17.46, file_cluster_3: 20.22
- **Magnitude:** 1958.1 | **LOC:** 1804 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); blast radius 3.923; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.5%), Complexity Load (formerly Cognitive Load) (80.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `topoplot` **(Many-Argument Workhorses)** (Impact: 584.5)
    * *Intent:* % 2-26-98 Revised by Colin % -changed image back to surface command % -added fill and blank styles %...
  * `disk` **(Many-Argument Workhorses)** (Impact: 8.8)
    * *Intent:* % %%%%%%%%%%%%% Draw circle %%%%%%%%%%%%%%%%%%%%%%%% %
  * `gdatav4` **(Many-Argument Workhorses)** (Impact: 3.3)
    * *Intent:* % % X(2:size(X,1)-1,2:size(X,2)-1) = NaN; % X(isnan(X(:))) = []; % X(1:2:end) = []; % X(1:2:end) = [...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 328 instances
* *Memory Alloc (weighted view):* 32
* *State Mutation (weighted view):* 1116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 429`, `structural_boundaries: 243`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 460`, `dead_code: 8`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`
* *Defense:* `safety: 79`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.923
  * `Choke Point (Betweenness):` 0.003142 | `Ripple Effect (Closeness):` 0.047209
  * `Imports (Out-Degree: 6):` None
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `functions/timefreqfunc/newcrossf.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.629)
- **Top Global Matches:** file_cluster_8: 11.629, file_cluster_3: 13.779, file_cluster_6: 23.861
- **Magnitude:** 1779.84 | **LOC:** 1468 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `newcrossf` **(Many-Argument Workhorses)** (Impact: 120.6)
    * *Intent:* % There are 3 "objects" Tf, Coher and Boot which are handled % - by specific functions under Matlab ...
  * `ampcorr` **(Many-Argument Workhorses)** (Impact: 87.7)
    * *Intent:* % *********************************************************************** % ------------------------...
  * `plotall` **(Many-Argument Workhorses)** (Impact: 67.6)
    * *Intent:* % ------------------ % plotting functions % ------------------
  * `coherinit` **(Many-Argument Workhorses)** (Impact: 44.4)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% COHERENCE OBSOLETE %%%%%%%%%%%%%%%%%%%%%%%%% %%%%%%%%%%%%%%%%%%%%%%...
  * `cohercomp` **(Many-Argument Workhorses)** (Impact: 39.6)
    * *Intent:* % function for coherence calculation % ------------------------------------- %function Coher = coher...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 207 instances
* *State Mutation (weighted view):* 638
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 353`, `structural_boundaries: 233`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 224`, `dead_code: 5`, `unreferenced_by_name: 5`
* *Architecture:* `api: 10`
* *Defense:* `safety: 129`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.762
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/runica_ml2.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.356)
- **Top Global Matches:** file_cluster_1: 6.356, file_cluster_3: 48.321, file_cluster_8: 70.128
- **Magnitude:** 1699.14 | **LOC:** 1113 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runica` **(Many-Argument Workhorses)** (Impact: 881.3)
    * *Intent:* % 02-27-98 use PINV instead of INV to rank order comps if ncomps < chans -sm % 04-28-98 added 'posac...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 204 instances
* *Memory Alloc (weighted view):* 21
* *State Mutation (weighted view):* 668
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 198`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 260`, `fragile_debt: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.762
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/runica_ml.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.357)
- **Top Global Matches:** file_cluster_1: 6.357, file_cluster_3: 48.322, file_cluster_8: 70.128
- **Magnitude:** 1695.1 | **LOC:** 1113 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runica` **(Many-Argument Workhorses)** (Impact: 881.3)
    * *Intent:* % 02-27-98 use PINV instead of INV to rank order comps if ncomps < chans -sm % 04-28-98 added 'posac...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 202 instances
* *Memory Alloc (weighted view):* 21
* *State Mutation (weighted view):* 662
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 198`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 258`, `fragile_debt: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.762
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/runica.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.898)
- **Top Global Matches:** file_cluster_3: 6.898, file_cluster_8: 20.657, file_cluster_6: 33.504
- **Magnitude:** 1679.74 | **LOC:** 1582 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.8%), Complexity Load (formerly Cognitive Load) (73.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runica` **(Many-Argument Workhorses)** (Impact: 343.8)
    * *Intent:* % 02-27-98 use PINV instead of INV to rank order comps if ncomps < chans -sm % 04-28-98 added 'posac...
  * `icaprintf` **(Defensive Guards)** (Impact: 6.3)
    * *Intent:* % printing functions % ------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 322 instances
* *State Mutation (weighted view):* 1081
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 349`, `structural_boundaries: 226`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 437`, `dead_code: 5`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 2`
* *Defense:* `safety: 42`, `doc: 5`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.762
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/runica_mlb.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.325)
- **Top Global Matches:** file_cluster_1: 6.325, file_cluster_3: 48.317, file_cluster_8: 70.125
- **Magnitude:** 1673.06 | **LOC:** 1098 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runica` **(Many-Argument Workhorses)** (Impact: 881.3)
    * *Intent:* % 02-27-98 use PINV instead of INV to rank order comps if ncomps < chans -sm % 04-28-98 added 'posac...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 198 instances
* *Memory Alloc (weighted view):* 17
* *State Mutation (weighted view):* 651
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 192`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 255`, `fragile_debt: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.762
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/sigprocfunc/eegplot.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.171)
- **Top Global Matches:** file_cluster_8: 7.171, file_cluster_6: 17.578, file_cluster_3: 19.942
- **Magnitude:** 1671.02 | **LOC:** 2222 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); blast radius 3.254; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (72.8%), Guard Balance (formerly Safety Score) (72.4%), Debt Markers (formerly Tech Debt) (8.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `eegplot` **(Defensive Guards)** (Impact: 28.8)
    * *Intent:* % 1 - winlength % 2 - srate % 3 - children % 'backeeg' axis % 1 - trialtag % 2 - g.winrej % 3 - nest...
  * `defmotion` **(Compute Cores)** (Impact: 26.4)
    * *Intent:* % Function to show the value and electrode at mouse position
  * `myhistc` **(Compute Cores)** (Impact: 4.2)
    * *Intent:* % function not supported under Mac % --------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 333 instances
* *State Mutation (weighted view):* 1118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 381`, `structural_boundaries: 388`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 452`, `dead_code: 4`, `fragile_debt: 1`
* *Architecture:* `api: 3`
* *Defense:* `safety: 185`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.254
  * `Choke Point (Betweenness):` 0.001291 | `Ripple Effect (Closeness):` 0.02329
  * `Imports (Out-Degree: 13):` None
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `functions/sigprocfunc/eegplotlegacy.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.156)
- **Top Global Matches:** file_cluster_8: 7.156, file_cluster_6: 17.562, file_cluster_3: 19.945
- **Magnitude:** 1634.94 | **LOC:** 2187 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.976; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (72.4%), Complexity Load (formerly Cognitive Load) (72.3%), Debt Markers (formerly Tech Debt) (8.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `defmotion` **(Compute Cores)** (Impact: 24.9)
    * *Intent:* % Function to show the value and electrode at mouse position
  * `eegplotlegacy` **(Defensive Guards)** (Impact: 18.9)
    * *Intent:* % 1 - winlength % 2 - srate % 3 - children % 'backeeg' axis % 1 - trialtag % 2 - g.winrej % 3 - nest...
  * `myhistc` **(Compute Cores)** (Impact: 4.2)
    * *Intent:* % function not supported under Mac % --------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 324 instances
* *State Mutation (weighted view):* 1097
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 372`, `structural_boundaries: 375`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 449`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 3`
* *Defense:* `safety: 178`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.976
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012748
  * `Imports (Out-Degree: 11):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `functions/miscfunc/runicatest.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.298)
- **Top Global Matches:** file_cluster_1: 6.298, file_cluster_3: 48.311, file_cluster_8: 70.12
- **Magnitude:** 1599.66 | **LOC:** 1062 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runica` **(Many-Argument Workhorses)** (Impact: 864.0)
    * *Intent:* % 02-27-98 use PINV instead of INV to rank order comps if ncomps < chans -sm % 04-28-98 added 'posac...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 180 instances
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 597
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 191`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 237`, `fragile_debt: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.762
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/miscfunc/runicalowmem.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.639)
- **Top Global Matches:** file_cluster_8: 7.639, file_cluster_6: 17.607, file_cluster_3: 20.372
- **Magnitude:** 1583.2 | **LOC:** 1504 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runica` **(Many-Argument Workhorses)** (Impact: 311.9)
    * *Intent:* % 02-27-98 use PINV instead of INV to rank order comps if ncomps < chans -sm % 04-28-98 added 'posac...
  * `icaprintf` **(Defensive Guards)** (Impact: 11.3)
    * *Intent:* % printing functions % ------------------
  * `mycov` **(Defensive Guards)** (Impact: 4.9)
    * *Intent:* % this function compute covariance % without using much memory (no need to transpose a) % ----------...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 308 instances
* *Memory Alloc (weighted view):* 32
* *State Mutation (weighted view):* 1028
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 247`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 412`, `dead_code: 5`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 3`
* *Defense:* `safety: 33`, `doc: 5`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.762
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/studyfunc/toporeplot.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.309)
- **Top Global Matches:** file_cluster_1: 6.309, file_cluster_3: 48.323, file_cluster_8: 70.129
- **Magnitude:** 1540.92 | **LOC:** 849 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.892; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.9%), Complexity Load (formerly Cognitive Load) (81.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `toporeplot` **(Many-Argument Workhorses)** (Impact: 1025.4)
    * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRI...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 151 instances
* *Memory Alloc (weighted view):* 10
* *State Mutation (weighted view):* 500
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 97`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 198`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 32`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.892
  * `Choke Point (Betweenness):` 0.000106 | `Ripple Effect (Closeness):` 0.001456
  * `Imports (Out-Degree: 4):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `functions/popfunc/pop_chanedit.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.398)
- **Top Global Matches:** file_cluster_8: 7.398, file_cluster_6: 17.665, file_cluster_3: 20.044
- **Magnitude:** 1439.12 | **LOC:** 1170 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.803; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` **(Many-Argument Workhorses)** (Impact: 540.0)
  * `add_locfiles` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* % adding channel location file % ----------------------------
  * `popask` **(Defensive Guards)** (Impact: 27.6)
    * *Intent:* % ask for confirmation % --------------------
  * `update_datafield` **(Defensive Guards)** (Impact: 22.9)
    * *Intent:* % for multiple dataset processing % -------------------------------
  * `pop_chanedit` **(Defensive Guards)** (Impact: 11.1)
    * *Intent:* % AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE % IMPLIED WARRANTIES OF ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 223 instances
* *State Mutation (weighted view):* 733
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 214`, `args: 8`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 287`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 6`
* *Defense:* `safety: 122`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.803
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.001456
  * `Imports (Out-Degree: 8):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `functions/adminfunc/eeg_checkset.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.97)
- **Top Global Matches:** file_cluster_8: 8.97, file_cluster_6: 18.704, file_cluster_3: 20.302
- **Magnitude:** 1424.02 | **LOC:** 1444 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **49** in-repo importer(s); blast radius 8.572; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.3%), Guard Balance (formerly Safety Score) (61.3%), Dead Code Surface (formerly Dead Code) (6.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `eeg_checkset` **(Many-Argument Workhorses)** (Impact: 300.4)
    * *Intent:* % THE POSSIBILITY OF SUCH DAMAGE. % 01-25-02 reformated help & license -ad % 01-26-02 chandeg events...
  * `mycellfun` **(Defensive Guards)** (Impact: 18.8)
  * `popask` **(Defensive Guards)** (Impact: 18.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 222 instances
* *State Mutation (weighted view):* 708
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 438`, `structural_boundaries: 351`, `args: 7`, `func_start: 3`
* *Risk/State:* `state_mutation: 264`, `dead_code: 4`
* *Architecture:* `io: 2`, `api: 3`
* *Defense:* `safety: 234`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.572
  * `Choke Point (Betweenness):` 0.00839 | `Ripple Effect (Closeness):` 0.091956
  * `Imports (Out-Degree: 19):` None
  * `Imported By (In-Degree: 49):` (Excluded from Brief to save tokens)

### `functions/sigprocfunc/coregister.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 20.504)
- **Top Global Matches:** file_cluster_1: 20.504, file_cluster_3: 28.366, file_cluster_8: 50.066
- **Magnitude:** 1369.6 | **LOC:** 941 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `coregister` **(Many-Argument Workhorses)** (Impact: 257.4)
    * *Intent:* % LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR % CONSEQUENTIAL DAMAGES (INCLU...
  * `plotelec` **(Many-Argument Workhorses)** (Impact: 102.2)
    * *Intent:* % plot electrodes % ---------------
  * `plotlabels` **(Many-Argument Workhorses)** (Impact: 81.1)
    * *Intent:* % plot electrode labels % ---------------------
  * `align_fiducials` **(Many-Argument Workhorses)** (Impact: 78.3)
    * *Intent:* % align fiducials % --------------- % rename fiducials % ---------------- ind1 = strmatch(fidnames1{...
  * `decodelabels` **(Many-Argument Workhorses)** (Impact: 77.6)
    * *Intent:* % decode labels for electrode caps % -------------------------------- % 86 channels
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 146 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 573
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 80`, `args: 9`, `func_start: 9`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 281`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 2`, `api: 9`
* *Defense:* `safety: 55`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.762
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/timefreqfunc/timef.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.633)
- **Top Global Matches:** file_cluster_8: 7.633, file_cluster_6: 17.565, file_cluster_3: 20.397
- **Magnitude:** 1178.48 | **LOC:** 1130 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.475; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `timef` **(Many-Argument Workhorses)** (Impact: 422.5)
    * *Intent:* % 02-28-00 added NOTE on formula derivation below -sm % 03-16-00 added AXCOPY feature -sm & tpj % 04...
  * `hanning` **(Compute Cores)** (Impact: 4.6)
    * *Intent:* % symmetric Hanning tapering function % -----------------------------------
  * `myprintf` **(Parameter Forwarders)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 171 instances
* *State Mutation (weighted view):* 551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 177`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 209`, `fragile_debt: 3`
* *Architecture:* `api: 3`
* *Defense:* `safety: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.475
  * `Choke Point (Betweenness):` 0.000172 | `Ripple Effect (Closeness):` 0.003684
  * `Imports (Out-Degree: 8):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `functions/sigprocfunc/envtopo.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 15.977)
- **Top Global Matches:** file_cluster_3: 15.977, file_cluster_1: 33.59, file_cluster_8: 37.138
- **Magnitude:** 1141.42 | **LOC:** 1284 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 1.121; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.0%), Complexity Load (formerly Cognitive Load) (77.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` **(Many-Argument Workhorses)** (Impact: 262.2)
  * `envtopo` **(Many-Argument Workhorses)** (Impact: 75.5)
    * *Intent:* % 01-21-00 added 'bold' option for colorfile arg -sm % 02-28-00 added fill_comp_env arg -sm % 03-16-...
  * `envelope` **(Compute Cores)** (Impact: 11.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 196 instances
* *State Mutation (weighted view):* 621
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 173`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 229`, `dead_code: 3`, `fragile_debt: 6`
* *Architecture:* `io: 5`, `api: 2`
* *Defense:* `safety: 31`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.121
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.002911
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `functions/sigprocfunc/headplot.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.058)
- **Top Global Matches:** file_cluster_1: 6.058, file_cluster_3: 48.271, file_cluster_8: 70.082
- **Magnitude:** 1101.4 | **LOC:** 896 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); blast radius 2.339; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.9%), Complexity Load (formerly Cognitive Load) (73.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fastcalcgx` **(Many-Argument Workhorses)** (Impact: 144.0)
    * *Intent:* %%%%%%%%%%%%%%%%%%%
  * `headplot` **(Many-Argument Workhorses)** (Impact: 123.3)
    * *Intent:* % CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) % ARISING IN ANY WAY OUT O...
  * `plotelec` **(Many-Argument Workhorses)** (Impact: 109.7)
    * *Intent:* % %%%%%%%%%%%%%%% % plot electrodes % %%%%%%%%%%%%%%%
  * `distance` **(Defensive Guards)** (Impact: 89.0)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % DISTANCE - function used in 'setup' %%%%%%%%%%%%%%%%%%%%%%...
  * `calcgx` **(Defensive Guards)** (Impact: 83.2)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % CALCGX - function used in 'setup' %%%%%%%%%%%%%%%%%%%%%%%%...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 133 instances
* *Memory Alloc (weighted view):* 14
* *State Mutation (weighted view):* 446
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 91`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 180`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 6`
* *Defense:* `safety: 40`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.339
  * `Choke Point (Betweenness):` 0.000229 | `Ripple Effect (Closeness):` 0.009825
  * `Imports (Out-Degree: 8):` None
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `functions/sigprocfunc/spectopo.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.599)
- **Top Global Matches:** file_cluster_3: 9.599, file_cluster_8: 30.14, file_cluster_1: 40.361
- **Magnitude:** 1074.1 | **LOC:** 994 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.893; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.6%), Guard Balance (formerly Safety Score) (76.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `spectopo` **(Many-Argument Workhorses)** (Impact: 239.4)
    * *Intent:* % CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) % ARISING IN ANY WAY OUT O...
  * `spectcomp` **(Many-Argument Workhorses)** (Impact: 94.8)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%%%%%%%% % function computing spectrum %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  * `closestplot` **(Many-Argument Workhorses)** (Impact: 73.5)
    * *Intent:* %%%%%%%%%%%%%%%%%%%%%%% % function closest plot %%%%%%%%%%%%%%%%%%%%%%%
  * `myfprintf` **(Parameter Forwarders)** (Impact: 3.7)
  * `plotcolbar` **(Defensive Guards)** (Impact: 3.5)
    * *Intent:* %%%%%%%%%%%%%%%% % Plot color bar %%%%%%%%%%%%%%%%
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 166 instances
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 514
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 146`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 182`, `dead_code: 3`
* *Architecture:* `api: 4`
* *Defense:* `safety: 60`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.893
  * `Choke Point (Betweenness):` 0.000199 | `Ripple Effect (Closeness):` 0.004755
  * `Imports (Out-Degree: 10):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `functions/studyfunc/std_dipplot.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 15.467)
- **Top Global Matches:** file_cluster_3: 15.467, file_cluster_1: 33.562, file_cluster_8: 36.824
- **Magnitude:** 1064.04 | **LOC:** 839 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `std_plotcompdip` **(Many-Argument Workhorses)** (Impact: 119.7)
    * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRI...
  * `std_centroid` **(Many-Argument Workhorses)** (Impact: 75.9)
    * *Intent:* % ----------------------- % load all dipoles and % compute dipole centroid % DEVELOPMENT: this funct...
  * `std_dipplot` **(Many-Argument Workhorses)** (Impact: 42.5)
    * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRI...
  * `computecentroid` **(Compute Cores)** (Impact: 33.0)
    * *Intent:* % -------------------------------- % new function to compute centroid % was programmed to debug the ...
  * `dipgroups` **(Many-Argument Workhorses)** (Impact: 26.9)
    * *Intent:* % first, extract the subject number for n = 1:length(comp_to_disp) subjectnum(n,1) = str2num(comp_to...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 173 instances
* *State Mutation (weighted view):* 625
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 155`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 279`, `dead_code: 4`
* *Architecture:* `io: 5`, `api: 6`
* *Defense:* `safety: 34`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.762
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/studyfunc/std_readdata.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.358)
- **Top Global Matches:** file_cluster_3: 7.358, file_cluster_8: 21.196, file_cluster_6: 34.007
- **Magnitude:** 967.0 | **LOC:** 624 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); blast radius 3.715; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `std_readdata` **(Many-Argument Workhorses)** (Impact: 240.1)
    * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRI...
  * `processtf` **(Many-Argument Workhorses)** (Impact: 88.4)
    * *Intent:* % call newtimef (duplicate function in std_erspplot) % -------------- % compute ITC or ERSP if strcm...
  * `reorganizedata` **(Defensive Guards)** (Impact: 69.4)
    * *Intent:* % reorganize data % ---------------
  * `reorganizedata2` **(Defensive Guards)** (Impact: 66.1)
    * *Intent:* % reorganize data 2 % -----------------
  * `processerpim` **(Defensive Guards)** (Impact: 18.7)
    * *Intent:* % call erpimage % -------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 133 instances
* *State Mutation (weighted view):* 403
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 149`, `args: 18`, `func_start: 8`
* *Risk/State:* `state_mutation: 137`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 8`
* *Defense:* `safety: 59`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.715
  * `Choke Point (Betweenness):` 0.000792 | `Ripple Effect (Closeness):` 0.014202
  * `Imports (Out-Degree: 17):` None
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `functions/studyfunc/pop_clustedit.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.4)
- **Top Global Matches:** file_cluster_3: 6.4, file_cluster_8: 20.395, file_cluster_6: 33.276
- **Magnitude:** 962.76 | **LOC:** 969 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pop_clustedit` **(Many-Argument Workhorses)** (Impact: 180.6)
    * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRI...
  * `renameclust` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 177 instances
* *State Mutation (weighted view):* 652
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 136`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 298`, `dead_code: 3`
* *Architecture:* `io: 1`, `api: 2`
* *Defense:* `safety: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.762
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `functions/studyfunc/std_limo.m` (MATLAB | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.881)
- **Top Global Matches:** file_cluster_8: 6.881, file_cluster_6: 17.497, file_cluster_3: 19.831
- **Magnitude:** 892.28 | **LOC:** 755 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.871; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.6%), Guard Balance (formerly Safety Score) (84.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `std_limo` **(Many-Argument Workhorses)** (Impact: 65.5)
    * *Intent:* % and/or other materials provided with the distribution. % % THIS SOFTWARE IS PROVIDED BY THE COPYRI...
  * `rel2fullpath` **(Defensive Guards)** (Impact: 12.8)
    * *Intent:* % ------------------------------------------------------------------------- % Return full path if 'f...
  * `getfilename` **(Compute Cores)** (Impact: 7.6)
    * *Intent:* % get file base name (from std_precomp) % ------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 169 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 550
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 119`, `args: 16`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 212`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 3`, `concurrency: 4`
* *Defense:* `safety: 37`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.871
  * `Choke Point (Betweenness):` 5e-05 | `Ripple Effect (Closeness):` 0.001456
  * `Imports (Out-Degree: 17):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `functions/@memmapdata/memmapdata.m` (MATLAB) | Magnitude: 40.26 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, branch: 8, structural_boundaries: 8, state_mutation: 7
- `functions/@eegobj/length.m` (MATLAB) | Magnitude: 16.7 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9, core_var_decl: 5, design_snake_case: 5, state_mutation: 4
- `functions/studyfunc/compute_ersp_times.m` (MATLAB) | Magnitude: 38.5 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9, state_mutation: 8, core_var_decl: 6, design_snake_case: 6
- `functions/popfunc/eeg_timeinterp.m` (MATLAB) | Magnitude: 47.24 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 14, core_var_decl: 10, branch: 9
- `functions/sigprocfunc/compvar.m` (MATLAB) | Magnitude: 42.02 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 11, design_snake_case: 11, state_mutation: 10, indent_spaces: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `functions/miscfunc/averef.m` (MATLAB) | Magnitude: 49.2 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 12, core_var_decl: 12, design_snake_case: 9, indent_tabs: 7
- `functions/@mmo/double.m` (MATLAB) | Magnitude: 2.64 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `functions/miscfunc/zica.m` (MATLAB) | Magnitude: 85.42 | Delta: **0.141** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 18, core_var_decl: 18, design_snake_case: 18, indent_spaces: 17

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `functions/sigprocfunc/readeetraklocs.m` -> Churn: **100.0%** | Cog Load: 76.8525% | Debt: 37.7541%
- `functions/timefreqfunc/tf_cycle_calc.m` -> Churn: **62.98%** | Cog Load: 79.5365% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `functions/sigprocfunc/runica.m` -> **Arnaud Delorme** (100.0% isolated ownership) | Magnitude: 1679.74
- `functions/popfunc/pop_select.m` -> **Arnaud Delorme** (100.0% isolated ownership) | Magnitude: 734.9
- `functions/studyfunc/pop_chanplot.m` -> **Arnaud Delorme** (100.0% isolated ownership) | Magnitude: 523.64
- `functions/popfunc/pop_loadset.m` -> **Arnaud Delorme** (100.0% isolated ownership) | Magnitude: 445.36
- `functions/adminfunc/plugin_askinstall.m` -> **Arnaud Delorme** (100.0% isolated ownership) | Magnitude: 75.86

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `functions/adminfunc/eeg_checkset.m` -> **Severity: 0.839** (Bridge: 0.0084 * Flux: 100.0%)
- `functions/adminfunc/eeg_getdatact.m` -> **Severity: 0.502** (Bridge: 0.005 * Flux: 100.0%)
- `functions/miscfunc/corrimage.m` -> **Severity: 0.376** (Bridge: 0.0038 * Flux: 100.0%)
- `functions/sigprocfunc/readlocs.m` -> **Severity: 0.331** (Bridge: 0.0033 * Flux: 100.0%)
- `functions/sigprocfunc/topoplot.m` -> **Severity: 0.314** (Bridge: 0.0031 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `functions/guifunc/finputcheck.m` -> **Severity: 14.522** (Embedded: 0.2212 * Error Risk: 65.6639%)
- `functions/adminfunc/unique_bc.m` -> **Severity: 10.808** (Embedded: 0.1765 * Error Risk: 61.2336%)
- `functions/adminfunc/vararg2str.m` -> **Severity: 10.206** (Embedded: 0.1259 * Error Risk: 81.0697%)
- `functions/guifunc/supergui.m` -> **Severity: 8.435** (Embedded: 0.1063 * Error Risk: 79.3845%)
- `functions/guifunc/questdlg2.m` -> **Severity: 7.583** (Embedded: 0.1045 * Error Risk: 72.5404%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `functions/@eegobj/isfield.m` -> **Severity: 6139.3** (Blast Radius: 61.393 * Doc Risk: 100.0%)
- `functions/@eegobj/isstruct.m` -> **Severity: 2737.3** (Blast Radius: 27.373 * Doc Risk: 100.0%)
- `functions/@eegobj/fieldnames.m` -> **Severity: 2319.6** (Blast Radius: 23.196 * Doc Risk: 100.0%)
- `functions/guifunc/finputcheck.m` -> **Severity: 2241.721** (Blast Radius: 41.284 * Doc Risk: 54.3%)
- `functions/adminfunc/unique_bc.m` -> **Severity: 1631.7** (Blast Radius: 16.317 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 3047 literal sites + 3 sites through wrappers = 3050
- **`panics_and_aborts`:** 1321 literal sites + 3 sites through wrappers = 1324

- `mywhich` (function, debug_prints, primitive): 3 call sites in 1 files -- `functions/adminfunc/eeglab_update.m`
- `mywhich` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `functions/adminfunc/eeglab_update.m`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 24931 call pairs -- scoped 2.7%, unique 9.7%, ambiguous 10.8%, external 76.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| matlab | 24929 | 2.7% | 9.7% | 10.8% | 76.7% |
| shell | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
