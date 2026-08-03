# ARCHITECTURAL_BRIEF: sqlite
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/sqlite` |
| **Timestamp** | `2026-08-03T21:37:51.730570+00:00` |
| **Scan Duration** | `5.9s` |
| **Git Branch** | `master` |
| **Git Commit** | `f270460366134e350ad6e1509957f812c9700d2b` |
| **Git Remote** | `https://github.com/sqlite/sqlite.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 473 malicious artifacts.

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
| Total Artifacts | 2200 |
| Analyzed Artifacts (Scanned) | 533 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1667 |
| Total LOC | 226313 |
| Volatility Index | 0.008 |
| % Scanned of codebase = | 24.2% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6467 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3011 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5163 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 33 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 313 | 194940 | 58.7% |
| JAVA | 58 | 5367 | 10.9% |
| TCL | 37 | 9992 | 6.9% |
| JAVASCRIPT | 37 | 10046 | 6.9% |
| MARKDOWN | 26 | 0 | 4.9% |
| HTML | 18 | 1867 | 3.4% |
| PLAINTEXT | 13 | 0 | 2.4% |
| SHELL | 13 | 1920 | 2.4% |
| MAKEFILE | 7 | 1450 | 1.3% |
| CSS | 2 | 122 | 0.4% |
| SQLITE | 2 | 45 | 0.4% |
| BATCH | 2 | 237 | 0.4% |
| M4 | 2 | 20 | 0.4% |
| CSHARP | 2 | 307 | 0.4% |
| XML | 1 | 0 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.368`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 395 | 74.1% |
| file_cluster_13 | 60 | 11.3% |
| file_cluster_16 | 9 | 1.7% |
| file_cluster_4 | 7 | 1.3% |
| file_cluster_17 | 6 | 1.1% |
| file_cluster_0 | 6 | 1.1% |
| file_cluster_9 | 4 | 0.8% |
| file_cluster_11 | 4 | 0.8% |
| file_cluster_12 | 1 | 0.2% |
| file_cluster_2 | 1 | 0.2% |
| file_cluster_6 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 39 | 7.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1667*

**Composition by Extension & Reason:**
- `.test`: 1466x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.test)
- `.tcl`: 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 21x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 167 LOC)
- `.c`: 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 6204 LOC), 1x Excluded (Machine-Generated Source Code Signature: 384 LOC)
- `.db`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sql`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.linux-generic'), 1x Excluded (Lexical Monotony: High structural repetition detected in 2205 LOC)
- `.txt`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 24429 LOC), 1x Unsupported Format (.undeterminable)
- `.sh`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.in`: 1x Excluded (Machine-Generated Source Code Signature: 560 LOC), 1x Excluded (Machine-Generated Source Code Signature: 51 LOC), 1x Excluded (Machine-Generated Source Code Signature: 41 LOC)
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1297 LOC)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.y`: 1x Excluded (Machine-Generated Source Code Signature: 2161 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.msc`: 2x Excluded (Unsupported Extension: '.msc')
- `.gif`: 2x Excluded (Explicitly Denied Extension: '.gif')
- `.def`: 2x Unsupported Format (.undeterminable)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 53.3 | 67.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 46.1 | 52.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 28.6 | 13.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 35.3 | 2.5 | 80.0 |
| API Exposure | 0.0 | 16.9 | 8.3 | 10.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 67.5 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 98.5 | 1.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 91.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.2 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 7.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 59.7 | 82.7 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 54.3 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 16.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 4.9 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `autosetup/teaish/core.tcl` (Hits: 94)
- `ext/wasm/index.html` (Hits: 83)
- `autosetup/autosetup` (Hits: 81)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **sqliteInt.h** (`src/sqliteInt.h`) — 107 inbound connections
2. **sqlite3ext.h** (`src/sqlite3ext.h`) — 61 inbound connections
3. **tclsqlite.h** (`src/tclsqlite.h`) — 43 inbound connections
4. **vdbeInt.h** (`src/vdbeInt.h`) — 15 inbound connections
5. **fts3Int.h** (`ext/fts3/fts3Int.h`) — 12 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **jimsh0.c** (`autosetup/jimsh0.c`) — 38 outbound dependencies
2. **sqliteInt.h** (`src/sqliteInt.h`) — 26 outbound dependencies
3. **shell.c.in** (`src/shell.c.in`) — 24 outbound dependencies
4. **os_unix.c** (`src/os_unix.c`) — 21 outbound dependencies
5. **fileio.c** (`ext/misc/fileio.c`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `jsonTranslateBlobToText` (@ `src/json.c`) -> Impact: **11485.2** | LOC: 1904
- `balance` (@ `src/btree.c`) -> Impact: **5568.6** | LOC: 1362
- `translate_code` (@ `tool/lemon.c`) -> Impact: **4837.7** | LOC: 1456
- `setupLookaside` (@ `src/main.c`) -> Impact: **4594.0** | LOC: 1862
  * *Intent:* /* EVIDENCE-OF: R-39100-27317 The SQLITE_CONFIG_PCACHE_HDRSZ option takes ** a single parameter which is a pointer to an integer and writes into
- `tclSqlFunc` (@ `src/tclsqlite.c`) -> Impact: **4305.2** | LOC: 1825
- `sqlite3VdbeExec` (@ `src/vdbe.c`) -> Impact: **4113.6** | LOC: 2009
- `ctor` (@ `ext/wasm/api/sqlite3-api-oo1.c-pp.js`) -> Impact: **3153.8** | LOC: 757
- `sqlite3Update` (@ `src/update.c`) -> Impact: **2423.1** | LOC: 747
  * *Intent:* ** ** Or, if pLimit and pOrderBy are not NULL, and pTab is not a view: ** ** SELECT <other-columns>, pChanges FROM pTabList ** WHERE pWhere ** GROUP B...
- `sqlite3Select` (@ `src/select.c`) -> Impact: **2414.6** | LOC: 1251
- `setSharedCacheTableLock` (@ `src/btree.c`) -> Impact: **2035.3** | LOC: 1900
  * *Intent:* /* If the client is reading or writing an index and the schema is ** not loaded, then it is too difficult to actually check to see if ** the correct l...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `JimGlobMatch` (@ `autosetup/jimsh0.c`) -> **O(2^N) [Recursive]**
- `Jim_GetVariable` (@ `autosetup/jimsh0.c`) -> **O(2^N) [Recursive]**
- `base64` (@ `ext/misc/base64.c`) -> **O(2^N) [Recursive]**
- `base85` (@ `ext/misc/base85.c`) -> **O(2^N) [Recursive]**
  * *Intent:* # endif /* This function does the work for the SQLite base85(x) UDF. */
- `is_base85` (@ `ext/misc/base85.c`) -> **O(2^N) [Recursive]**
  * *Intent:* #endif #ifndef BASE85_STANDALONE # ifndef OMIT_BASE85_CHECKER /* This function does the work for the SQLite is_base85(t) UDF. */
- `zipfileUpdate` (@ `ext/misc/zipfile.c`) -> **O(2^N) [Recursive]**
- `qrfEqpRenderLevel` (@ `ext/qrf/qrf.c`) -> **O(2^N) [Recursive]**
- `balance` (@ `src/btree.c`) -> **O(2^N) [Recursive]**
- `exprDup` (@ `src/expr.c`) -> **O(2^N) [Recursive]**
  * *Intent:* /* ** Construct a new expression node for a function with multiple ** arguments. */
- `sqlite3ExprIsInteger` (@ `src/expr.c`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `translate_code` (@ `tool/lemon.c`) -> DB Complexity: **658**
- `setSharedCacheTableLock` (@ `src/btree.c`) -> DB Complexity: **484**
  * *Intent:* /* If the client is reading or writing an index and the schema is ** not loaded, then it is too difficult to actually check to see if ** the correct l...
- `sqlite3VdbeExec` (@ `src/vdbe.c`) -> DB Complexity: **478**
- `setupLookaside` (@ `src/main.c`) -> DB Complexity: **411**
  * *Intent:* /* EVIDENCE-OF: R-39100-27317 The SQLITE_CONFIG_PCACHE_HDRSZ option takes ** a single parameter which is a pointer to an integer and writes into
- `jsonTranslateBlobToText` (@ `src/json.c`) -> DB Complexity: **400**
- `tclSqlFunc` (@ `src/tclsqlite.c`) -> DB Complexity: **393**
- `balance` (@ `src/btree.c`) -> DB Complexity: **304**
- `KeccakF1600Step` (@ `ext/misc/shathree.c`) -> DB Complexity: **247**
  * *Intent:* ** The sha3_agg(Y) function computes the SHA3 hash of all Y inputs. Since ** order is important for the hash, it is recommended that the Y expression ...
- `KeccakF1600Step` (@ `tool/mksourceid.c`) -> DB Complexity: **247**
  * *Intent:* # define BYTEORDER 1234 # elif defined(sparc) || defined(__ppc__) # define BYTEORDER 4321 # else
- `KeccakF1600Step` (@ `tool/src-verify.c`) -> DB Complexity: **247**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 149 | 182825.94 | 64.22% | 27.82% |
| `tool` | 54 | 35699.34 | 62.62% | 29.82% |
| `ext/misc` | 62 | 32357.8 | 73.71% | 26.83% |
| `autosetup` | 12 | 23195.5 | 47.02% | 27.8% |
| `ext/fts5` | 16 | 21645.08 | 63.09% | 25.48% |
| `ext/wasm` | 28 | 19089.76 | 29.19% | 32.81% |
| `ext/fts3` | 17 | 12416.92 | 61.48% | 17.5% |
| `ext/wasm/api` | 20 | 10925.55 | 25.13% | 37.57% |
| `ext/session` | 6 | 8642.38 | 68.81% | 27.85% |
| `ext/qrf` | 4 | 5349.26 | 20.08% | 2.19% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `autosetup/autosetup-find-tclsh` -> **100.0%** Exposure
- `configure` -> **100.0%** Exposure
- `ext/fts3/tool/fts3cov.sh` -> **100.0%** Exposure
- `ext/wasm/split-speedtest1-script.sh` -> **100.0%** Exposure
- `tool/cktclsh.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `autoconf/tea/configure` -> **100.0%** Exposure
- `configure` -> **100.0%** Exposure
- `ext/fts3/tool/fts3cov.sh` -> **100.0%** Exposure
- `ext/wasm/split-speedtest1-script.sh` -> **100.0%** Exposure
- `tool/mkautoconfamal.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/vdbeapi.c` -> **73** Orphaned Functions | **0** Duplicates
- `src/vdbeaux.c` -> **62** Orphaned Functions | **0** Duplicates
- `ext/jni/src/org/sqlite/jni/wrapper1/Sqlite.java` -> **42** Orphaned Functions | **18** Duplicates
- `ext/jni/src/org/sqlite/jni/wrapper1/SqlFunction.java` -> **21** Orphaned Functions | **35** Duplicates
- `ext/jni/src/org/sqlite/jni/capi/SQLTester.java` -> **6** Orphaned Functions | **32** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`ext/misc/base85.c`** -> AI Confidence: **99.48%**
2. **`ext/misc/fileio.c`** -> AI Confidence: **99.48%**
3. **`src/shell.c.in`** -> AI Confidence: **99.48%**
4. **`tool/showdb.c`** -> AI Confidence: **99.48%**
5. **`tool/showwal.c`** -> AI Confidence: **99.48%**
6. **`tool/sqldiff.c`** -> AI Confidence: **99.48%**
7. **`tool/sqlite3_rsync.c`** -> AI Confidence: **99.48%**
8. **`autosetup/jimsh0.c`** -> AI Confidence: **99.39%**
9. **`ext/misc/csv.c`** -> AI Confidence: **99.39%**
10. **`ext/misc/sqlite3_stdio.c`** -> AI Confidence: **99.39%**
11. **`src/os_unix.c`** -> AI Confidence: **99.39%**
12. **`src/tclsqlite.c`** -> AI Confidence: **99.39%**
13. **`src/test_sqllog.c`** -> AI Confidence: **99.39%**
14. **`tool/dbhash.c`** -> AI Confidence: **99.39%**
15. **`tool/loadfts.c`** -> AI Confidence: **99.39%**
16. **`tool/showshm.c`** -> AI Confidence: **99.39%**
17. **`ext/expert/expert.c`** -> AI Confidence: **99.34%**
18. **`ext/fts3/fts3_porter.c`** -> AI Confidence: **99.34%**
19. **`ext/fts3/fts3_write.c`** -> AI Confidence: **99.34%**
20. **`ext/fts3/tool/fts3view.c`** -> AI Confidence: **99.34%**
21. **`ext/misc/decimal.c`** -> AI Confidence: **99.34%**
22. **`ext/misc/series.c`** -> AI Confidence: **99.34%**
23. **`ext/misc/spellfix.c`** -> AI Confidence: **99.34%**
24. **`ext/repair/checkindex.c`** -> AI Confidence: **99.34%**
25. **`ext/session/changeset.c`** -> AI Confidence: **99.34%**
26. **`ext/session/changesetfuzz.c`** -> AI Confidence: **99.34%**
27. **`src/test_config.c`** -> AI Confidence: **99.34%**
28. **`src/test_delete.c`** -> AI Confidence: **99.34%**
29. **`tool/index_usage.c`** -> AI Confidence: **99.34%**
30. **`tool/showstat4.c`** -> AI Confidence: **99.34%**
31. **`tool/showtmlog.c`** -> AI Confidence: **99.34%**
32. **`tool/src-verify.c`** -> AI Confidence: **99.34%**
33. **`ext/misc/ieee754.c`** -> AI Confidence: **99.32%**
34. **`ext/misc/regexp.c`** -> AI Confidence: **99.32%**
35. **`ext/misc/totype.c`** -> AI Confidence: **99.32%**
36. **`ext/wasm/mkwasmbuilds.c`** -> AI Confidence: **99.32%**
37. **`src/tokenize.c`** -> AI Confidence: **99.32%**
38. **`src/utf.c`** -> AI Confidence: **99.32%**
39. **`src/vdbe.c`** -> AI Confidence: **99.32%**
40. **`tool/checkSpacing.c`** -> AI Confidence: **99.32%**
41. **`tool/enlargedb.c`** -> AI Confidence: **99.32%**
42. **`tool/stripccomments.c`** -> AI Confidence: **99.32%**
43. **`tool/version-info.c`** -> AI Confidence: **99.32%**
44. **`autosetup/autosetup`** -> AI Confidence: **99.31%**
45. **`ext/fts3/fts3_icu.c`** -> AI Confidence: **99.31%**
46. **`ext/icu/icu.c`** -> AI Confidence: **99.31%**
47. **`ext/misc/vfslog.c`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `src/where.c` -> **0.002%** Exposure
- `src/pager.c` -> **0.0001%** Exposure
- `src/vdbemem.c` -> **0.0001%** Exposure
### Exploit Generation Surface
- `ext/wasm/GNUmakefile` -> **100.0%** Exposure
- `autoconf/tea/teaish.tcl` -> **100.0%** Exposure
- `autosetup/find_tclconfig.tcl` -> **100.0%** Exposure
- `autosetup/proj.tcl` -> **100.0%** Exposure
- `autosetup/sqlite-config.tcl` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `ext/jni/GNUmakefile` -> **100.0%** Exposure
- `ext/wasm/GNUmakefile` -> **100.0%** Exposure
- `autosetup/find_tclconfig.tcl` -> **100.0%** Exposure
- `autosetup/pkg-config.tcl` -> **100.0%** Exposure
- `autosetup/proj.tcl` -> **100.0%** Exposure
### Raw Memory Manipulation
- `ext/wasm/c-pp-lite.c` -> **100.0%** Exposure
- `autosetup/jimsh0.c` -> **10.0%** Exposure
- `ext/expert/sqlite3expert.c` -> **10.0%** Exposure
- `ext/fts3/fts3_aux.c` -> **10.0%** Exposure
- `ext/fts3/fts3_expr.c` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `autosetup/autosetup` -> **100.0%** Exposure
- `autosetup/jimsh0.c` -> **100.0%** Exposure
- `ext/expert/expert.c` -> **100.0%** Exposure
- `ext/expert/sqlite3expert.c` -> **100.0%** Exposure
- `ext/expert/test_expert.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `15` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1311` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `ext/wasm/c-pp-lite.c` (C) -> Cumulative Risk: **905.87**
- **Archetype:** `file_cluster_8` (Distance: 14.096 IQR)
- **Magnitude:** 2150.04 | **LOC:** 2805 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `cmpp_t_out_expand` (Impact: 101.8), `cmpp_is_legal_key` (Impact: 97.5), `cmpp_kwd_include` (Impact: 75.1)

### 2. `src/select.c` (C) -> Cumulative Risk: **849.76**
- **Archetype:** `file_cluster_8` (Distance: 15.197 IQR)
- **Magnitude:** 13613.12 | **LOC:** 8983 | **CtrlFlow:** 83.7% | **Authorship Centralization:** 72.2%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `sqlite3Select` (Impact: 2414.6), `selectExpander` (Impact: 558.4), `flattenSubquery` (Impact: 541.3)

### 3. `ext/fts5/fts5_main.c` (C) -> Cumulative Risk: **831.52**
- **Archetype:** `file_cluster_8` (Distance: 14.499 IQR)
- **Magnitude:** 3497.94 | **LOC:** 3876 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `fts5FilterMethod` (Impact: 143.5), `fts5UpdateMethod` (Impact: 101.8), `fts5CacheInstArray` (Impact: 63.1)

### 4. `ext/wasm/fiddle/fiddle-worker.js` (JAVASCRIPT) -> Cumulative Risk: **800.32**
- **Archetype:** `file_cluster_8` (Distance: 10.439 IQR)
- **Magnitude:** 369.66 | **LOC:** 387 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9956%)
- **Heaviest Functions:** `f` (Impact: 226.1), `f` (Impact: 29.9), `f` (Impact: 27.4)

