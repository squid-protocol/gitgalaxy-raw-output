# ARCHITECTURAL_BRIEF: sqlmap
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/sqlmapproject/sqlmap.git` |
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
- **Scope:** 510 analyzed artifact(s), 39982 LOC.
- **Load-bearing artifact:** `lib/core/enums.py` -- 200 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `lib/core/common.py` -- pulls in 70 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/core/common.py` at magnitude 6649.34 (structural weight, not risk).
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
| Total Artifacts | 653 |
| Analyzed Artifacts (Scanned) | 510 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 143 |
| Total LOC | 39982 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 78.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2836 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2843 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.665 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 8 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 412 | 38946 | 80.8% |
| MARKDOWN | 34 | 0 | 6.7% |
| PLAINTEXT | 15 | 0 | 2.9% |
| XML | 15 | 0 | 2.9% |
| SHELL | 12 | 244 | 2.4% |
| SQLITE | 10 | 30 | 2.0% |
| YAML | 3 | 330 | 0.6% |
| CPP | 3 | 27 | 0.6% |
| DB2_SQL | 2 | 7 | 0.4% |
| C | 2 | 353 | 0.4% |
| POSTGRESQL | 1 | 14 | 0.2% |
| PERL | 1 | 31 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 510 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Parameter Forwarders Files 27%, Data / Markup / Trivial 27%, Compute Cores Files 22%, Large Core Modules (2) 8%, Large Core Modules (3) 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 461 | 90.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 49 | 9.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 143*

