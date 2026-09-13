# ARCHITECTURAL_BRIEF: alembic
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
| Total Artifacts | 144 |
| Analyzed Artifacts (Scanned) | 119 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 25 |
| Total LOC | 42393 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 82.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4874 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1573 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 10.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.0891 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 13 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 112 | 42393 | 94.1% |
| MARKDOWN | 5 | 0 | 4.2% |
| PLAINTEXT | 2 | 0 | 1.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 112 | 94.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 7 | 5.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 25*

**Composition by Extension & Reason:**
- `.mako`: 12x Excluded (Unsupported Extension: '.mako')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 568 LOC), 1x Packed Payload Guard (Impossible Density: 3.27 hits/line), 1x Packed Payload Guard (Impossible Density: 3.88 hits/line)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `.pyi`: 1x Excluded (Machine-Generated Source Code Signature: 877 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1430 LOC)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 89.7 | 27.1 | 19.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.5 | 68.5 | 73.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.5 | 8.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 87.4 | 25.0 | 12.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 41.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 24.8 | 1.9 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 83.9 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 71.9 | 94.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 452 | 58 | 11 | `alembic-1.18.4/alembic/script/revision.py` |
| cleanup | 15 | 11 | 0 | `alembic-1.18.4/tests/test_command.py` |
| guards | 1294 | 82 | 24 | `alembic-1.18.4/alembic/script/revision.py` |
| danger | 957 | 75 | 22 | `alembic-1.18.4/alembic/operations/ops.py` |
| concurrency | 119 | 29 | 4 | `alembic-1.18.4/alembic/testing/fixtures.py` |
| connectivity | 3147 | 96 | 69 | `alembic-1.18.4/tests/test_autogen_render.py` |
| io | 1054 | 84 | 22 | `alembic-1.18.4/tests/test_script_production.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 10 | 4 | 0 | `alembic-1.18.4/alembic/script/write_hooks.py` |
| time | 24 | 3 | 0 | `alembic-1.18.4/tests/test_script_production.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 111 | 27 | 4 | `alembic-1.18.4/tests/test_autogen_render.py` |
| events | 20 | 7 | 0 | `alembic-1.18.4/tests/test_config.py` |
| tests | 1915 | 41 | 57 | `alembic-1.18.4/tests/test_batch.py` |
| docs | 734 | 69 | 20 | `alembic-1.18.4/alembic/runtime/environment.py` |
| debt | 198 | 40 | 5 | `alembic-1.18.4/tests/test_command.py` |
| mutation | 13580 | 97 | 287 | `alembic-1.18.4/tests/test_autogen_render.py` |
| dead_code | 1361 | 58 | 32 | `alembic-1.18.4/tests/test_autogen_render.py` |
| credential | 1 | 1 | 0 | `alembic-1.18.4/tests/test_autogen_render.py` |
| threat | 403 | 43 | 9 | `alembic-1.18.4/alembic/operations/ops.py` |
| ml_ai | 80 | 7 | 0 | `alembic-1.18.4/tests/test_revision.py` |
| ui | 103 | 8 | 0 | `alembic-1.18.4/tests/test_autogen_render.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.7857**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `alembic-1.18.4/tests/test_script_production.py` (Hits: 63)
- `alembic-1.18.4/tests/test_command.py` (Hits: 44)
- `alembic-1.18.4/tests/test_autogen_diffs.py` (Hits: 41)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **fixtures.py** (`alembic-1.18.4/alembic/testing/fixtures.py`) — 28 inbound connections
2. **schema.py** (`alembic-1.18.4/alembic/autogenerate/compare/schema.py`) — 26 inbound connections
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

- `_compare_indexes_and_uniques` (@ `alembic-1.18.4/alembic/autogenerate/compare/constraints.py`) -> Impact: **236.4** | LOC: 389
- `alter_column` (@ `alembic-1.18.4/alembic/ddl/mysql.py`) -> Impact: **170.9** | LOC: 119
- `_generate_stub_for_meth` (@ `alembic-1.18.4/tools/write_pyi.py`) -> Impact: **129.2** | LOC: 123
- `generate_revision` (@ `alembic-1.18.4/alembic/script/base.py`) -> Impact: **123.6** | LOC: 151
- `tox_parameters` (@ `alembic-1.18.4/tools/toxnox.py`) -> Impact: **108.0** | LOC: 151
- `_compare_foreign_keys` (@ `alembic-1.18.4/alembic/autogenerate/compare/constraints.py`) -> Impact: **104.1** | LOC: 125
- `configure` (@ `alembic-1.18.4/alembic/runtime/environment.py`) -> Impact: **80.7** | LOC: 532
- `alter_column` (@ `alembic-1.18.4/alembic/ddl/mssql.py`) -> Impact: **77.2** | LOC: 102
- `_recur_param` (@ `alembic-1.18.4/tools/toxnox.py`) -> Impact: **65.7** | LOC: 74
- `init` (@ `alembic-1.18.4/alembic/command.py`) -> Impact: **65.6** | LOC: 150

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `alembic-1.18.4/tests` | 34 | 12150.14 | 13.56% | 0.0% |
| `alembic-1.18.4/alembic/ddl` | 9 | 2697.1 | 36.54% | 57.59% |
| `alembic-1.18.4/alembic/operations` | 6 | 2553.22 | 49.35% | 21.06% |
| `alembic-1.18.4/alembic/script` | 4 | 2302.84 | 44.79% | 2.97% |
| `alembic-1.18.4/alembic/autogenerate/compare` | 8 | 1728.3 | 48.91% | 12.98% |
| `alembic-1.18.4/alembic/autogenerate` | 4 | 1567.66 | 47.08% | 2.19% |
| `alembic-1.18.4/alembic` | 8 | 1144.06 | 8.97% | 7.13% |
| `alembic-1.18.4/alembic/runtime` | 4 | 1140.12 | 31.93% | 2.12% |
| `alembic-1.18.4/alembic/testing/suite` | 9 | 1093.6 | 13.62% | 0.0% |
| `alembic-1.18.4/alembic/util` | 7 | 1044.64 | 45.07% | 9.02% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `alembic-1.18.4/alembic/ddl/oracle.py` -> **99.4852%** Exposure
- `alembic-1.18.4/alembic/ddl/mssql.py` -> **98.1993%** Exposure
- `alembic-1.18.4/alembic/ddl/sqlite.py` -> **97.8654%** Exposure
- `alembic-1.18.4/alembic/operations/schemaobj.py` -> **91.6672%** Exposure
- `alembic-1.18.4/alembic/ddl/postgresql.py` -> **91.4296%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `alembic-1.18.4/alembic/autogenerate/compare/tables.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/autogenerate/render.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/operations/batch.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/operations/schemaobj.py` -> **100.0%** Exposure
- `alembic-1.18.4/alembic/templates/multidb/env.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `alembic-1.18.4/tests/test_autogen_render.py` -> **153** Orphaned Functions | **3** Duplicates
- `alembic-1.18.4/tests/test_revision.py` -> **123** Orphaned Functions | **0** Duplicates
- `alembic-1.18.4/tests/test_batch.py` -> **100** Orphaned Functions | **12** Duplicates
- `alembic-1.18.4/tests/test_postgresql.py` -> **108** Orphaned Functions | **4** Duplicates
- `alembic-1.18.4/tests/test_command.py` -> **96** Orphaned Functions | **15** Duplicates

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
- **Unknown Dependencies:** `813` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `alembic-1.18.4/alembic/operations/schemaobj.py` (PYTHON) -> Cumulative Risk: **684.9**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 270.7 | **LOC:** 291 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (95.6522%), Safety Score (93.3673%)
- **Heaviest Functions:** `foreign_key_constraint` (Impact: 49.4), `table` (Impact: 33.2), `_ensure_table_for_fk` (Impact: 10.7)

