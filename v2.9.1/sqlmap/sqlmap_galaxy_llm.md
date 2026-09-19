# ARCHITECTURAL_BRIEF: sqlmap
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/sqlmapproject/sqlmap.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 422 analyzed artifact(s), 18702 LOC.
- **Load-bearing artifact:** `plugins/generic/connector.py` -- 31 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `lib/utils/api.py` -- pulls in 32 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `plugins/generic/databases.py` at magnitude 1957.12 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 422 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 231 |
| Total LOC | 18702 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 64.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5061 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.7847 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1529 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 331 | 17699 | 78.4% |
| MARKDOWN | 29 | 0 | 6.9% |
| PLAINTEXT | 15 | 0 | 3.6% |
| XML | 15 | 0 | 3.6% |
| SHELL | 12 | 244 | 2.8% |
| SQLITE | 11 | 44 | 2.6% |
| CPP | 3 | 27 | 0.7% |
| DB2_SQL | 2 | 7 | 0.5% |
| C | 2 | 353 | 0.5% |
| PERL | 1 | 31 | 0.2% |
| YAML | 1 | 297 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `1.963`
> **Composition Archetype:** `Small Flat Repo (2)` (z +1.96; from the repo's file-archetype mix)
> **File Composition:** Parameter Forwarders Files 32%, Data / Markup / Trivial 28%, Compute Cores Files 25%, Large Core Modules (2) 7%, Large Core Modules (3) 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 378 | 89.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 44 | 10.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 231*

**Composition by Extension & Reason:**
- `.py`: 156x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 29 exceeds 500 chars)
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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.2 | 21.4 | 7.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 64.9 | 69.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 27.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 9.4 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 98.0 | 21.4 | 8.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 62.0 | 91.7 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.4 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 27.1 | 3.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 64.2 | 80.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 227 | 44 | 1 | `extra/icmpsh/icmpsh-s.c` |
| cleanup | 49 | 27 | 0 | `lib/utils/hashdb.py` |
| guards | 638 | 72 | 6 | `lib/utils/tui.py` |
| danger | 928 | 197 | 5 | `sqlmap.py` |
| concurrency | 35 | 8 | 0 | `lib/utils/hash.py` |
| connectivity | 1279 | 319 | 5 | `lib/utils/api.py` |
| io | 379 | 70 | 1 | `extra/shutils/pypi.sh` |
| crypto | 7 | 2 | 0 | `lib/utils/hash.py` |
| ipc | 28 | 9 | 0 | `lib/utils/hash.py` |
| time | 15 | 6 | 0 | `lib/utils/hashdb.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 152 | 65 | 1 | `lib/utils/sgmllib.py` |
| events | 809 | 112 | 5 | `lib/utils/api.py` |
| tests | 4 | 2 | 0 | `sqlmap.py` |
| docs | 632 | 329 | 2 | `sqlmapapi.yaml` |
| debt | 86 | 22 | 0 | `lib/utils/sgmllib.py` |
| mutation | 8815 | 317 | 43 | `plugins/generic/databases.py` |
| dead_code | 233 | 143 | 2 | `lib/utils/har.py` |
| credential | 6 | 5 | 0 | `lib/utils/hash.py` |
| threat | 111 | 51 | 1 | `lib/utils/deps.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `extra/shutils/pypi.sh` (Hits: 59)
- `sqlmap.py` (Hits: 37)
- `lib/utils/api.py` (Hits: 30)

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

- `getColumns` **(Many-Argument Workhorses)** (@ `plugins/generic/databases.py`) -> Impact: **563.1** | LOC: 484
- `dumpTable` **(Many-Argument Workhorses)** (@ `plugins/generic/entries.py`) -> Impact: **313.6** | LOC: 418
- `getPrivileges` **(Many-Argument Workhorses)** (@ `plugins/generic/users.py`) -> Impact: **245.0** | LOC: 292
- `getTables` **(Many-Argument Workhorses)** (@ `plugins/generic/databases.py`) -> Impact: **234.7** | LOC: 259
- `main` **(I/O & Config Routines)** (@ `sqlmap.py`) -> Impact: **180.9** | LOC: 478
  * *Intent:* """ Main function of sqlmap when running from command line. """
