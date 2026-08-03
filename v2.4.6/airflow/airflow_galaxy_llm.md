# ARCHITECTURAL_BRIEF: airflow
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/airflow` |
| **Timestamp** | `2026-08-03T19:34:45.928021+00:00` |
| **Scan Duration** | `34.45s` |
| **Git Branch** | `main` |
| **Git Commit** | `f391942b90f2347272c321bcdd092c7b109cdc9e` |
| **Git Remote** | `https://github.com/apache/airflow.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 7471 malicious artifacts.

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
| Total Artifacts | 12060 |
| Analyzed Artifacts (Scanned) | 8706 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3354 |
| Total LOC | 1001276 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 72.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1342 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 514 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 6523 | 864288 | 74.9% |
| TYPESCRIPT | 767 | 49376 | 8.8% |
| JSON | 378 | 39769 | 4.3% |
| PLAINTEXT | 306 | 0 | 3.5% |
| YAML | 288 | 24831 | 3.3% |
| XML | 125 | 6 | 1.4% |
| MARKDOWN | 106 | 0 | 1.2% |
| SHELL | 75 | 3524 | 0.9% |
| JAVASCRIPT | 48 | 3481 | 0.6% |
| GO | 36 | 2372 | 0.4% |
| HTML | 18 | 567 | 0.2% |
| SQLITE | 11 | 54 | 0.1% |
| CSS | 10 | 10954 | 0.1% |
| DOCKERFILE | 9 | 1866 | 0.1% |
| CSV | 4 | 108 | 0.0% |
| PROTO | 1 | 46 | 0.0% |
| JAVA | 1 | 34 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.501`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 5179 | 59.5% |
| file_cluster_13 | 2499 | 28.7% |
| file_cluster_0 | 204 | 2.3% |
| file_cluster_16 | 170 | 2.0% |
| file_cluster_2 | 84 | 1.0% |
| file_cluster_4 | 78 | 0.9% |
| file_cluster_17 | 35 | 0.4% |
| file_cluster_12 | 23 | 0.3% |
| file_cluster_9 | 4 | 0.0% |
| file_cluster_6 | 4 | 0.0% |
| file_cluster_1 | 4 | 0.0% |
| file_cluster_11 | 3 | 0.0% |
| file_cluster_7 | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 412 | 4.7% |
| Static: Minified & Vendor Opaque Mass | 5 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3354*

**Composition by Extension & Reason:**
- `.rst`: 1325x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 172x Excluded (Unsupported Extension: '.rst')
- `.png`: 510x Excluded (Explicitly Denied Extension: '.png')
- `.py`: 399x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 76 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 2072 LOC)
- `no_extension`: 289x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 12x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.kubernetes-helm-yaml')
- `.txt`: 133x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 95x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 75 LOC)
- `.yml`: 63x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 2970 LOC)
- `.svg`: 46x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 6240 LOC), 1x Excluded (Massive Static Asset Blob: 3631 LOC)
- `.jinja2`: 31x Unsupported Format (.jinja2), 4x Excluded (Unsupported Extension: '.jinja2')
- `.md`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 146 LOC), 1x Excluded (Machine-Generated Source Code Signature: 175 LOC)
- `.go`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 313 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1122 LOC)
- `.njk`: 20x Unsupported Format (.njk)
- `.sh`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 6x Excluded (Saturation: Line 4 exceeds 500 chars), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.json`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 14452 LOC), 1x Excluded (Massive Static Asset Blob: 2617 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 10.0 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 8.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 8.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.9 | 0.2 | 0.0 |
| API Exposure | 0.0 | 18.8 | 3.0 | 2.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 13.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.6 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 74.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.7 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 8.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 25.6 | 0.8 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 34.6 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 23.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `task-sdk/tests/task_sdk/api/test_client.py` (Hits: 326)
- `airflow-ctl/tests/airflow_ctl/api/test_operations.py` (Hits: 282)
- `task-sdk/tests/task_sdk/execution_time/test_supervisor.py` (Hits: 112)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **sdk.py** (`providers/common/compat/src/airflow/providers/common/compat/sdk.py`) — 1201 inbound connections
2. **json.py** (`airflow-core/src/airflow/utils/json.py`) — 535 inbound connections
3. **models.go** (`go-sdk/pkg/api/models.go`) — 475 inbound connections
4. **system_tests.py** (`devel-common/src/tests_common/test_utils/system_tests.py`) — 448 inbound connections
5. **dag.py** (`airflow-core/src/airflow/models/dag.py`) — 413 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **pytest_plugin.py** (`devel-common/src/tests_common/pytest_plugin.py`) — 106 outbound dependencies
2. **test_dag_serialization.py** (`airflow-core/tests/unit/serialization/test_dag_serialization.py`) — 85 outbound dependencies
3. **test_scheduler_job.py** (`airflow-core/tests/unit/jobs/test_scheduler_job.py`) — 82 outbound dependencies
4. **scheduler_job_runner.py** (`airflow-core/src/airflow/jobs/scheduler_job_runner.py`) — 78 outbound dependencies
5. **dag.py** (`task-sdk/src/airflow/sdk/definitions/dag.py`) — 78 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_parse_sgr_mouse` (@ `dev/breeze/src/airflow_breeze/utils/tui_display.py`) -> Impact: **7217.6** | LOC: 1833
- `_ensure_ti_has_dag_version_id` (@ `airflow-core/src/airflow/jobs/scheduler_job_runner.py`) -> Impact: **6053.4** | LOC: 2909
- `get_all_provider_pyproject_toml_provider` (@ `devel-common/src/tests_common/pytest_plugin.py`) -> Impact: **5090.3** | LOC: 2629
- `startup` (@ `task-sdk/src/airflow/sdk/execution_time/task_runner.py`) -> Impact: **2724.3** | LOC: 1007
- `default_serialization` (@ `airflow-core/src/airflow/serialization/serialized_objects.py`) -> Impact: **2626.6** | LOC: 1572
- `test_only_idle_no_dags_exits_after_n_idl` (@ `airflow-core/tests/unit/jobs/test_scheduler_job.py`) -> Impact: **2430.3** | LOC: 4927
- `_read_requires_python` (@ `dev/ide_setup/setup_idea.py`) -> Impact: **2165.7** | LOC: 754
  * *Intent:* """Return the ``requires-python`` value from *pyproject_path*."""
- `_fetch_remote_logging_conn` (@ `task-sdk/src/airflow/sdk/execution_time/supervisor.py`) -> Impact: **1796.9** | LOC: 1020
- `wait_until_job_complete` (@ `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/hooks/kubernetes.py`) -> Impact: **1716.8** | LOC: 527
- `_get_field` (@ `providers/snowflake/src/airflow/providers/snowflake/hooks/snowflake.py`) -> Impact: **1627.1** | LOC: 622

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `init` (@ `airflow-core/src/airflow/api_fastapi/auth/managers/simple/simple_auth_manager.py`) -> **O(2^N) [Recursive]**
- `_validate_executor_fields` (@ `airflow-core/src/airflow/dag_processing/dagbag.py`) -> **O(2^N) [Recursive]**
- `_timeout` (@ `airflow-core/src/airflow/dag_processing/importers/python_importer.py`) -> **O(2^N) [Recursive]**
- `_get_observed_filelocs` (@ `airflow-core/src/airflow/dag_processing/manager.py`) -> **O(2^N) [Recursive]**
- `_get_log_dir` (@ `airflow-core/src/airflow/dag_processing/manager.py`) -> **O(2^N) [Recursive]**
- `_ensure_ti_has_dag_version_id` (@ `airflow-core/src/airflow/jobs/scheduler_job_runner.py`) -> **O(2^N) [Recursive]**
- `_sort_serialized_dag_dict` (@ `airflow-core/src/airflow/models/serialized_dag.py`) -> **O(2^N) [Recursive]**
- `to_downstream` (@ `airflow-core/src/airflow/partition_mappers/chain.py`) -> **O(2^N) [Recursive]**
- `get_flask_plugins` (@ `airflow-core/src/airflow/plugins_manager.py`) -> **O(2^N) [Recursive]**
- `filter_task_group` (@ `airflow-core/src/airflow/serialization/definitions/dag.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Make sure to not recursively deepcopy the dag or task_group while copying the task. # task_group is reset later

### Highest Data Gravity (Database Complexity)
- `test_validate_executor_fields_does_not_a` (@ `airflow-core/tests/unit/dag_processing/test_dagbag.py`) -> DB Complexity: **226**
- `get_all_provider_pyproject_toml_provider` (@ `devel-common/src/tests_common/pytest_plugin.py`) -> DB Complexity: **225**
- `_parse_sgr_mouse` (@ `dev/breeze/src/airflow_breeze/utils/tui_display.py`) -> DB Complexity: **203**
- `test_only_idle_no_dags_exits_after_n_idl` (@ `airflow-core/tests/unit/jobs/test_scheduler_job.py`) -> DB Complexity: **172**
- `execute` (@ `providers/google/src/airflow/providers/google/cloud/operators/dlp.py`) -> DB Complexity: **151**
- `determine_airflow_to_use_[Truncated]` (@ `scripts/docker/entrypoint_ci.sh`) -> DB Complexity: **148**
  * *Intent:* # Determine which airflow version to use
- `Anonymous_Block_[Truncated]` (@ `scripts/docker/install_os_dependencies.sh`) -> DB Complexity: **144**
- `set_pythonpath_for_root_user_[Truncated]` (@ `scripts/docker/entrypoint_prod.sh`) -> DB Complexity: **135**
- `test_run_command` (@ `airflow-core/tests/unit/core/test_configuration.py`) -> DB Complexity: **130**
- `_fetch_remote_logging_conn` (@ `task-sdk/src/airflow/sdk/execution_time/supervisor.py`) -> DB Complexity: **123**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `dev/breeze/src/airflow_breeze/utils` | 61 | 25029.74 | 14.92% | 4.01% |
| `providers/google/src/airflow/providers/google/cloud/operators` | 43 | 23251.71 | 15.2% | 68.76% |
| `providers/amazon/src/airflow/providers/amazon/aws/operators` | 35 | 12223.51 | 16.45% | 38.6% |
| `scripts/ci/prek` | 112 | 11803.74 | 18.78% | 5.54% |
| `providers/google/tests/unit/google/cloud/hooks` | 49 | 10782.1 | 9.04% | 0.0% |
| `airflow-core/tests/unit/models` | 29 | 10340.56 | 2.94% | 0.0% |
| `dev/breeze/src/airflow_breeze/commands` | 38 | 10271.08 | 9.11% | 2.02% |
| `airflow-core/tests/unit/utils` | 37 | 10039.12 | 8.48% | 0.0% |
| `providers/google/src/airflow/providers/google/cloud/hooks` | 47 | 9965.0 | 9.82% | 21.14% |
| `providers/google/tests/unit/google/cloud/operators` | 44 | 9771.56 | 4.9% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `airflow-core/src/airflow/api_fastapi/common/exceptions.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api_fastapi/core_api/datamodels/config.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/assets/evaluation.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/config_templates/default_webserver_config.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/example_dags/example_dynamic_task_mapping_with_no_taskflow_operators.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `providers/amazon/src/airflow/providers/amazon/aws/executors/aws_lambda/docker/Dockerfile` -> **100.0%** Exposure
- `airflow-core/src/airflow/api_fastapi/auth/managers/simple/user.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/executors/executor_utils.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/models/log.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/utils/dag_version_inflation_checker.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `airflow-core/tests/unit/api_fastapi/core_api/routes/public/test_task_instances.py` -> **61** Orphaned Functions | **87** Duplicates
- `airflow-core/tests/unit/models/test_taskinstance.py` -> **87** Orphaned Functions | **12** Duplicates
- `providers/databricks/tests/unit/databricks/operators/test_databricks.py` -> **50** Orphaned Functions | **47** Duplicates
- `airflow-core/tests/unit/api_fastapi/execution_api/versions/head/test_task_instances.py` -> **66** Orphaned Functions | **30** Duplicates
- `providers/databricks/tests/unit/databricks/hooks/test_databricks_base.py` -> **89** Orphaned Functions | **7** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`Dockerfile`** -> AI Confidence: **99.48%**
2. **`airflow-core/src/airflow/ui/src/components/Clear/TaskInstance/ClearTaskInstanceConfirmationDialog.tsx`** -> AI Confidence: **99.48%**
3. **`dev/breeze/src/airflow_breeze/commands/pr_commands.py`** -> AI Confidence: **99.39%**
4. **`scripts/ci/prek/check_common_compat_lazy_imports.py`** -> AI Confidence: **99.39%**
5. **`airflow-core/src/airflow/ui/src/layouts/Details/DagBreadcrumb.tsx`** -> AI Confidence: **99.39%**
6. **`airflow-core/src/airflow/ui/src/layouts/Details/TaskStreamFilter.tsx`** -> AI Confidence: **99.39%**
7. **`airflow-core/src/airflow/ui/src/pages/TaskInstance/Details.tsx`** -> AI Confidence: **99.39%**
8. **`airflow-core/src/airflow/ui/src/pages/Dag/Code/Code.tsx`** -> AI Confidence: **99.35%**
9. **`scripts/ci/prek/mypy_folder.py`** -> AI Confidence: **99.34%**
10. **`airflow-core/src/airflow/api/common/mark_tasks.py`** -> AI Confidence: **99.31%**
11. **`airflow-core/src/airflow/api_fastapi/core_api/routes/public/task_instances.py`** -> AI Confidence: **99.31%**
12. **`airflow-core/src/airflow/api_fastapi/core_api/routes/ui/partitioned_dag_runs.py`** -> AI Confidence: **99.31%**
13. **`airflow-core/src/airflow/api_fastapi/core_api/services/public/connections.py`** -> AI Confidence: **99.31%**
14. **`airflow-core/src/airflow/api_fastapi/core_api/services/public/task_instances.py`** -> AI Confidence: **99.31%**
15. **`airflow-core/src/airflow/api_fastapi/core_api/services/public/variables.py`** -> AI Confidence: **99.31%**
16. **`airflow-core/src/airflow/api_fastapi/core_api/services/ui/dependencies.py`** -> AI Confidence: **99.31%**
17. **`airflow-core/src/airflow/api_fastapi/core_api/services/ui/grid.py`** -> AI Confidence: **99.31%**
18. **`airflow-core/src/airflow/api_fastapi/core_api/services/ui/structure.py`** -> AI Confidence: **99.31%**
19. **`airflow-core/src/airflow/api_fastapi/core_api/services/ui/task_group.py`** -> AI Confidence: **99.31%**
20. **`airflow-core/src/airflow/api_fastapi/execution_api/routes/task_instances.py`** -> AI Confidence: **99.31%**
21. **`airflow-core/src/airflow/api_fastapi/execution_api/routes/xcoms.py`** -> AI Confidence: **99.31%**
22. **`airflow-core/src/airflow/api_fastapi/logging/decorators.py`** -> AI Confidence: **99.31%**
23. **`airflow-core/src/airflow/cli/cli_config.py`** -> AI Confidence: **99.31%**
24. **`airflow-core/src/airflow/cli/commands/config_command.py`** -> AI Confidence: **99.31%**
25. **`airflow-core/src/airflow/cli/commands/connection_command.py`** -> AI Confidence: **99.31%**
26. **`airflow-core/src/airflow/cli/commands/dag_command.py`** -> AI Confidence: **99.31%**
27. **`airflow-core/src/airflow/cli/commands/db_command.py`** -> AI Confidence: **99.31%**
28. **`airflow-core/src/airflow/cli/commands/jobs_command.py`** -> AI Confidence: **99.31%**
29. **`airflow-core/src/airflow/dag_processing/collection.py`** -> AI Confidence: **99.31%**
30. **`airflow-core/src/airflow/dag_processing/dagbag.py`** -> AI Confidence: **99.31%**
31. **`airflow-core/src/airflow/dag_processing/manager.py`** -> AI Confidence: **99.31%**
32. **`airflow-core/src/airflow/executors/executor_loader.py`** -> AI Confidence: **99.31%**
33. **`airflow-core/src/airflow/jobs/scheduler_job_runner.py`** -> AI Confidence: **99.31%**
34. **`airflow-core/src/airflow/migrations/versions/0094_3_2_0_replace_deadline_inline_callback_with_fkey.py`** -> AI Confidence: **99.31%**
35. **`airflow-core/src/airflow/migrations/versions/0101_3_2_0_ui_improvements_for_deadlines.py`** -> AI Confidence: **99.31%**
36. **`airflow-core/src/airflow/models/connection.py`** -> AI Confidence: **99.31%**
37. **`airflow-core/src/airflow/models/dagrun.py`** -> AI Confidence: **99.31%**
38. **`airflow-core/src/airflow/models/taskinstance.py`** -> AI Confidence: **99.31%**
39. **`airflow-core/src/airflow/security/kerberos.py`** -> AI Confidence: **99.31%**
40. **`airflow-core/src/airflow/serialization/definitions/dag.py`** -> AI Confidence: **99.31%**
41. **`airflow-core/src/airflow/serialization/serialized_objects.py`** -> AI Confidence: **99.31%**
42. **`airflow-core/src/airflow/ti_deps/deps/trigger_rule_dep.py`** -> AI Confidence: **99.31%**
43. **`airflow-core/src/airflow/utils/dag_edges.py`** -> AI Confidence: **99.31%**
44. **`airflow-core/src/airflow/utils/dag_version_inflation_checker.py`** -> AI Confidence: **99.31%**
45. **`airflow-core/src/airflow/utils/db_cleanup.py`** -> AI Confidence: **99.31%**
46. **`airflow-core/src/airflow/utils/deprecation_tools.py`** -> AI Confidence: **99.31%**
47. **`airflow-core/src/airflow/utils/process_utils.py`** -> AI Confidence: **99.31%**
48. **`airflow-core/tests/unit/always/test_project_structure.py`** -> AI Confidence: **99.31%**
49. **`airflow-core/tests/unit/cli/commands/_common_cli_classes.py`** -> AI Confidence: **99.31%**
50. **`airflow-core/tests/unit/cli/test_cli_parser.py`** -> AI Confidence: **99.31%**
51. **`airflow-ctl/src/airflowctl/ctl/cli_config.py`** -> AI Confidence: **99.31%**
52. **`airflow-ctl/src/airflowctl/ctl/commands/auth_command.py`** -> AI Confidence: **99.31%**
53. **`airflow-ctl/src/airflowctl/ctl/commands/config_command.py`** -> AI Confidence: **99.31%**
54. **`dev/assign_cherry_picked_prs_with_milestone.py`** -> AI Confidence: **99.31%**
55. **`dev/breeze/src/airflow_breeze/commands/ci_commands.py`** -> AI Confidence: **99.31%**
56. **`dev/breeze/src/airflow_breeze/commands/ci_image_commands.py`** -> AI Confidence: **99.31%**
57. **`dev/breeze/src/airflow_breeze/commands/common_options.py`** -> AI Confidence: **99.31%**
58. **`dev/breeze/src/airflow_breeze/commands/developer_commands.py`** -> AI Confidence: **99.31%**
59. **`dev/breeze/src/airflow_breeze/commands/kubernetes_commands.py`** -> AI Confidence: **99.31%**
60. **`dev/breeze/src/airflow_breeze/commands/main_command.py`** -> AI Confidence: **99.31%**
61. **`dev/breeze/src/airflow_breeze/commands/production_image_commands.py`** -> AI Confidence: **99.31%**
62. **`dev/breeze/src/airflow_breeze/commands/release_candidate_command.py`** -> AI Confidence: **99.31%**
63. **`dev/breeze/src/airflow_breeze/commands/release_command.py`** -> AI Confidence: **99.31%**
64. **`dev/breeze/src/airflow_breeze/commands/release_management_commands.py`** -> AI Confidence: **99.31%**
65. **`dev/breeze/src/airflow_breeze/commands/release_management_validation.py`** -> AI Confidence: **99.31%**
66. **`dev/breeze/src/airflow_breeze/commands/sbom_commands.py`** -> AI Confidence: **99.31%**
67. **`dev/breeze/src/airflow_breeze/commands/setup_commands.py`** -> AI Confidence: **99.31%**
68. **`dev/breeze/src/airflow_breeze/commands/ui_commands.py`** -> AI Confidence: **99.31%**
69. **`dev/breeze/src/airflow_breeze/params/shell_params.py`** -> AI Confidence: **99.31%**
70. **`dev/breeze/src/airflow_breeze/prepare_providers/provider_distributions.py`** -> AI Confidence: **99.31%**
71. **`dev/breeze/src/airflow_breeze/utils/add_back_references.py`** -> AI Confidence: **99.31%**
72. **`dev/breeze/src/airflow_breeze/utils/airflow_release_validator.py`** -> AI Confidence: **99.31%**
73. **`dev/breeze/src/airflow_breeze/utils/cdxgen.py`** -> AI Confidence: **99.31%**
74. **`dev/breeze/src/airflow_breeze/utils/confirm.py`** -> AI Confidence: **99.31%**
75. **`dev/breeze/src/airflow_breeze/utils/docker_command_utils.py`** -> AI Confidence: **99.31%**
76. **`dev/breeze/src/airflow_breeze/utils/gh_workflow_utils.py`** -> AI Confidence: **99.31%**
77. **`dev/breeze/src/airflow_breeze/utils/github.py`** -> AI Confidence: **99.31%**
78. **`dev/breeze/src/airflow_breeze/utils/llm_utils.py`** -> AI Confidence: **99.31%**
79. **`dev/breeze/src/airflow_breeze/utils/packages.py`** -> AI Confidence: **99.31%**
80. **`dev/breeze/src/airflow_breeze/utils/parallel.py`** -> AI Confidence: **99.31%**
81. **`dev/breeze/src/airflow_breeze/utils/projects_google_spreadsheet.py`** -> AI Confidence: **99.31%**
82. **`dev/breeze/src/airflow_breeze/utils/provider_dependencies.py`** -> AI Confidence: **99.31%**
83. **`dev/breeze/src/airflow_breeze/utils/publish_registry_versions.py`** -> AI Confidence: **99.31%**
84. **`dev/breeze/src/airflow_breeze/utils/reinstall.py`** -> AI Confidence: **99.31%**
85. **`dev/breeze/src/airflow_breeze/utils/release_validator.py`** -> AI Confidence: **99.31%**
86. **`dev/breeze/src/airflow_breeze/utils/run_tests.py`** -> AI Confidence: **99.31%**
87. **`dev/breeze/src/airflow_breeze/utils/run_utils.py`** -> AI Confidence: **99.31%**
88. **`dev/breeze/src/airflow_breeze/utils/selective_checks.py`** -> AI Confidence: **99.31%**
89. **`dev/breeze/src/airflow_breeze/utils/tui_display.py`** -> AI Confidence: **99.31%**
90. **`dev/ide_setup/setup_idea.py`** -> AI Confidence: **99.31%**
91. **`dev/prune_old_dirs.py`** -> AI Confidence: **99.31%**
92. **`dev/registry/extract_connections.py`** -> AI Confidence: **99.31%**
93. **`dev/registry/extract_parameters.py`** -> AI Confidence: **99.31%**
94. **`dev/registry/extract_versions.py`** -> AI Confidence: **99.31%**
95. **`dev/stats/get_important_pr_candidates.py`** -> AI Confidence: **99.31%**
96. **`dev/validate_version_added_fields_in_config.py`** -> AI Confidence: **99.31%**
97. **`devel-common/src/sphinx_exts/docs_build/docs_builder.py`** -> AI Confidence: **99.31%**
98. **`devel-common/src/sphinx_exts/docs_build/fetch_inventories.py`** -> AI Confidence: **99.31%**
99. **`devel-common/src/sphinx_exts/docs_build/package_filter.py`** -> AI Confidence: **99.31%**
100. **`devel-common/src/sphinx_exts/docs_build/spelling_checks.py`** -> AI Confidence: **99.31%**
101. **`devel-common/src/sphinx_exts/exampleinclude.py`** -> AI Confidence: **99.31%**
102. **`devel-common/src/sphinx_exts/providers_extensions.py`** -> AI Confidence: **99.31%**
103. **`devel-common/src/tests_common/test_utils/config.py`** -> AI Confidence: **99.31%**
104. **`devel-common/src/tests_common/test_utils/otel_utils.py`** -> AI Confidence: **99.31%**
105. **`providers/alibaba/src/airflow/providers/alibaba/cloud/hooks/analyticdb_spark.py`** -> AI Confidence: **99.31%**
106. **`providers/amazon/src/airflow/providers/amazon/aws/executors/aws_lambda/lambda_executor.py`** -> AI Confidence: **99.31%**
107. **`providers/amazon/src/airflow/providers/amazon/aws/hooks/glue.py`** -> AI Confidence: **99.31%**
108. **`providers/amazon/src/airflow/providers/amazon/aws/hooks/s3.py`** -> AI Confidence: **99.31%**
109. **`providers/amazon/src/airflow/providers/amazon/aws/hooks/sagemaker.py`** -> AI Confidence: **99.31%**
110. **`providers/amazon/src/airflow/providers/amazon/aws/operators/datasync.py`** -> AI Confidence: **99.31%**
111. **`providers/amazon/src/airflow/providers/amazon/aws/operators/ecs.py`** -> AI Confidence: **99.31%**
112. **`providers/amazon/src/airflow/providers/amazon/aws/operators/eks.py`** -> AI Confidence: **99.31%**
113. **`providers/amazon/src/airflow/providers/amazon/aws/operators/emr.py`** -> AI Confidence: **99.31%**
114. **`providers/amazon/src/airflow/providers/amazon/aws/operators/glue.py`** -> AI Confidence: **99.31%**
115. **`providers/amazon/src/airflow/providers/amazon/aws/operators/redshift_cluster.py`** -> AI Confidence: **99.31%**
116. **`providers/amazon/src/airflow/providers/amazon/aws/sensors/s3.py`** -> AI Confidence: **99.31%**
117. **`providers/amazon/src/airflow/providers/amazon/aws/transfers/redshift_to_s3.py`** -> AI Confidence: **99.31%**
118. **`providers/amazon/src/airflow/providers/amazon/aws/transfers/s3_to_redshift.py`** -> AI Confidence: **99.31%**
119. **`providers/amazon/src/airflow/providers/amazon/aws/transfers/sql_to_s3.py`** -> AI Confidence: **99.31%**
120. **`providers/amazon/src/airflow/providers/amazon/aws/triggers/mwaa.py`** -> AI Confidence: **99.31%**
121. **`providers/apache/hive/src/airflow/providers/apache/hive/hooks/hive.py`** -> AI Confidence: **99.31%**
122. **`providers/apache/hive/src/airflow/providers/apache/hive/transfers/s3_to_hive.py`** -> AI Confidence: **99.31%**
123. **`providers/apache/kafka/src/airflow/providers/apache/kafka/operators/consume.py`** -> AI Confidence: **99.31%**
124. **`providers/apache/kylin/src/airflow/providers/apache/kylin/operators/kylin_cube.py`** -> AI Confidence: **99.31%**
125. **`providers/apache/livy/src/airflow/providers/apache/livy/hooks/livy.py`** -> AI Confidence: **99.31%**
126. **`providers/apache/pinot/src/airflow/providers/apache/pinot/hooks/pinot.py`** -> AI Confidence: **99.31%**
127. **`providers/apache/spark/src/airflow/providers/apache/spark/hooks/spark_sql.py`** -> AI Confidence: **99.31%**
128. **`providers/apache/spark/src/airflow/providers/apache/spark/hooks/spark_submit.py`** -> AI Confidence: **99.31%**
129. **`providers/celery/src/airflow/providers/celery/executors/default_celery.py`** -> AI Confidence: **99.31%**
130. **`providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/executors/kubernetes_executor_utils.py`** -> AI Confidence: **99.31%**
131. **`providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/kube_client.py`** -> AI Confidence: **99.31%**
132. **`providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/operators/custom_object_launcher.py`** -> AI Confidence: **99.31%**
133. **`providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/operators/pod.py`** -> AI Confidence: **99.31%**
134. **`providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/utils/pod_manager.py`** -> AI Confidence: **99.31%**
135. **`providers/common/ai/src/airflow/providers/common/ai/utils/file_analysis.py`** -> AI Confidence: **99.31%**
136. **`providers/databricks/src/airflow/providers/databricks/operators/databricks.py`** -> AI Confidence: **99.31%**
137. **`providers/databricks/src/airflow/providers/databricks/operators/databricks_repos.py`** -> AI Confidence: **99.31%**
138. **`providers/databricks/src/airflow/providers/databricks/operators/databricks_sql.py`** -> AI Confidence: **99.31%**
139. **`providers/databricks/src/airflow/providers/databricks/utils/mixins.py`** -> AI Confidence: **99.31%**
140. **`providers/databricks/src/airflow/providers/databricks/utils/openlineage.py`** -> AI Confidence: **99.31%**
141. **`providers/fab/src/airflow/providers/fab/auth_manager/api_fastapi/services/users.py`** -> AI Confidence: **99.31%**
142. **`providers/fab/src/airflow/providers/fab/auth_manager/cli_commands/role_command.py`** -> AI Confidence: **99.31%**
143. **`providers/fab/src/airflow/providers/fab/auth_manager/cli_commands/user_command.py`** -> AI Confidence: **99.31%**
144. **`providers/git/src/airflow/providers/git/bundles/git.py`** -> AI Confidence: **99.31%**
145. **`providers/google/src/airflow/providers/google/cloud/hooks/cloud_sql.py`** -> AI Confidence: **99.31%**
146. **`providers/google/src/airflow/providers/google/cloud/hooks/dlp.py`** -> AI Confidence: **99.31%**
147. **`providers/google/src/airflow/providers/google/cloud/hooks/gcs.py`** -> AI Confidence: **99.31%**
148. **`providers/google/src/airflow/providers/google/cloud/openlineage/mixins.py`** -> AI Confidence: **99.31%**
149. **`providers/google/src/airflow/providers/google/cloud/openlineage/utils.py`** -> AI Confidence: **99.31%**
150. **`providers/google/src/airflow/providers/google/cloud/operators/compute.py`** -> AI Confidence: **99.31%**
151. **`providers/google/src/airflow/providers/google/cloud/operators/dataproc.py`** -> AI Confidence: **99.31%**
152. **`providers/google/src/airflow/providers/google/cloud/sensors/cloud_composer.py`** -> AI Confidence: **99.31%**
153. **`providers/google/src/airflow/providers/google/cloud/transfers/gcs_to_bigquery.py`** -> AI Confidence: **99.31%**
154. **`providers/google/src/airflow/providers/google/cloud/transfers/gcs_to_gcs.py`** -> AI Confidence: **99.31%**
155. **`providers/google/src/airflow/providers/google/cloud/transfers/sql_to_gcs.py`** -> AI Confidence: **99.31%**
156. **`providers/google/src/airflow/providers/google/cloud/utils/credentials_provider.py`** -> AI Confidence: **99.31%**
157. **`providers/google/tests/system/google/cloud/gen_ai/example_gen_ai_generative_model.py`** -> AI Confidence: **99.31%**
158. **`providers/hashicorp/src/airflow/providers/hashicorp/_internal_client/vault_client.py`** -> AI Confidence: **99.31%**
159. **`providers/hashicorp/src/airflow/providers/hashicorp/hooks/vault.py`** -> AI Confidence: **99.31%**
160. **`providers/informatica/src/airflow/providers/informatica/plugins/listener.py`** -> AI Confidence: **99.31%**
161. **`providers/keycloak/src/airflow/providers/keycloak/auth_manager/cli/commands.py`** -> AI Confidence: **99.31%**
162. **`providers/microsoft/azure/src/airflow/providers/microsoft/azure/fs/adls.py`** -> AI Confidence: **99.31%**
163. **`providers/microsoft/azure/src/airflow/providers/microsoft/azure/operators/batch.py`** -> AI Confidence: **99.31%**
164. **`providers/microsoft/azure/src/airflow/providers/microsoft/azure/operators/container_instances.py`** -> AI Confidence: **99.31%**
165. **`providers/microsoft/psrp/src/airflow/providers/microsoft/psrp/operators/psrp.py`** -> AI Confidence: **99.31%**
166. **`providers/microsoft/winrm/src/airflow/providers/microsoft/winrm/hooks/winrm.py`** -> AI Confidence: **99.31%**
167. **`providers/mysql/src/airflow/providers/mysql/hooks/mysql.py`** -> AI Confidence: **99.31%**
168. **`providers/odbc/src/airflow/providers/odbc/hooks/odbc.py`** -> AI Confidence: **99.31%**
169. **`providers/openlineage/src/airflow/providers/openlineage/plugins/listener.py`** -> AI Confidence: **99.31%**
170. **`providers/openlineage/src/airflow/providers/openlineage/utils/sql.py`** -> AI Confidence: **99.31%**
171. **`providers/oracle/src/airflow/providers/oracle/hooks/oracle.py`** -> AI Confidence: **99.31%**
172. **`providers/sendgrid/src/airflow/providers/sendgrid/utils/emailer.py`** -> AI Confidence: **99.31%**
173. **`providers/sftp/src/airflow/providers/sftp/hooks/sftp.py`** -> AI Confidence: **99.31%**
174. **`providers/sftp/src/airflow/providers/sftp/operators/sftp.py`** -> AI Confidence: **99.31%**
175. **`providers/singularity/src/airflow/providers/singularity/operators/singularity.py`** -> AI Confidence: **99.31%**
176. **`providers/snowflake/src/airflow/providers/snowflake/hooks/snowflake_sql_api.py`** -> AI Confidence: **99.31%**
177. **`providers/snowflake/src/airflow/providers/snowflake/utils/openlineage.py`** -> AI Confidence: **99.31%**
178. **`providers/ssh/src/airflow/providers/ssh/hooks/ssh.py`** -> AI Confidence: **99.31%**
179. **`providers/ssh/src/airflow/providers/ssh/operators/ssh_remote_job.py`** -> AI Confidence: **99.31%**
180. **`providers/standard/src/airflow/providers/standard/operators/hitl.py`** -> AI Confidence: **99.31%**
181. **`providers/standard/src/airflow/providers/standard/operators/trigger_dagrun.py`** -> AI Confidence: **99.31%**
182. **`providers/standard/src/airflow/providers/standard/sensors/external_task.py`** -> AI Confidence: **99.31%**
183. **`providers/standard/tests/unit/standard/operators/test_branch_operator.py`** -> AI Confidence: **99.31%**
184. **`providers/teradata/src/airflow/providers/teradata/hooks/bteq.py`** -> AI Confidence: **99.31%**
185. **`providers/teradata/src/airflow/providers/teradata/hooks/teradata.py`** -> AI Confidence: **99.31%**
186. **`providers/teradata/src/airflow/providers/teradata/hooks/tpt.py`** -> AI Confidence: **99.31%**
187. **`providers/teradata/src/airflow/providers/teradata/operators/bteq.py`** -> AI Confidence: **99.31%**
188. **`providers/teradata/src/airflow/providers/teradata/operators/tpt.py`** -> AI Confidence: **99.31%**
189. **`providers/teradata/src/airflow/providers/teradata/utils/tpt_util.py`** -> AI Confidence: **99.31%**
190. **`providers/vertica/src/airflow/providers/vertica/hooks/vertica.py`** -> AI Confidence: **99.31%**
191. **`providers/weaviate/src/airflow/providers/weaviate/hooks/weaviate.py`** -> AI Confidence: **99.31%**
192. **`scripts/ci/analyze_e2e_flaky_tests.py`** -> AI Confidence: **99.31%**
193. **`scripts/ci/prek/check_airflow_imports_in_shared.py`** -> AI Confidence: **99.31%**
194. **`scripts/ci/prek/check_cli_definition_imports.py`** -> AI Confidence: **99.31%**
195. **`scripts/ci/prek/check_core_imports_in_sdk.py`** -> AI Confidence: **99.31%**
196. **`scripts/ci/prek/check_core_imports_in_shared.py`** -> AI Confidence: **99.31%**
197. **`scripts/ci/prek/check_deprecations.py`** -> AI Confidence: **99.31%**
198. **`scripts/ci/prek/check_init_decorator_arguments.py`** -> AI Confidence: **99.31%**
199. **`scripts/ci/prek/check_integrations_list.py`** -> AI Confidence: **99.31%**
200. **`scripts/ci/prek/check_lazy_logging.py`** -> AI Confidence: **99.31%**
201. **`scripts/ci/prek/check_metrics_synced_with_the_registry.py`** -> AI Confidence: **99.31%**
202. **`scripts/ci/prek/check_providers_subpackages_all_have_init.py`** -> AI Confidence: **99.31%**
203. **`scripts/ci/prek/check_shared_distributions_structure.py`** -> AI Confidence: **99.31%**
204. **`scripts/ci/prek/check_shared_distributions_usage.py`** -> AI Confidence: **99.31%**
205. **`scripts/ci/prek/check_system_tests.py`** -> AI Confidence: **99.31%**
206. **`scripts/ci/prek/check_test_only_imports_in_src.py`** -> AI Confidence: **99.31%**
207. **`scripts/ci/prek/check_version_consistency.py`** -> AI Confidence: **99.31%**
208. **`scripts/ci/prek/compile_provider_assets.py`** -> AI Confidence: **99.31%**
209. **`scripts/ci/prek/compile_ui_assets.py`** -> AI Confidence: **99.31%**
210. **`scripts/ci/prek/download_k8s_schemas.py`** -> AI Confidence: **99.31%**
211. **`scripts/ci/prek/new_session_in_provide_session.py`** -> AI Confidence: **99.31%**
212. **`scripts/ci/prek/update_providers_dependencies.py`** -> AI Confidence: **99.31%**
213. **`scripts/ci/prek/upgrade_important_versions.py`** -> AI Confidence: **99.31%**
214. **`scripts/ci/slack_notification_state.py`** -> AI Confidence: **99.31%**
215. **`scripts/ci/testing/summarize_captured_warnings.py`** -> AI Confidence: **99.31%**
216. **`scripts/ci/testing/summarize_junit_failures.py`** -> AI Confidence: **99.31%**
217. **`scripts/in_container/benchmark_cli_latency.py`** -> AI Confidence: **99.31%**
218. **`scripts/in_container/bin/generate_mprocs_config.py`** -> AI Confidence: **99.31%**
219. **`scripts/in_container/install_airflow_and_providers.py`** -> AI Confidence: **99.31%**
220. **`scripts/in_container/run_capture_airflowctl_help.py`** -> AI Confidence: **99.31%**
221. **`scripts/in_container/run_migration_reference.py`** -> AI Confidence: **99.31%**
222. **`scripts/in_container/run_provider_yaml_files_check.py`** -> AI Confidence: **99.31%**
223. **`scripts/in_container/run_schema_defaults_check.py`** -> AI Confidence: **99.31%**
224. **`scripts/in_container/run_template_fields_check.py`** -> AI Confidence: **99.31%**
225. **`scripts/tools/generate_yaml_format_for_hooks.py`** -> AI Confidence: **99.31%**
226. **`scripts/tools/initialize_virtualenv.py`** -> AI Confidence: **99.31%**
227. **`shared/configuration/src/airflow_shared/configuration/parser.py`** -> AI Confidence: **99.31%**
228. **`shared/module_loading/src/airflow_shared/module_loading/file_discovery.py`** -> AI Confidence: **99.31%**
229. **`shared/observability/src/airflow_shared/observability/common.py`** -> AI Confidence: **99.31%**
230. **`shared/observability/src/airflow_shared/observability/metrics/datadog_logger.py`** -> AI Confidence: **99.31%**
231. **`task-sdk/src/airflow/sdk/bases/decorator.py`** -> AI Confidence: **99.31%**
232. **`task-sdk/src/airflow/sdk/definitions/_internal/node.py`** -> AI Confidence: **99.31%**
233. **`task-sdk/src/airflow/sdk/definitions/connection.py`** -> AI Confidence: **99.31%**
234. **`task-sdk/src/airflow/sdk/execution_time/supervisor.py`** -> AI Confidence: **99.31%**
235. **`task-sdk/src/airflow/sdk/serde/__init__.py`** -> AI Confidence: **99.31%**
236. **`providers/common/sql/src/airflow/providers/common/sql/operators/sql.py`** -> AI Confidence: **99.31%**
237. **`airflow-core/src/airflow/api_fastapi/auth/managers/simple/ui/rules/unicorn.js`** -> AI Confidence: **99.31%**
238. **`airflow-core/src/airflow/ui/rules/unicorn.js`** -> AI Confidence: **99.31%**
239. **`providers/fab/src/airflow/providers/fab/www/webpack.config.js`** -> AI Confidence: **99.31%**
240. **`airflow-core/src/airflow/ui/src/components/AssetExpression/AssetExpression.tsx`** -> AI Confidence: **99.31%**
241. **`airflow-core/src/airflow/ui/src/components/Assets/AssetEvent.tsx`** -> AI Confidence: **99.31%**
242. **`airflow-core/src/airflow/ui/src/components/Assets/AssetEvents.tsx`** -> AI Confidence: **99.31%**
243. **`airflow-core/src/airflow/ui/src/components/Clear/TaskInstance/ClearTaskInstanceButton.tsx`** -> AI Confidence: **99.31%**
244. **`airflow-core/src/airflow/ui/src/components/DataTable/DataTable.tsx`** -> AI Confidence: **99.31%**
245. **`airflow-core/src/airflow/ui/src/components/DurationChart.tsx`** -> AI Confidence: **99.31%**
246. **`airflow-core/src/airflow/ui/src/components/FlexibleForm/FieldRow.tsx`** -> AI Confidence: **99.31%**
247. **`airflow-core/src/airflow/ui/src/components/FlexibleForm/FlexibleForm.tsx`** -> AI Confidence: **99.31%**
248. **`airflow-core/src/airflow/ui/src/components/Graph/AssetNode.tsx`** -> AI Confidence: **99.31%**
249. **`airflow-core/src/airflow/ui/src/components/Graph/DagNode.tsx`** -> AI Confidence: **99.31%**
250. **`airflow-core/src/airflow/ui/src/components/Graph/TaskNode.tsx`** -> AI Confidence: **99.31%**
251. **`airflow-core/src/airflow/ui/src/components/TaskTrySelect.tsx`** -> AI Confidence: **99.31%**
252. **`airflow-core/src/airflow/ui/src/components/TriggerDag/TriggerDAGForm.tsx`** -> AI Confidence: **99.31%**
253. **`airflow-core/src/airflow/ui/src/components/renderStructuredLog.tsx`** -> AI Confidence: **99.31%**
254. **`airflow-core/src/airflow/ui/src/hooks/navigation/useNavigation.ts`** -> AI Confidence: **99.31%**
255. **`airflow-core/src/airflow/ui/src/hooks/useDateRangeFilter.ts`** -> AI Confidence: **99.31%**
256. **`airflow-core/src/airflow/ui/src/layouts/Details/DetailsLayout.tsx`** -> AI Confidence: **99.31%**
257. **`airflow-core/src/airflow/ui/src/layouts/Details/Gantt/Gantt.tsx`** -> AI Confidence: **99.31%**
258. **`airflow-core/src/airflow/ui/src/layouts/Details/Gantt/utils.ts`** -> AI Confidence: **99.31%**
259. **`airflow-core/src/airflow/ui/src/layouts/Details/Graph/Graph.tsx`** -> AI Confidence: **99.31%**
260. **`airflow-core/src/airflow/ui/src/layouts/Details/Grid/TaskInstancesColumn.tsx`** -> AI Confidence: **99.31%**
261. **`airflow-core/src/airflow/ui/src/layouts/Nav/Nav.tsx`** -> AI Confidence: **99.31%**
262. **`airflow-core/src/airflow/ui/src/pages/Asset/AssetGraph.tsx`** -> AI Confidence: **99.31%**
263. **`airflow-core/src/airflow/ui/src/pages/Asset/AssetLayout.tsx`** -> AI Confidence: **99.31%**
264. **`airflow-core/src/airflow/ui/src/pages/Asset/CreateAssetEventModal.tsx`** -> AI Confidence: **99.31%**
265. **`airflow-core/src/airflow/ui/src/pages/Connections/EditConnectionButton.tsx`** -> AI Confidence: **99.31%**
266. **`airflow-core/src/airflow/ui/src/pages/Connections/TestConnectionButton.tsx`** -> AI Confidence: **99.31%**
267. **`airflow-core/src/airflow/ui/src/pages/Dag/Calendar/Calendar.tsx`** -> AI Confidence: **99.31%**
268. **`airflow-core/src/airflow/ui/src/pages/Dag/Dag.tsx`** -> AI Confidence: **99.31%**
269. **`airflow-core/src/airflow/ui/src/pages/Dag/Header.tsx`** -> AI Confidence: **99.31%**
270. **`airflow-core/src/airflow/ui/src/pages/Dag/Overview/Overview.tsx`** -> AI Confidence: **99.31%**
271. **`airflow-core/src/airflow/ui/src/pages/Dag/Tasks/Tasks.tsx`** -> AI Confidence: **99.31%**
272. **`airflow-core/src/airflow/ui/src/pages/DagRuns.tsx`** -> AI Confidence: **99.31%**
273. **`airflow-core/src/airflow/ui/src/pages/DagsList/AssetSchedule.tsx`** -> AI Confidence: **99.31%**
274. **`airflow-core/src/airflow/ui/src/pages/Dashboard/PoolSummary/PoolSummary.tsx`** -> AI Confidence: **99.31%**
275. **`airflow-core/src/airflow/ui/src/pages/Dashboard/Stats/Stats.tsx`** -> AI Confidence: **99.31%**
276. **`airflow-core/src/airflow/ui/src/pages/Events/Events.tsx`** -> AI Confidence: **99.31%**
277. **`airflow-core/src/airflow/ui/src/pages/HITLTaskInstances/HITLResponseForm.tsx`** -> AI Confidence: **99.31%**
278. **`airflow-core/src/airflow/ui/src/pages/HITLTaskInstances/HITLTaskInstances.tsx`** -> AI Confidence: **99.31%**
279. **`airflow-core/src/airflow/ui/src/pages/Task/Overview/Overview.tsx`** -> AI Confidence: **99.31%**
280. **`airflow-core/src/airflow/ui/src/pages/TaskInstance/HITLResponse.tsx`** -> AI Confidence: **99.31%**
281. **`airflow-core/src/airflow/ui/src/pages/TaskInstances/TaskInstances.tsx`** -> AI Confidence: **99.31%**
282. **`airflow-core/src/airflow/ui/src/queries/useLogs.tsx`** -> AI Confidence: **99.31%**
283. **`providers/common/ai/src/airflow/providers/common/ai/plugins/www/src/components/ChatPage.tsx`** -> AI Confidence: **99.31%**
284. **`providers/edge3/src/airflow/providers/edge3/plugins/www/src/pages/JobsPage.tsx`** -> AI Confidence: **99.31%**
285. **`go-sdk/bundle/bundlev1/task.go`** -> AI Confidence: **99.31%**
286. **`go-sdk/pkg/bundles/shared/discovery.go`** -> AI Confidence: **99.31%**
287. **`go-sdk/pkg/config/config.go`** -> AI Confidence: **99.31%**
288. **`go-sdk/pkg/logging/server/server.go`** -> AI Confidence: **99.31%**
289. **`providers/amazon/src/airflow/providers/amazon/aws/executors/aws_lambda/docker/Dockerfile`** -> AI Confidence: **99.29%**
290. **`scripts/ci/dockerfiles/krb5-kdc-server/Dockerfile`** -> AI Confidence: **99.29%**
291. **`registry/src/_data/exploreCategoryProviders.js`** -> AI Confidence: **99.29%**
292. **`registry/src/_data/providerCategoryMap.js`** -> AI Confidence: **99.29%**
293. **`registry/src/_data/providerVersionPayloads.js`** -> AI Confidence: **99.29%**
294. **`registry/src/js/mobile-menu.js`** -> AI Confidence: **99.29%**
295. **`airflow-core/src/airflow/ui/src/constants/urlRegex.ts`** -> AI Confidence: **99.29%**
296. **`dev/breeze/autocomplete/breeze-complete-fish.sh`** -> AI Confidence: **99.29%**
297. **`dev/breeze/autocomplete/breeze-complete-zsh.sh`** -> AI Confidence: **99.29%**
298. **`scripts/ci/constraints/ci_branch_constraints.sh`** -> AI Confidence: **99.29%**
299. **`scripts/ci/dockerfiles/krb5-kdc-server/entrypoint.sh`** -> AI Confidence: **99.29%**
300. **`scripts/ci/dockerfiles/trino/entrypoint.sh`** -> AI Confidence: **99.29%**
301. **`scripts/ci/testing/run_unit_tests.sh`** -> AI Confidence: **99.29%**
302. **`scripts/docker/airflow-scheduler-autorestart.sh`** -> AI Confidence: **99.29%**
303. **`scripts/docker/install_additional_dependencies.sh`** -> AI Confidence: **99.29%**
304. **`scripts/docker/install_airflow_when_building_images.sh`** -> AI Confidence: **99.29%**
305. **`scripts/in_container/bin/run_tmux`** -> AI Confidence: **99.29%**
306. **`scripts/in_container/check_environment.sh`** -> AI Confidence: **99.29%**
307. **`scripts/in_container/run_ci_tests.sh`** -> AI Confidence: **99.29%**
308. **`airflow-core/src/airflow/ui/playwright.config.ts`** -> AI Confidence: **99.26%**
309. **`airflow-core/src/airflow/api_fastapi/core_api/services/public/pools.py`** -> AI Confidence: **99.25%**
310. **`dev/registry/extract_metadata.py`** -> AI Confidence: **99.25%**
311. **`providers/git/src/airflow/providers/git/hooks/git.py`** -> AI Confidence: **99.25%**
312. **`airflow-core/src/airflow/api/common/trigger_dag.py`** -> AI Confidence: **99.24%**
313. **`airflow-core/src/airflow/api_fastapi/app.py`** -> AI Confidence: **99.24%**
314. **`airflow-core/src/airflow/api_fastapi/core_api/datamodels/task_instances.py`** -> AI Confidence: **99.24%**
315. **`airflow-core/src/airflow/api_fastapi/core_api/routes/public/dag_run.py`** -> AI Confidence: **99.24%**
316. **`airflow-core/src/airflow/api_fastapi/core_api/routes/ui/structure.py`** -> AI Confidence: **99.24%**
317. **`airflow-core/src/airflow/api_fastapi/core_api/services/ui/calendar.py`** -> AI Confidence: **99.24%**
318. **`airflow-core/src/airflow/assets/manager.py`** -> AI Confidence: **99.24%**
319. **`airflow-core/src/airflow/cli/cli_parser.py`** -> AI Confidence: **99.24%**
320. **`airflow-core/src/airflow/cli/commands/asset_command.py`** -> AI Confidence: **99.24%**
321. **`airflow-core/src/airflow/cli/commands/task_command.py`** -> AI Confidence: **99.24%**
322. **`airflow-core/src/airflow/cli/commands/variable_command.py`** -> AI Confidence: **99.24%**
323. **`airflow-core/src/airflow/configuration.py`** -> AI Confidence: **99.24%**
324. **`airflow-core/src/airflow/dag_processing/bundles/manager.py`** -> AI Confidence: **99.24%**
325. **`airflow-core/src/airflow/dag_processing/processor.py`** -> AI Confidence: **99.24%**
326. **`airflow-core/src/airflow/executors/local_executor.py`** -> AI Confidence: **99.24%**
327. **`airflow-core/src/airflow/models/backfill.py`** -> AI Confidence: **99.24%**
328. **`airflow-core/src/airflow/models/serialized_dag.py`** -> AI Confidence: **99.24%**
329. **`airflow-core/src/airflow/plugins_manager.py`** -> AI Confidence: **99.24%**
330. **`airflow-core/src/airflow/secrets/local_filesystem.py`** -> AI Confidence: **99.24%**
331. **`airflow-core/src/airflow/ti_deps/deps/prev_dagrun_dep.py`** -> AI Confidence: **99.24%**
332. **`airflow-core/src/airflow/utils/cli.py`** -> AI Confidence: **99.24%**
333. **`airflow-core/src/airflow/utils/db.py`** -> AI Confidence: **99.24%**
334. **`airflow-core/src/airflow/utils/dot_renderer.py`** -> AI Confidence: **99.24%**
335. **`airflow-core/src/airflow/utils/email.py`** -> AI Confidence: **99.24%**
336. **`airflow-core/src/airflow/utils/helpers.py`** -> AI Confidence: **99.24%**
337. **`airflow-core/tests/unit/always/test_secrets_local_filesystem.py`** -> AI Confidence: **99.24%**
338. **`airflow-core/tests/unit/models/test_backfill.py`** -> AI Confidence: **99.24%**
339. **`clients/python/test_python_client.py`** -> AI Confidence: **99.24%**
340. **`dev/breeze/src/airflow_breeze/commands/minor_release_command.py`** -> AI Confidence: **99.24%**
341. **`dev/breeze/src/airflow_breeze/commands/registry_commands.py`** -> AI Confidence: **99.24%**
342. **`dev/breeze/src/airflow_breeze/commands/testing_commands.py`** -> AI Confidence: **99.24%**
343. **`dev/breeze/src/airflow_breeze/commands/workflow_commands.py`** -> AI Confidence: **99.24%**
344. **`dev/breeze/src/airflow_breeze/params/build_prod_params.py`** -> AI Confidence: **99.24%**
345. **`dev/breeze/src/airflow_breeze/utils/ci_group.py`** -> AI Confidence: **99.24%**
346. **`dev/breeze/src/airflow_breeze/utils/constraints_version_check.py`** -> AI Confidence: **99.24%**
347. **`dev/breeze/src/airflow_breeze/utils/custom_param_types.py`** -> AI Confidence: **99.24%**
348. **`dev/breeze/src/airflow_breeze/utils/docker_compose_utils.py`** -> AI Confidence: **99.24%**
349. **`dev/breeze/src/airflow_breeze/utils/path_utils.py`** -> AI Confidence: **99.24%**
350. **`dev/breeze/src/airflow_breeze/utils/publish_docs_to_s3.py`** -> AI Confidence: **99.24%**
351. **`dev/breeze/src/airflow_breeze/utils/reproducible.py`** -> AI Confidence: **99.24%**
352. **`dev/verify_release_calendar.py`** -> AI Confidence: **99.24%**
353. **`devel-common/src/sphinx_exts/airflow_intersphinx.py`** -> AI Confidence: **99.24%**
354. **`devel-common/src/sphinx_exts/docs_build/errors.py`** -> AI Confidence: **99.24%**
355. **`devel-common/src/sphinx_exts/operators_and_hooks_ref.py`** -> AI Confidence: **99.24%**
356. **`devel-common/src/sphinx_exts/providers_commits.py`** -> AI Confidence: **99.24%**
357. **`devel-common/src/tests_common/_internals/capture_warnings.py`** -> AI Confidence: **99.24%**
358. **`devel-common/src/tests_common/pytest_plugin.py`** -> AI Confidence: **99.24%**
359. **`devel-common/src/tests_common/test_utils/perf/perf_kit/python.py`** -> AI Confidence: **99.24%**
360. **`docker-tests/tests/docker_tests/test_prod_image.py`** -> AI Confidence: **99.24%**
361. **`helm-tests/tests/chart_utils/helm_template_generator.py`** -> AI Confidence: **99.24%**
362. **`kubernetes-tests/tests/kubernetes_tests/test_base.py`** -> AI Confidence: **99.24%**
363. **`performance/src/performance_dags/performance_dag/performance_dag_utils.py`** -> AI Confidence: **99.24%**
364. **`providers/amazon/src/airflow/providers/amazon/aws/executors/batch/batch_executor.py`** -> AI Confidence: **99.24%**
365. **`providers/amazon/src/airflow/providers/amazon/aws/executors/ecs/ecs_executor.py`** -> AI Confidence: **99.24%**
366. **`providers/amazon/src/airflow/providers/amazon/aws/hooks/batch_client.py`** -> AI Confidence: **99.24%**
367. **`providers/amazon/src/airflow/providers/amazon/aws/hooks/emr.py`** -> AI Confidence: **99.24%**
368. **`providers/amazon/src/airflow/providers/amazon/aws/hooks/redshift_sql.py`** -> AI Confidence: **99.24%**
369. **`providers/amazon/src/airflow/providers/amazon/aws/hooks/sagemaker_unified_studio.py`** -> AI Confidence: **99.24%**
370. **`providers/amazon/src/airflow/providers/amazon/aws/operators/batch.py`** -> AI Confidence: **99.24%**
371. **`providers/amazon/src/airflow/providers/amazon/aws/operators/bedrock.py`** -> AI Confidence: **99.24%**
372. **`providers/amazon/src/airflow/providers/amazon/aws/operators/kinesis_analytics.py`** -> AI Confidence: **99.24%**
373. **`providers/amazon/src/airflow/providers/amazon/aws/operators/neptune.py`** -> AI Confidence: **99.24%**
374. **`providers/amazon/src/airflow/providers/amazon/aws/operators/sagemaker.py`** -> AI Confidence: **99.24%**
375. **`providers/amazon/src/airflow/providers/amazon/aws/operators/ssm.py`** -> AI Confidence: **99.24%**
376. **`providers/amazon/src/airflow/providers/amazon/aws/sensors/mwaa.py`** -> AI Confidence: **99.24%**
377. **`providers/amazon/src/airflow/providers/amazon/aws/transfers/gcs_to_s3.py`** -> AI Confidence: **99.24%**
378. **`providers/amazon/src/airflow/providers/amazon/aws/utils/connection_wrapper.py`** -> AI Confidence: **99.24%**
379. **`providers/amazon/tests/unit/amazon/aws/auth_manager/cli/test_avp_commands.py`** -> AI Confidence: **99.24%**
380. **`providers/apache/beam/src/airflow/providers/apache/beam/hooks/beam.py`** -> AI Confidence: **99.24%**
381. **`providers/apache/beam/src/airflow/providers/apache/beam/operators/beam.py`** -> AI Confidence: **99.24%**
382. **`providers/apache/cassandra/src/airflow/providers/apache/cassandra/hooks/cassandra.py`** -> AI Confidence: **99.24%**
383. **`providers/apache/druid/src/airflow/providers/apache/druid/hooks/druid.py`** -> AI Confidence: **99.24%**
384. **`providers/apache/hdfs/src/airflow/providers/apache/hdfs/hooks/webhdfs.py`** -> AI Confidence: **99.24%**
385. **`providers/apache/livy/src/airflow/providers/apache/livy/operators/livy.py`** -> AI Confidence: **99.24%**
386. **`providers/celery/src/airflow/providers/celery/cli/celery_command.py`** -> AI Confidence: **99.24%**
387. **`providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/cli/kubernetes_command.py`** -> AI Confidence: **99.24%**
388. **`providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/executors/kubernetes_executor.py`** -> AI Confidence: **99.24%**
389. **`providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/operators/job.py`** -> AI Confidence: **99.24%**
390. **`providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/operators/kueue.py`** -> AI Confidence: **99.24%**
391. **`providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/operators/spark_kubernetes.py`** -> AI Confidence: **99.24%**
392. **`providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/pod_generator.py`** -> AI Confidence: **99.24%**
393. **`providers/common/ai/src/airflow/providers/common/ai/mixins/approval.py`** -> AI Confidence: **99.24%**
394. **`providers/common/ai/src/airflow/providers/common/ai/mixins/hitl_review.py`** -> AI Confidence: **99.24%**
395. **`providers/common/ai/src/airflow/providers/common/ai/operators/llm_schema_compare.py`** -> AI Confidence: **99.24%**
396. **`providers/common/ai/src/airflow/providers/common/ai/toolsets/hook.py`** -> AI Confidence: **99.24%**
397. **`providers/databricks/src/airflow/providers/databricks/hooks/databricks_base.py`** -> AI Confidence: **99.24%**
398. **`providers/databricks/src/airflow/providers/databricks/operators/databricks_workflow.py`** -> AI Confidence: **99.24%**
399. **`providers/databricks/src/airflow/providers/databricks/sensors/databricks.py`** -> AI Confidence: **99.24%**
400. **`providers/dbt/cloud/src/airflow/providers/dbt/cloud/operators/dbt.py`** -> AI Confidence: **99.24%**
401. **`providers/discord/src/airflow/providers/discord/hooks/discord_webhook.py`** -> AI Confidence: **99.24%**
402. **`providers/docker/src/airflow/providers/docker/operators/docker_swarm.py`** -> AI Confidence: **99.24%**
403. **`providers/edge3/src/airflow/providers/edge3/cli/edge_command.py`** -> AI Confidence: **99.24%**
404. **`providers/edge3/src/airflow/providers/edge3/migrations/env.py`** -> AI Confidence: **99.24%**
405. **`providers/edge3/src/airflow/providers/edge3/worker_api/routes/ui.py`** -> AI Confidence: **99.24%**
406. **`providers/edge3/src/airflow/providers/edge3/worker_api/routes/worker.py`** -> AI Confidence: **99.24%**
407. **`providers/fab/src/airflow/providers/fab/auth_manager/api_fastapi/services/roles.py`** -> AI Confidence: **99.24%**
408. **`providers/fab/src/airflow/providers/fab/auth_manager/cli_commands/permissions_command.py`** -> AI Confidence: **99.24%**
409. **`providers/fab/src/airflow/providers/fab/auth_manager/models/db.py`** -> AI Confidence: **99.24%**
410. **`providers/fab/src/airflow/providers/fab/auth_manager/security_manager/override.py`** -> AI Confidence: **99.24%**
411. **`providers/fab/src/airflow/providers/fab/migrations/env.py`** -> AI Confidence: **99.24%**
412. **`providers/fab/tests/unit/fab/auth_manager/security_manager/test_fab_alignment.py`** -> AI Confidence: **99.24%**
413. **`providers/google/src/airflow/providers/google/cloud/hooks/bigquery.py`** -> AI Confidence: **99.24%**
414. **`providers/google/src/airflow/providers/google/cloud/hooks/compute_ssh.py`** -> AI Confidence: **99.24%**
415. **`providers/google/src/airflow/providers/google/cloud/hooks/mlengine.py`** -> AI Confidence: **99.24%**
416. **`providers/google/src/airflow/providers/google/cloud/hooks/stackdriver.py`** -> AI Confidence: **99.24%**
417. **`providers/google/src/airflow/providers/google/cloud/operators/alloy_db.py`** -> AI Confidence: **99.24%**
418. **`providers/google/src/airflow/providers/google/cloud/operators/bigquery.py`** -> AI Confidence: **99.24%**
419. **`providers/google/src/airflow/providers/google/cloud/operators/dlp.py`** -> AI Confidence: **99.24%**
420. **`providers/google/src/airflow/providers/google/cloud/operators/gcs.py`** -> AI Confidence: **99.24%**
421. **`providers/google/src/airflow/providers/google/cloud/operators/gen_ai.py`** -> AI Confidence: **99.24%**
422. **`providers/google/src/airflow/providers/google/cloud/operators/spanner.py`** -> AI Confidence: **99.24%**
423. **`providers/google/src/airflow/providers/google/cloud/transfers/azure_fileshare_to_gcs.py`** -> AI Confidence: **99.24%**
424. **`providers/google/src/airflow/providers/google/cloud/transfers/bigquery_to_sql.py`** -> AI Confidence: **99.24%**
425. **`providers/google/src/airflow/providers/google/cloud/transfers/local_to_gcs.py`** -> AI Confidence: **99.24%**
426. **`providers/google/src/airflow/providers/google/cloud/triggers/cloud_composer.py`** -> AI Confidence: **99.24%**
427. **`providers/google/tests/unit/google/cloud/operators/test_functions.py`** -> AI Confidence: **99.24%**
428. **`providers/http/src/airflow/providers/http/hooks/http.py`** -> AI Confidence: **99.24%**
429. **`providers/imap/src/airflow/providers/imap/hooks/imap.py`** -> AI Confidence: **99.24%**
430. **`providers/informatica/src/airflow/providers/informatica/hooks/edc.py`** -> AI Confidence: **99.24%**
431. **`providers/jdbc/src/airflow/providers/jdbc/hooks/jdbc.py`** -> AI Confidence: **99.24%**
432. **`providers/jenkins/src/airflow/providers/jenkins/operators/jenkins_job_trigger.py`** -> AI Confidence: **99.24%**
433. **`providers/microsoft/azure/src/airflow/providers/microsoft/azure/hooks/asb.py`** -> AI Confidence: **99.24%**
434. **`providers/microsoft/azure/src/airflow/providers/microsoft/azure/hooks/batch.py`** -> AI Confidence: **99.24%**
435. **`providers/microsoft/azure/src/airflow/providers/microsoft/azure/operators/data_factory.py`** -> AI Confidence: **99.24%**
436. **`providers/microsoft/azure/src/airflow/providers/microsoft/azure/transfers/s3_to_wasb.py`** -> AI Confidence: **99.24%**
437. **`providers/microsoft/psrp/src/airflow/providers/microsoft/psrp/hooks/psrp.py`** -> AI Confidence: **99.24%**
438. **`providers/microsoft/psrp/tests/unit/microsoft/psrp/operators/test_psrp.py`** -> AI Confidence: **99.24%**
439. **`providers/microsoft/winrm/src/airflow/providers/microsoft/winrm/operators/winrm.py`** -> AI Confidence: **99.24%**
440. **`providers/openlineage/src/airflow/providers/openlineage/extractors/manager.py`** -> AI Confidence: **99.24%**
441. **`providers/openlineage/src/airflow/providers/openlineage/plugins/adapter.py`** -> AI Confidence: **99.24%**
442. **`providers/openlineage/src/airflow/providers/openlineage/sqlparser.py`** -> AI Confidence: **99.24%**
443. **`providers/openlineage/src/airflow/providers/openlineage/utils/sql_hook_lineage.py`** -> AI Confidence: **99.24%**
444. **`providers/openlineage/src/airflow/providers/openlineage/utils/utils.py`** -> AI Confidence: **99.24%**
445. **`providers/openlineage/tests/system/openlineage/operator.py`** -> AI Confidence: **99.24%**
446. **`providers/pagerduty/src/airflow/providers/pagerduty/hooks/pagerduty_events.py`** -> AI Confidence: **99.24%**
447. **`providers/sftp/src/airflow/providers/sftp/sensors/sftp.py`** -> AI Confidence: **99.24%**
448. **`providers/smtp/src/airflow/providers/smtp/hooks/smtp.py`** -> AI Confidence: **99.24%**
449. **`providers/snowflake/src/airflow/providers/snowflake/hooks/snowflake.py`** -> AI Confidence: **99.24%**
450. **`providers/snowflake/src/airflow/providers/snowflake/operators/snowflake.py`** -> AI Confidence: **99.24%**
451. **`providers/snowflake/src/airflow/providers/snowflake/transfers/copy_into_snowflake.py`** -> AI Confidence: **99.24%**
452. **`providers/ssh/src/airflow/providers/ssh/operators/ssh.py`** -> AI Confidence: **99.24%**
453. **`providers/standard/src/airflow/providers/standard/operators/python.py`** -> AI Confidence: **99.24%**
454. **`providers/standard/src/airflow/providers/standard/utils/python_virtualenv.py`** -> AI Confidence: **99.24%**
455. **`providers/standard/src/airflow/providers/standard/utils/sensor_helper.py`** -> AI Confidence: **99.24%**
456. **`providers/standard/tests/unit/standard/operators/test_trigger_dagrun.py`** -> AI Confidence: **99.24%**
457. **`providers/standard/tests/unit/standard/operators/test_weekday.py`** -> AI Confidence: **99.24%**
458. **`providers/standard/tests/unit/standard/sensors/test_external_task_sensor.py`** -> AI Confidence: **99.24%**
459. **`providers/standard/tests/unit/standard/sensors/test_weekday.py`** -> AI Confidence: **99.24%**
460. **`providers/standard/tests/unit/standard/utils/test_sensor_helper.py`** -> AI Confidence: **99.24%**
461. **`providers/teradata/src/airflow/providers/teradata/utils/bteq_util.py`** -> AI Confidence: **99.24%**
462. **`providers/trino/src/airflow/providers/trino/hooks/trino.py`** -> AI Confidence: **99.24%**
463. **`scripts/ci/prek/check_airflow_v_imports_in_tests.py`** -> AI Confidence: **99.24%**
464. **`scripts/ci/prek/check_common_sql_dependency.py`** -> AI Confidence: **99.24%**
465. **`scripts/ci/prek/common_prek_utils.py`** -> AI Confidence: **99.24%**
466. **`scripts/ci/prek/update_airflow_pyproject_toml.py`** -> AI Confidence: **99.24%**
467. **`scripts/in_container/run_generate_constraints.py`** -> AI Confidence: **99.24%**
468. **`scripts/in_container/update_quarantined_test_status.py`** -> AI Confidence: **99.24%**
469. **`scripts/in_container/verify_providers.py`** -> AI Confidence: **99.24%**
470. **`shared/logging/src/airflow_shared/logging/percent_formatter.py`** -> AI Confidence: **99.24%**
471. **`shared/observability/src/airflow_shared/observability/metrics/validators.py`** -> AI Confidence: **99.24%**
472. **`shared/secrets_masker/src/airflow_shared/secrets_masker/secrets_masker.py`** -> AI Confidence: **99.24%**
473. **`task-sdk/src/airflow/sdk/bases/sensor.py`** -> AI Confidence: **99.24%**
474. **`task-sdk/src/airflow/sdk/bases/skipmixin.py`** -> AI Confidence: **99.24%**
475. **`task-sdk/src/airflow/sdk/definitions/_internal/expandinput.py`** -> AI Confidence: **99.24%**
476. **`task-sdk/src/airflow/sdk/definitions/_internal/templater.py`** -> AI Confidence: **99.24%**
477. **`task-sdk/src/airflow/sdk/definitions/dag.py`** -> AI Confidence: **99.24%**
478. **`task-sdk/src/airflow/sdk/definitions/edges.py`** -> AI Confidence: **99.24%**
479. **`task-sdk/src/airflow/sdk/definitions/taskgroup.py`** -> AI Confidence: **99.24%**
480. **`task-sdk/src/airflow/sdk/execution_time/task_runner.py`** -> AI Confidence: **99.24%**
481. **`airflow-core/src/airflow/ui/src/components/DagActions/RunBackfillForm.tsx`** -> AI Confidence: **99.24%**
482. **`airflow-core/src/airflow/ui/src/components/Time.tsx`** -> AI Confidence: **99.24%**
483. **`airflow-core/src/airflow/ui/src/layouts/Details/Grid/Bar.tsx`** -> AI Confidence: **99.24%**
484. **`airflow-core/src/airflow/ui/src/layouts/Details/Grid/Grid.tsx`** -> AI Confidence: **99.24%**
485. **`airflow-core/src/airflow/ui/src/pages/Connections/ConnectionForm.tsx`** -> AI Confidence: **99.24%**
486. **`airflow-core/src/airflow/ui/src/pages/Dag/Tasks/TaskFilters/TaskFilters.tsx`** -> AI Confidence: **99.24%**
487. **`airflow-core/src/airflow/ui/src/pages/Dashboard/Health/Health.tsx`** -> AI Confidence: **99.24%**
488. **`airflow-core/src/airflow/ui/src/pages/Jobs.tsx`** -> AI Confidence: **99.24%**
489. **`airflow-core/src/airflow/ui/src/pages/TaskInstance/AssetEvents.tsx`** -> AI Confidence: **99.24%**
490. **`airflow-core/src/airflow/ui/src/pages/XCom/XCom.tsx`** -> AI Confidence: **99.24%**
491. **`airflow-core/src/airflow/ui/src/queries/useTrigger.ts`** -> AI Confidence: **99.24%**
492. **`providers/edge3/src/airflow/providers/edge3/plugins/www/src/components/WorkerStateIcon.tsx`** -> AI Confidence: **99.24%**
493. **`providers/edge3/src/airflow/providers/edge3/plugins/www/src/pages/WorkerPage.tsx`** -> AI Confidence: **99.24%**
494. **`go-sdk/edge/worker.go`** -> AI Confidence: **99.24%**
495. **`providers/google/tests/system/google/cloud/dataflow/resources/wordcount.go`** -> AI Confidence: **99.24%**
496. **`airflow-core/src/airflow/api_fastapi/core_api/routes/ui/assets.py`** -> AI Confidence: **99.23%**
497. **`airflow-core/src/airflow/migrations/versions/0041_3_0_0_rename_dataset_as_asset.py`** -> AI Confidence: **99.23%**
498. **`airflow-core/src/airflow/migrations/versions/0055_3_0_0_remove_pickled_data_from_dagrun_table.py`** -> AI Confidence: **99.23%**
499. **`airflow-core/tests/unit/cli/commands/test_api_server_command.py`** -> AI Confidence: **99.23%**
500. **`dev/airflow_perf/dags/elastic_dag.py`** -> AI Confidence: **99.23%**
501. **`dev/breeze/src/airflow_breeze/utils/docs_version_validation.py`** -> AI Confidence: **99.23%**
502. **`dev/breeze/src/airflow_breeze/utils/pr_cache.py`** -> AI Confidence: **99.23%**
503. **`dev/provider_db_inventory.py`** -> AI Confidence: **99.23%**
504. **`devel-common/src/tests_common/_internals/forbidden_warnings.py`** -> AI Confidence: **99.23%**
505. **`providers/airbyte/src/airflow/providers/airbyte/sensors/airbyte.py`** -> AI Confidence: **99.23%**
506. **`providers/amazon/src/airflow/providers/amazon/aws/hooks/athena.py`** -> AI Confidence: **99.23%**
507. **`providers/amazon/src/airflow/providers/amazon/aws/transfers/ftp_to_s3.py`** -> AI Confidence: **99.23%**
508. **`providers/amazon/src/airflow/providers/amazon/aws/utils/waiter_with_logging.py`** -> AI Confidence: **99.23%**
509. **`providers/amazon/tests/unit/amazon/aws/hooks/test_hooks_signature.py`** -> AI Confidence: **99.23%**
510. **`providers/apache/hive/src/airflow/providers/apache/hive/operators/hive_stats.py`** -> AI Confidence: **99.23%**
511. **`providers/apache/kafka/src/airflow/providers/apache/kafka/operators/produce.py`** -> AI Confidence: **99.23%**
512. **`providers/apache/spark/src/airflow/providers/apache/spark/operators/spark_pyspark.py`** -> AI Confidence: **99.23%**
513. **`providers/common/compat/src/airflow/providers/common/compat/openlineage/check.py`** -> AI Confidence: **99.23%**
514. **`providers/common/messaging/src/airflow/providers/common/messaging/triggers/msg_queue.py`** -> AI Confidence: **99.23%**
515. **`providers/fab/tests/unit/fab/www/views/test_connection_form_fields.py`** -> AI Confidence: **99.23%**
516. **`providers/google/src/airflow/providers/google/cloud/sensors/dataflow.py`** -> AI Confidence: **99.23%**
517. **`providers/google/src/airflow/providers/google/suite/hooks/drive.py`** -> AI Confidence: **99.23%**
518. **`providers/standard/src/airflow/providers/standard/utils/skipmixin.py`** -> AI Confidence: **99.23%**
519. **`providers/teradata/src/airflow/providers/teradata/triggers/teradata_compute_cluster.py`** -> AI Confidence: **99.23%**
520. **`scripts/ci/airflow_version_check.py`** -> AI Confidence: **99.23%**
521. **`scripts/ci/prek/check_excluded_provider_markers.py`** -> AI Confidence: **99.23%**
522. **`scripts/ci/prek/check_execution_api_versions.py`** -> AI Confidence: **99.23%**
523. **`scripts/ci/prek/validate_operators_init.py`** -> AI Confidence: **99.23%**
524. **`scripts/in_container/run_fix_ownership.py`** -> AI Confidence: **99.23%**
525. **`shared/dagnode/src/airflow_shared/dagnode/node.py`** -> AI Confidence: **99.23%**
526. **`task-sdk/src/airflow/sdk/io/store.py`** -> AI Confidence: **99.23%**
527. **`registry/src/_data/providerVersions.js`** -> AI Confidence: **99.23%**
528. **`airflow-core/src/airflow/ui/src/components/ActionAccordion/ActionAccordion.tsx`** -> AI Confidence: **99.23%**
529. **`airflow-core/src/airflow/ui/src/components/DagRunInfo.tsx`** -> AI Confidence: **99.23%**
530. **`airflow-core/src/airflow/ui/src/components/PoolBar.tsx`** -> AI Confidence: **99.23%**
531. **`airflow-core/src/airflow/ui/src/components/TriggerDag/TriggerDAGModal.tsx`** -> AI Confidence: **99.23%**
532. **`airflow-core/src/airflow/ui/src/layouts/BaseLayout.tsx`** -> AI Confidence: **99.23%**
533. **`airflow-core/src/airflow/ui/src/pages/Dashboard/Stats/PluginImportErrors.tsx`** -> AI Confidence: **99.23%**
534. **`airflow-core/src/airflow/ui/src/pages/XCom/XComModal.tsx`** -> AI Confidence: **99.23%**
535. **`airflow-core/src/airflow/ui/src/queries/useClearTaskInstances.ts`** -> AI Confidence: **99.23%**
536. **`go-sdk/edge/commands/run.go`** -> AI Confidence: **99.23%**
537. **`go-sdk/pkg/logging/shclog/shclog.go`** -> AI Confidence: **99.23%**
538. **`go-sdk/sdk/client.go`** -> AI Confidence: **99.23%**
539. **`airflow-core/src/airflow/ui/src/hooks/useSelectedVersion.ts`** -> AI Confidence: **99.2%**
540. **`airflow-core/src/airflow/ui/src/utils/query.ts`** -> AI Confidence: **99.2%**
541. **`airflow-core/src/airflow/__main__.py`** -> AI Confidence: **99.18%**
542. **`airflow-core/src/airflow/api/common/delete_dag.py`** -> AI Confidence: **99.18%**
543. **`airflow-core/src/airflow/api_fastapi/auth/middlewares/refresh_token.py`** -> AI Confidence: **99.18%**
544. **`airflow-core/src/airflow/api_fastapi/common/db/dag_runs.py`** -> AI Confidence: **99.18%**
545. **`airflow-core/src/airflow/api_fastapi/common/exceptions.py`** -> AI Confidence: **99.18%**
546. **`airflow-core/src/airflow/api_fastapi/core_api/app.py`** -> AI Confidence: **99.18%**
547. **`airflow-core/src/airflow/api_fastapi/core_api/datamodels/dag_run.py`** -> AI Confidence: **99.18%**
548. **`airflow-core/src/airflow/api_fastapi/core_api/routes/public/auth.py`** -> AI Confidence: **99.18%**
549. **`airflow-core/src/airflow/api_fastapi/core_api/routes/public/backfills.py`** -> AI Confidence: **99.18%**
550. **`airflow-core/src/airflow/api_fastapi/core_api/routes/public/config.py`** -> AI Confidence: **99.18%**
551. **`airflow-core/src/airflow/api_fastapi/core_api/routes/public/connections.py`** -> AI Confidence: **99.18%**
552. **`airflow-core/src/airflow/api_fastapi/core_api/routes/public/hitl.py`** -> AI Confidence: **99.18%**
553. **`airflow-core/src/airflow/api_fastapi/core_api/routes/public/import_error.py`** -> AI Confidence: **99.18%**
554. **`airflow-core/src/airflow/api_fastapi/core_api/routes/public/log.py`** -> AI Confidence: **99.18%**
555. **`airflow-core/src/airflow/api_fastapi/core_api/routes/ui/dags.py`** -> AI Confidence: **99.18%**
556. **`airflow-core/src/airflow/api_fastapi/core_api/routes/ui/dashboard.py`** -> AI Confidence: **99.18%**
557. **`airflow-core/src/airflow/api_fastapi/core_api/routes/ui/deadlines.py`** -> AI Confidence: **99.18%**
558. **`airflow-core/src/airflow/api_fastapi/core_api/services/public/config.py`** -> AI Confidence: **99.18%**
559. **`airflow-core/src/airflow/api_fastapi/core_api/services/public/dag_run.py`** -> AI Confidence: **99.18%**
560. **`airflow-core/src/airflow/cli/commands/backfill_command.py`** -> AI Confidence: **99.18%**
561. **`airflow-core/src/airflow/cli/commands/pool_command.py`** -> AI Confidence: **99.18%**
562. **`airflow-core/src/airflow/cli/commands/scheduler_command.py`** -> AI Confidence: **99.18%**
563. **`airflow-core/src/airflow/cli/commands/standalone_command.py`** -> AI Confidence: **99.18%**
564. **`airflow-core/src/airflow/cli/commands/triggerer_command.py`** -> AI Confidence: **99.18%**
565. **`airflow-core/src/airflow/dag_processing/bundles/base.py`** -> AI Confidence: **99.18%**
566. **`airflow-core/src/airflow/example_dags/plugins/event_listener.py`** -> AI Confidence: **99.18%**
567. **`airflow-core/src/airflow/executors/base_executor.py`** -> AI Confidence: **99.18%**
568. **`airflow-core/src/airflow/executors/workloads/callback.py`** -> AI Confidence: **99.18%**
569. **`airflow-core/src/airflow/models/asset.py`** -> AI Confidence: **99.18%**
570. **`airflow-core/src/airflow/models/dag.py`** -> AI Confidence: **99.18%**
571. **`airflow-core/src/airflow/models/dagbundle.py`** -> AI Confidence: **99.18%**
572. **`airflow-core/src/airflow/models/deadline.py`** -> AI Confidence: **99.18%**
573. **`airflow-core/src/airflow/models/deadline_alert.py`** -> AI Confidence: **99.18%**
574. **`airflow-core/src/airflow/models/expandinput.py`** -> AI Confidence: **99.18%**
575. **`airflow-core/src/airflow/models/pool.py`** -> AI Confidence: **99.18%**
576. **`airflow-core/src/airflow/models/trigger.py`** -> AI Confidence: **99.18%**
577. **`airflow-core/src/airflow/serialization/definitions/deadline.py`** -> AI Confidence: **99.18%**
578. **`airflow-core/src/airflow/serialization/definitions/operatorlink.py`** -> AI Confidence: **99.18%**
579. **`airflow-core/src/airflow/serialization/definitions/xcom_arg.py`** -> AI Confidence: **99.18%**
580. **`airflow-core/src/airflow/serialization/encoders.py`** -> AI Confidence: **99.18%**
581. **`airflow-core/src/airflow/ti_deps/dep_context.py`** -> AI Confidence: **99.18%**
582. **`airflow-core/src/airflow/timetables/_cron.py`** -> AI Confidence: **99.18%**
583. **`airflow-core/src/airflow/timetables/interval.py`** -> AI Confidence: **99.18%**
584. **`airflow-core/src/airflow/timetables/simple.py`** -> AI Confidence: **99.18%**
585. **`airflow-core/src/airflow/utils/cli_action_loggers.py`** -> AI Confidence: **99.18%**
586. **`airflow-core/src/airflow/utils/context.py`** -> AI Confidence: **99.18%**
587. **`airflow-core/src/airflow/utils/scheduler_health.py`** -> AI Confidence: **99.18%**
588. **`airflow-core/src/airflow/utils/serve_logs/log_server.py`** -> AI Confidence: **99.18%**
589. **`airflow-core/src/airflow/utils/session.py`** -> AI Confidence: **99.18%**
590. **`airflow-core/tests/integration/cli/commands/test_celery_command.py`** -> AI Confidence: **99.18%**
591. **`airflow-core/tests/unit/always/test_connection.py`** -> AI Confidence: **99.18%**
592. **`airflow-core/tests/unit/always/test_secrets_metastore.py`** -> AI Confidence: **99.18%**
593. **`airflow-core/tests/unit/api_fastapi/common/test_parameters.py`** -> AI Confidence: **99.18%**
594. **`airflow-core/tests/unit/api_fastapi/core_api/routes/public/test_backfills.py`** -> AI Confidence: **99.18%**
595. **`airflow-core/tests/unit/api_fastapi/core_api/routes/public/test_dag_run.py`** -> AI Confidence: **99.18%**
596. **`airflow-core/tests/unit/api_fastapi/core_api/routes/public/test_dags.py`** -> AI Confidence: **99.18%**
597. **`airflow-core/tests/unit/api_fastapi/core_api/routes/public/test_event_logs.py`** -> AI Confidence: **99.18%**
598. **`airflow-core/tests/unit/api_fastapi/core_api/routes/public/test_log.py`** -> AI Confidence: **99.18%**
599. **`airflow-core/tests/unit/api_fastapi/core_api/routes/public/test_task_instances.py`** -> AI Confidence: **99.18%**
600. **`airflow-core/tests/unit/api_fastapi/core_api/routes/public/test_variables.py`** -> AI Confidence: **99.18%**
601. **`airflow-core/tests/unit/api_fastapi/core_api/routes/public/test_xcom.py`** -> AI Confidence: **99.18%**
602. **`airflow-core/tests/unit/api_fastapi/core_api/routes/ui/test_gantt.py`** -> AI Confidence: **99.18%**
603. **`airflow-core/tests/unit/api_fastapi/core_api/routes/ui/test_structure.py`** -> AI Confidence: **99.18%**
604. **`airflow-core/tests/unit/api_fastapi/test_app.py`** -> AI Confidence: **99.18%**
605. **`airflow-core/tests/unit/cli/commands/test_dag_command.py`** -> AI Confidence: **99.18%**
606. **`airflow-core/tests/unit/cli/commands/test_db_command.py`** -> AI Confidence: **99.18%**
607. **`airflow-core/tests/unit/core/test_configuration.py`** -> AI Confidence: **99.18%**
608. **`airflow-core/tests/unit/dag_processing/bundles/test_base.py`** -> AI Confidence: **99.18%**
609. **`airflow-core/tests/unit/dag_processing/bundles/test_dag_bundle_manager.py`** -> AI Confidence: **99.18%**
610. **`airflow-core/tests/unit/dag_processing/test_dagbag.py`** -> AI Confidence: **99.18%**
611. **`airflow-core/tests/unit/dag_processing/test_manager.py`** -> AI Confidence: **99.18%**
612. **`airflow-core/tests/unit/models/test_dagrun.py`** -> AI Confidence: **99.18%**
613. **`airflow-core/tests/unit/models/test_deadline.py`** -> AI Confidence: **99.18%**
614. **`airflow-core/tests/unit/models/test_serialized_dag.py`** -> AI Confidence: **99.18%**
615. **`airflow-core/tests/unit/models/test_trigger.py`** -> AI Confidence: **99.18%**
616. **`airflow-core/tests/unit/security/test_kerberos.py`** -> AI Confidence: **99.18%**
617. **`airflow-core/tests/unit/serialization/test_dag_serialization.py`** -> AI Confidence: **99.18%**
618. **`airflow-core/tests/unit/utils/test_db_cleanup.py`** -> AI Confidence: **99.18%**
619. **`airflow-core/tests/unit/utils/test_log_handlers.py`** -> AI Confidence: **99.18%**
620. **`airflow-core/tests/unit/utils/test_retries.py`** -> AI Confidence: **99.18%**
621. **`airflow-core/tests/unit/utils/test_sqlalchemy.py`** -> AI Confidence: **99.18%**
622. **`airflow-core/tests/unit/utils/test_state.py`** -> AI Confidence: **99.18%**
623. **`airflow-core/tests/unit/utils/test_task_group.py`** -> AI Confidence: **99.18%**
624. **`airflow-ctl/tests/airflow_ctl/api/test_client.py`** -> AI Confidence: **99.18%**
625. **`airflow-ctl/tests/airflow_ctl/ctl/test_cli_config.py`** -> AI Confidence: **99.18%**
626. **`dev/breeze/src/airflow_breeze/commands/common_image_options.py`** -> AI Confidence: **99.18%**
627. **`dev/breeze/src/airflow_breeze/params/common_build_params.py`** -> AI Confidence: **99.18%**
628. **`dev/breeze/tests/test_packages.py`** -> AI Confidence: **99.18%**
629. **`dev/breeze/tests/test_selective_checks.py`** -> AI Confidence: **99.18%**
630. **`dev/prepare_bulk_issues.py`** -> AI Confidence: **99.18%**
631. **`dev/registry/tests/test_extract_parameters.py`** -> AI Confidence: **99.18%**
632. **`devel-common/src/sphinx_exts/docs_build/dev_index_generator.py`** -> AI Confidence: **99.18%**
633. **`devel-common/src/sphinx_exts/generate_erd.py`** -> AI Confidence: **99.18%**
634. **`devel-common/src/sphinx_exts/substitution_extensions.py`** -> AI Confidence: **99.18%**
635. **`devel-common/src/tests_common/test_utils/api_client_helpers.py`** -> AI Confidence: **99.18%**
636. **`devel-common/src/tests_common/test_utils/file_task_handler.py`** -> AI Confidence: **99.18%**
637. **`devel-common/src/tests_common/test_utils/gcp_system_helpers.py`** -> AI Confidence: **99.18%**
638. **`devel-common/src/tests_common/test_utils/providers.py`** -> AI Confidence: **99.18%**
639. **`devel-common/src/tests_common/test_utils/salesforce_system_helpers.py`** -> AI Confidence: **99.18%**
640. **`devel-common/src/tests_common/test_utils/taskinstance.py`** -> AI Confidence: **99.18%**
641. **`helm-tests/tests/helm_tests/security/test_extra_configmaps_secrets.py`** -> AI Confidence: **99.18%**
642. **`performance/tests/test_performance_dag.py`** -> AI Confidence: **99.18%**
643. **`providers/airbyte/src/airflow/providers/airbyte/hooks/airbyte.py`** -> AI Confidence: **99.18%**
644. **`providers/airbyte/src/airflow/providers/airbyte/triggers/airbyte.py`** -> AI Confidence: **99.18%**
645. **`providers/alibaba/src/airflow/providers/alibaba/cloud/operators/maxcompute.py`** -> AI Confidence: **99.18%**
646. **`providers/amazon/src/airflow/providers/amazon/aws/auth_manager/routes/login.py`** -> AI Confidence: **99.18%**
647. **`providers/amazon/src/airflow/providers/amazon/aws/executors/ecs/utils.py`** -> AI Confidence: **99.18%**
648. **`providers/amazon/src/airflow/providers/amazon/aws/hooks/batch_waiters.py`** -> AI Confidence: **99.18%**
649. **`providers/amazon/src/airflow/providers/amazon/aws/hooks/chime.py`** -> AI Confidence: **99.18%**
650. **`providers/amazon/src/airflow/providers/amazon/aws/hooks/ec2.py`** -> AI Confidence: **99.18%**
651. **`providers/amazon/src/airflow/providers/amazon/aws/hooks/ecr.py`** -> AI Confidence: **99.18%**
652. **`providers/amazon/src/airflow/providers/amazon/aws/hooks/rds.py`** -> AI Confidence: **99.18%**
653. **`providers/amazon/src/airflow/providers/amazon/aws/links/emr.py`** -> AI Confidence: **99.18%**
654. **`providers/amazon/src/airflow/providers/amazon/aws/operators/comprehend.py`** -> AI Confidence: **99.18%**
655. **`providers/amazon/src/airflow/providers/amazon/aws/operators/lambda_function.py`** -> AI Confidence: **99.18%**
656. **`providers/amazon/src/airflow/providers/amazon/aws/operators/mwaa.py`** -> AI Confidence: **99.18%**
657. **`providers/amazon/src/airflow/providers/amazon/aws/sensors/bedrock.py`** -> AI Confidence: **99.18%**
658. **`providers/amazon/src/airflow/providers/amazon/aws/sensors/dms.py`** -> AI Confidence: **99.18%**
659. **`providers/amazon/src/airflow/providers/amazon/aws/sensors/dynamodb.py`** -> AI Confidence: **99.18%**
660. **`providers/amazon/src/airflow/providers/amazon/aws/sensors/opensearch_serverless.py`** -> AI Confidence: **99.18%**
661. **`providers/amazon/src/airflow/providers/amazon/aws/sensors/ssm.py`** -> AI Confidence: **99.18%**
662. **`providers/amazon/src/airflow/providers/amazon/aws/transfers/dynamodb_to_s3.py`** -> AI Confidence: **99.18%**
663. **`providers/amazon/src/airflow/providers/amazon/aws/transfers/hive_to_dynamodb.py`** -> AI Confidence: **99.18%**
664. **`providers/amazon/src/airflow/providers/amazon/aws/transfers/sftp_to_s3.py`** -> AI Confidence: **99.18%**
665. **`providers/amazon/src/airflow/providers/amazon/aws/triggers/eks.py`** -> AI Confidence: **99.18%**
666. **`providers/amazon/src/airflow/providers/amazon/aws/triggers/ssm.py`** -> AI Confidence: **99.18%**
667. **`providers/amazon/src/airflow/providers/amazon/aws/utils/task_log_fetcher.py`** -> AI Confidence: **99.18%**
668. **`providers/amazon/tests/system/amazon/aws/example_bedrock_retrieve_and_generate.py`** -> AI Confidence: **99.18%**
669. **`providers/amazon/tests/system/amazon/aws/example_ses.py`** -> AI Confidence: **99.18%**
670. **`providers/amazon/tests/system/amazon/aws/utils/ec2.py`** -> AI Confidence: **99.18%**
671. **`providers/amazon/tests/unit/amazon/aws/auth_manager/avp/test_facade.py`** -> AI Confidence: **99.18%**
672. **`providers/amazon/tests/unit/amazon/aws/bundles/test_s3.py`** -> AI Confidence: **99.18%**
673. **`providers/amazon/tests/unit/amazon/aws/hooks/test_base_aws.py`** -> AI Confidence: **99.18%**
674. **`providers/amazon/tests/unit/amazon/aws/hooks/test_emr.py`** -> AI Confidence: **99.18%**
675. **`providers/amazon/tests/unit/amazon/aws/hooks/test_glue.py`** -> AI Confidence: **99.18%**
676. **`providers/amazon/tests/unit/amazon/aws/hooks/test_rds.py`** -> AI Confidence: **99.18%**
677. **`providers/amazon/tests/unit/amazon/aws/hooks/test_sagemaker_unified_studio.py`** -> AI Confidence: **99.18%**
678. **`providers/amazon/tests/unit/amazon/aws/operators/test_ecs.py`** -> AI Confidence: **99.18%**
679. **`providers/amazon/tests/unit/amazon/aws/operators/test_eks.py`** -> AI Confidence: **99.18%**
680. **`providers/amazon/tests/unit/amazon/aws/operators/test_emr_serverless.py`** -> AI Confidence: **99.18%**
681. **`providers/amazon/tests/unit/amazon/aws/sensors/test_emr_step.py`** -> AI Confidence: **99.18%**
682. **`providers/amazon/tests/unit/amazon/aws/sensors/test_s3.py`** -> AI Confidence: **99.18%**
683. **`providers/amazon/tests/unit/amazon/aws/sensors/test_sqs.py`** -> AI Confidence: **99.18%**
684. **`providers/amazon/tests/unit/amazon/aws/system/utils/test_helpers.py`** -> AI Confidence: **99.18%**
685. **`providers/amazon/tests/unit/amazon/aws/transfers/test_gcs_to_s3.py`** -> AI Confidence: **99.18%**
686. **`providers/amazon/tests/unit/amazon/aws/triggers/test_opensearch_serverless.py`** -> AI Confidence: **99.18%**
687. **`providers/amazon/tests/unit/amazon/aws/utils/test_connection_wrapper.py`** -> AI Confidence: **99.18%**
688. **`providers/amazon/tests/unit/amazon/aws/waiters/test_custom_waiters.py`** -> AI Confidence: **99.18%**
689. **`providers/apache/beam/src/airflow/providers/apache/beam/triggers/beam.py`** -> AI Confidence: **99.18%**
690. **`providers/apache/cassandra/tests/integration/apache/cassandra/hooks/test_cassandra.py`** -> AI Confidence: **99.18%**
691. **`providers/apache/drill/src/airflow/providers/apache/drill/hooks/drill.py`** -> AI Confidence: **99.18%**
692. **`providers/apache/hive/src/airflow/providers/apache/hive/transfers/hive_to_mysql.py`** -> AI Confidence: **99.18%**
693. **`providers/apache/hive/src/airflow/providers/apache/hive/transfers/mssql_to_hive.py`** -> AI Confidence: **99.18%**
694. **`providers/apache/hive/src/airflow/providers/apache/hive/transfers/mysql_to_hive.py`** -> AI Confidence: **99.18%**
695. **`providers/apache/hive/tests/unit/apache/hive/hooks/test_hive.py`** -> AI Confidence: **99.18%**
696. **`providers/apache/hive/tests/unit/apache/hive/operators/test_hive_stats.py`** -> AI Confidence: **99.18%**
697. **`providers/apache/impala/tests/unit/apache/impala/hooks/test_impala_sql.py`** -> AI Confidence: **99.18%**
698. **`providers/apache/kafka/src/airflow/providers/apache/kafka/hooks/base.py`** -> AI Confidence: **99.18%**
699. **`providers/apache/kafka/src/airflow/providers/apache/kafka/triggers/await_message.py`** -> AI Confidence: **99.18%**
700. **`providers/apache/kafka/tests/system/apache/kafka/example_dag_hello_kafka.py`** -> AI Confidence: **99.18%**
701. **`providers/apache/livy/tests/unit/apache/livy/sensors/test_livy.py`** -> AI Confidence: **99.18%**
702. **`providers/apache/spark/src/airflow/providers/apache/spark/hooks/spark_connect.py`** -> AI Confidence: **99.18%**
703. **`providers/apprise/src/airflow/providers/apprise/hooks/apprise.py`** -> AI Confidence: **99.18%**
704. **`providers/arangodb/src/airflow/providers/arangodb/hooks/arangodb.py`** -> AI Confidence: **99.18%**
705. **`providers/atlassian/jira/src/airflow/providers/atlassian/jira/hooks/jira.py`** -> AI Confidence: **99.18%**
706. **`providers/celery/src/airflow/providers/celery/executors/celery_kubernetes_executor.py`** -> AI Confidence: **99.18%**
707. **`providers/celery/tests/integration/celery/test_celery_executor.py`** -> AI Confidence: **99.18%**
708. **`providers/celery/tests/unit/celery/cli/test_celery_command.py`** -> AI Confidence: **99.18%**
709. **`providers/celery/tests/unit/celery/executors/test_celery_executor.py`** -> AI Confidence: **99.18%**
710. **`providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/cli/definition.py`** -> AI Confidence: **99.18%**
711. **`providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/kubernetes_helper_functions.py`** -> AI Confidence: **99.18%**
712. **`providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/secrets/kubernetes_secrets_backend.py`** -> AI Confidence: **99.18%**
713. **`providers/cncf/kubernetes/tests/unit/cncf/kubernetes/decorators/test_kubernetes_cmd.py`** -> AI Confidence: **99.18%**
714. **`providers/cncf/kubernetes/tests/unit/cncf/kubernetes/decorators/test_kubernetes_commons.py`** -> AI Confidence: **99.18%**
715. **`providers/cncf/kubernetes/tests/unit/cncf/kubernetes/executors/test_kubernetes_executor.py`** -> AI Confidence: **99.18%**
716. **`providers/cncf/kubernetes/tests/unit/cncf/kubernetes/operators/test_job.py`** -> AI Confidence: **99.18%**
717. **`providers/cncf/kubernetes/tests/unit/cncf/kubernetes/operators/test_kueue.py`** -> AI Confidence: **99.18%**
718. **`providers/cncf/kubernetes/tests/unit/cncf/kubernetes/operators/test_pod.py`** -> AI Confidence: **99.18%**
719. **`providers/cncf/kubernetes/tests/unit/cncf/kubernetes/test_pod_generator.py`** -> AI Confidence: **99.18%**
720. **`providers/cncf/kubernetes/tests/unit/cncf/kubernetes/utils/test_pod_manager.py`** -> AI Confidence: **99.18%**
721. **`providers/cohere/src/airflow/providers/cohere/hooks/cohere.py`** -> AI Confidence: **99.18%**
722. **`providers/common/ai/src/airflow/providers/common/ai/durable/storage.py`** -> AI Confidence: **99.18%**
723. **`providers/common/ai/src/airflow/providers/common/ai/plugins/hitl_review.py`** -> AI Confidence: **99.18%**
724. **`providers/common/ai/src/airflow/providers/common/ai/toolsets/datafusion.py`** -> AI Confidence: **99.18%**
725. **`providers/common/ai/tests/unit/common/ai/mixins/test_hitl_review.py`** -> AI Confidence: **99.18%**
726. **`providers/common/ai/tests/unit/common/ai/utils/test_file_analysis.py`** -> AI Confidence: **99.18%**
727. **`providers/common/io/src/airflow/providers/common/io/operators/file_transfer.py`** -> AI Confidence: **99.18%**
728. **`providers/common/sql/src/airflow/providers/common/sql/datafusion/format_handlers.py`** -> AI Confidence: **99.18%**
729. **`providers/common/sql/src/airflow/providers/common/sql/dialects/dialect.py`** -> AI Confidence: **99.18%**
730. **`providers/common/sql/tests/unit/common/sql/datafusion/test_engine.py`** -> AI Confidence: **99.18%**
731. **`providers/common/sql/tests/unit/common/sql/datafusion/test_format_handlers.py`** -> AI Confidence: **99.18%**
732. **`providers/databricks/src/airflow/providers/databricks/hooks/databricks.py`** -> AI Confidence: **99.18%**
733. **`providers/databricks/src/airflow/providers/databricks/sensors/databricks_sql.py`** -> AI Confidence: **99.18%**
734. **`providers/databricks/tests/unit/databricks/hooks/test_databricks_base.py`** -> AI Confidence: **99.18%**
735. **`providers/databricks/tests/unit/databricks/operators/test_databricks.py`** -> AI Confidence: **99.18%**
736. **`providers/databricks/tests/unit/databricks/plugins/test_databricks_workflow.py`** -> AI Confidence: **99.18%**
737. **`providers/databricks/tests/unit/databricks/sensors/test_databricks_partition.py`** -> AI Confidence: **99.18%**
738. **`providers/databricks/tests/unit/databricks/utils/test_openlineage.py`** -> AI Confidence: **99.18%**
739. **`providers/dbt/cloud/src/airflow/providers/dbt/cloud/sensors/dbt.py`** -> AI Confidence: **99.18%**
740. **`providers/dbt/cloud/src/airflow/providers/dbt/cloud/triggers/dbt.py`** -> AI Confidence: **99.18%**
741. **`providers/dbt/cloud/tests/unit/dbt/cloud/hooks/test_dbt.py`** -> AI Confidence: **99.18%**
742. **`providers/dbt/cloud/tests/unit/dbt/cloud/utils/test_openlineage.py`** -> AI Confidence: **99.18%**
743. **`providers/docker/src/airflow/providers/docker/decorators/docker.py`** -> AI Confidence: **99.18%**
744. **`providers/docker/tests/unit/docker/operators/test_docker_swarm.py`** -> AI Confidence: **99.18%**
745. **`providers/edge3/src/airflow/providers/edge3/example_dags/win_test.py`** -> AI Confidence: **99.18%**
746. **`providers/edge3/src/airflow/providers/edge3/plugins/edge_executor_plugin.py`** -> AI Confidence: **99.18%**
747. **`providers/edge3/src/airflow/providers/edge3/worker_api/routes/jobs.py`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `providers/google/tests/unit/google/cloud/transfers/test_gcs_to_local.py` -> **0.0013%** Exposure
- `airflow-core/tests/unit/always/test_example_dags.py` -> **0.0005%** Exposure
- `providers/apache/hive/tests/unit/apache/hive/transfers/test_mysql_to_hive.py` -> **0.0003%** Exposure
- `task-sdk/tests/task_sdk/definitions/test_param.py` -> **0.0002%** Exposure
- `dev/breeze/tests/test_pr_commands_utils.py` -> **0.0001%** Exposure
### Exploit Generation Surface
- `airflow-core/src/airflow/api/common/mark_tasks.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api_fastapi/app.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api_fastapi/auth/managers/base_auth_manager.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api_fastapi/auth/managers/simple/simple_auth_manager.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api_fastapi/auth/tokens.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `airflow-core/src/airflow/api_fastapi/auth/managers/base_auth_manager.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api_fastapi/common/parameters.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api_fastapi/core_api/routes/public/assets.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api_fastapi/core_api/routes/public/dags.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api_fastapi/core_api/routes/public/pools.py` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `providers/amazon/tests/unit/amazon/aws/utils/test_redshift.py` -> **100.0%** Exposure
- `providers/microsoft/azure/tests/unit/microsoft/azure/fs/test_msgraph.py` -> **100.0%** Exposure
- `providers/openai/tests/unit/openai/hooks/test_openai.py` -> **100.0%** Exposure
- `providers/pagerduty/tests/unit/pagerduty/hooks/test_pagerduty.py` -> **100.0%** Exposure
- `providers/ssh/tests/unit/ssh/hooks/test_ssh_async.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `airflow-core/src/airflow/api/client/local_client.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api_fastapi/auth/managers/base_auth_manager.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api_fastapi/auth/managers/simple/simple_auth_manager.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api_fastapi/auth/tokens.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api_fastapi/common/parameters.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `137` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `46036` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `registry/src/js/connection-builder.js` (JAVASCRIPT) -> Cumulative Risk: **1020.74**
- **Archetype:** `file_cluster_17` (Distance: 13.382 IQR)
- **Magnitude:** 574.88 | **LOC:** 421 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `renderField` (Impact: 143.7), `generateURI` (Impact: 86.0), `generateJSON` (Impact: 41.5)

### 2. `task-sdk/src/airflow/sdk/execution_time/callback_runner.py` (PYTHON) -> Cumulative Risk: **937.63**
- **Archetype:** `file_cluster_13` (Distance: 11.118 IQR)
- **Magnitude:** 120.06 | **LOC:** 175 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `run` (Impact: 50.1), `run` (Impact: 31.2), `__call__` (Impact: 1.8)

### 3. `providers/elasticsearch/src/airflow/providers/elasticsearch/hooks/elasticsearch.py` (PYTHON) -> Cumulative Risk: **915.69**
- **Archetype:** `file_cluster_13` (Distance: 11.587 IQR)
- **Magnitude:** 228.3 | **LOC:** 271 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `get_uri` (Impact: 31.6), `get_conn` (Impact: 18.3), `__init__` (Impact: 12.2)

### 4. `providers/apache/beam/src/airflow/providers/apache/beam/operators/beam.py` (PYTHON) -> Cumulative Risk: **896.36**
- **Archetype:** `file_cluster_13` (Distance: 11.303 IQR)
- **Magnitude:** 703.92 | **LOC:** 961 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `execute_on_dataflow` (Impact: 107.4), `execute` (Impact: 94.0), `on_kill` (Impact: 57.4)

### 5. `providers/databricks/src/airflow/providers/databricks/operators/databricks.py` (PYTHON) -> Cumulative Risk: **894.79**
- **Archetype:** `file_cluster_16` (Distance: 12.308 IQR)
- **Magnitude:** 1480.1 | **LOC:** 1708 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 12.5%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `_handle_databricks_operator_execution` (Impact: 425.8), `_handle_terminal_run_state` (Impact: 270.1), `execute` (Impact: 94.9)

### 6. `airflow-core/src/airflow/utils/thread_safe_dict.py` (PYTHON) -> Cumulative Risk: **892.59**
- **Archetype:** `file_cluster_4` (Distance: 11.564 IQR)
- **Magnitude:** 82.64 | **LOC:** 50 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `get` (Impact: 14.0), `clear` (Impact: 14.0), `delete` (Impact: 13.2)

### 7. `providers/databricks/src/airflow/providers/databricks/hooks/databricks.py` (PYTHON) -> Cumulative Risk: **890.71**
- **Archetype:** `file_cluster_16` (Distance: 11.887 IQR)
- **Magnitude:** 490.08 | **LOC:** 917 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9988%)
- **Heaviest Functions:** `reset_job` (Impact: 204.9), `__init__` (Impact: 18.9), `__eq__` (Impact: 14.3)

### 8. `providers/apache/beam/src/airflow/providers/apache/beam/triggers/beam.py` (PYTHON) -> Cumulative Risk: **882.74**
- **Archetype:** `file_cluster_13` (Distance: 11.03 IQR)
- **Magnitude:** 184.86 | **LOC:** 234 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `run` (Impact: 57.6), `run` (Impact: 37.5), `provide_gcs_tempfile` (Impact: 10.0)

### 9. `providers/amazon/src/airflow/providers/amazon/aws/sensors/s3.py` (PYTHON) -> Cumulative Risk: **879.64**
- **Archetype:** `file_cluster_13` (Distance: 11.862 IQR)
- **Magnitude:** 469.64 | **LOC:** 402 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_check_key` (Impact: 185.6), `is_keys_unchanged` (Impact: 49.7), `execute` (Impact: 49.7)

### 10. `providers/openai/src/airflow/providers/openai/operators/openai.py` (PYTHON) -> Cumulative Risk: **867.41**
- **Archetype:** `file_cluster_13` (Distance: 11.583 IQR)
- **Magnitude:** 122.92 | **LOC:** 169 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `execute` (Impact: 37.8), `execute` (Impact: 26.4), `on_kill` (Impact: 14.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `providers/fab/tests/unit/fab/auth_manager/test_security.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.832 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.463 IQR)
- **Top Global Matches:** file_cluster_8: 10.832, file_cluster_0: 11.087, file_cluster_13: 11.088
- **Magnitude:** 8164.45 | **LOC:** 1211 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.7408%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 287`, `args: 69`, `func_start: 69`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 3`
* *Architecture:* `io: 4`, `api: 58`, `import: 41`
* *Defense:* `safety: 116`, `doc: 4`, `test: 194`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` tests_common.test_utils.version_compat, tests_common.test_utils.config, time_machine, airflow.providers.fab.auth_manager.security_manager, airflow.providers.fab.auth_manager.security_manager.override, __future__, logging, airflow.api_fastapi.auth.managers.models.resource_details...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/breeze/src/airflow_breeze/utils/tui_display.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.628 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.633 IQR)
- **Top Global Matches:** file_cluster_8: 12.628, file_cluster_13: 12.673, file_cluster_16: 12.726
- **Magnitude:** 7750.8 | **LOC:** 1983 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 203
- **Risk Profile:** Cognitive Load (47.8378%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_parse_sgr_mouse` (Impact: 7217.6 | O(2^N) | DB: 203)
  * `_are_only_static_checks` (Impact: 12.3 | O(N^2))
  * `_get_terminal_size` (Impact: 5.6 | O(N^2) | DB: 3)
  * `_enable_mouse` (Impact: 5.5 | O(N^2) | DB: 6)
  * `_disable_mouse` (Impact: 5.5 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 515`, `structural_boundaries: 312`, `args: 50`, `func_start: 49`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 439`
* *Architecture:* `io: 16`, `api: 28`, `import: 25`
* *Defense:* `safety: 17`, `doc: 106`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` select, termios, airflow_breeze.utils.console, __future__, rich.syntax, enum, io, typing...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `airflow-core/src/airflow/jobs/scheduler_job_runner.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.807 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.406 IQR)
- **Top Global Matches:** file_cluster_8: 11.807, file_cluster_13: 11.894, file_cluster_7: 12.07
- **Magnitude:** 6196.0 | **LOC:** 3261 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 14.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (7.8591%), Tech Debt (10.1117%)
**Top Internal Functions/Classes:**
  * `_ensure_ti_has_dag_version_id` (Impact: 6053.4 | O(2^N) | DB: 63)
  * `_eager_load_dag_run_for_validation` (Impact: 3.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 422`, `structural_boundaries: 353`, `args: 65`, `func_start: 64`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 80`, `planned_debt: 11`, `fragile_debt: 1`
* *Architecture:* `io: 19`, `api: 8`, `concurrency: 4`, `import: 84`
* *Defense:* `safety: 50`, `doc: 110`, `test: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.191
  * `Choke Point (Betweenness):` 0.000435 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 47):` airflow.models.dagbag, __future__, airflow._shared.observability.metrics.dual_stats_manager, airflow.models.taskinstance, tracemalloc, airflow.utils.session, airflow._shared.observability.metrics.stats, collections...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `airflow-core/tests/unit/utils/test_task_group.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.103 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.037 IQR)