### 5. `ext/session/session_common.tcl` (TCL) -> Cumulative Risk: **794.89**
- **Archetype:** `file_cluster_4` (Distance: 13.633 IQR)
- **Magnitude:** 449.26 | **LOC:** 304 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9999%), Safety Score (98.5161%)
- **Heaviest Functions:** `xConflict` (Impact: 162.5), `do_changeset_test` (Impact: 2.0), `do_patchset_test` (Impact: 2.0)

### 6. `ext/qrf/qrf.c` (C) -> Cumulative Risk: **794.14**
- **Archetype:** `file_cluster_8` (Distance: 15.08 IQR)
- **Magnitude:** 5277.66 | **LOC:** 2984 | **CtrlFlow:** 84.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `qrfColumnar` (Impact: 823.3), `qrfOneSimpleRow` (Impact: 300.2), `qrfWrapLine` (Impact: 182.9)

### 7. `src/vdbeapi.c` (C) -> Cumulative Risk: **789.9**
- **Archetype:** `file_cluster_8` (Distance: 14.188 IQR)
- **Magnitude:** 2444.54 | **LOC:** 2633 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `sqlite3_stmt_scanstatus_v2` (Impact: 157.4), `sqlite3_preupdate_old` (Impact: 76.8), `sqlite3Step` (Impact: 64.0)

