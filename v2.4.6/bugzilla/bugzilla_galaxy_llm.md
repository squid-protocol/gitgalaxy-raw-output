# ARCHITECTURAL_BRIEF: bugzilla
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/bugzilla` |
| **Timestamp** | `2026-08-03T19:24:53.276494+00:00` |
| **Scan Duration** | `2.28s` |
| **Git Branch** | `5.2` |
| **Git Commit** | `4299886770979cfb98c7417a6094c36a3ab19c00` |
| **Git Remote** | `https://github.com/bugzilla/bugzilla` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 29 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.03`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 343 | 54.7% |
| file_cluster_0 | 140 | 22.3% |
| file_cluster_13 | 94 | 15.0% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 32.4 | 11.7 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 24.6 | 6.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 43.1 | 20.4 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 17.2 | 2.3 | 2.3 |
| API Exposure | 0.0 | 14.3 | 2.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 96.9 | 0.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 45.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 24.5 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 96.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 52.1 | 51.8 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 18.0 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 22.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `name` (@ `Bugzilla/User.pm`) -> Impact: **5725.9** | LOC: 2060
  * *Intent:* ################################################################################ # Methods ###########################################################...
- `_check_groups` (@ `Bugzilla/Bug.pm`) -> Impact: **4495.1** | LOC: 2092
- `TO_JSON` (@ `Bugzilla/Object.pm`) -> Impact: **4195.4** | LOC: 1544
  * *Intent:* # This allows the JSON-RPC interface to return Bugzilla::Object instances # as though they were hashes. In the future, this may be modified to return ...
- `DiffDate` (@ `buglist.cgi`) -> Impact: **3665.7** | LOC: 999
  * *Intent:* ################################################################################ # Utilities #########################################################...
- `comments` (@ `Bugzilla/WebService/Bug.pm`) -> Impact: **3001.0** | LOC: 1961
- `set_name` (@ `Bugzilla/Product.pm`) -> Impact: **2735.7** | LOC: 673
- `init_page` (@ `Bugzilla.pm`) -> Impact: **2365.8** | LOC: 1029
  * *Intent:* ##################################################################### # Global Code ##################################################################...
- `set_content_type` (@ `Bugzilla/Attachment.pm`) -> Impact: **2249.7** | LOC: 619
  * *Intent:* ############################### #### Validators ###### ###############################
- `_bz_check_dbd` (@ `Bugzilla/DB.pm`) -> Impact: **2247.9** | LOC: 2401
- `DB_COLUMNS` (@ `Bugzilla/Bug.pm`) -> Impact: **2050.9** | LOC: 1421
  * *Intent:* # This is a sub because it needs to call other subroutines.

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `set_content_type` (@ `Bugzilla/Attachment.pm`) -> **O(2^N) [Recursive]**
  * *Intent:* ############################### #### Validators ###### ###############################
- `datasize` (@ `Bugzilla/Attachment.pm`) -> **O(2^N) [Recursive]**
  * *Intent:* # datasize is a property of the data itself, and it's unclear whether we should # expose it at all, since you can easily derive it from the data itsel...
- `data` (@ `Bugzilla/Attachment.pm`) -> **O(2^N) [Recursive]**
- `relationships` (@ `Bugzilla/BugMail.pm`) -> **O(2^N) [Recursive]**
- `check_etag` (@ `Bugzilla/CGI.pm`) -> **O(2^N) [Recursive]**
- `set_name` (@ `Bugzilla/Component.pm`) -> **O(2^N) [Recursive]**
- `set_column` (@ `Bugzilla/DB/Schema.pm`) -> **O(2^N) [Recursive]**
- `get_add_index_ddl` (@ `Bugzilla/DB/Schema.pm`) -> **O(2^N) [Recursive]**
- `get_add_column_ddl` (@ `Bugzilla/DB/Schema.pm`) -> **O(2^N) [Recursive]**
  * *Intent:* #--------------------------------------------------------------------------
