# ARCHITECTURAL_BRIEF: bugzilla
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/bugzilla` |
| **Timestamp** | `2026-08-07T03:47:24.049961+00:00` |
| **Scan Duration** | `2.19s` |
| **Git Branch** | `5.2` |
| **Git Commit** | `4299886770979cfb98c7417a6094c36a3ab19c00` |
| **Git Remote** | `https://github.com/bugzilla/bugzilla` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 29 malicious artifacts.

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
| Total Artifacts | 927 |
| Analyzed Artifacts (Scanned) | 627 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 300 |
| Total LOC | 103711 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 67.6% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3467 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3714 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3078 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| HTML | 276 | 26555 | 44.0% |
| PERL | 261 | 71363 | 41.6% |
| PLAINTEXT | 32 | 0 | 5.1% |
| JAVASCRIPT | 19 | 2357 | 3.0% |
| CSS | 14 | 2612 | 2.2% |
| MARKDOWN | 7 | 0 | 1.1% |
| SHELL | 7 | 163 | 1.1% |
| CSV | 5 | 136 | 0.8% |
| PYTHON | 2 | 423 | 0.3% |
| XML | 2 | 0 | 0.3% |
| DOCKERFILE | 1 | 60 | 0.2% |
| YAML | 1 | 42 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.075`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 350 | 55.8% |
| file_cluster_0 | 129 | 20.6% |
| file_cluster_13 | 98 | 15.6% |
| file_cluster_12 | 4 | 0.6% |
| file_cluster_17 | 3 | 0.5% |
| file_cluster_2 | 2 | 0.3% |
| file_cluster_11 | 1 | 0.2% |
| file_cluster_9 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 39 | 6.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 300*

**Composition by Extension & Reason:**
- `.rst`: 87x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 47x Excluded (Saturation: Line 7 exceeds 500 chars), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.png`: 43x Excluded (Explicitly Denied Extension: '.png')
- `.pm`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 294 LOC), 1x Excluded (Machine-Generated Source Code Signature: 122 LOC)
- `.css`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Saturation: Line 7 exceeds 500 chars)
- `.gif`: 16x Excluded (Explicitly Denied Extension: '.gif')
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.undeterminable)
- `.tmpl`: 1x Excluded (Machine-Generated Source Code Signature: 79 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 34 LOC)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pl`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.conf`: 2x Excluded (Unsupported Extension: '.conf')
- `.cnf`: 2x Excluded (Unsupported Extension: '.cnf')
- `.swf`: 2x Excluded (Unsupported Extension: '.swf')
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 27.3 | 10.5 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 43.3 | 55.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 43.8 | 21.5 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 15.3 | 2.3 | 2.3 |
| API Exposure | 0.0 | 14.3 | 2.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 57.2 | 0.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 45.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 24.5 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 96.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 40.8 | 33.4 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Bugzilla/WebService/Bug.pm` (Hits: 66)
- `Bugzilla/DB/Schema.pm` (Hits: 63)
- `template/en/default/pages/release-notes.html.tmpl` (Hits: 61)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **base.css** (`js/yui/base/base.css`) — 101 inbound connections
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

- `_check_groups` (@ `Bugzilla/Bug.pm`) -> Impact: **1122.0** | LOC: 2092
- `_set_product` (@ `Bugzilla/Bug.pm`) -> Impact: **1010.2** | LOC: 2125
  * *Intent:* # For security reasons, you have to use set_all to change the product. # See the strict_isolation check in set_all for an explanation.
- `set_priority` (@ `Bugzilla/Bug.pm`) -> Impact: **1010.1** | LOC: 2122
- `set_platform` (@ `Bugzilla/Bug.pm`) -> Impact: **1009.8** | LOC: 2116
- `_set_everconfirmed` (@ `Bugzilla/Bug.pm`) -> Impact: **1007.8** | LOC: 2116
- `set_op_sys` (@ `Bugzilla/Bug.pm`) -> Impact: **1007.8** | LOC: 2115
- `set_estimated_time` (@ `Bugzilla/Bug.pm`) -> Impact: **1007.6** | LOC: 2112
- `set_deadline` (@ `Bugzilla/Bug.pm`) -> Impact: **999.6** | LOC: 2113
- `set_comment_is_private` (@ `Bugzilla/Bug.pm`) -> Impact: **991.0** | LOC: 2099
- `set_cclist_accessible` (@ `Bugzilla/Bug.pm`) -> Impact: **990.8** | LOC: 2096

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `Bugzilla` | 44 | 69976.08 | 40.87% | 52.76% |
| `__monolith__` | 70 | 20683.72 | 62.99% | 41.64% |
| `Bugzilla/Install` | 6 | 5010.8 | 45.96% | 21.71% |
| `Bugzilla/DB` | 7 | 4370.2 | 43.38% | 29.22% |
| `Bugzilla/WebService` | 13 | 3488.4 | 17.49% | 42.08% |
| `js` | 14 | 2611.28 | 63.73% | 90.84% |
| `template/en/default/bug` | 20 | 2291.12 | 5.7% | 79.08% |
| `t` | 13 | 1922.06 | 78.7% | 24.79% |
| `Bugzilla/DB/Schema` | 5 | 1687.76 | 58.97% | 11.65% |
| `Bugzilla/Search` | 6 | 1496.82 | 36.14% | 22.33% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Bugzilla/BugUrl/Debian.pm` -> **100.0%** Exposure
- `Bugzilla/BugUrl/Launchpad.pm` -> **100.0%** Exposure
- `Bugzilla/Config/BugChange.pm` -> **100.0%** Exposure
- `Bugzilla/Config/Memcached.pm` -> **100.0%** Exposure
- `Bugzilla/Migrate.pm` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Bugzilla/Attachment.pm` -> **100.0%** Exposure
- `Bugzilla/Attachment/PatchReader.pm` -> **100.0%** Exposure
- `Bugzilla/Auth/Login/CGI.pm` -> **100.0%** Exposure
- `Bugzilla/Auth/Login/Cookie.pm` -> **100.0%** Exposure
- `Bugzilla/Auth/Login/Stack.pm` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `js/field.js` -> **0** Orphaned Functions | **16** Duplicates
- `js/attachment.js` -> **0** Orphaned Functions | **12** Duplicates
- `js/custom-search.js` -> **4** Orphaned Functions | **8** Duplicates
- `js/util.js` -> **9** Orphaned Functions | **2** Duplicates
- `js/comment-tagging.js` -> **3** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`contrib/bugzilla-submit/bugzilla-submit`** -> AI Confidence: **99.39%**
2. **`contrib/jb2bz.py`** -> AI Confidence: **99.31%**
3. **`Dockerfile`** -> AI Confidence: **99.29%**
4. **`contrib/cmdline/buglist`** -> AI Confidence: **99.29%**
5. **`contrib/cmdline/makequery`** -> AI Confidence: **99.29%**
6. **`docker/startup.sh`** -> AI Confidence: **99.29%**
7. **`template/en/default/bug/field-events.js.tmpl`** -> AI Confidence: **99.29%**
8. **`template/en/default/global/calendar.js.tmpl`** -> AI Confidence: **99.29%**
9. **`contrib/cmdline/bugcount`** -> AI Confidence: **99.06%**
10. **`contrib/cmdline/bugslink`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3044` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `extensions/OldBugMove/Extension.pm` (PERL) -> Cumulative Risk: **607.65**
- **Archetype:** `file_cluster_0` (Distance: 12.62 IQR)
- **Magnitude:** 170.82 | **LOC:** 201 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9987%), Safety Score (89.93%)
- **Heaviest Functions:** `_move_bug` (Impact: 16.1), `object_end_of_set` (Impact: 7.5), `_check_bug_resolution` (Impact: 6.4)

