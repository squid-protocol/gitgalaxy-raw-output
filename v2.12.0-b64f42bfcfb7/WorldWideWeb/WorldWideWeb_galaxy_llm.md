# ARCHITECTURAL_BRIEF: WorldWideWeb
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/simonw/1991-WWW-NeXT-Implementation.git` |
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
- **Scope:** 38 analyzed artifact(s), 6114 LOC.
- **Load-bearing artifact:** `Anchor.h` -- 7 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `NewsAccess.m` -- pulls in 18 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `HyperText.m` at magnitude 1274.78 (structural weight, not risk).
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
| Total Artifacts | 63 |
| Analyzed Artifacts (Scanned) | 38 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 25 |
| Total LOC | 6114 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 60.3% |
| Dominant Lang | OBJECTIVE-C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3711 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2232 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4516 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| OBJECTIVE-C | 20 | 4462 | 52.6% |
| HTML | 11 | 1063 | 28.9% |
| C | 3 | 550 | 7.9% |
| MAKEFILE | 2 | 39 | 5.3% |
| MARKDOWN | 1 | 0 | 2.6% |
| PLAINTEXT | 1 | 0 | 2.6% |

## 4.1 SOURCE ENCODINGS
All 38 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 34%, Large Core Modules (3) 18%, State Mutators Files 13%, Parameter Forwarders Files 11%, Declarative / Non-Code 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 36 | 94.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 5.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 25*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (Binary Format Detected), 1x Excluded (Unsupported Extension: '.dependencies'), 1x Unsupported Format (.undeterminable)
- `.style`: 6x Excluded (Unsupported Extension: '.style')
- `.h`: 2x Excluded (Machine-Generated Source Code Signature: 12 LOC), 1x Excluded (Machine-Generated Source Code Signature: 20 LOC), 1x Excluded (Machine-Generated Source Code Signature: 31 LOC)
- `.tiff`: 3x Excluded (Explicitly Denied Extension: '.tiff')
- `.iconheader`: 2x Excluded (Unsupported Extension: '.iconheader')
- `.proj`: 1x Excluded (Unsupported Extension: '.proj')
- `.debug`: 1x Excluded (Unsupported Extension: '.debug')
- `.nib`: 1x Excluded (Unsupported Extension: '.nib')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 91.6 | 24.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 84.1 | 36.5 | 54.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 38.3 | 4.2 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 23.7 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 17.9 | 2.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 37.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.0 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 52.7 | 84.0 | 84.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 348 | 18 | 28 | `HyperText.m` |
| cleanup | 60 | 13 | 6 | `FileAccess.m` |
| guards | 67 | 15 | 4 | `NewsAccess.m` |
| danger | 54 | 16 | 3 | `HText.c` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 244 | 22 | 15 | `HText.c` |
| io | 212 | 25 | 18 | `SourceFiles.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 1 | 1 | 0 | `WorldWideWeb_main.m` |
| tests | 0 | 0 | 0 | - |
| docs | 13 | 12 | 1 | `FileAccess.m` |
| debt | 244 | 19 | 19 | `HyperText.m` |
| mutation | 1655 | 28 | 120 | `HyperText.m` |
| dead_code | 149 | 15 | 13 | `HyperText.m` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 23 | 2 | 0 | `HyperText.m` |
| ui | 96 | 16 | 10 | `HyperText.m` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `SourceFiles.html` (Hits: 21)
- `WorldWideWeb.app/default.html` (Hits: 19)
- `default.html` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Anchor.h** (`Anchor.h`) — 7 inbound connections
2. **HTStyle.h** (`HTStyle.h`) — 7 inbound connections
3. **HyperText.h** (`HyperText.h`) — 7 inbound connections
4. **HTStyle.m** (`HTStyle.m`) — 4 inbound connections
5. **HyperAccess.h** (`HyperAccess.h`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **NewsAccess.m** (`NewsAccess.m`) — 18 outbound dependencies
2. **FileAccess.m** (`FileAccess.m`) — 12 outbound dependencies
3. **HyperText.m** (`HyperText.m`) — 11 outbound dependencies
4. **Anchor.m** (`Anchor.m`) — 9 outbound dependencies
5. **WorldWideWeb_main.m** (`WorldWideWeb_main.m`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `readSGML` **(I/O & Config Routines)** (@ `ParseHTML.h`) -> Impact: **260.8** | LOC: 556
  * *Intent:* #else
- `read_group` **(Many-Argument Workhorses)** (@ `NewsAccess.m`) -> Impact: **126.6** | LOC: 212
  * *Intent:* /* Read in a Newsgroup ** ------------------- ** Unfortunately, we have to ask for each article one by one if we want more ** than one field. ** */
- `change_run` **(Many-Argument Workhorses)** (@ `ParseHTML.h`) -> Impact: **77.2** | LOC: 123
  * *Intent:* /* This function generates the code for one run, given the previous run. ** */
- `applyStyle` **(Many-Argument Workhorses)** (@ `HyperText.m`) -> Impact: **64.8** | LOC: 137
  * *Intent:* // Apply style to a given region // ----------------------------- // // Note that one should not have two consecutive runs of the same style, // nor a...
- `Unknown_Block` **(Many-Argument Workhorses)** (@ `HText.c`) -> Impact: **60.2** | LOC: 85
  * *Intent:* /* Append a character to the text object ** ------------------------------------- */
- `accessName` **(Many-Argument Workhorses)** (@ `NewsAccess.m`) -> Impact: **59.1** | LOC: 143
  * *Intent:* // Open by name -accessName:anchor:diagnostic: // ------------
- `loadAnchor` **(Many-Argument Workhorses)** (@ `FileAccess.m`) -> Impact: **48.8** | LOC: 110
  * *Intent:* ////////////////////////////////////////////////////////////////////////////////// // // O P E N I N G // LOAD ANCHOR // // Returns If successful, the...
- `Unknown_Block` **(Many-Argument Workhorses)** (@ `HText.c`) -> Impact: **45.0** | LOC: 51
  * *Intent:* /* Output a page ** ------------- */
- `Unknown_Block` **(Many-Argument Workhorses)** (@ `HText.c`) -> Impact: **40.1** | LOC: 86
  * *Intent:* ** split is zero for newline function, else number of characters ** before split. ** text->display_on_the_fly ** may be set to indicate direct output ...
- `read_article` **(I/O & Config Routines)** (@ `NewsAccess.m`) -> Impact: **40.0** | LOC: 119
  * *Intent:* /* Read in an Article ** ------------------ */ // // Note the termination condition of a single dot on a line by itself. // RFC 977 specifies that the...

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 31 | 5364.42 | 28.1% | 44.43% |
| `WorldWideWeb.app` | 3 | 43.86 | 0.0% | 0.0% |
| `Test` | 4 | 43.62 | 1.8% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `HyperManager.m` -> **100.0%** Exposure
- `TextToy.m` -> **99.9998%** Exposure
- `,Features.html` -> **99.9993%** Exposure
- `HyperAccess.m` -> **99.9993%** Exposure
- `Features.html` -> **99.999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `FileAccess.m` -> **100.0%** Exposure
- `HTStyle.m` -> **100.0%** Exposure
- `HyperText.m` -> **100.0%** Exposure
- `NewsAccess.m` -> **100.0%** Exposure
- `StyleToy.m` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `HyperText.m` -> **30** Orphaned Functions | **0** Duplicates
- `HyperManager.m` -> **27** Orphaned Functions | **0** Duplicates
- `HyperAccess.m` -> **15** Orphaned Functions | **0** Duplicates
- `TextToy.m` -> **14** Orphaned Functions | **0** Duplicates
- `FileAccess.m` -> **13** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `121` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `HyperText.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.211)
- **Top Global Matches:** file_cluster_15: 8.211, file_cluster_12: 8.57, file_cluster_4: 9.021
- **Magnitude:** 1274.78 | **LOC:** 1614 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 32.459; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (88.6%), Guard Balance (formerly Safety Score) (84.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `applyStyle` **(Many-Argument Workhorses)** (Impact: 64.8)
    * *Intent:* // Apply style to a given region // ----------------------------- // // Note that one should not hav...
  * `adjustWindow` **(I/O & Config Routines)** (Impact: 18.5)
    * *Intent:* // Adjust Scrollers and Window size for current text size // ---------------------------------------...
  * `willChange` **(Compute Cores)** (Impact: 18.2)
    * *Intent:* // Check whether copying a style into a run will change it // --------------------------------------...
  * `apply` **(Compute Cores)** (Impact: 17.0)
    * *Intent:* // Copy a style into a run // -----------------------
  * `endOfParagraph` **(Compute Cores)** (Impact: 15.7)
    * *Intent:* // Find end of paragraph // ----------------------- // // Returns the position after the newline, or...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 267 instances
* *State Mutation (weighted view):* 862
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 84`, `args: 31`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 328`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 30`
* *Architecture:* `io: 14`, `api: 3`, `import: 11`
* *Defense:* `immutability_locks: 4`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 32.459
  * `Choke Point (Betweenness):` 0.006757 | `Ripple Effect (Closeness):` 0.081081
  * `Imports (Out-Degree: 4):` HTAnchor.h, HTML.h, HTAnchor.h, HTML.h, HTParse.h, HTStyle.h, HTUtils.h, HyperAccess.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `HText.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.587)
- **Top Global Matches:** file_cluster_4: 7.587, file_cluster_12: 9.631, file_cluster_7: 11.337
- **Magnitude:** 747.44 | **LOC:** 794 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 16.898; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.8%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Unknown_Block` **(Many-Argument Workhorses)** (Impact: 60.2)
    * *Intent:* /* Append a character to the text object ** ------------------------------------- */
  * `Unknown_Block` **(Many-Argument Workhorses)** (Impact: 45.0)
    * *Intent:* /* Output a page ** ------------- */
  * `Unknown_Block` **(Many-Argument Workhorses)** (Impact: 40.1)
    * *Intent:* ** split is zero for newline function, else number of characters ** before split. ** text->display_o...
  * `Unknown_Block` **(Many-Argument Workhorses)** (Impact: 22.0)
  * `Unknown_Block` **(Many-Argument Workhorses)** (Impact: 16.6)
    * *Intent:* } /* split_line */ /* Allow vertical blank space ** -------------------------- */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 100 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 321
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 62`, `args: 44`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 121`
* *Architecture:* `api: 82`, `import: 5`
* *Defense:* `safety: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HTString.h, HTUtils.h, HText.h, HyperText.h, ctype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ParseHTML.h` (OBJECTIVE-C | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.746)
- **Top Global Matches:** file_cluster_6: 7.746, file_cluster_4: 9.794, file_cluster_9: 16.583
- **Magnitude:** 706.82 | **LOC:** 1170 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 16.898; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.1%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readSGML` **(I/O & Config Routines)** (Impact: 260.8)
    * *Intent:* #else
  * `change_run` **(Many-Argument Workhorses)** (Impact: 77.2)
    * *Intent:* /* This function generates the code for one run, given the previous run. ** */
  * `parse_example` **(Compute Cores)** (Impact: 19.2)
    * *Intent:* /* Read example text ** ----------------- ** ** Returns when terminator or end-of-file found. ** ** ...
  * `findSGML` **(Type Conversions)** (Impact: 10.8)
    * *Intent:* static const char * saveName; /* pointer to name node is being saved under */ static char * prefix; ...
  * `writeSGML` **(Many-Argument Workhorses)** (Impact: 10.7)
    * *Intent:* } /* change_run */ /* This is the body of the SGML output method. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 276
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 38`, `args: 9`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 110`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 1`, `import: 1`
* *Defense:* `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` HTStyle.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `NewsAccess.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.729)
- **Top Global Matches:** file_cluster_6: 7.729, file_cluster_8: 10.94, file_cluster_4: 15.02
- **Magnitude:** 667.82 | **LOC:** 905 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 16.898; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.5%), Guard Balance (formerly Safety Score) (74.3%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_group` **(Many-Argument Workhorses)** (Impact: 126.6)
    * *Intent:* /* Read in a Newsgroup ** ------------------- ** Unfortunately, we have to ask for each article one ...
  * `accessName` **(Many-Argument Workhorses)** (Impact: 59.1)
    * *Intent:* // Open by name -accessName:anchor:diagnostic: // ------------
  * `read_article` **(I/O & Config Routines)** (Impact: 40.0)
    * *Intent:* /* Read in an Article ** ------------------ */ // // Note the termination condition of a single dot ...
  * `response` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* /* Send NNTP Command line to remote host & Check Response ** ---------------------------------------...
  * `read_list` **(I/O & Config Routines)** (Impact: 13.7)
    * *Intent:* /* Read in a List of Newsgroups ** ---------------------------- */ // // Note the termination condit...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 109 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 330
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 40`, `args: 9`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 112`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 8`, `api: 4`, `import: 18`
* *Defense:* `immutability_locks: 14`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Anchor.h, HTParse.h, HTStyle.h, HTUtils.h, NewsAccess.h, defaults.h, inet.h, ctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `FileAccess.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.843)
- **Top Global Matches:** file_cluster_4: 5.843, file_cluster_15: 10.546, file_cluster_6: 10.846
- **Magnitude:** 398.88 | **LOC:** 643 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 20.489; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.0%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadAnchor` **(Many-Argument Workhorses)** (Impact: 48.8)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////// // // O P E N I N...
  * `ask_name` **(Compute Cores)** (Impact: 29.5)
    * *Intent:* // Get Filename near a "hint" node // ------------------------------- // // On entry, // hint is a h...
  * `saveNode` **(Compute Cores)** (Impact: 22.2)
    * *Intent:* // Save as an HTML file of same name // --------------------------------- // // We don't use a suffi...
  * `makeNew` **(Compute Cores)** (Impact: 20.2)
    * *Intent:* // Make a new blank node named like the current node // --------------------------------------------...
  * `save` **(Many-Argument Workhorses)** (Impact: 19.1)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////////// // S A V I N ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 61 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 184
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 49`, `args: 21`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 62`, `unreferenced_by_name: 13`
* *Architecture:* `io: 14`, `api: 1`, `import: 12`
* *Defense:* `doc: 2`, `immutability_locks: 12`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 20.489
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.027027
  * `Imports (Out-Degree: 0):` FileAccess.h, HTFTP.h, HTFile.h, HTParse.h, HTTCP.h, HTUtils.h, WWW.h, appkit.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `HTStyle.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.939)
