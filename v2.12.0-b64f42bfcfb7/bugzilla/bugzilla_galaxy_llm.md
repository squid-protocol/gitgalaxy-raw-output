# ARCHITECTURAL_BRIEF: bugzilla
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/bugzilla/bugzilla` |
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
- **Scope:** 658 analyzed artifact(s), 107667 LOC.
- **Load-bearing artifact:** `Bugzilla/Constants.pm` -- 151 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `importxml.pl` -- pulls in 33 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Bugzilla/Bug.pm` at magnitude 4038.98 (structural weight, not risk).
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
| Total Artifacts | 927 |
| Analyzed Artifacts (Scanned) | 658 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 269 |
| Total LOC | 107667 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 71.0% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3003 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.277 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.9161 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 16 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 287 | 74371 | 43.6% |
| HTML | 277 | 26882 | 42.1% |
| PLAINTEXT | 30 | 0 | 4.6% |
| JAVASCRIPT | 19 | 2904 | 2.9% |
| CSS | 16 | 2617 | 2.4% |
| MARKDOWN | 9 | 0 | 1.4% |
| SHELL | 7 | 163 | 1.1% |
| CSV | 5 | 138 | 0.8% |
| YAML | 3 | 109 | 0.5% |
| PYTHON | 2 | 423 | 0.3% |
| XML | 2 | 0 | 0.3% |
| DOCKERFILE | 1 | 60 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 658 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 52%, Compute Cores Files 14%, Large Core Modules (3) 12%, Declarative / Non-Code 11%, Parameter Forwarders Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 619 | 94.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 39 | 5.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 269*

