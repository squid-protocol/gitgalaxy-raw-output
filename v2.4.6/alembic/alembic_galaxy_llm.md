# ARCHITECTURAL_BRIEF: alembic
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/alembic` |
| **Timestamp** | `2026-08-03T21:19:14.628924+00:00` |
| **Scan Duration** | `0.92s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 112 malicious artifacts.

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
| Total Artifacts | 144 |
| Analyzed Artifacts (Scanned) | 119 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 25 |
| Total LOC | 42108 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 82.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4897 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1686 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 10.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.0907 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 13 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 112 | 42108 | 94.1% |
| MARKDOWN | 5 | 0 | 4.2% |
| PLAINTEXT | 2 | 0 | 1.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.407`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 61 | 51.3% |
| file_cluster_8 | 44 | 37.0% |
| file_cluster_16 | 4 | 3.4% |
| file_cluster_0 | 3 | 2.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 7 | 5.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 25*

**Composition by Extension & Reason:**
- `.mako`: 12x Excluded (Unsupported Extension: '.mako')
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 568 LOC)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `.pyi`: 1x Excluded (Machine-Generated Source Code Signature: 877 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1430 LOC)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 66.8 | 10.0 | 5.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 92.8 | 19.4 | 4.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 15.5 | 0.0 | 0.0 |
| API Exposure | 0.0 | 16.2 | 4.3 | 4.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 17.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 24.8 | 1.9 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 88.0 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 99.8 | 28.1 | 9.3 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 64.7 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 62.1 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 11.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `alembic-1.18.4/tests/test_script_production.py` (Hits: 63)
- `alembic-1.18.4/tests/test_command.py` (Hits: 48)
- `alembic-1.18.4/tests/test_autogen_diffs.py` (Hits: 41)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **fixtures.py** (`alembic-1.18.4/alembic/testing/fixtures.py`) — 28 inbound connections
2. **schema.py** (`alembic-1.18.4/alembic/autogenerate/compare/schema.py`) — 25 inbound connections
3. **env.py** (`alembic-1.18.4/alembic/testing/env.py`) — 16 inbound connections
4. **config.py** (`alembic-1.18.4/alembic/config.py`) — 16 inbound connections
5. **types.py** (`alembic-1.18.4/alembic/autogenerate/compare/types.py`) — 15 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **postgresql.py** (`alembic-1.18.4/alembic/ddl/postgresql.py`) — 29 outbound dependencies
2. **base.py** (`alembic-1.18.4/alembic/operations/base.py`) — 28 outbound dependencies
3. **api.py** (`alembic-1.18.4/alembic/autogenerate/api.py`) — 24 outbound dependencies
4. **ops.py** (`alembic-1.18.4/alembic/operations/ops.py`) — 23 outbound dependencies
5. **migration.py** (`alembic-1.18.4/alembic/runtime/migration.py`) — 22 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_assert_data` (@ `alembic-1.18.4/tests/test_batch.py`) -> Impact: **983.1** | LOC: 943
- `to_constraint` (@ `alembic-1.18.4/alembic/operations/ops.py`) -> Impact: **837.7** | LOC: 1477
- `flush` (@ `alembic-1.18.4/alembic/operations/batch.py`) -> Impact: **817.6** | LOC: 591
- `_generate_create_date` (@ `alembic-1.18.4/alembic/script/base.py`) -> Impact: **603.6** | LOC: 190
  * *Intent:* # figure out if the dest is a descendant or an