- **Top Global Matches:** file_cluster_15: 5.939, file_cluster_11: 7.844, file_cluster_16: 7.938
- **Magnitude:** 281.36 | **LOC:** 353 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 36.962; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.2%), Complexity Load (formerly Cognitive Load) (68.1%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HTStyleForRun` **(Compute Cores)** (Impact: 24.0)
    * *Intent:* /* Find the style which best fits a given run ** ------------------------------------------ ** ** Th...
  * `HTStyleRead` **(Many-Argument Workhorses)** (Impact: 18.0)
    * *Intent:* /* Read a style from a typed stream (without its name) ** -------------------------------- ** ** Rea...
  * `HTStyleSheetRead` **(Type Conversions)** (Impact: 9.7)
    * *Intent:* /* Read a stylesheet from a typed stream ** ------------------------------------- ** ** Reads a styl...
  * `HTStyleSheetRemoveStyle` **(Compute Cores)** (Impact: 9.5)
    * *Intent:* /* Remove the given object from a style sheet if it exists */
  * `HTStyleWrite` **(Compute Cores)** (Impact: 8.4)
    * *Intent:* /* Write a style to a stream in a compatible way */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 52 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 20`, `args: 13`, `func_start: 15`
* *Risk/State:* `state_mutation: 55`, `unreferenced_by_name: 7`
* *Architecture:* `io: 4`, `import: 2`
* *Defense:* `immutability_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.112613
  * `Imports (Out-Degree: 1):` HTStyle.h, HTUtils.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `StyleToy.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.807)
