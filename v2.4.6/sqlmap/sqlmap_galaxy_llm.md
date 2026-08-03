# ARCHITECTURAL_BRIEF: sqlmap
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/sqlmap` |
| **Timestamp** | `2026-08-03T21:37:55.643945+00:00` |
| **Scan Duration** | `1.21s` |
| **Git Branch** | `master` |
| **Git Commit** | `c310c695a100268f8b91613c33e0541a6e5cda17` |
| **Git Remote** | `https://github.com/sqlmapproject/sqlmap.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 360 malicious artifacts.

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
| Total Artifacts | 653 |
| Analyzed Artifacts (Scanned) | 421 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 232 |
| Total LOC | 18684 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 64.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5061 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.7847 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3445 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 330 | 17683 | 78.4% |
| MARKDOWN | 29 | 0 | 6.9% |
| PLAINTEXT | 15 | 0 | 3.6% |
| XML | 15 | 0 | 3.6% |
| SQLITE | 13 | 51 | 3.1% |
| SHELL | 12 | 242 | 2.9% |
| CPP | 3 | 27 | 0.7% |
| C | 2 | 353 | 0.5% |
| PERL | 1 | 31 | 0.2% |
| YAML | 1 | 297 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.343`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 208 | 49.4% |
| file_cluster_8 | 163 | 38.7% |
| file_cluster_0 | 2 | 0.5% |
| file_cluster_12 | 2 | 0.5% |
| file_cluster_4 | 1 | 0.2% |
| file_cluster_9 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 44 | 10.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 232*

**Composition by Extension & Reason:**
- `.py`: 157x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 29 exceeds 500 chars)
- `.so_`: 27x Excluded (Unsupported Extension: '.so_')
- `.dll_`: 6x Excluded (Unsupported Extension: '.dll_')
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 1x Excluded (Massive Static Asset Blob: 4246 LOC), 1x Excluded (Static Asset Blob without Intent: 1613 LOC), 1x Excluded (Static Asset Blob without Intent: 1576 LOC)
- `.txt`: 1x Excluded (Lexical Monotony: High structural repetition detected in 2855 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 3423 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 10181 LOC)
- `.exe_`: 3x Excluded (Unsupported Extension: '.exe_')
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.asp_`: 2x Excluded (Unsupported Extension: '.asp_')
- `.aspx_`: 2x Excluded (Unsupported Extension: '.aspx_')
- `.cfm_`: 2x Excluded (Unsupported Extension: '.cfm_')
- `.jsp_`: 2x Excluded (Unsupported Extension: '.jsp_')
- `.php_`: 2x Excluded (Unsupported Extension: '.php_')
- `.tx_`: 1x Excluded (Unsupported Extension: '.tx_')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 2.6 | 99.6 | 11.7 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 89.7 | 22.4 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 32.1 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 24.1 | 2.8 | 80.0 |
| API Exposure | 0.0 | 15.1 | 5.4 | 4.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 22.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.1 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 77.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.4 | 0.6 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 27.1 | 3.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 100.0 | 70.8 | 80.0 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 51.7 | 59.4 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 22.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 3.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `extra/shutils/pypi.sh` (Hits: 59)
- `sqlmap.py` (Hits: 38)
- `lib/utils/api.py` (Hits: 32)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **connector.py** (`plugins/generic/connector.py`) — 31 inbound connections
2. **enumeration.py** (`plugins/generic/enumeration.py`) — 30 inbound connections
3. **filesystem.py** (`plugins/generic/filesystem.py`) — 30 inbound connections
4. **fingerprint.py** (`plugins/generic/fingerprint.py`) — 30 inbound connections
5. **misc.py** (`plugins/generic/misc.py`) — 30 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **api.py** (`lib/utils/api.py`) — 32 outbound dependencies
2. **sqlmap.py** (`sqlmap.py`) — 32 outbound dependencies
3. **deps.py** (`lib/utils/deps.py`) — 29 outbound dependencies
4. **hash.py** (`lib/utils/hash.py`) — 29 outbound dependencies
5. **vulnserver.py** (`extra/vulnserver/vulnserver.py`) — 19 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getTables` (@ `plugins/generic/databases.py`) -> Impact: **4200.4** | LOC: 834
- `dumpTable` (@ `plugins/generic/entries.py`) -> Impact: **2635.9** | LOC: 584
- `main` (@ `sqlmap.py`) -> Impact: **2122.3** | LOC: 496
- `__init__` (@ `plugins/generic/takeover.py`) -> Impact: **1436.4** | LOC: 358
  * *Intent:* """ def __init__(self): self.cmdTblName = ("%soutput" % conf.tablePrefix) self.tblField = "data" Abstraction.__init__(self) def osCmd(self):
- `attackDumpedTable` (@ `lib/utils/hash.py`) -> Impact: **1426.4** | LOC: 642
- `getPasswordHashes` (@ `plugins/generic/users.py`) -> Impact: **1340.8** | LOC: 506
- `tableExists` (@ `lib/utils/brute.py`) -> Impact: **1193.3** | LOC: 345
- `getDbs` (@ `plugins/dbms/maxdb/enumeration.py`) -> Impact: **845.7** | LOC: 182
- `getTables` (@ `plugins/dbms/mssqlserver/enumeration.py`) -> Impact: **794.9** | LOC: 378
- `crawl` (@ `lib/utils/crawler.py`) -> Impact: **641.1** | LOC: 222

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `main` (@ `extra/icmpsh/icmpsh_m.py`) -> **O(2^N) [Recursive]**
- `connect` (@ `lib/utils/api.py`) -> **O(2^N) [Recursive]**
- `tableExists` (@ `lib/utils/brute.py`) -> **O(2^N) [Recursive]**
- `_get_cursor` (@ `lib/utils/hashdb.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `lib/utils/sqlalchemy.py`) -> **O(2^N) [Recursive]**
- `getDbs` (@ `plugins/dbms/maxdb/enumeration.py`) -> **O(2^N) [Recursive]**
- `_commentCheck` (@ `plugins/dbms/mysql/fingerprint.py`) -> **O(2^N) [Recursive]**
- `getRoles` (@ `plugins/dbms/oracle/enumeration.py`) -> **O(2^N) [Recursive]**
- `sqlQuery` (@ `plugins/generic/custom.py`) -> **O(2^N) [Recursive]**
- `getTables` (@ `plugins/generic/databases.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `main` (@ `extra/icmpsh/icmpsh_m.py`) -> DB Complexity: **81**
- `connect` (@ `lib/utils/api.py`) -> DB Complexity: **79**
- `main` (@ `sqlmap.py`) -> DB Complexity: **77**
- `purge` (@ `lib/utils/purge.py`) -> DB Complexity: **53**
- `Anonymous_Block_[Truncated]` (@ `extra/shutils/precommit-hook.sh`) -> DB Complexity: **43**
- `runGui` (@ `lib/utils/gui.py`) -> DB Complexity: **41**
- `main` (@ `extra/icmpsh/icmpsh-m.c`) -> DB Complexity: **31**
- `convert` (@ `extra/dbgtool/dbgtool.py`) -> DB Complexity: **30**
- `main` (@ `extra/icmpsh/icmpsh-s.c`) -> DB Complexity: **28**
- `_import_config` (@ `lib/utils/tui.py`) -> DB Complexity: **26**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `plugins/generic` | 13 | 13994.4 | 21.21% | 0.75% |
| `lib/utils` | 21 | 10763.96 | 34.8% | 31.38% |
| `__monolith__` | 4 | 2366.52 | 18.06% | 8.72% |
| `tamper` | 69 | 2011.96 | 8.46% | 97.61% |
| `plugins/dbms/mssqlserver` | 7 | 1789.82 | 13.29% | 10.68% |
| `plugins/dbms/mysql` | 7 | 1183.66 | 17.5% | 12.45% |
| `plugins/dbms/sybase` | 7 | 1160.16 | 11.83% | 9.1% |
| `plugins/dbms/maxdb` | 7 | 1076.62 | 11.2% | 14.29% |
| `plugins/dbms/oracle` | 7 | 987.34 | 13.04% | 8.89% |
| `extra/icmpsh` | 6 | 800.46 | 40.81% | 7.1% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `data/procs/mssqlserver/activate_sp_oacreate.sql` -> **100.0%** Exposure
- `data/procs/mssqlserver/configure_openrowset.sql` -> **100.0%** Exposure
- `data/procs/mssqlserver/configure_xp_cmdshell.sql` -> **100.0%** Exposure
- `data/procs/mssqlserver/create_new_xp_cmdshell.sql` -> **100.0%** Exposure
- `data/procs/mssqlserver/disable_xp_cmdshell_2000.sql` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `lib/utils/getch.py` -> **100.0%** Exposure
- `lib/utils/gui.py` -> **100.0%** Exposure
- `lib/utils/har.py` -> **100.0%** Exposure
- `lib/utils/progress.py` -> **100.0%** Exposure
- `lib/utils/sgmllib.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lib/utils/har.py` -> **5** Orphaned Functions | **7** Duplicates
- `lib/utils/getch.py` -> **0** Orphaned Functions | **8** Duplicates
- `lib/utils/xrange.py` -> **6** Orphaned Functions | **0** Duplicates
- `data/procs/mssqlserver/configure_openrowset.sql` -> **2** Orphaned Functions | **3** Duplicates
- `data/procs/mssqlserver/configure_xp_cmdshell.sql` -> **2** Orphaned Functions | **3** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`lib/utils/deps.py`** -> AI Confidence: **99.39%**
2. **`plugins/generic/databases.py`** -> AI Confidence: **99.39%**
3. **`plugins/generic/users.py`** -> AI Confidence: **99.35%**
4. **`plugins/generic/search.py`** -> AI Confidence: **99.34%**
5. **`extra/vulnserver/vulnserver.py`** -> AI Confidence: **99.31%**
6. **`lib/utils/brute.py`** -> AI Confidence: **99.31%**
7. **`lib/utils/crawler.py`** -> AI Confidence: **99.31%**
8. **`lib/utils/hash.py`** -> AI Confidence: **99.31%**
9. **`lib/utils/hashdb.py`** -> AI Confidence: **99.31%**
10. **`lib/utils/tui.py`** -> AI Confidence: **99.31%**
11. **`plugins/dbms/maxdb/enumeration.py`** -> AI Confidence: **99.31%**
12. **`plugins/dbms/mssqlserver/enumeration.py`** -> AI Confidence: **99.31%**
13. **`plugins/dbms/mssqlserver/fingerprint.py`** -> AI Confidence: **99.31%**
14. **`plugins/dbms/mysql/fingerprint.py`** -> AI Confidence: **99.31%**
15. **`plugins/dbms/oracle/enumeration.py`** -> AI Confidence: **99.31%**
16. **`plugins/dbms/postgresql/fingerprint.py`** -> AI Confidence: **99.31%**
17. **`plugins/dbms/sybase/enumeration.py`** -> AI Confidence: **99.31%**
18. **`plugins/generic/entries.py`** -> AI Confidence: **99.31%**
19. **`plugins/generic/misc.py`** -> AI Confidence: **99.31%**
20. **`plugins/generic/takeover.py`** -> AI Confidence: **99.31%**
21. **`sqlmap.py`** -> AI Confidence: **99.31%**
22. **`lib/utils/api.py`** -> AI Confidence: **99.24%**
23. **`lib/utils/pivotdumptable.py`** -> AI Confidence: **99.24%**
24. **`lib/utils/sqlalchemy.py`** -> AI Confidence: **99.24%**
25. **`plugins/dbms/access/fingerprint.py`** -> AI Confidence: **99.24%**
26. **`plugins/generic/custom.py`** -> AI Confidence: **99.24%**
27. **`plugins/generic/filesystem.py`** -> AI Confidence: **99.24%**
28. **`plugins/dbms/db2/fingerprint.py`** -> AI Confidence: **99.23%**
29. **`plugins/dbms/hsqldb/fingerprint.py`** -> AI Confidence: **99.23%**
30. **`plugins/dbms/presto/fingerprint.py`** -> AI Confidence: **99.23%**
31. **`extra/icmpsh/icmpsh-s.c`** -> AI Confidence: **99.23%**
32. **`lib/utils/har.py`** -> AI Confidence: **99.18%**
33. **`plugins/dbms/access/connector.py`** -> AI Confidence: **99.18%**
34. **`plugins/dbms/altibase/fingerprint.py`** -> AI Confidence: **99.18%**
35. **`plugins/dbms/cache/connector.py`** -> AI Confidence: **99.18%**
36. **`plugins/dbms/clickhouse/fingerprint.py`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `extra/beep/beep.py` -> **100.0%** Exposure
- `extra/icmpsh/icmpsh_m.py` -> **100.0%** Exposure
- `extra/vulnserver/vulnserver.py` -> **100.0%** Exposure
- `lib/utils/api.py` -> **100.0%** Exposure
- `lib/utils/brute.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `extra/beep/beep.py` -> **100.0%** Exposure
- `lib/utils/api.py` -> **100.0%** Exposure
- `lib/utils/gui.py` -> **100.0%** Exposure
- `lib/utils/sqlalchemy.py` -> **100.0%** Exposure
- `plugins/dbms/hsqldb/connector.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `extra/beep/beep.py` -> **100.0%** Exposure
- `extra/cloak/cloak.py` -> **100.0%** Exposure
- `extra/dbgtool/dbgtool.py` -> **100.0%** Exposure
- `extra/icmpsh/icmpsh_m.py` -> **100.0%** Exposure
- `extra/vulnserver/vulnserver.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### 📡 API Network Audit (Set Theory)
- **Shadow APIs (Critical):** `0` undocumented endpoints actively listening.
- **Ghost APIs (Bloat):** `12` endpoints documented but missing from code.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `15` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1683` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `lib/utils/sqlalchemy.py` (PYTHON) -> Cumulative Risk: **835.43**
- **Archetype:** `file_cluster_13` (Distance: 12.779 IQR)
- **Magnitude:** 381.78 | **LOC:** 140 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 245.3), `fetchall` (Impact: 79.2), `select` (Impact: 7.3)

### 2. `lib/utils/har.py` (PYTHON) -> Cumulative Risk: **821.17**
- **Archetype:** `file_cluster_13` (Distance: 11.866 IQR)
- **Magnitude:** 293.52 | **LOC:** 237 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `parse` (Impact: 60.5), `toDict` (Impact: 36.7), `toDict` (Impact: 14.0)

### 3. `lib/utils/hashdb.py` (PYTHON) -> Cumulative Risk: **816.82**
- **Archetype:** `file_cluster_13` (Distance: 11.443 IQR)
- **Magnitude:** 714.08 | **LOC:** 244 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_get_cursor` (Impact: 453.6), `flush` (Impact: 93.0), `write` (Impact: 61.1)

### 4. `lib/utils/api.py` (PYTHON) -> Cumulative Risk: **801.91**
- **Archetype:** `file_cluster_13` (Distance: 11.504 IQR)
- **Magnitude:** 1734.82 | **LOC:** 919 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_client` (Impact: 632.5), `connect` (Impact: 554.3), `task_flush` (Impact: 141.4)

### 5. `lib/utils/progress.py` (PYTHON) -> Cumulative Risk: **781.52**
- **Archetype:** `file_cluster_13` (Distance: 12.874 IQR)
- **Magnitude:** 99.28 | **LOC:** 105 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_convertSeconds` (Impact: 37.8), `__init__` (Impact: 10.5), `__str__` (Impact: 2.8)

### 6. `lib/utils/gui.py` (PYTHON) -> Cumulative Risk: **778.6**
- **Archetype:** `file_cluster_13` (Distance: 10.318 IQR)
- **Magnitude:** 333.14 | **LOC:** 427 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `runGui` (Impact: 274.1)

### 7. `plugins/generic/connector.py` (PYTHON) -> Cumulative Risk: **754.12**
- **Archetype:** `file_cluster_13` (Distance: 12.602 IQR)
- **Magnitude:** 125.58 | **LOC:** 83 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `close` (Impact: 43.8), `printConnected` (Impact: 17.9), `initConnection` (Impact: 8.1)

### 8. `plugins/dbms/oracle/connector.py` (PYTHON) -> Cumulative Risk: **750.44**
- **Archetype:** `file_cluster_13` (Distance: 12.708 IQR)
- **Magnitude:** 101.6 | **LOC:** 78 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%), Documentation (99.9999%)
- **Heaviest Functions:** `fetchall` (Impact: 49.4), `connect` (Impact: 26.9), `select` (Impact: 7.3)