### 2. `js/comment-tagging.js` (JAVASCRIPT) -> Cumulative Risk: **577.63**
- **Archetype:** `file_cluster_8` (Distance: 12.763 IQR)
- **Magnitude:** 420.76 | **LOC:** 388 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.5882%), Safety Score (97.9648%)
- **Heaviest Functions:** `updateCollapseControls` (Impact: 21.0), `add` (Impact: 19.4), `onKeyPress` (Impact: 12.4)

### 3. `js/field.js` (JAVASCRIPT) -> Cumulative Risk: **575.96**
- **Archetype:** `file_cluster_17` (Distance: 12.465 IQR)
- **Magnitude:** 675.3 | **LOC:** 1117 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.78%), Safety Score (91.8548%)
- **Heaviest Functions:** `showFieldWhen` (Impact: 101.2), `handleVisControllerValueChange` (Impact: 89.4), `getPossiblyHiddenOption` (Impact: 54.3)

### 4. `Bugzilla/Bug.pm` (PERL) -> Cumulative Risk: **574.78**
- **Archetype:** `file_cluster_0` (Distance: 14.309 IQR)
- **Magnitude:** 23694.96 | **LOC:** 5124 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9988%), Safety Score (94.0652%)
- **Heaviest Functions:** `_check_groups` (Impact: 1122.0), `_set_product` (Impact: 1010.2), `set_priority` (Impact: 1010.1)

### 5. `extensions/Voting/Extension.pm` (PERL) -> Cumulative Risk: **574.17**
- **Archetype:** `file_cluster_0` (Distance: 12.373 IQR)
- **Magnitude:** 631.52 | **LOC:** 924 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9997%), Safety Score (89.9957%)
- **Heaviest Functions:** `_page_user` (Impact: 58.8), `_update_votes` (Impact: 42.7), `_modify_bug_votes` (Impact: 28.0)

### 6. `js/attachment.js` (JAVASCRIPT) -> Cumulative Risk: **573.4**
- **Archetype:** `file_cluster_8` (Distance: 11.047 IQR)
- **Magnitude:** 297.4 | **LOC:** 338 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), State Flux (99.9392%), Safety Score (87.9934%)
- **Heaviest Functions:** `switchToMode` (Impact: 35.1), `TextFieldHandler` (Impact: 13.2), `DataFieldHandler` (Impact: 13.1)