- **Top Global Matches:** file_cluster_15: 5.807, file_cluster_11: 7.801, file_cluster_12: 7.851
- **Magnitude:** 228.26 | **LOC:** 345 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 16.898; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (92.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.5%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `saveAs` **(Compute Cores)** (Impact: 14.8)
    * *Intent:* // Save style sheet to a file // --------------------------
  * `open` **(Type Conversions)** (Impact: 12.9)
    * *Intent:* // Open a style sheet from a file // ------------------------------ // // We overlay any previously ...
  * `loadDefaultStyleSheet` **(I/O & Config Routines)** (Impact: 9.8)
    * *Intent:* // Load default style sheet // ------------------------ // // We load EITHER the user's style sheet ...
  * `display_style` **(I/O & Config Routines)** (Impact: 8.3)
    * *Intent:* // ACTION METHODS // ============== // Display style in the panel
  * `NextButton` **(Compute Cores)** (Impact: 7.7)
    * *Intent:* // Move to next style // ------------------
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 43 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 24`, `args: 13`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 52`, `unreferenced_by_name: 12`
* *Architecture:* `io: 5`, `api: 1`, `import: 5`
* *Defense:* `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` HTParse.h, HTStyle.h, HTUtils.h, HyperText.h, StyleToy.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HyperManager.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.747)
- **Top Global Matches:** file_cluster_12: 6.747, file_cluster_15: 7.55, file_cluster_11: 8.931
- **Magnitude:** 217.68 | **LOC:** 441 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 16.898; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadAnchor` **(Many-Argument Workhorses)** (Impact: 27.7)
    * *Intent:* // Load an anchor from some access loadAnchor: // ------------------------------- // // This impleme...
  * `closeOthers` **(Compute Cores)** (Impact: 11.1)
    * *Intent:* // Close all unedited windows except this one // ------------------------------------------ //
  * `searchDiagnostic` **(Compute Cores)** (Impact: 10.9)
    * *Intent:* // Search with a given diagnostic level // // This involves making a special address string, being t...
  * `saveAll` **(Compute Cores)** (Impact: 9.5)
    * *Intent:* // Save all hypertexts back // -------------------------
  * `registerAccess` **(Type Conversions)** (Impact: 6.1)
    * *Intent:* // Access Management functions //
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 29 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 40`, `args: 30`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 33`, `dead_code: 2`, `fragile_debt: 2`, `unreferenced_by_name: 27`
* *Architecture:* `io: 8`, `api: 1`, `import: 6`
* *Defense:* `immutability_locks: 8`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` HTAccess.h, HTParse.h, HTUtils.h, HyperManager.h, HyperText.h, WWWPageLayout.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Anchor.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.819)
- **Top Global Matches:** file_cluster_15: 6.819, file_cluster_11: 6.891, file_cluster_12: 7.895
- **Magnitude:** 156.3 | **LOC:** 364 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 16.898; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (92.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.4%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `selectDiagnostic` **(Type Conversions)** (Impact: 15.2)
    * *Intent:* /* Select the anchor select ** ----------------- ** ** This will load the node is necessary, if the ...
  * `newAddress` **(Compute Cores)** (Impact: 11.8)
    * *Intent:* // Create new or find old named anchor // ----------------------------------- // // This one is for ...
  * `newParent` **(Type Conversions)** (Impact: 9.8)
    * *Intent:* // Create new or find old sub-anchor // --------------------------------- // // This one is for a ne...
  * `moveBy` **(Type Conversions)** (Impact: 9.3)
    * *Intent:* // Go to next logical step // ----------------------- // // We take the link After or before the one...
  * `equivalent` **(Compute Cores)** (Impact: 7.3)
    * *Intent:* // Case insensitive string comparison // ---------------------------------- // On entry, // s Points...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 14 instances
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 35`, `args: 9`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 26`, `unreferenced_by_name: 11`
* *Architecture:* `io: 2`, `api: 2`, `import: 9`
* *Defense:* `immutability_locks: 6`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Anchor.h, HTParse.h, HTUtils.h, HyperManager.h, HyperText.h, appkit.h, ctype.h, Object.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HyperText.h` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 8.068)
- **Top Global Matches:** file_cluster_17: 8.068, file_cluster_2: 8.882, file_cluster_15: 8.909
- **Magnitude:** 93.44 | **LOC:** 95 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **4**; blast radius 81.514; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readSGML` **(Type Conversions)** (Impact: 1.8)
  * `writeSGML` **(Type Conversions)** (Impact: 1.8)
  * `replaceSel` **(Type Conversions)** (Impact: 1.8)
  * `newAnchor` **(Type Conversions)** (Impact: 1.5)
  * `readText` **(Type Conversions)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 27`, `func_start: 40`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 7`, `api: 38`, `import: 4`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 81.514
  * `Choke Point (Betweenness):` 0.008258 | `Ripple Effect (Closeness):` 0.228935
  * `Imports (Out-Degree: 2):` Anchor.h, HTStyle.h, Text.h, List.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `HTStyle.h` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 5.007)
- **Top Global Matches:** file_cluster_7: 5.007, file_cluster_12: 7.386, file_cluster_5: 8.793
- **Magnitude:** 78.94 | **LOC:** 78 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **1**; blast radius 117.386; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (89.8%), Debt Markers (formerly Tech Debt) (60.9%), Guard Balance (formerly Safety Score) (59.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `args: 13`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 15`, `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 117.386
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.243243
  * `Imports (Out-Degree: 0):` appkit.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `HyperAccess.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.958)
- **Top Global Matches:** file_cluster_15: 5.958, file_cluster_11: 6.362, file_cluster_17: 7.896
- **Magnitude:** 49.68 | **LOC:** 159 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 16.898; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (74.3%), Guard Balance (formerly Safety Score) (54.0%), Complexity Load (formerly Cognitive Load) (14.9%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `text` **(Type Conversions)** (Impact: 3.7)
    * *Intent:* // Text Delegate methods // --------------------- // These default methods for an access allow editi...
  * `textDidChange` **(Type Conversions)** (Impact: 3.1)
    * *Intent:* #endif
  * `textWillChange` **(Type Conversions)** (Impact: 3.1)
  * `accessName` **(Type Conversions)** (Impact: 1.9)
  * `loadAnchor` **(Type Conversions)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 22`, `args: 18`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 15`
* *Architecture:* `io: 1`, `import: 6`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Anchor.h, HTUtils.h, HyperAccess.h, HyperManager.h, appkit.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `WWWPageLayout.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.587)
- **Top Global Matches:** file_cluster_12: 6.587, file_cluster_7: 8.3, file_cluster_15: 8.47
- **Magnitude:** 45.34 | **LOC:** 133 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 16.898; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Complexity Load (formerly Cognitive Load) (66.0%), Guard Balance (formerly Safety Score) (64.7%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writePrintInfo` **(I/O & Config Routines)** (Impact: 4.1)
  * `pickedUnits` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* /* * PageLayout is overridden so that the user can set the margins of * the page. This is important ...
  * `readPrintInfo` **(I/O & Config Routines)** (Impact: 2.0)
  * `setTopBotForm` **(Parameter Forwarders)** (Impact: 1.8)
    * *Intent:* /* NIB outlet setting methods */
  * `setSideForm` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 11`, `args: 7`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 21`, `unreferenced_by_name: 9`
* *Architecture:* `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` WWWPageLayout.h, Application.h, Matrix.h, PrintInfo.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Anchor.h` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.785)
- **Top Global Matches:** file_cluster_7: 7.785, file_cluster_12: 10.053, file_cluster_5: 10.449
- **Magnitude:** 40.64 | **LOC:** 58 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **3**; blast radius 102.079; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (98.4%), Guard Balance (formerly Safety Score) (60.0%), Test Surface (formerly Verification) (3.0%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `newParent` **(Type Conversions)** (Impact: 1.8)
  * `setManager` **(State Mutators)** (Impact: 1.5)
  * `newAddress` **(State Mutators)** (Impact: 1.5)
  * `setNode` **(Type Conversions)** (Impact: 1.5)
  * `setAddress` **(State Mutators)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 7`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `api: 16`, `import: 3`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 102.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.228378
  * `Imports (Out-Degree: 0):` appkit.h, List.h, Object.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `TextToy.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.896)
- **Top Global Matches:** file_cluster_15: 4.896, file_cluster_11: 7.285, file_cluster_2: 7.481
- **Magnitude:** 40.4 | **LOC:** 136 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 16.898; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (83.2%), Guard Balance (formerly Safety Score) (54.1%), Complexity Load (formerly Cognitive Load) (17.0%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `windowDidBecomeMain` **(Compute Cores)** (Impact: 6.3)
    * *Intent:* // When a document is selected, turn the index search on or off as // appropriate
  * `registerAccess` **(Type Conversions)** (Impact: 3.1)
    * *Intent:* // Access Management functions // ===========================
  * `Do_getStartLength` **(Parameter Forwarders)** (Impact: 2.0)
    * *Intent:* /* Action Methods ** ============== */ #ifdef JUNK
  * `Do_getSel` **(Parameter Forwarders)** (Impact: 1.8)
    * *Intent:* /* Method: Get the extent of the selection */
  * `setSearchWindow` **(Parameter Forwarders)** (Impact: 1.7)
    * *Intent:* #import <appkit/appkit.h> #import "Anchor.h" #import "HyperText.h" #import <objc/List.h> #import "HT...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 17`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 14`
* *Architecture:* `io: 3`, `import: 6`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Anchor.h, HTUtils.h, HyperText.h, TextToy.h, appkit.h, List.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HyperAccess.h` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.86)
- **Top Global Matches:** file_cluster_7: 7.86, file_cluster_14: 10.15, file_cluster_12: 10.658
- **Magnitude:** 36.32 | **LOC:** 56 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 54.138; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (83.4%), Guard Balance (formerly Safety Score) (60.0%), Test Surface (formerly Verification) (2.7%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadAnchor` **(Type Conversions)** (Impact: 1.8)
  * `setOpenString` **(State Mutators)** (Impact: 1.5)
    * *Intent:* // Interface builder initialisation methods:
  * `setKeywords` **(State Mutators)** (Impact: 1.5)
  * `setContentSearch` **(State Mutators)** (Impact: 1.5)
  * `search` **(State Mutators)** (Impact: 1.5)
    * *Intent:* // Action methods for buttons etc:
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `io: 2`, `api: 13`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 54.138
  * `Choke Point (Betweenness):` 0.004505 | `Ripple Effect (Closeness):` 0.133056
  * `Imports (Out-Degree: 2):` Anchor.h, HyperText.h, List.h, Object.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `HyperManager.h` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.055)
- **Top Global Matches:** file_cluster_2: 6.055, file_cluster_13: 6.317, file_cluster_17: 6.546
- **Magnitude:** 35.42 | **LOC:** 35 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 30.065; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (88.0%), Test Surface (formerly Verification) (2.7%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `traceOn` **(State Mutators)** (Impact: 1.5)
  * `traceOff` **(State Mutators)** (Impact: 1.5)
  * `back` **(State Mutators)** (Impact: 1.5)
  * `next` **(State Mutators)** (Impact: 1.5)
  * `previous` **(State Mutators)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 14`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.065
  * `Choke Point (Betweenness):` 0.001502 | `Ripple Effect (Closeness):` 0.081081
  * `Imports (Out-Degree: 1):` HyperAccess.h, List.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `TcpAccess.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.289)
- **Top Global Matches:** file_cluster_11: 7.289, file_cluster_15: 7.785, file_cluster_2: 8.684
- **Magnitude:** 34.76 | **LOC:** 109 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 16.898; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (81.8%), Guard Balance (formerly Safety Score) (59.2%), Complexity Load (formerly Cognitive Load) (41.1%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `accessName` **(Many-Argument Workhorses)** (Impact: 10.2)
    * *Intent:* // Open or search by name // -----------------------
  * `loadAnchor` **(Type Conversions)** (Impact: 9.4)
    * *Intent:* // Actions: // This will load an anchor which has a name // // On entry, // Anchor's address is vali...
  * `name` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* #import "HTUtils.h" #import "HTTP.h" /* Module parameters: ** ----------------- ** ** These may be u...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 9`, `args: 2`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `import: 4`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Anchor.h, HTTP.h, HTUtils.h, TcpAccess.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HTextNeXT.h` (OBJECTIVE-C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 3.498)
- **Top Global Matches:** file_cluster_17: 3.498, file_cluster_2: 5.717, file_cluster_13: 7.294
- **Magnitude:** 32.24 | **LOC:** 173 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 16.898; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (11.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 16`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HTAnchor.h, HTStyle.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Features.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.152)
- **Top Global Matches:** file_cluster_2: 4.152, file_cluster_17: 5.266, file_cluster_13: 5.937
- **Magnitude:** 30.14 | **LOC:** 258 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (8.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 86`, `args: 28`
* *Risk/State:* `fragile_debt: 24`
* *Architecture:* `io: 18`, `api: 10`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `,Features.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.187)
- **Top Global Matches:** file_cluster_2: 4.187, file_cluster_17: 5.288, file_cluster_13: 5.951
- **Magnitude:** 30.02 | **LOC:** 252 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (8.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 86`, `args: 28`
* *Risk/State:* `fragile_debt: 24`
* *Architecture:* `io: 18`, `api: 10`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `WorldWideWeb_main.m` (OBJECTIVE-C | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.679)
- **Top Global Matches:** file_cluster_15: 8.679, file_cluster_2: 8.709, file_cluster_17: 9.146
- **Magnitude:** 27.44 | **LOC:** 73 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 16.898; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.9%), Complexity Load (formerly Cognitive Load) (41.1%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 7.3)
  * `int_default` **(Type Conversions)** (Impact: 3.2)
    * *Intent:* #import <stdlib.h> #import <appkit/Application.h> // #import <appkit/defaults.h> /* TBL */ #import "...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 4 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 1`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTUtils.h, Application.h, PrintInfo.h, defaults.h, libc.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugs.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.633)