- `_branched_connection_env` (@ `alembic-1.18.4/tests/test_script_consumption.py`) -> Impact: **494.0** | LOC: 527
- `autogen_column_reflect` (@ `alembic-1.18.4/alembic/ddl/postgresql.py`) -> Impact: **422.8** | LOC: 317
- `test_render_unicode_server_default` (@ `alembic-1.18.4/tests/test_autogen_render.py`) -> Impact: **351.1** | LOC: 1445
- `get_current_revision` (@ `alembic-1.18.4/alembic/runtime/migration.py`) -> Impact: **347.1** | LOC: 273
- `test_default_schema_omitted_by_table_nam` (@ `alembic-1.18.4/tests/test_autogen_diffs.py`) -> Impact: **308.6** | LOC: 595
- `display_version` (@ `alembic-1.18.4/alembic/command.py`) -> Impact: **307.9** | LOC: 96
  * *Intent:* """List changeset scripts in chronological order. :param config: a :class:`.Config` instance. :param rev_range: string revision range. :param verbose:...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `to_constraint` (@ `alembic-1.18.4/alembic/operations/ops.py`) -> **O(2^N) [Recursive]**
- `_generate_create_date` (@ `alembic-1.18.4/alembic/script/base.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # figure out if the dest is a descendant or an
- `dispatch` (@ `alembic-1.18.4/alembic/util/langhelpers.py`) -> **O(2^N) [Recursive]**
- `custom_template_fixture` (@ `alembic-1.18.4/tests/test_command.py`) -> **O(2^N) [Recursive]**
- `_test_ignore_dot_hash_py` (@ `alembic-1.18.4/tests/test_script_consumption.py`) -> **O(2^N) [Recursive]**
- `display_version` (@ `alembic-1.18.4/alembic/command.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """List changeset scripts in chronological order. :param config: a :class:`.Config` instance. :param rev_range: string revision range. :param verbose:...
- `do_expr_where_opts` (@ `alembic-1.18.4/alembic/ddl/postgresql.py`) -> **O(2^N) [Recursive]**
- `register` (@ `alembic-1.18.4/alembic/operations/base.py`) -> **O(2^N) [Recursive]**
- `metadata` (@ `alembic-1.18.4/alembic/testing/fixtures.py`) -> **O(2^N) [Recursive]**
- `_assert_data` (@ `alembic-1.18.4/tests/test_batch.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `test_new_locations_no_autogen` (@ `alembic-1.18.4/tests/test_script_production.py`) -> DB Complexity: **118**
- `to_constraint` (@ `alembic-1.18.4/alembic/operations/ops.py`) -> DB Complexity: **94**
- `custom_template_fixture` (@ `alembic-1.18.4/tests/test_command.py`) -> DB Complexity: **45**
- `_branched_connection_env` (@ `alembic-1.18.4/tests/test_script_consumption.py`) -> DB Complexity: **44**
- `_test_ignore_dot_hash_py` (@ `alembic-1.18.4/tests/test_script_consumption.py`) -> DB Complexity: **42**
- `flush` (@ `alembic-1.18.4/alembic/operations/batch.py`) -> DB Complexity: **39**
- `_multi_dir_testing_config` (@ `alembic-1.18.4/alembic/testing/env.py`) -> DB Complexity: **33**
- `list_templates` (@ `alembic-1.18.4/alembic/command.py`) -> DB Complexity: **30**
  * *Intent:* """List available templates. :param config: a :class:`.Config` object. """
- `_test_007_long_name` (@ `alembic-1.18.4/tests/test_script_production.py`) -> DB Complexity: **22**
- `test_pk_constraint_normally_prevents_dup` (@ `alembic-1.18.4/tests/test_command.py`) -> DB Complexity: **20**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `alembic-1.18.4/tests` | 33 | 14325.6 | 4.73% | 0.0% |
| `alembic-1.18.4/alembic/operations` | 6 | 2930.94 | 20.3% | 33.65% |
| `alembic-1.18.4/alembic/ddl` | 8 | 1462.16 | 15.32% | 62.73% |
| `alembic-1.18.4/alembic/runtime` | 4 | 1308.08 | 15.01% | 39.03% |
| `alembic-1.18.4/alembic/script` | 4 | 1248.86 | 13.18% | 15.19% |
| `alembic-1.18.4/alembic/testing` | 8 | 1237.42 | 10.13% | 0.0% |
| `alembic-1.18.4/alembic` | 8 | 1226.02 | 6.13% | 16.46% |
| `alembic-1.18.4/alembic/testing/suite` | 9 | 1221.1 | 3.69% | 0.0% |
| `alembic-1.18.4/alembic/autogenerate` | 4 | 953.66 | 18.99% | 9.34% |
| `alembic-1.18.4/alembic/util` | 8 | 804.34 | 14.37% | 26.43% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `alembic-1.18.4/alembic/util/compat.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/autogenerate/compare/util.py` -> **99.9998%** Exposure
- `alembic-1.18.4/alembic/ddl/base.py` -> **99.9264%** Exposure
- `alembic-1.18.4/alembic/ddl/mssql.py` -> **98.9971%** Exposure
- `alembic-1.18.4/alembic/ddl/sqlite.py` -> **96.1687%** Exposure
### Highest State Flux (Mutation/Volatility)
- `alembic-1.18.4/alembic/util/exc.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/operations/batch.py` -> **99.7669%** Exposure
- `alembic-1.18.4/noxfile.py` -> **99.6731%** Exposure
- `alembic-1.18.4/alembic/runtime/migration.py` -> **94.9565%** Exposure
- `alembic-1.18.4/alembic/autogenerate/render.py` -> **93.4801%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `alembic-1.18.4/tests/test_postgresql.py` -> **98** Orphaned Functions | **9** Duplicates
- `alembic-1.18.4/tests/test_version_traversal.py` -> **60** Orphaned Functions | **40** Duplicates
- `alembic-1.18.4/tests/test_batch.py` -> **60** Orphaned Functions | **12** Duplicates
- `alembic-1.18.4/tests/test_mysql.py` -> **62** Orphaned Functions | **10** Duplicates
- `alembic-1.18.4/tests/test_autogen_render.py` -> **68** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`alembic-1.18.4/alembic/autogenerate/compare/constraints.py`** -> AI Confidence: **99.31%**
2. **`alembic-1.18.4/alembic/autogenerate/render.py`** -> AI Confidence: **99.31%**
3. **`alembic-1.18.4/alembic/ddl/mysql.py`** -> AI Confidence: **99.31%**
4. **`alembic-1.18.4/alembic/operations/batch.py`** -> AI Confidence: **99.31%**
5. **`alembic-1.18.4/alembic/script/base.py`** -> AI Confidence: **99.31%**
6. **`alembic-1.18.4/alembic/script/revision.py`** -> AI Confidence: **99.31%**
7. **`alembic-1.18.4/noxfile.py`** -> AI Confidence: **99.31%**
8. **`alembic-1.18.4/tools/toxnox.py`** -> AI Confidence: **99.31%**
9. **`alembic-1.18.4/tools/write_pyi.py`** -> AI Confidence: **99.31%**
10. **`alembic-1.18.4/alembic/command.py`** -> AI Confidence: **99.31%**
11. **`alembic-1.18.4/alembic/config.py`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `alembic-1.18.4/alembic/autogenerate/api.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/autogenerate/compare/constraints.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/autogenerate/compare/util.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/autogenerate/render.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/ddl/base.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `alembic-1.18.4/alembic/operations/toimpl.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/script/write_hooks.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/testing/suite/test_environment.py` -> **100.0%** Exposure
- `alembic-1.18.4/tests/test_bulk_insert.py` -> **100.0%** Exposure
- `alembic-1.18.4/tests/test_environment.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `alembic-1.18.4/alembic/autogenerate/render.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/ddl/postgresql.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/operations/base.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/operations/batch.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/operations/ops.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `803` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `alembic-1.18.4/alembic/runtime/migration.py` (PYTHON) -> Cumulative Risk: **766.51**
- **Archetype:** `file_cluster_13` (Distance: 11.935 IQR)
- **Magnitude:** 1041.72 | **LOC:** 1347 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (95.8137%)
- **Heaviest Functions:** `get_current_revision` (Impact: 347.1), `__repr__` (Impact: 212.2), `autocommit_block` (Impact: 70.1)

### 2. `alembic-1.18.4/alembic/util/langhelpers.py` (PYTHON) -> Cumulative Risk: **763.52**
- **Archetype:** `file_cluster_13` (Distance: 10.886 IQR)
- **Magnitude:** 413.26 | **LOC:** 446 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.85%)
- **Heaviest Functions:** `dispatch` (Impact: 242.3), `decorate` (Impact: 24.4), `_install_proxy` (Impact: 13.3)

### 3. `alembic-1.18.4/alembic/ddl/base.py` (PYTHON) -> Cumulative Risk: **759.97**
- **Archetype:** `file_cluster_13` (Distance: 9.994 IQR)
- **Magnitude:** 164.78 | **LOC:** 407 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Tech Debt (99.9264%), Algorithmic Dos (98.3157%)
- **Heaviest Functions:** `visit_column_name` (Impact: 48.9), `visit_drop_column` (Impact: 12.9), `visit_column_type` (Impact: 3.3)

