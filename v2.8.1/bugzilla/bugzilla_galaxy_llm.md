# ARCHITECTURAL_BRIEF: bugzilla
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/bugzilla/bugzilla` |
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
| Total Artifacts | 927 |
| Analyzed Artifacts (Scanned) | 629 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 298 |
| Total LOC | 104531 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 67.9% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3538 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3605 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.015 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| HTML | 276 | 26766 | 43.9% |
| PERL | 262 | 71419 | 41.7% |
| PLAINTEXT | 33 | 0 | 5.2% |
| JAVASCRIPT | 19 | 2904 | 3.0% |
| CSS | 14 | 2616 | 2.2% |
| MARKDOWN | 7 | 0 | 1.1% |
| SHELL | 7 | 163 | 1.1% |
| CSV | 5 | 138 | 0.8% |
| PYTHON | 2 | 423 | 0.3% |
| XML | 2 | 0 | 0.3% |
| DOCKERFILE | 1 | 60 | 0.2% |
| YAML | 1 | 42 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +0.18; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 53%, Large Core Modules 16%, Declarative / Non-Code 11%, Compute Cores Files 8%, Interface Declarations Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 589 | 93.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 40 | 6.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 298*

**Composition by Extension & Reason:**
- `.rst`: 87x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 50x Excluded (Saturation: Line 7 exceeds 500 chars), 1x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Saturation: Line 14 exceeds 500 chars)
- `.png`: 43x Excluded (Explicitly Denied Extension: '.png')
- `.pm`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 294 LOC), 1x Excluded (Machine-Generated Source Code Signature: 122 LOC)
- `.css`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Saturation: Line 7 exceeds 500 chars)
- `.gif`: 16x Excluded (Explicitly Denied Extension: '.gif')
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.undeterminable)
- `.tmpl`: 1x Excluded (Machine-Generated Source Code Signature: 79 LOC), 1x Excluded (Machine-Generated Source Code Signature: 34 LOC), 1x Excluded (Machine-Generated Source Code Signature: 32 LOC)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pl`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.conf`: 2x Excluded (Unsupported Extension: '.conf')
- `.cnf`: 2x Excluded (Unsupported Extension: '.cnf')
- `.swf`: 2x Excluded (Unsupported Extension: '.swf')
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 93.6 | 15.5 | 4.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 35.0 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 39.0 | 17.2 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 7.4 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 79.9 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 35.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 24.5 | 0.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 62.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 36.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1296 | 145 | 4 | `Bugzilla/Bug.pm` |
| cleanup | 122 | 62 | 0 | `contrib/extension-convert.pl` |
| guards | 1010 | 338 | 3 | `template/en/default/global/user-error.html.tmpl` |
| danger | 1019 | 173 | 4 | `js/field.js` |
| concurrency | 15 | 10 | 0 | `Bugzilla/JobQueue.pm` |
| connectivity | 3472 | 351 | 15 | `Bugzilla/Bug.pm` |
| io | 1998 | 284 | 8 | `Bugzilla/WebService/Bug.pm` |
| crypto | 0 | 0 | 0 | - |
| ipc | 28 | 19 | 0 | `Bugzilla/Install.pm` |
| time | 186 | 62 | 0 | `Bugzilla/WebService/Bug.pm` |
| serialization | 12 | 3 | 0 | `js/comment-tagging.js` |
| regex | 1664 | 164 | 6 | `Bugzilla/Template.pm` |
| events | 445 | 148 | 2 | `Bugzilla/Migrate/Gnats.pm` |
| tests | 96 | 17 | 0 | `t/002goodperl.t` |
| docs | 4726 | 152 | 14 | `Bugzilla/WebService/Bug.pm` |
| debt | 4490 | 321 | 15 | `Bugzilla/WebService/Bug.pm` |
| mutation | 19406 | 530 | 74 | `Bugzilla/DB/Schema.pm` |
| dead_code | 304 | 109 | 1 | `js/field.js` |
| credential | 0 | 0 | 0 | - |
| threat | 416 | 125 | 1 | `template/en/default/setup/strings.txt.pl` |
| ml_ai | 295 | 40 | 0 | `Bugzilla/WebService/Bug.pm` |
| ui | 753 | 128 | 2 | `template/en/default/global/messages.html.tmpl` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.2727**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Bugzilla/WebService/Bug.pm` (Hits: 66)
- `Bugzilla/DB/Schema.pm` (Hits: 63)
- `template/en/default/pages/release-notes.html.tmpl` (Hits: 61)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **base.css** (`js/yui/base/base.css`) — 102 inbound connections
2. **bugs** (`contrib/cmdline/bugs`) — 9 inbound connections
3. **params.js** (`js/params.js`) — 5 inbound connections
4. **query.cgi** (`query.cgi`) — 3 inbound connections
5. **field.js** (`js/field.js`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **User.pm** (`Bugzilla/User.pm`) — 53 outbound dependencies
2. **Bug.pm** (`Bugzilla/Bug.pm`) — 50 outbound dependencies
3. **Bugzilla.pm** (`Bugzilla.pm`) — 45 outbound dependencies
4. **Bug.pm** (`Bugzilla/WebService/Bug.pm`) — 45 outbound dependencies
5. **Search.pm** (`Bugzilla/Search.pm`) — 44 outbound dependencies

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
- `update` **(Compute Cores)** (@ `Bugzilla/Bug.pm`) -> Impact: **203.9** | LOC: 336
- `Send` **(Many-Argument Workhorses)** (@ `Bugzilla/BugMail.pm`) -> Impact: **147.4** | LOC: 268
  * *Intent:* # args: bug_id, and an optional hash ref which may have keys for: # changer, owner, qa, reporter, cc # Optional hash contains values of people which w...
- `notify` **(Many-Argument Workhorses)** (@ `Bugzilla/Flag.pm`) -> Impact: **130.8** | LOC: 117

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Bugzilla` | 44 | 19799.14 | 23.63% | 52.16% |
| `__monolith__` | 70 | 8980.46 | 44.89% | 35.92% |
| `Bugzilla/Install` | 6 | 5283.2 | 21.5% | 19.55% |
| `Bugzilla/DB` | 7 | 4745.92 | 26.65% | 44.77% |
| `js` | 14 | 2503.92 | 55.65% | 86.13% |
| `template/en/default/bug` | 20 | 2328.38 | 2.32% | 74.42% |
| `Bugzilla/WebService` | 13 | 2266.82 | 11.74% | 38.27% |
| `template/en/default/search` | 12 | 1638.27 | 4.99% | 24.27% |
| `Bugzilla/DB/Schema` | 5 | 1262.46 | 36.53% | 24.05% |
| `template/en/default/bug/create` | 7 | 970.96 | 1.86% | 70.61% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Bugzilla/BugUrl.pm` -> **100.0%** Exposure
- `Bugzilla/BugUrl/Bugzilla/Local.pm` -> **100.0%** Exposure
- `Bugzilla/BugUrl/Debian.pm` -> **100.0%** Exposure
- `Bugzilla/BugUrl/Launchpad.pm` -> **100.0%** Exposure
- `Bugzilla/Config/BugChange.pm` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Bugzilla/Chart.pm` -> **100.0%** Exposure
- `Bugzilla/DB/Schema/Oracle.pm` -> **100.0%** Exposure
- `Bugzilla/Migrate/Gnats.pm` -> **100.0%** Exposure
- `Bugzilla/User/Setting/Skin.pm` -> **100.0%** Exposure
- `Bugzilla/User/Setting/Timezone.pm` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `js/field.js` -> **20** Orphaned Functions | **0** Duplicates
- `js/attachment.js` -> **15** Orphaned Functions | **0** Duplicates
- `Bugzilla/DB/Schema.pm` -> **14** Orphaned Functions | **0** Duplicates
- `js/util.js` -> **12** Orphaned Functions | **0** Duplicates
- `Bugzilla/DB/Oracle.pm` -> **9** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `10` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3048` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `js/comments.js` (JAVASCRIPT) -> Cumulative Risk: **735.61**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +1.74)
- **Magnitude:** 122.34 | **LOC:** 166 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.125%)
- **Heaviest Functions:** `wrapReplyText` (Compute Cores, Impact: 12.2), `toggle_all_comments` (Compute Cores, Impact: 9.6), `getText` (Compute Cores, Impact: 7.8)