### 2. `alembic-1.18.4/alembic/ddl/postgresql.py` (PYTHON) -> Cumulative Risk: **684.33**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 598.96 | **LOC:** 865 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9988%), Safety Score (92.7313%)
- **Heaviest Functions:** `_exclude_constraint` (Impact: 33.0), `_cleanup_index_expr` (Impact: 31.6), `compare_indexes` (Impact: 30.9)

### 3. `alembic-1.18.4/alembic/ddl/sqlite.py` (PYTHON) -> Cumulative Risk: **667.33**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 140.02 | **LOC:** 238 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.3794%), Tech Debt (97.8654%)
- **Heaviest Functions:** `add_constraint` (Impact: 18.8), `requires_recreate_in_batch` (Impact: 16.9), `_guess_if_default_is_unparenthesized_sql_expr` (Impact: 16.6)

### 4. `alembic-1.18.4/alembic/operations/ops.py` (PYTHON) -> Cumulative Risk: **651.77**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1027.02 | **LOC:** 2919 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.813%), Documentation (93.75%), Safety Score (89.6339%)
- **Heaviest Functions:** `create_foreign_key` (Impact: 20.2), `from_constraint` (Impact: 19.3), `batch_create_foreign_key` (Impact: 17.6)

### 5. `alembic-1.18.4/alembic/ddl/mssql.py` (PYTHON) -> Cumulative Risk: **649.37**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 340.84 | **LOC:** 524 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.8189%), Tech Debt (98.1993%)
- **Heaviest Functions:** `alter_column` (Impact: 77.2), `_compare_identity_default` (Impact: 12.8), `visit_column_comment` (Impact: 11.2)