**Composition by Extension & Reason:**
- `.py`: 75x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 29 exceeds 500 chars)
- `.so_`: 27x Excluded (Unsupported Extension: '.so_')
- `.dll_`: 6x Excluded (Unsupported Extension: '.dll_')
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 1x Excluded (Massive Static Asset Blob: 4246 LOC), 1x Excluded (Static Asset Blob without Intent: 1613 LOC), 1x Excluded (Static Asset Blob without Intent: 1576 LOC)
- `.txt`: 1x Excluded (Lexical Monotony: High structural repetition detected in 2855 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 3423 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 10181 LOC)
- `.exe_`: 3x Excluded (Unsupported Extension: '.exe_')
- `.asp_`: 2x Excluded (Unsupported Extension: '.asp_')
- `.aspx_`: 2x Excluded (Unsupported Extension: '.aspx_')
- `.cfm_`: 2x Excluded (Unsupported Extension: '.cfm_')
- `.jsp_`: 2x Excluded (Unsupported Extension: '.jsp_')
- `.php_`: 2x Excluded (Unsupported Extension: '.php_')
- `.tx_`: 1x Excluded (Unsupported Extension: '.tx_')
- `.wav`: 1x Excluded (Explicitly Denied Extension: '.wav')
- `.sln`: 1x Unsupported Format (.sln)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.2 | 25.6 | 7.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 93.0 | 54.3 | 54.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 95.9 | 14.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 14.7 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 24.5 | 20.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 65.0 | 91.7 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.3 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.4 | 0.7 | 0.8 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.6 | 5.2 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 62.2 | 73.4 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 494 | 80 | 2 | `lib/core/common.py` |
| cleanup | 100 | 47 | 0 | `lib/core/testing.py` |
| guards | 1904 | 126 | 10 | `lib/core/common.py` |
| danger | 1843 | 263 | 8 | `lib/core/option.py` |
| concurrency | 103 | 27 | 0 | `lib/core/common.py` |
| connectivity | 1970 | 385 | 6 | `lib/core/common.py` |
| io | 877 | 104 | 3 | `lib/core/common.py` |
| crypto | 11 | 6 | 0 | `lib/utils/hash.py` |
| ipc | 54 | 18 | 0 | `lib/core/update.py` |
| time | 69 | 26 | 0 | `lib/request/connect.py` |
| serialization | 5 | 2 | 0 | `lib/core/bigarray.py` |
| regex | 677 | 103 | 2 | `lib/core/common.py` |
| events | 1327 | 156 | 8 | `lib/controller/checks.py` |
| tests | 6 | 4 | 0 | `sqlmap.py` |
| docs | 1094 | 410 | 2 | `lib/core/common.py` |
| debt | 111 | 34 | 0 | `lib/utils/sgmllib.py` |
| mutation | 21604 | 386 | 85 | `lib/core/common.py` |
| dead_code | 173 | 104 | 2 | `extra/vulnserver/vulnserver.py` |
| credential | 17 | 7 | 0 | `lib/core/settings.py` |
| threat | 6 | 4 | 0 | `lib/core/settings.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lib/core/common.py` (Hits: 123)
- `lib/core/option.py` (Hits: 106)
- `extra/shutils/pypi.sh` (Hits: 59)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **enums.py** (`lib/core/enums.py`) — 200 inbound connections
2. **data.py** (`lib/core/data.py`) — 174 inbound connections
3. **common.py** (`lib/core/common.py`) — 162 inbound connections
4. **exception.py** (`lib/core/exception.py`) — 137 inbound connections
5. **settings.py** (`lib/core/settings.py`) — 135 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **common.py** (`lib/core/common.py`) — 70 outbound dependencies
2. **option.py** (`lib/core/option.py`) — 60 outbound dependencies
3. **handler.py** (`lib/controller/handler.py`) — 37 outbound dependencies
4. **connect.py** (`lib/request/connect.py`) — 35 outbound dependencies
5. **patch.py** (`lib/core/patch.py`) — 34 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `queryPage` **(Many-Argument Workhorses)** (@ `lib/request/connect.py`) -> Impact: **1634.6** | LOC: 624
  * *Intent:* """ This method calls a function to get the target URL page content and returns its page ratio (0 <= ratio <= 1) or a boolean value representing False...
- `bisection` **(Many-Argument Workhorses)** (@ `lib/techniques/blind/inference.py`) -> Impact: **856.6** | LOC: 670
  * *Intent:* """ Bisection algorithm that can be used to perform blind SQL injection on an affected host """
- `checkSqlInjection` **(Many-Argument Workhorses)** (@ `lib/controller/checks.py`) -> Impact: **755.6** | LOC: 753
  * *Intent:* # Store here the details about boundaries and payload used to # successfully inject injection = InjectionDict() # Localized thread data needed for som...
- `getColumns` **(Many-Argument Workhorses)** (@ `plugins/generic/databases.py`) -> Impact: **563.1** | LOC: 484
- `getPage` **(Many-Argument Workhorses)** (@ `lib/request/connect.py`) -> Impact: **521.4** | LOC: 755
  * *Intent:* """ This method connects to the target URL or proxy and returns the target URL page content """
- `getValue` **(Many-Argument Workhorses)** (@ `lib/request/inject.py`) -> Impact: **454.6** | LOC: 183
  * *Intent:* """ Called each time sqlmap inject a SQL query on the SQL injection affected parameter. """
- `cmdLineParser` **(Many-Argument Workhorses)** (@ `lib/parse/cmdline.py`) -> Impact: **322.7** | LOC: 1051
  * *Intent:* """ This function parses the command line parameters and arguments """
- `dumpTable` **(Many-Argument Workhorses)** (@ `plugins/generic/entries.py`) -> Impact: **313.6** | LOC: 418
- `payload` **(Many-Argument Workhorses)** (@ `lib/core/agent.py`) -> Impact: **294.5** | LOC: 175
  * *Intent:* """ This method replaces the affected parameter with the SQL injection statement to request """
- `start` **(I/O & Config Routines)** (@ `lib/controller/controller.py`) -> Impact: **292.4** | LOC: 527
  * *Intent:* """ This function calls a function that performs checks on both URL stability and all GET, POST, Cookie and User-Agent parameters to check if they are...

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib/core` | 32 | 18501.46 | 46.24% | 0.52% |
| `lib/request` | 15 | 6878.72 | 46.84% | 7.62% |
| `lib/utils` | 21 | 6806.06 | 62.87% | 4.57% |
| `plugins/generic` | 13 | 6415.4 | 61.4% | 0.66% |
| `lib/controller` | 5 | 3330.98 | 50.55% | 0.0% |
| `lib/takeover` | 8 | 2422.28 | 61.04% | 1.24% |
| `tamper` | 70 | 2080.24 | 21.8% | 62.99% |
| `lib/techniques/blind` | 2 | 1808.7 | 40.09% | 0.0% |
| `lib/techniques/union` | 3 | 1608.02 | 51.4% | 0.0% |
| `lib/parse` | 9 | 1368.08 | 44.18% | 1.4% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lib/utils/sgmllib.py` -> **95.9181%** Exposure
- `plugins/dbms/sqlite/connector.py` -> **93.5379%** Exposure
- `plugins/dbms/access/connector.py` -> **81.7574%** Exposure
- `plugins/dbms/cratedb/connector.py` -> **81.7574%** Exposure
- `plugins/dbms/cubrid/connector.py` -> **81.7574%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `extra/cloak/cloak.py` -> **100.0%** Exposure
- `extra/dbgtool/dbgtool.py` -> **100.0%** Exposure
- `extra/icmpsh/icmpsh_m.py` -> **100.0%** Exposure
- `extra/vulnserver/vulnserver.py` -> **100.0%** Exposure
- `lib/controller/checks.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `extra/vulnserver/vulnserver.py` -> **5** Orphaned Functions | **0** Duplicates
- `lib/utils/sgmllib.py` -> **5** Orphaned Functions | **0** Duplicates
- `plugins/dbms/sqlite/connector.py` -> **3** Orphaned Functions | **0** Duplicates
- `plugins/dbms/access/connector.py` -> **2** Orphaned Functions | **0** Duplicates
- `plugins/dbms/cache/connector.py` -> **2** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `lib/core/settings.py` -> **99.9998%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### 📡 API Network Audit (Set Theory)
- **Shadow APIs (Critical):** `0` undocumented endpoints actively listening.
- **Ghost APIs (Bloat):** `12` endpoints documented but missing from code.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2521` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/core/common.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.734)
- **Top Global Matches:** file_cluster_4: 8.734, file_cluster_6: 9.885, file_cluster_12: 13.858
- **Magnitude:** 6649.34 | **LOC:** 5657 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 90.0%
- **Blast Radius:** changing it is visible to **162** in-repo importer(s); it depends on **70**; blast radius 38.661; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 18.8053% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseRequestFile` **(Many-Argument Workhorses)** (Impact: 171.4)
    * *Intent:* """ Parses WebScarab and Burp logs and adds results to the target URL list >>> handle, reqFile = tem...
  * `paramToDict` **(Many-Argument Workhorses)** (Impact: 154.1)
    * *Intent:* """ Split the parameters into names and values, check if these parameters are within the testable pa...
  * `_parseBurpLog` **(Compute Cores)** (Impact: 123.4)
    * *Intent:* """ Parses Burp logs """
  * `findPageForms` **(Many-Argument Workhorses)** (Impact: 122.9)
    * *Intent:* """ Parses given page content for possible forms (Note: still not implemented for Python3) >>> findP...
  * `readInput` **(Many-Argument Workhorses)** (Impact: 96.2)
    * *Intent:* """ Reads input from terminal """
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 984 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 3053
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1528`, `structural_boundaries: 988`, `args: 228`, `func_start: 221`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 97`, `high_risk_execution: 3`, `state_mutation: 1085`, `fragile_debt: 3`
* *Architecture:* `io: 123`, `api: 212`, `concurrency: 2`, `import: 208`
* *Defense:* `safety: 190`, `doc: 175`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.661
  * `Choke Point (Betweenness):` 0.014044 | `Ripple Effect (Closeness):` 0.401154
  * `Imports (Out-Degree: 18):` __future__, _mssql, binascii, codecs, contextlib, copy, ctypes, curses...
  * `Imported By (In-Degree: 162):` (Excluded from Brief to save tokens)

### `lib/request/connect.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.806)
- **Top Global Matches:** file_cluster_3: 7.806, file_cluster_8: 20.907, file_cluster_6: 33.599
- **Magnitude:** 3703.52 | **LOC:** 1659 | **CtrlFlow:** 59.6% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **35**; blast radius 2.661; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.5%), Guard Balance (formerly Safety Score) (87.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 45.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `queryPage` **(Many-Argument Workhorses)** (Impact: 1634.6)
    * *Intent:* """ This method calls a function to get the target URL page content and returns its page ratio (0 <=...
  * `getPage` **(Many-Argument Workhorses)** (Impact: 521.4)
    * *Intent:* """ This method connects to the target URL or proxy and returns the target URL page content """
  * `_retryProxy` **(Compute Cores)** (Impact: 36.8)
  * `_connReadProxy` **(Stateful Encapsulated Methods)** (Impact: 29.0)
  * `_randomizeParameter` **(Stateful Encapsulated Methods)** (Impact: 28.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 454 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1380
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 796`, `structural_boundaries: 364`, `args: 12`, `func_start: 10`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 1`, `state_mutation: 472`, `dead_code: 1`
* *Architecture:* `io: 24`, `api: 5`, `import: 136`
* *Defense:* `safety: 57`, `doc: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.661
  * `Choke Point (Betweenness):` 0.003537 | `Ripple Effect (Closeness):` 0.074293
  * `Imports (Out-Degree: 16):` binascii, httpx, inspect, lib.core.agent, lib.core.common, lib.core.compat, lib.core.convert, lib.core.data...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `lib/core/option.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.406)
- **Top Global Matches:** file_cluster_6: 9.406, file_cluster_4: 14.449, file_cluster_8: 14.985
- **Magnitude:** 3273.5 | **LOC:** 3000 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 87.5%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **60**; blast radius 1.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.4%)
- **Documentation Coverage:** 46.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_basicOptionValidation` **(Compute Cores)** (Impact: 192.2)
  * `_cleanupOptions` **(I/O & Config Routines)** (Impact: 120.2)
    * *Intent:* """ Cleanup configuration attributes. """
  * `_setMetasploit` **(I/O & Config Routines)** (Impact: 58.9)
  * `_setHTTPHandlers` **(I/O & Config Routines)** (Impact: 47.0)
    * *Intent:* """ Check and set the HTTP/SOCKS proxy for all HTTP requests. """
  * `_mergeOptions` **(Many-Argument Workhorses)** (Impact: 44.2)
    * *Intent:* """ Merge command line options with configuration file and default options. @param inputOptions: opt...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 607 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 2061
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 845`, `structural_boundaries: 553`, `args: 79`, `func_start: 74`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 91`, `state_mutation: 847`
* *Architecture:* `io: 106`, `api: 14`, `concurrency: 3`, `import: 161`
* *Defense:* `safety: 104`, `doc: 40`, `sync_locks: 1`, `immutability_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.14
  * `Choke Point (Betweenness):` 0.000868 | `Ripple Effect (Closeness):` 0.010478
  * `Imports (Out-Degree: 32):` __future__, codecs, collections, functools, glob, inspect, json, lib.controller.checks...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/core/agent.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.274)
- **Top Global Matches:** file_cluster_3: 8.274, file_cluster_8: 16.755, file_cluster_6: 29.573
- **Magnitude:** 2283.32 | **LOC:** 1285 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **24** in-repo importer(s); it depends on **11**; blast radius 4.531; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.7%)
- **Documentation Coverage:** 29.4118% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `payload` **(Many-Argument Workhorses)** (Impact: 294.5)
    * *Intent:* """ This method replaces the affected parameter with the SQL injection statement to request """
  * `limitQuery` **(Many-Argument Workhorses)** (Impact: 172.1)
    * *Intent:* """ Take in input a query string and return its limited query string. Example: Input: SELECT user FR...
  * `forgeUnionQuery` **(Many-Argument Workhorses)** (Impact: 124.6)
    * *Intent:* """ Take in input an query (pseudo query) string and return its processed UNION ALL SELECT query. Ex...
  * `concatQuery` **(Many-Argument Workhorses)** (Impact: 87.4)
    * *Intent:* """ Take in input a query string and return its processed nulled, casted and concatenated query stri...
  * `prefixQuery` **(Many-Argument Workhorses)** (Impact: 70.9)
    * *Intent:* """ This method defines how the input expression has to be escaped to perform the injection dependin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 329 instances
* *State Mutation (weighted view):* 1016
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 469`, `structural_boundaries: 177`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 358`, `planned_debt: 1`
* *Architecture:* `api: 26`, `import: 53`
* *Defense:* `safety: 9`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.531
  * `Choke Point (Betweenness):` 0.00035 | `Ripple Effect (Closeness):` 0.117826
  * `Imports (Out-Degree: 9):` lib.core.common, lib.core.compat, lib.core.convert, lib.core.data, lib.core.dicts, lib.core.enums, lib.core.exception, lib.core.settings...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `lib/controller/checks.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.496)