### 8. `src/vdbeblob.c` (C) -> Cumulative Risk: **786.25**
- **Archetype:** `file_cluster_8` (Distance: 13.884 IQR)
- **Magnitude:** 625.62 | **LOC:** 535 | **CtrlFlow:** 82.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.565%)
- **Heaviest Functions:** `sqlite3_blob_open` (Impact: 195.9), `blobSeekToRow` (Impact: 26.9), `sqlite3_blob_reopen` (Impact: 8.4)

### 9. `src/util.c` (C) -> Cumulative Risk: **785.32**
- **Archetype:** `file_cluster_8` (Distance: 15.229 IQR)
- **Magnitude:** 2201.64 | **LOC:** 2041 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `sqlite3Atoi64` (Impact: 148.5), `sqlite3AtoF` (Impact: 88.0), `sqlite3GetVarint` (Impact: 86.8)

### 10. `src/vdbeaux.c` (C) -> Cumulative Risk: **772.83**
- **Archetype:** `file_cluster_8` (Distance: 15.09 IQR)
- **Magnitude:** 5627.68 | **LOC:** 5585 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `sqlite3VdbeRecordCompareWithSkip` (Impact: 426.6), `vdbeRecordCompareDebug` (Impact: 239.1), `displayP4Expr` (Impact: 213.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `autosetup/jimsh0.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.296 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.806 IQR)
- **Top Global Matches:** file_cluster_8: 15.296, file_cluster_13: 15.529, file_cluster_11: 15.538
- **Magnitude:** 20134.76 | **LOC:** 24509 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 73
- **Risk Profile:** Cognitive Load (80.5532%), Tech Debt (8.6321%)
**Top Internal Functions/Classes:**
  * `JimGlobMatch` (Impact: 501.4 | O(2^N) | DB: 27)
  * `JimEscape` (Impact: 462.6 | O(N^6) | DB: 73)
  * `JimParseStr` (Impact: 306.1 | O(N^6) | DB: 31)
  * `ListElementQuotingType` (Impact: 300.8 | O(N^5) | DB: 16)
  * `JimParseVar` (Impact: 197.0 | O(N^5) | DB: 38)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4534`, `structural_boundaries: 1846`, `args: 190`, `func_start: 562`, `class_start: 145`
* *Risk/State:* `safety_bypasses: 54`, `high_risk_execution: 7`, `state_mutation: 10767`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 8`
* *Architecture:* `io: 55`, `api: 3457`, `import: 63`
* *Defense:* `safety: 40`, `test: 7`, `immutability_locks: 526`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, stdarg.h, err.h, setjmp.h, dirent.h, stdlib.h, signal.h, in.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/json.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.43 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.316 IQR)
- **Top Global Matches:** file_cluster_8: 14.43, file_cluster_11: 14.662, file_cluster_13: 14.693
- **Magnitude:** 17339.76 | **LOC:** 5635 | **CtrlFlow:** 78.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 400
- **Risk Profile:** Cognitive Load (95.6029%), Tech Debt (10.146%)
**Top Internal Functions/Classes:**
  * `jsonTranslateBlobToText` (Impact: 11485.2 | O(2^N) | DB: 400)
  * `jsonTranslateTextToBlob` (Impact: 1173.0 | O(2^N) | DB: 135)
    * *Intent:* ** U+000b 0b vertical tab ** U+000c 0c form feed ** U+000d 0d carriage return ** U+0020 20 space ** ...
  * `jsonbValidityCheck` (Impact: 417.6 | O(2^N) | DB: 50)
  * `json5Whitespace` (Impact: 272.5 | O(N^3) | DB: 19)
  * `jsonEachColumn` (Impact: 151.8 | O(N^6) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1293`, `structural_boundaries: 354`, `args: 12`, `func_start: 82`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 2627`, `dead_code: 1`, `fragile_debt: 3`, `orphaned_logic: 3`
* *Architecture:* `api: 663`, `import: 1`
* *Defense:* `safety: 64`, `doc: 9`, `test: 63`, `immutability_locks: 97`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sqliteInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/select.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.197 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.866 IQR)
- **Top Global Matches:** file_cluster_8: 15.197, file_cluster_11: 15.438, file_cluster_0: 15.46
- **Magnitude:** 13613.12 | **LOC:** 8983 | **CtrlFlow:** 83.7% | **Authorship Centralization:** 72.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 246
- **Risk Profile:** Cognitive Load (92.466%), Tech Debt (9.5869%)
**Top Internal Functions/Classes:**
  * `sqlite3Select` (Impact: 2414.6 | O(2^N) | DB: 246)
  * `selectExpander` (Impact: 558.4 | O(N^6) | DB: 99)
  * `flattenSubquery` (Impact: 541.3 | O(N^6) | DB: 90)
    * *Intent:* ** ** Also, each component of the sub-query must return the same number ** of result columns. This i...
  * `selectInnerLoop` (Impact: 446.4 | O(N^6) | DB: 71)
  * `multiSelectByMerge` (Impact: 272.1 | O(N^6) | DB: 103)
    * *Intent:* ** ** AltB: Called when there is data from both coroutines and A<B. ** ** AeqB: Called when there is...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2199`, `structural_boundaries: 428`, `args: 4`, `func_start: 104`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 4839`, `dead_code: 1`, `planned_debt: 10`, `fragile_debt: 2`, `orphaned_logic: 6`
* *Architecture:* `io: 16`, `api: 1040`, `import: 1`
* *Defense:* `safety: 353`, `doc: 3`, `test: 352`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sqliteInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/btree.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.671 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.795 IQR)
- **Top Global Matches:** file_cluster_8: 15.671, file_cluster_11: 15.785, file_cluster_0: 15.807
- **Magnitude:** 13061.76 | **LOC:** 11569 | **CtrlFlow:** 77.6% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 484
- **Risk Profile:** Cognitive Load (95.83%), Tech Debt (18.4284%)
**Top Internal Functions/Classes:**
  * `balance` (Impact: 5568.6 | O(2^N) | DB: 304)
  * `setSharedCacheTableLock` (Impact: 2035.3 | O(N^6) | DB: 484)
    * *Intent:* /* If the client is reading or writing an index and the schema is ** not loaded, then it is too diff...
  * `lockBtree` (Impact: 146.7 | O(N^6) | DB: 35)
    * *Intent:* /* EVIDENCE-OF: R-24089-57979 If a page contains no cells (which is only
  * `accessPayload` (Impact: 129.7 | O(N^3) | DB: 41)
  * `autoVacuumCommit` (Impact: 70.9 | O(N^2) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1223`, `structural_boundaries: 354`, `args: 13`, `func_start: 159`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 3699`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 29`
* *Architecture:* `io: 1`, `api: 872`, `import: 1`
* *Defense:* `safety: 424`, `test: 424`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` btreeInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ext/wasm/GNUmakefile` (MAKEFILE | Tier 1 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_17` (Drift: 17.991 IQR)
- **Top Global Matches:** file_cluster_17: 17.991, file_cluster_11: 18.088, file_cluster_0: 18.211
- **Magnitude:** 12435.18 | **LOC:** 1711 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (81.747%), Tech Debt (21.878%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 181`, `args: 101`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 5`, `state_mutation: 135`, `dead_code: 57`, `planned_debt: 6`, `fragile_debt: 3`
* *Architecture:* `io: 44`, `api: 12`, `import: 2`
* *Defense:* `safety: 4`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` config.make, .wasmbuilds.make
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tool/lemon.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.584 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.665 IQR)
- **Top Global Matches:** file_cluster_8: 15.584, file_cluster_11: 15.638, file_cluster_13: 15.667
- **Magnitude:** 11310.5 | **LOC:** 6076 | **CtrlFlow:** 66.3% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 658
- **Risk Profile:** Cognitive Load (91.7266%), Tech Debt (8.7521%)
**Top Internal Functions/Classes:**
  * `translate_code` (Impact: 4837.7 | O(2^N) | DB: 658)
  * `eval_preprocessor_boolean` (Impact: 365.0 | O(2^N) | DB: 38)
    * *Intent:* /* Insert transaction set at index i. */ #if 0
  * `Parse` (Impact: 335.7 | O(N^3) | DB: 105)
  * `FindStates` (Impact: 185.2 | O(N^3) | DB: 31)
  * `acttab_insert` (Impact: 168.8 | O(N^6) | DB: 34)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 939`, `structural_boundaries: 478`, `args: 135`, `func_start: 78`, `class_start: 150`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 3669`, `dead_code: 5`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 21`, `api: 599`, `import: 7`
* *Defense:* `safety: 17`, `doc: 15`, `test: 12`, `immutability_locks: 69`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, stdarg.h, string.h, stdlib.h, unistd.h, stdio.h, assert.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/vdbe.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 16.226 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.916 IQR)
- **Top Global Matches:** file_cluster_8: 16.226, file_cluster_11: 16.31, file_cluster_0: 16.378
- **Magnitude:** 8463.02 | **LOC:** 9319 | **CtrlFlow:** 97.1% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(N^6) | **DB Complexity:** 478
- **Risk Profile:** Cognitive Load (98.4087%), Tech Debt (10.0612%)
**Top Internal Functions/Classes:**
  * `sqlite3VdbeExec` (Impact: 4113.6 | O(N^6) | DB: 478)
  * `vdbeColumnFromOverflow` (Impact: 76.9 | O(N^6) | DB: 24)
  * `sqlite3VdbeMemPrettyPrint` (Impact: 30.9 | O(N^1) | DB: 18)
  * `applyAffinity` (Impact: 29.4 | O(N^3) | DB: 1)
    * *Intent:* ** always taken, the flags should be 0x05 since the fall-through and ** alternate branch are never t...
  * `memTracePrint` (Impact: 18.3 | O(N^1) | DB: 1)
    * *Intent:* /* ** Try to convert a value into a numeric representation if we can ** do so without loss of inform...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1571`, `structural_boundaries: 47`, `args: 3`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 3381`, `planned_debt: 3`, `orphaned_logic: 7`
* *Architecture:* `api: 637`, `import: 3`
* *Defense:* `safety: 577`, `doc: 4`, `test: 577`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` sqliteInt.h, hwtime.h, vdbeInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.559 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.059 IQR)
- **Top Global Matches:** file_cluster_8: 14.559, file_cluster_11: 14.766, file_cluster_13: 14.773
- **Magnitude:** 8078.24 | **LOC:** 5190 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(N^6) | **DB Complexity:** 411
- **Risk Profile:** Cognitive Load (95.0605%), Tech Debt (21.8058%)
**Top Internal Functions/Classes:**
  * `setupLookaside` (Impact: 4594.0 | O(N^6) | DB: 411)
    * *Intent:* /* EVIDENCE-OF: R-39100-27317 The SQLITE_CONFIG_PCACHE_HDRSZ option takes ** a single parameter whic...
  * `openDatabase` (Impact: 649.0 | O(N^6) | DB: 61)
    * *Intent:* #ifdef SQLITE_ENABLE_PREUPDATE_HOOK /*
  * `sqlite3_config` (Impact: 254.8 | O(N^2) | DB: 56)
    * *Intent:* /* Do the rest of the initialization under the recursive mutex so ** that we will be able to handle ...
  * `sqlite3_initialize` (Impact: 51.0 | O(N^2) | DB: 23)
  * `sqlite3_open16` (Impact: 48.5 | O(N^5) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 782`, `structural_boundaries: 360`, `args: 34`, `func_start: 70`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 1729`, `planned_debt: 2`, `orphaned_logic: 20`
* *Architecture:* `io: 4`, `api: 607`, `import: 4`
* *Defense:* `safety: 62`, `doc: 4`, `test: 61`, `immutability_locks: 94`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` sqliteInt.h, sqliteicu.h, fts3.h, rtree.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ext/fts5/fts5_index.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.136 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.339 IQR)
- **Top Global Matches:** file_cluster_8: 15.136, file_cluster_11: 15.341, file_cluster_0: 15.357
- **Magnitude:** 7824.24 | **LOC:** 9546 | **CtrlFlow:** 77.9% | **Authorship Centralization:** 62.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 100
- **Risk Profile:** Cognitive Load (75.5971%), Tech Debt (14.9161%)
**Top Internal Functions/Classes:**
  * `fts5FlushOneHash` (Impact: 198.8 | O(N^5) | DB: 57)
    * *Intent:* /* If this is to be the first rowid written to the page, set the ** rowid-pointer in the page-header...
  * `fts5DoSecureDelete` (Impact: 141.8 | O(N^3) | DB: 100)
  * `fts5DecodeFunction` (Impact: 104.3 | O(N^2) | DB: 68)
  * `fts5StructureDecode` (Impact: 63.1 | O(N^3) | DB: 50)
  * `fts5SegIterNext` (Impact: 61.8 | O(N^3) | DB: 37)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1200`, `structural_boundaries: 341`, `args: 10`, `func_start: 179`, `class_start: 48`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 4125`, `planned_debt: 5`, `orphaned_logic: 22`
* *Architecture:* `api: 1169`, `import: 1`
* *Defense:* `safety: 156`, `test: 162`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fts5Int.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tclsqlite.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.268 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.293 IQR)
- **Top Global Matches:** file_cluster_8: 14.268, file_cluster_13: 14.443, file_cluster_0: 14.536
- **Magnitude:** 7424.78 | **LOC:** 4600 | **CtrlFlow:** 77.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 393
- **Risk Profile:** Cognitive Load (95.7513%), Tech Debt (17.8738%)
**Top Internal Functions/Classes:**
  * `tclSqlFunc` (Impact: 4305.2 | O(2^N) | DB: 393)
  * `DbMain` (Impact: 477.3 | O(N^6) | DB: 41)
  * `DbTraceV2Handler` (Impact: 81.6 | O(N^6) | DB: 11)
  * `TCLSH_MAIN` (Impact: 41.8 | O(N^2) | DB: 8)
  * `tclsh_main_loop` (Impact: 39.2 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 846`, `structural_boundaries: 248`, `args: 20`, `func_start: 60`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 1589`, `planned_debt: 1`, `orphaned_logic: 17`
* *Architecture:* `io: 3`, `api: 648`, `import: 15`
* *Defense:* `safety: 29`, `doc: 2`, `test: 28`, `immutability_locks: 73`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ctype.h, qrf.h, io.h, tcl.h, windows.h, string.h, errno.h, sqlite3.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/vdbeaux.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.09 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.913 IQR)
- **Top Global Matches:** file_cluster_8: 15.09, file_cluster_0: 15.26, file_cluster_11: 15.274
- **Magnitude:** 5627.68 | **LOC:** 5585 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 66
- **Risk Profile:** Cognitive Load (93.8627%), Tech Debt (65.5369%)
**Top Internal Functions/Classes:**
  * `sqlite3VdbeRecordCompareWithSkip` (Impact: 426.6 | O(N^6) | DB: 66)
  * `vdbeRecordCompareDebug` (Impact: 239.1 | O(N^6) | DB: 16)
  * `displayP4Expr` (Impact: 213.3 | O(2^N) | DB: 27)
  * `sqlite3VdbeHalt` (Impact: 184.8 | O(N^5) | DB: 38)
    * *Intent:* #ifdef SQLITE_ENABLE_BYTECODE_VTAB
  * `sqlite3VdbeDisplayP4` (Impact: 177.2 | O(N^6) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 922`, `structural_boundaries: 289`, `args: 16`, `func_start: 149`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 2349`, `planned_debt: 2`, `fragile_debt: 2`, `orphaned_logic: 62`
* *Architecture:* `io: 2`, `api: 671`, `import: 2`
* *Defense:* `safety: 202`, `test: 202`, `immutability_locks: 77`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` sqliteInt.h, vdbeInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/expr.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.271 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.855 IQR)
- **Top Global Matches:** file_cluster_8: 15.271, file_cluster_0: 15.423, file_cluster_11: 15.439
- **Magnitude:** 5616.04 | **LOC:** 7703 | **CtrlFlow:** 75.4% | **Authorship Centralization:** 85.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 199
- **Risk Profile:** Cognitive Load (93.9033%), Tech Debt (32.8653%)
**Top Internal Functions/Classes:**
  * `sqlite3CodeRhsOfIN` (Impact: 870.1 | O(N^6) | DB: 199)
    * *Intent:* /*
  * `exprDup` (Impact: 279.9 | O(2^N) | DB: 35)
    * *Intent:* /* ** Construct a new expression node for a function with multiple ** arguments. */
  * `sqlite3FindInIndex` (Impact: 255.1 | O(N^6) | DB: 61)
  * `sqlite3ExprIsInteger` (Impact: 170.5 | O(2^N) | DB: 10)
  * `sqlite3ExprDataType` (Impact: 87.0 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 939`, `structural_boundaries: 307`, `args: 2`, `func_start: 128`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 2067`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 29`
* *Architecture:* `api: 748`, `import: 1`
* *Defense:* `safety: 275`, `test: 275`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sqliteInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ext/qrf/qrf.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.08 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.944 IQR)
- **Top Global Matches:** file_cluster_8: 15.08, file_cluster_13: 15.336, file_cluster_7: 15.374
- **Magnitude:** 5277.66 | **LOC:** 2984 | **CtrlFlow:** 84.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 124
- **Risk Profile:** Cognitive Load (80.332%), Tech Debt (8.7774%)
**Top Internal Functions/Classes:**
  * `qrfColumnar` (Impact: 823.3 | O(N^6) | DB: 124)
  * `qrfOneSimpleRow` (Impact: 300.2 | O(N^6) | DB: 46)
    * *Intent:* sqlite3_int64 i, j; /* Loop counters */ const char *colSep = 0; /* Column separator text */ const ch...
  * `qrfWrapLine` (Impact: 182.9 | O(N^2) | DB: 37)
    * *Intent:* /* ** The current iCol-th column of p->pStmt is known to be a BLOB. Check ** to see if that BLOB is ...
  * `qrfExplain` (Impact: 179.5 | O(N^6) | DB: 58)
  * `qrfInitialize` (Impact: 132.4 | O(N^2) | DB: 59)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 748`, `structural_boundaries: 134`, `args: 22`, `func_start: 43`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2226`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 402`, `import: 4`
* *Defense:* `safety: 10`, `test: 6`, `immutability_locks: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, qrf.h, stdint.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/insert.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.445 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.899 IQR)
- **Top Global Matches:** file_cluster_8: 14.445, file_cluster_0: 14.708, file_cluster_11: 14.708
- **Magnitude:** 5271.6 | **LOC:** 3394 | **CtrlFlow:** 87.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 157
- **Risk Profile:** Cognitive Load (95.577%), Tech Debt (8.7733%)
**Top Internal Functions/Classes:**
  * `sqlite3Insert` (Impact: 1783.5 | O(2^N) | DB: 125)
  * `sqlite3GenerateConstraintChecks` (Impact: 783.8 | O(N^6) | DB: 157)
  * `xferOptimization` (Impact: 362.4 | O(N^6) | DB: 51)
    * *Intent:* /* Determine if it is possible that triggers (either explicitly coded ** triggers or FK resolution a...
  * `sqlite3MultiValues` (Impact: 89.0 | O(N^6) | DB: 35)
    * *Intent:* /*
  * `sqlite3CompleteInsertion` (Impact: 76.8 | O(N^6) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 666`, `structural_boundaries: 96`, `args: 2`, `func_start: 29`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1522`, `orphaned_logic: 3`
* *Architecture:* `api: 344`, `import: 1`
* *Defense:* `safety: 114`, `test: 114`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sqliteInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ext/fts3/fts3_write.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.761 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.845 IQR)
- **Top Global Matches:** file_cluster_8: 14.761, file_cluster_11: 14.975, file_cluster_0: 14.987
- **Magnitude:** 4724.42 | **LOC:** 5857 | **CtrlFlow:** 82.3% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^5) | **DB Complexity:** 51
- **Risk Profile:** Cognitive Load (76.58%), Tech Debt (15.5153%)
**Top Internal Functions/Classes:**
  * `fts3SqlStmt` (Impact: 140.3 | O(N^3) | DB: 45)
  * `sqlite3Fts3Incrmerge` (Impact: 103.2 | O(N^3) | DB: 51)
    * *Intent:* /* ** iAbsLevel is an absolute level that may be assumed to exist within
  * `fts3IncrmergeLoad` (Impact: 82.0 | O(N^4) | DB: 47)
  * `sqlite3Fts3IntegrityCheck` (Impact: 73.3 | O(N^5) | DB: 36)
  * `sqlite3Fts3UpdateMethod` (Impact: 56.5 | O(N^2) | DB: 24)
    * *Intent:* *pnByte = ((i64)iVal * (i64)iMul);
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 718`, `structural_boundaries: 154`, `args: 12`, `func_start: 75`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 2522`, `planned_debt: 2`, `fragile_debt: 2`, `orphaned_logic: 10`
* *Architecture:* `api: 723`, `import: 5`
* *Defense:* `safety: 62`, `test: 61`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` string.h, stdlib.h, stdio.h, assert.h, fts3Int.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/os_win.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.308 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.367 IQR)
- **Top Global Matches:** file_cluster_8: 14.308, file_cluster_0: 14.574, file_cluster_11: 14.589
- **Magnitude:** 4180.44 | **LOC:** 6500 | **CtrlFlow:** 75.2% | **Authorship Centralization:** 72.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 71
- **Risk Profile:** Cognitive Load (73.3508%), Tech Debt (14.9102%)
**Top Internal Functions/Classes:**
  * `winFileControl` (Impact: 263.2 | O(N^6) | DB: 71)
  * `winWrite` (Impact: 124.2 | O(N^6) | DB: 44)
  * `winClose` (Impact: 121.5 | O(2^N) | DB: 15)
    * *Intent:* /*
  * `winShmMap` (Impact: 114.7 | O(N^6) | DB: 48)
    * *Intent:* #else
  * `winShmLock` (Impact: 110.4 | O(N^3) | DB: 32)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 695`, `structural_boundaries: 229`, `args: 23`, `func_start: 70`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 1924`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 2`, `orphaned_logic: 10`
* *Architecture:* `io: 1`, `api: 440`, `import: 3`
* *Defense:* `safety: 79`, `doc: 5`, `test: 78`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` sqliteInt.h, os_win.h, os_common.h, time.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/os_unix.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.92 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.791 IQR)
- **Top Global Matches:** file_cluster_13: 14.92, file_cluster_8: 14.934, file_cluster_11: 14.958
- **Magnitude:** 4118.04 | **LOC:** 8590 | **CtrlFlow:** 71.0% | **Authorship Centralization:** 88.5%
- **Algorithmic:** O(N^6) | **DB Complexity:** 215
- **Risk Profile:** Cognitive Load (90.365%), Tech Debt (25.6485%)
**Top Internal Functions/Classes:**
  * `afpLock` (Impact: 1258.0 | O(N^6) | DB: 215)
  * `posixUnlock` (Impact: 103.3 | O(N^3) | DB: 46)
    * *Intent:* #endif
  * `unixLock` (Impact: 98.0 | O(N^3) | DB: 43)
  * `afpSetLock` (Impact: 75.4 | O(N^5) | DB: 9)
  * `proxyFileControl` (Impact: 42.8 | O(N^3) | DB: 15)
    * *Intent:* unsigned long long offset; /* offset to first byte to lock */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 668`, `structural_boundaries: 273`, `args: 20`, `func_start: 76`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 74`, `state_mutation: 1602`, `dead_code: 7`, `planned_debt: 1`, `fragile_debt: 2`, `orphaned_logic: 21`