### 9. `tamper/if2case.py` (PYTHON) -> Cumulative Risk: **738.28**
- **Archetype:** `file_cluster_13` (Distance: 9.312 IQR)
- **Magnitude:** 82.08 | **LOC:** 72 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9999%), Documentation (99.972%)
- **Heaviest Functions:** `tamper` (Impact: 74.6), `dependencies` (Impact: 1.8)

### 10. `lib/utils/xrange.py` (PYTHON) -> Cumulative Risk: **736.43**
- **Archetype:** `file_cluster_0` (Distance: 11.211 IQR)
- **Magnitude:** 141.32 | **LOC:** 105 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (99.9999%)
- **Heaviest Functions:** `__getitem__` (Impact: 61.9), `__init__` (Impact: 17.7), `start` (Impact: 14.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `plugins/generic/databases.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.868 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.562 IQR)
- **Top Global Matches:** file_cluster_8: 9.868, file_cluster_13: 10.091, file_cluster_7: 10.482
- **Magnitude:** 4790.82 | **LOC:** 1125 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (31.9031%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getTables` (Impact: 4200.4 | O(2^N) | DB: 6)
  * `getDbs` (Impact: 308.8 | O(N^6) | DB: 2)
  * `getStatements` (Impact: 191.8 | O(N^6) | DB: 2)
  * `getCurrentDb` (Impact: 28.9 | O(N^3))
  * `__init__` (Impact: 3.0 | O(N^2))
    * *Intent:* """ def __init__(self): kb.data.currentDb = "" kb.data.cachedDbs = [] kb.data.cachedTables = {} kb.d...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 428`, `structural_boundaries: 157`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 30`
* *Architecture:* `api: 10`, `import: 50`
* *Defense:* `safety: 18`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.766
  * `Choke Point (Betweenness):` 0.000162 | `Ripple Effect (Closeness):` 0.058672
  * `Imports (Out-Degree: 1):` re, lib.core.common, lib.core.settings, lib.core.enums, lib.request, lib.core.decorators, lib.core.agent, lib.core.dicts...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/generic/entries.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.881 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.745 IQR)
- **Top Global Matches:** file_cluster_8: 9.881, file_cluster_13: 9.918, file_cluster_7: 10.505
- **Magnitude:** 2668.72 | **LOC:** 647 | **CtrlFlow:** 63.5% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (23.8038%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dumpTable` (Impact: 2635.9 | O(2^N) | DB: 6)
  * `__init__` (Impact: 2.7 | O(N^2))
    * *Intent:* """ def __init__(self): pass def dumpTable(self, foundData=None): self.forceDbmsEnum() if conf.db is...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 123`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 14`
* *Architecture:* `api: 6`, `import: 45`
* *Defense:* `safety: 22`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.766
  * `Choke Point (Betweenness):` 0.000497 | `Ripple Effect (Closeness):` 0.058672
  * `Imports (Out-Degree: 2):` re, lib.core.common, lib.core.settings, lib.utils.pivotdumptable, lib.core.convert, lib.core.bigarray, lib.core.enums, lib.request...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sqlmap.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.075 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.734 IQR)