### 4. `alembic-1.18.4/alembic/operations/batch.py` (PYTHON) -> Cumulative Risk: **738.11**
- **Archetype:** `file_cluster_13` (Distance: 11.569 IQR)
- **Magnitude:** 1014.82 | **LOC:** 721 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.7669%)
- **Heaviest Functions:** `flush` (Impact: 817.6), `_should_recreate` (Impact: 14.2), `drop_index` (Impact: 7.3)

### 5. `alembic-1.18.4/alembic/operations/ops.py` (PYTHON) -> Cumulative Risk: **733.06**
- **Archetype:** `file_cluster_16` (Distance: 11.347 IQR)
- **Magnitude:** 1387.22 | **LOC:** 2919 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (93.8796%)
- **Heaviest Functions:** `to_constraint` (Impact: 837.7), `upgrade_ops` (Impact: 88.4), `reverse` (Impact: 14.2)

### 6. `alembic-1.18.4/alembic/autogenerate/compare/util.py` (PYTHON) -> Cumulative Risk: **716.8**
- **Archetype:** `file_cluster_13` (Distance: 9.597 IQR)
- **Magnitude:** 157.84 | **LOC:** 315 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Tech Debt (99.9998%), Algorithmic Dos (99.9775%)
- **Heaviest Functions:** `_apply_reflectinfo_conv` (Impact: 30.8), `_apply_reflectinfo_conv` (Impact: 22.1), `_apply_constraint_conv` (Impact: 22.0)

### 7. `alembic-1.18.4/alembic/ddl/sqlite.py` (PYTHON) -> Cumulative Risk: **711.77**
- **Archetype:** `file_cluster_13` (Distance: 12.123 IQR)
- **Magnitude:** 97.02 | **LOC:** 238 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Tech Debt (96.1687%), Documentation (94.7664%)
- **Heaviest Functions:** `add_constraint` (Impact: 45.8), `drop_constraint` (Impact: 25.4), `compare_server_default` (Impact: 1.8)

### 8. `alembic-1.18.4/alembic/ddl/postgresql.py` (PYTHON) -> Cumulative Risk: **695.89**
- **Archetype:** `file_cluster_13` (Distance: 10.121 IQR)
- **Magnitude:** 644.02 | **LOC:** 865 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Verification (80.0%)
- **Heaviest Functions:** `autogen_column_reflect` (Impact: 422.8), `do_expr_where_opts` (Impact: 53.6), `create_index` (Impact: 24.6)

### 9. `alembic-1.18.4/alembic/autogenerate/api.py` (PYTHON) -> Cumulative Risk: **691.81**
- **Archetype:** `file_cluster_13` (Distance: 10.482 IQR)
- **Magnitude:** 124.14 | **LOC:** 668 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), State Flux (92.0285%), Algorithmic Dos (90.5558%)
- **Heaviest Functions:** `inspector` (Impact: 17.7), `_default_revision` (Impact: 7.6), `generate_scripts` (Impact: 7.1)