- **Top Global Matches:** file_cluster_8: 12.496, file_cluster_3: 12.722, file_cluster_6: 24.869
- **Magnitude:** 2234.44 | **LOC:** 1600 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **28**; blast radius 1.059; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.2%), Guard Balance (formerly Safety Score) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkSqlInjection` **(Many-Argument Workhorses)** (Impact: 755.6)
    * *Intent:* # Store here the details about boundaries and payload used to # successfully inject injection = Inje...
  * `heuristicCheckSqlInjection` **(Many-Argument Workhorses)** (Impact: 106.9)
  * `checkConnection` **(Compute Cores)** (Impact: 86.6)
  * `checkFalsePositives` **(Compute Cores)** (Impact: 38.6)
    * *Intent:* """ Checks for false positives (only in single special cases) """
  * `checkStability` **(I/O & Config Routines)** (Impact: 27.6)
    * *Intent:* """ This function checks if the URL content is stable requesting the same page two times with a smal...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 331 instances
* *State Mutation (weighted view):* 1046
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 589`, `structural_boundaries: 313`, `args: 19`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 384`
* *Architecture:* `io: 5`, `api: 15`, `import: 98`
* *Defense:* `safety: 32`, `doc: 9`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.059
  * `Choke Point (Betweenness):` 0.000433 | `Ripple Effect (Closeness):` 0.009946
  * `Imports (Out-Degree: 20):` copy, extra.beep.beep, lib.core.agent, lib.core.common, lib.core.compat, lib.core.convert, lib.core.data, lib.core.datatype...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `plugins/generic/databases.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.858)