**Composition by Extension & Reason:**
- `.rst`: 87x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 50x Excluded (Saturation: Line 7 exceeds 500 chars), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 14 exceeds 500 chars)
- `.png`: 43x Excluded (Explicitly Denied Extension: '.png')
- `.css`: 24x Excluded (Saturation: Line 7 exceeds 500 chars), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 16x Excluded (Explicitly Denied Extension: '.gif')
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.undeterminable)
- `.tmpl`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 16 exceeds 500 chars)
- `.pm`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 51 LOC)
- `.txt`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.conf`: 2x Excluded (Unsupported Extension: '.conf')
- `.cnf`: 2x Excluded (Unsupported Extension: '.cnf')
- `.swf`: 2x Excluded (Unsupported Extension: '.swf')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mariadb`: 1x Excluded (Unsupported Extension: '.mariadb')
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 93.6 | 18.1 | 5.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.6 | 27.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 36.7 | 15.3 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 13.6 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 5.6 | 4.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 79.9 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 24.5 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 38.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1345 | 161 | 4 | `Bugzilla/Bug.pm` |
| cleanup | 122 | 62 | 0 | `contrib/extension-convert.pl` |
| guards | 1057 | 360 | 3 | `template/en/default/global/user-error.html.tmpl` |
| danger | 1026 | 177 | 4 | `js/field.js` |
| concurrency | 15 | 10 | 0 | `Bugzilla/JobQueue.pm` |
| connectivity | 3635 | 379 | 15 | `Bugzilla/Bug.pm` |
| io | 2106 | 289 | 8 | `xt/lib/Bugzilla/Test/Search/Constants.pm` |
| crypto | 0 | 0 | 0 | - |
| ipc | 28 | 19 | 0 | `Bugzilla/Install.pm` |
| time | 186 | 62 | 0 | `Bugzilla/WebService/Bug.pm` |
| serialization | 12 | 3 | 0 | `js/comment-tagging.js` |
| regex | 1717 | 176 | 5 | `Bugzilla/Template.pm` |
| events | 445 | 148 | 2 | `Bugzilla/Migrate/Gnats.pm` |
| tests | 107 | 20 | 0 | `t/002goodperl.t` |
| docs | 374 | 155 | 1 | `Bugzilla/DB/Schema.pm` |
| debt | 4660 | 329 | 15 | `Bugzilla/WebService/Bug.pm` |
| mutation | 20159 | 551 | 73 | `Bugzilla/DB/Schema.pm` |
| dead_code | 395 | 111 | 1 | `extensions/Example/Extension.pm` |
| credential | 51 | 1 | 0 | `docker/startup.sh` |
| threat | 3 | 3 | 0 | `Bugzilla/WebService/Server/XMLRPC.pm` |
| ml_ai | 295 | 40 | 0 | `Bugzilla/WebService/Bug.pm` |
| ui | 740 | 128 | 2 | `template/en/default/global/messages.html.tmpl` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.3063**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `xt/lib/Bugzilla/Test/Search/Constants.pm` (Hits: 90)
- `Bugzilla/WebService/Bug.pm` (Hits: 66)
- `Bugzilla/DB/Schema.pm` (Hits: 63)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Constants.pm** (`Bugzilla/Constants.pm`) — 151 inbound connections
2. **Error.pm** (`Bugzilla/Error.pm`) — 139 inbound connections
3. **Util.pm** (`Bugzilla/Util.pm`) — 132 inbound connections
4. **base.css** (`js/yui/base/base.css`) — 119 inbound connections
5. **User.pm** (`Bugzilla/User.pm`) — 52 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **importxml.pl** (`importxml.pl`) — 33 outbound dependencies
2. **User.pm** (`Bugzilla/User.pm`) — 30 outbound dependencies
3. **Bugzilla.pm** (`Bugzilla.pm`) — 29 outbound dependencies
4. **Bug.pm** (`Bugzilla/Bug.pm`) — 28 outbound dependencies
5. **Template.pm** (`Bugzilla/Template.pm`) — 28 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_convert_attachment_statuses_to_flags` **(Many-Argument Workhorses)** (@ `Bugzilla/Install/DB.pm`) -> Impact: **1126.1** | LOC: 1754
- `bz_setup_database` **(Many-Argument Workhorses)** (@ `Bugzilla/DB/MariaDB.pm`) -> Impact: **970.9** | LOC: 993
- `bz_setup_database` **(Many-Argument Workhorses)** (@ `Bugzilla/DB/Mysql.pm`) -> Impact: **966.4** | LOC: 993
- `_add_unique_login_name_index_to_profiles` **(Many-Argument Workhorses)** (@ `Bugzilla/Install/DB.pm`) -> Impact: **756.4** | LOC: 1753
- `_update_bugs_activity_to_only_record_changes` **(Many-Argument Workhorses)** (@ `Bugzilla/Install/DB.pm`) -> Impact: **746.2** | LOC: 1746
- `process_bug` **(Many-Argument Workhorses)** (@ `importxml.pl`) -> Impact: **465.8** | LOC: 864
  * *Intent:* # This subroutine will be called once for each <bug> in the xml file. # It is called as soon as the closing </bug> tag is parsed. # If this bug had an...
- `create` **(Many-Argument Workhorses)** (@ `Bugzilla/Template.pm`) -> Impact: **462.1** | LOC: 499
  * *Intent:* # Construct the Template object # Note that all of the failure cases here can't use templateable errors, # since we won't have a template to use...
- `update` **(Many-Argument Workhorses)** (@ `Bugzilla/Bug.pm`) -> Impact: **203.9** | LOC: 336
- `Send` **(Many-Argument Workhorses)** (@ `Bugzilla/BugMail.pm`) -> Impact: **147.4** | LOC: 268
  * *Intent:* # changer, owner, qa, reporter, cc # Optional hash contains values of people which will be forced to those # roles when the email is sent. # All the n...
- `notify` **(Many-Argument Workhorses)** (@ `Bugzilla/Flag.pm`) -> Impact: **130.8** | LOC: 117

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Bugzilla` | 45 | 19880.5 | 36.9% | 49.24% |
| `__monolith__` | 71 | 8992.38 | 45.88% | 33.54% |
| `Bugzilla/Install` | 6 | 5283.2 | 34.48% | 19.29% |
| `Bugzilla/DB` | 7 | 4745.92 | 43.29% | 41.75% |
| `js` | 14 | 2486.62 | 55.07% | 78.03% |
| `template/en/default/bug` | 20 | 2328.38 | 2.32% | 74.42% |
| `Bugzilla/WebService` | 13 | 2266.82 | 20.65% | 35.15% |
| `template/en/default/search` | 12 | 1638.27 | 4.99% | 24.27% |
| `Bugzilla/DB/Schema` | 5 | 1262.46 | 62.26% | 18.55% |
| `template/en/default/attachment` | 14 | 967.09 | 0.88% | 72.93% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Bugzilla/BugUrl/Bugzilla/Local.pm` -> **100.0%** Exposure
- `Bugzilla/BugUrl/Debian.pm` -> **100.0%** Exposure
- `Bugzilla/BugUrl/Launchpad.pm` -> **100.0%** Exposure
- `Bugzilla/Field/ChoiceInterface.pm` -> **100.0%** Exposure
- `Bugzilla/Flag.pm` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Bugzilla/Chart.pm` -> **100.0%** Exposure
- `Bugzilla/DB/Schema/Oracle.pm` -> **100.0%** Exposure
- `Bugzilla/Migrate/Gnats.pm` -> **100.0%** Exposure
- `Bugzilla/User/Setting/Skin.pm` -> **100.0%** Exposure
- `Bugzilla/User/Setting/Timezone.pm` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `extensions/Example/Extension.pm` -> **68** Orphaned Functions | **0** Duplicates
- `js/field.js` -> **20** Orphaned Functions | **0** Duplicates
- `extensions/Voting/Extension.pm` -> **17** Orphaned Functions | **0** Duplicates
- `js/attachment.js` -> **15** Orphaned Functions | **0** Duplicates
- `Bugzilla/DB/Schema.pm` -> **14** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `docker/startup.sh` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `10` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2484` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Bugzilla/Bug.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.989)
- **Top Global Matches:** file_cluster_4: 6.989, file_cluster_6: 11.684, file_cluster_15: 11.782
- **Magnitude:** 4038.98 | **LOC:** 5124 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); it depends on **28**; blast radius 5.837; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Many-Argument Workhorses)** (Impact: 203.9)
  * `get_activity` **(Many-Argument Workhorses)** (Impact: 129.2)
    * *Intent:* # Get the activity of a bug, starting from $starttime (if given). # This routine assumes Bugzilla::B...
  * `_check_bug_status` **(Many-Argument Workhorses)** (Impact: 76.7)
  * `create` **(Many-Argument Workhorses)** (Impact: 71.2)
    * *Intent:* # C<status_whiteboard> - A string. # C<bug_status> - The initial status of the bug, a string. # C<bu...
  * `check_can_change_field` **(Compute Cores)** (Impact: 69.0)
    * *Intent:* # can add code here for site-specific policy changes, according to the # instructions given in the B...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 437 instances
* *Memory Alloc (weighted view):* 83
* *State Mutation (weighted view):* 1350
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1072`, `structural_boundaries: 1524`, `args: 153`, `func_start: 194`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 476`, `fragile_debt: 215`, `unreferenced_by_name: 1`
* *Architecture:* `api: 138`, `import: 40`
* *Defense:* `safety: 10`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.837
  * `Choke Point (Betweenness):` 0.003011 | `Ripple Effect (Closeness):` 0.091081
  * `Imports (Out-Degree: 21):` Bugzilla::Attachment, Bugzilla::BugMail, Bugzilla::BugUrl, Bugzilla::BugUserLastVisit, Bugzilla::Comment, Bugzilla::Component, Bugzilla::Constants, Bugzilla::Error...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `Bugzilla/Install/DB.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.271)