* *Architecture:* `io: 23`, `api: 485`, `import: 21`
* *Defense:* `safety: 115`, `doc: 13`, `test: 104`, `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` param.h, os_common.h, mount.h, time.h, pthread.h, dcmd_blk.h, statvfs.h, unistd.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ext/jni/src/c/sqlite3-jni.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.746 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.393 IQR)
- **Top Global Matches:** file_cluster_8: 13.746, file_cluster_7: 13.929, file_cluster_13: 13.984
- **Magnitude:** 3779.62 | **LOC:** 6353 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (51.4902%), Tech Debt (9.9686%)
**Top Internal Functions/Classes:**
  * `SQLTester_strnotglob` (Impact: 384.9 | O(2^N) | DB: 39)
  * `sqlite3_jni_prepare_v123` (Impact: 335.4 | O(N^6) | DB: 15)
    * *Intent:* #define S3JniHook_unref(hook) S3JniHook__unref(env, (hook)) /* ** Allocates one blank S3JniHook obje...
  * `s3jni__get_nio_buffer` (Impact: 329.5 | O(N^6) | DB: 45)
    * *Intent:* /* ** Cache keys for each concrete NativePointerHolder subclasses and ** OutputPointer.T types. The ...
  * `result_blob_text` (Impact: 262.5 | O(N^6) | DB: 6)
  * `s3jni_trace_impl` (Impact: 143.7 | O(N^6) | DB: 16)
    * *Intent:* //////////////////////////////////////////////////////////////////////// // What follows is the JNI/...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 478`, `structural_boundaries: 285`, `args: 18`, `func_start: 55`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 1298`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 534`, `import: 4`
* *Defense:* `safety: 38`, `doc: 100`, `test: 37`, `immutability_locks: 252`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assert.h, stdint.h, stdio.h, sqlite3-jni.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ext/session/sqlite3session.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.602 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.061 IQR)
- **Top Global Matches:** file_cluster_8: 14.602, file_cluster_13: 14.802, file_cluster_0: 14.813
- **Magnitude:** 3770.76 | **LOC:** 6791 | **CtrlFlow:** 73.4% | **Authorship Centralization:** 87.5%
- **Algorithmic:** O(N^3) | **DB Complexity:** 70
- **Risk Profile:** Cognitive Load (75.0373%), Tech Debt (20.9079%)
**Top Internal Functions/Classes:**
  * `sessionUpdateMaxSize` (Impact: 166.1 | O(N^3) | DB: 36)
  * `sessionPreupdateOneChange` (Impact: 155.6 | O(N^2) | DB: 50)
  * `sessionTableInfo` (Impact: 118.7 | O(N^2) | DB: 70)
    * *Intent:* /* It should not be possible for eType to be SQLITE_NULL or 0x00 here, ** as the session module does...
  * `sessionSerializeValue` (Impact: 76.9 | O(N^3) | DB: 14)
    * *Intent:* ** there is no separation of header and data. Each field begins with a ** single byte describing its...
  * `sqlite3session_diff` (Impact: 72.1 | O(N^3) | DB: 37)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 500`, `structural_boundaries: 181`, `args: 29`, `func_start: 70`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 1880`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 13`
* *Architecture:* `io: 1`, `api: 588`, `import: 5`
* *Defense:* `safety: 35`, `test: 33`, `immutability_locks: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` string.h, vdbeInt.h, sqliteInt.h, assert.h, sqlite3session.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tool/sqldiff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.157 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.198 IQR)
- **Top Global Matches:** file_cluster_8: 14.157, file_cluster_13: 14.384, file_cluster_11: 14.466
- **Magnitude:** 3569.36 | **LOC:** 2056 | **CtrlFlow:** 88.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 92
- **Risk Profile:** Cognitive Load (77.1111%), Tech Debt (8.533%)
**Top Internal Functions/Classes:**
  * `changeset_one_table` (Impact: 342.6 | O(N^6) | DB: 77)
  * `diff_one_table` (Impact: 293.8 | O(N^4) | DB: 92)
  * `columnNames` (Impact: 193.6 | O(N^3) | DB: 53)
  * `main` (Impact: 163.5 | O(N^2) | DB: 60)
  * `rbuDeltaCreate` (Impact: 95.6 | O(N^2) | DB: 66)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 56`, `args: 31`, `func_start: 32`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1615`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 234`, `import: 8`
* *Defense:* `safety: 8`, `doc: 1`, `test: 4`, `immutability_locks: 48`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ctype.h, sqlite3_stdio.h, stdarg.h, string.h, sqlite3.h, stdlib.h, stdio.h, assert.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ext/wasm/api/sqlite3-api-oo1.c-pp.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.097 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.683 IQR)
- **Top Global Matches:** file_cluster_11: 14.097, file_cluster_8: 14.138, file_cluster_15: 14.209
- **Magnitude:** 3534.26 | **LOC:** 2430 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 175
- **Risk Profile:** Cognitive Load (49.1642%), Tech Debt (12.9838%)
**Top Internal Functions/Classes:**
  * `ctor` (Impact: 3153.8 | O(2^N) | DB: 175)
  * `dbCtorApplySEEKey` (Impact: 71.3 | O(N^3) | DB: 3)
    * *Intent:* */
  * `checkSqlite3Rc` (Impact: 11.0 | O(N^2))
  * `byteArrayToHex` (Impact: 4.8 | O(N^1) | DB: 1)
  * `getOwnOption` (Impact: 4.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 120`, `args: 68`, `func_start: 99`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 271`, `planned_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 26`
* *Defense:* `safety: 95`, `doc: 48`, `immutability_locks: 69`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ext/fts5/fts5_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.499 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.286 IQR)
- **Top Global Matches:** file_cluster_8: 14.499, file_cluster_0: 14.71, file_cluster_13: 14.743
- **Magnitude:** 3497.94 | **LOC:** 3876 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 72
- **Risk Profile:** Cognitive Load (72.2799%), Tech Debt (9.1601%)
**Top Internal Functions/Classes:**
  * `fts5FilterMethod` (Impact: 143.5 | O(N^3) | DB: 72)
    * *Intent:* /*
  * `fts5UpdateMethod` (Impact: 101.8 | O(N^3) | DB: 40)
  * `fts5CacheInstArray` (Impact: 63.1 | O(N^3) | DB: 27)
  * `fts5ApiColumnSize` (Impact: 47.5 | O(N^4) | DB: 24)
    * *Intent:* /* ** Return true if the value passed as the only argument is an ** fts5_locale() value. */
  * `fts5ColumnMethod` (Impact: 47.1 | O(N^3) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 482`, `structural_boundaries: 181`, `args: 6`, `func_start: 78`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 1872`, `orphaned_logic: 4`
* *Architecture:* `api: 611`, `import: 1`
* *Defense:* `safety: 59`, `test: 58`, `immutability_locks: 84`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fts5Int.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/update.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.016 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.697 IQR)
- **Top Global Matches:** file_cluster_8: 14.016, file_cluster_0: 14.318, file_cluster_13: 14.325
- **Magnitude:** 3450.44 | **LOC:** 1363 | **CtrlFlow:** 95.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 185
- **Risk Profile:** Cognitive Load (96.4267%), Tech Debt (8.7871%)
**Top Internal Functions/Classes:**
  * `sqlite3Update` (Impact: 2423.1 | O(2^N) | DB: 185)
    * *Intent:* ** ** Or, if pLimit and pOrderBy are not NULL, and pTab is not a view: ** ** SELECT <other-columns>,...
  * `updateVirtualTable` (Impact: 56.0 | O(N^2) | DB: 39)
    * *Intent:* /* Populate the array of registers beginning at regNew with the new ** row data. This array is used ...
  * `updateFromSelect` (Impact: 34.4 | O(N^2) | DB: 33)
  * `sqlite3ColumnDefault` (Impact: 18.7 | O(N^6) | DB: 3)
    * *Intent:* ** a legal notice, here is a blessing: ** ** May you do good and not evil. ** May you find forgivene...
  * `indexColumnIsBeingUpdated` (Impact: 7.8 | O(N^6) | DB: 1)
    * *Intent:* /* ** The most recently coded instruction was an OP_Column to retrieve the ** i-th column of table p...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 297`, `structural_boundaries: 13`, `args: 1`, `func_start: 7`
* *Risk/State:* `state_mutation: 727`, `orphaned_logic: 1`
* *Architecture:* `api: 155`, `import: 1`
* *Defense:* `safety: 36`, `test: 36`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sqliteInt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tool/fuzzershell.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.861 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.133 IQR)
- **Top Global Matches:** file_cluster_8: 13.861, file_cluster_13: 13.995, file_cluster_7: 14.107
- **Magnitude:** 3272.46 | **LOC:** 1268 | **CtrlFlow:** 77.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 207
- **Risk Profile:** Cognitive Load (89.8106%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 2023.1 | O(2^N) | DB: 207)
    * *Intent:* int i; /* Loop over constraints */ int idxNum = 0; /* The query plan bitmask */ int startIdx = -1; /...
  * `seriesBestIndex` (Impact: 33.0 | O(N^2) | DB: 31)
  * `integerValue` (Impact: 30.1 | O(N^1) | DB: 15)
  * `callback` (Impact: 24.8 | O(N^2) | DB: 10)
  * `execCallback` (Impact: 17.6 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 274`, `structural_boundaries: 80`, `args: 17`, `func_start: 33`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 819`
* *Architecture:* `io: 13`, `api: 166`, `import: 6`
* *Defense:* `safety: 3`, `doc: 6`, `immutability_locks: 27`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, stdarg.h, string.h, sqlite3.h, stdlib.h, stdio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tool/sqlite3_rsync.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.836 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.685 IQR)
- **Top Global Matches:** file_cluster_8: 13.836, file_cluster_13: 14.046, file_cluster_7: 14.124
- **Magnitude:** 3219.52 | **LOC:** 2425 | **CtrlFlow:** 81.6% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 104
- **Risk Profile:** Cognitive Load (89.5953%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 763.3 | O(N^6) | DB: 104)
  * `originSide` (Impact: 281.6 | O(N^6) | DB: 53)
  * `popen2` (Impact: 262.0 | O(2^N) | DB: 68)
  * `replicaSide` (Impact: 258.9 | O(N^6) | DB: 43)
  * `runSql` (Impact: 25.2 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 451`, `structural_boundaries: 102`, `args: 9`, `func_start: 43`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 4`, `state_mutation: 1045`
* *Architecture:* `io: 41`, `api: 259`, `import: 12`
* *Defense:* `doc: 9`, `immutability_locks: 43`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, io.h, stdarg.h, windows.h, string.h, wait.h, sqlite3.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/btmutex.c` (C) | Magnitude: 186.94 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: pointers: 155, indent_spaces: 113, state_mutation: 85, branch: 55
- `ext/jni/src/org/sqlite/jni/fts5/fts5_api.java` (JAVA) | Magnitude: 21.4 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 6, args: 5, safety: 5
- `ext/wasm/speedtest1.html` (HTML) | Magnitude: 169.12 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 168, state_mutation: 41, structural_boundaries: 27, branch: 26
- `ext/jni/src/org/sqlite/jni/fts5/fts5_tokenizer.java` (JAVA) | Magnitude: 3.98 | Delta: **0.272 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, safety: 3, dead_code: 3
- `ext/jni/src/org/sqlite/jni/fts5/Fts5ExtensionApi.java` (JAVA) | Magnitude: 24.8 | Delta: **0.462 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, safety: 39, args: 22, func_start: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `ext/misc/totype.c` (C) | Magnitude: 1176.48 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 284, indent_spaces: 255, branch: 133, api: 66
- `ext/wasm/split-speedtest1-script.sh` (SHELL) | Magnitude: 29.98 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 12, safety_bypasses: 8, branch: 5, indent_spaces: 5
- `ext/wasm/api/sqlite3-api-oo1.c-pp.js` (JAVASCRIPT) | Magnitude: 3534.26 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 751, branch: 285, state_mutation: 271, structural_boundaries: 120
- `src/legacy.c` (C) | Magnitude: 345.62 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 102, indent_spaces: 91, branch: 35, api: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `ext/fts3/tool/fts3cov.sh` (SHELL) | Magnitude: 11.92 | Delta: **0.187 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 6, safety_bypasses: 5, reflection_metaprogramming: 4, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `ext/misc/memtrace.c` (C) | Magnitude: 77.7 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 50, state_mutation: 22, structural_boundaries: 20, pointers: 14
- `tool/GetFile.cs` (CSHARP) | Magnitude: 292.58 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 380, indent_spaces: 183, branch: 29, func_start: 27
- `src/os_unix.c` (C) | Magnitude: 4118.04 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1947, state_mutation: 1602, pointers: 794, branch: 668
- `ext/misc/uuid.c` (C) | Magnitude: 218.14 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 90, api: 39, branch: 26
- `tool/version-info.c` (C) | Magnitude: 178.4 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 87, indent_spaces: 82, branch: 27, debug_prints: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `ext/jni/src/org/sqlite/jni/capi/NativePointerHolder.java` (JAVA) | Magnitude: 9.7 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 4, api: 4, immutability_locks: 3
- `ext/jni/src/org/sqlite/jni/capi/ValueHolder.java` (JAVA) | Magnitude: 7.92 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 4, indent_spaces: 3, structural_boundaries: 2, args: 2
- `ext/jni/src/org/sqlite/jni/wrapper1/ValueHolder.java` (JAVA) | Magnitude: 7.92 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 4, indent_spaces: 3, structural_boundaries: 2, args: 2
- `ext/jni/src/org/sqlite/jni/fts5/Fts5Tokenizer.java` (JAVA) | Magnitude: 2.9 | Delta: **0.134 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, args: 1, func_start: 1, class_start: 1
- `ext/jni/src/org/sqlite/jni/fts5/Fts5PhraseIter.java` (JAVA) | Magnitude: 14.12 | Delta: **0.183 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, encapsulation: 2, indent_spaces: 2, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tool/fragck.tcl` (TCL) | Magnitude: 50.78 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 60, state_mutation: 45, branch: 16, debug_prints: 9
- `autosetup/teaish/tester.tcl` (TCL) | Magnitude: 83.64 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 109, state_mutation: 76, branch: 30, structural_boundaries: 24
- `ext/wasm/SQLTester/GNUmakefile` (MAKEFILE) | Magnitude: 26.5 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 11, debug_prints: 8, state_mutation: 7
- `contrib/sqlitecon.tcl` (TCL) | Magnitude: 5.09 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 440, state_mutation: 382, branch: 94, structural_boundaries: 52
- `ext/wasm/GNUmakefile` (MAKEFILE) | Magnitude: 12435.18 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 194, structural_boundaries: 181, state_mutation: 135, branch: 117

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `ext/rtree/viewrtree.tcl` (TCL) | Magnitude: 163.54 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 151, indent_spaces: 104, branch: 25, scientific: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/threads.c` (C) | Magnitude: 184.62 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 131, state_mutation: 108, pointers: 79, structural_boundaries: 45
- `ext/session/session_common.tcl` (TCL) | Magnitude: 449.26 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 252, indent_spaces: 218, branch: 40, structural_boundaries: 25
- `ext/wasm/tests/opfs/concurrency/worker.js` (JAVASCRIPT) | Magnitude: 170.92 | Delta: **0.135 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 102, concurrency: 36, branch: 34, func_start: 24
- `ext/wasm/tester1-worker.c-pp.html` (HTML) | Magnitude: 85.92 | Delta: **0.223 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 90, io: 22, branch: 20, state_mutation: 16
- `ext/wasm/api/pre-js.c-pp.js` (JAVASCRIPT) | Magnitude: 275.77 | Delta: **0.242 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, state_mutation: 28, structural_boundaries: 10, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `ext/jni/src/org/sqlite/jni/capi/SQLFunction.java` (JAVA) | Magnitude: 12.56 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, planned_debt: 2, class_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `ext/wasm/speedtest1-worker.html` (HTML) | Magnitude: 245.94 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 361, branch: 56, structural_boundaries: 47, state_mutation: 39
- `ext/jni/src/org/sqlite/jni/capi/OutputPointer.java` (JAVA) | Magnitude: 126.58 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 86, api: 57, doc: 57, structural_boundaries: 36
- `ext/misc/randomjson.c` (C) | Magnitude: 265.94 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 158, state_mutation: 134, pointers: 30, api: 29
- `ext/jni/src/org/sqlite/jni/annotation/NotNull.java` (JAVA) | Magnitude: 14.12 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 3, decorators: 3, api: 1, doc: 1
- `ext/jni/src/org/sqlite/jni/annotation/Nullable.java` (JAVA) | Magnitude: 14.12 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 3, decorators: 3, api: 1, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/sqlite.h.in` (C) | Magnitude: 152.98 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: macros: 355, api: 115, structural_boundaries: 112, pointers: 111
- `ext/wasm/config.make.in` (MAKEFILE) | Magnitude: 12.6 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 5, dead_code: 4, sec_dead_code: 1
- `Makefile.in` (MAKEFILE) | Magnitude: 35.16 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 71, dead_code: 27, indent_tabs: 20, func_start: 11
- `ext/expert/sqlite3expert.h` (C) | Magnitude: 26.42 | Delta: **0.232 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 11, macros: 8, pointers: 7, structural_boundaries: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/shell.c.in` -> Churn: **100.0%** | Cog Load: 87.2419% | Debt: 11.2171%
- `ext/qrf/qrf.c` -> Churn: **86.48%** | Cog Load: 80.332% | Debt: 8.7774%
- `ext/wasm/GNUmakefile` -> Churn: **82.88%** | Cog Load: 81.747% | Debt: 21.878%
- `ext/wasm/api/sqlite3-vfs-kvvfs.c-pp.js` -> Churn: **81.85%** | Cog Load: 34.289% | Debt: 89.712%
- `ext/wasm/mkwasmbuilds.c` -> Churn: **74.43%** | Cog Load: 57.6381% | Debt: 18.594%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/json.c` -> **drh** (100.0% isolated ownership) | Magnitude: 17339.76
- `ext/wasm/GNUmakefile` -> **stephan** (100.0% isolated ownership) | Magnitude: 12435.18
- `src/tclsqlite.c` -> **drh** (100.0% isolated ownership) | Magnitude: 7424.78
- `src/vdbeaux.c` -> **drh** (100.0% isolated ownership) | Magnitude: 5627.68
- `src/expr.c` -> **drh** (85.7% isolated ownership) | Magnitude: 5616.04

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/btreeInt.h` -> **Severity: 0.005** (Bridge: 0.0002 * Flux: 21.9913%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/sqliteInt.h` -> **Severity: 1.127** (Embedded: 0.201 * Error Risk: 5.6046%)
- `src/sqlite3ext.h` -> **Severity: 0.638** (Embedded: 0.1231 * Error Risk: 5.1796%)
- `src/vdbe.h` -> **Severity: 0.558** (Embedded: 0.1037 * Error Risk: 5.3848%)
- `ext/jni/src/org/sqlite/jni/capi/sqlite3_context.java` -> **Severity: 0.354** (Embedded: 0.0038 * Error Risk: 94.4055%)
- `ext/jni/src/org/sqlite/jni/capi/sqlite3.java` -> **Severity: 0.3** (Embedded: 0.0038 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/sqliteInt.h` -> **Severity: 8817.4** (Blast Radius: 88.174 * Doc Risk: 100.0%)
- `src/sqlite3ext.h` -> **Severity: 5044.331** (Blast Radius: 68.951 * Doc Risk: 73.1582%)
- `ext/fts3/fts3Int.h` -> **Severity: 1262.4** (Blast Radius: 12.624 * Doc Risk: 100.0%)
- `ext/fts5/fts5Int.h` -> **Severity: 1158.8** (Blast Radius: 11.588 * Doc Risk: 100.0%)
- `src/btree.h` -> **Severity: 871.5** (Blast Radius: 8.715 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