### 6. `alembic-1.18.4/alembic/ddl/_autogen.py` (PYTHON) -> Cumulative Risk: **647.92**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 177.22 | **LOC:** 330 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.5783%), Documentation (90.7692%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 33.9), `__init__` (Impact: 5.0), `column_names_optional` (Impact: 3.0)

### 7. `alembic-1.18.4/alembic/autogenerate/compare/util.py` (PYTHON) -> Cumulative Risk: **644.67**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 230.34 | **LOC:** 315 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.929%), Safety Score (84.1292%)
- **Heaviest Functions:** `_return_from_cache` (Impact: 38.9), `_pre_cache` (Impact: 31.2), `_apply_reflectinfo_conv` (Impact: 12.6)

### 8. `alembic-1.18.4/alembic/ddl/base.py` (PYTHON) -> Cumulative Risk: **640.27**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 244.88 | **LOC:** 407 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.5371%), Api Exposure (85.2249%)
- **Heaviest Functions:** `add_column` (Impact: 39.6), `__init__` (Impact: 10.0), `drop_column` (Impact: 7.1)

### 9. `alembic-1.18.4/alembic/ddl/impl.py` (PYTHON) -> Cumulative Risk: **639.27**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 620.64 | **LOC:** 922 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.95%), Documentation (91.3978%), Safety Score (90.1254%)
- **Heaviest Functions:** `alter_column` (Impact: 59.4), `_exec` (Impact: 41.4), `bulk_insert` (Impact: 33.2)