### 10. `alembic-1.18.4/alembic/ddl/mssql.py` (PYTHON) -> Cumulative Risk: **684.3**
- **Archetype:** `file_cluster_13` (Distance: 9.282 IQR)
- **Magnitude:** 200.16 | **LOC:** 524 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Tech Debt (98.9971%), Algorithmic Dos (97.6337%)
- **Heaviest Functions:** `_compare_identity_default` (Impact: 48.9), `_exec` (Impact: 27.1), `emit_commit` (Impact: 21.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `alembic-1.18.4/tests/test_batch.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.013 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.163 IQR)
- **Top Global Matches:** file_cluster_8: 10.013, file_cluster_13: 10.356, file_cluster_7: 10.491
- **Magnitude:** 1979.22 | **LOC:** 2580 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (4.5908%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_assert_data` (Impact: 983.1 | O(2^N) | DB: 15)
  * `test_change_type_int_to_boolean` (Impact: 42.9 | O(N^5))
  * `test_rename_col_literal_ck` (Impact: 40.0 | O(N^5))
  * `test_downgrade_batch_fails_gracefully` (Impact: 18.8 | O(N^3))
  * `test_change_type_boolean_to_int` (Impact: 18.2 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 429`, `args: 177`, `func_start: 177`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 62`, `duplicate_logic: 12`, `orphaned_logic: 60`
* *Architecture:* `io: 26`, `api: 148`, `import: 55`
* *Defense:* `safety: 35`, `doc: 16`, `test: 162`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` alembic.ddl, alembic.util, alembic.testing.fixtures, sqlalchemy.dialects, sqlalchemy.schema, alembic, alembic.runtime.migration, alembic.util.sqla_compat...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/operations/ops.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.347 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.34 IQR)
- **Top Global Matches:** file_cluster_16: 11.347, file_cluster_13: 11.634, file_cluster_0: 11.712
- **Magnitude:** 1387.22 | **LOC:** 2919 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 94
- **Risk Profile:** Cognitive Load (19.079%), Tech Debt (93.8796%)
**Top Internal Functions/Classes:**
  * `to_constraint` (Impact: 837.7 | O(2^N) | DB: 94)
  * `upgrade_ops` (Impact: 88.4 | O(2^N) | DB: 1)
  * `reverse` (Impact: 14.2 | O(2^N))
  * `reverse` (Impact: 14.1 | O(2^N))
  * `from_constraint` (Impact: 7.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 349`, `args: 124`, `func_start: 124`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 86`, `state_mutation: 173`, `planned_debt: 1`, `duplicate_logic: 22`
* *Architecture:* `io: 21`, `api: 127`, `import: 49`
* *Defense:* `safety: 7`, `doc: 233`, `test: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 69.633
  * `Choke Point (Betweenness):` 0.01052 | `Ripple Effect (Closeness):` 0.255506
  * `Imports (Out-Degree: 4):` __future__, abc, alembic, sqlalchemy, sqlalchemy.sql.elements, ..runtime.migration, sqlalchemy.sql.schema, .....
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_autogen_diffs.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.244 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.446 IQR)
- **Top Global Matches:** file_cluster_8: 9.244, file_cluster_13: 9.61, file_cluster_7: 9.717
- **Magnitude:** 1258.5 | **LOC:** 2686 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (3.934%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_default_schema_omitted_by_table_nam` (Impact: 308.6 | O(N^6) | DB: 4)
  * `test_drop_fk_with_mixed_case_name` (Impact: 82.2 | O(N^5))
  * `test_compare_metadata_include_name` (Impact: 49.6 | O(N^5))
  * `test_fk_to_different_columns_in_filtered` (Impact: 46.2 | O(N^6) | DB: 1)
    * *Intent:* # Should not raise NoReferencedTableError # Should only create one placeholder table even with multi...
  * `test_fk_placeholder_type_preservation` (Impact: 39.8 | O(N^6) | DB: 1)
    * *Intent:* # obj.referred_table in include_object diffs = self._fixture( m1, m2, name_filters=include_name, obj...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 404`, `args: 138`, `func_start: 138`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 22`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 20`
* *Architecture:* `io: 41`, `api: 207`, `import: 67`
* *Defense:* `safety: 17`, `doc: 32`, `test: 104`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` alembic.autogenerate, alembic.testing.suite._autogen_fixtures, alembic.migration, sqlalchemy.types, alembic.util, sqlalchemy.dialects, alembic, alembic.autogenerate.compare.tables...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/tests/test_command.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.045 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.382 IQR)
- **Top Global Matches:** file_cluster_13: 11.045, file_cluster_8: 11.054, file_cluster_0: 11.21
- **Magnitude:** 1118.4 | **LOC:** 1709 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (6.8042%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_pk_constraint_normally_prevents_dup` (Impact: 215.2 | O(N^5) | DB: 20)
  * `custom_template_fixture` (Impact: 113.7 | O(2^N) | DB: 45)
  * `test_help_text` (Impact: 75.4 | O(N^6) | DB: 7)
  * `test_stamp_argparser_single_rev` (Impact: 51.2 | O(N^4) | DB: 17)
  * `test_init_file_exists_and_is_empty` (Impact: 31.5 | O(N^4) | DB: 12)
    * *Intent:* # ends with a period # not too long assert len(help_text) < 80 assert not commands, "Commands withou...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 365`, `args: 142`, `func_start: 142`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 69`, `dead_code: 1`, `planned_debt: 4`, `duplicate_logic: 18`, `orphaned_logic: 42`
* *Architecture:* `io: 48`, `api: 146`, `import: 45`
* *Defense:* `safety: 61`, `doc: 32`, `test: 175`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` alembic, sqlalchemy, sqlalchemy.sql.schema, alembic.testing.env, alembic.util.sqla_compat, re, contextlib, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/runtime/migration.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.935 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.697 IQR)
- **Top Global Matches:** file_cluster_13: 11.935, file_cluster_16: 11.979, file_cluster_0: 12.028
- **Magnitude:** 1041.72 | **LOC:** 1347 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (34.5717%), Tech Debt (93.1734%)
**Top Internal Functions/Classes:**
  * `get_current_revision` (Impact: 347.1 | O(N^6) | DB: 6)
  * `__repr__` (Impact: 212.2 | O(N^5) | DB: 1)
  * `autocommit_block` (Impact: 70.1 | O(N^5) | DB: 4)
  * `short_log` (Impact: 26.8 | O(2^N))
  * `__exit__` (Impact: 18.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 283`, `args: 81`, `func_start: 81`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 109`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 11`
* *Architecture:* `io: 14`, `api: 75`, `import: 41`
* *Defense:* `safety: 33`, `doc: 63`, `test: 26`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.931
  * `Choke Point (Betweenness):` 0.007389 | `Ripple Effect (Closeness):` 0.165281
  * `Imports (Out-Degree: 4):` __future__, alembic, ..script.base, sqlalchemy, alembic.operations, alembic.migration, .., contextlib...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/alembic/operations/batch.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.569 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.243 IQR)
- **Top Global Matches:** file_cluster_13: 11.569, file_cluster_11: 11.932, file_cluster_16: 11.939
- **Magnitude:** 1014.82 | **LOC:** 721 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (66.7527%), Tech Debt (9.6653%)
**Top Internal Functions/Classes:**
  * `flush` (Impact: 817.6 | O(N^6) | DB: 39)
  * `_should_recreate` (Impact: 14.2 | O(N^3) | DB: 2)
  * `drop_index` (Impact: 7.3 | O(N^3))
    * *Intent:* # type-bound constraints are only included in the new # table via their type object in any case, so ...
  * `dialect` (Impact: 5.3 | O(2^N))
  * `impl` (Impact: 5.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 152`, `args: 39`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 118`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 18`, `api: 31`, `import: 41`
* *Defense:* `safety: 23`, `doc: 6`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.411
  * `Choke Point (Betweenness):` 0.000435 | `Ripple Effect (Closeness):` 0.076271
  * `Imports (Out-Degree: 3):` __future__, sqlalchemy.sql.type_api, sqlalchemy.engine, ..util.sqla_compat, sqlalchemy, ..ddl.impl, sqlalchemy.sql.elements, sqlalchemy.util...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_op.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.065 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.15 IQR)
- **Top Global Matches:** file_cluster_8: 9.065, file_cluster_13: 9.609, file_cluster_7: 9.653
- **Magnitude:** 1008.8 | **LOC:** 1770 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (2.9214%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_alter_column_schema_type_unnamed` (Impact: 32.5 | O(N^5))
  * `test_add_foreign_key_dialect_kw` (Impact: 32.3 | O(N^6) | DB: 3)
  * `test_run_async_error` (Impact: 31.3 | O(N^4))
  * `test_custom_op` (Impact: 25.4 | O(N^4) | DB: 5)
  * `test_add_column_primary_key` (Impact: 22.9 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 269`, `args: 162`, `func_start: 162`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 14`, `planned_debt: 4`, `duplicate_logic: 6`
* *Architecture:* `io: 22`, `api: 288`, `concurrency: 3`, `import: 41`
* *Defense:* `safety: 10`, `doc: 22`, `test: 161`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` sqlalchemy.ext.asyncio, alembic.util, alembic.testing.fixtures, alembic, unittest.mock, alembic.testing.assertions, alembic.testing, sqlalchemy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/tests/test_autogen_render.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.084 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.432 IQR)
- **Top Global Matches:** file_cluster_8: 9.084, file_cluster_7: 9.626, file_cluster_13: 9.727
- **Magnitude:** 963.46 | **LOC:** 2723 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (2.3427%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_render_unicode_server_default` (Impact: 351.1 | O(N^6) | DB: 11)
  * `test_add_fk_constraint_kwarg` (Impact: 25.7 | O(N^4))
  * `test_render_table_w_unsupported_constrai` (Impact: 14.0 | O(N^4) | DB: 3)
  * `test_add_fk_constraint_schema_batch` (Impact: 9.9 | O(N^4))
  * `test_drop_fk_constraint_batch_schema` (Impact: 9.9 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 310`, `args: 167`, `func_start: 166`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 6`, `orphaned_logic: 68`
* *Architecture:* `io: 39`, `api: 173`, `import: 57`
* *Defense:* `safety: 4`, `doc: 56`, `test: 159`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` alembic.autogenerate, sqlalchemy.dialects.mysql, alembic.migration, sqlalchemy.types, alembic.testing.fixtures, alembic, alembic.util, sqlalchemy.dialects...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/tests/test_autogen_indexes.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.079 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.817 IQR)
- **Top Global Matches:** file_cluster_8: 9.079, file_cluster_7: 9.737, file_cluster_13: 9.834
- **Magnitude:** 914.24 | **LOC:** 2135 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (3.2816%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_remove_connection_uq` (Impact: 57.9 | O(N^6))
  * `test_remove_connection_index` (Impact: 57.5 | O(N^6))
  * `test_unnamed_cols_changed` (Impact: 44.7 | O(N^6))
  * `test_expression_indexes_add` (Impact: 42.1 | O(N^5))
  * `_lots_of_indexes` (Impact: 37.1 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 195`, `args: 161`, `func_start: 83`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 6`, `dead_code: 1`, `duplicate_logic: 8`, `orphaned_logic: 56`
* *Architecture:* `io: 20`, `api: 88`, `import: 36`
* *Defense:* `safety: 17`, `doc: 16`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` alembic.testing.suite._autogen_fixtures, sqlalchemy.sql.expression, alembic.util, alembic, alembic.testing.assertions, alembic.testing, sqlalchemy, contextlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/tests/test_script_consumption.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.227 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.338 IQR)
- **Top Global Matches:** file_cluster_13: 11.227, file_cluster_8: 11.421, file_cluster_0: 11.563
- **Magnitude:** 909.38 | **LOC:** 1221 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (3.8981%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_branched_connection_env` (Impact: 494.0 | O(2^N) | DB: 44)
  * `_test_ignore_dot_hash_py` (Impact: 262.0 | O(2^N) | DB: 42)
  * `_patch_environment` (Impact: 11.1 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 214`, `args: 64`, `func_start: 64`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 62`, `dead_code: 1`
* *Architecture:* `io: 19`, `api: 65`, `import: 37`
* *Defense:* `safety: 60`, `doc: 36`, `test: 78`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, textwrap, alembic.testing.fixtures, alembic, alembic.config, alembic.environment, alembic.script, alembic.testing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/script/base.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.904 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.304 IQR)
- **Top Global Matches:** file_cluster_13: 10.904, file_cluster_16: 11.013, file_cluster_8: 11.236
- **Magnitude:** 882.72 | **LOC:** 1053 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (19.9599%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_generate_create_date` (Impact: 603.6 | O(2^N) | DB: 6)
    * *Intent:* # figure out if the dest is a descendant or an
  * `log_entry` (Impact: 88.8 | O(N^4))
  * `longdoc` (Impact: 21.4 | O(N^5))
  * `_ensure_directory` (Impact: 13.3 | O(N^4) | DB: 3)
  * `_append_template` (Impact: 11.8 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 183`, `args: 40`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 52`, `dead_code: 2`
* *Architecture:* `io: 11`, `api: 27`, `import: 36`
* *Defense:* `safety: 26`, `doc: 48`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.123
  * `Choke Point (Betweenness):` 0.000169 | `Ripple Effect (Closeness):` 0.008475
  * `Imports (Out-Degree: 4):` __future__, ..runtime, zoneinfo, ..runtime.migration, .., datetime, re, contextlib...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_postgresql.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.453 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.503 IQR)
- **Top Global Matches:** file_cluster_8: 9.453, file_cluster_13: 9.66, file_cluster_0: 9.954
- **Magnitude:** 795.64 | **LOC:** 1894 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (3.1666%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_change_identity_in_column` (Impact: 51.3 | O(N^5) | DB: 4)
  * `_lots_of_indexes` (Impact: 21.0 | O(N^4))
  * `test_array_type_user_defined_inner` (Impact: 18.1 | O(N^4) | DB: 1)
  * `_index_op_clause` (Impact: 16.7 | O(N^3))
  * `test_numeric` (Impact: 15.7 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 314`, `args: 174`, `func_start: 132`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 19`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 9`, `orphaned_logic: 98`
* *Architecture:* `io: 37`, `api: 134`, `import: 69`
* *Defense:* `safety: 15`, `doc: 25`, `test: 119`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` alembic.autogenerate, alembic.testing.suite._autogen_fixtures, sqlalchemy.sql.expression, alembic.migration, alembic.autogenerate.compare.server_defaults, alembic.testing.fixtures, alembic, alembic.autogenerate.compare.tables...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/autogenerate/render.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.831 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.288 IQR)
- **Top Global Matches:** file_cluster_13: 10.831, file_cluster_8: 10.965, file_cluster_16: 11.076
- **Magnitude:** 767.36 | **LOC:** 1173 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (45.0106%), Tech Debt (8.7525%)
**Top Internal Functions/Classes:**
  * `_drop_index` (Impact: 219.3 | O(N^4) | DB: 10)
  * `__repr__` (Impact: 135.2 | O(N^4) | DB: 9)
  * `_add_table` (Impact: 91.9 | O(N^5))
  * `_render_fetched_value` (Impact: 87.7 | O(N^3) | DB: 12)
  * `_add_index` (Impact: 33.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 231`, `args: 50`, `func_start: 50`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 119`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 30`, `api: 13`, `import: 44`
* *Defense:* `safety: 23`, `doc: 4`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.705
  * `Choke Point (Betweenness):` 0.000359 | `Ripple Effect (Closeness):` 0.022599
  * `Imports (Out-Degree: 4):` __future__, io, mako.pygen, sqlalchemy.sql.type_api, sqlalchemy.dialects, .., alembic.autogenerate.api, sqlalchemy.sql.sqltypes...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/alembic/command.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.771 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.41 IQR)
- **Top Global Matches:** file_cluster_8: 9.771, file_cluster_16: 9.95, file_cluster_13: 10.027
- **Magnitude:** 759.9 | **LOC:** 849 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (8.113%), Tech Debt (86.1395%)
**Top Internal Functions/Classes:**
  * `display_version` (Impact: 307.9 | O(2^N) | DB: 1)
    * *Intent:* """List changeset scripts in chronological order. :param config: a :class:`.Config` instance. :param...
  * `list_templates` (Impact: 231.7 | O(N^6) | DB: 30)
    * *Intent:* """List available templates. :param config: a :class:`.Config` object. """
  * `_display_history` (Impact: 37.5 | O(N^5))
  * `branches` (Impact: 31.4 | O(N^6))
  * `_display_history_w_current` (Impact: 28.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 83`, `args: 29`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`, `dead_code: 1`, `duplicate_logic: 6`, `orphaned_logic: 7`
* *Architecture:* `io: 12`, `api: 26`, `import: 16`
* *Defense:* `safety: 4`, `doc: 84`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, alembic.script.revision, .util, , .runtime.environment, pathlib, alembic.config, alembic.script.base...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/tests/test_version_traversal.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.393 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.473 IQR)
- **Top Global Matches:** file_cluster_8: 10.393, file_cluster_16: 10.475, file_cluster_0: 10.728
- **Magnitude:** 743.88 | **LOC:** 1526 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (10.4141%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_downgrade_once_order_right` (Impact: 13.8 | O(N^4))
    * *Intent:* # Old downgrade -1 behaviour depends on order of branch upgrades. # This should probably fail (ambig...
  * `test_downgrade_once_order_left` (Impact: 13.8 | O(N^4))
  * `test_downgrade_branch_dependency` (Impact: 11.7 | O(N^3))
  * `_assert_downgrade` (Impact: 10.2 | O(N^3))
  * `_assert_upgrade` (Impact: 10.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 158`, `args: 107`, `func_start: 107`, `class_start: 17`
* *Risk/State:* `state_mutation: 133`, `duplicate_logic: 40`, `orphaned_logic: 60`
* *Architecture:* `api: 122`, `import: 10`
* *Defense:* `safety: 5`, `doc: 48`, `test: 83`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` alembic.migration, alembic.testing.fixtures, alembic, alembic.testing, alembic.testing.env
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/tests/test_script_production.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.929 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.23 IQR)
- **Top Global Matches:** file_cluster_8: 9.929, file_cluster_13: 10.077, file_cluster_7: 10.367
- **Magnitude:** 651.94 | **LOC:** 1593 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 118
- **Risk Profile:** Cognitive Load (4.2609%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_new_locations_no_autogen` (Impact: 226.9 | O(N^6) | DB: 118)
  * `_test_007_long_name` (Impact: 117.9 | O(N^6) | DB: 22)
  * `test_create_script_branches_old_template` (Impact: 27.3 | O(N^4) | DB: 6)
  * `test_env_emits_warning` (Impact: 19.2 | O(N^6) | DB: 6)
  * `_env_fixture` (Impact: 18.9 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 262`, `args: 97`, `func_start: 92`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 57`, `duplicate_logic: 7`, `orphaned_logic: 8`
* *Architecture:* `io: 63`, `api: 93`, `import: 52`
* *Defense:* `safety: 31`, `doc: 28`, `test: 92`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` sqlalchemy.dialects.mysql, sqlalchemy.dialects, alembic.util, alembic.testing.fixtures, alembic, zoneinfo, pathlib, unittest.mock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/ddl/postgresql.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.121 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.449 IQR)
- **Top Global Matches:** file_cluster_13: 10.121, file_cluster_16: 10.654, file_cluster_8: 10.663
- **Magnitude:** 644.02 | **LOC:** 865 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (24.3897%), Tech Debt (37.6846%)
**Top Internal Functions/Classes:**
  * `autogen_column_reflect` (Impact: 422.8 | O(N^6) | DB: 17)
  * `do_expr_where_opts` (Impact: 53.6 | O(2^N) | DB: 3)
  * `create_index` (Impact: 24.6 | O(N^5))
    * *Intent:* # this likely defaults to None if not present, so get() # should normally not return the default val...
  * `prep_table_for_batch` (Impact: 20.4 | O(N^4))
  * `_postgresql_autogenerate_prefix` (Impact: 6.2 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 227`, `args: 34`, `func_start: 34`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 61`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 8`
* *Architecture:* `io: 32`, `api: 23`, `import: 67`
* *Defense:* `safety: 11`, `doc: 15`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.287
  * `Choke Point (Betweenness):` 0.000688 | `Ripple Effect (Closeness):` 0.016949
  * `Imports (Out-Degree: 6):` __future__, .impl, alembic, sqlalchemy.dialects, sqlalchemy.sql.functions, sqlalchemy, sqlalchemy.sql.elements, ..runtime.migration...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_revision.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.49 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.103 IQR)
- **Top Global Matches:** file_cluster_8: 8.49, file_cluster_7: 9.173, file_cluster_13: 9.445
- **Magnitude:** 553.1 | **LOC:** 1684 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (3.0675%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_no_revision_exists` (Impact: 95.5 | O(N^4) | DB: 10)
  * `test_invalid_datatype` (Impact: 81.6 | O(N^5) | DB: 3)
  * `test_partial_traversal_implicit_base_thr` (Impact: 5.4 | O(N^4))
  * `test_revision_map_lower_simple_dep_cycle` (Impact: 5.0 | O(N^4))
  * `test_revision_map_upper_simple_dep_cycle` (Impact: 5.0 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 205`, `args: 152`, `func_start: 152`, `class_start: 19`
* *Risk/State:* `state_mutation: 21`, `dead_code: 1`, `duplicate_logic: 2`, `orphaned_logic: 35`
* *Architecture:* `io: 1`, `api: 165`, `import: 14`
* *Defense:* `safety: 4`, `doc: 4`, `test: 133`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` alembic.script.revision, alembic.testing.fixtures, , alembic.testing, sqlalchemy.testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/tests/requirements.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.235 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.052 IQR)
- **Top Global Matches:** file_cluster_0: 10.235, file_cluster_8: 10.528, file_cluster_12: 10.56
- **Magnitude:** 444.8 | **LOC:** 425 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (22.2994%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mysql_check_col_name_change` (Impact: 32.2 | O(N^5))
  * `_sqlite_json` (Impact: 31.3 | O(N^6))
  * `stubs_test` (Impact: 27.4 | O(N^5) | DB: 9)
  * `_mysql_and_check_constraints_exist` (Impact: 26.7 | O(N^5))
  * `json_type` (Impact: 25.2 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 154`, `args: 69`, `func_start: 60`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `planned_debt: 4`, `fragile_debt: 1`, `orphaned_logic: 40`
* *Architecture:* `io: 11`, `api: 56`, `import: 10`
* *Defense:* `safety: 9`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` alembic.testing.requirements, alembic.util, alembic.testing, sqlalchemy, black, zimports, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/util/langhelpers.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.886 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.137 IQR)
- **Top Global Matches:** file_cluster_13: 10.886, file_cluster_16: 10.972, file_cluster_0: 11.335
- **Magnitude:** 413.26 | **LOC:** 446 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (27.2907%), Tech Debt (34.2007%)
**Top Internal Functions/Classes:**
  * `dispatch` (Impact: 242.3 | O(2^N) | DB: 2)
  * `decorate` (Impact: 24.4 | O(N^5))
  * `_install_proxy` (Impact: 13.3 | O(N^4))
  * `_remove_proxy` (Impact: 13.3 | O(N^4))
  * `_name_error` (Impact: 9.1 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 119`, `args: 31`, `func_start: 31`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 56`, `high_risk_execution: 1`, `state_mutation: 26`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 32`, `import: 28`
* *Defense:* `safety: 11`, `doc: 30`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.941
  * `Choke Point (Betweenness):` 7.2e-05 | `Ripple Effect (Closeness):` 0.008475
  * `Imports (Out-Degree: 2):` __future__, textwrap, collections, uuid, enum, .compat, sqlalchemy.util, collections.abc...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_mysql.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.294 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.111 IQR)
- **Top Global Matches:** file_cluster_8: 8.294, file_cluster_13: 8.86, file_cluster_7: 9.082
- **Magnitude:** 408.24 | **LOC:** 787 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (3.0007%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_compare_default_roundtrip` (Impact: 29.0 | O(N^4))
  * `test_alter_column_computed_not_supported` (Impact: 12.7 | O(N^3))
  * `test_alter_column_identity_not_supported` (Impact: 12.7 | O(N^3))
  * `test_alter_column_modify_programmatic_de` (Impact: 10.3 | O(N^4))
    * *Intent:* # test issue #736 # when autogenerate.compare creates the operation object # programmatically, the s...
  * `tearDown` (Impact: 7.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 163`, `args: 74`, `func_start: 74`, `class_start: 4`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 1`, `duplicate_logic: 10`, `orphaned_logic: 62`
* *Architecture:* `io: 17`, `api: 76`, `import: 35`
* *Defense:* `safety: 1`, `doc: 2`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` alembic.autogenerate, sqlalchemy.dialects.mysql, alembic.migration, alembic.autogenerate.compare.server_defaults, alembic.testing.fixtures, alembic, alembic.testing, sqlalchemy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/testing/suite/test_autogen_fks.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.67 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.606 IQR)
- **Top Global Matches:** file_cluster_8: 7.67, file_cluster_7: 8.356, file_cluster_1: 8.631
- **Magnitude:** 399.9 | **LOC:** 1192 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.3302%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_change_fk` (Impact: 72.1 | O(N^6))
  * `test_remove_connection_fk` (Impact: 58.4 | O(N^6))
  * `test_add_metadata_fk` (Impact: 19.7 | O(N^4))
  * `test_no_change_composite_fk` (Impact: 6.3 | O(N^4))
  * `test_add_composite_fk_with_name` (Impact: 6.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 77`, `args: 40`, `func_start: 40`, `class_start: 3`
* *Risk/State:* `duplicate_logic: 2`
* *Architecture:* `io: 6`, `api: 74`, `import: 12`
* *Defense:* `safety: 3`, `doc: 16`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.123
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.008475
  * `Imports (Out-Degree: 1):` ...testing, sqlalchemy, ._autogen_fixtures
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/alembic/config.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.929 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.314 IQR)
- **Top Global Matches:** file_cluster_16: 10.929, file_cluster_13: 11.038, file_cluster_8: 11.174
- **Magnitude:** 399.36 | **LOC:** 1052 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (10.9657%), Tech Debt (45.521%)
**Top Internal Functions/Classes:**
  * `get_version_locations_list` (Impact: 86.4 | O(N^5))
  * `file_config` (Impact: 74.0 | O(2^N))
  * `get_hooks_list` (Impact: 43.3 | O(N^5) | DB: 3)
  * `toml_alembic_config` (Impact: 32.1 | O(N^5) | DB: 3)
  * `print_stdout` (Impact: 12.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 146`, `args: 39`, `func_start: 39`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 45`, `duplicate_logic: 6`
* *Architecture:* `io: 9`, `api: 38`, `import: 27`
* *Defense:* `safety: 17`, `doc: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 46.665
  * `Choke Point (Betweenness):` 0.019744 | `Ripple Effect (Closeness):` 0.265778
  * `Imports (Out-Degree: 1):` __future__, sys, .util, logging, , .util.pyfiles, pathlib, alembic...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_mssql.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.792 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.307 IQR)
- **Top Global Matches:** file_cluster_8: 8.792, file_cluster_13: 9.05, file_cluster_0: 9.359
- **Magnitude:** 384.84 | **LOC:** 731 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (6.6686%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_issue_1744` (Impact: 19.5 | O(N^4))
  * `test_add_column_identity` (Impact: 18.2 | O(N^4))
  * `test_alter_column_nullable_type_required` (Impact: 14.5 | O(N^3))
  * `test_begin_commit` (Impact: 14.4 | O(N^3))
  * `test_alter_column_computed_not_supported` (Impact: 12.7 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 146`, `args: 57`, `func_start: 57`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 17`, `state_mutation: 5`, `orphaned_logic: 56`
* *Architecture:* `io: 25`, `api: 60`, `import: 35`
* *Defense:* `safety: 3`, `doc: 7`, `test: 59`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` __future__, alembic.testing.fixtures, alembic, alembic.testing, sqlalchemy, alembic.testing.env, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/testing/fixtures.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.608 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.797 IQR)
- **Top Global Matches:** file_cluster_13: 9.608, file_cluster_0: 9.915, file_cluster_11: 10.347
- **Magnitude:** 366.8 | **LOC:** 405 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (9.224%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_run_alter_col` (Impact: 90.3 | O(N^5))
  * `metadata` (Impact: 53.1 | O(2^N) | DB: 3)
  * `write` (Impact: 33.0 | O(N^5) | DB: 1)
  * `clear_staging_dir` (Impact: 22.1 | O(N^4) | DB: 18)
  * `restore_operations` (Impact: 11.2 | O(N^3) | DB: 1)
    * *Intent:* """Restore runners for modified operations"""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 137`, `args: 33`, `func_start: 33`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 23`, `planned_debt: 2`, `duplicate_logic: 5`
* *Architecture:* `io: 27`, `api: 46`, `import: 38`
* *Defense:* `safety: 7`, `doc: 4`, `test: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.951
  * `Choke Point (Betweenness):` 0.013617 | `Ripple Effect (Closeness):` 0.237288
  * `Imports (Out-Degree: 2):` __future__, sqlalchemy.testing.assertions, alembic, sqlalchemy, .env, re, contextlib, ..migration...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `alembic-1.18.4/tests/test_dispatch.py` (PYTHON) | Magnitude: 196.4 | Delta: **0.2 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 256, structural_boundaries: 100, api: 62, args: 57
- `alembic-1.18.4/tests/requirements.py` (PYTHON) | Magnitude: 444.8 | Delta: **0.293 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 307, structural_boundaries: 154, args: 69, func_start: 60
- `alembic-1.18.4/alembic/testing/requirements.py` (PYTHON) | Magnitude: 187.08 | Delta: **0.442 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 135, structural_boundaries: 86, api: 69, args: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `alembic-1.18.4/alembic/runtime/environment.py` (PYTHON) | Magnitude: 136.08 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 219, structural_boundaries: 112, doc: 92, generics: 69
- `alembic-1.18.4/alembic/testing/suite/_autogen_fixtures.py` (PYTHON) | Magnitude: 66.5 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 372, structural_boundaries: 102, encapsulation: 40, import: 33
- `alembic-1.18.4/tests/test_command.py` (PYTHON) | Magnitude: 1118.4 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1230, structural_boundaries: 365, test: 175, encapsulation: 148
- `alembic-1.18.4/alembic/autogenerate/compare/util.py` (PYTHON) | Magnitude: 157.84 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 241, structural_boundaries: 77, encapsulation: 48, branch: 43
- `alembic-1.18.4/noxfile.py` (PYTHON) | Magnitude: 56.4 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 158, state_mutation: 39, branch: 26, structural_boundaries: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `alembic-1.18.4/alembic/config.py` (PYTHON) | Magnitude: 399.36 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 633, structural_boundaries: 146, branch: 128, generics: 97
- `alembic-1.18.4/alembic/script/revision.py` (PYTHON) | Magnitude: 317.9 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1143, branch: 295, encapsulation: 272, structural_boundaries: 222
- `alembic-1.18.4/alembic/operations/base.py` (PYTHON) | Magnitude: 310.14 | Delta: **0.204 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 505, doc: 229, structural_boundaries: 182, generics: 162
- `alembic-1.18.4/alembic/operations/ops.py` (PYTHON) | Magnitude: 1387.22 | Delta: **0.287 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1509, structural_boundaries: 349, generics: 326, doc: 233

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `alembic-1.18.4/alembic/autogenerate/compare/tables.py` (PYTHON) | Magnitude: 36.9 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 225, structural_boundaries: 49, branch: 39, state_mutation: 27
- `alembic-1.18.4/tests/test_messaging.py` (PYTHON) | Magnitude: 16.64 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 15, import: 6, test: 4
- `alembic-1.18.4/alembic/autogenerate/compare/types.py` (PYTHON) | Magnitude: 10.66 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 59, import: 14, encapsulation: 14
- `alembic-1.18.4/alembic/autogenerate/compare/constraints.py` (PYTHON) | Magnitude: 64.2 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 601, branch: 156, structural_boundaries: 114, encapsulation: 61
- `alembic-1.18.4/alembic/testing/env.py` (PYTHON) | Magnitude: 160.52 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 196, structural_boundaries: 80, encapsulation: 67, doc: 34

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `alembic-1.18.4/alembic/autogenerate/api.py` -> **Severity: 2.366** (Bridge: 0.0257 * Flux: 92.0285%)
- `alembic-1.18.4/alembic/config.py` -> **Severity: 1.189** (Bridge: 0.0197 * Flux: 60.2193%)
- `alembic-1.18.4/alembic/operations/ops.py` -> **Severity: 0.928** (Bridge: 0.0105 * Flux: 88.2507%)
- `alembic-1.18.4/alembic/runtime/migration.py` -> **Severity: 0.702** (Bridge: 0.0074 * Flux: 94.9565%)
- `alembic-1.18.4/alembic/util/sqla_compat.py` -> **Severity: 0.526** (Bridge: 0.0113 * Flux: 46.5424%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `alembic-1.18.4/alembic/migration.py` -> **Severity: 17.2** (Embedded: 0.215 * Error Risk: 80.0%)
- `alembic-1.18.4/alembic/operations/ops.py` -> **Severity: 14.506** (Embedded: 0.2555 * Error Risk: 56.7746%)
- `alembic-1.18.4/alembic/autogenerate/compare/types.py` -> **Severity: 14.343** (Embedded: 0.2404 * Error Risk: 59.661%)
- `alembic-1.18.4/alembic/config.py` -> **Severity: 13.146** (Embedded: 0.2658 * Error Risk: 49.4611%)
- `alembic-1.18.4/alembic/util/exc.py` -> **Severity: 12.782** (Embedded: 0.1598 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `alembic-1.18.4/alembic/runtime/plugins.py` -> **Severity: 5750.322** (Blast Radius: 57.741 * Doc Risk: 99.5882%)
- `alembic-1.18.4/alembic/config.py` -> **Severity: 3821.136** (Blast Radius: 46.665 * Doc Risk: 81.8844%)
- `alembic-1.18.4/alembic/autogenerate/compare/schema.py` -> **Severity: 3543.502** (Blast Radius: 83.057 * Doc Risk: 42.6635%)
- `alembic-1.18.4/alembic/operations/ops.py` -> **Severity: 2723.277** (Blast Radius: 69.633 * Doc Risk: 39.109%)
- `alembic-1.18.4/alembic/autogenerate/compare/types.py` -> **Severity: 2468.779** (Blast Radius: 93.881 * Doc Risk: 26.2969%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