- `visibility_values` (@ `Bugzilla/Field.pm`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `COLUMNS` (@ `Bugzilla/Search.pm`) -> DB Complexity: **362**
  * *Intent:* # 2. name: The name of the column in the database (may also be an expression # that returns the value of the column); # # 3. title: The title of the c...
- `name` (@ `Bugzilla/User.pm`) -> DB Complexity: **329**
  * *Intent:* ################################################################################ # Methods ###########################################################...
- `_check_groups` (@ `Bugzilla/Bug.pm`) -> DB Complexity: **317**
- `TO_JSON` (@ `Bugzilla/Object.pm`) -> DB Complexity: **301**
  * *Intent:* # This allows the JSON-RPC interface to return Bugzilla::Object instances # as though they were hashes. In the future, this may be modified to return ...
- `_add_longdescs_already_wrapped` (@ `Bugzilla/Install/DB.pm`) -> DB Complexity: **272**
- `DB_COLUMNS` (@ `Bugzilla/Bug.pm`) -> DB Complexity: **260**
  * *Intent:* # This is a sub because it needs to call other subroutines.
- `comments` (@ `Bugzilla/WebService/Bug.pm`) -> DB Complexity: **251**
- `_bz_check_dbd` (@ `Bugzilla/DB.pm`) -> DB Complexity: **223**
- `_user_nonchanged` (@ `Bugzilla/Search.pm`) -> DB Complexity: **196**
  * *Intent:* # For all the "user" fields--assigned_to, reporter, qa_contact, # cc, commenter, requestee, etc.
- `DiffDate` (@ `buglist.cgi`) -> DB Complexity: **159**
  * *Intent:* ################################################################################ # Utilities #########################################################...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `Bugzilla` | 44 | 70155.18 | 48.48% | 52.19% |
| `__monolith__` | 70 | 32353.26 | 76.24% | 41.64% |
| `Bugzilla/Install` | 6 | 9173.2 | 57.46% | 21.71% |
| `Bugzilla/DB` | 7 | 9066.8 | 46.1% | 29.22% |
| `Bugzilla/WebService` | 13 | 6281.7 | 24.82% | 42.08% |
| `js` | 14 | 3795.88 | 66.38% | 61.18% |
| `Bugzilla/WebService/Server` | 3 | 2866.78 | 67.67% | 56.04% |
| `Bugzilla/DB/Schema` | 5 | 2573.46 | 59.05% | 11.65% |
| `t` | 13 | 2358.33 | 90.27% | 24.79% |
| `template/en/default/bug` | 20 | 2291.12 | 5.7% | 79.08% |

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
- `js/util.js` -> **9** Orphaned Functions | **0** Duplicates
- `js/change-columns.js` -> **6** Orphaned Functions | **0** Duplicates
- `js/global.js` -> **6** Orphaned Functions | **0** Duplicates
- `Bugzilla/Install/DB.pm` -> **4** Orphaned Functions | **0** Duplicates
- `js/custom-search.js` -> **4** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`contrib/bugzilla-submit/bugzilla-submit`** -> AI Confidence: **99.39%**
2. **`contrib/jb2bz.py`** -> AI Confidence: **99.31%**
3. **`Dockerfile`** -> AI Confidence: **99.29%**
4. **`contrib/cmdline/buglist`** -> AI Confidence: **99.29%**
5. **`contrib/cmdline/makequery`** -> AI Confidence: **99.29%**
6. **`template/en/default/bug/field-events.js.tmpl`** -> AI Confidence: **99.29%**
7. **`template/en/default/global/calendar.js.tmpl`** -> AI Confidence: **99.29%**
8. **`docker/startup.sh`** -> AI Confidence: **99.17%**
9. **`contrib/cmdline/bugcount`** -> AI Confidence: **99.06%**
10. **`js/TUI.js`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `Bugzilla/Attachment.pm` -> **100.0%** Exposure
- `Bugzilla/Attachment/PatchReader.pm` -> **100.0%** Exposure
- `Bugzilla/Auth/Login/Cookie.pm` -> **100.0%** Exposure
- `Bugzilla/Auth/Persist/Cookie.pm` -> **100.0%** Exposure
- `Bugzilla/Auth/Verify.pm` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `Bugzilla/Auth/Login.pm` -> **100.0%** Exposure
- `Bugzilla/Extension.pm` -> **100.0%** Exposure
- `Bugzilla/Install.pm` -> **100.0%** Exposure
- `contrib/mysqld-watcher.pl` -> **100.0%** Exposure
- `contrib/recode.pl` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `Bugzilla.pm` -> **100.0%** Exposure
- `Bugzilla/Attachment.pm` -> **100.0%** Exposure
- `Bugzilla/Auth/Login/Cookie.pm` -> **100.0%** Exposure
- `Bugzilla/Auth/Login/Stack.pm` -> **100.0%** Exposure
- `Bugzilla/Auth/Persist/Cookie.pm` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3044` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `js/comment-tagging.js` (JAVASCRIPT) -> Cumulative Risk: **898.87**
- **Archetype:** `file_cluster_8` (Distance: 12.804 IQR)
- **Magnitude:** 591.86 | **LOC:** 388 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `updateCollapseControls` (Impact: 67.0), `add` (Impact: 46.5), `onKeyPress` (Impact: 29.4)

### 2. `js/bug.js` (JAVASCRIPT) -> Cumulative Risk: **804.96**
- **Archetype:** `file_cluster_8` (Distance: 11.706 IQR)
- **Magnitude:** 293.04 | **LOC:** 244 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `set_assign_to` (Impact: 130.8), `doBeforeParseData` (Impact: 21.6), `update` (Impact: 20.8)

### 3. `js/change-columns.js` (JAVASCRIPT) -> Cumulative Risk: **801.83**
- **Archetype:** `file_cluster_2` (Distance: 11.93 IQR)
- **Magnitude:** 167.7 | **LOC:** 133 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.997%)
- **Heaviest Functions:** `updateView` (Impact: 36.3), `move_up` (Impact: 14.7), `move_down` (Impact: 14.7)

### 4. `contrib/jb2bz.py` (PYTHON) -> Cumulative Risk: **795.55**
- **Archetype:** `file_cluster_8` (Distance: 9.952 IQR)
- **Magnitude:** 4.51 | **LOC:** 350 | **CtrlFlow:** 67.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `add_notes` (Impact: 337.0), `main` (Impact: 44.5), `process_reply_file` (Impact: 37.4)

### 5. `Bugzilla/Attachment/PatchReader.pm` (PERL) -> Cumulative Risk: **785.7**
- **Archetype:** `file_cluster_0` (Distance: 12.465 IQR)
- **Magnitude:** 503.58 | **LOC:** 333 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9998%)
- **Heaviest Functions:** `process_interdiff` (Impact: 289.9), `process_diff` (Impact: 90.1)

### 6. `js/custom-search.js` (JAVASCRIPT) -> Cumulative Risk: **777.89**
- **Archetype:** `file_cluster_8` (Distance: 12.349 IQR)
- **Magnitude:** 409.64 | **LOC:** 345 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9962%)
- **Heaviest Functions:** `_cs_trigger_j_listeners` (Impact: 63.2), `_cs_j_change` (Impact: 56.0), `_cs_add_listeners` (Impact: 42.4)

### 7. `js/expanding-tree.js` (JAVASCRIPT) -> Cumulative Risk: **775.91**
- **Archetype:** `file_cluster_8` (Distance: 10.521 IQR)
- **Magnitude:** 222.24 | **LOC:** 143 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), State Flux (99.9842%), Tech Debt (99.7808%)
- **Heaviest Functions:** `changeChildren` (Impact: 140.2), `duplicated` (Impact: 31.4), `duplicatedout` (Impact: 8.1)

### 8. `extensions/Voting/Extension.pm` (PERL) -> Cumulative Risk: **773.81**
- **Archetype:** `file_cluster_0` (Distance: 12.562 IQR)
- **Magnitude:** 1036.32 | **LOC:** 924 | **CtrlFlow:** 49.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_page_user` (Impact: 239.9), `_modify_bug_votes` (Impact: 112.9), `_update_votes` (Impact: 68.4)

### 9. `contrib/cmdline/makequery` (SHELL) -> Cumulative Risk: **763.25**
- **Archetype:** `file_cluster_11` (Distance: 16.213 IQR)
- **Magnitude:** 1.64 | **LOC:** 96 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Cognitive Load (99.9996%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 80.3), `__global_context__` (Impact: 1.5)

### 10. `Bugzilla/Migrate/Gnats.pm` (PERL) -> Cumulative Risk: **763.22**
- **Archetype:** `file_cluster_13` (Distance: 13.279 IQR)
- **Magnitude:** 884.38 | **LOC:** 749 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_store_audit_change` (Impact: 152.7), `_parse_audit_trail` (Impact: 79.4), `translate_bug` (Impact: 59.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Bugzilla/Bug.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.45 IQR)
- **Top Global Matches:** file_cluster_0: 14.45, file_cluster_8: 14.518, file_cluster_13: 14.548
- **Magnitude:** 9861.86 | **LOC:** 5124 | **CtrlFlow:** 50.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 317
- **Risk Profile:** Cognitive Load (73.8361%), Tech Debt (99.8742%)
**Top Internal Functions/Classes:**
  * `_check_groups` (Impact: 4495.1 | O(N^6) | DB: 317)
  * `DB_COLUMNS` (Impact: 2050.9 | O(N^6) | DB: 260)
    * *Intent:* # This is a sub because it needs to call other subroutines.
  * `_check_bug_status` (Impact: 166.1 | O(N^3) | DB: 14)
  * `check_can_change_field` (Impact: 107.9 | O(N^2) | DB: 18)
    * *Intent:* # can add code here for site-specific policy changes, according to the # instructions given in the B...
  * `get_activity` (Impact: 105.8 | O(N^6) | DB: 20)
    * *Intent:* # Get the activity of a bug, starting from $starttime (if given). # This routine assumes Bugzilla::B...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1349`, `structural_boundaries: 1327`, `args: 151`, `func_start: 194`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 2234`, `dead_code: 5`, `fragile_debt: 215`
* *Architecture:* `api: 1`, `import: 40`
* *Defense:* `safety: 10`, `doc: 140`, `cleanup: 84`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Scalar::Util, Bugzilla::Error, longer, Bugzilla::BugMail, if, Bugzilla::Attachment, base, set_bug_status...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/User.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.088 IQR)
- **Top Global Matches:** file_cluster_0: 14.088, file_cluster_13: 14.129, file_cluster_8: 14.205
- **Magnitude:** 7516.08 | **LOC:** 3408 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 329
- **Risk Profile:** Cognitive Load (49.9717%), Tech Debt (68.4454%)
**Top Internal Functions/Classes:**
  * `name` (Impact: 5725.9 | O(2^N) | DB: 329)
    * *Intent:* ################################################################################ # Methods #########...
  * `DB_COLUMNS` (Impact: 440.3 | O(N^5) | DB: 82)
    * *Intent:* # XXX Note that Bugzilla::User->name does not return the same thing # that you passed in for "name" ...
  * `validate_password_check` (Impact: 48.4 | O(N^1) | DB: 1)
  * `login_to_id` (Impact: 29.4 | O(N^3) | DB: 4)
    * *Intent:* # This is used in a few performance-critical areas where we don't want to # do check() and pull all ...
  * `validate_password` (Impact: 2.2 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1000`, `structural_boundaries: 666`, `args: 111`, `func_start: 116`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1222`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 50`
* *Architecture:* `io: 19`, `api: 1`, `import: 55`
* *Defense:* `safety: 2`, `doc: 164`, `cleanup: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Scalar::Util, Bugzilla::Error, Bugzilla::BugMail, a, base, Bugzilla::Search::Recent, arguments, match...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editusers.cgi` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.285 IQR)
- **Top Global Matches:** file_cluster_8: 12.285, file_cluster_0: 12.42, file_cluster_13: 12.482
- **Magnitude:** 5149.32 | **LOC:** 776 | **CtrlFlow:** 59.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (83.7249%), Tech Debt (43.5846%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 152`, `args: 3`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 282`, `fragile_debt: 8`
* *Architecture:* `import: 15`
* *Defense:* `safety: 2`, `cleanup: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bugzilla::Constants, warnings, Bugzilla::Error, Bugzilla::User, lib, strict, Bugzilla::Token, Bugzilla::Group...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Object.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.377 IQR)
- **Top Global Matches:** file_cluster_0: 13.377, file_cluster_13: 13.381, file_cluster_8: 13.577
- **Magnitude:** 4746.28 | **LOC:** 1595 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 301
- **Risk Profile:** Cognitive Load (42.2089%), Tech Debt (20.9718%)
**Top Internal Functions/Classes:**
  * `TO_JSON` (Impact: 4195.4 | O(2^N) | DB: 301)
    * *Intent:* # This allows the JSON-RPC interface to return Bugzilla::Object instances # as though they were hash...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 431`, `structural_boundaries: 497`, `args: 43`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `state_mutation: 530`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 6`
* *Architecture:* `io: 37`, `import: 34`
* *Defense:* `safety: 7`, `doc: 132`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Scalar::Util, Bugzilla::Error, DEFAULT, List::MoreUtils, by, Date::Parse, matches, constant...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Install/DB.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.99 IQR)
- **Top Global Matches:** file_cluster_8: 12.99, file_cluster_0: 13.233, file_cluster_13: 13.279
- **Magnitude:** 4634.76 | **LOC:** 4300 | **CtrlFlow:** 48.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 272
- **Risk Profile:** Cognitive Load (90.0601%), Tech Debt (99.9653%)
**Top Internal Functions/Classes:**
  * `_add_longdescs_already_wrapped` (Impact: 1997.4 | O(N^6) | DB: 272)
  * `_write_one_longdesc` (Impact: 186.8 | O(2^N) | DB: 27)
    * *Intent:* # A helper for the function below.
  * `_convert_groups_system_from_groupset` (Impact: 154.6 | O(N^6) | DB: 35)
  * `_copy_old_charts_into_database` (Impact: 142.2 | O(N^4) | DB: 39)
  * `_convert_attachment_statuses_to_flags` (Impact: 98.6 | O(N^6) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 708`, `structural_boundaries: 758`, `args: 11`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `state_mutation: 1334`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 134`, `orphaned_logic: 4`
* *Architecture:* `io: 9`, `import: 22`
* *Defense:* `safety: 5`, `doc: 8`, `cleanup: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` longer, files, Digest, stats, URI, List::MoreUtils, Date::Parse, Date::Format...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Search.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.988 IQR)
- **Top Global Matches:** file_cluster_8: 13.988, file_cluster_13: 14.073, file_cluster_0: 14.095
- **Magnitude:** 4516.98 | **LOC:** 3562 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 362
- **Risk Profile:** Cognitive Load (85.4091%), Tech Debt (24.1083%)
**Top Internal Functions/Classes:**
  * `COLUMNS` (Impact: 1677.7 | O(2^N) | DB: 362)
    * *Intent:* # 2. name: The name of the column in the database (may also be an expression # that returns the valu...
  * `_user_nonchanged` (Impact: 1102.8 | O(N^6) | DB: 196)
    * *Intent:* # For all the "user" fields--assigned_to, reporter, qa_contact, # cc, commenter, requestee, etc.
  * `_contact_exact_group` (Impact: 23.7 | O(N^1) | DB: 19)
  * `COLUMN_JOINS` (Impact: 10.1 | O(N^2) | DB: 4)
    * *Intent:* # This describes tables that must be joined when you want to display # certain columns in the buglis...
  * `SqlifyDate` (Impact: 9.3 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 652`, `structural_boundaries: 979`, `args: 128`, `func_start: 132`, `class_start: 1`
* *Risk/State:* `state_mutation: 1620`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 21`
* *Architecture:* `io: 4`, `api: 1`, `import: 41`
* *Defense:* `safety: 2`, `doc: 39`, `test: 3`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Bugzilla::Search::Condition, Scalar::Util, values, Time::HiRes, Bugzilla::Error, override, base, table...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `buglist.cgi` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.376 IQR)
- **Top Global Matches:** file_cluster_0: 13.376, file_cluster_17: 13.421, file_cluster_13: 13.489
- **Magnitude:** 4199.28 | **LOC:** 1166 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 159
- **Risk Profile:** Cognitive Load (85.1996%), Tech Debt (99.998%)
**Top Internal Functions/Classes:**
  * `DiffDate` (Impact: 3665.7 | O(2^N) | DB: 159)
    * *Intent:* ################################################################################ # Utilities #######...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 304`, `structural_boundaries: 181`, `args: 7`, `func_start: 7`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 519`, `dead_code: 2`, `fragile_debt: 64`
* *Architecture:* `import: 18`
* *Defense:* `safety: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bugzilla::Error, for, Bugzilla::Search::Quicksearch, control, Bugzilla::Search::Recent, Bugzilla::Bug, QuickSearch, Bugzilla...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Template.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.181 IQR)
- **Top Global Matches:** file_cluster_0: 14.181, file_cluster_13: 14.308, file_cluster_11: 14.39
- **Magnitude:** 4194.28 | **LOC:** 1439 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 127
- **Risk Profile:** Cognitive Load (73.4128%), Tech Debt (97.7491%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 2034.9 | O(2^N) | DB: 127)
    * *Intent:* # Construct the Template object # Note that all of the failure cases here can't use templateable err...
  * `SAFE_URL_REGEXP` (Impact: 1232.4 | O(2^N) | DB: 70)
    * *Intent:* # Pseudo-constant.
  * `get_bug_link` (Impact: 57.9 | O(N^1) | DB: 20)
    * *Intent:* # Creates a link to a bug, including its title. # It takes either two or three parameters: # - The b...
  * `_css_url_rewrite` (Impact: 31.8 | O(N^1) | DB: 15)
  * `_css_link_set` (Impact: 23.7 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 498`, `structural_boundaries: 325`, `args: 49`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 764`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 36`
* *Architecture:* `io: 3`, `api: 1`, `import: 33`
* *Defense:* `safety: 5`, `doc: 25`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003195
  * `Imports (Out-Degree: 1):` Digest::MD5, Scalar::Util, Bugzilla::Error, base, MIME::Base64, Bugzilla::Bug, Bugzilla::WebService::Constants, colon...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Bugzilla/Product.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.185 IQR)
- **Top Global Matches:** file_cluster_0: 13.185, file_cluster_13: 13.263, file_cluster_8: 13.462
- **Magnitude:** 3939.78 | **LOC:** 1186 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 90
- **Risk Profile:** Cognitive Load (51.02%), Tech Debt (68.2955%)
**Top Internal Functions/Classes:**
  * `set_name` (Impact: 2735.7 | O(2^N) | DB: 90)
  * `update` (Impact: 403.1 | O(2^N) | DB: 25)
  * `remove_from_db` (Impact: 209.3 | O(2^N) | DB: 7)
  * `create` (Impact: 35.7 | O(2^N) | DB: 10)
    * *Intent:* ############################### #### Constructors ##### ###############################
  * `_create_bug_group` (Impact: 29.4 | O(N^3) | DB: 6)
    * *Intent:* ############################### #### Methods #### ###############################
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 359`, `structural_boundaries: 275`, `args: 28`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 405`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 17`
* *Architecture:* `io: 5`, `api: 2`, `import: 32`
* *Defense:* `safety: 2`, `doc: 56`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Scalar::Util, Bugzilla::Error, longer, base, Bugzilla::Bug, problem, Bugzilla::Status, Bugzilla::Group...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/WebService/Bug.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.261 IQR)
- **Top Global Matches:** file_cluster_8: 13.261, file_cluster_7: 13.279, file_cluster_13: 13.317
- **Magnitude:** 3862.86 | **LOC:** 4693 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 251
- **Risk Profile:** Cognitive Load (20.8229%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `comments` (Impact: 3001.0 | O(2^N) | DB: 251)
  * `_legal_field_values` (Impact: 137.3 | O(N^3) | DB: 19)
  * `fields` (Impact: 60.5 | O(2^N) | DB: 14)
    * *Intent:* ########### # Methods # ###########
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 763`, `structural_boundaries: 593`, `args: 16`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 603`, `fragile_debt: 448`
* *Architecture:* `io: 66`, `api: 1`, `import: 58`
* *Defense:* `safety: 5`, `doc: 812`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` with, Bugzilla::Error, longer, Bugzilla::BugMail, aliases, Bugzilla::Search::Quicksearch, a, extra...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `report.cgi` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.941 IQR)
- **Top Global Matches:** file_cluster_0: 12.941, file_cluster_8: 12.951, file_cluster_13: 12.964
- **Magnitude:** 3593.62 | **LOC:** 442 | **CtrlFlow:** 60.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (90.1315%), Tech Debt (47.5186%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 93`, `args: 4`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 239`, `fragile_debt: 4`
* *Architecture:* `import: 12`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bugzilla::Search, Bugzilla::Constants, warnings, Bugzilla::Error, lib, strict, Bugzilla::Token, Bugzilla::Report...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `testserver.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.093 IQR)
- **Top Global Matches:** file_cluster_0: 13.093, file_cluster_13: 13.181, file_cluster_8: 13.414
- **Magnitude:** 3527.1 | **LOC:** 306 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (90.3701%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 65`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 199`
* *Architecture:* `io: 14`, `import: 14`
* *Defense:* `safety: 6`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bugzilla::Constants, warnings, GD, https, Template::Plugin::GD::Image, lib, strict, LWP::UserAgent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB/Schema.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.177 IQR)
- **Top Global Matches:** file_cluster_8: 12.177, file_cluster_0: 12.317, file_cluster_13: 12.418
- **Magnitude:** 3283.22 | **LOC:** 3189 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 93
- **Risk Profile:** Cognitive Load (16.7139%), Tech Debt (13.1885%)
**Top Internal Functions/Classes:**
  * `set_column` (Impact: 1365.4 | O(2^N) | DB: 93)
  * `get_alter_column_ddl` (Impact: 252.4 | O(2^N) | DB: 19)
  * `get_add_index_ddl` (Impact: 142.6 | O(2^N) | DB: 4)
  * `get_add_column_ddl` (Impact: 122.0 | O(2^N) | DB: 9)
    * *Intent:* #--------------------------------------------------------------------------
  * `get_table_ddl` (Impact: 85.0 | O(2^N) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 381`, `structural_boundaries: 272`, `args: 54`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `state_mutation: 437`, `dead_code: 6`, `planned_debt: 3`, `fragile_debt: 8`
* *Architecture:* `io: 63`, `import: 31`
* *Defense:* `safety: 5`, `doc: 169`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Digest::MD5, simple, Bugzilla::Error, a, Bugzilla::DB::Schema, DEFAULT, List::MoreUtils, Moo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.427 IQR)
- **Top Global Matches:** file_cluster_8: 13.427, file_cluster_13: 13.431, file_cluster_7: 13.492
- **Magnitude:** 2846.46 | **LOC:** 3011 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 223
- **Risk Profile:** Cognitive Load (42.6437%), Tech Debt (15.6224%)
**Top Internal Functions/Classes:**
  * `_bz_check_dbd` (Impact: 2247.9 | O(N^6) | DB: 223)
  * `bz_check_requirements` (Impact: 14.9 | O(N^1) | DB: 4)
  * `_connect` (Impact: 9.6 | O(N^1) | DB: 2)
  * `quote` (Impact: 6.0 | O(2^N) | DB: 3)
    * *Intent:* ##################################################################### # Overridden Superclass Method...
  * `_handle_error` (Impact: 4.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 436`, `structural_boundaries: 422`, `args: 73`, `func_start: 78`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 521`, `dead_code: 2`, `fragile_debt: 5`, `orphaned_logic: 1`
* *Architecture:* `io: 23`, `import: 38`
* *Defense:* `safety: 10`, `doc: 464`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FK, Scalar::Util, handles, now, Bugzilla::Error, longer, Bugzilla::DB::Schema, DEFAULT...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Attachment.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.162 IQR)
- **Top Global Matches:** file_cluster_13: 13.162, file_cluster_0: 13.171, file_cluster_8: 13.44
- **Magnitude:** 2724.66 | **LOC:** 1056 | **CtrlFlow:** 56.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 97
- **Risk Profile:** Cognitive Load (48.6124%), Tech Debt (99.9945%)
**Top Internal Functions/Classes:**
  * `set_content_type` (Impact: 2249.7 | O(2^N) | DB: 97)
    * *Intent:* ############################### #### Validators ###### ###############################
  * `datasize` (Impact: 70.6 | O(2^N) | DB: 8)
    * *Intent:* # datasize is a property of the data itself, and it's unclear whether we should # expose it at all, ...
  * `data` (Impact: 50.7 | O(2^N) | DB: 11)
  * `bug` (Impact: 12.2 | O(2^N))
  * `flag_types` (Impact: 12.0 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 198`, `args: 20`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 297`, `dead_code: 1`, `fragile_debt: 54`
* *Architecture:* `io: 9`, `api: 1`, `import: 30`
* *Defense:* `safety: 4`, `doc: 100`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` File::Copy, Bugzilla::Error, attachment, Bugzilla::Attachment, base, Bugzilla::Bug, effect, constant...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.878 IQR)
- **Top Global Matches:** file_cluster_13: 12.878, file_cluster_0: 12.916, file_cluster_8: 13.225
- **Magnitude:** 2595.56 | **LOC:** 1107 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 91
- **Risk Profile:** Cognitive Load (40.6234%), Tech Debt (12.7403%)
**Top Internal Functions/Classes:**
  * `init_page` (Impact: 2365.8 | O(2^N) | DB: 91)
    * *Intent:* ##################################################################### # Global Code ################...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 406`, `structural_boundaries: 289`, `args: 23`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 215`, `fragile_debt: 2`