- **Top Global Matches:** file_cluster_13: 11.075, file_cluster_8: 11.311, file_cluster_17: 11.348
- **Magnitude:** 2211.86 | **LOC:** 638 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 77
- **Risk Profile:** Cognitive Load (28.7456%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 2122.3 | O(2^N) | DB: 77)
  * `checkEnvironment` (Impact: 28.9 | O(N^3) | DB: 12)
  * `modulePath` (Impact: 26.5 | O(2^N) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 135`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 15`
* *Architecture:* `io: 38`, `api: 3`, `concurrency: 6`, `import: 67`
* *Defense:* `safety: 43`, `doc: 6`, `test: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.907
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.002381
  * `Imports (Out-Degree: 3):` lib.utils.crawler, lib.controller.controller, os, json, tempfile, bdb, inspect, re...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/utils/hash.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.44 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.309 IQR)
- **Top Global Matches:** file_cluster_13: 11.44, file_cluster_8: 11.706, file_cluster_7: 11.983
- **Magnitude:** 2059.7 | **LOC:** 1331 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (28.9341%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `attackDumpedTable` (Impact: 1426.4 | O(N^6) | DB: 15)
  * `storeHashesToFile` (Impact: 184.5 | O(N^6) | DB: 3)
  * `oscommerce_old_passwd` (Impact: 73.0 | O(N^4) | DB: 2)
  * `unix_md5_passwd` (Impact: 70.4 | O(N^3))
  * `_finalize` (Impact: 68.8 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 337`, `structural_boundaries: 250`, `args: 37`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 48`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 34`, `concurrency: 7`, `import: 74`
* *Defense:* `safety: 54`, `doc: 56`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.044159
  * `Imports (Out-Degree: 0):` os, tempfile, crypt, re, lib.core.common, lib.core.datatype, Crypto.Cipher.DES, gc...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/utils/api.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.504 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.888 IQR)