### 7. `js/comments.js` (JAVASCRIPT) -> Cumulative Risk: **570.33**
- **Archetype:** `file_cluster_8` (Distance: 11.957 IQR)
- **Magnitude:** 113.58 | **LOC:** 166 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9955%), Safety Score (97.7344%)
- **Heaviest Functions:** `toggle_all_comments` (Impact: 15.0), `getText` (Impact: 9.4), `updateCommentPrivacy` (Impact: 7.5)

### 8. `Bugzilla/Comment.pm` (PERL) -> Cumulative Risk: **567.69**
- **Archetype:** `file_cluster_13` (Distance: 12.489 IQR)
- **Magnitude:** 1837.72 | **LOC:** 647 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9997%), Tech Debt (99.7951%), Safety Score (83.087%)
- **Heaviest Functions:** `already_wrapped` (Impact: 177.4), `body` (Impact: 177.3), `bug_id` (Impact: 177.3)

### 9. `js/bug.js` (JAVASCRIPT) -> Cumulative Risk: **567.11**
- **Archetype:** `file_cluster_8` (Distance: 11.693 IQR)
- **Magnitude:** 143.84 | **LOC:** 244 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9137%), Safety Score (95.371%)
- **Heaviest Functions:** `set_assign_to` (Impact: 39.9), `doBeforeParseData` (Impact: 6.5), `updateTable` (Impact: 5.6)