* *Architecture:* `io: 6`, `import: 48`
* *Defense:* `safety: 7`, `doc: 71`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` error, Bugzilla::Error, Bugzilla::Memcached, for, Bugzilla::Config, currently, shadow, Bugzilla...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/CGI.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.39 IQR)
- **Top Global Matches:** file_cluster_0: 13.39, file_cluster_13: 13.512, file_cluster_8: 13.654
- **Magnitude:** 2563.68 | **LOC:** 844 | **CtrlFlow:** 63.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 91
- **Risk Profile:** Cognitive Load (56.9355%), Tech Debt (50.1278%)
**Top Internal Functions/Classes:**
  * `check_etag` (Impact: 1982.1 | O(2^N) | DB: 91)
  * `new` (Impact: 102.2 | O(2^N) | DB: 9)
  * `clean_search_url` (Impact: 76.9 | O(N^2) | DB: 19)
  * `canonicalise_query` (Impact: 24.8 | O(N^2) | DB: 5)
    * *Intent:* # We want this sorted plus the ability to exclude certain params
  * `_init_bz_cgi_globals` (Impact: 7.9 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 138`, `args: 26`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 356`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 7`
* *Architecture:* `api: 4`, `import: 13`
* *Defense:* `safety: 2`, `doc: 30`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::Error, a, base, Bugzilla::Search::Recent, C, need, L, File::Basename...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Token.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.823 IQR)
- **Top Global Matches:** file_cluster_0: 12.823, file_cluster_13: 12.954, file_cluster_8: 13.151
- **Magnitude:** 2294.44 | **LOC:** 693 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 67
- **Risk Profile:** Cognitive Load (56.2885%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `IssueEmailChangeToken` (Impact: 2049.3 | O(2^N) | DB: 67)
  * `issue_new_user_account_token` (Impact: 19.7 | O(N^4) | DB: 6)
    * *Intent:* # Creates and sends a token to create a new user account. # It assumes that the login has the correc...
  * `issue_api_token` (Impact: 6.7 | O(N^3) | DB: 2)
    * *Intent:* ################################################################################ # Public Functions ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 129`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 209`
* *Architecture:* `api: 1`, `import: 19`
* *Defense:* `safety: 3`, `doc: 27`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Bugzilla::Error, Digest::SHA, longer, for, base, account, Date::Format, Date::Parse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Util.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.717 IQR)
- **Top Global Matches:** file_cluster_13: 13.717, file_cluster_0: 13.796, file_cluster_8: 13.856
- **Magnitude:** 2285.72 | **LOC:** 1361 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 75
- **Risk Profile:** Cognitive Load (48.4609%), Tech Debt (13.707%)
**Top Internal Functions/Classes:**
  * `validate_date` (Impact: 1138.3 | O(2^N) | DB: 61)
  * `css_class_quote` (Impact: 393.5 | O(N^3) | DB: 75)
  * `html_quote` (Impact: 89.7 | O(N^2) | DB: 52)
    * *Intent:* # Bug 120030: Override html filter to obscure the '@' in user # visible strings. # Bug 319331: Handl...
  * `datetime_from` (Impact: 37.5 | O(N^1) | DB: 8)
  * `validate_email_syntax` (Impact: 21.2 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 381`, `structural_boundaries: 272`, `args: 33`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `state_mutation: 553`, `fragile_debt: 3`
* *Architecture:* `io: 6`, `api: 1`, `import: 31`
* *Defense:* `safety: 3`, `doc: 86`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Scalar::Util, Bugzilla::Error, attributes, Digest, SERVER_SOFTWARE, a, base, format...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Group.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.229 IQR)
- **Top Global Matches:** file_cluster_13: 13.229, file_cluster_0: 13.276, file_cluster_8: 13.379
- **Magnitude:** 2197.76 | **LOC:** 733 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 96
- **Risk Profile:** Cognitive Load (41.4285%), Tech Debt (36.8152%)
**Top Internal Functions/Classes:**
  * `description` (Impact: 1904.3 | O(2^N) | DB: 96)
    * *Intent:* ############################### #### Accessors ###### ###############################
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 167`, `args: 23`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `state_mutation: 282`, `fragile_debt: 6`
* *Architecture:* `api: 1`, `import: 19`
* *Defense:* `safety: 3`, `doc: 61`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::Constants, warnings, Bugzilla::Error, Bugzilla::User, strict, Bugzilla::Group, Bugzilla::Product, Bugzilla::Config...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Component.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.884 IQR)
- **Top Global Matches:** file_cluster_0: 12.884, file_cluster_13: 13.013, file_cluster_8: 13.234
- **Magnitude:** 2068.66 | **LOC:** 687 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (54.2434%), Tech Debt (92.1814%)
**Top Internal Functions/Classes:**
  * `set_name` (Impact: 1619.6 | O(2^N) | DB: 40)
  * `remove_from_db` (Impact: 52.7 | O(2^N) | DB: 5)
  * `_update_cc_list` (Impact: 49.7 | O(N^6) | DB: 4)
    * *Intent:* ############################### #### Methods #### ###############################
  * `new` (Impact: 41.0 | O(2^N) | DB: 12)
    * *Intent:* ###############################
  * `_check_name` (Impact: 23.3 | O(N^1) | DB: 3)
    * *Intent:* ################################ # Validators ################################
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 147`, `args: 24`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 215`, `planned_debt: 1`, `fragile_debt: 14`
* *Architecture:* `api: 1`, `import: 22`
* *Defense:* `safety: 2`, `doc: 34`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::Constants, warnings, Scalar::Util, Bugzilla::Error, Bugzilla::User, strict, Bugzilla::Product, Bugzilla::Series...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Install.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.203 IQR)
- **Top Global Matches:** file_cluster_0: 12.203, file_cluster_13: 12.288, file_cluster_8: 12.515
- **Magnitude:** 2025.64 | **LOC:** 527 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 59
- **Risk Profile:** Cognitive Load (53.8023%), Tech Debt (99.6725%)
**Top Internal Functions/Classes:**
  * `SETTINGS` (Impact: 1886.4 | O(2^N) | DB: 59)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 92`, `args: 4`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 132`, `fragile_debt: 19`