- **Top Global Matches:** file_cluster_3: 10.858, file_cluster_8: 16.157, file_cluster_6: 28.516
- **Magnitude:** 1957.12 | **LOC:** 1125 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 1.76; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (89.3%), Complexity Load (formerly Cognitive Load) (87.2%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getColumns` **(Many-Argument Workhorses)** (Impact: 563.1)
  * `getTables` **(Many-Argument Workhorses)** (Impact: 234.7)
  * `getDbs` **(Compute Cores)** (Impact: 79.2)
  * `getStatements` **(Compute Cores)** (Impact: 47.7)
  * `getCount` **(Compute Cores)** (Impact: 21.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 303 instances
* *State Mutation (weighted view):* 933
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 465`, `structural_boundaries: 157`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 327`
* *Architecture:* `api: 9`, `import: 50`
* *Defense:* `safety: 13`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.76
  * `Choke Point (Betweenness):` 0.000243 | `Ripple Effect (Closeness):` 0.047282
  * `Imports (Out-Degree: 10):` lib.core.agent, lib.core.common, lib.core.data, lib.core.decorators, lib.core.dicts, lib.core.enums, lib.core.exception, lib.core.settings...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/techniques/blind/inference.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.255)
- **Top Global Matches:** file_cluster_3: 6.255, file_cluster_8: 20.696, file_cluster_6: 33.622
- **Magnitude:** 1797.66 | **LOC:** 758 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.931; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.9%), Complexity Load (formerly Cognitive Load) (80.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bisection` **(Many-Argument Workhorses)** (Impact: 856.6)
    * *Intent:* """ Bisection algorithm that can be used to perform blind SQL injection on an affected host """
  * `getChar` **(Many-Argument Workhorses)** (Impact: 255.5)
    * *Intent:* """ continuousOrder means that distance between each two neighbour's numerical values is exactly 1 "...
  * `blindThread` **(I/O & Config Routines)** (Impact: 32.1)
  * `tryHint` **(Compute Cores)** (Impact: 14.0)
  * `validateChar` **(Compute Cores)** (Impact: 13.6)
    * *Intent:* """ Used in inference - in time-based SQLi if original and retrieved value are not equal there will ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 192 instances
* *State Mutation (weighted view):* 599
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 294`, `structural_boundaries: 155`, `args: 7`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 215`
* *Architecture:* `api: 6`, `import: 56`
* *Defense:* `safety: 31`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.931
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.006425
  * `Imports (Out-Degree: 12):` __future__, lib.core.agent, lib.core.common, lib.core.data, lib.core.enums, lib.core.exception, lib.core.settings, lib.core.threads...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/utils/hash.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.253)
- **Top Global Matches:** file_cluster_6: 8.253, file_cluster_4: 11.82, file_cluster_8: 16.57
- **Magnitude:** 1600.0 | **LOC:** 1331 | **CtrlFlow:** 39.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **29**; blast radius 1.193; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (86.6%), Guard Balance (formerly Safety Score) (86.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 25.6757% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dictionaryAttack` **(Many-Argument Workhorses)** (Impact: 160.7)
  * `_bruteProcessVariantB` **(Many-Argument Workhorses)** (Impact: 86.8)
  * `_bruteProcessVariantA` **(Many-Argument Workhorses)** (Impact: 86.1)
  * `attackDumpedTable` **(Compute Cores)** (Impact: 58.2)
  * `phpass_passwd` **(Many-Argument Workhorses)** (Impact: 37.6)
    * *Intent:* """ Reference(s): https://web.archive.org/web/20120219120128/packetstormsecurity.org/files/74448/php...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 242 instances
* *Concurrency (weighted view):* 42
* *State Mutation (weighted view):* 759
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 337`, `structural_boundaries: 256`, `args: 37`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 275`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 33`, `concurrency: 7`, `import: 74`
* *Defense:* `safety: 37`, `doc: 28`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.193
  * `Choke Point (Betweenness):` 0.000271 | `Ripple Effect (Closeness):` 0.039327
  * `Imports (Out-Degree: 10):` Crypto.Cipher.DES, __future__, base64, binascii, crypt, gc, hashlib, lib.core.common...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/request/inject.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.028)
- **Top Global Matches:** file_cluster_8: 6.028, file_cluster_6: 14.285, file_cluster_3: 23.06
- **Magnitude:** 1197.34 | **LOC:** 567 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **22**; blast radius 0.932; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.9%)
- **Documentation Coverage:** 61.5385% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getValue` **(Many-Argument Workhorses)** (Impact: 454.6)
    * *Intent:* """ Called each time sqlmap inject a SQL query on the SQL injection affected parameter. """
  * `_goInferenceProxy` **(Many-Argument Workhorses)** (Impact: 160.4)
    * *Intent:* """ Retrieve the output of a SQL query characted by character taking advantage of an blind SQL injec...
  * `_goInference` **(Many-Argument Workhorses)** (Impact: 87.4)
  * `_goInferenceFields` **(Many-Argument Workhorses)** (Impact: 23.5)
  * `goStacked` **(Compute Cores)** (Impact: 14.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 130 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 398
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 157`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 138`
* *Architecture:* `api: 3`, `concurrency: 1`, `import: 60`
* *Defense:* `safety: 20`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.932
  * `Choke Point (Betweenness):` 0.000202 | `Ripple Effect (Closeness):` 0.007556
  * `Imports (Out-Degree: 18):` __future__, lib.core.agent, lib.core.bigarray, lib.core.common, lib.core.compat, lib.core.data, lib.core.decorators, lib.core.dicts...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/generic/users.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.68)
- **Top Global Matches:** file_cluster_3: 11.68, file_cluster_8: 14.153, file_cluster_6: 26.531
- **Magnitude:** 981.78 | **LOC:** 676 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 1.76; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.1%), Complexity Load (formerly Cognitive Load) (84.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getPrivileges` **(Many-Argument Workhorses)** (Impact: 245.0)
  * `getPasswordHashes` **(Compute Cores)** (Impact: 131.9)
  * `getUsers` **(Compute Cores)** (Impact: 50.1)
  * `isDba` **(Compute Cores)** (Impact: 21.9)
  * `getCurrentUser` **(Parameter Forwarders)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 166 instances
* *State Mutation (weighted view):* 508
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 114`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 176`
* *Architecture:* `io: 3`, `api: 8`, `import: 43`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.76
  * `Choke Point (Betweenness):` 0.000559 | `Ripple Effect (Closeness):` 0.047282
  * `Imports (Out-Degree: 13):` lib.core.agent, lib.core.common, lib.core.compat, lib.core.convert, lib.core.data, lib.core.dicts, lib.core.enums, lib.core.exception...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/generic/search.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 12.274)