### 10. `js/custom-search.js` (JAVASCRIPT) -> Cumulative Risk: **566.02**
- **Archetype:** `file_cluster_8` (Distance: 12.331 IQR)
- **Magnitude:** 243.04 | **LOC:** 345 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9988%), Safety Score (97.2845%)
- **Heaviest Functions:** `_cs_j_change` (Impact: 23.1), `_cs_build_structure` (Impact: 20.3), `_cs_trigger_j_listeners` (Impact: 16.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Bugzilla/Bug.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.309 IQR)
- **Top Global Matches:** file_cluster_0: 14.309, file_cluster_8: 14.369, file_cluster_13: 14.408
- **Magnitude:** 23694.96 | **LOC:** 5124 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.6729%), Tech Debt (99.9988%)
**Top Internal Functions/Classes:**
  * `_check_groups` (Impact: 1122.0)
  * `_set_product` (Impact: 1010.2)
    * *Intent:* # For security reasons, you have to use set_all to change the product. # See the strict_isolation ch...
  * `set_priority` (Impact: 1010.1)
  * `set_platform` (Impact: 1009.8)
  * `_set_everconfirmed` (Impact: 1007.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1059`, `structural_boundaries: 1523`, `args: 151`, `func_start: 194`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 2188`, `dead_code: 5`, `fragile_debt: 215`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 40`
* *Defense:* `safety: 10`, `doc: 140`, `cleanup: 84`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Bugzilla::Flag, Bugzilla::Error, Bugzilla::Product, Bugzilla::Comment, POD, Scalar::Util, email_in, this...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/User.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.904 IQR)
- **Top Global Matches:** file_cluster_0: 13.904, file_cluster_13: 13.947, file_cluster_8: 14.009
- **Magnitude:** 8791.88 | **LOC:** 3408 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.7241%), Tech Debt (92.2404%)
**Top Internal Functions/Classes:**
  * `is_enabled` (Impact: 721.6)
  * `email` (Impact: 719.9)
  * `disabledtext` (Impact: 719.9)
  * `extern_id` (Impact: 719.8)
  * `name` (Impact: 719.6)
    * *Intent:* ################################################################################ # Methods #########...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 726`, `structural_boundaries: 788`, `args: 111`, `func_start: 116`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1154`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 50`, `orphaned_logic: 1`
* *Architecture:* `io: 19`, `api: 1`, `import: 55`
* *Defense:* `safety: 2`, `doc: 164`, `cleanup: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Bugzilla::Flag, Bugzilla::Error, Bugzilla::Product, Scalar::Util, way, URI, confirmation, it...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Flag.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.06 IQR)
- **Top Global Matches:** file_cluster_0: 13.06, file_cluster_13: 13.086, file_cluster_8: 13.227
- **Magnitude:** 5655.82 | **LOC:** 1310 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.6083%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `id` (Impact: 477.2)
  * `name` (Impact: 477.1)
  * `type_id` (Impact: 477.1)
  * `bug_id` (Impact: 477.0)
  * `attach_id` (Impact: 477.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 301`, `structural_boundaries: 311`, `args: 30`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 390`, `dead_code: 1`, `fragile_debt: 94`
* *Architecture:* `api: 1`, `import: 24`
* *Defense:* `safety: 8`, `doc: 70`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::Error, Bugzilla::Mailer, Scalar::Util, alias, the, Storable, Bugzilla::Field, Bugzilla::Hook...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editusers.cgi` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.119 IQR)
- **Top Global Matches:** file_cluster_8: 12.119, file_cluster_0: 12.272, file_cluster_13: 12.334
- **Magnitude:** 4051.32 | **LOC:** 776 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.5317%), Tech Debt (43.5846%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 156`, `args: 3`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 264`, `fragile_debt: 8`
* *Architecture:* `import: 15`
* *Defense:* `safety: 2`, `cleanup: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bugzilla::Flag, Bugzilla::Error, Bugzilla::Mailer, Bugzilla::Group, Bugzilla, sense, strict, Bugzilla::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/FlagType.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.735 IQR)
- **Top Global Matches:** file_cluster_13: 12.735, file_cluster_0: 12.745, file_cluster_8: 12.754
- **Magnitude:** 3533.66 | **LOC:** 798 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.295%), Tech Debt (34.761%)
**Top Internal Functions/Classes:**
  * `id` (Impact: 161.6)
  * `name` (Impact: 161.5)
  * `description` (Impact: 161.5)
  * `cc_list` (Impact: 161.4)
  * `target_type` (Impact: 161.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 191`, `args: 21`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `state_mutation: 222`, `fragile_debt: 6`
* *Architecture:* `api: 1`, `import: 16`
* *Defense:* `safety: 2`, `doc: 67`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` exclusions, Bugzilla::Error, base, Bugzilla::Group, Email::Address::XS, strict, Bugzilla::Util, List::MoreUtils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Object.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.181 IQR)
- **Top Global Matches:** file_cluster_0: 13.181, file_cluster_13: 13.185, file_cluster_8: 13.365
- **Magnitude:** 3028.28 | **LOC:** 1595 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.255%), Tech Debt (20.9718%)
**Top Internal Functions/Classes:**
  * `TO_JSON` (Impact: 501.5)
    * *Intent:* # This allows the JSON-RPC interface to return Bugzilla::Object instances # as though they were hash...
  * `id` (Impact: 474.6)
    * *Intent:* ############################### #### Accessors ###### ###############################
  * `name` (Impact: 474.6)
  * `_insert_dep_field` (Impact: 311.6)
  * `_get_validators` (Impact: 181.5)
    * *Intent:* # This method is private and should only be called by Bugzilla::Object.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 299`, `structural_boundaries: 546`, `args: 43`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `state_mutation: 496`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 6`
* *Architecture:* `io: 37`, `import: 34`
* *Defense:* `safety: 7`, `doc: 132`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bugzilla::Error, this, Scalar::Util, dependencies, changes, the, matches, object...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Install/DB.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.91 IQR)
- **Top Global Matches:** file_cluster_8: 12.91, file_cluster_0: 13.157, file_cluster_13: 13.204
- **Magnitude:** 2928.66 | **LOC:** 4300 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.578%), Tech Debt (99.967%)
**Top Internal Functions/Classes:**
  * `_add_longdescs_already_wrapped` (Impact: 605.7)
  * `_fix_broken_all_closed_series` (Impact: 451.0)
  * `_convert_groups_system_from_groupset` (Impact: 54.5)
  * `_copy_old_charts_into_database` (Impact: 53.1)
  * `update_table_definitions` (Impact: 46.2)
    * *Intent:* # absolutely necessary. # # The subroutines should have long, descriptive names, so that you # can e...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 620`, `structural_boundaries: 851`, `args: 11`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `state_mutation: 1326`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 134`, `orphaned_logic: 5`
* *Architecture:* `io: 9`, `import: 22`
* *Defense:* `safety: 5`, `doc: 8`, `cleanup: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` this, component, URI, Bugzilla::Install, Bugzilla::Install::DB, the, Bugzilla::Install::Util, Bugzilla::BugUrl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Search.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.861 IQR)
- **Top Global Matches:** file_cluster_8: 13.861, file_cluster_13: 13.955, file_cluster_0: 13.976
- **Magnitude:** 2876.08 | **LOC:** 3562 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.4647%), Tech Debt (24.1083%)
**Top Internal Functions/Classes:**
  * `COLUMNS` (Impact: 501.1)
    * *Intent:* # 2. name: The name of the column in the database (may also be an expression # that returns the valu...
  * `_user_nonchanged` (Impact: 337.2)
    * *Intent:* # For all the "user" fields--assigned_to, reporter, qa_contact, # cc, commenter, requestee, etc.
  * `_deadline` (Impact: 241.9)
  * `_content_matches` (Impact: 17.9)
  * `_contact_exact_group` (Impact: 16.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 510`, `structural_boundaries: 1117`, `args: 128`, `func_start: 132`, `class_start: 1`
* *Risk/State:* `state_mutation: 1608`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 21`
* *Architecture:* `io: 4`, `api: 1`, `import: 41`
* *Defense:* `safety: 2`, `doc: 39`, `test: 3`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Bugzilla::Error, in, Scalar::Util, Bugzilla::Search::Clause, check, way, _all_values, need...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `report.cgi` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.841 IQR)
- **Top Global Matches:** file_cluster_8: 12.841, file_cluster_0: 12.843, file_cluster_13: 12.865
- **Magnitude:** 2825.35 | **LOC:** 442 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.708%), Tech Debt (47.5186%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 96`, `args: 4`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 231`, `fragile_debt: 4`
* *Architecture:* `import: 12`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bugzilla::Error, format, Bugzilla, strict, Bugzilla::Util, Bugzilla::Report, List::MoreUtils, warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `testserver.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.008 IQR)
- **Top Global Matches:** file_cluster_0: 13.008, file_cluster_13: 13.095, file_cluster_8: 13.32
- **Magnitude:** 2539.23 | **LOC:** 306 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.773%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 69`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 195`
* *Architecture:* `io: 14`, `import: 14`
* *Defense:* `safety: 6`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Socket, Template::Plugin::GD::Image, GD, Bugzilla, LWP, strict, https, Bugzilla::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Group.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.894 IQR)
- **Top Global Matches:** file_cluster_13: 12.894, file_cluster_0: 12.94, file_cluster_8: 13.015
- **Magnitude:** 2414.36 | **LOC:** 733 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.1928%), Tech Debt (36.8152%)
**Top Internal Functions/Classes:**
  * `description` (Impact: 204.4)
    * *Intent:* ############################### #### Accessors ###### ###############################
  * `is_bug_group` (Impact: 204.3)
  * `user_regexp` (Impact: 204.3)
  * `is_active` (Impact: 204.2)
  * `icon_url` (Impact: 204.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 203`, `args: 23`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `state_mutation: 246`, `fragile_debt: 6`
* *Architecture:* `api: 1`, `import: 19`
* *Defense:* `safety: 3`, `doc: 61`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` base, Bugzilla::Error, Bugzilla::Product, Bugzilla::Group, Bugzilla::Config, strict, Bugzilla::FlagType, Bugzilla::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Product.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.957 IQR)
- **Top Global Matches:** file_cluster_0: 12.957, file_cluster_13: 13.038, file_cluster_8: 13.214
- **Magnitude:** 2047.78 | **LOC:** 1186 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.0165%), Tech Debt (68.2955%)
**Top Internal Functions/Classes:**
  * `set_name` (Impact: 279.6)
  * `set_description` (Impact: 279.6)
  * `allows_unconfirmed` (Impact: 102.6)
    * *Intent:* ############################### #### Accessors ###### ###############################
  * `description` (Impact: 102.5)
  * `is_active` (Impact: 102.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 313`, `args: 28`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 385`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 17`
* *Architecture:* `io: 5`, `api: 2`, `import: 32`
* *Defense:* `safety: 2`, `doc: 56`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::Error, Bugzilla::Product, Scalar::Util, entry, the, special, C, Bugzilla::Group...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Attachment.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.021 IQR)
- **Top Global Matches:** file_cluster_13: 13.021, file_cluster_0: 13.029, file_cluster_8: 13.289
- **Magnitude:** 1972.46 | **LOC:** 1056 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.9032%), Tech Debt (99.9945%)
**Top Internal Functions/Classes:**
  * `set_content_type` (Impact: 268.2)
    * *Intent:* ############################### #### Validators ###### ###############################
  * `set_description` (Impact: 268.2)
  * `set_filename` (Impact: 268.1)
  * `set_is_patch` (Impact: 268.1)
  * `set_is_private` (Impact: 268.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 239`, `args: 20`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 293`, `dead_code: 1`, `fragile_debt: 54`
* *Architecture:* `io: 9`, `api: 1`, `import: 30`
* *Defense:* `safety: 4`, `doc: 100`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::Flag, Bugzilla::Error, this, attachment, File::Copy, the, effect, Storable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/WebService/Bug.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.122 IQR)
- **Top Global Matches:** file_cluster_8: 13.122, file_cluster_7: 13.149, file_cluster_13: 13.192
- **Magnitude:** 1969.86 | **LOC:** 4693 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.1305%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `comments` (Impact: 643.6)
  * `render_comment` (Impact: 621.3)
  * `_legal_field_values` (Impact: 40.3)
  * `fields` (Impact: 18.6)
    * *Intent:* ########### # Methods # ###########
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 583`, `structural_boundaries: 643`, `args: 16`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 585`, `fragile_debt: 448`
* *Architecture:* `io: 66`, `api: 1`, `import: 58`
* *Defense:* `safety: 5`, `doc: 812`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::Error, Bugzilla::Product, Bugzilla::Comment, in, this, as, with, aliases...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Comment.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.489 IQR)
- **Top Global Matches:** file_cluster_13: 12.489, file_cluster_0: 12.595, file_cluster_8: 12.67
- **Magnitude:** 1837.72 | **LOC:** 647 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.6532%), Tech Debt (99.7951%)
**Top Internal Functions/Classes:**
  * `already_wrapped` (Impact: 177.4)
    * *Intent:* ############################### #### Accessors ###### ###############################
  * `body` (Impact: 177.3)
  * `bug_id` (Impact: 177.3)
  * `creation_ts` (Impact: 177.2)
  * `is_private` (Impact: 177.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 169`, `args: 22`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 167`, `fragile_debt: 25`
* *Architecture:* `io: 4`, `api: 1`, `import: 22`
* *Defense:* `safety: 2`, `doc: 56`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` base, Bugzilla::Error, List::Util, Bugzilla::Comment, Scalar::Util, strict, Bugzilla::Attachment, Bugzilla::User...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.321 IQR)
- **Top Global Matches:** file_cluster_8: 13.321, file_cluster_13: 13.33, file_cluster_7: 13.393
- **Magnitude:** 1758.46 | **LOC:** 3011 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.2166%), Tech Debt (16.7539%)
**Top Internal Functions/Classes:**
  * `_bz_check_dbd` (Impact: 637.9)
  * `_bz_init_schema_storage` (Impact: 430.2)
  * `_check_references` (Impact: 26.7)
    * *Intent:* # This is used before adding a foreign key to a column, to make sure # that the database won't fail ...
  * `bz_check_requirements` (Impact: 14.9)
  * `_bz_populate_enum_table` (Impact: 11.1)
    * *Intent:* # For bz_populate_enum_tables
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 517`, `args: 74`, `func_start: 78`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 519`, `dead_code: 2`, `fragile_debt: 5`, `orphaned_logic: 2`
* *Architecture:* `io: 23`, `import: 38`
* *Defense:* `safety: 10`, `doc: 464`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` value, Bugzilla::Mailer, Bugzilla::Error, now, this, Scalar::Util, bz_table_list, NAME...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Component.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.639 IQR)
- **Top Global Matches:** file_cluster_0: 12.639, file_cluster_13: 12.771, file_cluster_8: 12.971
- **Magnitude:** 1320.96 | **LOC:** 687 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.9063%), Tech Debt (92.1814%)
**Top Internal Functions/Classes:**
  * `set_name` (Impact: 175.1)
  * `set_description` (Impact: 175.0)
  * `set_is_active` (Impact: 175.0)
  * `description` (Impact: 146.5)
    * *Intent:* ############################### #### Accessors #### ###############################
  * `product_id` (Impact: 146.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 176`, `args: 24`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 201`, `planned_debt: 1`, `fragile_debt: 14`
* *Architecture:* `api: 1`, `import: 22`
* *Defense:* `safety: 2`, `doc: 34`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` base, Bugzilla::Error, Bugzilla::Product, Scalar::Util, strict, Bugzilla::FlagType, Bugzilla::Series, Bugzilla::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Template.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.922 IQR)
- **Top Global Matches:** file_cluster_0: 13.922, file_cluster_13: 14.054, file_cluster_17: 14.153
- **Magnitude:** 1210.08 | **LOC:** 1439 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.8209%), Tech Debt (97.7491%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 165.3)
    * *Intent:* # Construct the Template object # Note that all of the failure cases here can't use templateable err...
  * `SAFE_URL_REGEXP` (Impact: 120.9)
    * *Intent:* # Pseudo-constant.
  * `get_bug_link` (Impact: 49.9)
    * *Intent:* # Creates a link to a bug, including its title. # It takes either two or three parameters: # - The b...
  * `_css_url_rewrite` (Impact: 31.8)
  * `_css_link_set` (Impact: 23.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 400`, `args: 49`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 738`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 36`
* *Architecture:* `io: 3`, `api: 1`, `import: 33`
* *Defense:* `safety: 5`, `doc: 25`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003195
  * `Imports (Out-Degree: 1):` Bugzilla::Error, this, Scalar::Util, in, abs2rel, File::Path, it, File::Spec...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `template/en/default/bug/edit.html.tmpl` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.392 IQR)
- **Top Global Matches:** file_cluster_8: 7.392, file_cluster_0: 8.126, file_cluster_7: 8.331
- **Magnitude:** 1196.67 | **LOC:** 1253 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.8504%), Tech Debt (100.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 49`, `args: 157`, `func_start: 13`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 12`, `fragile_debt: 229`
* *Architecture:* `io: 54`, `api: 100`
* *Defense:* `safety: 6`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `reports.cgi` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.737 IQR)
- **Top Global Matches:** file_cluster_0: 12.737, file_cluster_13: 12.765, file_cluster_17: 12.919
- **Magnitude:** 1109.12 | **LOC:** 227 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.9731%), Tech Debt (76.6007%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 58`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 128`, `dead_code: 1`, `fragile_debt: 3`
* *Architecture:* `io: 6`, `import: 10`
* *Defense:* `safety: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bugzilla::Error, Bugzilla, strict, Bugzilla::Status, File::Basename, data, a, Bugzilla::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Util.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.61 IQR)
- **Top Global Matches:** file_cluster_13: 13.61, file_cluster_0: 13.689, file_cluster_8: 13.741
- **Magnitude:** 1107.92 | **LOC:** 1361 | **CtrlFlow:** 46.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.0943%), Tech Debt (13.707%)
**Top Internal Functions/Classes:**
  * `validate_date` (Impact: 257.3)
  * `css_class_quote` (Impact: 160.2)
  * `html_quote` (Impact: 48.6)
    * *Intent:* # Bug 120030: Override html filter to obscure the '@' in user # visible strings. # Bug 319331: Handl...
  * `datetime_from` (Impact: 34.0)
  * `validate_email_syntax` (Impact: 12.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 273`, `structural_boundaries: 319`, `args: 33`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `state_mutation: 551`, `fragile_debt: 3`
* *Architecture:* `io: 6`, `api: 1`, `import: 31`
* *Defense:* `safety: 3`, `doc: 86`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` specific, Bugzilla::Error, format, Email::Address::XS, Scalar::Util, in, this, way...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB/Schema.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.045 IQR)
- **Top Global Matches:** file_cluster_8: 12.045, file_cluster_0: 12.192, file_cluster_13: 12.295
- **Magnitude:** 1067.72 | **LOC:** 3189 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.1367%), Tech Debt (13.1885%)
**Top Internal Functions/Classes:**
  * `set_column` (Impact: 166.9)
  * `get_alter_column_ddl` (Impact: 54.4)
  * `get_type_ddl` (Impact: 35.5)
    * *Intent:* #--------------------------------------------------------------------------
  * `_set_nulls_sql` (Impact: 32.9)
    * *Intent:* # Helps handle any fields that were NULL before, if we have a default, # when doing an ALTER COLUMN.
  * `get_table_ddl` (Impact: 22.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 311`, `structural_boundaries: 337`, `args: 54`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `state_mutation: 431`, `dead_code: 6`, `planned_debt: 3`, `fragile_debt: 8`
* *Architecture:* `io: 63`, `import: 31`
* *Defense:* `safety: 5`, `doc: 169`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bugzilla::Error, this, in, Bugzilla::DB, way, old, of, leading...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB/MariaDB.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.897 IQR)
- **Top Global Matches:** file_cluster_0: 12.897, file_cluster_13: 12.906, file_cluster_8: 12.921
- **Magnitude:** 1029.8 | **LOC:** 1301 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.8029%), Tech Debt (46.9175%)
**Top Internal Functions/Classes:**
  * `sql_date_format` (Impact: 186.7)
  * `bz_enum_initial_values` (Impact: 172.8)
  * `_bz_raw_column_info` (Impact: 126.8)
  * `BUILDARGS` (Impact: 74.8)
  * `_fix_defaults` (Impact: 26.6)
    * *Intent:* # When you import a MySQL 3/4 mysqldump into MySQL 5, columns that # aren't supposed to have default...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 293`, `args: 31`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 374`, `dead_code: 3`, `fragile_debt: 12`
* *Architecture:* `io: 6`, `import: 16`
* *Defense:* `safety: 1`, `doc: 42`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` so, Bugzilla::Error, now, in, with, for, the, Text::ParseWords...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB/Mysql.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.896 IQR)
- **Top Global Matches:** file_cluster_0: 12.896, file_cluster_13: 12.905, file_cluster_8: 12.919
- **Magnitude:** 1028.0 | **LOC:** 1301 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.7941%), Tech Debt (46.9175%)
**Top Internal Functions/Classes:**
  * `sql_date_format` (Impact: 186.7)
  * `bz_enum_initial_values` (Impact: 172.8)
  * `_bz_raw_column_info` (Impact: 126.8)
  * `BUILDARGS` (Impact: 74.8)
  * `_fix_defaults` (Impact: 26.6)
    * *Intent:* # When you import a MySQL 3/4 mysqldump into MySQL 5, columns that # aren't supposed to have default...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 293`, `args: 31`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 374`, `dead_code: 3`, `fragile_debt: 12`