- **Top Global Matches:** file_cluster_13: 11.504, file_cluster_0: 11.824, file_cluster_8: 11.962
- **Magnitude:** 1734.82 | **LOC:** 919 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 79
- **Risk Profile:** Cognitive Load (24.4366%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_client` (Impact: 632.5 | O(2^N))
    * *Intent:* # Supported adapters: aiohttp, auto, bjoern, cgi, cherrypy, diesel, eventlet, fapws3, flup, gae, gev...
  * `connect` (Impact: 554.3 | O(2^N) | DB: 79)
  * `task_flush` (Impact: 141.4 | O(N^3) | DB: 3)
  * `version` (Impact: 107.0 | O(2^N) | DB: 21)
  * `check_authentication` (Impact: 61.7 | O(N^4))
    * *Intent:* # Generic functions
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 258`, `args: 54`, `func_start: 53`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 61`
* *Architecture:* `io: 32`, `api: 65`, `concurrency: 7`, `import: 62`
* *Defense:* `safety: 26`, `doc: 42`, `sync_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.447
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004762
  * `Imports (Out-Degree: 0):` lib.core.shell, socket, shlex, os, tempfile, gevent, sqlite3, re...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `plugins/generic/users.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.417 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.827 IQR)
- **Top Global Matches:** file_cluster_8: 9.417, file_cluster_13: 9.53, file_cluster_7: 10.011
- **Magnitude:** 1684.28 | **LOC:** 676 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (49.6973%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getPasswordHashes` (Impact: 1340.8 | O(N^6) | DB: 13)
  * `getUsers` (Impact: 191.4 | O(N^6) | DB: 2)
  * `isDba` (Impact: 105.0 | O(2^N))
  * `getCurrentUser` (Impact: 7.4 | O(N^3))
  * `__init__` (Impact: 2.9 | O(N^2))
    * *Intent:* """ def __init__(self): kb.data.currentUser = "" kb.data.isDba = None kb.data.cachedUsers = [] kb.da...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 112`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 18`
* *Architecture:* `io: 3`, `api: 9`, `import: 43`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.766
  * `Choke Point (Betweenness):` 0.000497 | `Ripple Effect (Closeness):` 0.058672
  * `Imports (Out-Degree: 2):` re, lib.core.common, lib.core.settings, lib.utils.pivotdumptable, lib.core.convert, lib.core.enums, lib.request, lib.core.agent...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/generic/takeover.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.224 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.961 IQR)
- **Top Global Matches:** file_cluster_8: 9.224, file_cluster_13: 9.393, file_cluster_7: 9.837
- **Magnitude:** 1563.14 | **LOC:** 482 | **CtrlFlow:** 64.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (20.454%), Tech Debt (9.7306%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 1436.4 | O(2^N) | DB: 6)
    * *Intent:* """ def __init__(self): self.cmdTblName = ("%soutput" % conf.tablePrefix) self.tblField = "data" Abs...
  * `regAdd` (Impact: 99.4 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 77`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 11`, `import: 26`
* *Defense:* `safety: 6`, `doc: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 44.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.095238
  * `Imports (Out-Degree: 0):` lib.core.common, lib.core.enums, lib.takeover.abstraction, lib.takeover.registry, os, lib.takeover.icmpsh, impacket, lib.core.data...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `plugins/generic/search.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.542 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.418 IQR)
- **Top Global Matches:** file_cluster_8: 9.542, file_cluster_13: 9.685, file_cluster_7: 10.157
- **Magnitude:** 1334.46 | **LOC:** 641 | **CtrlFlow:** 69.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (29.93%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `searchColumn` (Impact: 541.2 | O(N^6) | DB: 5)
  * `searchTable` (Impact: 452.7 | O(N^6) | DB: 4)
  * `searchDb` (Impact: 186.4 | O(N^6) | DB: 2)
  * `search` (Impact: 104.7 | O(2^N))
  * `__init__` (Impact: 2.7 | O(N^2))
    * *Intent:* """ def __init__(self): pass def searchDb(self): foundDbs = [] rootQuery = queries[Backend.getIdenti...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 86`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 31`
* *Architecture:* `api: 6`, `import: 33`
* *Defense:* `safety: 3`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.766
  * `Choke Point (Betweenness):` 0.000162 | `Ripple Effect (Closeness):` 0.058672
  * `Imports (Out-Degree: 1):` re, lib.core.common, lib.core.settings, lib.core.enums, lib.request, lib.core.agent, lib.utils.brute, thirdparty...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/utils/tui.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.046 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.907 IQR)
- **Top Global Matches:** file_cluster_8: 12.046, file_cluster_13: 12.13, file_cluster_7: 12.382
- **Magnitude:** 1267.32 | **LOC:** 769 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (20.2744%), Tech Debt (11.3612%)
**Top Internal Functions/Classes:**
  * `_import_config` (Impact: 401.9 | O(N^6) | DB: 26)
  * `_draw_current_tab` (Impact: 336.4 | O(N^6) | DB: 3)
    * *Intent:* # Calculate tab bar height tab_bar_height = self._get_tab_bar_height() start_y = tab_bar_height + 1 ...
  * `run` (Impact: 130.1 | O(N^6) | DB: 9)
    * *Intent:* # Get input key = self.stdscr.getch() tab = self.tabs[self.current_tab] # Handle input if key == cur...
  * `_export_config` (Impact: 119.0 | O(N^6) | DB: 3)
  * `_parse_options` (Impact: 68.7 | O(N^5) | DB: 2)
    * *Intent:* # Parse option groups
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 100`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 80`, `orphaned_logic: 2`
* *Architecture:* `io: 6`, `api: 4`, `import: 15`
* *Defense:* `safety: 59`, `doc: 32`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.486
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib.core.common, lib.core.settings, sys, subprocess, lib.core.enums, lib.core.defaults, thirdparty.six.moves, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils/brute.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.07 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.889 IQR)
- **Top Global Matches:** file_cluster_13: 10.07, file_cluster_8: 10.304, file_cluster_17: 10.812
- **Magnitude:** 1250.58 | **LOC:** 409 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (26.462%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tableExists` (Impact: 1193.3 | O(2^N) | DB: 8)
  * `_addPageTextWords` (Impact: 18.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 95`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 27`
* *Architecture:* `api: 6`, `import: 37`
* *Defense:* `safety: 13`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.343
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.045874
  * `Imports (Out-Degree: 0):` lib.core.common, lib.core.settings, time, lib.core.enums, lib.request, lib.core.decorators, __future__, lib.core.threads...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `plugins/dbms/maxdb/enumeration.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.695 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.17 IQR)
- **Top Global Matches:** file_cluster_8: 8.695, file_cluster_13: 8.717, file_cluster_7: 9.322
- **Magnitude:** 897.88 | **LOC:** 246 | **CtrlFlow:** 50.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (33.8058%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getDbs` (Impact: 845.7 | O(2^N) | DB: 1)
  * `__init__` (Impact: 15.8 | O(2^N))
  * `search` (Impact: 5.3 | O(2^N))
  * `getPrivileges` (Impact: 3.2 | O(N^2))
  * `getPasswordHashes` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 69`, `args: 10`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 3`
* *Architecture:* `api: 13`, `import: 22`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.696
  * `Choke Point (Betweenness):` 5.7e-05 | `Ripple Effect (Closeness):` 0.002381
  * `Imports (Out-Degree: 3):` re, lib.core.common, lib.core.settings, lib.utils.pivotdumptable, lib.core.enums, plugins.generic.enumeration, thirdparty.six.moves, lib.utils.brute...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/dbms/sybase/enumeration.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.726 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.876 IQR)
- **Top Global Matches:** file_cluster_8: 8.726, file_cluster_13: 8.831, file_cluster_7: 9.395
- **Magnitude:** 878.98 | **LOC:** 327 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (34.2016%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getColumns` (Impact: 503.8 | O(N^6))
  * `getUsers` (Impact: 194.5 | O(2^N))
  * `getTables` (Impact: 135.7 | O(N^6) | DB: 1)
  * `search` (Impact: 5.3 | O(2^N))
  * `searchDb` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 85`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 3`
* *Architecture:* `api: 18`, `import: 25`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.696
  * `Choke Point (Betweenness):` 5.7e-05 | `Ripple Effect (Closeness):` 0.002381
  * `Imports (Out-Degree: 3):` re, lib.core.common, lib.core.settings, lib.utils.pivotdumptable, lib.core.enums, plugins.generic.enumeration, thirdparty.six.moves, lib.core.dicts...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/dbms/mssqlserver/enumeration.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.525 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.668 IQR)
- **Top Global Matches:** file_cluster_8: 9.525, file_cluster_13: 9.582, file_cluster_7: 10.149
- **Magnitude:** 874.3 | **LOC:** 447 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (28.1365%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getTables` (Impact: 794.9 | O(N^6) | DB: 8)
  * `getPrivileges` (Impact: 41.5 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 79`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 24`
* *Architecture:* `api: 7`, `import: 27`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.696
  * `Choke Point (Betweenness):` 5.7e-05 | `Ripple Effect (Closeness):` 0.002381
  * `Imports (Out-Degree: 1):` re, lib.core.common, lib.core.settings, lib.core.enums, lib.request, plugins.generic.enumeration, lib.core.agent, thirdparty...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/utils/hashdb.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.443 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.22 IQR)
- **Top Global Matches:** file_cluster_13: 11.443, file_cluster_8: 11.826, file_cluster_4: 11.994
- **Magnitude:** 714.08 | **LOC:** 244 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (39.2628%), Tech Debt (21.8486%)
**Top Internal Functions/Classes:**
  * `_get_cursor` (Impact: 453.6 | O(2^N) | DB: 4)
  * `flush` (Impact: 93.0 | O(N^6) | DB: 5)
  * `write` (Impact: 61.1 | O(N^5))
  * `endTransaction` (Impact: 37.7 | O(N^5) | DB: 2)
  * `beginTransaction` (Impact: 26.7 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 74`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 19`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 9`, `concurrency: 7`, `import: 24`
* *Defense:* `safety: 32`, `doc: 2`, `sync_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.486
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib.core.common, lib.core.datatype, lib.core.settings, threading, time, hashlib, lib.core.convert, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugins/dbms/mysql/fingerprint.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.791 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.421 IQR)
- **Top Global Matches:** file_cluster_8: 7.791, file_cluster_13: 8.379, file_cluster_7: 8.54
- **Magnitude:** 688.52 | **LOC:** 343 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (13.0225%), Tech Debt (15.8408%)
**Top Internal Functions/Classes:**
  * `_commentCheck` (Impact: 406.8 | O(2^N))
  * `checkDbms` (Impact: 243.8 | O(N^6))
  * `checkDbmsOs` (Impact: 21.8 | O(N^3))
  * `__init__` (Impact: 5.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 55`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `api: 6`, `import: 18`
* *Defense:* `doc: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.696
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.002381
  * `Imports (Out-Degree: 1):` re, lib.core.common, lib.core.settings, lib.core.convert, lib.core.enums, lib.request, plugins.generic.fingerprint, lib.core.data...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/utils/crawler.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.115 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.902 IQR)
- **Top Global Matches:** file_cluster_13: 11.115, file_cluster_17: 11.621, file_cluster_8: 11.657
- **Magnitude:** 655.4 | **LOC:** 266 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (24.4454%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `crawl` (Impact: 641.1 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 85`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 6`, `dead_code: 3`
* *Architecture:* `io: 2`, `api: 4`, `import: 33`
* *Defense:* `safety: 18`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003175
  * `Imports (Out-Degree: 0):` os, tempfile, thirdparty.beautifulsoup.beautifulsoup, re, lib.core.common, lib.core.datatype, thirdparty.six.moves, thirdparty...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/dbms/oracle/enumeration.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.983 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.336 IQR)
- **Top Global Matches:** file_cluster_8: 7.983, file_cluster_13: 8.23, file_cluster_7: 8.748
- **Magnitude:** 617.48 | **LOC:** 166 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (18.5639%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getRoles` (Impact: 613.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 46`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 19`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.696
  * `Choke Point (Betweenness):` 5.7e-05 | `Ripple Effect (Closeness):` 0.002381
  * `Imports (Out-Degree: 1):` lib.core.common, lib.core.settings, lib.core.enums, lib.request, plugins.generic.enumeration, lib.core.data, lib.core.compat, lib.core.exception
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/generic/filesystem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.833 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.063 IQR)
- **Top Global Matches:** file_cluster_13: 9.833, file_cluster_8: 10.131, file_cluster_7: 10.571
- **Magnitude:** 570.88 | **LOC:** 328 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (16.2337%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `askCheckWrittenFile` (Impact: 313.1 | O(N^6) | DB: 1)
  * `fileContentEncode` (Impact: 104.5 | O(N^6) | DB: 1)
  * `__init__` (Impact: 86.0 | O(N^5) | DB: 8)
    * *Intent:* """ def __init__(self): self.fileTblName = "%sfile" % conf.tablePrefix self.tblField = "data" def _c...
  * `fileToSqlQueries` (Impact: 18.2 | O(N^4) | DB: 2)
  * `fileEncode` (Impact: 10.3 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 88`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 18`
* *Architecture:* `io: 3`, `api: 16`, `import: 31`
* *Defense:* `safety: 4`, `doc: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 44.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.095238
  * `Imports (Out-Degree: 0):` lib.core.common, lib.core.settings, sys, lib.core.convert, lib.core.enums, lib.request, lib.core.agent, codecs...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `plugins/generic/custom.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.18 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.151 IQR)
- **Top Global Matches:** file_cluster_13: 9.18, file_cluster_8: 9.316, file_cluster_7: 9.915
- **Magnitude:** 561.54 | **LOC:** 160 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (13.7278%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sqlQuery` (Impact: 551.5 | O(2^N) | DB: 3)
  * `__init__` (Impact: 2.7 | O(N^2))
    * *Intent:* """ def __init__(self): pass def sqlQuery(self, query): output = None sqlType = None query = query.r...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 62`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 1`, `api: 5`, `import: 23`
* *Defense:* `safety: 6`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.766
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.058672
  * `Imports (Out-Degree: 0):` re, lib.core.common, lib.core.settings, lib.core.shell, sys, lib.core.convert, lib.core.enums, lib.request...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/dbms/mssqlserver/filesystem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.703 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.365 IQR)
- **Top Global Matches:** file_cluster_13: 9.703, file_cluster_8: 9.766, file_cluster_17: 10.181
- **Magnitude:** 528.18 | **LOC:** 427 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (12.38%), Tech Debt (11.0899%)
**Top Internal Functions/Classes:**
  * `_dataToScr` (Impact: 286.1 | O(2^N) | DB: 11)
  * `_stackedWriteFileCertutilExe` (Impact: 201.9 | O(2^N) | DB: 3)
  * `_stackedWriteFileVbs` (Impact: 11.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 65`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 20`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 4`, `import: 23`
* *Defense:* `safety: 3`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.696
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.002381
  * `Imports (Out-Degree: 1):` lib.core.common, lib.core.convert, lib.core.enums, lib.request, plugins.generic.filesystem, codecs, os, ntpath...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/utils/pivotdumptable.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.863 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.265 IQR)
- **Top Global Matches:** file_cluster_13: 9.863, file_cluster_8: 10.261, file_cluster_7: 10.841
- **Magnitude:** 445.48 | **LOC:** 189 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (26.9792%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pivotDumpTable` (Impact: 427.6 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 73`, `args: 3`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 13`
* *Architecture:* `api: 2`, `import: 29`
* *Defense:* `safety: 6`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.895
  * `Choke Point (Betweenness):` 0.000358 | `Ripple Effect (Closeness):` 0.045874
  * `Imports (Out-Degree: 1):` re, lib.core.common, lib.core.settings, lib.core.convert, lib.core.bigarray, lib.core.enums, lib.request, lib.core.agent...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/utils/sqlalchemy.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.779 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.982 IQR)
- **Top Global Matches:** file_cluster_13: 12.779, file_cluster_17: 13.332, file_cluster_8: 13.373
- **Magnitude:** 381.78 | **LOC:** 140 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (66.6581%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 245.3 | O(2^N) | DB: 17)
  * `fetchall` (Impact: 79.2 | O(2^N) | DB: 2)
  * `select` (Impact: 7.3 | O(N^3))
  * `getSafeExString` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 46`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 39`
* *Architecture:* `io: 7`, `api: 7`, `import: 18`
* *Defense:* `safety: 18`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.486
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` re, traceback, sys, plugins.generic.connector, importlib, logging, os, sqlalchemy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils/search.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.618 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.119 IQR)
- **Top Global Matches:** file_cluster_13: 9.618, file_cluster_8: 9.751, file_cluster_7: 10.351
- **Magnitude:** 379.3 | **LOC:** 214 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (10.3146%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_search` (Impact: 372.2 | O(2^N) | DB: 9)
  * `setHTTPHandlers` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 76`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 6`
* *Architecture:* `io: 4`, `api: 2`, `import: 30`
* *Defense:* `safety: 17`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.486
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, lib.core.common, lib.core.settings, lib.request.basic, lib.core.convert, socket, lib.core.enums, lib.core.decorators...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extra/icmpsh/icmpsh-s.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.64 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.478 IQR)
- **Top Global Matches:** file_cluster_8: 12.64, file_cluster_13: 12.697, file_cluster_0: 13.047
- **Magnitude:** 375.14 | **LOC:** 345 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (74.435%), Tech Debt (12.703%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 137.6 | O(N^2) | DB: 28)
  * `load_deps` (Impact: 19.7 | O(N^3) | DB: 8)
  * `spawn_shell` (Impact: 8.3 | O(N^1) | DB: 8)
    * *Intent:* * along with this program. If not, see <http://www.gnu.org/licenses/>. */ #include <stdio.h> #includ...
  * `transfer_icmp` (Impact: 7.2 | O(N^1) | DB: 6)
  * `usage` (Impact: 5.9 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 22`, `args: 2`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 150`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 40`, `import: 6`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.486
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` iphlpapi.h, windows.h, stdlib.h, winsock2.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugins/generic/misc.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.415 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.81 IQR)
- **Top Global Matches:** file_cluster_8: 8.415, file_cluster_13: 8.478, file_cluster_7: 8.998
- **Magnitude:** 344.22 | **LOC:** 205 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (13.693%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getRemoteTempPath` (Impact: 310.5 | O(N^6))
  * `likeOrExact` (Impact: 18.2 | O(N^3))
  * `__init__` (Impact: 2.7 | O(N^2))
    * *Intent:* """ def __init__(self): pass def getRemoteTempPath(self): if not conf.tmpPath and Backend.isDbms(DBM...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 57`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 10`, `import: 20`
* *Defense:* `safety: 1`, `doc: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.799
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.071429
  * `Imports (Out-Degree: 0):` re, lib.core.common, lib.core.enums, lib.request, ntpath, lib.core.data, lib.core.exception
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `extra/icmpsh/icmpsh-m.pl` (PERL) | Magnitude: 30.62 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 19, indent_spaces: 17, state_mutation: 15, structural_boundaries: 14
- `lib/utils/xrange.py` (PYTHON) | Magnitude: 141.32 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 29, encapsulation: 26, branch: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `extra/shutils/autocompletion.sh` (SHELL) | Magnitude: 9.58 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: io: 7, state_mutation: 6, structural_boundaries: 5, reflection_metaprogramming: 2
- `extra/shutils/recloak.sh` (SHELL) | Magnitude: 9.08 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, io: 7, safety_bypasses: 4, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tamper/space2mysqlblank.py` (PYTHON) | Magnitude: 56.62 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 15, branch: 9, import: 6
- `plugins/dbms/altibase/enumeration.py` (PYTHON) | Magnitude: 10.72 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 7, api: 5, args: 2
- `tamper/apostrophemask.py` (PYTHON) | Magnitude: 5.94 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, doc: 4, args: 2, func_start: 2
- `tamper/apostrophenullencode.py` (PYTHON) | Magnitude: 5.94 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, doc: 4, args: 2, func_start: 2
- `tamper/escapequotes.py` (PYTHON) | Magnitude: 5.94 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, doc: 4, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `lib/utils/timeout.py` (PYTHON) | Magnitude: 70.42 | Delta: **0.217 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, state_mutation: 16, structural_boundaries: 14, concurrency: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tamper/randomcomments.py` (PYTHON) | Magnitude: 49.68 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 12, branch: 8, import: 5
- `plugins/dbms/maxdb/enumeration.py` (PYTHON) | Magnitude: 897.88 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 155, branch: 70, structural_boundaries: 69, import: 22
- `tamper/bluecoat.py` (PYTHON) | Magnitude: 33.9 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 12, branch: 7, doc: 4
- `tamper/charunicodeencode.py` (PYTHON) | Magnitude: 25.22 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 9, branch: 4, doc: 4
- `tamper/least.py` (PYTHON) | Magnitude: 25.58 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 7, branch: 5, doc: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `extra/shutils/strip.sh` (SHELL) | Magnitude: 2.36 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: sec_dead_code: 3, args: 2, dead_code: 1, orphaned_logic: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `sqlmap.py` -> **Miroslav Stampar** (100.0% isolated ownership) | Magnitude: 2211.86
- `lib/utils/hash.py` -> **Miroslav Stampar** (100.0% isolated ownership) | Magnitude: 2059.7
- `lib/utils/api.py` -> **Miroslav Stampar** (100.0% isolated ownership) | Magnitude: 1734.82
- `plugins/generic/users.py` -> **Miroslav Stampar** (100.0% isolated ownership) | Magnitude: 1684.28
- `plugins/generic/takeover.py` -> **Miroslav Stampar** (100.0% isolated ownership) | Magnitude: 1563.14

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/utils/pivotdumptable.py` -> **Severity: 0.033** (Bridge: 0.0004 * Flux: 90.9678%)
- `plugins/generic/users.py` -> **Severity: 0.015** (Bridge: 0.0005 * Flux: 30.8401%)
- `plugins/generic/entries.py` -> **Severity: 0.012** (Bridge: 0.0005 * Flux: 23.6263%)
- `plugins/generic/search.py` -> **Severity: 0.009** (Bridge: 0.0002 * Flux: 56.4878%)
- `plugins/dbms/mssqlserver/enumeration.py` -> **Severity: 0.004** (Bridge: 0.0001 * Flux: 62.3072%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `plugins/generic/syntax.py` -> **Severity: 4.3** (Embedded: 0.0952 * Error Risk: 45.1515%)
- `plugins/generic/search.py` -> **Severity: 3.083** (Embedded: 0.0587 * Error Risk: 52.541%)
- `plugins/generic/entries.py` -> **Severity: 2.978** (Embedded: 0.0587 * Error Risk: 50.751%)
- `lib/utils/hash.py` -> **Severity: 2.265** (Embedded: 0.0442 * Error Risk: 51.3018%)
- `plugins/generic/connector.py` -> **Severity: 1.973** (Embedded: 0.0738 * Error Risk: 26.7252%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `plugins/generic/syntax.py` -> **Severity: 4473.596** (Blast Radius: 44.736 * Doc Risk: 99.9999%)
- `plugins/generic/fingerprint.py` -> **Severity: 4473.587** (Blast Radius: 44.736 * Doc Risk: 99.9997%)
- `plugins/generic/filesystem.py` -> **Severity: 4454.842** (Blast Radius: 44.736 * Doc Risk: 99.5807%)
- `plugins/generic/enumeration.py` -> **Severity: 4276.331** (Blast Radius: 42.814 * Doc Risk: 99.8816%)
- `plugins/generic/connector.py` -> **Severity: 4062.9** (Blast Radius: 40.629 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