### 2. `js/bug.js` (JAVASCRIPT) -> Cumulative Risk: **707.16**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.14)
- **Magnitude:** 167.0 | **LOC:** 244 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9992%), Tech Debt (99.8755%)
- **Heaviest Functions:** `set_assign_to` (Compute Cores, Impact: 31.8), `formatStatus` (Many-Argument Workhorses, Impact: 7.3), `doBeforeParseData` (Callbacks & Closures, Impact: 6.5)

### 3. `Bugzilla/Bug.pm` (PERL) -> Cumulative Risk: **692.88**
- **Archetype:** `file_cluster_3` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.24)
- **Magnitude:** 4039.98 | **LOC:** 5124 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Tech Debt (99.872%)
- **Heaviest Functions:** `update` (Compute Cores, Impact: 203.9), `get_activity` (Many-Argument Workhorses, Impact: 129.2), `_check_bug_status` (Many-Argument Workhorses, Impact: 76.7)

### 4. `extensions/Voting/Extension.pm` (PERL) -> Cumulative Risk: **690.06**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.74)
- **Magnitude:** 489.42 | **LOC:** 924 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9995%), State Flux (99.9744%)
- **Heaviest Functions:** `_update_votes` (Compute Cores, Impact: 72.7), `_page_user` (Compute Cores, Impact: 40.5), `_remove_votes` (I/O & Config Routines, Impact: 25.4)