* *Architecture:* `io: 6`, `import: 16`
* *Defense:* `safety: 1`, `doc: 42`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` so, Bugzilla::Error, now, in, with, for, Bugzilla::DB::Schema::Mysql, the...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `buglist.cgi` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.298 IQR)
- **Top Global Matches:** file_cluster_0: 13.298, file_cluster_17: 13.342, file_cluster_13: 13.411
- **Magnitude:** 1002.18 | **LOC:** 1166 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.8426%), Tech Debt (99.998%)
**Top Internal Functions/Classes:**
  * `DiffDate` (Impact: 472.6)
    * *Intent:* ################################################################################ # Utilities #######...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 224`, `structural_boundaries: 188`, `args: 7`, `func_start: 7`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 515`, `dead_code: 2`, `fragile_debt: 64`
* *Architecture:* `import: 18`
* *Defense:* `safety: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bugzilla::Error, Bugzilla::Product, it, for, the, Bugzilla::Search, lib, Apache2::RequestUtil...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `Bugzilla/DB/Pg.pm` (PERL) | Magnitude: 276.9 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 255, structural_boundaries: 139, state_mutation: 124, branch: 57
- `Bugzilla/Auth/Verify/RADIUS.pm` (PERL) | Magnitude: 31.7 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 21, indent_spaces: 21, state_mutation: 18, decorators: 12
- `Bugzilla/Object.pm` (PERL) | Magnitude: 3028.28 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 573, structural_boundaries: 546, state_mutation: 496, branch: 299
- `Bugzilla/DB/Mysql.pm` (PERL) | Magnitude: 1028.0 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 628, state_mutation: 374, structural_boundaries: 293, branch: 249
- `Bugzilla/DB/MariaDB.pm` (PERL) | Magnitude: 1029.8 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 628, state_mutation: 374, structural_boundaries: 293, branch: 250

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `contrib/cmdline/makequery` (SHELL) | Magnitude: 1.26 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 81, indent_spaces: 57, reflection_metaprogramming: 37, safety_bypasses: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `contrib/cmdline/bugslink` (SHELL) | Magnitude: 0.14 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 9, io: 4, reflection_metaprogramming: 3, debug_prints: 3
- `contrib/cmdline/bugcount` (SHELL) | Magnitude: 0.1 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 6, reflection_metaprogramming: 2, orphaned_logic: 2, branch: 1
- `contrib/cmdline/bugids` (SHELL) | Magnitude: 0.14 | Delta: **0.137 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 9, io: 6, reflection_metaprogramming: 3, structural_boundaries: 2
- `contrib/cmdline/buglist` (SHELL) | Magnitude: 0.14 | Delta: **0.31 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 10, reflection_metaprogramming: 5, safety: 2, orphaned_logic: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Bugzilla/Config.pm` (PERL) | Magnitude: 278.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 200, state_mutation: 100, branch: 96, structural_boundaries: 74
- `Bugzilla/Search/ClauseGroup.pm` (PERL) | Magnitude: 52.84 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 34, pointers: 20, branch: 15
- `Bugzilla/Extension.pm` (PERL) | Magnitude: 1001.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 170, indent_spaces: 119, branch: 117, state_mutation: 113
- `rest.cgi` (PERL) | Magnitude: 17.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 11, decorators: 10, import: 8, indent_spaces: 3
- `contrib/mysqld-watcher.pl` (PERL) | Magnitude: 0.32 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 37, state_mutation: 23, structural_boundaries: 15, branch: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `Bugzilla/Update.pm` (PERL) | Magnitude: 166.92 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, state_mutation: 92, branch: 61, structural_boundaries: 58
- `editflagtypes.cgi` (PERL) | Magnitude: 341.22 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 375, state_mutation: 266, branch: 131, structural_boundaries: 130
- `js/field.js` (JAVASCRIPT) | Magnitude: 675.3 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 400, state_mutation: 204, branch: 93, structural_boundaries: 84

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `js/change-columns.js` (JAVASCRIPT) | Magnitude: 126.4 | Delta: **0.159 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 96, state_mutation: 69, structural_boundaries: 32, branch: 19
- `js/global.js` (JAVASCRIPT) | Magnitude: 38.2 | Delta: **0.268 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 21, state_mutation: 18, globals: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `request.cgi` (PERL) | Magnitude: 257.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 231, state_mutation: 159, structural_boundaries: 70, branch: 62
- `report.cgi` (PERL) | Magnitude: 2825.35 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 231, indent_spaces: 195, branch: 108, structural_boundaries: 96
- `contrib/syncLDAP.pl` (PERL) | Magnitude: 1.22 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 168, state_mutation: 102, branch: 90, structural_boundaries: 47
- `Bugzilla/Hook.pm` (PERL) | Magnitude: 95.02 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 367, branch: 217, decorators: 124, structural_boundaries: 117
- `Bugzilla/Install/Filesystem.pm` (PERL) | Magnitude: 580.6 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 596, state_mutation: 202, structural_boundaries: 170, branch: 151

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `js/yui/fonts/fonts-min.css` (CSS) | Magnitude: 0.53 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: globals: 1, ownership: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `js/params.js` -> **Severity: 0.738** (Embedded: 0.008 * Error Risk: 92.4142%)
- `query.cgi` -> **Severity: 0.456** (Embedded: 0.0048 * Error Risk: 95.213%)
- `js/field.js` -> **Severity: 0.44** (Embedded: 0.0048 * Error Risk: 91.8548%)
- `Bugzilla/Template.pm` -> **Severity: 0.311** (Embedded: 0.0032 * Error Risk: 97.4874%)
- `js/comments.js` -> **Severity: 0.156** (Embedded: 0.0016 * Error Risk: 97.7344%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Bugzilla/Auth/Login/Env.pm` -> **Severity: 229.994** (Blast Radius: 2.543 * Doc Risk: 90.4421%)
- `js/params.js` -> **Severity: 181.631** (Blast Radius: 7.218 * Doc Risk: 25.1636%)
- `Bugzilla/FlagType.pm` -> **Severity: 135.773** (Blast Radius: 1.375 * Doc Risk: 98.7442%)
- `Bugzilla/BugUrl/Bugzilla.pm` -> **Severity: 119.354** (Blast Radius: 1.375 * Doc Risk: 86.8032%)
- `extensions/MoreBugUrl/Extension.pm` -> **Severity: 112.824** (Blast Radius: 1.375 * Doc Risk: 82.0538%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