### 10. `alembic-1.18.4/alembic/runtime/migration.py` (PYTHON) -> Cumulative Risk: **637.06**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 775.06 | **LOC:** 1347 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9894%), Safety Score (82.8868%), Verification (80.0%)
- **Heaviest Functions:** `configure` (Impact: 29.7), `run_migrations` (Impact: 27.8), `__init__` (Impact: 26.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `alembic-1.18.4/alembic/script/revision.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1354.12 | **LOC:** 1729 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.9998%), Tech Debt (11.8727%)
**Top Internal Functions/Classes:**
  * `_parse_downgrade_target` (Impact: 64.1)
  * `_parse_upgrade_target` (Impact: 61.4)
  * `_collect_upgrade_revisions` (Impact: 60.6)
  * `_collect_downgrade_revisions` (Impact: 58.0)
  * `_walk` (Impact: 52.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 141 instances
* *State Mutation (weighted view):* 461
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 226`, `args: 69`, `func_start: 65`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 179`, `dead_code: 1`, `planned_debt: 11`
* *Architecture:* `io: 1`, `api: 37`, `import: 26`
* *Defense:* `safety: 38`, `doc: 33`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 42.795
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.220604
  * `Imports (Out-Degree: 0):` .., ..util, __future__, collections, re, sqlalchemy, typing
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_autogen_diffs.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1246.4 | **LOC:** 2686 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.8733%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_drop_fk_with_mixed_case_name` (Impact: 30.2)
    * *Intent:* """Test #1743"""
  * `test_include_object` (Impact: 22.3)
  * `include_object` (Impact: 20.4)
  * `test_include_name` (Impact: 17.5)
  * `test_compare_metadata_include_name` (Impact: 15.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 411
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 406`, `args: 138`, `func_start: 138`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 303`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 8`
* *Architecture:* `io: 41`, `api: 148`, `import: 67`
* *Defense:* `safety: 17`, `doc: 16`, `test: 89`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.53
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` alembic, alembic.autogenerate, alembic.autogenerate.compare.tables, alembic.autogenerate.compare.types, alembic.autogenerate.compare.util, alembic.ddl, alembic.migration, alembic.operations...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/autogenerate/render.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1125.72 | **LOC:** 1173 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.7322%), Tech Debt (8.7486%)
**Top Internal Functions/Classes:**
  * `_repr_type` (Impact: 40.1)
  * `_alter_column` (Impact: 32.5)
  * `_uq_constraint` (Impact: 32.1)
  * `_add_table` (Impact: 30.5)
  * `_render_column` (Impact: 30.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 156 instances
* *State Mutation (weighted view):* 495
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 235`, `args: 50`, `func_start: 50`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 183`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 30`, `api: 26`, `import: 43`
* *Defense:* `safety: 20`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.638
  * `Choke Point (Betweenness):` 0.000347 | `Ripple Effect (Closeness):` 0.022222
  * `Imports (Out-Degree: 4):` .., ..operations, ..util, __future__, alembic.autogenerate.api, alembic.config, alembic.operations.ops, io...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_autogen_render.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1113.88 | **LOC:** 2723 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.656%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_repr_custom_type` (Impact: 19.6)
    * *Intent:* """test #1167 as well as other user defined type variations"""
  * `render` (Impact: 16.8)
  * `test_render_custom` (Impact: 13.7)
  * `test_render_create_table_comment_op_batch` (Impact: 13.6)
    * *Intent:* """test #1361"""
  * `test_render_drop_table_comment_op_batch` (Impact: 13.5)
    * *Intent:* """test #1361"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *Amplified Sql Injection:* 1 instances
* *State Mutation (weighted view):* 439
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 324`, `args: 169`, `func_start: 166`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 399`, `duplicate_logic: 3`, `unreferenced_by_name: 153`
* *Architecture:* `io: 39`, `api: 173`, `import: 54`
* *Defense:* `safety: 4`, `doc: 28`, `test: 157`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.53
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` alembic, alembic.autogenerate, alembic.migration, alembic.operations, alembic.testing, alembic.testing.fixtures, alembic.util, mypackage...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/tests/test_batch.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1039.7 | **LOC:** 2580 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.9709%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_assert_impl` (Impact: 50.0)
  * `test_change_type_int_to_boolean` (Impact: 11.2)
  * `test_add_col_table_has_native_boolean` (Impact: 10.4)
  * `_multi_fk_fixture` (Impact: 7.9)
  * `_literal_ck_fixture` (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 338
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 528`, `args: 177`, `func_start: 177`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 260`, `duplicate_logic: 12`, `unreferenced_by_name: 100`
* *Architecture:* `io: 26`, `api: 148`, `import: 55`
* *Defense:* `safety: 35`, `doc: 8`, `test: 137`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.53
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` alembic, alembic.ddl, alembic.operations, alembic.operations.batch, alembic.runtime.migration, alembic.script, alembic.testing, alembic.testing.env...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/operations/ops.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1027.02 | **LOC:** 2919 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.8915%), Tech Debt (12.5692%)
**Top Internal Functions/Classes:**
  * `create_foreign_key` (Impact: 20.2)
  * `from_constraint` (Impact: 19.3)
  * `batch_create_foreign_key` (Impact: 17.6)
  * `reverse` (Impact: 17.1)
  * `to_table` (Impact: 16.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *Amplified Sql Injection:* 1 instances
* *State Mutation (weighted view):* 349
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 349`, `args: 124`, `func_start: 124`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 86`, `state_mutation: 223`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 21`, `api: 125`, `import: 49`
* *Defense:* `safety: 7`, `doc: 62`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 69.132
  * `Choke Point (Betweenness):` 0.010276 | `Ripple Effect (Closeness):` 0.255183
  * `Imports (Out-Degree: 4):` , .., ..autogenerate.rewriter, ..ddl.base, ..runtime.migration, ..script.revision, ..util, .base...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_autogen_indexes.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 870.74 | **LOC:** 2135 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.0183%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_remove_connection_uq` (Impact: 18.9)
  * `test_remove_connection_index` (Impact: 18.5)
  * `include_object` (Impact: 15.2)
  * `test_drop_table_w_uq_constraint` (Impact: 13.2)
  * `include_object` (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 199`, `args: 161`, `func_start: 83`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 252`, `dead_code: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 57`
* *Architecture:* `io: 20`, `api: 88`, `import: 36`
* *Defense:* `safety: 17`, `doc: 8`, `test: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.53
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` alembic, alembic.operations.base, alembic.testing, alembic.testing.assertions, alembic.testing.env, alembic.testing.suite._autogen_fixtures, alembic.util, contextlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/tests/test_op.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 822.5 | **LOC:** 1770 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.5584%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_generic_alter_column_type_and_nullability` (Impact: 11.1)
  * `test_alter_column_schema_type_unnamed` (Impact: 10.0)
  * `test_add_column_primary_key` (Impact: 9.9)
  * `test_add_foreign_key_dialect_kw` (Impact: 7.7)
  * `test_alter_column_computed_not_supported` (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *Amplified Sql Injection:* 7 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 280`, `args: 175`, `func_start: 162`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 220`, `planned_debt: 4`
* *Architecture:* `io: 22`, `api: 166`, `concurrency: 3`, `import: 41`
* *Defense:* `safety: 10`, `doc: 11`, `test: 156`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.53
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` alembic, alembic.operations, alembic.operations.toimpl, alembic.testing, alembic.testing.assertions, alembic.testing.fixtures, alembic.util, sqlalchemy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/script/base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 822.48 | **LOC:** 1053 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.7284%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generate_revision` (Impact: 123.6)
  * `_head_only` (Impact: 57.5)
  * `_from_path` (Impact: 38.6)
  * `_stamp_revs` (Impact: 32.6)
  * `_catch_revision_errors` (Impact: 28.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 198`, `args: 40`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 104`, `dead_code: 2`
* *Architecture:* `io: 10`, `api: 27`, `import: 36`
* *Defense:* `safety: 24`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.067
  * `Choke Point (Betweenness):` 0.000163 | `Ripple Effect (Closeness):` 0.008333
  * `Imports (Out-Degree: 4):` , .., ..config, ..runtime, ..runtime.migration, ..util, ..util.pyfiles, .revision...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/alembic/autogenerate/compare/constraints.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 808.7 | **LOC:** 813 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.9532%), Tech Debt (8.7467%)
**Top Internal Functions/Classes:**
  * `_compare_indexes_and_uniques` (Impact: 236.4)
  * `_compare_foreign_keys` (Impact: 104.1)
  * `_correct_for_uq_duplicates_uix` (Impact: 45.4)
  * `_compare_nullable` (Impact: 24.7)
  * `_make_foreign_key` (Impact: 22.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 271
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 114`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 97`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `io: 13`, `api: 4`, `import: 37`
* *Defense:* `safety: 14`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.837
  * `Choke Point (Betweenness):` 0.000271 | `Ripple Effect (Closeness):` 0.008333
  * `Imports (Out-Degree: 6):` ..., ...autogenerate.api, ...ddl._autogen, ...ddl.impl, ...operations, ...operations.ops, ...runtime.plugins, ...util...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_postgresql.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 808.58 | **LOC:** 1894 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.1281%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_compare_default_roundtrip` (Impact: 12.1)
  * `test_add_identity_to_column` (Impact: 10.7)
  * `test_add_column_identity` (Impact: 10.6)
  * `test_toggle_not_distinct` (Impact: 10.1)
  * `test_add` (Impact: 10.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *Amplified Sql Injection:* 6 instances
* *State Mutation (weighted view):* 272
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 324`, `args: 180`, `func_start: 132`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 202`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 4`, `unreferenced_by_name: 108`
* *Architecture:* `io: 37`, `api: 134`, `import: 65`
* *Defense:* `safety: 15`, `doc: 12`, `test: 106`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.53
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` alembic, alembic.autogenerate, alembic.autogenerate.compare.server_defaults, alembic.autogenerate.compare.tables, alembic.migration, alembic.operations, alembic.script, alembic.testing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/runtime/migration.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 775.06 | **LOC:** 1347 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.1426%), Tech Debt (8.4659%)
**Top Internal Functions/Classes:**
  * `configure` (Impact: 29.7)
  * `run_migrations` (Impact: 27.8)
  * `__init__` (Impact: 26.5)
  * `begin_transaction` (Impact: 25.7)
  * `autocommit_block` (Impact: 20.2)
    * *Intent:* """Enter an "autocommit" block, for databases that support AUTOCOMMIT isolation levels. This special...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 70 instances
* *Amplified Sql Injection:* 1 instances
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 286`, `args: 81`, `func_start: 81`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 102`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 14`, `api: 69`, `import: 41`
* *Defense:* `safety: 33`, `doc: 27`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.778
  * `Choke Point (Betweenness):` 0.007214 | `Ripple Effect (Closeness):` 0.165119
  * `Imports (Out-Degree: 4):` .., ..config, ..script.base, ..script.revision, ..util, ..util.compat, .environment, __future__...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_command.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 766.22 | **LOC:** 1709 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.7267%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_assert_sql` (Impact: 21.3)
  * `test_help_text` (Impact: 16.0)
  * `_eq_cmd_output` (Impact: 11.2)
  * `test_init_file_exists_and_is_empty` (Impact: 9.7)
  * `test_init_custom_template_location` (Impact: 9.1)
    * *Intent:* """test #1660"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *Amplified Sql Injection:* 1 instances
* *State Mutation (weighted view):* 220
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 433`, `args: 142`, `func_start: 142`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 162`, `dead_code: 1`, `planned_debt: 4`, `duplicate_logic: 15`, `unreferenced_by_name: 96`
* *Architecture:* `io: 44`, `api: 146`, `import: 45`
* *Defense:* `safety: 59`, `doc: 16`, `test: 120`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.53
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` alembic, alembic.script, alembic.testing, alembic.testing.env, alembic.testing.fixtures, alembic.util, alembic.util.sqla_compat, configparser...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/operations/batch.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 682.12 | **LOC:** 721 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.9788%), Tech Debt (9.6653%)
**Top Internal Functions/Classes:**
  * `alter_column` (Impact: 50.2)
  * `_setup_dependencies_for_add_column` (Impact: 47.1)
  * `_grab_table_elements` (Impact: 24.9)
  * `_setup_referent` (Impact: 21.8)
  * `drop_constraint` (Impact: 20.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 294
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 155`, `args: 39`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 118`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 18`, `api: 30`, `import: 41`
* *Defense:* `safety: 20`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.769
  * `Choke Point (Betweenness):` 0.0007 | `Ripple Effect (Closeness):` 0.079167
  * `Imports (Out-Degree: 3):` ..ddl.base, ..ddl.impl, ..util, ..util.sqla_compat, __future__, sqlalchemy, sqlalchemy.engine, sqlalchemy.sql.elements...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/alembic/ddl/impl.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 620.64 | **LOC:** 922 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.2477%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `alter_column` (Impact: 59.4)
  * `_exec` (Impact: 41.4)
  * `bulk_insert` (Impact: 33.2)
  * `compare_indexes` (Impact: 20.1)
  * `_column_args_match` (Impact: 19.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *Amplified Sql Injection:* 1 instances
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 209`, `args: 49`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 71`, `dead_code: 1`
* *Architecture:* `io: 25`, `api: 42`, `import: 54`
* *Defense:* `safety: 13`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.66
  * `Choke Point (Betweenness):` 0.005875 | `Ripple Effect (Closeness):` 0.10744
  * `Imports (Out-Degree: 4):` , .., ..autogenerate.api, ..operations.batch, ..util, ._autogen, .base, __future__...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_revision.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 612.96 | **LOC:** 1684 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.2751%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_assert_iteration` (Impact: 19.8)
  * `test_all` (Impact: 9.5)
  * `test_no_revision_exists` (Impact: 6.5)
  * `test_partial_id_resolve_too_short` (Impact: 4.7)
  * `test_ancestor_nodes` (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 210`, `args: 200`, `func_start: 152`, `class_start: 19`
* *Risk/State:* `state_mutation: 75`, `dead_code: 1`, `unreferenced_by_name: 123`
* *Architecture:* `io: 1`, `api: 165`, `import: 14`
* *Defense:* `safety: 3`, `doc: 2`, `test: 130`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.53
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` , alembic.script.revision, alembic.testing, alembic.testing.fixtures, sqlalchemy.testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/ddl/postgresql.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 598.96 | **LOC:** 865 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.9317%), Tech Debt (91.4296%)
**Top Internal Functions/Classes:**
  * `_exclude_constraint` (Impact: 33.0)
  * `_cleanup_index_expr` (Impact: 31.6)
  * `compare_indexes` (Impact: 30.9)
  * `autogen_column_reflect` (Impact: 28.7)
  * `compare_server_default` (Impact: 27.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 233
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 229`, `args: 34`, `func_start: 34`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 97`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 21`
* *Architecture:* `io: 32`, `api: 23`, `import: 66`
* *Defense:* `safety: 9`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.228
  * `Choke Point (Betweenness):` 0.000805 | `Ripple Effect (Closeness):` 0.016667
  * `Imports (Out-Degree: 6):` .., ..autogenerate, ..autogenerate.api, ..autogenerate.render, ..operations, ..operations.base, ..runtime.migration, ..util...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_script_production.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 572.0 | **LOC:** 1593 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.3386%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_reordering_example_wo_copy` (Impact: 11.6)
    * *Intent:* """test related to #1692 in that we identified the recipe for rewriting column ordering was using co...
  * `order_columns` (Impact: 11.3)
  * `test_file_template_with_directory_path` (Impact: 11.0)
  * `test_create_script_branches_old_template` (Impact: 8.4)
  * `_test_tz` (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 287`, `args: 97`, `func_start: 92`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 149`, `duplicate_logic: 12`, `unreferenced_by_name: 47`
* *Architecture:* `io: 63`, `api: 93`, `import: 49`
* *Defense:* `safety: 29`, `doc: 13`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.53
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` alembic, alembic.environment, alembic.operations, alembic.script, alembic.testing, alembic.testing.env, alembic.testing.fixtures, alembic.util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/tests/test_version_traversal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 570.78 | **LOC:** 1526 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.8405%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_downgrade_branch_dependency` (Impact: 5.6)
    * *Intent:* """c2branch depends on c1branch so taking down c1branch requires taking down both"""
  * `_assert_downgrade` (Impact: 5.3)
  * `_assert_upgrade` (Impact: 5.3)
  * `test_upgrade` (Impact: 4.1)
  * `setup_class` (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 197
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 162`, `args: 107`, `func_start: 107`, `class_start: 17`
* *Risk/State:* `state_mutation: 171`, `duplicate_logic: 16`, `unreferenced_by_name: 63`
* *Architecture:* `api: 122`, `import: 10`
* *Defense:* `safety: 5`, `doc: 24`, `test: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.53
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` alembic, alembic.migration, alembic.testing, alembic.testing.env, alembic.testing.fixtures
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/config.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 552.78 | **LOC:** 1052 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.3956%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_inis_from_config` (Impact: 27.9)
  * `__init__` (Impact: 20.3)
  * `_inspect_function` (Impact: 18.8)
  * `_generate_args` (Impact: 18.4)
  * `get_prepend_sys_paths_list` (Impact: 14.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 236
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 151`, `args: 39`, `func_start: 39`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 82`
* *Architecture:* `io: 8`, `api: 34`, `import: 27`
* *Defense:* `safety: 12`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 46.1
  * `Choke Point (Betweenness):` 0.019229 | `Ripple Effect (Closeness):` 0.26534
  * `Imports (Out-Degree: 1):` , .util, .util.pyfiles, __future__, alembic, alembic.config, argparse, configparser...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/alembic/command.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 523.52 | **LOC:** 849 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.2288%), Tech Debt (57.0308%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 65.6)
  * `history` (Impact: 41.4)
  * `revision` (Impact: 37.5)
  * `stamp` (Impact: 27.7)
  * `current` (Impact: 13.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 104`, `args: 29`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 56`, `dead_code: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 9`
* *Architecture:* `io: 12`, `api: 26`, `import: 16`
* *Defense:* `safety: 4`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.53
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` , .runtime.environment, .script, .util, __future__, alembic.config, alembic.script.base, alembic.script.revision...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/tests/test_script_consumption.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 468.88 | **LOC:** 1221 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.6038%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_setup_revision_files` (Impact: 19.0)
  * `_assert_setup` (Impact: 16.6)
  * `test_steps` (Impact: 11.7)
  * `_opened_transaction_fixture` (Impact: 10.9)
  * `_setup_for_fixture` (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 239`, `args: 64`, `func_start: 64`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 123`, `dead_code: 1`, `duplicate_logic: 7`, `unreferenced_by_name: 27`
* *Architecture:* `io: 19`, `api: 65`, `import: 37`
* *Defense:* `safety: 58`, `doc: 18`, `test: 35`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.53
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, alembic, alembic.config, alembic.environment, alembic.script, alembic.testing, alembic.testing.env, alembic.testing.fixtures...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/ddl/mysql.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 457.3 | **LOC:** 527 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.8509%), Tech Debt (86.7843%)
**Top Internal Functions/Classes:**
  * `alter_column` (Impact: 170.9)
  * `compare_server_default` (Impact: 52.3)
  * `correct_for_autogen_constraints` (Impact: 26.3)
  * `correct_for_autogen_foreignkeys` (Impact: 21.4)
  * `_mysql_colspec` (Impact: 19.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 110`, `args: 15`, `func_start: 15`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 33`, `dead_code: 1`, `planned_debt: 3`, `unreferenced_by_name: 11`
* *Architecture:* `io: 10`, `api: 11`, `import: 31`
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.804
  * `Choke Point (Betweenness):` 0.001045 | `Ripple Effect (Closeness):` 0.025
  * `Imports (Out-Degree: 3):` .., ..util, ..util.sqla_compat, .base, .impl, __future__, re, sqlalchemy...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `alembic-1.18.4/tests/test_config.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 385.58 | **LOC:** 779 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.3129%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_bool` (Impact: 24.3)
  * `test_truncate_slug_length_types` (Impact: 24.1)
  * `test_prepend_sys_path_locations` (Impact: 19.5)
  * `test_version_locations` (Impact: 17.0)
  * `test_write_hooks` (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 132`, `args: 39`, `func_start: 39`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 96`, `duplicate_logic: 3`, `unreferenced_by_name: 32`
* *Architecture:* `io: 18`, `api: 45`, `import: 25`
* *Defense:* `safety: 15`, `doc: 10`, `test: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.53
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` alembic, alembic.migration, alembic.operations, alembic.script, alembic.testing, alembic.testing.assertions, alembic.testing.env, alembic.testing.fixtures...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alembic-1.18.4/alembic/operations/base.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 372.1 | **LOC:** 2002 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.1642%), Tech Debt (12.4603%)
**Top Internal Functions/Classes:**
  * `register_operation` (Impact: 20.9)
  * `register` (Impact: 15.1)
  * `create_foreign_key` (Impact: 11.1)
  * `run_async` (Impact: 10.9)
  * `batch_alter_table` (Impact: 10.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 16 instances
* *Amplified Sql Injection:* 2 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 184`, `args: 51`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 52`, `high_risk_execution: 1`, `state_mutation: 32`, `planned_debt: 5`
* *Architecture:* `io: 12`, `api: 53`, `concurrency: 1`, `import: 60`
* *Defense:* `safety: 2`, `doc: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.379
  * `Choke Point (Betweenness):` 0.001998 | `Ripple Effect (Closeness):` 0.025
  * `Imports (Out-Degree: 7):` , .., ..ddl, ..ddl.base, ..runtime.migration, ..util, ..util.compat, ..util.sqla_compat...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `alembic-1.18.4/alembic/autogenerate/api.py` -> **Severity: 2.549** (Bridge: 0.0255 * Flux: 99.9995%)
- `alembic-1.18.4/alembic/config.py` -> **Severity: 1.923** (Bridge: 0.0192 * Flux: 99.9992%)
- `alembic-1.18.4/alembic/autogenerate/compare/schema.py` -> **Severity: 1.857** (Bridge: 0.0186 * Flux: 99.9932%)
- `alembic-1.18.4/alembic/util/pyfiles.py` -> **Severity: 1.639** (Bridge: 0.0164 * Flux: 100.0%)
- `alembic-1.18.4/alembic/autogenerate/compare/types.py` -> **Severity: 1.558** (Bridge: 0.0156 * Flux: 99.9169%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `alembic-1.18.4/alembic/config.py` -> **Severity: 24.555** (Embedded: 0.2653 * Error Risk: 92.5424%)
- `alembic-1.18.4/alembic/autogenerate/compare/schema.py` -> **Severity: 23.74** (Embedded: 0.303 * Error Risk: 78.3421%)
- `alembic-1.18.4/alembic/autogenerate/api.py` -> **Severity: 23.722** (Embedded: 0.254 * Error Risk: 93.4036%)
- `alembic-1.18.4/alembic/operations/ops.py` -> **Severity: 22.873** (Embedded: 0.2552 * Error Risk: 89.6339%)
- `alembic-1.18.4/alembic/testing/fixtures.py` -> **Severity: 22.169** (Embedded: 0.2333 * Error Risk: 95.0096%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `alembic-1.18.4/alembic/autogenerate/compare/types.py` -> **Severity: 9304.6** (Blast Radius: 93.046 * Doc Risk: 100.0%)
- `alembic-1.18.4/alembic/autogenerate/compare/schema.py` -> **Severity: 8286.2** (Blast Radius: 82.862 * Doc Risk: 100.0%)
- `alembic-1.18.4/alembic/operations/ops.py` -> **Severity: 6481.125** (Blast Radius: 69.132 * Doc Risk: 93.75%)
- `alembic-1.18.4/alembic/autogenerate/api.py` -> **Severity: 4612.828** (Blast Radius: 56.379 * Doc Risk: 81.8182%)
- `alembic-1.18.4/alembic/runtime/plugins.py` -> **Severity: 3825.735** (Blast Radius: 57.386 * Doc Risk: 66.6667%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
