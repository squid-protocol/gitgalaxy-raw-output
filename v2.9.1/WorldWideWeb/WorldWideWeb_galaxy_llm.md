# ARCHITECTURAL_BRIEF: WorldWideWeb
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/simonw/1991-WWW-NeXT-Implementation.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 37 analyzed artifact(s), 6034 LOC.
- **Load-bearing artifact:** `Anchor.h` -- 7 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `NewsAccess.m` -- pulls in 18 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `HyperText.m` at magnitude 1280.58 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 37 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 26 |
| Total LOC | 6034 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 58.7% |
| Dominant Lang | OBJECTIVE-C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3145 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2311 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| OBJECTIVE-C | 20 | 4462 | 54.1% |
| HTML | 10 | 983 | 27.0% |
| C | 3 | 550 | 8.1% |
| MAKEFILE | 2 | 39 | 5.4% |
| MARKDOWN | 1 | 0 | 2.7% |
| PLAINTEXT | 1 | 0 | 2.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `2.611`
> **Composition Archetype:** `Small Flat Repo (2)` (z +2.61; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 32%, Large Core Modules (3) 19%, State Mutators Files 14%, Parameter Forwarders Files 11%, Declarative / Non-Code 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 35 | 94.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 5.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 26*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (Binary Format Detected), 1x Excluded (Unsupported Extension: '.dependencies'), 1x Unsupported Format (.undeterminable)
- `.style`: 6x Excluded (Unsupported Extension: '.style')
- `.h`: 2x Excluded (Machine-Generated Source Code Signature: 12 LOC), 1x Excluded (Machine-Generated Source Code Signature: 20 LOC), 1x Excluded (Machine-Generated Source Code Signature: 31 LOC)
- `.tiff`: 3x Excluded (Explicitly Denied Extension: '.tiff')
- `.iconheader`: 2x Excluded (Unsupported Extension: '.iconheader')
- `.proj`: 1x Excluded (Unsupported Extension: '.proj')
- `.html`: 1x Excluded (Machine-Generated Source Code Signature: 83 LOC)
- `.debug`: 1x Excluded (Unsupported Extension: '.debug')
- `.nib`: 1x Excluded (Unsupported Extension: '.nib')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 91.8 | 25.5 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.4 | 48.3 | 68.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 41.2 | 9.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 24.3 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.4 | 2.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 38.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 14.1 | 1.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 54.2 | 84.0 | 84.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1351 | 21 | 83 | `HyperText.m` |
| cleanup | 61 | 14 | 6 | `FileAccess.m` |
| guards | 67 | 15 | 4 | `NewsAccess.m` |
| danger | 54 | 16 | 3 | `HText.c` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 243 | 22 | 15 | `HText.c` |
| io | 192 | 25 | 14 | `WorldWideWeb.app/default.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 1 | 1 | 0 | `WorldWideWeb_main.m` |
| tests | 0 | 0 | 0 | - |
| docs | 12 | 11 | 1 | `FileAccess.m` |
| debt | 244 | 19 | 19 | `HyperText.m` |
| mutation | 1638 | 27 | 120 | `HyperText.m` |
| dead_code | 168 | 16 | 14 | `HyperManager.m` |
| credential | 0 | 0 | 0 | - |
| threat | 1 | 1 | 0 | `HText.c` |
| ml_ai | 23 | 2 | 0 | `HyperText.m` |
| ui | 97 | 17 | 10 | `HyperText.m` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `WorldWideWeb.app/default.html` (Hits: 19)
- `default.html` (Hits: 19)
- `,Features.html` (Hits: 18)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Anchor.h** (`Anchor.h`) — 7 inbound connections
2. **HTStyle.h** (`HTStyle.h`) — 7 inbound connections
3. **HyperText.h** (`HyperText.h`) — 7 inbound connections
4. **HyperAccess.h** (`HyperAccess.h`) — 3 inbound connections
5. **HyperManager.h** (`HyperManager.h`) — 3 inbound connections

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
- `read_group` **(Many-Argument Workhorses)** (@ `NewsAccess.m`) -> Impact: **128.6** | LOC: 212
  * *Intent:* /* Read in a Newsgroup ** ------------------- ** Unfortunately, we have to ask for each article one by one if we want more ** than one field. ** */
- `change_run` **(Many-Argument Workhorses)** (@ `ParseHTML.h`) -> Impact: **77.2** | LOC: 123
  * *Intent:* /* This function generates the code for one run, given the previous run. ** */
- `accessName` **(Many-Argument Workhorses)** (@ `NewsAccess.m`) -> Impact: **65.2** | LOC: 143
  * *Intent:* // Open by name -accessName:anchor:diagnostic: // ------------
- `applyStyle` **(Many-Argument Workhorses)** (@ `HyperText.m`) -> Impact: **64.8** | LOC: 137
  * *Intent:* // Apply style to a given region // ----------------------------- // // Note that one should not have two consecutive runs of the same style, // nor a...
- `Unknown_Block` **(Many-Argument Workhorses)** (@ `HText.c`) -> Impact: **60.2** | LOC: 85
  * *Intent:* /* Append a character to the text object ** ------------------------------------- */
- `loadAnchor` **(Many-Argument Workhorses)** (@ `FileAccess.m`) -> Impact: **48.8** | LOC: 110
  * *Intent:* ////////////////////////////////////////////////////////////////////////////////// // // O P E N I N G // LOAD ANCHOR // // Returns If successful, the...
- `Unknown_Block` **(Many-Argument Workhorses)** (@ `HText.c`) -> Impact: **45.0** | LOC: 51
  * *Intent:* /* Output a page ** ------------- */
- `read_article` **(I/O & Config Routines)** (@ `NewsAccess.m`) -> Impact: **43.0** | LOC: 119
  * *Intent:* /* Read in an Article ** ------------------ */ // // Note the termination condition of a single dot on a line by itself. // RFC 977 specifies that the...
- `Unknown_Block` **(Many-Argument Workhorses)** (@ `HText.c`) -> Impact: **40.1** | LOC: 86
  * *Intent:* ** split is zero for newline function, else number of characters ** before split. ** text->display_on_the_fly ** may be set to indicate direct output ...

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 30 | 5413.23 | 29.51% | 48.04% |
| `WorldWideWeb.app` | 3 | 43.86 | 0.0% | 0.0% |
| `Test` | 4 | 43.62 | 1.8% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `HyperManager.m` -> **100.0%** Exposure
- `TextToy.m` -> **99.9999%** Exposure
- `HyperAccess.m` -> **99.9996%** Exposure
- `,Features.html` -> **99.9993%** Exposure
- `Features.html` -> **99.999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `FileAccess.m` -> **100.0%** Exposure
- `HTStyle.m` -> **100.0%** Exposure
- `HyperText.m` -> **100.0%** Exposure
- `NewsAccess.m` -> **100.0%** Exposure
- `StyleToy.m` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `HyperText.m` -> **29** Orphaned Functions | **0** Duplicates
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
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1280.58 | **LOC:** 1614 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 17.717; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Debt Markers (formerly Tech Debt) (87.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `applyStyle` **(Many-Argument Workhorses)** (Impact: 64.8)
    * *Intent:* // Apply style to a given region // ----------------------------- // // Note that one should not hav...
  * `adjustWindow` **(I/O & Config Routines)** (Impact: 19.5)
    * *Intent:* // Adjust Scrollers and Window size for current text size // ---------------------------------------...
  * `willChange` **(Compute Cores)** (Impact: 18.2)
    * *Intent:* // Check whether copying a style into a run will change it // --------------------------------------...
  * `apply` **(Compute Cores)** (Impact: 17.0)
    * *Intent:* // Copy a style into a run // -----------------------
  * `endOfParagraph` **(Compute Cores)** (Impact: 15.7)
    * *Intent:* // Find end of paragraph // ----------------------- // // Returns the position after the newline, or...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 274 instances
* *State Mutation (weighted view):* 876
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 84`, `args: 31`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 328`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 29`
* *Architecture:* `io: 14`, `api: 3`, `import: 11`
* *Defense:* `immutability_locks: 4`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` HTAnchor.h, HTML.h, HTAnchor.h, HTML.h, HTParse.h, HTStyle.h, HTUtils.h, HyperAccess.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HText.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 749.14 | **LOC:** 794 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 17.717; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.5%), Complexity Load (formerly Cognitive Load) (91.8%), Test Surface (formerly Verification) (80.0%)
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
* *Structure:* `branch: 110`, `structural_boundaries: 62`, `args: 44`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 121`, `dead_code: 1`
* *Architecture:* `api: 82`, `import: 5`
* *Defense:* `safety: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HTString.h, HTUtils.h, HText.h, HyperText.h, ctype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ParseHTML.h` (OBJECTIVE-C | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 708.62 | **LOC:** 1170 | **CtrlFlow:** 38.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 17.717; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.4%), Complexity Load (formerly Cognitive Load) (81.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readSGML` **(I/O & Config Routines)** (Impact: 260.8)
    * *Intent:* #else
  * `change_run` **(Many-Argument Workhorses)** (Impact: 77.2)
    * *Intent:* /* This function generates the code for one run, given the previous run. ** */
  * `parse_example` **(Compute Cores)** (Impact: 21.0)
    * *Intent:* /* Read example text ** ----------------- ** ** Returns when terminator or end-of-file found. ** ** ...
  * `findSGML` **(Type Conversions)** (Impact: 10.8)
    * *Intent:* static const char * saveName; /* pointer to name node is being saved under */ static char * prefix; ...
  * `writeSGML` **(Many-Argument Workhorses)** (Impact: 10.7)
    * *Intent:* } /* change_run */ /* This is the body of the SGML output method. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 276
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 313`, `structural_boundaries: 38`, `args: 9`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 110`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 1`, `import: 1`
* *Defense:* `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HTStyle.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `NewsAccess.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 683.62 | **LOC:** 905 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 17.717; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.9%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_group` **(Many-Argument Workhorses)** (Impact: 128.6)
    * *Intent:* /* Read in a Newsgroup ** ------------------- ** Unfortunately, we have to ask for each article one ...
  * `accessName` **(Many-Argument Workhorses)** (Impact: 65.2)
    * *Intent:* // Open by name -accessName:anchor:diagnostic: // ------------
  * `read_article` **(I/O & Config Routines)** (Impact: 43.0)
    * *Intent:* /* Read in an Article ** ------------------ */ // // Note the termination condition of a single dot ...
  * `read_list` **(I/O & Config Routines)** (Impact: 16.6)
    * *Intent:* /* Read in a List of Newsgroups ** ---------------------------- */ // // Note the termination condit...
  * `response` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* /* Send NNTP Command line to remote host & Check Response ** ---------------------------------------...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 109 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 330
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 40`, `args: 9`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 112`, `dead_code: 12`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 8`, `api: 4`, `import: 18`
* *Defense:* `immutability_locks: 14`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Anchor.h, HTParse.h, HTStyle.h, HTUtils.h, NewsAccess.h, defaults.h, inet.h, ctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `FileAccess.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 400.28 | **LOC:** 643 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 17.717; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.7%), Complexity Load (formerly Cognitive Load) (87.0%), Test Surface (formerly Verification) (80.0%)
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
* *Structure:* `branch: 94`, `structural_boundaries: 49`, `args: 21`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 62`, `dead_code: 1`, `unreferenced_by_name: 13`
* *Architecture:* `io: 14`, `api: 1`, `import: 12`
* *Defense:* `doc: 2`, `immutability_locks: 12`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FileAccess.h, HTFTP.h, HTFile.h, HTParse.h, HTTCP.h, HTUtils.h, WWW.h, appkit.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HTStyle.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 283.06 | **LOC:** 353 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 17.717; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.5%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HTStyleForRun` **(Compute Cores)** (Impact: 25.7)
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
* *Structure:* `branch: 49`, `structural_boundaries: 20`, `args: 13`, `func_start: 15`
* *Risk/State:* `state_mutation: 55`, `dead_code: 2`, `unreferenced_by_name: 7`
* *Architecture:* `io: 4`, `import: 2`
* *Defense:* `immutability_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HTStyle.h, HTUtils.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `StyleToy.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 233.66 | **LOC:** 345 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 17.717; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.5%), Debt Markers (formerly Tech Debt) (93.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `saveAs` **(Compute Cores)** (Impact: 16.2)
    * *Intent:* // Save style sheet to a file // --------------------------
  * `loadDefaultStyleSheet` **(I/O & Config Routines)** (Impact: 13.8)
    * *Intent:* // Load default style sheet // ------------------------ // // We load EITHER the user's style sheet ...
  * `open` **(Type Conversions)** (Impact: 12.9)
    * *Intent:* // Open a style sheet from a file // ------------------------------ // // We overlay any previously ...
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
* *Structure:* `branch: 45`, `structural_boundaries: 24`, `args: 13`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 52`, `unreferenced_by_name: 12`
* *Architecture:* `io: 5`, `api: 1`, `import: 5`
* *Defense:* `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` HTParse.h, HTStyle.h, HTUtils.h, HyperText.h, StyleToy.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HyperManager.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 227.18 | **LOC:** 441 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 17.717; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.2%), Complexity Load (formerly Cognitive Load) (89.1%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadAnchor` **(Many-Argument Workhorses)** (Impact: 32.9)
    * *Intent:* // Load an anchor from some access loadAnchor: // ------------------------------- // // This impleme...
  * `searchDiagnostic` **(Compute Cores)** (Impact: 13.8)
    * *Intent:* // Search with a given diagnostic level // // This involves making a special address string, being t...
  * `closeOthers` **(Compute Cores)** (Impact: 11.1)
    * *Intent:* // Close all unedited windows except this one // ------------------------------------------ //
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
* *Structure:* `branch: 46`, `structural_boundaries: 40`, `args: 30`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 33`, `dead_code: 4`, `fragile_debt: 2`, `unreferenced_by_name: 27`
* *Architecture:* `io: 8`, `api: 1`, `import: 6`
* *Defense:* `immutability_locks: 8`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` HTAccess.h, HTParse.h, HTUtils.h, HyperManager.h, HyperText.h, WWWPageLayout.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Anchor.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 140.8 | **LOC:** 364 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 17.717; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (90.7%), Guard Balance (formerly Safety Score) (82.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `selectDiagnostic` **(Type Conversions)** (Impact: 15.2)
    * *Intent:* /* Select the anchor select ** ----------------- ** ** This will load the node is necessary, if the ...
  * `newParent` **(Type Conversions)** (Impact: 9.8)
    * *Intent:* // Create new or find old sub-anchor // --------------------------------- // // This one is for a ne...
  * `moveBy` **(Type Conversions)** (Impact: 9.3)
    * *Intent:* // Go to next logical step // ----------------------- // // We take the link After or before the one...
  * `equivalent` **(Compute Cores)** (Impact: 7.3)
    * *Intent:* // Case insensitive string comparison // ---------------------------------- // On entry, // s Points...
  * `free` **(Type Conversions)** (Impact: 5.5)
    * *Intent:* // // Free an anchor // --------------
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 14 instances
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 35`, `args: 9`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 26`, `unreferenced_by_name: 10`
* *Architecture:* `io: 2`, `api: 2`, `import: 9`
* *Defense:* `immutability_locks: 6`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Anchor.h, HTParse.h, HTUtils.h, HyperManager.h, HyperText.h, appkit.h, ctype.h, Object.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HTStyle.h` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 116.35 | **LOC:** 78 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **1**; blast radius 119.754; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (89.8%), Debt Markers (formerly Tech Debt) (80.6%), Guard Balance (formerly Safety Score) (75.0%), Complexity Load (formerly Cognitive Load) (4.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 8`, `args: 13`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 15`, `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 119.754
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.236715
  * `Imports (Out-Degree: 0):` appkit.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `HyperText.h` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 93.44 | **LOC:** 95 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **4**; blast radius 86.533; role: Transceiver (Middle-Tier)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 86.533
  * `Choke Point (Betweenness):` 0.008333 | `Ripple Effect (Closeness):` 0.204545
  * `Imports (Out-Degree: 2):` Anchor.h, HTStyle.h, Text.h, List.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `HyperAccess.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 49.48 | **LOC:** 159 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 17.717; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (74.3%), Guard Balance (formerly Safety Score) (66.3%), Complexity Load (formerly Cognitive Load) (14.9%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Anchor.h, HTUtils.h, HyperAccess.h, HyperManager.h, appkit.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `WWWPageLayout.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 45.34 | **LOC:** 133 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 17.717; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (88.7%), Complexity Load (formerly Cognitive Load) (66.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` WWWPageLayout.h, Application.h, Matrix.h, PrintInfo.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Anchor.h` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 40.64 | **LOC:** 58 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **3**; blast radius 118.29; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (98.4%), Guard Balance (formerly Safety Score) (75.3%), Test Surface (formerly Verification) (3.1%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 118.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.235294
  * `Imports (Out-Degree: 0):` appkit.h, List.h, Object.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `TextToy.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 40.3 | **LOC:** 136 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 17.717; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (83.2%), Guard Balance (formerly Safety Score) (67.0%), Complexity Load (formerly Cognitive Load) (17.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Anchor.h, HTUtils.h, HyperText.h, TextToy.h, appkit.h, List.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `TcpAccess.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 36.46 | **LOC:** 109 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 17.717; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (92.4%), Guard Balance (formerly Safety Score) (81.1%), Complexity Load (formerly Cognitive Load) (43.0%)
- **Documentation Coverage:** 84.047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadAnchor` **(Type Conversions)** (Impact: 11.1)
    * *Intent:* // Actions: // This will load an anchor which has a name // // On entry, // Anchor's address is vali...
  * `accessName` **(Many-Argument Workhorses)** (Impact: 10.2)
    * *Intent:* // Open or search by name // -----------------------
  * `name` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* #import "HTUtils.h" #import "HTTP.h" /* Module parameters: ** ----------------- ** ** These may be u...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 9`, `args: 2`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `import: 4`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Anchor.h, HTTP.h, HTUtils.h, TcpAccess.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HyperAccess.h` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 36.32 | **LOC:** 56 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 55.617; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (83.4%), Guard Balance (formerly Safety Score) (75.3%), Test Surface (formerly Verification) (2.8%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 55.617
  * `Choke Point (Betweenness):` 0.004365 | `Ripple Effect (Closeness):` 0.099206
  * `Imports (Out-Degree: 2):` Anchor.h, HyperText.h, List.h, Object.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `HyperManager.h` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 35.42 | **LOC:** 35 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 32.777; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (88.0%), Test Surface (formerly Verification) (2.8%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 32.777
  * `Choke Point (Betweenness):` 0.001587 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 1):` HyperAccess.h, List.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `HTextNeXT.h` (OBJECTIVE-C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 31.24 | **LOC:** 173 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 17.717; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (10.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `func_start: 13`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 15`, `import: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HTAnchor.h, HTStyle.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Features.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `,Features.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `WorldWideWeb_main.m` (OBJECTIVE-C | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 27.44 | **LOC:** 73 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 17.717; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.0%), Debt Markers (formerly Tech Debt) (62.2%), Complexity Load (formerly Cognitive Load) (41.1%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTUtils.h, Application.h, PrintInfo.h, defaults.h, libc.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugs.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Test/backup_of_test.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 17.717
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `HTStyle.h` -> **Severity: 17.754** (Embedded: 0.2367 * Error Risk: 74.9996%)
- `Anchor.h` -> **Severity: 17.716** (Embedded: 0.2353 * Error Risk: 75.2927%)
- `HyperAccess.h` -> **Severity: 7.469** (Embedded: 0.0992 * Error Risk: 75.2927%)
- `WWWPageLayout.h` -> **Severity: 4.431** (Embedded: 0.0556 * Error Risk: 79.7611%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Anchor.h` -> **Severity: 9941.92** (Blast Radius: 118.29 * Doc Risk: 84.047%)
- `HyperText.h` -> **Severity: 7272.839** (Blast Radius: 86.533 * Doc Risk: 84.047%)
- `HyperAccess.h` -> **Severity: 4674.442** (Blast Radius: 55.617 * Doc Risk: 84.047%)
- `WWWPageLayout.h` -> **Severity: 3176.724** (Blast Radius: 37.797 * Doc Risk: 84.047%)
- `HyperManager.h` -> **Severity: 2754.809** (Blast Radius: 32.777 * Doc Risk: 84.047%)

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