- **Top Global Matches:** file_cluster_3: 12.274, file_cluster_8: 31.175, file_cluster_1: 40.935
- **Magnitude:** 959.56 | **LOC:** 641 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 1.76; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.0%), Complexity Load (formerly Cognitive Load) (84.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `searchColumn` **(Compute Cores)** (Impact: 158.0)
  * `searchTable` **(Compute Cores)** (Impact: 126.2)
  * `searchDb` **(Compute Cores)** (Impact: 52.6)
  * `search` **(Compute Cores)** (Impact: 13.5)
  * `__init__` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 189 instances
* *State Mutation (weighted view):* 592
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 89`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 214`
* *Architecture:* `api: 6`, `import: 33`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.76
  * `Choke Point (Betweenness):` 0.000178 | `Ripple Effect (Closeness):` 0.047282
  * `Imports (Out-Degree: 8):` lib.core.agent, lib.core.common, lib.core.data, lib.core.enums, lib.core.exception, lib.core.settings, lib.request, lib.utils.brute...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/generic/entries.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.746)
- **Top Global Matches:** file_cluster_3: 11.746, file_cluster_8: 30.964, file_cluster_1: 40.791
- **Magnitude:** 936.82 | **LOC:** 647 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 1.76; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.6%), Complexity Load (formerly Cognitive Load) (81.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dumpTable` **(Many-Argument Workhorses)** (Impact: 313.6)
  * `dumpFoundColumn` **(Many-Argument Workhorses)** (Impact: 59.2)
  * `dumpFoundTables` **(Compute Cores)** (Impact: 35.8)
  * `dumpAll` **(Defensive Guards)** (Impact: 17.6)
  * `__init__` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 155 instances
* *State Mutation (weighted view):* 493
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 125`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 183`
* *Architecture:* `api: 6`, `import: 45`
* *Defense:* `safety: 21`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.76
  * `Choke Point (Betweenness):` 0.000528 | `Ripple Effect (Closeness):` 0.047282
  * `Imports (Out-Degree: 12):` lib.core.agent, lib.core.bigarray, lib.core.common, lib.core.convert, lib.core.data, lib.core.dicts, lib.core.enums, lib.core.exception...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/core/dump.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.587)
- **Top Global Matches:** file_cluster_6: 7.587, file_cluster_8: 12.038, file_cluster_4: 14.412
- **Magnitude:** 928.58 | **LOC:** 730 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 0.949; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dbTableValues` **(Many-Argument Workhorses)** (Impact: 165.0)
  * `dbTableColumns` **(Many-Argument Workhorses)** (Impact: 59.6)
  * `userSettings` **(Stateful Encapsulated Methods)** (Impact: 41.0)
  * `dbTables` **(Compute Cores)** (Impact: 36.7)
  * `dbTablesCount` **(Many-Argument Workhorses)** (Impact: 33.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 124 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 391
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 148`, `args: 29`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 143`
* *Architecture:* `io: 15`, `api: 24`, `concurrency: 2`, `import: 53`
* *Defense:* `safety: 33`, `doc: 2`, `sync_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.949
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.003143
  * `Imports (Out-Degree: 10):` hashlib, lib.core.common, lib.core.compat, lib.core.convert, lib.core.data, lib.core.dicts, lib.core.enums, lib.core.exception...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/core/target.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.163)
- **Top Global Matches:** file_cluster_8: 9.163, file_cluster_6: 12.565, file_cluster_4: 20.529
- **Magnitude:** 923.28 | **LOC:** 782 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **23**; blast radius 0.953; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.4%)
- **Documentation Coverage:** 20.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_setRequestParams` **(I/O & Config Routines)** (Impact: 195.5)
    * *Intent:* """ Check and set the parameters and perform checks on 'data' option for HTTP method POST. """
  * `process` **(Defensive Guards)** (Impact: 37.3)
  * `_resumeHashDBValues` **(Stateful Encapsulated Methods)** (Impact: 22.6)
    * *Intent:* """ Resume stored data values from HashDB """
  * `initTargetEnv` **(I/O & Config Routines)** (Impact: 18.6)
    * *Intent:* """ Initialize target environment. """
  * `_resumeDBMS` **(I/O & Config Routines)** (Impact: 14.4)
    * *Intent:* """ Resume stored DBMS information from HashDB """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 180 instances
* *State Mutation (weighted view):* 561
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 199`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 201`
* *Architecture:* `io: 21`, `api: 3`, `import: 75`
* *Defense:* `safety: 19`, `doc: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.953
  * `Choke Point (Betweenness):` 0.000119 | `Ripple Effect (Closeness):` 0.002947
  * `Imports (Out-Degree: 13):` functools, lib.core.common, lib.core.compat, lib.core.convert, lib.core.data, lib.core.datatype, lib.core.dicts, lib.core.dump...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/controller/controller.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.58)
- **Top Global Matches:** file_cluster_8: 9.58, file_cluster_6: 15.21, file_cluster_4: 23.379
- **Magnitude:** 911.36 | **LOC:** 795 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **17**; blast radius 0.937; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.0%), Guard Balance (formerly Safety Score) (83.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 55.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `start` **(I/O & Config Routines)** (Impact: 292.4)
    * *Intent:* """ This function calls a function that performs checks on both URL stability and all GET, POST, Coo...
  * `_selectInjection` **(I/O & Config Routines)** (Impact: 23.1)
    * *Intent:* """ Selection function for injection place, parameters and type. """
  * `_randomFillBlankFields` **(Stateful Encapsulated Methods)** (Impact: 19.2)
  * `_formatInjection` **(Stateful Encapsulated Methods)** (Impact: 16.8)
  * `_saveToHashDB` **(Stateful Encapsulated Methods)** (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 169 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 510
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 336`, `structural_boundaries: 190`, `args: 8`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 2`, `state_mutation: 172`
* *Architecture:* `io: 3`, `api: 1`, `import: 71`
* *Defense:* `safety: 19`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.937
  * `Choke Point (Betweenness):` 0.001662 | `Ripple Effect (Closeness):` 0.00262
  * `Imports (Out-Degree: 12):` __future__, lib.controller.action, lib.controller.checks, lib.core.agent, lib.core.common, lib.core.compat, lib.core.data, lib.core.decorators...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/utils/api.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.111)
- **Top Global Matches:** file_cluster_12: 7.111, file_cluster_15: 9.166, file_cluster_4: 9.476
- **Magnitude:** 864.72 | **LOC:** 919 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **32**; blast radius 1.044; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.9%), Connectivity (formerly Api Exposure) (67.9%)
- **Documentation Coverage:** 60.1942% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `client` **(Many-Argument Workhorses)** (Impact: 117.5)
    * *Intent:* """ REST-JSON API client """
  * `server` **(Many-Argument Workhorses)** (Impact: 39.8)
    * *Intent:* """ REST-JSON API server """
  * `write` **(Many-Argument Workhorses)** (Impact: 35.0)
  * `scan_log_limited` **(Type Conversions)** (Impact: 17.2)
    * *Intent:* # Functions to handle scans' logs """ Retrieve a subset of log messages """
  * `execute` **(Defensive Guards)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 98 instances
* *Api Near Db Sink:* 4 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 332
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 262`, `args: 54`, `func_start: 53`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 136`
* *Architecture:* `io: 30`, `api: 54`, `concurrency: 2`, `import: 62`
* *Defense:* `safety: 19`, `doc: 21`, `sync_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.044
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.003929
  * `Imports (Out-Degree: 15):` __future__, contextlib, eventlet, gevent, lib.core.common, lib.core.compat, lib.core.convert, lib.core.data...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/techniques/union/use.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.531)
- **Top Global Matches:** file_cluster_3: 11.531, file_cluster_8: 14.215, file_cluster_6: 26.641
- **Magnitude:** 824.26 | **LOC:** 468 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **20**; blast radius 1.159; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.2%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unionUse` **(Many-Argument Workhorses)** (Impact: 241.4)
    * *Intent:* """ This function tests for an UNION SQL injection on the target URL then call its subsidiary functi...
  * `_oneShotUnionUse` **(Many-Argument Workhorses)** (Impact: 123.0)
  * `unionThread` **(Compute Cores)** (Impact: 52.7)
  * `configUnion` **(Stateful Encapsulated Methods)** (Impact: 22.4)
  * `_configUnionCols` **(Stateful Encapsulated Methods)** (Impact: 10.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 109 instances
* *State Mutation (weighted view):* 349
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 138`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 131`
* *Architecture:* `api: 3`, `import: 56`
* *Defense:* `safety: 18`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.159
  * `Choke Point (Betweenness):` 0.000299 | `Ripple Effect (Closeness):` 0.044456
  * `Imports (Out-Degree: 15):` json, lib.core.agent, lib.core.bigarray, lib.core.common, lib.core.compat, lib.core.convert, lib.core.data, lib.core.dicts...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/techniques/union/test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.887)
- **Top Global Matches:** file_cluster_3: 11.887, file_cluster_8: 32.726, file_cluster_1: 37.828
- **Magnitude:** 772.72 | **LOC:** 403 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 0.932; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.0%)
- **Documentation Coverage:** 55.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_findUnionCharCount` **(Many-Argument Workhorses)** (Impact: 198.7)
    * *Intent:* """ Finds number of columns affected by UNION based injection """
  * `_unionPosition` **(Many-Argument Workhorses)** (Impact: 97.3)
  * `_unionTestByCharBruteforce` **(Many-Argument Workhorses)** (Impact: 85.0)
    * *Intent:* """ This method tests if the target URL is affected by an union SQL injection vulnerability. The tes...
  * `_orderByTechnique` **(Stateful Encapsulated Methods)** (Impact: 53.8)
  * `_fuzzUnionCols` **(Stateful Encapsulated Methods)** (Impact: 43.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 119`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 96`
* *Architecture:* `api: 1`, `import: 45`
* *Defense:* `safety: 8`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.932
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007556
  * `Imports (Out-Degree: 11):` itertools, lib.core.agent, lib.core.common, lib.core.compat, lib.core.data, lib.core.decorators, lib.core.dicts, lib.core.enums...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/techniques/error/use.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.539)
- **Top Global Matches:** file_cluster_3: 7.539, file_cluster_8: 20.899, file_cluster_6: 33.648
- **Magnitude:** 744.92 | **LOC:** 471 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 0.931; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_oneShotErrorUse` **(Many-Argument Workhorses)** (Impact: 200.1)
  * `errorUse` **(Many-Argument Workhorses)** (Impact: 122.9)
    * *Intent:* """ Retrieve the output of a SQL query taking advantage of the error-based SQL injection vulnerabili...
  * `_errorFields` **(Many-Argument Workhorses)** (Impact: 71.0)
  * `errorThread` **(Defensive Guards)** (Impact: 14.6)
  * `_formatPartialContent` **(Stateful Encapsulated Methods)** (Impact: 4.9)
    * *Intent:* """ Prepares (possibly hex-encoded) partial content for safe console output """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 319
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 135`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 123`
* *Architecture:* `api: 2`, `import: 54`
* *Defense:* `safety: 16`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.931
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.006425
  * `Imports (Out-Degree: 15):` __future__, lib.core.agent, lib.core.bigarray, lib.core.common, lib.core.compat, lib.core.convert, lib.core.data, lib.core.dicts...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/utils/sgmllib.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.77)