- `dictionaryAttack` **(Many-Argument Workhorses)** (@ `lib/utils/hash.py`) -> Impact: **160.7** | LOC: 329
- `searchColumn` **(Compute Cores)** (@ `plugins/generic/search.py`) -> Impact: **158.0** | LOC: 276
- `crawl` **(Many-Argument Workhorses)** (@ `lib/utils/crawler.py`) -> Impact: **155.8** | LOC: 195
- `pivotDumpTable` **(Many-Argument Workhorses)** (@ `lib/utils/pivotdumptable.py`) -> Impact: **149.6** | LOC: 150
- `getColumns` **(Many-Argument Workhorses)** (@ `plugins/dbms/sybase/enumeration.py`) -> Impact: **148.6** | LOC: 131

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib/utils` | 21 | 6794.06 | 62.87% | 28.64% |
| `plugins/generic` | 13 | 6415.4 | 61.4% | 0.75% |
| `tamper` | 70 | 2080.24 | 21.8% | 79.03% |
| `plugins/dbms/mssqlserver` | 7 | 1192.56 | 38.39% | 23.68% |
| `plugins/dbms/sybase` | 7 | 671.56 | 26.79% | 22.09% |
| `__monolith__` | 4 | 593.52 | 36.96% | 8.72% |
| `plugins/dbms/mysql` | 7 | 592.96 | 31.71% | 24.36% |
| `plugins/dbms/maxdb` | 7 | 536.82 | 23.37% | 17.78% |
| `plugins/dbms/oracle` | 7 | 499.54 | 37.53% | 22.09% |
| `extra/icmpsh` | 6 | 490.56 | 32.8% | 7.1% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lib/utils/xrange.py` -> **99.9889%** Exposure
- `lib/utils/timeout.py` -> **98.9013%** Exposure
- `plugins/dbms/sqlite/connector.py` -> **97.1653%** Exposure
- `lib/utils/progress.py` -> **96.8696%** Exposure
- `lib/utils/sgmllib.py` -> **96.5757%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `extra/cloak/cloak.py` -> **100.0%** Exposure
- `extra/dbgtool/dbgtool.py` -> **100.0%** Exposure
- `extra/icmpsh/icmpsh_m.py` -> **100.0%** Exposure
- `extra/vulnserver/vulnserver.py` -> **100.0%** Exposure
- `lib/utils/api.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lib/utils/har.py` -> **6** Orphaned Functions | **0** Duplicates
- `lib/utils/xrange.py` -> **6** Orphaned Functions | **0** Duplicates
- `extra/vulnserver/vulnserver.py` -> **5** Orphaned Functions | **0** Duplicates
- `lib/utils/sgmllib.py` -> **5** Orphaned Functions | **0** Duplicates
- `lib/utils/hashdb.py` -> **4** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### 📡 API Network Audit (Set Theory)
- **Shadow APIs (Critical):** `0` undocumented endpoints actively listening.
- **Ghost APIs (Bloat):** `12` endpoints documented but missing from code.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `15` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1677` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `plugins/generic/databases.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 1957.12 | **LOC:** 1125 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 8.753; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.8%), Complexity Load (formerly Cognitive Load) (87.2%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.753
  * `Choke Point (Betweenness):` 0.000161 | `Ripple Effect (Closeness):` 0.058533
  * `Imports (Out-Degree: 1):` lib.core.agent, lib.core.common, lib.core.data, lib.core.decorators, lib.core.dicts, lib.core.enums, lib.core.exception, lib.core.settings...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/utils/hash.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1600.0 | **LOC:** 1331 | **CtrlFlow:** 39.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **29**; blast radius 8.92; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Concurrency Surface (formerly Concurrency) (86.6%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.92
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.044054
  * `Imports (Out-Degree: 0):` Crypto.Cipher.DES, __future__, base64, binascii, crypt, gc, hashlib, lib.core.common...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `plugins/generic/users.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 981.78 | **LOC:** 676 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 8.753; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Complexity Load (formerly Cognitive Load) (84.5%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.753
  * `Choke Point (Betweenness):` 0.000495 | `Ripple Effect (Closeness):` 0.058533
  * `Imports (Out-Degree: 2):` lib.core.agent, lib.core.common, lib.core.compat, lib.core.convert, lib.core.data, lib.core.dicts, lib.core.enums, lib.core.exception...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/generic/search.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 959.56 | **LOC:** 641 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 8.753; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (100.0%), Complexity Load (formerly Cognitive Load) (84.0%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.753
  * `Choke Point (Betweenness):` 0.000161 | `Ripple Effect (Closeness):` 0.058533
  * `Imports (Out-Degree: 1):` lib.core.agent, lib.core.common, lib.core.data, lib.core.enums, lib.core.exception, lib.core.settings, lib.request, lib.utils.brute...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/generic/entries.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 936.82 | **LOC:** 647 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 8.753; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Complexity Load (formerly Cognitive Load) (81.7%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.753
  * `Choke Point (Betweenness):` 0.000495 | `Ripple Effect (Closeness):` 0.058533
  * `Imports (Out-Degree: 2):` lib.core.agent, lib.core.bigarray, lib.core.common, lib.core.convert, lib.core.data, lib.core.dicts, lib.core.enums, lib.core.exception...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/utils/api.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 864.72 | **LOC:** 919 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **32**; blast radius 2.443; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.9%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.443
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004751
  * `Imports (Out-Degree: 0):` __future__, contextlib, eventlet, gevent, lib.core.common, lib.core.compat, lib.core.convert, lib.core.data...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/utils/sgmllib.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 715.32 | **LOC:** 575 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.483; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.1%), Debt Markers (formerly Tech Debt) (96.6%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, _markupbase, markupbase, re, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils/tui.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 656.52 | **LOC:** 769 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 1.483; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (56.8%)
- **Documentation Coverage:** 15.0% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 47`, `high_risk_execution: 1`, `state_mutation: 132`, `unreferenced_by_name: 2`
* *Architecture:* `io: 6`, `api: 4`, `import: 15`
* *Defense:* `safety: 37`, `doc: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` curses, fcntl, lib.core.common, lib.core.data, lib.core.defaults, lib.core.enums, lib.core.exception, lib.core.settings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugins/dbms/mssqlserver/enumeration.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 647.3 | **LOC:** 447 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 1.694; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Complexity Load (formerly Cognitive Load) (82.4%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.694
  * `Choke Point (Betweenness):` 5.7e-05 | `Ripple Effect (Closeness):` 0.002375
  * `Imports (Out-Degree: 1):` lib.core.agent, lib.core.common, lib.core.compat, lib.core.data, lib.core.enums, lib.core.exception, lib.core.settings, lib.request...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/generic/takeover.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 525.74 | **LOC:** 482 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **10**; blast radius 44.67; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `osPwn` **(Compute Cores)** (Impact: 93.8)
  * `osShell` **(Defensive Guards)** (Impact: 24.4)
  * `osSmb` **(Compute Cores)** (Impact: 20.8)
  * `regAdd` **(Compute Cores)** (Impact: 20.7)
  * `osCmd` **(Compute Cores)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 93 instances
* *State Mutation (weighted view):* 285
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 80`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 99`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 11`, `import: 26`
* *Defense:* `safety: 6`, `doc: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 44.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.095012
  * `Imports (Out-Degree: 0):` impacket, lib.core.common, lib.core.data, lib.core.enums, lib.core.exception, lib.takeover.abstraction, lib.takeover.icmpsh, lib.takeover.metasploit...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `lib/utils/brute.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 516.28 | **LOC:** 409 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **10**; blast radius 17.317; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tableExists` **(Many-Argument Workhorses)** (Impact: 82.4)
  * `columnExists` **(Many-Argument Workhorses)** (Impact: 77.7)
  * `fileExists` **(Defensive Guards)** (Impact: 19.8)
  * `tableExistsThread` **(I/O & Config Routines)** (Impact: 17.0)
  * `columnExistsThread` **(I/O & Config Routines)** (Impact: 11.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 95`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 107`
* *Architecture:* `api: 6`, `import: 37`
* *Defense:* `safety: 12`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.317
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.045765
  * `Imports (Out-Degree: 0):` __future__, lib.core.common, lib.core.data, lib.core.decorators, lib.core.enums, lib.core.exception, lib.core.settings, lib.core.threads...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `sqlmap.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 507.86 | **LOC:** 638 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **32**; blast radius 1.904; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.0%), Concurrency Surface (formerly Concurrency) (87.0%), Complexity Load (formerly Cognitive Load) (85.8%)
- **Documentation Coverage:** 18.1818% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 180.9)
    * *Intent:* """ Main function of sqlmap when running from command line. """
  * `checkEnvironment` **(Defensive Guards)** (Impact: 7.2)
  * `modulePath` **(Defensive Guards)** (Impact: 4.6)
    * *Intent:* """ This will get us the program's directory, even if we are frozen using py2exe """
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 89 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 276
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 143`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 4`, `state_mutation: 98`
* *Architecture:* `io: 37`, `api: 3`, `concurrency: 6`, `import: 67`
* *Defense:* `safety: 34`, `doc: 3`, `test: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.904
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.002375
  * `Imports (Out-Degree: 3):` __future__, bdb, glob, inspect, json, lib.controller.controller, lib.core.common, lib.core.compat...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/dbms/sybase/enumeration.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 488.88 | **LOC:** 327 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 1.694; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Complexity Load (formerly Cognitive Load) (93.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getColumns` **(Many-Argument Workhorses)** (Impact: 148.6)
  * `getTables` **(Compute Cores)** (Impact: 49.1)
  * `getPrivileges` **(Many-Argument Workhorses)** (Impact: 17.5)
  * `getDbs` **(Compute Cores)** (Impact: 14.0)
  * `getUsers` **(Compute Cores)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 71 instances
* *State Mutation (weighted view):* 222
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 85`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 80`
* *Architecture:* `api: 12`, `import: 25`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.694
  * `Choke Point (Betweenness):` 5.7e-05 | `Ripple Effect (Closeness):` 0.002375
  * `Imports (Out-Degree: 3):` lib.core.common, lib.core.data, lib.core.dicts, lib.core.enums, lib.core.exception, lib.core.settings, lib.utils.brute, lib.utils.pivotdumptable...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/generic/filesystem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 397.48 | **LOC:** 328 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **12**; blast radius 44.67; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (71.3%)
- **Documentation Coverage:** 84.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readFile` **(Many-Argument Workhorses)** (Impact: 41.7)
  * `_checkFileLength` **(Many-Argument Workhorses)** (Impact: 38.4)
  * `fileContentEncode` **(Many-Argument Workhorses)** (Impact: 31.0)
  * `writeFile` **(Many-Argument Workhorses)** (Impact: 24.0)
  * `askCheckWrittenFile` **(Many-Argument Workhorses)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 207
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 94`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 75`
* *Architecture:* `io: 3`, `api: 13`, `import: 31`
* *Defense:* `safety: 4`, `doc: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 44.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.095012
  * `Imports (Out-Degree: 0):` codecs, lib.core.agent, lib.core.common, lib.core.compat, lib.core.convert, lib.core.data, lib.core.enums, lib.core.exception...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `plugins/dbms/maxdb/enumeration.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 367.38 | **LOC:** 246 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 1.694; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Complexity Load (formerly Cognitive Load) (92.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getColumns` **(Many-Argument Workhorses)** (Impact: 133.5)
  * `getTables` **(Compute Cores)** (Impact: 43.5)
  * `getDbs` **(Compute Cores)** (Impact: 6.6)
  * `__init__` **(Callbacks & Closures)** (Impact: 4.4)
  * `getPrivileges` **(Parameter Forwarders)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 69`, `args: 10`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 59`
* *Architecture:* `api: 10`, `import: 22`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.694
  * `Choke Point (Betweenness):` 5.7e-05 | `Ripple Effect (Closeness):` 0.002375
  * `Imports (Out-Degree: 3):` lib.core.common, lib.core.data, lib.core.enums, lib.core.exception, lib.core.settings, lib.utils.brute, lib.utils.pivotdumptable, plugins.generic.enumeration...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/utils/gui.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 367.14 | **LOC:** 427 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 1.483; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runGui` **(Compute Cores)** (Impact: 73.2)
  * `populate_tab` **(Compute Cores)** (Impact: 24.0)
    * *Intent:* # Function to populate a tab in the background
  * `run` **(I/O & Config Routines)** (Impact: 19.2)
  * `onKeyPress` **(Compute Cores)** (Impact: 6.1)
  * `check` **(Type Conversions)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 53 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 202
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 83`, `args: 17`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 96`, `unreferenced_by_name: 2`
* *Architecture:* `io: 9`, `api: 10`, `concurrency: 2`, `import: 27`
* *Defense:* `safety: 10`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib.core.common, lib.core.data, lib.core.defaults, lib.core.enums, lib.core.exception, lib.core.settings, os, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils/crawler.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 361.6 | **LOC:** 266 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 2.023; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.5%), Complexity Load (formerly Cognitive Load) (82.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `crawl` **(Many-Argument Workhorses)** (Impact: 155.8)
  * `crawlThread` **(Defensive Guards)** (Impact: 35.2)
  * `storeResultsToFile` **(Compute Cores)** (Impact: 18.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 91`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 51`, `dead_code: 3`
* *Architecture:* `io: 2`, `api: 3`, `import: 33`
* *Defense:* `safety: 17`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003167
  * `Imports (Out-Degree: 0):` __future__, lib.core.common, lib.core.compat, lib.core.convert, lib.core.data, lib.core.datatype, lib.core.enums, lib.core.exception...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/utils/pivotdumptable.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 303.48 | **LOC:** 189 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **15**; blast radius 9.88; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Complexity Load (formerly Cognitive Load) (81.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pivotDumpTable` **(Many-Argument Workhorses)** (Impact: 149.6)
  * `def` **(Compute Cores)** (Impact: 16.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 76`, `args: 3`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 48`
* *Architecture:* `api: 1`, `import: 29`
* *Defense:* `safety: 6`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.88
  * `Choke Point (Betweenness):` 0.000356 | `Ripple Effect (Closeness):` 0.045765
  * `Imports (Out-Degree: 1):` lib.core.agent, lib.core.bigarray, lib.core.common, lib.core.compat, lib.core.convert, lib.core.data, lib.core.dicts, lib.core.enums...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `extra/icmpsh/icmpsh-s.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 287.74 | **LOC:** 345 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.483; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.1%)
- **Documentation Coverage:** 73.4% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 78.7)
  * `transfer_icmp` **(Many-Argument Workhorses)** (Impact: 17.1)
  * `spawn_shell` **(Many-Argument Workhorses)** (Impact: 14.3)
  * `load_deps` **(I/O & Config Routines)** (Impact: 10.7)
  * `usage` **(Compute Cores)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 49 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 31`, `args: 9`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 51`, `unreferenced_by_name: 1`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` iphlpapi.h, stdio.h, stdlib.h, windows.h, winsock2.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugins/dbms/mssqlserver/filesystem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 277.3 | **LOC:** 427 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 1.694; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (54.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_stackedWriteFileDebugExe` **(Many-Argument Workhorses)** (Impact: 32.2)
  * `stackedWriteFile` **(Many-Argument Workhorses)** (Impact: 19.2)
    * *Intent:* # NOTE: this is needed here because we use xp_cmdshell extended # procedure to write a file on the b...
  * `_dataToScr` **(Stateful Encapsulated Methods)** (Impact: 11.5)
  * `_stackedWriteFileCertutilExe` **(Stateful Encapsulated Methods)** (Impact: 9.3)
  * `_stackedWriteFilePS` **(Many-Argument Workhorses)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 166
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 70`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 86`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 4`, `import: 23`
* *Defense:* `safety: 3`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.694
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.002375
  * `Imports (Out-Degree: 1):` codecs, lib.core.common, lib.core.compat, lib.core.convert, lib.core.data, lib.core.enums, lib.core.exception, lib.request...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugins/dbms/mysql/fingerprint.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 272.32 | **LOC:** 343 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 1.694; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.2%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkDbms` **(Compute Cores)** (Impact: 62.9)
    * *Intent:* """ References for fingerprint: * http://dev.mysql.com/doc/refman/5.0/en/news-5-0-x.html (up to 5.0....
  * `getFingerprint` **(Compute Cores)** (Impact: 38.9)
  * `_commentCheck` **(Compute Cores)** (Impact: 15.8)
  * `checkDbmsOs` **(Compute Cores)** (Impact: 11.4)
  * `__init__` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 55`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 46`, `fragile_debt: 1`
* *Architecture:* `api: 5`, `import: 18`
* *Defense:* `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.694
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.002375
  * `Imports (Out-Degree: 1):` lib.core.common, lib.core.compat, lib.core.convert, lib.core.data, lib.core.enums, lib.core.session, lib.core.settings, lib.request...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/utils/har.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 260.82 | **LOC:** 237 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.483; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.5%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (73.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `toDict` **(Compute Cores)** (Impact: 11.2)
  * `parse` **(Defensive Guards)** (Impact: 10.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 9.4)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 141
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 58`, `args: 21`, `func_start: 21`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 65`, `unreferenced_by_name: 6`
* *Architecture:* `api: 21`, `import: 11`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` base64, datetime, io, lib.core.bigarray, lib.core.convert, lib.core.settings, re, thirdparty.six.moves...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extra/vulnserver/vulnserver.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 252.76 | **LOC:** 354 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 1.483; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.8%), Complexity Load (formerly Cognitive Load) (89.0%), Concurrency Surface (formerly Concurrency) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_REQUEST` **(Compute Cores)** (Impact: 71.7)
  * `do_POST` **(Compute Cores)** (Impact: 12.6)
  * `finish_request` **(Defensive Guards)** (Impact: 4.3)
  * `init` **(Parameter Forwarders)** (Impact: 3.9)
  * `run` **(Defensive Guards)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 33 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 78`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 56`, `unreferenced_by_name: 5`
* *Architecture:* `io: 2`, `api: 11`, `concurrency: 2`, `import: 26`
* *Defense:* `safety: 10`, `doc: 2`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BaseHTTPServer, SocketServer, __future__, base64, http.client, http.server, httplib, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils/hashdb.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 246.68 | **LOC:** 244 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 1.483; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.7%), Complexity Load (formerly Cognitive Load) (80.6%), Concurrency Surface (formerly Concurrency) (48.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `retrieve` **(Many-Argument Workhorses)** (Impact: 44.1)
  * `flush` **(Stateful Encapsulated Methods)** (Impact: 16.2)
  * `write` **(Defensive Guards)** (Impact: 14.1)
  * `endTransaction` **(Defensive Guards)** (Impact: 7.0)
  * `_get_cursor` **(Stateful Encapsulated Methods)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 34 instances
* *Api Near Db Sink:* 1 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 78`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 49`, `unreferenced_by_name: 4`
* *Architecture:* `io: 2`, `api: 9`, `concurrency: 2`, `import: 24`
* *Defense:* `safety: 25`, `doc: 1`, `sync_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hashlib, lib.core.common, lib.core.compat, lib.core.convert, lib.core.data, lib.core.datatype, lib.core.exception, lib.core.settings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugins/generic/misc.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 227.52 | **LOC:** 205 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **7**; blast radius 7.788; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (69.6%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cleanup` **(Many-Argument Workhorses)** (Impact: 54.9)
    * *Intent:* """ Cleanup file system and database from sqlmap create files, tables and functions """
  * `getRemoteTempPath` **(Compute Cores)** (Impact: 21.7)
  * `getVersionFromBanner` **(Compute Cores)** (Impact: 12.2)
  * `likeOrExact` **(Compute Cores)** (Impact: 9.5)
  * `createSupportTbl` **(Compute Cores)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 59`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 34`
* *Architecture:* `api: 8`, `import: 20`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.788
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.071259
  * `Imports (Out-Degree: 0):` lib.core.common, lib.core.data, lib.core.enums, lib.core.exception, lib.request, ntpath, re
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/utils/hash.py` -> **Miroslav Stampar** (100.0% isolated ownership) | Magnitude: 1600.0
- `plugins/generic/users.py` -> **Miroslav Stampar** (100.0% isolated ownership) | Magnitude: 981.78
- `lib/utils/api.py` -> **Miroslav Stampar** (100.0% isolated ownership) | Magnitude: 864.72
- `lib/utils/tui.py` -> **Miroslav Stampar** (100.0% isolated ownership) | Magnitude: 656.52
- `plugins/generic/takeover.py` -> **Miroslav Stampar** (100.0% isolated ownership) | Magnitude: 525.74

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `plugins/generic/enumeration.py` -> **Severity: 0.299** (Bridge: 0.003 * Flux: 100.0%)
- `plugins/generic/entries.py` -> **Severity: 0.05** (Bridge: 0.0005 * Flux: 100.0%)
- `plugins/generic/users.py` -> **Severity: 0.05** (Bridge: 0.0005 * Flux: 100.0%)
- `lib/utils/pivotdumptable.py` -> **Severity: 0.036** (Bridge: 0.0004 * Flux: 100.0%)
- `plugins/generic/search.py` -> **Severity: 0.016** (Bridge: 0.0002 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `plugins/generic/filesystem.py` -> **Severity: 9.43** (Embedded: 0.095 * Error Risk: 99.2554%)
- `plugins/generic/takeover.py` -> **Severity: 9.373** (Embedded: 0.095 * Error Risk: 98.6459%)
- `plugins/generic/enumeration.py` -> **Severity: 9.02** (Embedded: 0.095 * Error Risk: 94.9389%)
- `plugins/generic/syntax.py` -> **Severity: 8.549** (Embedded: 0.095 * Error Risk: 89.9735%)
- `plugins/generic/fingerprint.py` -> **Severity: 8.212** (Embedded: 0.095 * Error Risk: 86.4295%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `plugins/generic/fingerprint.py` -> **Severity: 4467.0** (Blast Radius: 44.67 * Doc Risk: 100.0%)
- `plugins/generic/syntax.py` -> **Severity: 4467.0** (Blast Radius: 44.67 * Doc Risk: 100.0%)
- `plugins/generic/takeover.py` -> **Severity: 4467.0** (Blast Radius: 44.67 * Doc Risk: 100.0%)
- `plugins/generic/enumeration.py` -> **Severity: 4275.0** (Blast Radius: 42.75 * Doc Risk: 100.0%)
- `plugins/generic/connector.py` -> **Severity: 4056.9** (Blast Radius: 40.569 * Doc Risk: 100.0%)

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