### 5. `Bugzilla/Template.pm` (PERL) -> Cumulative Risk: **667.26**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.00)
- **Magnitude:** 1140.1 | **LOC:** 1439 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9981%), Tech Debt (97.6057%)
- **Heaviest Functions:** `create` (Many-Argument Workhorses, Impact: 462.1), `quoteUrls` (Many-Argument Workhorses, Impact: 115.0), `get_format` (Many-Argument Workhorses, Impact: 24.3)

### 6. `contrib/bugzilla-submit/bugzilla-submit` (PYTHON) -> Cumulative Risk: **660.16**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.89)
- **Magnitude:** 2.25 | **LOC:** 308 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `check_result_POST` (Compute Cores, Impact: 34.6), `validate_fields` (Compute Cores, Impact: 13.9), `ensure_defaults` (Compute Cores, Impact: 12.1)

### 7. `js/expanding-tree.js` (JAVASCRIPT) -> Cumulative Risk: **654.66**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.82)
- **Magnitude:** 117.76 | **LOC:** 143 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (99.177%)
- **Heaviest Functions:** `changeChildren` (Compute Cores, Impact: 29.4), `doToggle` (Compute Cores, Impact: 15.1), `duplicated` (Compute Cores, Impact: 11.0)

### 8. `js/attachment.js` (JAVASCRIPT) -> Cumulative Risk: **649.71**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.74)
- **Magnitude:** 279.2 | **LOC:** 338 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.8613%)
- **Heaviest Functions:** `switchToMode` (Compute Cores, Impact: 35.1), `restore_elem` (Compute Cores, Impact: 11.1), `TextFieldHandler` (I/O & Config Routines, Impact: 8.1)

### 9. `Bugzilla/Migrate/Gnats.pm` (PERL) -> Cumulative Risk: **646.06**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.53)
- **Magnitude:** 552.9 | **LOC:** 749 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9944%)
- **Heaviest Functions:** `_parse_audit_trail` (Many-Argument Workhorses, Impact: 54.4), `_parse_attachments` (Compute Cores, Impact: 42.0), `translate_value` (Many-Argument Workhorses, Impact: 39.7)