- **Top Global Matches:** file_cluster_12: 7.77, file_cluster_4: 8.501, file_cluster_7: 10.14
- **Magnitude:** 715.32 | **LOC:** 575 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.887; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (95.9%), Guard Balance (formerly Safety Score) (82.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 78.1609% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `goahead` **(Compute Cores)** (Impact: 93.8)
    * *Intent:* # Internal -- handle data as far as reasonable. May leave state # and data to be processed by a subs...
  * `parse_starttag` **(Stateful Encapsulated Methods)** (Impact: 60.2)
    * *Intent:* # Internal -- handle starttag, return length or -1 if not terminated
  * `_convert_ref` **(Stateful Encapsulated Methods)** (Impact: 24.7)
    * *Intent:* # Internal -- convert entity or character reference
  * `finish_endtag` **(Defensive Guards)** (Impact: 20.6)
    * *Intent:* # Internal -- finish processing of end tag
  * `test` **(Defensive Guards)** (Impact: 17.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 99 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 324
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 108`, `args: 43`, `func_start: 43`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 1`, `state_mutation: 126`, `fragile_debt: 7`, `unreferenced_by_name: 5`
* *Architecture:* `io: 4`, `api: 44`, `import: 5`
* *Defense:* `safety: 13`, `doc: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.887
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, _markupbase, markupbase, re, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/takeover/metasploit.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.236)
- **Top Global Matches:** file_cluster_4: 6.236, file_cluster_6: 10.65, file_cluster_16: 11.214
- **Magnitude:** 685.64 | **LOC:** 706 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 2.29; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.7%), Complexity Load (formerly Cognitive Load) (73.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_controlMsfCmd` **(Many-Argument Workhorses)** (Impact: 62.6)
  * `_selectPayload` **(Compute Cores)** (Impact: 43.5)
  * `_forgeMsfPayloadCmd` **(Stateful Encapsulated Methods)** (Impact: 38.5)
  * `_skeletonSelection` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `_initVars` **(Stateful Encapsulated Methods)** (Impact: 24.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 314
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 160`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 3`, `state_mutation: 126`
* *Architecture:* `io: 17`, `api: 6`, `import: 43`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 0.000392 | `Ripple Effect (Closeness):` 0.047282
  * `Imports (Out-Degree: 8):` __future__, errno, extra.cloak.cloak, lib.core.common, lib.core.convert, lib.core.data, lib.core.enums, lib.core.exception...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/request/basic.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.031)
- **Top Global Matches:** file_cluster_8: 12.031, file_cluster_3: 14.602, file_cluster_6: 23.832
- **Magnitude:** 680.2 | **LOC:** 456 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **22**; blast radius 1.261; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.8%)
- **Documentation Coverage:** 44.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decodePage` **(Many-Argument Workhorses)** (Impact: 121.5)
    * *Intent:* """ Decode compressed/charset HTTP response >>> getText(decodePage(b"<html>foo&amp;bar</html>", None...
  * `processResponse` **(Many-Argument Workhorses)** (Impact: 108.8)
  * `forgeHeaders` **(Compute Cores)** (Impact: 71.4)
    * *Intent:* """ Prepare HTTP Cookie, HTTP User-Agent and HTTP Referer headers to use when performing the HTTP re...
  * `checkCharEncoding` **(Many-Argument Workhorses)** (Impact: 56.6)
    * *Intent:* """ Checks encoding name, repairs common misspellings and adjusts to proper namings used in codecs m...
  * `parseResponse` **(Compute Cores)** (Impact: 10.7)
    * *Intent:* """ @param page: the page to parse to feed the knowledge base htmlFp (back-end DBMS fingerprint base...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 92 instances
* *State Mutation (weighted view):* 278
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 141`, `args: 16`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 94`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 8`, `import: 54`
* *Defense:* `safety: 10`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.261
  * `Choke Point (Betweenness):` 0.001275 | `Ripple Effect (Closeness):` 0.05931
  * `Imports (Out-Degree: 10):` codecs, gzip, io, lib.core.common, lib.core.convert, lib.core.data, lib.core.decorators, lib.core.dicts...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/utils/tui.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.968)