* *Architecture:* `io: 5`, `import: 18`
* *Defense:* `safety: 7`, `doc: 21`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, Bugzilla::Constants, Bugzilla::Error, Bugzilla::User, strict, editbugs, Bugzilla::Install, Bugzilla::Group...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/Install/Util.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.812 IQR)
- **Top Global Matches:** file_cluster_13: 13.812, file_cluster_0: 13.821, file_cluster_17: 14.1
- **Magnitude:** 1909.62 | **LOC:** 917 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 147
- **Risk Profile:** Cognitive Load (42.3249%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_version_and_os` (Impact: 1457.7 | O(2^N) | DB: 147)
  * `bin_loc` (Impact: 27.3 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 191`, `args: 17`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 411`, `dead_code: 2`
* *Architecture:* `io: 5`, `api: 2`, `import: 24`
* *Defense:* `safety: 9`, `doc: 58`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Scalar::Util, based, Term::ANSIColor, base, Template, extension_requirement_packages, Bugzilla, Win32::Console::ANSI...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB/MariaDB.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.973 IQR)
- **Top Global Matches:** file_cluster_0: 12.973, file_cluster_13: 12.982, file_cluster_8: 13.001
- **Magnitude:** 1886.0 | **LOC:** 1301 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 52
- **Risk Profile:** Cognitive Load (66.159%), Tech Debt (46.9175%)
**Top Internal Functions/Classes:**
  * `sql_date_format` (Impact: 652.6 | O(N^6) | DB: 52)
  * `bz_enum_initial_values` (Impact: 642.3 | O(2^N) | DB: 36)
  * `BUILDARGS` (Impact: 108.6 | O(N^2) | DB: 21)
  * `_fix_defaults` (Impact: 50.7 | O(N^3) | DB: 12)
    * *Intent:* # When you import a MySQL 3/4 mysqldump into MySQL 5, columns that # aren't supposed to have default...
  * `default_row_format` (Impact: 13.6 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 258`, `args: 31`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 380`, `dead_code: 3`, `fragile_debt: 12`
* *Architecture:* `io: 6`, `import: 16`
* *Defense:* `safety: 1`, `doc: 42`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` with, now, Bugzilla::Error, for, Bugzilla::Config, Text::ParseWords, fetchall_hashref, Moo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Bugzilla/DB/Mysql.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.972 IQR)
- **Top Global Matches:** file_cluster_0: 12.972, file_cluster_13: 12.981, file_cluster_8: 12.999
- **Magnitude:** 1884.2 | **LOC:** 1301 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 52
- **Risk Profile:** Cognitive Load (66.1541%), Tech Debt (46.9175%)
**Top Internal Functions/Classes:**
  * `sql_date_format` (Impact: 652.6 | O(N^6) | DB: 52)
  * `bz_enum_initial_values` (Impact: 642.3 | O(2^N) | DB: 36)
  * `BUILDARGS` (Impact: 108.6 | O(N^2) | DB: 21)
  * `_fix_defaults` (Impact: 50.7 | O(N^3) | DB: 12)
    * *Intent:* # When you import a MySQL 3/4 mysqldump into MySQL 5, columns that # aren't supposed to have default...
  * `default_row_format` (Impact: 11.8 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 258`, `args: 31`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 380`, `dead_code: 3`, `fragile_debt: 12`
* *Architecture:* `io: 6`, `import: 16`
* *Defense:* `safety: 1`, `doc: 42`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` with, now, Bugzilla::Error, for, Bugzilla::Config, Text::ParseWords, Bugzilla::DB::Schema::Mysql, fetchall_hashref...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `contrib/syncLDAP.pl` (PERL) | Magnitude: 1.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 168, branch: 102, state_mutation: 102, structural_boundaries: 46
- `Bugzilla/Config.pm` (PERL) | Magnitude: 401.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 200, branch: 146, state_mutation: 102, structural_boundaries: 68
- `Bugzilla/Search/ClauseGroup.pm` (PERL) | Magnitude: 129.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, branch: 45, structural_boundaries: 31, pointers: 20
- `Bugzilla/Config/Core.pm` (PERL) | Magnitude: 18.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 12, structural_boundaries: 7, decorators: 4, import: 4
- `Bugzilla/Object.pm` (PERL) | Magnitude: 4746.28 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 573, state_mutation: 530, structural_boundaries: 497, branch: 431

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `contrib/cmdline/makequery` (SHELL) | Magnitude: 1.64 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 81, indent_spaces: 57, reflection_metaprogramming: 37, safety_bypasses: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `contrib/cmdline/bugslink` (SHELL) | Magnitude: 0.14 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 9, io: 4, structural_boundaries: 3, reflection_metaprogramming: 3
- `contrib/cmdline/bugcount` (SHELL) | Magnitude: 0.1 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 6, reflection_metaprogramming: 2, orphaned_logic: 2, branch: 1
- `contrib/cmdline/bugids` (SHELL) | Magnitude: 0.14 | Delta: **0.137 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 9, io: 6, reflection_metaprogramming: 3, structural_boundaries: 2
- `contrib/cmdline/buglist` (SHELL) | Magnitude: 0.14 | Delta: **0.31 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 10, reflection_metaprogramming: 5, safety: 2, orphaned_logic: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Bugzilla/Auth/Verify/Stack.pm` (PERL) | Magnitude: 113.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 48, indent_spaces: 45, structural_boundaries: 38, branch: 36
- `contrib/mysqld-watcher.pl` (PERL) | Magnitude: 0.32 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 37, state_mutation: 23, branch: 14, structural_boundaries: 14
- `Bugzilla/Whine/Schedule.pm` (PERL) | Magnitude: 200.88 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 61, state_mutation: 39, structural_boundaries: 33, indent_spaces: 33
- `Bugzilla/Extension.pm` (PERL) | Magnitude: 591.84 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 223, structural_boundaries: 146, indent_spaces: 119, state_mutation: 113
- `colchange.cgi` (PERL) | Magnitude: 86.92 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 100, branch: 75, state_mutation: 69, structural_boundaries: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `Bugzilla/Update.pm` (PERL) | Magnitude: 220.92 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, state_mutation: 96, branch: 77, structural_boundaries: 55
- `js/field.js` (JAVASCRIPT) | Magnitude: 850.7 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 400, state_mutation: 206, branch: 93, structural_boundaries: 84
- `editflagtypes.cgi` (PERL) | Magnitude: 388.02 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 375, state_mutation: 272, branch: 167, structural_boundaries: 125

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `js/change-columns.js` (JAVASCRIPT) | Magnitude: 167.7 | Delta: **0.159 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 96, state_mutation: 69, structural_boundaries: 32, branch: 19
- `js/global.js` (JAVASCRIPT) | Magnitude: 61.8 | Delta: **0.268 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 21, state_mutation: 18, globals: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `Bugzilla/DB.pm` (PERL) | Magnitude: 2846.46 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 857, state_mutation: 521, doc: 464, branch: 436
- `t/007util.t` (PERL) | Magnitude: 26.3 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 31, indent_spaces: 27, structural_boundaries: 17, test: 13
- `Bugzilla/DB/Schema/Sqlite.pm` (PERL) | Magnitude: 351.78 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 207, indent_spaces: 159, structural_boundaries: 81, encapsulation: 57
- `Bugzilla/WebService/Bug.pm` (PERL) | Magnitude: 3862.86 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 1076, doc: 812, branch: 763, state_mutation: 603
- `whine.pl` (PERL) | Magnitude: 372.62 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 354, state_mutation: 336, branch: 141, structural_boundaries: 99

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `js/yui/fonts/fonts-min.css` (CSS) | Magnitude: 0.53 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: globals: 1, ownership: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `js/params.js` -> **Severity: 0.475** (Embedded: 0.008 * Error Risk: 59.4118%)
- `query.cgi` -> **Severity: 0.351** (Embedded: 0.0048 * Error Risk: 73.2341%)
- `Bugzilla/Template.pm` -> **Severity: 0.284** (Embedded: 0.0032 * Error Risk: 88.7884%)
- `js/field.js` -> **Severity: 0.275** (Embedded: 0.0048 * Error Risk: 57.4772%)
- `js/comments.js` -> **Severity: 0.141** (Embedded: 0.0016 * Error Risk: 88.2801%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `js/params.js` -> **Severity: 717.452** (Blast Radius: 7.218 * Doc Risk: 99.3976%)
- `Bugzilla/Auth/Login/Env.pm` -> **Severity: 252.872** (Blast Radius: 2.543 * Doc Risk: 99.4384%)
- `js/field.js` -> **Severity: 224.054** (Blast Radius: 4.296 * Doc Risk: 52.1541%)
- `js/comments.js` -> **Severity: 159.737** (Blast Radius: 1.667 * Doc Risk: 95.8231%)
- `js/global.js` -> **Severity: 137.498** (Blast Radius: 1.375 * Doc Risk: 99.9984%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