- **Top Global Matches:** file_cluster_6: 7.271, file_cluster_4: 9.378, file_cluster_15: 16.788
- **Magnitude:** 3936.76 | **LOC:** 4300 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.7%), Mutation Surface (formerly State Flux) (95.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_convert_attachment_statuses_to_flags` **(Many-Argument Workhorses)** (Impact: 1126.1)
  * `_add_unique_login_name_index_to_profiles` **(Many-Argument Workhorses)** (Impact: 756.4)
  * `_update_bugs_activity_to_only_record_changes` **(Many-Argument Workhorses)** (Impact: 746.2)
  * `_convert_groups_system_from_groupset` **(I/O & Config Routines)** (Impact: 54.5)
  * `_initialize_workflow_for_upgrade` **(Compute Cores)** (Impact: 53.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 129 instances
* *Memory Alloc (weighted view):* 49
* *State Mutation (weighted view):* 403
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 623`, `structural_boundaries: 852`, `args: 8`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `state_mutation: 145`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 134`
* *Architecture:* `io: 2`, `api: 2`, `import: 22`
* *Defense:* `safety: 5`, `doc: 1`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.001522
  * `Imports (Out-Degree: 8):` Bugzilla::BugUrl, Bugzilla::Constants, Bugzilla::Field, Bugzilla::Hook, Bugzilla::Install, Bugzilla::Install::Util, Bugzilla::Series, Bugzilla::Util...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Bugzilla/Search.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.945)
- **Top Global Matches:** file_cluster_4: 5.945, file_cluster_15: 8.461, file_cluster_16: 9.963
- **Magnitude:** 2056.28 | **LOC:** 3562 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **25**; blast radius 2.093; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.6%), Complexity Load (formerly Cognitive Load) (62.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_multiselect_isempty` **(Many-Argument Workhorses)** (Impact: 62.6)
    * *Intent:* # We can't use the normal operator_functions to build isempty queries which # join to different tabl...
  * `SqlifyDate` **(Compute Cores)** (Impact: 58.7)
  * `_user_nonchanged` **(Many-Argument Workhorses)** (Impact: 49.9)
    * *Intent:* # For all the "user" fields--assigned_to, reporter, qa_contact, # cc, commenter, requestee, etc.
  * `_multiselect_table` **(Compute Cores)** (Impact: 34.2)
  * `_special_parse_chfield` **(Compute Cores)** (Impact: 34.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 249 instances
* *State Mutation (weighted view):* 817
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 526`, `structural_boundaries: 1117`, `args: 126`, `func_start: 132`, `class_start: 1`
* *Risk/State:* `state_mutation: 319`, `planned_debt: 2`, `fragile_debt: 21`
* *Architecture:* `io: 4`, `api: 17`, `import: 41`
* *Defense:* `safety: 2`, `doc: 1`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.093
  * `Choke Point (Betweenness):` 0.001493 | `Ripple Effect (Closeness):` 0.062494
  * `Imports (Out-Degree: 13):` Bugzilla::Constants, Bugzilla::Error, Bugzilla::Field, Bugzilla::Group, Bugzilla::Keyword, Bugzilla::Search::Clause, Bugzilla::Search::ClauseGroup, Bugzilla::Search::Condition...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `Bugzilla/User.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.128)
- **Top Global Matches:** file_cluster_4: 6.128, file_cluster_6: 10.113, file_cluster_15: 11.593
- **Magnitude:** 1903.5 | **LOC:** 3408 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **52** in-repo importer(s); it depends on **30**; blast radius 10.787; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (65.8%), Guard Balance (formerly Safety Score) (60.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `match_field` **(Many-Argument Workhorses)** (Impact: 112.3)
  * `wants_bug_mail` **(Many-Argument Workhorses)** (Impact: 77.7)
    * *Intent:* # Returns true if the user wants mail for a given bug change.
  * `match` **(Many-Argument Workhorses)** (Impact: 48.6)
  * `validate_password_check` **(Compute Cores)** (Impact: 48.4)
  * `can_enter_product` **(Many-Argument Workhorses)** (Impact: 44.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 156 instances
* *State Mutation (weighted view):* 495
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 727`, `structural_boundaries: 788`, `args: 110`, `func_start: 116`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 183`, `planned_debt: 1`, `fragile_debt: 49`
* *Architecture:* `io: 19`, `api: 105`, `import: 55`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.787
  * `Choke Point (Betweenness):` 0.008045 | `Ripple Effect (Closeness):` 0.114921
  * `Imports (Out-Degree: 20):` Bugzilla::Auth, Bugzilla::BugMail, Bugzilla::BugUserLastVisit, Bugzilla::Classification, Bugzilla::Component, Bugzilla::Constants, Bugzilla::Error, Bugzilla::Field...
  * `Imported By (In-Degree: 52):` (Excluded from Brief to save tokens)

### `importxml.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.508)
- **Top Global Matches:** file_cluster_8: 9.508, file_cluster_3: 15.84, file_cluster_6: 21.481
- **Magnitude:** 1555.5 | **LOC:** 1399 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.862; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Complexity Load (formerly Cognitive Load) (93.6%), Guard Balance (formerly Safety Score) (82.9%)
- **Documentation Coverage:** 65.9205% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_bug` **(Many-Argument Workhorses)** (Impact: 465.8)
    * *Intent:* # This subroutine will be called once for each <bug> in the xml file. # It is called as soon as the ...
  * `flag_handler` **(Many-Argument Workhorses)** (Impact: 119.6)
    * *Intent:* # This subroutine handles flags for process_bug. It is generic in that # it can handle both attachme...
  * `process_attachment` **(Compute Cores)** (Impact: 34.7)
    * *Intent:* # Parse attachments. # # This subroutine is called once for each attachment in the xml file. # It is...
  * `init` **(Compute Cores)** (Impact: 13.2)
    * *Intent:* ############################################################################### # XML Handlers # ###...
  * `MailMessage` **(Compute Cores)** (Impact: 12.8)
    * *Intent:* ############################################################################### # Helper sub routine...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 283 instances
* *High Risk Execution (weighted view):* 2
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 863
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 269`, `args: 11`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 297`, `fragile_debt: 92`
* *Architecture:* `io: 7`, `api: 7`, `import: 37`
* *Defense:* `safety: 8`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.862
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` Bugzilla, Bugzilla::Attachment, Bugzilla::Bug, Bugzilla::BugMail, Bugzilla::Component, Bugzilla::Constants, Bugzilla::Field, Bugzilla::FlagType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB/MariaDB.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.418)
- **Top Global Matches:** file_cluster_4: 6.418, file_cluster_15: 9.113, file_cluster_16: 10.472
- **Magnitude:** 1427.74 | **LOC:** 1301 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.862; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (76.8%), Complexity Load (formerly Cognitive Load) (68.2%)
- **Documentation Coverage:** 90.1639% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bz_setup_database` **(Many-Argument Workhorses)** (Impact: 970.9)
  * `_fix_defaults` **(Compute Cores)** (Impact: 26.7)
    * *Intent:* # When you import a MySQL 3/4 mysqldump into MySQL 5, columns that # aren't supposed to have default...
  * `BUILDARGS` **(Compute Cores)** (Impact: 23.9)
  * `sql_fulltext_search` **(Many-Argument Workhorses)** (Impact: 23.7)
  * `bz_index_info_real` **(Many-Argument Workhorses)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 293`, `args: 31`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 58`, `fragile_debt: 12`, `unreferenced_by_name: 2`
* *Architecture:* `io: 6`, `api: 28`, `import: 16`
* *Defense:* `safety: 1`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.862
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Bugzilla::Config, Bugzilla::Constants, Bugzilla::DB::Schema::MariaDB, Bugzilla::Error, Bugzilla::Install::Util, Bugzilla::Util, Carp, List::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB/Mysql.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.317)
- **Top Global Matches:** file_cluster_4: 6.317, file_cluster_15: 9.056, file_cluster_16: 10.493
- **Magnitude:** 1421.44 | **LOC:** 1301 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.862; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (76.8%), Complexity Load (formerly Cognitive Load) (68.0%)
- **Documentation Coverage:** 90.1639% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bz_setup_database` **(Many-Argument Workhorses)** (Impact: 966.4)
  * `_fix_defaults` **(Compute Cores)** (Impact: 26.7)
    * *Intent:* # When you import a MySQL 3/4 mysqldump into MySQL 5, columns that # aren't supposed to have default...
  * `BUILDARGS` **(Compute Cores)** (Impact: 23.9)
  * `sql_fulltext_search` **(Many-Argument Workhorses)** (Impact: 23.7)
  * `bz_index_info_real` **(Many-Argument Workhorses)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 293`, `args: 31`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 58`, `fragile_debt: 12`, `unreferenced_by_name: 2`
* *Architecture:* `io: 6`, `api: 28`, `import: 16`
* *Defense:* `safety: 1`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.862
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Bugzilla::Config, Bugzilla::Constants, Bugzilla::DB::Schema::Mysql, Bugzilla::Error, Bugzilla::Install::Util, Bugzilla::Util, Carp, List::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `template/en/default/bug/edit.html.tmpl` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.152)
- **Top Global Matches:** file_cluster_2: 5.152, file_cluster_13: 5.661, file_cluster_17: 6.252
- **Magnitude:** 1204.87 | **LOC:** 1253 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (50.5%), Mutation Surface (formerly State Flux) (13.4%), Connectivity (formerly Api Exposure) (12.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 51`, `args: 157`, `func_start: 12`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 7`, `fragile_debt: 229`
* *Architecture:* `io: 54`, `api: 100`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.862
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Template.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.963)
- **Top Global Matches:** file_cluster_4: 7.963, file_cluster_6: 10.973, file_cluster_9: 11.841
- **Magnitude:** 1140.1 | **LOC:** 1439 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **28**; blast radius 1.32; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create` **(Many-Argument Workhorses)** (Impact: 462.1)
    * *Intent:* # Construct the Template object # Note that all of the failure cases here can't use templateable err...
  * `quoteUrls` **(Many-Argument Workhorses)** (Impact: 115.0)
    * *Intent:* # This routine quoteUrls contains inspirations from the HTML::FromText CPAN # module by Gareth Rees ...
  * `get_format` **(Many-Argument Workhorses)** (Impact: 24.3)
  * `get_attachment_link` **(Many-Argument Workhorses)** (Impact: 24.1)
    * *Intent:* # Creates a link to an attachment, including its title.
  * `_concatenate_js` **(Compute Cores)** (Impact: 22.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 295
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 252`, `structural_boundaries: 401`, `args: 45`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 107`, `planned_debt: 1`, `fragile_debt: 36`
* *Architecture:* `io: 3`, `api: 14`, `import: 33`
* *Defense:* `safety: 5`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.32
  * `Choke Point (Betweenness):` 0.000161 | `Ripple Effect (Closeness):` 0.004566
  * `Imports (Out-Degree: 14):` Bugzilla::Bug, Bugzilla::Classification, Bugzilla::Constants, Bugzilla::Error, Bugzilla::Hook, Bugzilla::Install::Requirements, Bugzilla::Install::Util, Bugzilla::Keyword...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Bugzilla/Flag.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.465)
- **Top Global Matches:** file_cluster_6: 6.465, file_cluster_4: 9.851, file_cluster_8: 16.02
- **Magnitude:** 997.42 | **LOC:** 1310 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **16**; blast radius 2.759; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.6%)
- **Documentation Coverage:** 68.1159% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `notify` **(Many-Argument Workhorses)** (Impact: 130.8)
  * `extract_flags_from_cgi` **(Many-Argument Workhorses)** (Impact: 117.3)
  * `set_flag` **(Many-Argument Workhorses)** (Impact: 79.3)
    * *Intent:* ###################################################################### # Creating and Modifying ####...
  * `_check_requestee` **(Many-Argument Workhorses)** (Impact: 75.7)
  * `multi_extract_flags_from_cgi` **(Many-Argument Workhorses)** (Impact: 68.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 67 instances
* *Memory Alloc (weighted view):* 17
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 305`, `structural_boundaries: 311`, `args: 29`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 71`, `fragile_debt: 94`, `unreferenced_by_name: 1`
* *Architecture:* `api: 31`, `import: 24`
* *Defense:* `safety: 8`, `doc: 10`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.759
  * `Choke Point (Betweenness):` 0.001029 | `Ripple Effect (Closeness):` 0.088722
  * `Imports (Out-Degree: 11):` Bugzilla::Attachment, Bugzilla::Bug, Bugzilla::Constants, Bugzilla::Error, Bugzilla::Field, Bugzilla::FlagType, Bugzilla::Hook, Bugzilla::Mailer...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `Bugzilla/WebService/Bug.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.815)