- **Top Global Matches:** file_cluster_2: 3.633, file_cluster_17: 4.777, file_cluster_13: 5.494
- **Magnitude:** 20.46 | **LOC:** 124 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (76.1%), Connectivity (formerly Api Exposure) (5.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 47`, `args: 22`
* *Risk/State:* `fragile_debt: 3`
* *Architecture:* `io: 6`, `api: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.946)
- **Top Global Matches:** file_cluster_2: 3.946, file_cluster_17: 5.114, file_cluster_13: 5.732
- **Magnitude:** 16.98 | **LOC:** 103 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 36`, `args: 21`
* *Risk/State:* None
* *Architecture:* `io: 13`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Test/backup_of_test.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.598)
- **Top Global Matches:** file_cluster_2: 3.598, file_cluster_17: 4.978, file_cluster_13: 5.634
- **Magnitude:** 16.86 | **LOC:** 99 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 33`, `args: 8`
* *Risk/State:* None
* *Architecture:* `io: 11`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `WorldWideWeb_main.m` (OBJECTIVE-C) | Magnitude: 27.44 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, indent_tabs: 11, ui_framework: 10, core_var_decl: 10
- `Anchor.m` (OBJECTIVE-C) | Magnitude: 156.3 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 78, branch: 40, structural_boundaries: 35, indent_tabs: 31

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `HyperText.m` -> **Severity: 0.676** (Bridge: 0.0068 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `HTStyle.h` -> **Severity: 14.452** (Embedded: 0.2432 * Error Risk: 59.4118%)
- `Anchor.h` -> **Severity: 13.703** (Embedded: 0.2284 * Error Risk: 60.0%)
- `HTStyle.m` -> **Severity: 8.583** (Embedded: 0.1126 * Error Risk: 76.221%)
- `HyperAccess.h` -> **Severity: 7.983** (Embedded: 0.1331 * Error Risk: 60.0%)
- `HyperText.m` -> **Severity: 6.821** (Embedded: 0.0811 * Error Risk: 84.1257%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Anchor.h` -> **Severity: 8579.434** (Blast Radius: 102.079 * Doc Risk: 84.047%)
- `HyperText.h` -> **Severity: 6851.007** (Blast Radius: 81.514 * Doc Risk: 84.047%)
- `HyperAccess.h` -> **Severity: 4550.136** (Blast Radius: 54.138 * Doc Risk: 84.047%)
- `HTStyle.m` -> **Severity: 3106.545** (Blast Radius: 36.962 * Doc Risk: 84.047%)
- `WWWPageLayout.h` -> **Severity: 2929.29** (Blast Radius: 34.853 * Doc Risk: 84.047%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`memory_alloc`:** 56 literal sites + 16 sites through wrappers = 72

- `HTStyleNew` (function, memory_alloc, primitive): 7 call sites in 3 files -- `HTStyle.m`
- `start_style` (function, memory_alloc, primitive): 6 call sites in 1 files -- `ParseHTML.h`
- `HTStyleSheetNew` (function, memory_alloc, primitive): 2 call sites in 1 files -- `HTStyle.m`
- `HTStyleNewNamed` (function, memory_alloc, via HTStyleNew): 1 call sites in 1 files -- `HTStyle.m`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 836 call pairs -- scoped 19.0%, unique 2.8%, ambiguous 13.8%, external 64.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| objective-c | 769 | 20.7% | 3.0% | 14.7% | 61.6% |
| c | 67 | 0.0% | 0.0% | 3.0% | 97.0% |

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