- **Top Global Matches:** file_cluster_8: 11.968, file_cluster_3: 20.396, file_cluster_6: 20.986
- **Magnitude:** 657.52 | **LOC:** 769 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.952; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (56.8%)
- **Documentation Coverage:** 19.0476% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_draw_current_tab` **(Compute Cores)** (Impact: 41.7)
    * *Intent:* """Draw the current tab content"""
  * `_show_console` **(Many-Argument Workhorses)** (Impact: 40.1)
    * *Intent:* """Show console output from sqlmap"""
  * `run` **(Compute Cores)** (Impact: 32.4)
    * *Intent:* """Main UI loop"""
  * `_import_config` **(Defensive Guards)** (Impact: 30.4)
    * *Intent:* """Import configuration from a file"""
  * `_export_config` **(Compute Cores)** (Impact: 27.8)
    * *Intent:* """Export current configuration to a file"""
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 106 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 344
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 101`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 47`, `high_risk_execution: 1`, `state_mutation: 132`
* *Architecture:* `io: 6`, `api: 5`, `import: 15`
* *Defense:* `safety: 37`, `doc: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.952
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003929
  * `Imports (Out-Degree: 6):` curses, fcntl, lib.core.common, lib.core.data, lib.core.defaults, lib.core.enums, lib.core.exception, lib.core.settings...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/dbms/mssqlserver/enumeration.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 24.364)