### 10. `importxml.pl` (PERL) -> Cumulative Risk: **644.47**
- **Archetype:** `file_cluster_16` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +1.80)
- **Magnitude:** 1555.5 | **LOC:** 1399 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.997%), Safety Score (99.1649%)
- **Heaviest Functions:** `process_bug` (Many-Argument Workhorses, Impact: 465.8), `flag_handler` (Many-Argument Workhorses, Impact: 119.6), `process_attachment` (Compute Cores, Impact: 34.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Bugzilla/Bug.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 4039.98 | **LOC:** 5124 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.8839%), Tech Debt (99.872%)
**Top Internal Functions/Classes:**
  * `update` **(Compute Cores)** (Impact: 203.9)
  * `get_activity` **(Many-Argument Workhorses)** (Impact: 129.2)
    * *Intent:* # Get the activity of a bug, starting from $starttime (if given). # This routine assumes Bugzilla::B...
  * `_check_bug_status` **(Many-Argument Workhorses)** (Impact: 76.7)
  * `create` **(Compute Cores)** (Impact: 71.2)
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
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 476`, `dead_code: 5`, `fragile_debt: 215`
* *Architecture:* `api: 139`, `import: 40`
* *Defense:* `safety: 10`, `doc: 140`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Bugzilla::Attachment, Bugzilla::BugMail, Bugzilla::BugUrl, Bugzilla::BugUserLastVisit, Bugzilla::Comment, Bugzilla::Component, Bugzilla::Constants, Bugzilla::Error...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Install/DB.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3936.76 | **LOC:** 4300 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.0108%), Tech Debt (98.695%)
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
* *Risk/State:* `state_mutation: 145`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 134`
* *Architecture:* `io: 2`, `api: 2`, `import: 22`
* *Defense:* `safety: 5`, `doc: 8`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::BugUrl, Bugzilla::Constants, Bugzilla::Field, Bugzilla::Hook, Bugzilla::Install, Bugzilla::Install::DB, Bugzilla::Install::Util, Bugzilla::Object...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Search.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2056.28 | **LOC:** 3562 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.7583%), Tech Debt (23.7434%)
**Top Internal Functions/Classes:**
  * `_multiselect_isempty` **(Many-Argument Workhorses)** (Impact: 62.6)
    * *Intent:* # We can't use the normal operator_functions to build isempty queries which # join to different tabl...
  * `SqlifyDate` **(Compute Cores)** (Impact: 58.7)
  * `_user_nonchanged` **(Compute Cores)** (Impact: 49.9)
    * *Intent:* # For all the "user" fields--assigned_to, reporter, qa_contact, # cc, commenter, requestee, etc.
  * `_multiselect_table` **(Compute Cores)** (Impact: 34.2)
  * `_special_parse_chfield` **(Compute Cores)** (Impact: 34.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 249 instances
* *State Mutation (weighted view):* 817
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 526`, `structural_boundaries: 1117`, `args: 126`, `func_start: 132`, `class_start: 1`
* *Risk/State:* `state_mutation: 319`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 21`
* *Architecture:* `io: 4`, `api: 17`, `import: 41`
* *Defense:* `safety: 2`, `doc: 39`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ASC, Bugzilla::Constants, Bugzilla::Error, Bugzilla::Field, Bugzilla::Group, Bugzilla::Keyword, Bugzilla::Search, Bugzilla::Search::Clause...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/User.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 1903.5 | **LOC:** 3408 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.3891%), Tech Debt (66.544%)
**Top Internal Functions/Classes:**
  * `match_field` **(Many-Argument Workhorses)** (Impact: 112.3)
  * `wants_bug_mail` **(Many-Argument Workhorses)** (Impact: 77.7)
    * *Intent:* # Returns true if the user wants mail for a given bug change. # Note: the "+" signs before the const...
  * `match` **(Many-Argument Workhorses)** (Impact: 48.6)
  * `validate_password_check` **(Compute Cores)** (Impact: 48.4)
  * `can_enter_product` **(Many-Argument Workhorses)** (Impact: 44.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 156 instances
* *State Mutation (weighted view):* 495
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 727`, `structural_boundaries: 788`, `args: 110`, `func_start: 116`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 183`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 49`
* *Architecture:* `io: 19`, `api: 105`, `import: 55`
* *Defense:* `safety: 2`, `doc: 164`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Bugzilla::Auth, Bugzilla::BugMail, Bugzilla::BugUserLastVisit, Bugzilla::Classification, Bugzilla::Component, Bugzilla::Constants, Bugzilla::Error, Bugzilla::Field...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `importxml.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 1555.5 | **LOC:** 1399 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.6483%), Tech Debt (99.997%)
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
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 283 instances
* *High Risk Execution (weighted view):* 2
* *Memory Alloc (weighted view):* 19
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 863
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 269`, `args: 11`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 297`, `fragile_debt: 92`
* *Architecture:* `io: 7`, `api: 7`, `import: 37`
* *Defense:* `safety: 8`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bugzilla, Bugzilla::Attachment, Bugzilla::Bug, Bugzilla::BugMail, Bugzilla::Component, Bugzilla::Constants, Bugzilla::Field, Bugzilla::FlagType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB/MariaDB.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1427.74 | **LOC:** 1301 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.4999%), Tech Debt (79.1358%)
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
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 58`, `dead_code: 3`, `fragile_debt: 12`, `unreferenced_by_name: 2`
* *Architecture:* `io: 6`, `api: 28`, `import: 16`
* *Defense:* `safety: 1`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::Config, Bugzilla::Constants, Bugzilla::DB::Schema::MariaDB, Bugzilla::Error, Bugzilla::Install::Util, Bugzilla::Util, Carp, List::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB/Mysql.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1421.44 | **LOC:** 1301 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.4252%), Tech Debt (79.1358%)
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
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 58`, `dead_code: 3`, `fragile_debt: 12`, `unreferenced_by_name: 2`
* *Architecture:* `io: 6`, `api: 28`, `import: 16`
* *Defense:* `safety: 1`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::Config, Bugzilla::Constants, Bugzilla::DB::Schema::Mysql, Bugzilla::Error, Bugzilla::Install::Util, Bugzilla::Util, Carp, List::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `template/en/default/bug/edit.html.tmpl` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1204.87 | **LOC:** 1253 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.8591%), Tech Debt (100.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 51`, `args: 157`, `func_start: 12`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 7`, `fragile_debt: 229`
* *Architecture:* `io: 54`, `api: 100`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Template.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1140.1 | **LOC:** 1439 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.3735%), Tech Debt (97.6057%)
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
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 107`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 36`
* *Architecture:* `io: 3`, `api: 14`, `import: 33`
* *Defense:* `safety: 5`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.112
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.003185
  * `Imports (Out-Degree: 1):` Accept, Bugzilla::Bug, Bugzilla::Classification, Bugzilla::Constants, Bugzilla::Error, Bugzilla::Hook, Bugzilla::Install::Requirements, Bugzilla::Install::Util...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Bugzilla/Flag.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 997.42 | **LOC:** 1310 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.1956%), Tech Debt (100.0%)
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
* *Risk/State:* `state_mutation: 71`, `dead_code: 1`, `fragile_debt: 94`, `unreferenced_by_name: 1`
* *Architecture:* `api: 31`, `import: 24`
* *Defense:* `safety: 8`, `doc: 22`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::Attachment, Bugzilla::Bug, Bugzilla::Constants, Bugzilla::Error, Bugzilla::Field, Bugzilla::FlagType, Bugzilla::Hook, Bugzilla::Mailer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/WebService/Bug.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 978.86 | **LOC:** 4693 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.4817%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_bug_to_hash` **(Many-Argument Workhorses)** (Impact: 83.5)
    * *Intent:* ############################## # Private Helper Subroutines # ############################## # A hel...
  * `search` **(Compute Cores)** (Impact: 52.3)
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
* *Defense:* `safety: 5`, `doc: 812`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::Bug, Bugzilla::BugMail, Bugzilla::Comment, Bugzilla::Comment::TagWeights, Bugzilla::Constants, Bugzilla::Error, Bugzilla::Field, Bugzilla::FlagType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB/Schema.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 916.76 | **LOC:** 3189 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.2829%), Tech Debt (30.4337%)
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
* *Risk/State:* `state_mutation: 74`, `dead_code: 6`, `planned_debt: 3`, `fragile_debt: 7`, `unreferenced_by_name: 14`
* *Architecture:* `io: 63`, `api: 37`, `import: 31`
* *Defense:* `safety: 5`, `doc: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bugzilla::Constants, Bugzilla::DB, Bugzilla::DB::Schema, Bugzilla::Error, Bugzilla::Hook, Bugzilla::Util, Carp, DEFAULT...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `template/en/default/bug/create/create.html.tmpl` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 867.48 | **LOC:** 673 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.1392%), Tech Debt (99.9971%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 19`, `args: 102`, `func_start: 5`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `fragile_debt: 52`
* *Architecture:* `io: 4`, `api: 39`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 820.4 | **LOC:** 3011 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.1379%), Tech Debt (16.1673%)
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
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 57`, `dead_code: 2`, `fragile_debt: 5`, `unreferenced_by_name: 2`
* *Architecture:* `io: 23`, `api: 61`, `import: 38`
* *Defense:* `safety: 10`, `doc: 456`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bugzilla::Constants, Bugzilla::DB, Bugzilla::DB::QuoteIdentifier, Bugzilla::DB::Schema, Bugzilla::Error, Bugzilla::Install::Localconfig, Bugzilla::Install::Requirements, Bugzilla::Install::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `template/en/default/search/form.html.tmpl` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 722.9 | **LOC:** 340 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.7555%), Tech Debt (35.8227%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 33`, `args: 73`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 4`, `fragile_debt: 4`
* *Architecture:* `io: 6`, `api: 36`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/field.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 692.48 | **LOC:** 1117 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.0539%), Tech Debt (83.5547%)
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
* *Risk/State:* `safety_bypasses: 35`, `high_risk_execution: 5`, `state_mutation: 112`, `dead_code: 3`, `fragile_debt: 1`, `unreferenced_by_name: 20`
* *Architecture:* None
* *Defense:* `safety: 6`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.275
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004777
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Bugzilla/Object.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 687.88 | **LOC:** 1595 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.9053%), Tech Debt (20.189%)
**Top Internal Functions/Classes:**
  * `match` **(Compute Cores)** (Impact: 46.9)
    * *Intent:* # Note: Future extensions to this could be: # * Add a MATCH_JOIN constant so that we can join agains...
  * `_do_list_select` **(Many-Argument Workhorses)** (Impact: 37.9)
  * `update` **(Compute Cores)** (Impact: 36.1)
  * `_load_from_db` **(Compute Cores)** (Impact: 29.2)
    * *Intent:* # Note: Because this uses sql_istrcmp, if you make a new object use # Bugzilla::Object, make sure th...
  * `new` **(Compute Cores)** (Impact: 26.3)
    * *Intent:* ############################### #### Initialization #### ###############################
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 54 instances
* *Memory Alloc (weighted view):* 10
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 301`, `structural_boundaries: 552`, `args: 44`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `state_mutation: 61`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 6`
* *Architecture:* `io: 37`, `api: 26`, `import: 34`
* *Defense:* `safety: 7`, `doc: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bugzilla::Constants, Bugzilla::Error, Bugzilla::Hook, Bugzilla::Util, DEFAULT, Date::Parse, List::MoreUtils, Scalar::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Util.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 676.56 | **LOC:** 1361 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.5413%), Tech Debt (13.0264%)
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
* *Defense:* `safety: 3`, `doc: 86`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::Constants, Bugzilla::Error, Bugzilla::RNG, Bugzilla::Util, C, Carp, Date::Format, Date::Parse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Migrate.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 582.1 | **LOC:** 1249 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.4668%), Tech Debt (99.9992%)
**Top Internal Functions/Classes:**
  * `insert_bugs` **(Compute Cores)** (Impact: 64.3)
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
* *Defense:* `safety: 2`, `doc: 66`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bugzilla::Attachment, Bugzilla::Bug, Bugzilla::Component, Bugzilla::Constants, Bugzilla::Error, Bugzilla::Install::Requirements, Bugzilla::Install::Util, Bugzilla::Product...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Migrate/Gnats.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 552.9 | **LOC:** 749 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.6822%), Tech Debt (99.9944%)
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
* *Defense:* `safety: 2`, `doc: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::Constants, Bugzilla::Install::Util, Bugzilla::Util, Email::Address::XS, Email::MIME, File::Basename, IO::File, List::MoreUtils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/Example/Extension.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 539.76 | **LOC:** 1117 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.8218%), Tech Debt (0.0%)
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
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 57`, `dead_code: 3`, `fragile_debt: 50`
* *Architecture:* `api: 69`, `import: 15`
* *Defense:* `safety: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::Constants, Bugzilla::Error, Bugzilla::Extension::Example::Util, Bugzilla::Group, Bugzilla::Install::Filesystem, Bugzilla::Status, Bugzilla::User, Bugzilla::User::Setting...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB/Oracle.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 532.12 | **LOC:** 883 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.045%), Tech Debt (60.2381%)
**Top Internal Functions/Classes:**
  * `bz_setup_database` **(Compute Cores)** (Impact: 41.8)
    * *Intent:* ##################################################################### # Custom Database Setup ######...
  * `adjust_statement` **(Compute Cores)** (Impact: 29.7)
  * `BUILDARGS` **(Compute Cores)** (Impact: 13.2)
  * `selectall_arrayref` **(Type Conversions)** (Impact: 13.1)
  * `sql_in` **(Many-Argument Workhorses)** (Impact: 11.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 307`, `args: 54`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `state_mutation: 65`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 39`, `import: 15`
* *Defense:* `safety: 3`, `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::Constants, Bugzilla::Error, Bugzilla::Util, DBD::Oracle, List::Util, Moo, SUBSTR, base...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Product.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 509.08 | **LOC:** 1186 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.7292%), Tech Debt (66.9834%)
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
* *Risk/State:* `state_mutation: 51`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 17`
* *Architecture:* `io: 5`, `api: 32`, `import: 32`
* *Defense:* `safety: 2`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::Bug, Bugzilla::Component, Bugzilla::Constants, Bugzilla::Error, Bugzilla::Field, Bugzilla::FlagType, Bugzilla::Group, Bugzilla::Hook...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `buglist.cgi` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 508.28 | **LOC:** 1166 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.6527%), Tech Debt (99.9979%)
**Top Internal Functions/Classes:**
  * `GetGroups` **(Compute Cores)** (Impact: 14.1)
    * *Intent:* # Return groups available for at least one product of the buglist.
  * `InsertNamedQuery` **(Many-Argument Workhorses)** (Impact: 11.1)
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
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 152`, `dead_code: 2`, `fragile_debt: 64`
* *Architecture:* `api: 6`, `import: 18`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Apache2::RequestUtil, Bugzilla, Bugzilla::Bug, Bugzilla::Constants, Bugzilla::Error, Bugzilla::Field, Bugzilla::Product, Bugzilla::Search...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB/Schema/Oracle.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 502.64 | **LOC:** 563 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.1881%), Tech Debt (14.2037%)
**Top Internal Functions/Classes:**
  * `get_alter_column_ddl` **(Many-Argument Workhorses)** (Impact: 96.9)
  * `_get_alter_type_sql` **(Many-Argument Workhorses)** (Impact: 59.6)
  * `get_add_column_ddl` **(Many-Argument Workhorses)** (Impact: 18.7)
  * `get_add_fks_sql` **(Many-Argument Workhorses)** (Impact: 15.4)
  * `get_rename_table_sql` **(Many-Argument Workhorses)** (Impact: 13.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 60 instances
* *State Mutation (weighted view):* 194
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 134`, `args: 25`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 74`, `dead_code: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 1`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bugzilla::Util, Carp, Moo, constant, default, longer, of
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `js/params.js` -> **Severity: 0.755** (Embedded: 0.008 * Error Risk: 94.8548%)
- `query.cgi` -> **Severity: 0.468** (Embedded: 0.0048 * Error Risk: 97.9059%)
- `js/field.js` -> **Severity: 0.453** (Embedded: 0.0048 * Error Risk: 94.8669%)
- `Bugzilla/Template.pm` -> **Severity: 0.277** (Embedded: 0.0032 * Error Risk: 87.0512%)
- `js/comments.js` -> **Severity: 0.158** (Embedded: 0.0016 * Error Risk: 99.125%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `js/params.js` -> **Severity: 718.1** (Blast Radius: 7.181 * Doc Risk: 100.0%)
- `js/field.js` -> **Severity: 365.318** (Blast Radius: 4.275 * Doc Risk: 85.4545%)
- `Bugzilla/Template.pm` -> **Severity: 311.2** (Blast Radius: 3.112 * Doc Risk: 100.0%)
- `Bugzilla/Auth/Login/Env.pm` -> **Severity: 253.0** (Blast Radius: 2.53 * Doc Risk: 100.0%)
- `query.cgi` -> **Severity: 243.444** (Blast Radius: 3.693 * Doc Risk: 65.9205%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