- **Top Global Matches:** file_cluster_6: 7.815, file_cluster_8: 12.477, file_cluster_4: 14.294
- **Magnitude:** 978.86 | **LOC:** 4693 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 1.253; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (96.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_bug_to_hash` **(Many-Argument Workhorses)** (Impact: 83.5)
    * *Intent:* ############################## # Private Helper Subroutines # ############################## # A hel...
  * `search` **(Many-Argument Workhorses)** (Impact: 52.3)
  * `_legal_field_values` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `update_attachment` **(I/O & Config Routines)** (Impact: 30.8)
  * `update_comment_tags` **(Compute Cores)** (Impact: 26.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 133 instances
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 420
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 581`, `structural_boundaries: 643`, `args: 16`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 154`, `fragile_debt: 447`
* *Architecture:* `io: 66`, `api: 19`, `import: 58`
* *Defense:* `safety: 5`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.253
  * `Choke Point (Betweenness):` 0.000192 | `Ripple Effect (Closeness):` 0.002283
  * `Imports (Out-Degree: 19):` Bugzilla::Bug, Bugzilla::BugMail, Bugzilla::Comment, Bugzilla::Comment::TagWeights, Bugzilla::Constants, Bugzilla::Error, Bugzilla::Field, Bugzilla::FlagType...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Bugzilla/DB/Schema.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.176)
- **Top Global Matches:** file_cluster_4: 7.176, file_cluster_15: 8.407, file_cluster_9: 8.989
- **Magnitude:** 916.76 | **LOC:** 3189 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **14**; blast radius 1.326; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (74.5%), Guard Balance (formerly Safety Score) (53.9%), Debt Markers (formerly Tech Debt) (29.4%)
- **Documentation Coverage:** 72.2892% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_alter_column_ddl` **(Many-Argument Workhorses)** (Impact: 93.1)
  * `get_type_ddl` **(Compute Cores)** (Impact: 35.5)
    * *Intent:* #--------------------------------------------------------------------------
  * `_set_nulls_sql` **(Many-Argument Workhorses)** (Impact: 32.9)
    * *Intent:* # Helps handle any fields that were NULL before, if we have a default, # when doing an ALTER COLUMN.
  * `deserialize_abstract` **(Compute Cores)** (Impact: 23.5)
  * `get_table_ddl` **(Compute Cores)** (Impact: 22.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 208
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 318`, `structural_boundaries: 337`, `args: 48`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `state_mutation: 74`, `planned_debt: 3`, `fragile_debt: 7`, `unreferenced_by_name: 14`
* *Architecture:* `io: 63`, `api: 37`, `import: 31`
* *Defense:* `safety: 5`, `doc: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.326
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.004756
  * `Imports (Out-Degree: 4):` Bugzilla::Constants, Bugzilla::Error, Bugzilla::Hook, Bugzilla::Util, Carp, Data::Dumper, Digest::MD5, Hash::Util...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Bugzilla/DB.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.44)
- **Top Global Matches:** file_cluster_15: 5.44, file_cluster_11: 7.855, file_cluster_16: 7.946
- **Magnitude:** 820.4 | **LOC:** 3011 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **18**; blast radius 1.137; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (76.5%), Guard Balance (formerly Safety Score) (54.0%), Complexity Load (formerly Cognitive Load) (17.9%)
- **Documentation Coverage:** 97.8873% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bz_check_server_version` **(Many-Argument Workhorses)** (Impact: 37.0)
  * `bz_add_column` **(Many-Argument Workhorses)** (Impact: 29.3)
    * *Intent:* ##################################################################### # Schema Modification Methods ...
  * `_check_references` **(Many-Argument Workhorses)** (Impact: 26.7)
    * *Intent:* # This is used before adding a foreign key to a column, to make sure # that the database won't fail ...
  * `bz_add_fks` **(Many-Argument Workhorses)** (Impact: 19.4)
  * `bz_alter_column_raw` **(Many-Argument Workhorses)** (Impact: 19.2)
    * *Intent:* # object but you need to alter a column, for some reason. # (2) You need to alter a column for some ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 339`, `structural_boundaries: 519`, `args: 74`, `func_start: 78`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 57`, `fragile_debt: 5`, `unreferenced_by_name: 2`
* *Architecture:* `io: 23`, `api: 61`, `import: 38`
* *Defense:* `safety: 10`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.000126 | `Ripple Effect (Closeness):` 0.004566
  * `Imports (Out-Degree: 10):` Bugzilla::Constants, Bugzilla::DB::QuoteIdentifier, Bugzilla::DB::Schema, Bugzilla::Error, Bugzilla::Install::Localconfig, Bugzilla::Install::Requirements, Bugzilla::Install::Util, Bugzilla::Mailer...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `template/en/default/bug/create/create.html.tmpl` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.43)
- **Top Global Matches:** file_cluster_2: 4.43, file_cluster_13: 5.035, file_cluster_17: 5.588
- **Magnitude:** 766.0 | **LOC:** 673 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (49.3%), Mutation Surface (formerly State Flux) (13.4%), Connectivity (formerly Api Exposure) (11.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 19`, `args: 102`, `func_start: 5`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `fragile_debt: 52`
* *Architecture:* `io: 4`, `api: 39`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.862
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `template/en/default/search/form.html.tmpl` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.538)
- **Top Global Matches:** file_cluster_13: 5.538, file_cluster_2: 5.635, file_cluster_17: 6.496
- **Magnitude:** 722.9 | **LOC:** 340 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.6%), Debt Markers (formerly Tech Debt) (35.8%), Mutation Surface (formerly State Flux) (20.1%), Connectivity (formerly Api Exposure) (12.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 33`, `args: 73`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 4`, `fragile_debt: 4`
* *Architecture:* `io: 6`, `api: 36`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.862
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/field.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.052)
- **Top Global Matches:** file_cluster_12: 7.052, file_cluster_7: 8.612, file_cluster_5: 9.953
- **Magnitude:** 692.48 | **LOC:** 1117 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (81.6%), Guard Balance (formerly Safety Score) (72.3%), Complexity Load (formerly Cognitive Load) (54.1%)
- **Documentation Coverage:** 85.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `showEditableField` **(Compute Cores)** (Impact: 26.2)
    * *Intent:* /* showEditableField (e, ContainerInputArray) * Function hides the (edit) link and the text and disp...
  * `setFieldFromCalendar` **(Many-Argument Workhorses)** (Impact: 25.9)
    * *Intent:* /* This is the selectEvent for our Calendar objects on our custom * DateTime fields. */
  * `validateEnterBug` **(Compute Cores)** (Impact: 23.0)
  * `showHideStatusItems` **(Compute Cores)** (Impact: 21.2)
  * `handleVisControllerValueChange` **(Compute Cores)** (Impact: 20.4)
    * *Intent:* /** * Called by showFieldWhen when a field's visibility controller * changes values. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 266
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 176`, `args: 58`, `func_start: 54`
* *Risk/State:* `safety_bypasses: 35`, `high_risk_execution: 5`, `state_mutation: 112`, `fragile_debt: 1`, `unreferenced_by_name: 20`
* *Architecture:* None
* *Defense:* `safety: 6`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.862
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Object.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.144)
- **Top Global Matches:** file_cluster_4: 6.144, file_cluster_15: 10.261, file_cluster_9: 10.877
- **Magnitude:** 687.88 | **LOC:** 1595 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.908; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.2%), Complexity Load (formerly Cognitive Load) (36.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `match` **(Compute Cores)** (Impact: 46.9)
    * *Intent:* # * Add a MATCH_JOIN constant so that we can join against # certain other tables for the WHERE crite...
  * `_do_list_select` **(Many-Argument Workhorses)** (Impact: 37.9)
  * `update` **(Compute Cores)** (Impact: 36.1)
  * `_load_from_db` **(Compute Cores)** (Impact: 29.2)
    * *Intent:* # Bugzilla::Object, make sure that you modify bz_setup_database # in Bugzilla::DB::Pg appropriately,...
  * `new` **(Compute Cores)** (Impact: 26.3)
    * *Intent:* ############################### #### Initialization #### ###############################
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 54 instances
* *Memory Alloc (weighted view):* 10
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 301`, `structural_boundaries: 552`, `args: 44`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `state_mutation: 61`, `planned_debt: 4`, `fragile_debt: 6`
* *Architecture:* `io: 37`, `api: 26`, `import: 34`
* *Defense:* `safety: 7`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.908
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001522
  * `Imports (Out-Degree: 4):` Bugzilla::Constants, Bugzilla::Error, Bugzilla::Hook, Bugzilla::Util, Date::Parse, List::MoreUtils, Scalar::Util, constant...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `xt/lib/Bugzilla/Test/Search.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.143)
- **Top Global Matches:** file_cluster_4: 7.143, file_cluster_15: 7.482, file_cluster_11: 9.261
- **Magnitude:** 679.82 | **LOC:** 1032 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 1.229; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.1%), Complexity Load (formerly Cognitive Load) (45.3%), Connectivity (formerly Api Exposure) (9.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_create_one_bug` **(Many-Argument Workhorses)** (Impact: 89.8)
    * *Intent:* ################ # Bug Creation # ################
  * `_create_field_values` **(Many-Argument Workhorses)** (Impact: 61.0)
    * *Intent:* ######################## # Field Value Creation # ########################
  * `_get_attach_values` **(Compute Cores)** (Impact: 27.2)
    * *Intent:* # Attachments
  * `_get_flag_values` **(Many-Argument Workhorses)** (Impact: 14.7)
  * `_create_flagtypes` **(Compute Cores)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 267
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 378`, `args: 39`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `state_mutation: 101`, `fragile_debt: 95`, `unreferenced_by_name: 4`
* *Architecture:* `api: 27`, `import: 19`
* *Defense:* `safety: 3`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.229
  * `Choke Point (Betweenness):` 0.000135 | `Ripple Effect (Closeness):` 0.001522
  * `Imports (Out-Degree: 14):` Bugzilla::Attachment, Bugzilla::Bug, Bugzilla::Constants, Bugzilla::Field, Bugzilla::Field::Choice, Bugzilla::FlagType, Bugzilla::Group, Bugzilla::Install...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Bugzilla/Util.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.559)
- **Top Global Matches:** file_cluster_4: 7.559, file_cluster_15: 8.302, file_cluster_11: 9.706
- **Magnitude:** 676.56 | **LOC:** 1361 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **132** in-repo importer(s); it depends on **21**; blast radius 39.05; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.7%), Complexity Load (formerly Cognitive Load) (56.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `datetime_from` **(Compute Cores)** (Impact: 36.3)
  * `diff_arrays` **(Compute Cores)** (Impact: 36.0)
  * `format_time` **(Compute Cores)** (Impact: 29.3)
  * `join_activity_entries` **(Compute Cores)** (Impact: 25.6)
  * `html_light_quote` **(Compute Cores)** (Impact: 21.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 69 instances
* *Memory Alloc (weighted view):* 11
* *State Mutation (weighted view):* 219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 279`, `structural_boundaries: 320`, `args: 32`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `state_mutation: 81`, `fragile_debt: 3`
* *Architecture:* `io: 4`, `api: 43`, `import: 31`
* *Defense:* `safety: 3`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 39.05
  * `Choke Point (Betweenness):` 0.000701 | `Ripple Effect (Closeness):` 0.23033
  * `Imports (Out-Degree: 4):` Bugzilla::Constants, Bugzilla::Error, Bugzilla::RNG, Carp, Date::Format, Date::Parse, DateTime, Digest...
  * `Imported By (In-Degree: 132):` (Excluded from Brief to save tokens)

### `Bugzilla/Migrate.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.054)
- **Top Global Matches:** file_cluster_4: 7.054, file_cluster_15: 8.19, file_cluster_11: 9.782
- **Magnitude:** 582.1 | **LOC:** 1249 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **22**; blast radius 1.596; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `insert_bugs` **(Many-Argument Workhorses)** (Impact: 64.3)
  * `create_legal_values` **(Compute Cores)** (Impact: 41.3)
  * `translate_value` **(Many-Argument Workhorses)** (Impact: 20.1)
  * `_generate_description` **(Compute Cores)** (Impact: 16.7)
  * `translate_bug` **(Compute Cores)** (Impact: 15.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 359`, `args: 35`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 67`, `planned_debt: 3`, `fragile_debt: 80`
* *Architecture:* `io: 5`, `api: 32`, `import: 28`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.596
  * `Choke Point (Betweenness):` 0.000116 | `Ripple Effect (Closeness):` 0.001522
  * `Imports (Out-Degree: 12):` Bugzilla::Attachment, Bugzilla::Bug, Bugzilla::Component, Bugzilla::Constants, Bugzilla::Error, Bugzilla::Install::Requirements, Bugzilla::Install::Util, Bugzilla::Product...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Bugzilla/Migrate/Gnats.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.405)
- **Top Global Matches:** file_cluster_4: 7.405, file_cluster_6: 8.235, file_cluster_15: 13.8
- **Magnitude:** 552.9 | **LOC:** 749 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.862; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_parse_audit_trail` **(Many-Argument Workhorses)** (Impact: 54.4)
  * `_parse_attachments` **(Compute Cores)** (Impact: 42.0)
  * `translate_value` **(Many-Argument Workhorses)** (Impact: 39.7)
  * `_get_gnats_field_data` **(Compute Cores)** (Impact: 29.4)
  * `translate_bug` **(Compute Cores)** (Impact: 18.3)
    * *Intent:* #################### # Translating Bugs # ####################
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 166`, `args: 19`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 94`, `fragile_debt: 27`, `unreferenced_by_name: 3`
* *Architecture:* `io: 4`, `api: 8`, `import: 25`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.862
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Bugzilla::Constants, Bugzilla::Install::Util, Bugzilla::Util, Email::Address::XS, Email::MIME, File::Basename, IO::File, List::MoreUtils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/Example/Extension.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.372)
- **Top Global Matches:** file_cluster_15: 5.372, file_cluster_11: 7.588, file_cluster_16: 8.143
- **Magnitude:** 539.76 | **LOC:** 1117 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.862; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.9%), Complexity Load (formerly Cognitive Load) (29.8%), Connectivity (formerly Api Exposure) (12.1%), Dead Code Surface (formerly Dead Code) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bug_check_can_change_field` **(Compute Cores)** (Impact: 22.8)
  * `email_in_after_parse` **(Compute Cores)** (Impact: 17.2)
  * `bug_start_of_update` **(Compute Cores)** (Impact: 13.9)
  * `bug_end_of_update` **(Compute Cores)** (Impact: 13.9)
  * `error_catch` **(Compute Cores)** (Impact: 13.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 382`, `args: 73`, `func_start: 72`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 57`, `dead_code: 3`, `fragile_debt: 50`, `unreferenced_by_name: 68`
* *Architecture:* `api: 69`, `import: 15`
* *Defense:* `safety: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.862
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Bugzilla::Constants, Bugzilla::Error, Bugzilla::Extension::Example::Util, Bugzilla::Group, Bugzilla::Install::Filesystem, Bugzilla::Status, Bugzilla::User, Bugzilla::User::Setting...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB/Oracle.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.503)
- **Top Global Matches:** file_cluster_15: 7.503, file_cluster_4: 7.709, file_cluster_16: 9.425
- **Magnitude:** 532.12 | **LOC:** 883 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.862; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.2%), Complexity Load (formerly Cognitive Load) (62.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bz_setup_database` **(Compute Cores)** (Impact: 41.8)
    * *Intent:* ##################################################################### # Custom Database Setup ######...
  * `adjust_statement` **(Compute Cores)** (Impact: 29.7)
  * `BUILDARGS` **(Compute Cores)** (Impact: 13.2)
  * `selectall_arrayref` **(Type Conversions)** (Impact: 13.1)
  * `sql_in` **(Compute Cores)** (Impact: 11.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 307`, `args: 54`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `state_mutation: 65`, `fragile_debt: 2`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 39`, `import: 15`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.862
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Bugzilla::Constants, Bugzilla::Error, Bugzilla::Util, DBD::Oracle, List::Util, Moo, base, constant...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Product.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.7)
- **Top Global Matches:** file_cluster_4: 6.7, file_cluster_15: 8.27, file_cluster_11: 9.327
- **Magnitude:** 509.08 | **LOC:** 1186 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **19**; blast radius 4.914; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.6%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (65.0%), Guard Balance (formerly Safety Score) (57.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Compute Cores)** (Impact: 55.2)
  * `set_group_controls` **(Many-Argument Workhorses)** (Impact: 37.3)
  * `remove_from_db` **(Compute Cores)** (Impact: 21.6)
  * `groups_available` **(Compute Cores)** (Impact: 19.6)
  * `group_controls` **(Compute Cores)** (Impact: 18.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 313`, `args: 28`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 51`, `planned_debt: 1`, `fragile_debt: 17`
* *Architecture:* `io: 5`, `api: 32`, `import: 32`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.914
  * `Choke Point (Betweenness):` 0.002097 | `Ripple Effect (Closeness):` 0.096469
  * `Imports (Out-Degree: 15):` Bugzilla::Bug, Bugzilla::Component, Bugzilla::Constants, Bugzilla::Error, Bugzilla::Field, Bugzilla::FlagType, Bugzilla::Group, Bugzilla::Hook...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `buglist.cgi` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.284)
- **Top Global Matches:** file_cluster_15: 7.284, file_cluster_11: 7.979, file_cluster_16: 8.187
- **Magnitude:** 508.28 | **LOC:** 1166 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.862; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Complexity Load (formerly Cognitive Load) (77.7%), Guard Balance (formerly Safety Score) (76.3%)
- **Documentation Coverage:** 65.9205% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetGroups` **(Compute Cores)** (Impact: 14.1)
    * *Intent:* # Return groups available for at least one product of the buglist.
  * `InsertNamedQuery` **(Compute Cores)** (Impact: 11.1)
    * *Intent:* # query_name - A string that names the new Named Query, or the name # of an old Named Query to updat...
  * `DiffDate` **(Compute Cores)** (Impact: 10.7)
    * *Intent:* ################################################################################ # Utilities #######...
  * `LookupNamedQuery` **(Compute Cores)** (Impact: 9.4)
  * `_get_common_flag_types` **(Compute Cores)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 137 instances
* *State Mutation (weighted view):* 426
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 190`, `args: 6`, `func_start: 7`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 152`, `fragile_debt: 64`
* *Architecture:* `api: 6`, `import: 18`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.862
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` Apache2::RequestUtil, Bugzilla, Bugzilla::Bug, Bugzilla::Constants, Bugzilla::Error, Bugzilla::Field, Bugzilla::Product, Bugzilla::Search...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `t/Support/Files.pm` (PERL) | Magnitude: 23.02 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 22, indent_spaces: 17, branch: 10, globals: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `js/bug.js` (JAVASCRIPT) | Magnitude: 160.5 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 194, core_var_decl: 36, design_snake_case: 35, structural_boundaries: 34
- `js/custom-search.js` (JAVASCRIPT) | Magnitude: 199.86 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 209, structural_boundaries: 83, core_var_decl: 70, design_snake_case: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `template/en/default/account/prefs/apikey.html.tmpl` (HTML) | Magnitude: 85.02 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 56, core_var_decl: 19, design_snake_case: 19, args: 12
- `template/en/default/bug/navigate.html.tmpl` (HTML) | Magnitude: 16.26 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 56, core_var_decl: 20, design_snake_case: 20, io: 18
- `template/en/default/admin/params/editparams.html.tmpl` (HTML) | Magnitude: 23.8 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 76, core_var_decl: 32, design_snake_case: 32, args: 16
- `template/en/default/admin/milestones/confirm-delete.html.tmpl` (HTML) | Magnitude: 22.44 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 57, args: 23, core_var_decl: 14, design_snake_case: 14
- `template/en/default/bug/summarize-time.html.tmpl` (HTML) | Magnitude: 253.6 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 253, core_var_decl: 107, design_snake_case: 107, args: 54

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `template/en/default/account/prefs/saved-searches.html.tmpl` (HTML) | Magnitude: 19.04 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 152, args: 41, core_var_decl: 40, design_snake_case: 40
- `xt/lib/Bugzilla/Test/Search/InjectionTest.pm` (PERL) | Magnitude: 48.56 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 49, indent_spaces: 30, branch: 16, func_start: 8
- `template/en/default/attachment/list.html.tmpl` (HTML) | Magnitude: 29.04 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 136, core_var_decl: 39, design_snake_case: 37, structural_boundaries: 14
- `Bugzilla/WebService/Server.pm` (PERL) | Magnitude: 55.56 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 41, indent_spaces: 40, branch: 18, import: 7
- `template/en/default/bug/process/verify-new-product.html.tmpl` (HTML) | Magnitude: 29.7 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 179, core_var_decl: 64, design_snake_case: 64, args: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `template/en/default/admin/classifications/edit.html.tmpl` (HTML) | Magnitude: 19.86 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, args: 14, core_var_decl: 12, design_snake_case: 12
- `t/013dbschema.t` (PERL) | Magnitude: 28.2 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 18, import: 10, branch: 7
- `template/en/default/admin/sudo.html.tmpl` (HTML) | Magnitude: 25.62 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, args: 25, core_var_decl: 25, design_snake_case: 25
- `template/en/default/global/confirm-action.html.tmpl` (HTML) | Magnitude: 19.88 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, args: 12, core_var_decl: 8, design_snake_case: 8
- `Bugzilla/WebService/Server/REST/Resources/Product.pm` (PERL) | Magnitude: 7.74 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 24, bitwise_ops: 9, core_var_decl: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Bugzilla.pm` (PERL) | Magnitude: 462.6 | Delta: **0.138** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 377, structural_boundaries: 342, branch: 188, import: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `js/attachment.js` (JAVASCRIPT) | Magnitude: 275.5 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 220, branch: 66, state_mutation: 50, core_var_decl: 44
- `skins/standard/admin.css` (CSS) | Magnitude: 0.98 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 109, class_start: 102, safety_bypasses: 7, immutability_locks: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `Bugzilla/Auth/Verify/DB.pm` (PERL) | Magnitude: 50.76 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 32, branch: 13, import: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Bugzilla/User.pm` -> **Severity: 0.803** (Bridge: 0.008 * Flux: 99.7632%)
- `Bugzilla/Group.pm` -> **Severity: 0.304** (Bridge: 0.0031 * Flux: 98.7009%)
- `Bugzilla/Bug.pm` -> **Severity: 0.301** (Bridge: 0.003 * Flux: 99.9998%)
- `Bugzilla/Product.pm` -> **Severity: 0.207** (Bridge: 0.0021 * Flux: 98.6166%)
- `Bugzilla/Search/Saved.pm` -> **Severity: 0.163** (Bridge: 0.0016 * Flux: 99.6208%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Bugzilla/Error.pm` -> **Severity: 14.852** (Embedded: 0.2207 * Error Risk: 67.3026%)
- `Bugzilla/Util.pm` -> **Severity: 14.21** (Embedded: 0.2303 * Error Risk: 61.6944%)
- `Bugzilla/Constants.pm` -> **Severity: 13.52** (Embedded: 0.2598 * Error Risk: 52.0308%)
- `Bugzilla/Hook.pm` -> **Severity: 8.252** (Embedded: 0.1611 * Error Risk: 51.2224%)
- `Bugzilla/RNG.pm` -> **Severity: 7.349** (Embedded: 0.1357 * Error Risk: 54.1721%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Bugzilla/Constants.pm` -> **Severity: 5895.3** (Blast Radius: 58.953 * Doc Risk: 100.0%)
- `Bugzilla/Error.pm` -> **Severity: 4401.0** (Blast Radius: 44.01 * Doc Risk: 100.0%)
- `Bugzilla/Util.pm` -> **Severity: 3905.0** (Blast Radius: 39.05 * Doc Risk: 100.0%)
- `Bugzilla/Hook.pm` -> **Severity: 2146.3** (Blast Radius: 21.463 * Doc Risk: 100.0%)
- `Bugzilla/Config/Common.pm` -> **Severity: 1377.0** (Blast Radius: 13.77 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 751 literal sites + 1 sites through wrappers = 752
- **`panics_and_aborts`:** 365 literal sites + 22 sites through wrappers = 387

- `error` (function, panics_and_aborts, primitive): 22 call sites in 1 files -- `contrib/bugzilla-submit/bugzilla-submit`
- `d` (function, debug_prints, primitive): 1 call sites in 1 files -- `contrib/console.pl`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 14258 call pairs -- scoped 14.5%, unique 0.0%, ambiguous 2.3%, external 83.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| perl | 13480 | 14.3% | 0.0% | 2.2% | 83.4% |
| javascript | 605 | 18.0% | 0.0% | 3.1% | 78.8% |
| python | 113 | 23.0% | 0.0% | 0.0% | 77.0% |
| html | 41 | 2.4% | 2.4% | 0.0% | 95.1% |
| shell | 19 | 0.0% | 0.0% | 0.0% | 100.0% |

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