- **Top Global Matches:** file_cluster_8: 10.103, file_cluster_0: 10.524, file_cluster_7: 10.609
- **Magnitude:** 5799.0 | **LOC:** 1202 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.4332%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 201`, `args: 63`, `func_start: 63`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 63`, `concurrency: 32`, `import: 18`
* *Defense:* `safety: 45`, `doc: 52`, `test: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` airflow.providers.standard.operators.bash, airflow.providers.standard.operators.empty, unit.models, tests_common.test_utils.dag, airflow.api_fastapi.core_api.services.ui.task_group, airflow.providers.standard.operators.python, __future__, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devel-common/src/tests_common/pytest_plugin.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.233 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.736 IQR)
- **Top Global Matches:** file_cluster_13: 12.233, file_cluster_0: 12.521, file_cluster_11: 12.59
- **Magnitude:** 5458.82 | **LOC:** 3010 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 26.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 225
- **Risk Profile:** Cognitive Load (16.4527%), Tech Debt (10.001%)
**Top Internal Functions/Classes:**
  * `get_all_provider_pyproject_toml_provider` (Impact: 5090.3 | O(2^N) | DB: 225)
  * `listener_manager` (Impact: 25.6 | O(N^3) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 437`, `structural_boundaries: 636`, `args: 148`, `func_start: 140`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 186`, `dead_code: 6`, `planned_debt: 6`, `fragile_debt: 2`
* *Architecture:* `io: 70`, `api: 114`, `import: 185`
* *Defense:* `safety: 72`, `doc: 83`, `test: 148`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.081
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 63):` airflow.sdk.definitions.dag, hashlib, airflow., airflow.providers_manager, airflow.listeners.listener, code, airflow.models.dagbag, airflow.timetables.base...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `airflow-core/tests/unit/jobs/test_scheduler_job.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.432 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.835 IQR)
- **Top Global Matches:** file_cluster_8: 13.432, file_cluster_0: 13.546, file_cluster_13: 13.59
- **Magnitude:** 4774.62 | **LOC:** 9620 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 25.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 172
- **Risk Profile:** Cognitive Load (4.274%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_only_idle_no_dags_exits_after_n_idl` (Impact: 2430.3 | O(N^6) | DB: 172)
  * `test_activate_referenced_assets_no_in_ch` (Impact: 306.8 | O(N^6) | DB: 36)
    * *Intent:* # The DAG parser finds asset5. orphaned, active = self._find_assets_activation(session) assert activ...
  * `test_partitioned_dag_run_with_invalid_ma` (Impact: 184.5 | O(N^5))
  * `test_retry_on_db_error_when_update_timeo` (Impact: 97.6 | O(2^N) | DB: 5)
  * `test_should_mark_empty_task_as_success` (Impact: 64.2 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 542`, `structural_boundaries: 1282`, `args: 290`, `func_start: 276`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 54`, `high_risk_execution: 4`, `state_mutation: 378`, `dead_code: 4`, `planned_debt: 5`, `fragile_debt: 2`, `duplicate_logic: 12`, `orphaned_logic: 46`
* *Architecture:* `io: 19`, `api: 251`, `import: 89`
* *Defense:* `safety: 731`, `doc: 278`, `test: 1096`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 57):` airflow.timetables.base, __future__, airflow.models.taskinstance, airflow.partition_mappers.base, airflow.utils.session, airflow.models.taskinstancehistory, collections, airflow._shared.timezones...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `providers/teradata/src/airflow/providers/teradata/operators/tpt.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.864 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.886 IQR)
- **Top Global Matches:** file_cluster_8: 11.864, file_cluster_13: 11.956, file_cluster_16: 12.098
- **Magnitude:** 3729.42 | **LOC:** 641 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (18.4643%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 62`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 57`
* *Architecture:* `io: 1`, `api: 6`, `import: 10`
* *Defense:* `safety: 21`, `doc: 63`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.092
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` typing, airflow.providers.teradata.hooks.teradata, airflow.providers.ssh.hooks.ssh, airflow.providers.teradata.utils.tpt_util, __future__, airflow.sdk, logging, paramiko...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `task-sdk/src/airflow/sdk/execution_time/task_runner.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.407 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.657 IQR)
- **Top Global Matches:** file_cluster_13: 12.407, file_cluster_8: 12.767, file_cluster_11: 12.794
- **Magnitude:** 3133.48 | **LOC:** 1923 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 31.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 83
- **Risk Profile:** Cognitive Load (16.9742%), Tech Debt (10.2358%)
**Top Internal Functions/Classes:**
  * `startup` (Impact: 2724.3 | O(2^N) | DB: 83)
  * `get_template_context` (Impact: 65.3 | O(N^6) | DB: 4)
  * `_make_task_span` (Impact: 41.0 | O(N^4))
  * `log_url` (Impact: 24.9 | O(N^3))
  * `parse` (Impact: 23.9 | O(N^3) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 273`, `structural_boundaries: 320`, `args: 50`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 69`, `planned_debt: 8`
* *Architecture:* `io: 33`, `api: 40`, `import: 75`
* *Defense:* `safety: 146`, `doc: 91`, `test: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.417
  * `Choke Point (Betweenness):` 0.001439 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` opentelemetry.trace.propagation.tracecontext, jinja2, airflow.providers.smtp.notifications.smtp, airflow.sdk.plugins_manager, airflow.sdk.definitions.param, urllib.parse, pathlib, structlog.typing...
  * `Imported By (In-Degree: 36):` (Excluded from Brief to save tokens)

### `airflow-core/src/airflow/serialization/serialized_objects.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.703 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.36 IQR)
- **Top Global Matches:** file_cluster_13: 12.703, file_cluster_0: 12.844, file_cluster_16: 12.92
- **Magnitude:** 3071.24 | **LOC:** 2316 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (38.733%), Tech Debt (19.6842%)
**Top Internal Functions/Classes:**
  * `default_serialization` (Impact: 2626.6 | O(N^6) | DB: 37)
  * `deref` (Impact: 69.8 | O(2^N))
  * `_is_excluded` (Impact: 23.0 | O(N^4))
  * `validate_schema` (Impact: 21.4 | O(N^3))
  * `create_scheduler_operator` (Impact: 19.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 461`, `structural_boundaries: 496`, `args: 90`, `func_start: 90`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 102`, `dead_code: 2`, `planned_debt: 6`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 57`, `concurrency: 3`, `import: 86`
* *Defense:* `safety: 117`, `doc: 136`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.269
  * `Choke Point (Betweenness):` 0.004209 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 50):` airflow.sdk.definitions.deadline, airflow.sdk.definitions.dag, kubernetes.client, airflow.serialization.definitions.operatorlink, airflow.sdk.definitions.param, airflow.serialization.definitions.node, airflow.timetables.base, dateutil...
  * `Imported By (In-Degree: 47):` (Excluded from Brief to save tokens)

### `dev/breeze/src/airflow_breeze/utils/selective_checks.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.665 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.555 IQR)
- **Top Global Matches:** file_cluster_0: 11.665, file_cluster_16: 11.749, file_cluster_8: 11.804
- **Magnitude:** 2895.88 | **LOC:** 2025 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 38.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (26.3032%), Tech Debt (25.1327%)
**Top Internal Functions/Classes:**
  * `get_job_label` (Impact: 767.9 | O(2^N) | DB: 24)
  * `provider_dependency_bump` (Impact: 376.3 | O(N^6) | DB: 10)
  * `docs_list_as_string` (Impact: 121.4 | O(N^5) | DB: 7)
  * `_get_providers_test_types_to_run` (Impact: 106.2 | O(N^5))
  * `_is_large_enough_pr` (Impact: 94.1 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 373`, `structural_boundaries: 410`, `args: 120`, `func_start: 119`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 124`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `io: 11`, `api: 134`, `import: 28`
* *Defense:* `safety: 28`, `doc: 31`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` airflow_breeze.utils.console, pathlib, __future__, airflow_breeze.utils.run_utils, airflow_breeze.utils.provider_dependencies, airflow_breeze.utils.path_utils, airflow_breeze.utils.kubernetes_utils, enum...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `providers/google/src/airflow/providers/google/cloud/operators/dataproc.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.768 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.008 IQR)
- **Top Global Matches:** file_cluster_8: 12.768, file_cluster_13: 12.897, file_cluster_7: 12.937
- **Magnitude:** 2859.32 | **LOC:** 2978 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 22.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (24.9272%), Tech Debt (97.9491%)
**Top Internal Functions/Classes:**
  * `_build_lifecycle_config` (Impact: 585.6 | O(2^N) | DB: 19)
  * `execute_complete` (Impact: 371.1 | O(2^N) | DB: 18)
  * `_reconcile_cluster_state` (Impact: 286.9 | O(2^N))
  * `execute_complete` (Impact: 261.1 | O(2^N) | DB: 21)
  * `execute_complete` (Impact: 231.2 | O(2^N) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 234`, `args: 82`, `func_start: 82`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 371`, `planned_debt: 3`, `duplicate_logic: 33`
* *Architecture:* `api: 60`, `import: 33`
* *Defense:* `safety: 35`, `doc: 308`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.242
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` airflow.providers.google.common.hooks.base_google, airflow.providers.google.cloud.hooks.dataproc, __future__, google.cloud.dataproc_v1, enum, typing, functools, time...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `providers/openlineage/src/airflow/providers/openlineage/utils/utils.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.11 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.47 IQR)
- **Top Global Matches:** file_cluster_13: 12.11, file_cluster_8: 12.241, file_cluster_16: 12.262
- **Magnitude:** 2760.66 | **LOC:** 1757 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 58.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (23.8995%), Tech Debt (9.1352%)
**Top Internal Functions/Classes:**
  * `_truncate_string_to_byte_size` (Impact: 961.5 | O(2^N) | DB: 19)
    * *Intent:* # Function already uses parent as root if root is missing, no need to explicitly pass it return _get...
  * `_redact` (Impact: 524.8 | O(2^N))
  * `deadlines` (Impact: 522.8 | O(2^N) | DB: 6)
  * `_extract_ol_info_from_asset_event` (Impact: 313.2 | O(2^N) | DB: 2)
  * `_build_labeled_edge_map` (Impact: 62.8 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 341`, `args: 83`, `func_start: 63`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 66`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 5`, `api: 59`, `import: 55`
* *Defense:* `safety: 102`, `doc: 72`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.577
  * `Choke Point (Betweenness):` 0.000245 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` openlineage.client.facet_v2, custom, airflow.providers_manager, airflow.models.mappedoperator, airflow.utils.log.secrets_masker, __future__, openlineage.client.event_v2, logging...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `providers/fab/src/airflow/providers/fab/auth_manager/security_manager/override.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.836 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.223 IQR)
- **Top Global Matches:** file_cluster_13: 12.836, file_cluster_0: 12.925, file_cluster_16: 13.027
- **Magnitude:** 2717.3 | **LOC:** 2617 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (23.7298%), Tech Debt (14.9933%)
**Top Internal Functions/Classes:**
  * `create_permission` (Impact: 1122.5 | O(N^6) | DB: 12)
  * `_init_auth` (Impact: 355.8 | O(N^6) | DB: 9)
  * `add_role` (Impact: 343.1 | O(N^6))
  * `reset_user_sessions` (Impact: 86.7 | O(N^6))
  * `register_views` (Impact: 74.3 | O(N^4) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 368`, `structural_boundaries: 441`, `args: 124`, `func_start: 124`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 107`, `dead_code: 14`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 7`, `api: 109`, `import: 56`
* *Defense:* `safety: 65`, `doc: 289`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.000934 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` airflow.providers.fab.auth_manager.views.user, airflow.models.dagbag, airflow.providers.fab.auth_manager.views.auth_oauth, __future__, logging, jmespath, airflow.providers.fab.www.security_manager, flask_appbuilder.const...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `airflow-core/src/airflow/models/taskinstance.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.764 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.242 IQR)
- **Top Global Matches:** file_cluster_13: 12.764, file_cluster_0: 13.021, file_cluster_8: 13.113
- **Magnitude:** 2554.56 | **LOC:** 2394 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 31.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (26.0232%), Tech Debt (13.4595%)
**Top Internal Functions/Classes:**
  * `set_duration` (Impact: 559.6 | O(N^6) | DB: 26)
  * `_stop_remaining_tasks` (Impact: 473.7 | O(N^6))
    * *Intent:* """ Stop non-teardown tasks in dag. :meta private: """
  * `emit_state_change_metric` (Impact: 466.6 | O(N^6) | DB: 14)
  * `next_retry_datetime` (Impact: 405.4 | O(2^N) | DB: 1)
  * `set_state` (Impact: 199.9 | O(N^5) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 377`, `args: 74`, `func_start: 74`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 211`, `dead_code: 3`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 12`, `api: 62`, `import: 90`
* *Defense:* `safety: 54`, `doc: 178`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.57
  * `Choke Point (Betweenness):` 0.004993 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 49):` airflow.models.taskmap, hashlib, airflow.listeners.listener, airflow.utils.net, dill, airflow.models.dagbag, urllib.parse, __future__...
  * `Imported By (In-Degree: 121):` (Excluded from Brief to save tokens)

### `dev/ide_setup/setup_idea.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.203 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.43 IQR)
- **Top Global Matches:** file_cluster_8: 11.203, file_cluster_16: 11.334, file_cluster_13: 11.361
- **Magnitude:** 2505.84 | **LOC:** 1228 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (11.4714%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_read_requires_python` (Impact: 2165.7 | O(2^N) | DB: 63)
    * *Intent:* """Return the ``requires-python`` value from *pyproject_path*."""
  * `main` (Impact: 161.8 | O(N^4))
  * `_build_parser` (Impact: 50.4 | O(N^2) | DB: 3)
  * `_resolve_excludes` (Impact: 24.7 | O(N^3))
  * `_validate_python_version` (Impact: 12.6 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 141`, `args: 31`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 6`, `state_mutation: 64`
* *Architecture:* `io: 16`, `api: 10`, `import: 18`
* *Defense:* `safety: 14`, `doc: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` packaging.specifiers, rich, pathlib, __future__, argparse, rich.prompt, platform, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `providers/common/sql/src/airflow/providers/common/sql/operators/sql.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.184 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.435 IQR)
- **Top Global Matches:** file_cluster_13: 12.184, file_cluster_8: 12.245, file_cluster_16: 12.266
- **Magnitude:** 2320.6 | **LOC:** 1447 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (26.196%), Tech Debt (70.4534%)
**Top Internal Functions/Classes:**
  * `execute` (Impact: 1107.5 | O(2^N) | DB: 11)
  * `execute` (Impact: 631.2 | O(2^N) | DB: 22)
  * `_hook` (Impact: 240.4 | O(2^N))
  * `get_hook` (Impact: 40.5 | O(2^N))
  * `execute` (Impact: 29.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 151`, `args: 52`, `func_start: 49`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 125`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 7`, `orphaned_logic: 2`
* *Architecture:* `api: 30`, `import: 18`
* *Defense:* `safety: 41`, `doc: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.709
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` airflow.providers.common.compat.sdk, collections.abc, typing, airflow.providers.common.sql.hooks.handlers, airflow.providers.openlineage.sqlparser, functools, airflow.utils.helpers, airflow.providers.openlineage.extractors...
  * `Imported By (In-Degree: 44):` (Excluded from Brief to save tokens)

### `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/hooks/kubernetes.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.607 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.438 IQR)
- **Top Global Matches:** file_cluster_13: 12.607, file_cluster_4: 12.712, file_cluster_0: 12.758
- **Magnitude:** 2272.08 | **LOC:** 1287 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 16.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (45.7676%), Tech Debt (22.5584%)
**Top Internal Functions/Classes:**
  * `wait_until_job_complete` (Impact: 1716.8 | O(2^N) | DB: 23)
  * `_get_field` (Impact: 171.2 | O(2^N) | DB: 4)
  * `get_connection` (Impact: 26.4 | O(2^N))
  * `_coalesce_param` (Impact: 13.2 | O(N^4))
  * `_get_request_timeout` (Impact: 11.3 | O(N^2))
    * *Intent:* """Get the client-side request timeout."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 280`, `args: 67`, `func_start: 67`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 86`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 3`, `api: 63`, `concurrency: 90`, `import: 31`
* *Defense:* `safety: 37`, `doc: 201`, `test: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` airflow.providers.common.compat.connection, kubernetes.client, flask_appbuilder.fieldwidgets, __future__, asyncio, typing, functools, kubernetes_asyncio...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `task-sdk/src/airflow/sdk/execution_time/supervisor.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.351 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.914 IQR)
- **Top Global Matches:** file_cluster_13: 12.351, file_cluster_8: 12.661, file_cluster_0: 12.679
- **Magnitude:** 2240.88 | **LOC:** 2130 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 22.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 123
- **Risk Profile:** Cognitive Load (19.5532%), Tech Debt (15.5008%)
**Top Internal Functions/Classes:**
  * `_fetch_remote_logging_conn` (Impact: 1796.9 | O(2^N) | DB: 123)
  * `handle_requests` (Impact: 38.2 | O(N^6))
  * `block_orm_access` (Impact: 32.4 | O(N^4) | DB: 9)
    * *Intent:* # If that didn't work, do the best we can return stream class BlockedDBSession: """:meta private:"""...
  * `exit` (Impact: 24.8 | O(N^3) | DB: 18)
    * *Intent:* # includes libc symbols since CPython is linked against it. libc = ctypes.CDLL(None, use_errno=True)...
  * `ensure_secrets_backend_loaded` (Impact: 18.8 | O(N^3) | DB: 3)
    * *Intent:* # This will hold our accumulated/partial binary frame if it doesn't come in a single read buffer: me...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 278`, `args: 68`, `func_start: 68`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 122`, `planned_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 82`, `api: 42`, `concurrency: 6`, `import: 65`
* *Defense:* `safety: 117`, `doc: 115`, `immutability_locks: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.001004 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` selectors, airflow.models.dagbag, urllib.parse, structlog.typing, __future__, airflow.sdk.execution_time, typing_extensions, logging...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `providers/amazon/tests/unit/amazon/aws/operators/test_dms.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.222 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.482 IQR)
- **Top Global Matches:** file_cluster_8: 10.222, file_cluster_0: 10.46, file_cluster_13: 10.828
- **Magnitude:** 2119.55 | **LOC:** 1120 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.4447%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 198`, `args: 51`, `func_start: 51`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1`, `fragile_debt: 1`
* *Architecture:* `api: 62`, `concurrency: 9`, `import: 20`
* *Defense:* `safety: 93`, `test: 213`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` tests_common.test_utils.version_compat, __future__, pendulum, typing, unit.amazon.aws.utils.test_template_fields, tests_common.test_utils.taskinstance, airflow.utils.state, airflow.utils.types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `providers/standard/tests/unit/standard/operators/test_python.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.102 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.193 IQR)
- **Top Global Matches:** file_cluster_13: 12.102, file_cluster_0: 12.147, file_cluster_8: 12.213
- **Magnitude:** 1991.5 | **LOC:** 2682 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (7.787%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_clear_skipped_downstream_task` (Impact: 81.4 | O(N^6))
  * `test_clear_skipped_downstream_task` (Impact: 75.7 | O(N^5))
    * *Intent:* """ After a downstream task is skipped by BranchPythonOperator, clearing the skipped task should not...
  * `test_clear_skipped_downstream_task` (Impact: 70.4 | O(N^5))
  * `test_iter_serializable_context_keys` (Impact: 45.6 | O(N^3))
  * `test_empty_branch` (Impact: 41.8 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 639`, `args: 225`, `func_start: 222`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 1`, `state_mutation: 64`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 48`
* *Architecture:* `io: 35`, `api: 250`, `concurrency: 4`, `import: 89`
* *Defense:* `safety: 156`, `doc: 80`, `test: 448`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` tests_common.test_utils.version_compat, fix, dill, pathlib, airflow.providers.standard.operators.python, __future__, logging, asyncio...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `airflow-core/tests/unit/models/test_taskinstance.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.496 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.929 IQR)
- **Top Global Matches:** file_cluster_8: 12.496, file_cluster_0: 12.663, file_cluster_13: 12.671
- **Magnitude:** 1900.28 | **LOC:** 3583 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 23.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (2.6569%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_inlet_asset_extra` (Impact: 128.7 | O(2^N) | DB: 1)
  * `test_handle_failure_fail_fast` (Impact: 62.5 | O(2^N))
  * `test_outlet_multiple_asset_alias` (Impact: 57.5 | O(N^5))
  * `test_map_in_group` (Impact: 55.7 | O(N^5) | DB: 6)
  * `test_not_requeue_non_requeueable_task_in` (Impact: 53.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 807`, `args: 178`, `func_start: 171`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 22`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 12`, `orphaned_logic: 87`
* *Architecture:* `io: 13`, `api: 177`, `concurrency: 3`, `import: 86`
* *Defense:* `safety: 409`, `doc: 82`, `test: 603`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 48):` airflow.sdk.definitions.deadline, airflow.utils.state, airflow.models.taskmap, opentelemetry.trace.propagation.tracecontext, airflow.listeners.listener, opentelemetry.sdk.trace, time_machine, airflow.sdk.definitions.param...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `providers/google/src/airflow/providers/google/cloud/operators/dataplex.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.278 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.9 IQR)
- **Top Global Matches:** file_cluster_8: 12.278, file_cluster_16: 12.37, file_cluster_7: 12.429
- **Magnitude:** 1898.4 | **LOC:** 4221 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (13.6166%), Tech Debt (99.7997%)
**Top Internal Functions/Classes:**
  * `execute` (Impact: 141.9 | O(2^N) | DB: 23)
  * `execute` (Impact: 126.0 | O(N^6) | DB: 1)
  * `execute` (Impact: 102.6 | O(2^N) | DB: 23)
    * *Intent:* *args,
  * `execute` (Impact: 91.2 | O(2^N) | DB: 22)
  * `execute` (Impact: 89.2 | O(2^N) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 299`, `args: 112`, `func_start: 112`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 306`, `duplicate_logic: 89`
* *Architecture:* `api: 110`, `concurrency: 1`, `import: 19`
* *Defense:* `safety: 75`, `doc: 563`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.108
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` airflow.providers.common.compat.sdk, typing, google.api_core.gapic_v1.method, googleapiclient.errors, google.protobuf.field_mask_pb2, functools, airflow.providers.google.cloud.links.dataplex, airflow.providers.google.cloud.triggers.dataplex...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `providers/amazon/src/airflow/providers/amazon/aws/operators/sagemaker.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.629 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.241 IQR)
- **Top Global Matches:** file_cluster_16: 12.629, file_cluster_13: 12.642, file_cluster_8: 12.678
- **Magnitude:** 1880.46 | **LOC:** 1994 | **CtrlFlow:** 45.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (28.1367%), Tech Debt (99.2274%)
**Top Internal Functions/Classes:**
  * `execute` (Impact: 811.1 | O(2^N) | DB: 32)
  * `execute` (Impact: 273.9 | O(2^N) | DB: 9)
  * `execute` (Impact: 168.3 | O(2^N) | DB: 22)
  * `execute` (Impact: 70.8 | O(N^5) | DB: 3)
  * `execute` (Impact: 45.0 | O(2^N) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 191`, `args: 78`, `func_start: 76`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 237`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 23`
* *Architecture:* `api: 60`, `import: 26`
* *Defense:* `safety: 24`, `doc: 252`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.135
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` botocore.exceptions, __future__, airflow.providers.amazon.aws.operators.base_aws, airflow.providers.amazon.aws.hooks.sagemaker, airflow.providers.openlineage.extractors, airflow.providers.amazon.aws.utils.sagemaker, typing, airflow.providers.amazon.aws.utils.tags...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `airflow-core/src/airflow/cli/cli_parser.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.352 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.46 IQR)
- **Top Global Matches:** file_cluster_13: 11.352, file_cluster_17: 11.744, file_cluster_0: 11.892
- **Magnitude:** 1872.32 | **LOC:** 281 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.5555%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 66`, `args: 12`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 7`, `dead_code: 2`
* *Architecture:* `io: 1`, `api: 5`, `import: 21`
* *Defense:* `safety: 21`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.221
  * `Choke Point (Betweenness):` 6.3e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` typing, airflow.cli.utils, airflow._shared.module_loading, functools, airflow.utils.helpers, airflow.providers_manager, os, rich_argparse...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `scripts/in_container/install_airflow_and_providers.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.085 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.048 IQR)
- **Top Global Matches:** file_cluster_8: 10.085, file_cluster_13: 10.496, file_cluster_0: 10.543
- **Magnitude:** 1798.62 | **LOC:** 1261 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (15.7391%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `download_airflow_source_tarball` (Impact: 902.2 | O(2^N) | DB: 23)
  * `resolve_pr_number_to_repo_branch` (Impact: 680.4 | O(2^N) | DB: 46)
  * `find_provider_distributions` (Impact: 32.5 | O(N^3) | DB: 7)
  * `find_airflow_package` (Impact: 31.1 | O(N^2) | DB: 9)
  * `find_airflow_task_sdk_package` (Impact: 21.6 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 195`, `structural_boundaries: 118`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 42`, `dead_code: 1`
* *Architecture:* `io: 28`, `api: 17`, `import: 16`
* *Defense:* `safety: 10`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sys, typing, airflow, shutil, functools, packaging.version, os, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `providers/google/tests/unit/google/cloud/hooks/test_cloud_sql.py` (PYTHON) | Magnitude: 677.32 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1626, test: 374, structural_boundaries: 248, test_skip: 223
- `providers/google/tests/unit/google/cloud/triggers/test_bigquery.py` (PYTHON) | Magnitude: 298.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 600, test: 171, structural_boundaries: 170, concurrency: 121
- `providers/common/ai/src/airflow/providers/common/ai/example_dags/example_llm.py` (PYTHON) | Magnitude: 40.2 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 25, api: 10, args: 8
- `providers/microsoft/azure/tests/unit/microsoft/azure/sensors/test_wasb.py` (PYTHON) | Magnitude: 287.86 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 253, structural_boundaries: 96, test: 53, branch: 33
- `airflow-core/src/airflow/api_fastapi/auth/managers/simple/ui/index.html` (HTML) | Magnitude: 17.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, decorators: 4, reflection_metaprogramming: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `airflow-core/src/airflow/api_fastapi/auth/managers/simple/ui/rules/off.js` (JAVASCRIPT) | Magnitude: 19.88 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 4, args: 2, func_start: 1
- `airflow-core/src/airflow/ui/rules/off.js` (JAVASCRIPT) | Magnitude: 19.88 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 4, args: 2, func_start: 1
- `airflow-core/src/airflow/api_fastapi/auth/managers/simple/ui/rules/prettier.js` (JAVASCRIPT) | Magnitude: 15.64 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 4, events: 3, api: 2
- `airflow-core/src/airflow/ui/rules/prettier.js` (JAVASCRIPT) | Magnitude: 15.64 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 4, events: 3, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `scripts/docker/clean-logs.sh` (SHELL) | Magnitude: 7.38 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 30, branch: 26, indent_spaces: 24, io: 23
- `scripts/docker/entrypoint_prod.sh` (SHELL) | Magnitude: 52.56 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 181, branch: 152, state_mutation: 77, io: 59
- `go-sdk/sdk/client.go` (GO) | Magnitude: 110.54 | Delta: **0.162 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 71, state_mutation: 47, encapsulation: 25, structural_boundaries: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `dev/remove_artifacts.sh` (SHELL) | Magnitude: 59.16 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: io: 32, state_mutation: 27, indent_spaces: 26, reflection_metaprogramming: 16
- `go-sdk/bundle/bundlev1/task.go` (GO) | Magnitude: 103.8 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 83, state_mutation: 47, encapsulation: 36, structural_boundaries: 26
- `dev/sign.sh` (SHELL) | Magnitude: 8.86 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: safety: 5, reflection_metaprogramming: 4, branch: 3, state_mutation: 3
- `scripts/docker/install_os_dependencies.sh` (SHELL) | Magnitude: 43.0 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 232, branch: 93, reflection_metaprogramming: 82, state_mutation: 67
- `scripts/ci/dockerfiles/krb5-kdc-server/utils/create_client.sh` (SHELL) | Magnitude: 2.63 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 15, io: 14, reflection_metaprogramming: 9, safety_bypasses: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `providers/amazon/src/airflow/providers/amazon/aws/hooks/logs.py` (PYTHON) | Magnitude: 36.56 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 108, structural_boundaries: 34, doc: 28, branch: 21
- `airflow-ctl/src/airflowctl/api/client.py` (PYTHON) | Magnitude: 603.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 272, structural_boundaries: 121, doc: 54, branch: 51
- `airflow-core/tests/unit/dags/test_parsing_context.py` (PYTHON) | Magnitude: 6.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 13, encapsulation: 8, import: 7
- `providers/ftp/tests/unit/ftp/sensors/test_ftp.py` (PYTHON) | Magnitude: 48.24 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 27, test: 23, safety: 8
- `providers/pagerduty/src/airflow/providers/pagerduty/hooks/pagerduty_events.py` (PYTHON) | Magnitude: 100.44 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 210, doc: 53, structural_boundaries: 40, branch: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `providers/alibaba/src/airflow/providers/alibaba/cloud/operators/analyticdb_spark.py` (PYTHON) | Magnitude: 77.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 122, doc: 35, structural_boundaries: 32, encapsulation: 19
- `providers/common/sql/src/airflow/providers/common/sql/dialects/dialect.pyi` (PYTHON) | Magnitude: 24.98 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 31, generics: 29, api: 19
- `providers/microsoft/azure/src/airflow/providers/microsoft/azure/operators/asb.py` (PYTHON) | Magnitude: 154.34 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 325, doc: 107, state_mutation: 76, structural_boundaries: 51
- `providers/standard/src/airflow/providers/standard/utils/sensor_helper.py` (PYTHON) | Magnitude: 8.44 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 33, branch: 22, doc: 20
- `providers/teradata/src/airflow/providers/teradata/utils/tpt_util.py` (PYTHON) | Magnitude: 288.7 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 336, branch: 119, doc: 104, structural_boundaries: 80

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `airflow-core/src/airflow/ui/src/queries/useGridTISummaries.ts` (TYPESCRIPT) | Magnitude: 9.76 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 29, branch: 26, concurrency: 26
- `airflow-core/src/airflow/ui/src/queries/useBulkMarkAsDryRun.ts` (TYPESCRIPT) | Magnitude: 1.73 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 17, immutability_locks: 13, branch: 7
- `airflow-core/src/airflow/ui/src/pages/Dag/Calendar/calendarUtils.ts` (TYPESCRIPT) | Magnitude: 35.2 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 235, branch: 69, immutability_locks: 60, state_mutation: 57
- `airflow-core/src/airflow/ui/src/components/FlexibleForm/FieldMultiSelect.tsx` (TYPESCRIPT) | Magnitude: 2.31 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 21, branch: 15, args: 11
- `scripts/in_container/_in_container_utils.sh` (SHELL) | Magnitude: 9.78 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 33, state_mutation: 23, api: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `airflow-core/src/airflow/ui/src/components/FilterBar/defaultIcons.tsx` (TYPESCRIPT) | Magnitude: 2.13 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 10, generics: 7, ui_framework: 6, indent_spaces: 5
- `airflow-core/src/airflow/api_fastapi/auth/managers/simple/ui/openapi-gen/queries/queries.ts` (TYPESCRIPT) | Magnitude: 2.07 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 25, generics: 24, ui_framework: 22
- `airflow-core/src/airflow/api_fastapi/auth/managers/simple/ui/openapi-gen/requests/sdk.gen.ts` (TYPESCRIPT) | Magnitude: 4.41 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 21, branch: 16, generics: 14
- `airflow-core/src/airflow/ui/src/components/ui/Checkbox.tsx` (TYPESCRIPT) | Magnitude: 1.73 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, ui_framework: 8, generics: 8, structural_boundaries: 7
- `airflow-core/src/airflow/ui/src/pages/XCom/XComModal.tsx` (TYPESCRIPT) | Magnitude: 5.35 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 159, structural_boundaries: 30, ui_framework: 25, branch: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `airflow-core/src/airflow/ui/tests/e2e/specs/dag-calendar-tab.spec.ts` (TYPESCRIPT) | Magnitude: 10.27 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 103, concurrency: 71, structural_boundaries: 54, args: 23
- `providers/standard/tests/unit/standard/triggers/test_file.py` (PYTHON) | Magnitude: 46.6 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 30, concurrency: 22, test: 16
- `airflow-core/src/airflow/ui/openapi-gen/requests/core/OpenAPI.ts` (TYPESCRIPT) | Magnitude: 3.53 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 26, structural_boundaries: 15, state_mutation: 15, generics: 13
- `providers/edge3/src/airflow/providers/edge3/plugins/www/openapi-gen/requests/core/OpenAPI.ts` (TYPESCRIPT) | Magnitude: 3.53 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 26, structural_boundaries: 15, state_mutation: 15, generics: 13
- `airflow-core/src/airflow/ui/openapi-gen/requests/core/request.ts` (TYPESCRIPT) | Magnitude: 27.78 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 242, structural_boundaries: 99, branch: 71, immutability_locks: 45

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/exceptions.py` (PYTHON) | Magnitude: 17.12 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, doc: 8, class_start: 4, api: 4
- `providers/common/sql/src/airflow/providers/common/sql/hooks/handlers.pyi` (PYTHON) | Magnitude: 6.24 | Delta: **0.234 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 6, api: 5, args: 4, func_start: 4
- `providers/edge3/src/airflow/providers/edge3/plugins/www/src/utils/config.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.293 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, api: 1, planned_debt: 1, immutability_locks: 1
- `providers/common/sql/src/airflow/providers/common/sql/get_provider_info.pyi` (PYTHON) | Magnitude: 15.66 | Delta: **0.357 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `go-sdk/bundle/bundlev1/bundlev1server/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 1, sec_dead_code: 1
- `go-sdk/bundle/bundlev1/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 1, sec_dead_code: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `dev/airflow_mypy/plugin/decorators.py` (PYTHON) | Magnitude: 24.76 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 23, doc: 6, import: 6
- `providers/google/tests/system/google/cloud/cloud_sql/example_cloud_sql_query_iam.py` (PYTHON) | Magnitude: 151.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 273, structural_boundaries: 73, import: 24, branch: 22
- `task-sdk/tests/task_sdk/test_providers_manager_runtime.py` (PYTHON) | Magnitude: 307.76 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 216, structural_boundaries: 89, test: 44, encapsulation: 44
- `providers/amazon/tests/unit/amazon/aws/operators/test_sagemaker_transform.py` (PYTHON) | Magnitude: 145.46 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 328, test: 93, test_skip: 67, decorators: 62
- `providers/google/tests/unit/google/firebase/hooks/test_firestore.py` (PYTHON) | Magnitude: 111.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 164, test: 48, structural_boundaries: 36, test_skip: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `providers/amazon/src/airflow/providers/amazon/aws/executors/aws_lambda/docker/Dockerfile` (DOCKERFILE) | Magnitude: 12.62 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: io: 9, state_mutation: 9, dead_code: 8, branch: 6
- `dev/refresh_images.sh` (SHELL) | Magnitude: 14.36 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, api: 4, branch: 3
- `scripts/ci/dockerfiles/krb5-kdc-server/Dockerfile` (DOCKERFILE) | Magnitude: 141.6 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: io: 14, indent_spaces: 13, branch: 11, func_start: 6
- `scripts/ci/dockerfiles/trino/Dockerfile` (DOCKERFILE) | Magnitude: 21.9 | Delta: **0.336 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, ipc_rpc_bridges: 3, func_start: 2, args: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Dockerfile` -> Churn: **97.18%** | Cog Load: 23.8663% | Debt: 63.5773%
- `scripts/tools/setup_breeze` -> Churn: **79.97%** | Cog Load: 99.9968% | Debt: 69.1859%
- `airflow-core/src/airflow/models/dag.py` -> Churn: **76.79%** | Cog Load: 26.5089% | Debt: 99.9834%
- `airflow-core/src/airflow/serialization/definitions/dag.py` -> Churn: **70.69%** | Cog Load: 14.361% | Debt: 82.5821%
- `airflow-core/src/airflow/ui/tests/e2e/pages/DagsPage.ts` -> Churn: **70.38%** | Cog Load: 55.3999% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `airflow-core/tests/unit/utils/test_task_group.py` -> **Tzu-ping Chung** (100.0% isolated ownership) | Magnitude: 5799.0
- `providers/google/src/airflow/providers/google/cloud/operators/dataplex.py` -> **Ankit Chaurasia** (100.0% isolated ownership) | Magnitude: 1898.4
- `airflow-core/src/airflow/cli/cli_parser.py` -> **Jason(Zhe-You) Liu** (100.0% isolated ownership) | Magnitude: 1872.32
- `providers/google/src/airflow/providers/google/cloud/operators/compute.py` -> **SameerMesiah97** (100.0% isolated ownership) | Magnitude: 1608.92
- `dev/breeze/src/airflow_breeze/utils/pr_comments.py` -> **Jarek Potiuk** (100.0% isolated ownership) | Magnitude: 1345.14

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `airflow-core/src/airflow/models/taskinstance.py` -> **Severity: 0.472** (Bridge: 0.005 * Flux: 94.5677%)
- `airflow-core/src/airflow/models/xcom.py` -> **Severity: 0.325** (Bridge: 0.0037 * Flux: 88.5782%)
- `providers/common/compat/src/airflow/providers/common/compat/sdk.py` -> **Severity: 0.302** (Bridge: 0.0108 * Flux: 27.9272%)
- `airflow-core/src/airflow/triggers/base.py` -> **Severity: 0.296** (Bridge: 0.003 * Flux: 98.7711%)
- `airflow-core/src/airflow/serialization/serialized_objects.py` -> **Severity: 0.241** (Bridge: 0.0042 * Flux: 57.31%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `airflow-core/src/airflow/utils/json.py` -> **Severity: 1723.7** (Blast Radius: 17.237 * Doc Risk: 100.0%)
- `airflow-core/src/airflow/exceptions.py` -> **Severity: 1375.4** (Blast Radius: 13.754 * Doc Risk: 100.0%)
- `task-sdk/src/airflow/sdk/execution_time/comms.py` -> **Severity: 1022.1** (Blast Radius: 10.221 * Doc Risk: 100.0%)
- `shared/logging/src/airflow_shared/logging/structlog.py` -> **Severity: 924.6** (Blast Radius: 9.246 * Doc Risk: 100.0%)
- `task-sdk/src/airflow/sdk/exceptions.py` -> **Severity: 865.4** (Blast Radius: 8.654 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