- **Top Global Matches:** file_cluster_3: 24.364, file_cluster_1: 26.029, file_cluster_8: 45.613
- **Magnitude:** 647.3 | **LOC:** 447 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.973; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.2%), Complexity Load (formerly Cognitive Load) (82.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `searchColumn` **(Compute Cores)** (Impact: 91.9)
  * `getTables` **(Compute Cores)** (Impact: 87.2)
  * `searchTable` **(Compute Cores)** (Impact: 44.8)
  * `getPrivileges` **(Many-Argument Workhorses)** (Impact: 17.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 126 instances
* *State Mutation (weighted view):* 394
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 79`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 142`
* *Architecture:* `api: 5`, `import: 27`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.973
  * `Choke Point (Betweenness):` 8.2e-05 | `Ripple Effect (Closeness):` 0.003368
  * `Imports (Out-Degree: 11):` lib.core.agent, lib.core.common, lib.core.compat, lib.core.data, lib.core.enums, lib.core.exception, lib.core.settings, lib.request...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/parse/cmdline.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.999)
- **Top Global Matches:** file_cluster_4: 7.999, file_cluster_6: 8.322, file_cluster_12: 14.431
- **Magnitude:** 641.82 | **LOC:** 1148 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **22**; blast radius 0.996; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.6%)
- **Documentation Coverage:** 86.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cmdLineParser` **(Many-Argument Workhorses)** (Impact: 322.7)
    * *Intent:* """ This function parses the command line parameters and arguments """
  * `get_all_options` **(Defensive Guards)** (Impact: 12.3)
  * `get_actions` **(Defensive Guards)** (Impact: 4.4)
  * `def` **(Parameter Forwarders)** (Impact: 3.7)
  * `_format_action_invocation` **(Encapsulated Accessors)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 169`, `args: 9`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 102`, `fragile_debt: 3`
* *Architecture:* `io: 14`, `api: 4`, `import: 43`
* *Defense:* `safety: 20`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.996
  * `Choke Point (Betweenness):` 0.000188 | `Ripple Effect (Closeness):` 0.00442
  * `Imports (Out-Degree: 13):` __future__, argparse, hashlib, lib.core.common, lib.core.compat, lib.core.convert, lib.core.data, lib.core.defaults...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `extra/shutils/pypi.sh` (SHELL) | Magnitude: 54.7 | Delta: **0.144** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: io: 59, indent_spaces: 52, structural_boundaries: 36, core_var_decl: 24
- `plugins/dbms/cubrid/connector.py` (PYTHON) | Magnitude: 20.64 | Delta: **0.156** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 26, safety: 8, import: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `plugins/dbms/mssqlserver/syntax.py` (PYTHON) | Magnitude: 16.48 | Delta: **0.132** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 5, branch: 3, api: 3
- `plugins/dbms/oracle/syntax.py` (PYTHON) | Magnitude: 16.48 | Delta: **0.132** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 5, branch: 3, api: 3
- `plugins/dbms/sybase/syntax.py` (PYTHON) | Magnitude: 16.48 | Delta: **0.132** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 5, branch: 3, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `plugins/dbms/access/syntax.py` (PYTHON) | Magnitude: 10.08 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 5, api: 3, args: 2
- `plugins/dbms/altibase/syntax.py` (PYTHON) | Magnitude: 10.08 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 5, api: 3, args: 2
- `plugins/dbms/cache/syntax.py` (PYTHON) | Magnitude: 10.08 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 5, api: 3, args: 2
- `plugins/dbms/clickhouse/syntax.py` (PYTHON) | Magnitude: 10.08 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 5, api: 3, args: 2
- `plugins/dbms/cubrid/syntax.py` (PYTHON) | Magnitude: 10.08 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 5, api: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `data/procs/oracle/read_file_export_extension.sql` (DB2_SQL) | Magnitude: 4.48 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 34, high_risk_execution: 8, args: 6, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `plugins/dbms/informix/syntax.py` (PYTHON) | Magnitude: 34.32 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 14, state_mutation: 6, core_var_decl: 6
- `plugins/dbms/sqlite/connector.py` (PYTHON) | Magnitude: 29.66 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 33, safety: 10, import: 10
- `lib/request/basicauthhandler.py` (PYTHON) | Magnitude: 26.08 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, branch: 4, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `lib/controller/checks.py` (PYTHON) | Magnitude: 2234.44 | Delta: **0.226** (centroid distance) | Secondary Pull: `file_cluster_3`
  * Top Architectural Signatures: indent_spaces: 1013, branch: 589, state_mutation: 384, structural_boundaries: 313

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/core/common.py` -> **Miroslav Stampar** (90.0% isolated ownership) | Magnitude: 6649.34
- `lib/core/option.py` -> **Miroslav Stampar** (87.5% isolated ownership) | Magnitude: 3273.5
- `lib/core/agent.py` -> **Miroslav Stampar** (100.0% isolated ownership) | Magnitude: 2283.32
- `lib/controller/checks.py` -> **Miroslav Stampar** (100.0% isolated ownership) | Magnitude: 2234.44
- `lib/techniques/blind/inference.py` -> **Miroslav Stampar** (100.0% isolated ownership) | Magnitude: 1797.66

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/core/common.py` -> **Severity: 1.404** (Bridge: 0.014 * Flux: 100.0%)
- `plugins/generic/takeover.py` -> **Severity: 0.595** (Bridge: 0.0059 * Flux: 100.0%)
- `plugins/generic/enumeration.py` -> **Severity: 0.493** (Bridge: 0.0049 * Flux: 100.0%)
- `plugins/generic/filesystem.py` -> **Severity: 0.481** (Bridge: 0.0048 * Flux: 100.0%)
- `lib/request/connect.py` -> **Severity: 0.354** (Bridge: 0.0035 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/core/enums.py` -> **Severity: 40.12** (Embedded: 0.476 * Error Risk: 84.2882%)
- `lib/core/common.py` -> **Severity: 34.311** (Embedded: 0.4012 * Error Risk: 85.5297%)
- `lib/core/exception.py` -> **Severity: 33.577** (Embedded: 0.3789 * Error Risk: 88.6092%)
- `lib/core/settings.py` -> **Severity: 29.784** (Embedded: 0.3484 * Error Risk: 85.4985%)
- `lib/core/data.py` -> **Severity: 24.83** (Embedded: 0.436 * Error Risk: 56.9546%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/core/log.py` -> **Severity: 2562.2** (Blast Radius: 25.622 * Doc Risk: 100.0%)
- `lib/core/datatype.py` -> **Severity: 2514.408** (Blast Radius: 32.573 * Doc Risk: 77.193%)
- `plugins/generic/syntax.py` -> **Severity: 1648.2** (Blast Radius: 16.482 * Doc Risk: 100.0%)
- `lib/core/compat.py` -> **Severity: 1407.938** (Blast Radius: 22.527 * Doc Risk: 62.5%)
- `plugins/generic/filesystem.py` -> **Severity: 1376.844** (Blast Radius: 16.391 * Doc Risk: 84.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 793 literal sites + 12 sites through wrappers = 805

- `getSafeExString` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `lib/utils/sqlalchemy.py`
- `getPageTemplate` (function, panics_and_aborts, primitive): 2 call sites in 2 files -- `lib/core/common.py`
- `setHTTPHandlers` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `lib/request/connect.py`
- `_pympTempLeakPatch` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `lib/core/option.py`
- `setHTTPHandlers` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `lib/utils/search.py`
- `setVerbosity` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `lib/controller/checks.py`
- `shellExec` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `lib/core/convert.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 9733 call pairs -- scoped 38.3%, unique 0.0%, ambiguous 11.5%, external 50.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 9639 | 38.6% | 0.0% | 11.7% | 49.7% |
| shell | 45 | 2.2% | 0.0% | 0.0% | 97.8% |
| c | 42 | 14.3% | 0.0% | 0.0% | 85.7% |
| cpp | 5 | 0.0% | 0.0% | 0.0% | 100.0% |
| db2_sql | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
