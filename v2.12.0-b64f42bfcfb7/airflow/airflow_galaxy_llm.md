# ARCHITECTURAL_BRIEF: airflow
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/apache/airflow.git` |
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
- **Scope:** 8971 analyzed artifact(s), 1022007 LOC.
- **Load-bearing artifact:** `providers/common/compat/src/airflow/providers/common/compat/sdk.py` -- 1206 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `clients/python/README.md` -- pulls in 157 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `dev/breeze/src/airflow_breeze/commands/pr_commands.py` at magnitude 13439.42 (structural weight, not risk).
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
| Total Artifacts | 12060 |
| Analyzed Artifacts (Scanned) | 8971 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3089 |
| Total LOC | 1022007 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 74.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5845 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.104 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.5496 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 587 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 6735 | 878263 | 75.1% |
| TYPESCRIPT | 767 | 50295 | 8.5% |
| JSON | 382 | 40031 | 4.3% |
| PLAINTEXT | 290 | 0 | 3.2% |
| YAML | 288 | 28475 | 3.2% |
| XML | 134 | 6 | 1.5% |
| MARKDOWN | 130 | 0 | 1.4% |
| SHELL | 86 | 3747 | 1.0% |
| JAVASCRIPT | 48 | 3735 | 0.5% |
| GO | 43 | 3686 | 0.5% |
| DOCKERFILE | 23 | 2008 | 0.3% |
| HTML | 18 | 565 | 0.2% |
| SQLITE | 11 | 54 | 0.1% |
| CSS | 10 | 10954 | 0.1% |
| CSV | 4 | 108 | 0.0% |
| PROTO | 1 | 46 | 0.0% |
| JAVA | 1 | 34 | 0.0% |

## 4.1 SOURCE ENCODINGS
All 8971 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 38%, Large Core Modules (2) 16%, Generic / Templated Code Files 11%, Declarative / Non-Code 10%, Large Core Modules (3) 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 8546 | 95.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 420 | 4.7% |
| Static: Minified & Vendor Opaque Mass | 5 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3089*

**Composition by Extension & Reason:**
- `.rst`: 1249x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 250x Excluded (Unsupported Extension: '.rst')
- `.png`: 510x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 276x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 12x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.kubernetes-helm-yaml')
- `.txt`: 140x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 104x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 75 LOC)
- `.py`: 192x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 76 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 2072 LOC)
- `.yaml`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Zero-Density Threshold (LOC: 83, Signals: 0), 3x Zero-Density Threshold (LOC: 55, Signals: 0)
- `.svg`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jinja2`: 31x Unsupported Format (.jinja2), 4x Excluded (Unsupported Extension: '.jinja2')
- `.njk`: 20x Unsupported Format (.njk)
- `.ts`: 6x Excluded (Saturation: Line 4 exceeds 500 chars), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 9171 LOC)
- `.go`: 2x Excluded (Machine-Generated Source Code Signature: 313 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1122 LOC), 1x Excluded (Machine-Generated Source Code Signature: 166 LOC)
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 2970 LOC), 1x Zero-Density Threshold (LOC: 99, Signals: 0)
- `.md5sum`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 14452 LOC), 1x Excluded (Massive Static Asset Blob: 15411 LOC)
- `.cfg`: 4x Unsupported Format (.cfg), 4x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 16.1 | 3.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 91.2 | 36.0 | 49.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.2 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 13.7 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 6.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 28.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 98.3 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.7 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 41.8 | 19.4 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8253 | 2088 | 2 | `dev/breeze/src/airflow_breeze/commands/pr_commands.py` |
| cleanup | 492 | 234 | 0 | `task-sdk/src/airflow/sdk/execution_time/supervisor.py` |
| guards | 55374 | 3948 | 15 | `airflow-core/tests/unit/jobs/test_scheduler_job.py` |
| danger | 20420 | 2803 | 6 | `dev/breeze/src/airflow_breeze/commands/pr_commands.py` |
| concurrency | 11750 | 1226 | 2 | `airflow-core/src/airflow/ui/tests/e2e/pages/DagsPage.ts` |
| connectivity | 60629 | 5231 | 17 | `providers/google/tests/unit/google/cloud/operators/test_dataproc.py` |
| io | 9111 | 1773 | 2 | `task-sdk/tests/task_sdk/api/test_client.py` |
| crypto | 78 | 55 | 0 | `airflow-core/src/airflow/api_fastapi/auth/tokens.py` |
| ipc | 823 | 221 | 0 | `dev/breeze/tests/integration_tests/test_airflow_release_validator_integration.py` |
| time | 2990 | 709 | 0 | `airflow-core/tests/unit/jobs/test_scheduler_job.py` |
| serialization | 147 | 83 | 0 | `airflow-core/src/airflow/ui/src/pages/Connections/ConnectionForm.tsx` |
| regex | 636 | 292 | 0 | `scripts/ci/prek/upgrade_important_versions.py` |
| events | 2183 | 425 | 0 | `task-sdk/tests/task_sdk/execution_time/test_task_runner.py` |
| tests | 81007 | 1918 | 21 | `providers/google/tests/unit/google/cloud/operators/test_dataproc.py` |
| docs | 24963 | 3716 | 7 | `providers/google/src/airflow/providers/google/cloud/hooks/vertex_ai/custom_job.py` |
| debt | 7901 | 1147 | 1 | `Dockerfile` |
| mutation | 417136 | 6140 | 115 | `airflow-core/tests/unit/jobs/test_scheduler_job.py` |
| dead_code | 20698 | 2072 | 6 | `airflow-core/tests/unit/jobs/test_scheduler_job.py` |
| credential | 420 | 193 | 0 | `airflow-core/tests/unit/cli/commands/test_task_command.py` |
| threat | 19 | 16 | 0 | `providers/weaviate/tests/system/weaviate/example_weaviate_operator.py` |
| ml_ai | 223 | 108 | 0 | `airflow-core/src/airflow/ui/src/pages/Dag/Calendar/calendarUtils.ts` |
| ui | 5502 | 575 | 0 | `registry/src/css/main.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `task-sdk/tests/task_sdk/api/test_client.py` (Hits: 326)
- `airflow-ctl/tests/airflow_ctl/api/test_operations.py` (Hits: 282)
- `task-sdk/tests/task_sdk/execution_time/test_supervisor.py` (Hits: 102)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **sdk.py** (`providers/common/compat/src/airflow/providers/common/compat/sdk.py`) — 1206 inbound connections
2. **__init__.py** (`task-sdk/src/airflow/sdk/__init__.py`) — 729 inbound connections
3. **dag.py** (`task-sdk/src/airflow/sdk/definitions/dag.py`) — 594 inbound connections
4. **system_tests.py** (`devel-common/src/tests_common/test_utils/system_tests.py`) — 453 inbound connections
5. **dag.py** (`airflow-core/src/airflow/models/dag.py`) — 447 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`clients/python/README.md`) — 157 outbound dependencies
2. **pytest_plugin.py** (`devel-common/src/tests_common/pytest_plugin.py`) — 99 outbound dependencies
3. **test_dag_serialization.py** (`airflow-core/tests/unit/serialization/test_dag_serialization.py`) — 83 outbound dependencies
4. **test_scheduler_job.py** (`airflow-core/tests/unit/jobs/test_scheduler_job.py`) — 81 outbound dependencies
5. **dag.py** (`task-sdk/src/airflow/sdk/definitions/dag.py`) — 77 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_run_tui_triage` **(Many-Argument Workhorses)** (@ `dev/breeze/src/airflow_breeze/commands/pr_commands.py`) -> Impact: **1845.0** | LOC: 1392
- `auto_triage` **(Many-Argument Workhorses)** (@ `dev/breeze/src/airflow_breeze/commands/pr_commands.py`) -> Impact: **844.3** | LOC: 799
- `_evaluate_trigger_rule` **(Many-Argument Workhorses)** (@ `airflow-core/src/airflow/ti_deps/deps/trigger_rule_dep.py`) -> Impact: **424.3** | LOC: 571
- `__init__` **(Many-Argument Workhorses)** (@ `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/operators/pod.py`) -> Impact: **384.6** | LOC: 174
- `_review_ready_prs_review_mode` **(Many-Argument Workhorses)** (@ `dev/breeze/src/airflow_breeze/commands/pr_commands.py`) -> Impact: **319.7** | LOC: 414
- `_run_startup_enrichment` **(Many-Argument Workhorses)** (@ `dev/breeze/src/airflow_breeze/commands/pr_commands.py`) -> Impact: **273.0** | LOC: 183
- `upgrade` **(Many-Argument Workhorses)** (@ `dev/breeze/src/airflow_breeze/commands/ci_commands.py`) -> Impact: **266.5** | LOC: 342
- `_review_workflow_approval_prs` **(Many-Argument Workhorses)** (@ `dev/breeze/src/airflow_breeze/commands/pr_commands.py`) -> Impact: **263.4** | LOC: 488
  * *Intent:* """Present NOT_RUN PRs for workflow approval. Mutates ctx.stats."""
- `__init__` **(Many-Argument Workhorses)** (@ `task-sdk/src/airflow/sdk/bases/operator.py`) -> Impact: **244.9** | LOC: 217
- `find_installation_spec` **(Many-Argument Workhorses)** (@ `scripts/in_container/install_airflow_and_providers.py`) -> Impact: **241.5** | LOC: 247

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `dev/breeze/src/airflow_breeze/commands` | 38 | 26078.18 | 26.42% | 2.33% |
| `providers/google/src/airflow/providers/google/cloud/operators` | 43 | 15864.84 | 37.7% | 38.29% |
| `providers/google/src/airflow/providers/google/cloud/hooks` | 47 | 15351.8 | 33.85% | 2.75% |
| `dev/breeze/src/airflow_breeze/utils` | 61 | 15003.9 | 39.61% | 1.2% |
| `providers/google/tests/unit/google/cloud/hooks` | 49 | 13778.9 | 30.71% | 0.0% |
| `providers/google/tests/unit/google/cloud/operators` | 45 | 12539.66 | 19.63% | 0.0% |
| `airflow-core/tests/unit/models` | 29 | 9166.56 | 14.51% | 0.0% |
| `airflow-core/src/airflow/models` | 40 | 8809.26 | 30.29% | 5.58% |
| `scripts/ci/prek` | 112 | 8623.64 | 45.4% | 3.43% |
| `providers/amazon/src/airflow/providers/amazon/aws/operators` | 35 | 8266.36 | 40.17% | 10.32% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `providers/amazon/src/airflow/providers/amazon/aws/hooks/bedrock.py` -> **100.0%** Exposure
- `providers/amazon/src/airflow/providers/amazon/aws/sensors/sagemaker.py` -> **100.0%** Exposure
- `providers/common/ai/src/airflow/providers/common/ai/example_dags/example_llm_branch.py` -> **100.0%** Exposure
- `providers/common/sql/src/airflow/providers/common/sql/hooks/sql.pyi` -> **100.0%** Exposure
- `task-sdk/src/airflow/sdk/definitions/operator_resources.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `airflow-core/src/airflow/api/common/airflow_health.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api/common/delete_dag.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api/common/mark_tasks.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api/common/trigger_dag.py` -> **100.0%** Exposure
- `airflow-core/src/airflow/api_fastapi/app.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `airflow-core/tests/unit/jobs/test_scheduler_job.py` -> **210** Orphaned Functions | **11** Duplicates
- `task-sdk/tests/task_sdk/definitions/decorators/test_setup_teardown.py` -> **43** Orphaned Functions | **109** Duplicates
- `providers/openlineage/tests/unit/openlineage/utils/test_utils.py` -> **147** Orphaned Functions | **2** Duplicates
- `task-sdk/tests/task_sdk/execution_time/test_task_runner.py` -> **119** Orphaned Functions | **20** Duplicates
- `airflow-core/tests/unit/models/test_taskinstance.py` -> **112** Orphaned Functions | **16** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `airflow-core/tests/unit/cli/commands/test_task_command.py` -> **100.0%** Exposure
- `providers/amazon/tests/unit/amazon/aws/utils/test_redshift.py` -> **100.0%** Exposure
- `providers/microsoft/azure/tests/unit/microsoft/azure/fs/test_msgraph.py` -> **100.0%** Exposure
- `providers/openai/tests/unit/openai/hooks/test_openai.py` -> **100.0%** Exposure
- `providers/pagerduty/tests/unit/pagerduty/hooks/test_pagerduty.py` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `48` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `46922` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `dev/breeze/src/airflow_breeze/commands/pr_commands.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.804)
- **Top Global Matches:** file_cluster_8: 9.804, file_cluster_6: 13.122, file_cluster_4: 20.901
- **Magnitude:** 13439.42 | **LOC:** 10954 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 67.9%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **47**; blast radius 0.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.7%), Complexity Load (formerly Cognitive Load) (81.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.2488% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_run_tui_triage` **(Many-Argument Workhorses)** (Impact: 1845.0)
  * `auto_triage` **(Many-Argument Workhorses)** (Impact: 844.3)
  * `_review_ready_prs_review_mode` **(Many-Argument Workhorses)** (Impact: 319.7)
  * `_run_startup_enrichment` **(Many-Argument Workhorses)** (Impact: 273.0)
  * `_review_workflow_approval_prs` **(Many-Argument Workhorses)** (Impact: 263.4)
    * *Intent:* """Present NOT_RUN PRs for workflow approval. Mutates ctx.stats."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 1517 instances
* *Concurrency (weighted view):* 42
* *State Mutation (weighted view):* 4810
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2393`, `structural_boundaries: 970`, `args: 184`, `func_start: 167`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 190`, `high_risk_execution: 11`, `state_mutation: 1776`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 76`, `api: 32`, `concurrency: 12`, `import: 104`
* *Defense:* `safety: 80`, `doc: 180`, `sync_locks: 1`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.113
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.001164
  * `Imports (Out-Degree: 17):` __future__, airflow_breeze.commands.common_options, airflow_breeze.utils.click_utils, airflow_breeze.utils.confirm, airflow_breeze.utils.console, airflow_breeze.utils.custom_param_types, airflow_breeze.utils.github, airflow_breeze.utils.llm_utils...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `airflow-core/tests/unit/jobs/test_scheduler_job.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.177)
- **Top Global Matches:** file_cluster_12: 7.177, file_cluster_15: 7.667, file_cluster_16: 7.972
- **Magnitude:** 4616.52 | **LOC:** 9620 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 25.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **81**; blast radius 0.044; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (96.2%), Guard Balance (formerly Safety Score) (57.0%), Complexity Load (formerly Cognitive Load) (31.7%), Connectivity (formerly Api Exposure) (11.1%)
- **Documentation Coverage:** 54.3396% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_find_executable_task_instances_executor_with_teams` **(Many-Argument Workhorses)** (Impact: 31.1)
    * *Intent:* """ Test that tasks are correctly routed to team-specific executors when multi-team is enabled """
  * `test_handle_stuck_queued_tasks_reschedule_sensors` **(Many-Argument Workhorses)** (Impact: 29.6)
    * *Intent:* """Reschedule sensors go in and out of running repeatedly using the same try_number Make sure that t...
  * `task_maker` **(Many-Argument Workhorses)** (Impact: 25.2)
  * `test_should_mark_empty_task_as_success` **(Defensive Guards)** (Impact: 24.4)
  * `test_handle_stuck_queued_tasks_multiple_attempts` **(Many-Argument Workhorses)** (Impact: 23.9)
    * *Intent:* """Verify that tasks stuck in queued will be rescheduled up to N times."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 289 instances
* *Api Near Db Sink:* 4 instances
* *State Mutation (weighted view):* 2704
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 1581`, `args: 293`, `func_start: 276`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 54`, `high_risk_execution: 4`, `state_mutation: 2126`, `planned_debt: 5`, `fragile_debt: 2`, `duplicate_logic: 11`, `unreferenced_by_name: 210`
* *Architecture:* `io: 16`, `api: 273`, `import: 89`
* *Defense:* `safety: 731`, `doc: 139`, `test: 393`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 65):` __future__, airflow, airflow._shared.module_loading, airflow._shared.timezones, airflow.api_fastapi.auth.tokens, airflow.assets.manager, airflow.callbacks.callback_requests, airflow.callbacks.database_callback_sink...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/breeze/src/airflow_breeze/commands/release_management_commands.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.966)
- **Top Global Matches:** file_cluster_6: 6.966, file_cluster_4: 9.003, file_cluster_9: 16.382
- **Magnitude:** 3103.52 | **LOC:** 4438 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 34.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **67**; blast radius 0.048; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (99.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.8%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepare_provider_documentation` **(Many-Argument Workhorses)** (Impact: 142.8)
  * `prepare_python_client` **(Many-Argument Workhorses)** (Impact: 116.3)
  * `generate_issue_content_providers` **(Many-Argument Workhorses)** (Impact: 107.4)
  * `prepare_helm_chart_tarball` **(Many-Argument Workhorses)** (Impact: 83.8)
  * `prepare_provider_distributions` **(Many-Argument Workhorses)** (Impact: 81.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 339 instances
* *High Risk Execution (weighted view):* 47
* *State Mutation (weighted view):* 1149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 633`, `structural_boundaries: 468`, `args: 88`, `func_start: 85`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 49`, `state_mutation: 471`
* *Architecture:* `io: 69`, `api: 75`, `concurrency: 1`, `import: 81`
* *Defense:* `safety: 46`, `doc: 25`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.048
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.000972
  * `Imports (Out-Degree: 35):` __future__, airflow_breeze.branch_defaults, airflow_breeze.commands.ci_image_commands, airflow_breeze.commands.common_options, airflow_breeze.commands.common_package_installation_options, airflow_breeze.commands.release_management_group, airflow_breeze.global_constants, airflow_breeze.params.build_ci_params...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `devel-common/src/tests_common/pytest_plugin.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.234)
- **Top Global Matches:** file_cluster_4: 8.234, file_cluster_12: 9.234, file_cluster_16: 10.433
- **Magnitude:** 2515.22 | **LOC:** 3010 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 26.3%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **99**; blast radius 0.079; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (75.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.4%), Guard Balance (formerly Safety Score) (67.5%)
- **Documentation Coverage:** 71.1744% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dag_maker` **(Compute Cores)** (Impact: 159.1)
    * *Intent:* """ Fixture to help create DAG, DagModel, and SerializedDAG automatically. You have to use the dag_m...
  * `_create_task_instance` **(Many-Argument Workhorses)** (Impact: 106.6)
  * `maker` **(Many-Argument Workhorses)** (Impact: 85.2)
  * `create_dagrun` **(Many-Argument Workhorses)** (Impact: 67.0)
  * `run_task` **(Stateful Encapsulated Methods)** (Impact: 64.8)
    * *Intent:* """ Fixture to run a task without defining a dag file. This fixture builds on top of create_runtime_...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 301 instances
* *State Mutation (weighted view):* 988
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 368`, `structural_boundaries: 677`, `args: 149`, `func_start: 140`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 1`, `state_mutation: 386`, `dead_code: 2`, `planned_debt: 6`, `fragile_debt: 2`
* *Architecture:* `io: 32`, `api: 115`, `import: 185`
* *Defense:* `safety: 63`, `doc: 41`, `test: 143`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.079
  * `Choke Point (Betweenness):` 3.3e-05 | `Ripple Effect (Closeness):` 0.001107
  * `Imports (Out-Degree: 66):` __future__, _pytest.config.findpaths, airflow, airflow._shared.module_loading, airflow._shared.secrets_masker, airflow._shared.timezones, airflow.configuration, airflow.dag_processing.dagbag...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `dev/breeze/src/airflow_breeze/utils/tui_display.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.782)
- **Top Global Matches:** file_cluster_6: 6.782, file_cluster_4: 12.307, file_cluster_8: 14.039
- **Magnitude:** 2420.3 | **LOC:** 1983 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **20**; blast radius 0.087; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.5%)
- **Documentation Coverage:** 9.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_build_detail_lines` **(Many-Argument Workhorses)** (Impact: 152.6)
    * *Intent:* """Build the full list of detail lines for a PR entry (not truncated)."""
  * `run_interactive` **(Many-Argument Workhorses)** (Impact: 148.4)
  * `_build_pr_table` **(Many-Argument Workhorses)** (Impact: 126.1)
    * *Intent:* """Build the scrollable PR list table."""
  * `_read_tui_key` **(Compute Cores)** (Impact: 62.5)
    * *Intent:* """Read a keypress or mouse event and map it to a TUIAction, MouseEvent, or raw character. Returns `...
  * `_build_header` **(Stateful Encapsulated Methods)** (Impact: 52.7)
    * *Intent:* """Build the header as side-by-side main info (left) + status panel (right)."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 400 instances
* *State Mutation (weighted view):* 1329
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 509`, `structural_boundaries: 312`, `args: 50`, `func_start: 49`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 529`
* *Architecture:* `io: 16`, `api: 28`, `import: 25`
* *Defense:* `safety: 13`, `doc: 53`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000911
  * `Imports (Out-Degree: 4):` __future__, airflow_breeze.utils.confirm, airflow_breeze.utils.console, airflow_breeze.utils.pr_display, airflow_breeze.utils.pr_models, enum, io, os...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `airflow-core/src/airflow/serialization/serialized_objects.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 11.046)
- **Top Global Matches:** file_cluster_5: 11.046, file_cluster_4: 11.357, file_cluster_12: 12.813
- **Magnitude:** 2046.24 | **LOC:** 2316 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **51** in-repo importer(s); it depends on **73**; blast radius 2.732; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.2%), Complexity Load (formerly Cognitive Load) (63.0%)
- **Documentation Coverage:** 60.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `serialize` **(Defensive Guards)** (Impact: 101.5)
  * `populate_operator` **(Many-Argument Workhorses)** (Impact: 101.2)
  * `conversion_v1_to_v2` **(Compute Cores)** (Impact: 72.9)
  * `deserialize` **(Compute Cores)** (Impact: 72.0)
    * *Intent:* """ Deserialize an object; helper function of depth first search for deserialization. :meta private:...
  * `_is_excluded` **(Many-Argument Workhorses)** (Impact: 59.0)
    * *Intent:* """ Determine if a variable is excluded from the serialized object. :param var: The value to check. ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 267 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 847
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 450`, `structural_boundaries: 499`, `args: 90`, `func_start: 90`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 313`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 58`, `concurrency: 3`, `import: 86`
* *Defense:* `safety: 98`, `doc: 57`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.732
  * `Choke Point (Betweenness):` 0.004235 | `Ripple Effect (Closeness):` 0.125015
  * `Imports (Out-Degree: 51):` __future__, airflow, airflow._shared.module_loading, airflow._shared.timezones.timezone, airflow.callbacks.callback_requests, airflow.exceptions, airflow.models.connection, airflow.models.expandinput...
  * `Imported By (In-Degree: 51):` (Excluded from Brief to save tokens)

### `airflow-core/src/airflow/jobs/scheduler_job_runner.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.844)
- **Top Global Matches:** file_cluster_4: 7.844, file_cluster_6: 10.83, file_cluster_12: 12.253
- **Magnitude:** 1951.72 | **LOC:** 3261 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 14.3%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **76**; blast radius 0.249; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (97.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.3%)
- **Documentation Coverage:** 30.9211% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_executor_events` **(Many-Argument Workhorses)** (Impact: 154.5)
  * `_executable_task_instances_to_queued` **(Many-Argument Workhorses)** (Impact: 142.8)
    * *Intent:* """ Find TIs that are ready for execution based on conditions. Conditions include: - pool limits - D...
  * `_try_to_load_executor` **(Many-Argument Workhorses)** (Impact: 52.4)
  * `_schedule_dag_run` **(Many-Argument Workhorses)** (Impact: 52.2)
  * `_create_dag_runs` **(Many-Argument Workhorses)** (Impact: 38.9)
    * *Intent:* """Create a DAG run and update the dag_model to control if/when the next DAGRun should be created.""...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 223 instances
* *Api Near Db Sink:* 1 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 773
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 410`, `structural_boundaries: 375`, `args: 65`, `func_start: 64`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 55`, `high_risk_execution: 1`, `state_mutation: 327`, `planned_debt: 11`, `fragile_debt: 1`
* *Architecture:* `io: 20`, `api: 9`, `concurrency: 4`, `import: 84`
* *Defense:* `safety: 36`, `doc: 38`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.249
  * `Choke Point (Betweenness):` 0.000724 | `Ripple Effect (Closeness):` 0.105301
  * `Imports (Out-Degree: 52):` __future__, airflow, airflow._shared.logging.types, airflow._shared.observability.metrics.dual_stats_manager, airflow._shared.observability.metrics.stats, airflow._shared.timezones, airflow.api_fastapi.execution_api.datamodels.taskinstance, airflow.assets.evaluation...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `task-sdk/tests/task_sdk/execution_time/test_task_runner.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.599)
- **Top Global Matches:** file_cluster_12: 8.599, file_cluster_15: 9.88, file_cluster_16: 10.965
- **Magnitude:** 1922.2 | **LOC:** 4744 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 34.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **53**; blast radius 0.044; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (81.9%), Guard Balance (formerly Safety Score) (51.6%), Concurrency Surface (formerly Concurrency) (15.2%), Complexity Load (formerly Cognitive Load) (13.9%)
- **Documentation Coverage:** 67.6887% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_xcom_pull` **(Many-Argument Workhorses)** (Impact: 63.2)
  * `test_xcom_pull_return_values` **(Many-Argument Workhorses)** (Impact: 18.0)
  * `test_task_span_is_child_of_dag_run_span` **(Defensive Guards)** (Impact: 12.5)
    * *Intent:* """Full trace hierarchy: dag_run → task_run.my_task (API server) → worker.my_task (task runner)."""
  * `test_rendered_templates_mask_secrets_with_truncation` **(Defensive Guards)** (Impact: 12.4)
    * *Intent:* """Test that secrets are masked before truncation when rendered fields exceed max_templated_field_le...
  * `test_task_runner_both_callbacks_have_timing_info` **(Defensive Guards)** (Impact: 12.0)
    * *Intent:* """Test that both success and failure callbacks receive accurate timing information."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 60 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 745
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 788`, `args: 232`, `func_start: 216`, `class_start: 64`
* *Risk/State:* `safety_bypasses: 52`, `high_risk_execution: 1`, `state_mutation: 625`, `fragile_debt: 1`, `duplicate_logic: 20`, `unreferenced_by_name: 119`
* *Architecture:* `io: 8`, `api: 270`, `concurrency: 3`, `import: 77`
* *Defense:* `safety: 225`, `doc: 108`, `test: 321`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` __future__, airflow._shared.observability.traces, airflow.api_fastapi.execution_api.routes.task_instances, airflow.listeners, airflow.providers.standard.operators.bash, airflow.providers.standard.operators.empty, airflow.providers.standard.operators.python, airflow.providers.standard.operators.trigger_dagrun...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `airflow-core/tests/unit/api_fastapi/core_api/routes/public/test_task_instances.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.363)
- **Top Global Matches:** file_cluster_15: 7.363, file_cluster_12: 8.381, file_cluster_16: 8.687
- **Magnitude:** 1866.16 | **LOC:** 6155 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 22.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 0.044; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.0%), Guard Balance (formerly Safety Score) (47.5%), Complexity Load (formerly Cognitive Load) (23.0%), Concurrency Surface (formerly Concurrency) (14.0%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_should_handle_task_instance_deletion` **(Many-Argument Workhorses)** (Impact: 56.1)
  * `create_task_instances` **(Many-Argument Workhorses)** (Impact: 43.3)
  * `test_should_respond_200_with_mapped_task_at_different_try_numbers` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `test_bulk_task_instances` **(Many-Argument Workhorses)** (Impact: 18.9)
  * `test_mapped_task_should_respond_200` **(Many-Argument Workhorses)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 118 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 712
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 663`, `args: 157`, `func_start: 157`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 476`, `planned_debt: 1`, `duplicate_logic: 3`, `unreferenced_by_name: 71`
* *Architecture:* `io: 5`, `api: 181`, `concurrency: 3`, `import: 44`
* *Defense:* `safety: 356`, `doc: 15`, `test: 339`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` __future__, airflow._shared.timezones.timezone, airflow.configuration, airflow.dag_processing.bundles.manager, airflow.dag_processing.dagbag, airflow.jobs.job, airflow.jobs.triggerer_job_runner, airflow.models...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `providers/fab/src/airflow/providers/fab/auth_manager/security_manager/override.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.74)
- **Top Global Matches:** file_cluster_4: 8.74, file_cluster_12: 8.806, file_cluster_5: 8.847
- **Magnitude:** 1865.0 | **LOC:** 2617 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **52**; blast radius 0.235; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.3%), Connectivity (formerly Api Exposure) (68.8%)
- **Documentation Coverage:** 26.9912% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `auth_user_ldap` **(Many-Argument Workhorses)** (Impact: 98.5)
    * *Intent:* """ Authenticate user with LDAP. NOTE: this depends on python-ldap module. :param username: the user...
  * `_sync_dag_view_permissions` **(Many-Argument Workhorses)** (Impact: 56.5)
  * `auth_user_oauth` **(Many-Argument Workhorses)** (Impact: 43.0)
    * *Intent:* """ Authenticate user with OAuth. :userinfo: dict with user information (keys are the same as User m...
  * `get_oauth_user_info` **(Many-Argument Workhorses)** (Impact: 36.0)
    * *Intent:* """ There are different OAuth APIs with different ways to retrieve user info. All providers have dif...
  * `_search_ldap` **(Many-Argument Workhorses)** (Impact: 35.0)
    * *Intent:* """ Search LDAP for user. :param ldap: The ldap module reference :param con: The ldap connection :pa...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 237 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 786
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 338`, `structural_boundaries: 454`, `args: 124`, `func_start: 124`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 312`, `dead_code: 10`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 7`, `api: 101`, `import: 56`
* *Defense:* `safety: 42`, `doc: 117`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.235
  * `Choke Point (Betweenness):` 0.001198 | `Ripple Effect (Closeness):` 0.079519
  * `Imports (Out-Degree: 22):` __future__, airflow.models.dagbag, airflow.providers.common.compat.sdk, airflow.providers.common.compat.security.permissions, airflow.providers.fab.auth_manager.models, airflow.providers.fab.auth_manager.models.anonymous_user, airflow.providers.fab.auth_manager.security_manager.constants, airflow.providers.fab.auth_manager.views.auth_oauth...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `providers/google/src/airflow/providers/google/cloud/hooks/bigquery.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.007)
- **Top Global Matches:** file_cluster_5: 7.007, file_cluster_12: 9.374, file_cluster_7: 10.666
- **Magnitude:** 1862.72 | **LOC:** 2385 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **51**; blast radius 0.157; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (94.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.6%)
- **Documentation Coverage:** 59.7561% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_prepare_query_configuration` **(Many-Argument Workhorses)** (Impact: 172.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 65.2)
  * `split_tablename` **(Many-Argument Workhorses)** (Impact: 45.4)
  * `interval_check` **(Many-Argument Workhorses)** (Impact: 41.1)
  * `create_empty_dataset` **(Many-Argument Workhorses)** (Impact: 34.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 184 instances
* *Concurrency (weighted view):* 91
* *State Mutation (weighted view):* 631
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 334`, `args: 96`, `func_start: 94`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 82`, `state_mutation: 263`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 3`, `api: 76`, `concurrency: 21`, `import: 53`
* *Defense:* `safety: 21`, `doc: 76`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.003253
  * `Imports (Out-Degree: 16):` __future__, aiohttp, airflow.exceptions, airflow.providers.common.compat.lineage.hook, airflow.providers.common.compat.sdk, airflow.providers.common.sql.hooks.lineage, airflow.providers.common.sql.hooks.sql, airflow.providers.google.cloud.utils.bigquery...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `airflow-core/src/airflow/models/taskinstance.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.789)
- **Top Global Matches:** file_cluster_4: 6.789, file_cluster_12: 10.18, file_cluster_5: 10.76
- **Magnitude:** 1823.86 | **LOC:** 2394 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 31.2%
- **Blast Radius:** changing it is visible to **170** in-repo importer(s); it depends on **76**; blast radius 4.828; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (86.9%), Connectivity (formerly Api Exposure) (80.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 48.1752% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `register_asset_changes_in_db` **(Many-Argument Workhorses)** (Impact: 101.9)
  * `_check_and_change_state_before_execution` **(Many-Argument Workhorses)** (Impact: 92.1)
  * `clear_task_instances` **(Many-Argument Workhorses)** (Impact: 89.4)
  * `xcom_pull` **(Many-Argument Workhorses)** (Impact: 79.9)
  * `find_relevant_relatives` **(Many-Argument Workhorses)** (Impact: 32.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 234 instances
* *Api Near Db Sink:* 2 instances
* *State Mutation (weighted view):* 754
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 383`, `args: 76`, `func_start: 74`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 286`, `planned_debt: 3`
* *Architecture:* `io: 12`, `api: 58`, `import: 90`
* *Defense:* `safety: 45`, `doc: 55`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.828
  * `Choke Point (Betweenness):` 0.002355 | `Ripple Effect (Closeness):` 0.145726
  * `Imports (Out-Degree: 45):` __future__, airflow, airflow._shared.observability.metrics.dual_stats_manager, airflow._shared.observability.metrics.stats, airflow._shared.observability.traces, airflow._shared.timezones, airflow.api_fastapi.execution_api.datamodels.asset, airflow.assets.manager...
  * `Imported By (In-Degree: 170):` (Excluded from Brief to save tokens)

### `airflow-core/tests/unit/models/test_dagrun.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.89)
- **Top Global Matches:** file_cluster_12: 6.89, file_cluster_15: 7.353, file_cluster_11: 8.12
- **Magnitude:** 1807.2 | **LOC:** 3565 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 21.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **58**; blast radius 0.044; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (75.2%), Guard Balance (formerly Safety Score) (50.5%), Complexity Load (formerly Cognitive Load) (29.9%), Concurrency Surface (formerly Concurrency) (12.9%)
- **Documentation Coverage:** 77.6316% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_tis_considered_for_state` **(Many-Argument Workhorses)** (Impact: 22.6)
    * *Intent:* """ We use a convenience notation to wire up test scenarios: t<num> -- teardown task t<num>_ -- tear...
  * `create_dag_run` **(Many-Argument Workhorses)** (Impact: 20.7)
  * `test_schedulable_task_exist_when_rerun_removed_upstream_mapped_task` **(Defensive Guards)** (Impact: 19.8)
  * `test_mapped_task_rerun_with_different_length_of_args` **(Many-Argument Workhorses)** (Impact: 18.5)
  * `test_mapped_expand_kwargs` **(Defensive Guards)** (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 119 instances
* *State Mutation (weighted view):* 838
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 842`, `args: 198`, `func_start: 191`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 600`, `dead_code: 5`, `fragile_debt: 1`, `duplicate_logic: 28`, `unreferenced_by_name: 99`
* *Architecture:* `io: 3`, `api: 188`, `concurrency: 3`, `import: 61`
* *Defense:* `safety: 277`, `doc: 45`, `test: 177`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 40):` __future__, airflow, airflow._shared.observability.metrics.stats, airflow._shared.observability.traces, airflow._shared.timezones, airflow.callbacks.callback_requests, airflow.dag_processing.dagbag, airflow.models.dag...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `providers/databricks/tests/unit/databricks/hooks/test_databricks_base.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.163)
- **Top Global Matches:** file_cluster_12: 8.163, file_cluster_15: 8.659, file_cluster_13: 9.601
- **Magnitude:** 1764.12 | **LOC:** 1890 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.044; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (82.0%), Guard Balance (formerly Safety Score) (54.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.9%)
- **Documentation Coverage:** 68.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_a_get_federated_token_databricks_error` **(Many-Argument Workhorses)** (Impact: 8.7)
    * *Intent:* """Test async error handling when Databricks token exchange fails."""
  * `test_a_get_sp_token_retry_error` **(Defensive Guards)** (Impact: 8.5)
  * `test_get_federated_token_databricks_error` **(Many-Argument Workhorses)** (Impact: 7.4)
    * *Intent:* """Test error handling when Databricks token exchange fails."""
  * `test_get_federated_token` **(Defensive Guards)** (Impact: 5.4)
    * *Intent:* """Test Kubernetes OIDC token federation flow."""
  * `test_get_token_managed_identity` **(Defensive Guards)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 83 instances
* *Amplified Cascading Flux:* 41 instances
* *Concurrency (weighted view):* 523
* *State Mutation (weighted view):* 731
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 426`, `args: 101`, `func_start: 100`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 649`, `duplicate_logic: 3`, `unreferenced_by_name: 96`
* *Architecture:* `io: 73`, `api: 166`, `concurrency: 108`, `import: 14`
* *Defense:* `safety: 147`, `doc: 37`, `test: 349`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, aiohttp, aiohttp.client_exceptions, airflow.models, airflow.providers.common.compat.sdk, airflow.providers.databricks.hooks.databricks_base, datetime, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `providers/google/src/airflow/providers/google/cloud/operators/dataproc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.533)
- **Top Global Matches:** file_cluster_4: 7.533, file_cluster_16: 8.383, file_cluster_12: 8.781
- **Magnitude:** 1741.52 | **LOC:** 2978 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 22.2%
- **Blast Radius:** changing it is visible to **27** in-repo importer(s); it depends on **30**; blast radius 0.18; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.1%)
- **Documentation Coverage:** 77.686% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 131.9)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 48.2)
  * `_build_cluster_data` **(Compute Cores)** (Impact: 48.0)
  * `execute` **(Many-Argument Workhorses)** (Impact: 39.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 30.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 171 instances
* *Api Near Db Sink:* 3 instances
* *State Mutation (weighted view):* 767
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 238`, `args: 82`, `func_start: 82`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 425`, `planned_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `api: 58`, `import: 33`
* *Defense:* `safety: 27`, `doc: 37`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.18
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.002988
  * `Imports (Out-Degree: 11):` __future__, airflow.exceptions, airflow.providers.common.compat.sdk, airflow.providers.google.cloud.hooks.dataproc, airflow.providers.google.cloud.links.dataproc, airflow.providers.google.cloud.openlineage.utils, airflow.providers.google.cloud.operators.cloud_base, airflow.providers.google.cloud.triggers.dataproc...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `shared/configuration/src/airflow_shared/configuration/parser.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.572)
- **Top Global Matches:** file_cluster_5: 7.572, file_cluster_12: 8.845, file_cluster_4: 10.498
- **Magnitude:** 1693.92 | **LOC:** 2073 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 23.5%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **23**; blast radius 0.824; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.8%), Guard Balance (formerly Safety Score) (70.1%)
- **Documentation Coverage:** 37.2414% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_replace_section_config_with_display_sources` **(Many-Argument Workhorses)** (Impact: 75.3)
  * `_write_option_header` **(Many-Argument Workhorses)** (Impact: 61.5)
  * `_write_value` **(Many-Argument Workhorses)** (Impact: 48.6)
  * `as_dict` **(Many-Argument Workhorses)** (Impact: 47.3)
  * `write` **(Many-Argument Workhorses)** (Impact: 42.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 178 instances
* *State Mutation (weighted view):* 577
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 305`, `structural_boundaries: 283`, `args: 93`, `func_start: 93`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 48`, `high_risk_execution: 1`, `state_mutation: 221`, `planned_debt: 1`
* *Architecture:* `io: 5`, `api: 50`, `import: 24`
* *Defense:* `safety: 49`, `doc: 77`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.824
  * `Choke Point (Betweenness):` 0.000114 | `Ripple Effect (Closeness):` 0.102191
  * `Imports (Out-Degree: 4):` ..module_loading, .exceptions, __future__, airflow.providers_manager, airflow.sdk.providers_manager_runtime, collections.abc, configparser, contextlib...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `providers/openlineage/tests/unit/openlineage/utils/test_utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.315)
- **Top Global Matches:** file_cluster_12: 6.315, file_cluster_15: 9.23, file_cluster_7: 9.295
- **Magnitude:** 1665.96 | **LOC:** 4169 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 77.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.044; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (80.7%), Complexity Load (formerly Cognitive Load) (57.2%), Guard Balance (formerly Safety Score) (51.4%)
- **Documentation Coverage:** 65.5172% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_get_tasks_details` **(I/O & Config Routines)** (Impact: 14.0)
  * `test_get_tasks_details_with_edge_labels` **(I/O & Config Routines)** (Impact: 10.3)
    * *Intent:* """ Comprehensive test for dag with labeled edges. See ``_build_labeled_edge_map`` docstring for cla...
  * `test_get_airflow_dag_run_facet` **(I/O & Config Routines)** (Impact: 7.0)
  * `test_get_tasks_large_dag` **(I/O & Config Routines)** (Impact: 7.0)
    * *Intent:* """Test how get_tasks behaves for a large dag with many dependent tasks."""
  * `test_dag_info_schedule_dataset_or_time_schedule` **(I/O & Config Routines)** (Impact: 6.7)
    * *Intent:* # Airflow 2 import, this test is only run on Airflow 2 from airflow.timetables.datasets import Datas...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 42 instances
* *Concurrency (weighted view):* 148
* *State Mutation (weighted view):* 846
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 709`, `args: 171`, `func_start: 161`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 762`, `duplicate_logic: 2`, `unreferenced_by_name: 147`
* *Architecture:* `io: 18`, `api: 172`, `concurrency: 28`, `import: 37`
* *Defense:* `safety: 375`, `doc: 59`, `test: 204`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` __future__, airflow, airflow.models.dag_version, airflow.models.dagrun, airflow.models.taskinstance, airflow.providers.common.compat.assets, airflow.providers.common.compat.sdk, airflow.providers.openlineage.conf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `airflow-core/src/airflow/models/dagrun.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.012)
- **Top Global Matches:** file_cluster_4: 8.012, file_cluster_5: 10.576, file_cluster_12: 10.909
- **Magnitude:** 1655.36 | **LOC:** 2213 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 19.2%
- **Blast Radius:** changing it is visible to **129** in-repo importer(s); it depends on **65**; blast radius 3.822; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (81.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.5%)
- **Documentation Coverage:** 77.3109% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update_state` **(Many-Argument Workhorses)** (Impact: 111.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 83.7)
  * `schedule_tis` **(Many-Argument Workhorses)** (Impact: 64.9)
  * `find` **(Many-Argument Workhorses)** (Impact: 52.4)
  * `_get_ready_tis` **(Many-Argument Workhorses)** (Impact: 43.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 186 instances
* *State Mutation (weighted view):* 621
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 330`, `args: 69`, `func_start: 66`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 249`, `planned_debt: 2`
* *Architecture:* `io: 13`, `api: 45`, `import: 80`
* *Defense:* `safety: 33`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.822
  * `Choke Point (Betweenness):` 0.00169 | `Ripple Effect (Closeness):` 0.145785
  * `Imports (Out-Degree: 40):` __future__, airflow._shared.observability.metrics.dual_stats_manager, airflow._shared.observability.metrics.stats, airflow._shared.observability.traces, airflow._shared.timezones, airflow.api_fastapi.execution_api.datamodels.taskinstance, airflow.callbacks.callback_requests, airflow.configuration...
  * `Imported By (In-Degree: 129):` (Excluded from Brief to save tokens)

### `airflow-core/tests/unit/serialization/test_dag_serialization.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.114)
- **Top Global Matches:** file_cluster_12: 7.114, file_cluster_15: 7.306, file_cluster_11: 8.695
- **Magnitude:** 1655.12 | **LOC:** 4638 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **83**; blast radius 0.049; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (67.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.9%), Guard Balance (formerly Safety Score) (48.0%), Concurrency Surface (formerly Concurrency) (32.4%)
- **Documentation Coverage:** 50.9036% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validate_deserialized_task` **(Many-Argument Workhorses)** (Impact: 44.6)
  * `test_task_callback_boolean_optimization` **(Defensive Guards)** (Impact: 24.4)
    * *Intent:* """Test that task callbacks are optimized using has_on_*_callback boolean flags."""
  * `validate_deserialized_dag` **(Defensive Guards)** (Impact: 24.3)
    * *Intent:* """ Verify that all example DAGs work with DAG Serialization by checking fields between Serialized D...
  * `collect_dags` **(Compute Cores)** (Impact: 15.9)
    * *Intent:* """Collects DAGs to test."""
  * `test_mapped_operator_client_defaults_optimization` **(Many-Argument Workhorses)** (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 123 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 58
* *State Mutation (weighted view):* 694
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 876`, `args: 174`, `func_start: 152`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 2`, `state_mutation: 448`, `planned_debt: 4`, `fragile_debt: 2`, `duplicate_logic: 10`
* *Architecture:* `io: 5`, `api: 158`, `concurrency: 13`, `import: 115`
* *Defense:* `safety: 353`, `doc: 84`, `test: 198`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000111
  * `Imports (Out-Degree: 59):` __future__, airflow, airflow._shared.module_loading, airflow._shared.timezones, airflow.dag_processing.dagbag, airflow.exceptions, airflow.models.asset, airflow.models.connection...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/operators/pod.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.467)
- **Top Global Matches:** file_cluster_4: 6.467, file_cluster_6: 10.786, file_cluster_12: 11.824
- **Magnitude:** 1605.84 | **LOC:** 1533 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 18.2%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **45**; blast radius 0.152; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.9%), Complexity Load (formerly Cognitive Load) (67.6%)
- **Documentation Coverage:** 63.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 384.6)
  * `cleanup` **(Many-Argument Workhorses)** (Impact: 89.4)
  * `build_pod_request_obj` **(Many-Argument Workhorses)** (Impact: 42.3)
    * *Intent:* """ Return V1Pod object based on pod template file, full pod spec, and other operator parameters. Th...
  * `invoke_defer_method` **(Many-Argument Workhorses)** (Impact: 35.2)
  * `trigger_reentry` **(Many-Argument Workhorses)** (Impact: 31.4)
    * *Intent:* """ Point of re-entry from trigger. If ``logging_interval`` is None, then at this point, the pod sho...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 181 instances
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 593
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 198`, `args: 46`, `func_start: 46`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 231`, `planned_debt: 3`
* *Architecture:* `io: 3`, `api: 34`, `concurrency: 8`, `import: 48`
* *Defense:* `safety: 38`, `doc: 24`, `sync_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.152
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.002435
  * `Imports (Out-Degree: 25):` __future__, airflow.hooks.base, airflow.models, airflow.providers.cncf.kubernetes, airflow.providers.cncf.kubernetes.backcompat.backwards_compat_converters, airflow.providers.cncf.kubernetes.callbacks, airflow.providers.cncf.kubernetes.hooks.kubernetes, airflow.providers.cncf.kubernetes.kubernetes_helper_functions...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `airflow-core/tests/unit/models/test_taskinstance.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.727)
- **Top Global Matches:** file_cluster_12: 6.727, file_cluster_15: 7.302, file_cluster_11: 7.923
- **Magnitude:** 1551.78 | **LOC:** 3583 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 23.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **75**; blast radius 0.044; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (81.9%), Guard Balance (formerly Safety Score) (43.3%), Complexity Load (formerly Cognitive Load) (24.0%), Concurrency Surface (formerly Concurrency) (12.9%)
- **Documentation Coverage:** 78.6127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_check_task_dependencies` **(Many-Argument Workhorses)** (Impact: 21.7)
  * `test_outlet_multiple_asset_alias` **(Defensive Guards)** (Impact: 19.6)
  * `test_clear_task_instances_recalculates_dagrun_queued_deadlines` **(Many-Argument Workhorses)** (Impact: 16.1)
    * *Intent:* """Test that clearing tasks recalculates all (and only) DAGRUN_QUEUED_AT deadlines."""
  * `test_refresh_from_db` **(Many-Argument Workhorses)** (Impact: 15.8)
  * `test_check_task_dependencies_for_mapped` **(Many-Argument Workhorses)** (Impact: 15.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 704
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 914`, `args: 182`, `func_start: 171`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 548`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 16`, `unreferenced_by_name: 112`
* *Architecture:* `io: 8`, `api: 177`, `concurrency: 3`, `import: 86`
* *Defense:* `safety: 396`, `doc: 41`, `test: 221`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 60):` __future__, airflow, airflow._shared.observability.metrics.stats, airflow._shared.observability.traces, airflow._shared.timezones, airflow.exceptions, airflow.listeners.listener, airflow.models.asset...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `providers/amazon/src/airflow/providers/amazon/aws/hooks/s3.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.624)
- **Top Global Matches:** file_cluster_5: 7.624, file_cluster_12: 8.076, file_cluster_0: 9.939
- **Magnitude:** 1501.82 | **LOC:** 1818 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **50** in-repo importer(s); it depends on **35**; blast radius 0.631; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.0%)
- **Documentation Coverage:** 66.3551% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `list_keys` **(Many-Argument Workhorses)** (Impact: 52.9)
  * `is_keys_unchanged_async` **(Many-Argument Workhorses)** (Impact: 38.7)
  * `copy_object` **(Many-Argument Workhorses)** (Impact: 35.9)
  * `download_file` **(Many-Argument Workhorses)** (Impact: 35.8)
  * `get_files_async` **(Many-Argument Workhorses)** (Impact: 25.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 182 instances
* *Concurrency (weighted view):* 115
* *State Mutation (weighted view):* 573
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 225`, `args: 56`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 209`
* *Architecture:* `io: 13`, `api: 50`, `concurrency: 35`, `import: 36`
* *Defense:* `safety: 21`, `doc: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.631
  * `Choke Point (Betweenness):` 6.8e-05 | `Ripple Effect (Closeness):` 0.009326
  * `Imports (Out-Degree: 10):` __future__, aiobotocore.client, airflow.exceptions, airflow.providers.amazon.aws.exceptions, airflow.providers.amazon.aws.hooks.base_aws, airflow.providers.amazon.aws.utils.tags, airflow.providers.amazon.version_compat, airflow.providers.common.compat.connection...
  * `Imported By (In-Degree: 50):` (Excluded from Brief to save tokens)

### `dev/breeze/src/airflow_breeze/utils/selective_checks.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.357)
- **Top Global Matches:** file_cluster_4: 8.357, file_cluster_5: 9.406, file_cluster_0: 9.41
- **Magnitude:** 1472.38 | **LOC:** 2025 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 38.9%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **26**; blast radius 0.085; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.2%), Guard Balance (formerly Safety Score) (65.7%)
- **Documentation Coverage:** 90.1869% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_check_provider_deps_in_list` **(Many-Argument Workhorses)** (Impact: 44.9)
  * `_get_providers_test_types_to_run` **(Stateful Encapsulated Methods)** (Impact: 36.9)
  * `provider_dependency_bump` **(Defensive Guards)** (Impact: 34.9)
    * *Intent:* """Check for apache-airflow-providers dependency bumps in pyproject.toml files."""
  * `docs_list_as_string` **(Compute Cores)** (Impact: 34.4)
  * `get_job_label` **(Many-Argument Workhorses)** (Impact: 32.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 139 instances
* *State Mutation (weighted view):* 514
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 365`, `structural_boundaries: 414`, `args: 120`, `func_start: 119`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 20`, `high_risk_execution: 4`, `state_mutation: 236`, `planned_debt: 2`
* *Architecture:* `io: 9`, `api: 95`, `import: 28`
* *Defense:* `safety: 22`, `doc: 15`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.00137
  * `Imports (Out-Degree: 11):` __future__, airflow_breeze.branch_defaults, airflow_breeze.global_constants, airflow_breeze.utils.console, airflow_breeze.utils.exclude_from_matrix, airflow_breeze.utils.functools_cache, airflow_breeze.utils.github, airflow_breeze.utils.kubernetes_utils...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `providers/cncf/kubernetes/tests/unit/cncf/kubernetes/operators/test_pod.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.045)
- **Top Global Matches:** file_cluster_15: 7.045, file_cluster_13: 8.101, file_cluster_16: 8.297
- **Magnitude:** 1456.14 | **LOC:** 3174 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.044; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (57.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.2%), Guard Balance (formerly Safety Score) (48.6%), Concurrency Surface (formerly Concurrency) (29.3%)
- **Documentation Coverage:** 83.0435% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_mark_checked_if_not_deleted` **(Many-Argument Workhorses)** (Impact: 27.8)
  * `create_context` **(Many-Argument Workhorses)** (Impact: 24.9)
  * `test_omitted_namespace_with_conn` **(Many-Argument Workhorses)** (Impact: 24.4)
  * `test_pod_with_istio_delete_after_await_container_error` **(Many-Argument Workhorses)** (Impact: 24.1)
  * `test_pod_delete_not_called_when_creation_fails` **(Many-Argument Workhorses)** (Impact: 16.8)
    * *Intent:* """ When pod creation fails, we never get a read of the remote pod. In this case we don't attempt to...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 70 instances
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 677
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 438`, `args: 114`, `func_start: 114`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 537`, `planned_debt: 1`, `unreferenced_by_name: 104`
* *Architecture:* `io: 12`, `api: 117`, `concurrency: 15`, `import: 40`
* *Defense:* `safety: 198`, `doc: 34`, `test: 352`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` __future__, airflow.models, airflow.models.dag_version, airflow.models.xcom, airflow.providers.cncf.kubernetes, airflow.providers.cncf.kubernetes.callbacks, airflow.providers.cncf.kubernetes.operators.pod, airflow.providers.cncf.kubernetes.secret...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `providers/databricks/tests/unit/databricks/hooks/test_databricks.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.369)
- **Top Global Matches:** file_cluster_15: 7.369, file_cluster_12: 8.325, file_cluster_13: 8.38
- **Magnitude:** 1434.1 | **LOC:** 2362 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.044; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (83.2%), Guard Balance (formerly Safety Score) (46.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.8%)
- **Documentation Coverage:** 84.8684% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setup_mock_requests` **(Many-Argument Workhorses)** (Impact: 7.9)
  * `test_get_job_id_by_name_raise_exception_with_duplicates` **(Compute Cores)** (Impact: 4.7)
  * `test_init_bad_retry_limit` **(Compute Cores)** (Impact: 4.4)
  * `test_list_pipelines_raise_exception_with_duplicates` **(Compute Cores)** (Impact: 4.4)
  * `test_get_run_state` **(Defensive Guards)** (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 51 instances
* *Amplified Cascading Flux:* 36 instances
* *Concurrency (weighted view):* 331
* *State Mutation (weighted view):* 449
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 500`, `args: 152`, `func_start: 152`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 377`, `duplicate_logic: 8`, `unreferenced_by_name: 69`
* *Architecture:* `io: 92`, `api: 249`, `concurrency: 76`, `import: 21`
* *Defense:* `safety: 151`, `doc: 38`, `test: 303`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` __future__, aiohttp, airflow.models, airflow.providers.common.compat.sdk, airflow.providers.databricks.hooks.databricks, airflow.providers.databricks.hooks.databricks_base, airflow.providers.databricks.utils, airflow.providers.openlineage.sqlparser...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `shared/module_loading/src/airflow_shared/module_loading/__init__.py` (PYTHON) | Magnitude: 76.08 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 50, branch: 20, import: 14
- `providers/amazon/src/airflow/providers/amazon/aws/transfers/google_api_to_s3.py` (PYTHON) | Magnitude: 60.08 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 29, core_var_decl: 29, design_snake_case: 23
- `airflow-core/src/airflow/observability/metrics/otel_logger.py` (PYTHON) | Magnitude: 17.82 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 20, core_var_decl: 15, design_snake_case: 15, structural_boundaries: 12
- `task-sdk/src/airflow/sdk/observability/metrics/otel_logger.py` (PYTHON) | Magnitude: 17.82 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 20, core_var_decl: 15, design_snake_case: 15, structural_boundaries: 12
- `airflow-core/tests/unit/api/common/test_mark_tasks.py` (PYTHON) | Magnitude: 57.76 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 50, branch: 17, safety: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `providers/amazon/tests/system/amazon/aws/example_lambda.py` (PYTHON) | Magnitude: 22.28 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 42, core_var_decl: 31, design_snake_case: 27
- `providers/microsoft/azure/tests/system/microsoft/azure/example_msgraph.py` (PYTHON) | Magnitude: 19.56 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, core_var_decl: 15, structural_boundaries: 14, design_snake_case: 14
- `providers/fab/tests/unit/fab/auth_manager/api_fastapi/services/test_roles.py` (PYTHON) | Magnitude: 243.82 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 362, structural_boundaries: 127, state_mutation: 116, core_var_decl: 95
- `airflow-core/src/airflow/ui/src/utils/datetimeUtils.ts` (TYPESCRIPT) | Magnitude: 52.62 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 28, branch: 17, core_var_decl: 15
- `airflow-core/src/airflow/ui/src/components/Graph/Edge.tsx` (TYPESCRIPT) | Magnitude: 9.06 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 23, core_var_decl: 16, branch: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `providers/microsoft/azure/tests/unit/microsoft/azure/fs/test_msgraph.py` (PYTHON) | Magnitude: 51.76 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 103, core_var_decl: 40, design_snake_case: 40, structural_boundaries: 24
- `providers/amazon/tests/unit/amazon/aws/sensors/test_dms.py` (PYTHON) | Magnitude: 45.86 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 37, test: 15, safety: 13
- `providers/amazon/tests/unit/amazon/aws/sensors/test_redshift_cluster.py` (PYTHON) | Magnitude: 42.26 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 90, core_var_decl: 41, structural_boundaries: 38, design_snake_case: 36
- `providers/google/tests/unit/google/cloud/hooks/vertex_ai/test_pipeline_job.py` (PYTHON) | Magnitude: 134.54 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 265, core_var_decl: 108, design_snake_case: 104, structural_boundaries: 44
- `providers/amazon/tests/unit/amazon/aws/operators/test_emr_modify_cluster.py` (PYTHON) | Magnitude: 29.58 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 29, indent_spaces: 25, test: 11, core_var_decl: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `shared/secrets_backend/tests/secrets_backend/test_base.py` (PYTHON) | Magnitude: 83.98 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 49, state_mutation: 24, core_var_decl: 21
- `providers/google/tests/unit/google/common/hooks/test_base_google.py` (PYTHON) | Magnitude: 680.42 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 801, structural_boundaries: 263, core_var_decl: 256, design_snake_case: 248
- `providers/snowflake/tests/unit/snowflake/operators/test_snowpark.py` (PYTHON) | Magnitude: 86.84 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 53, core_var_decl: 52, design_snake_case: 46
- `dev/react-plugin-tools/bootstrap.py` (PYTHON) | Magnitude: 92.06 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 88, core_var_decl: 29, design_snake_case: 29, structural_boundaries: 23
- `airflow-core/tests/unit/api_fastapi/core_api/routes/public/test_connections.py` (PYTHON) | Magnitude: 391.42 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1462, structural_boundaries: 232, core_var_decl: 177, design_snake_case: 158

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `airflow-core/tests/unit/cli/commands/test_version_command.py` (PYTHON) | Magnitude: 7.64 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 7, import: 4, api: 3
- `providers/amazon/tests/unit/amazon/aws/sensors/test_sagemaker_training.py` (PYTHON) | Magnitude: 34.96 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 71, core_var_decl: 24, structural_boundaries: 23, design_snake_case: 20
- `providers/fab/tests/unit/fab/auth_manager/api_fastapi/conftest.py` (PYTHON) | Magnitude: 29.56 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 24, indent_spaces: 18, test: 10, args: 7
- `airflow-core/src/airflow/ui/tests/e2e/utils/health.ts` (TYPESCRIPT) | Magnitude: 20.92 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, core_var_decl: 10, structural_boundaries: 9, design_snake_case: 5
- `airflow-core/src/airflow/ui/src/pages/Dag/Code/CodeDiffViewer.tsx` (TYPESCRIPT) | Magnitude: 7.86 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 55, core_var_decl: 15, design_snake_case: 10, structural_boundaries: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `scripts/ci/dockerfiles/krb5-kdc-server/utils/create_service.sh` (SHELL) | Magnitude: 2.38 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: io: 12, structural_boundaries: 7, state_mutation: 6, core_var_decl: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `providers/amazon/tests/unit/amazon/aws/hooks/test_sts.py` (PYTHON) | Magnitude: 4.72 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 3, api: 2, import: 2
- `airflow-core/tests/unit/assets/test_manager.py` (PYTHON) | Magnitude: 141.36 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 198, structural_boundaries: 69, core_var_decl: 63, design_snake_case: 63
- `providers/amazon/tests/unit/amazon/aws/operators/test_eks.py` (PYTHON) | Magnitude: 504.42 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 868, core_var_decl: 279, design_snake_case: 237, structural_boundaries: 163
- `airflow-core/tests/unit/models/test_revoked_token.py` (PYTHON) | Magnitude: 37.06 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 22, state_mutation: 19, core_var_decl: 18
- `docker-tests/tests/docker_tests/test_ci_image.py` (PYTHON) | Magnitude: 5.3 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 8, safety: 4, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `dev/registry/tests/test_merge_registry_data.py` (PYTHON) | Magnitude: 125.68 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 218, core_var_decl: 47, design_snake_case: 47, state_mutation: 46
- `providers/google/tests/system/google/cloud/cloud_run/example_cloud_run_service.py` (PYTHON) | Magnitude: 13.32 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 34, core_var_decl: 25, structural_boundaries: 21, design_snake_case: 21
- `providers/apache/hive/src/airflow/providers/apache/hive/macros/hive.py` (PYTHON) | Magnitude: 84.22 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 24, branch: 15, core_var_decl: 15
- `airflow-core/src/airflow/ui/tests/e2e/pages/RequiredActionsPage.ts` (TYPESCRIPT) | Magnitude: 236.24 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 177, concurrency: 117, structural_boundaries: 110, core_var_decl: 24
- `airflow-core/src/airflow/models/backfill.py` (PYTHON) | Magnitude: 357.26 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 493, core_var_decl: 207, design_snake_case: 200, structural_boundaries: 102

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `.github/workflows/codeql-analysis.yml` (YAML) | Magnitude: 17.84 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 4, import: 4, immutability_locks: 4
- `airflow-core/src/airflow/ui/src/components/FilterBar/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, api: 7, import: 7
- `airflow-core/src/airflow/ui/src/utils/index.ts` (TYPESCRIPT) | Magnitude: 22.16 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, api: 8, import: 8
- `airflow-core/src/airflow/ui/eslint.config.js` (JAVASCRIPT) | Magnitude: 16.5 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 12, import: 11, doc: 3
- `airflow-core/src/airflow/api_fastapi/core_api/routes/public/__init__.py` (PYTHON) | Magnitude: 18.3 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 64, import: 32, core_var_decl: 3, design_snake_case: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `airflow-core/src/airflow/ti_deps/dependencies_deps.py` (PYTHON) | Magnitude: 18.76 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 22, indent_spaces: 20, import: 11, state_mutation: 3
- `chart/dockerfiles/pgbouncer-exporter/build_and_push.sh` (SHELL) | Magnitude: 18.86 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 10, state_mutation: 8, core_var_decl: 8
- `airflow-core/src/airflow/api_fastapi/core_api/routes/public/job.py` (PYTHON) | Magnitude: 29.78 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 26, core_var_decl: 21, design_snake_case: 20
- `providers/microsoft/mssql/tests/unit/microsoft/mssql/dialects/test_mssql.py` (PYTHON) | Magnitude: 36.7 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 178, structural_boundaries: 20, core_var_decl: 16, design_snake_case: 16
- `chart/dockerfiles/pgbouncer/build_and_push.sh` (SHELL) | Magnitude: 20.32 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 11, state_mutation: 9, core_var_decl: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `airflow-core/src/airflow/utils/cli.py` (PYTHON) | Magnitude: 437.3 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 252, structural_boundaries: 122, branch: 76, state_mutation: 74
- `airflow-core/src/airflow/models/xcom.py` (PYTHON) | Magnitude: 236.76 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 242, core_var_decl: 77, structural_boundaries: 72, design_snake_case: 63
- `airflow-core/src/airflow/api_fastapi/core_api/routes/ui/grid.py` (PYTHON) | Magnitude: 289.22 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 379, core_var_decl: 110, design_snake_case: 102, structural_boundaries: 74
- `providers/fab/src/airflow/providers/fab/auth_manager/security_manager/override.py` (PYTHON) | Magnitude: 1865.0 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1709, structural_boundaries: 454, branch: 338, state_mutation: 312
- `providers/fab/src/airflow/providers/fab/auth_manager/cli_commands/role_command.py` (PYTHON) | Magnitude: 158.02 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 131, structural_boundaries: 55, branch: 50, core_var_decl: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `providers/google/src/airflow/providers/google/cloud/transfers/bigquery_to_gcs.py` (PYTHON) | Magnitude: 156.22 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 232, core_var_decl: 82, design_snake_case: 73, structural_boundaries: 52
- `shared/observability/src/airflow_shared/observability/metrics/stats.py` (PYTHON) | Magnitude: 62.7 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 34, state_mutation: 14, core_var_decl: 13
- `providers/teradata/src/airflow/providers/teradata/hooks/teradata.py` (PYTHON) | Magnitude: 218.82 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 157, core_var_decl: 49, structural_boundaries: 48, branch: 46
- `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/hooks/kubernetes.py` (PYTHON) | Magnitude: 999.48 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 790, structural_boundaries: 289, core_var_decl: 211, design_snake_case: 170
- `providers/cncf/kubernetes/src/airflow/providers/cncf/kubernetes/operators/kueue.py` (PYTHON) | Magnitude: 77.48 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 31, branch: 18, state_mutation: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `airflow-core/src/airflow/api_fastapi/execution_api/routes/xcoms.py` (PYTHON) | Magnitude: 349.72 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 308, core_var_decl: 112, design_snake_case: 108, structural_boundaries: 57
- `shared/module_loading/src/airflow_shared/module_loading/file_discovery.py` (PYTHON) | Magnitude: 149.62 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 99, structural_boundaries: 46, branch: 40, core_var_decl: 20
- `providers/amazon/src/airflow/providers/amazon/aws/hooks/redshift_data.py` (PYTHON) | Magnitude: 251.76 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 146, core_var_decl: 61, structural_boundaries: 55, design_snake_case: 41
- `task-sdk/src/airflow/sdk/definitions/_internal/node.py` (PYTHON) | Magnitude: 135.02 | Delta: **0.159** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 40, branch: 35, core_var_decl: 16
- `dev/breeze/src/airflow_breeze/utils/cdxgen.py` (PYTHON) | Magnitude: 579.34 | Delta: **0.168** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 470, branch: 127, structural_boundaries: 109, core_var_decl: 101

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `providers/apache/hive/tests/unit/apache/hive/transfers/test_hive_to_mysql.py` (PYTHON) | Magnitude: 59.24 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 120, core_var_decl: 40, design_snake_case: 39, state_mutation: 29
- `airflow-core/tests/unit/serialization/definitions/test_assets.py` (PYTHON) | Magnitude: 28.52 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 22, core_var_decl: 15, design_snake_case: 15
- `providers/yandex/tests/unit/yandex/utils/test_fields.py` (PYTHON) | Magnitude: 36.7 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 43, core_var_decl: 31, design_snake_case: 31, state_mutation: 18
- `providers/google/tests/unit/google/cloud/sensors/test_vertex_ai.py` (PYTHON) | Magnitude: 80.6 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 97, core_var_decl: 54, design_snake_case: 49, state_mutation: 26
- `providers/salesforce/tests/unit/salesforce/operators/test_bulk.py` (PYTHON) | Magnitude: 79.52 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 185, core_var_decl: 110, design_snake_case: 110, state_mutation: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `providers/google/src/airflow/providers/google/suite/transfers/local_to_drive.py` (PYTHON) | Magnitude: 45.36 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 21, core_var_decl: 20, design_snake_case: 19
- `airflow-core/src/airflow/ui/src/components/FilterBar/utils.ts` (TYPESCRIPT) | Magnitude: 48.8 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 26, branch: 22, core_var_decl: 6
- `airflow-core/src/airflow/migrations/versions/0035_3_0_0_update_user_id_type.py` (PYTHON) | Magnitude: 1.2 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 18, core_var_decl: 12, design_snake_case: 12
- `scripts/ci/prek/vendor_k8s_json_schema.py` (PYTHON) | Magnitude: 46.5 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 17, state_mutation: 13, branch: 12
- `providers/postgres/src/airflow/providers/postgres/dialects/postgres.py` (PYTHON) | Magnitude: 115.44 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 57, branch: 22, structural_boundaries: 20, core_var_decl: 18

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `dev/breeze/src/airflow_breeze/global_constants.py` -> Churn: **100.0%** | Cog Load: 56.1527% | Debt: 11.5223%
- `dev/breeze/src/airflow_breeze/commands/release_management_commands.py` -> Churn: **99.1%** | Cog Load: 51.7099% | Debt: 0.0%
- `airflow-core/src/airflow/jobs/scheduler_job_runner.py` -> Churn: **97.18%** | Cog Load: 51.2978% | Debt: 9.9212%
- `airflow-core/src/airflow/models/taskinstance.py` -> Churn: **86.86%** | Cog Load: 50.1576% | Debt: 8.2511%
- `task-sdk/src/airflow/sdk/execution_time/task_runner.py` -> Churn: **86.86%** | Cog Load: 58.8951% | Debt: 9.9051%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `providers/google/src/airflow/providers/google/cloud/operators/dataplex.py` -> **Ankit Chaurasia** (100.0% isolated ownership) | Magnitude: 1349.8
- `providers/google/src/airflow/providers/google/cloud/hooks/gcs.py` -> **olegkachur-e** (100.0% isolated ownership) | Magnitude: 1150.72
- `providers/google/tests/unit/google/cloud/hooks/test_gcs.py` -> **Tzu-ping Chung** (100.0% isolated ownership) | Magnitude: 1095.94
- `providers/amazon/src/airflow/providers/amazon/aws/hooks/sagemaker.py` -> **Tzu-ping Chung** (100.0% isolated ownership) | Magnitude: 946.62
- `providers/google/tests/unit/google/cloud/triggers/test_dataflow.py` -> **GPK** (100.0% isolated ownership) | Magnitude: 935.22

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `airflow-core/src/airflow/api_fastapi/app.py` -> **Severity: 0.651** (Bridge: 0.0065 * Flux: 100.0%)
- `airflow-core/src/airflow/utils/db.py` -> **Severity: 0.634** (Bridge: 0.0063 * Flux: 100.0%)
- `airflow-core/src/airflow/api_fastapi/core_api/app.py` -> **Severity: 0.628** (Bridge: 0.0063 * Flux: 99.5752%)
- `airflow-core/src/airflow/utils/db_manager.py` -> **Severity: 0.615** (Bridge: 0.0061 * Flux: 100.0%)
- `task-sdk/src/airflow/sdk/definitions/dag.py` -> **Severity: 0.475** (Bridge: 0.0047 * Flux: 99.9999%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `task-sdk/src/airflow/sdk/definitions/context.py` -> **Severity: 12.796** (Embedded: 0.1599 * Error Risk: 80.0%)
- `task-sdk/src/airflow/sdk/configuration.py` -> **Severity: 11.148** (Embedded: 0.1557 * Error Risk: 71.5968%)
- `task-sdk/src/airflow/sdk/bases/decorator.py` -> **Severity: 11.033** (Embedded: 0.1393 * Error Risk: 79.1829%)
- `task-sdk/src/airflow/sdk/definitions/xcom_arg.py` -> **Severity: 10.614** (Embedded: 0.1327 * Error Risk: 80.0%)
- `task-sdk/src/airflow/sdk/bases/skipmixin.py` -> **Severity: 10.445** (Embedded: 0.1552 * Error Risk: 67.3225%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `task-sdk/src/airflow/sdk/__init__.py` -> **Severity: 1780.2** (Blast Radius: 17.802 * Doc Risk: 100.0%)
- `shared/logging/src/airflow_shared/logging/structlog.py` -> **Severity: 1068.792** (Blast Radius: 11.326 * Doc Risk: 94.3662%)
- `shared/logging/src/airflow_shared/logging/_config.py` -> **Severity: 1010.9** (Blast Radius: 10.109 * Doc Risk: 100.0%)
- `task-sdk/src/airflow/sdk/exceptions.py` -> **Severity: 857.92** (Blast Radius: 9.192 * Doc Risk: 93.3333%)
- `airflow-core/src/airflow/models/__init__.py` -> **Severity: 806.5** (Blast Radius: 8.065 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 5015 literal sites + 1965 sites through wrappers = 6980
- **`panics_and_aborts`:** 6804 literal sites + 41 sites through wrappers = 6845

- `console_print` (function, debug_prints, primitive): 1784 call sites in 54 files -- `dev/breeze/src/airflow_breeze/utils/console.py`
- `callable` (function, debug_prints, primitive): 86 call sites in 62 files -- `providers/openlineage/tests/unit/openlineage/extractors/test_python.py`
- `print_in_color` (function, debug_prints, primitive): 13 call sites in 1 files -- `dev/breeze/tests/test_selective_checks.py`
- `_forbidden_response` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `providers/edge3/src/airflow/providers/edge3/worker_api/auth.py`
- `print_stuff` (function, debug_prints, primitive): 5 call sites in 2 files -- `airflow-core/src/airflow/example_dags/libs/helper.py`
- `print_sorted` (function, debug_prints, primitive): 4 call sites in 1 files -- `airflow-core/tests/unit/always/test_project_structure.py`
- `_fetch_user` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `providers/fab/src/airflow/providers/fab/auth_manager/fab_auth_manager.py`
- `_save_dot_to_file` (function, debug_prints, primitive): 3 call sites in 1 files -- `airflow-core/src/airflow/cli/commands/dag_command.py`
- `get_task_map_length` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `task-sdk/src/airflow/sdk/definitions/xcom_arg.py`
- `stop_exec_on_error` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `dev/breeze/src/airflow_breeze/commands/developer_commands.py`
- `_get_rds_instance_endpoint` (function, debug_prints, primitive): 2 call sites in 1 files -- `providers/amazon/tests/system/amazon/aws/example_dms.py`
- `_get_rds_instance_endpoint` (function, debug_prints, primitive): 2 call sites in 1 files -- `providers/amazon/tests/system/amazon/aws/example_dms_serverless.py`
*(+52 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 189303 call pairs -- scoped 36.1%, unique 0.0%, ambiguous 20.6%, external 43.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 182108 | 37.0% | 0.0% | 21.2% | 41.8% |
| typescript | 5104 | 13.0% | 0.0% | 5.7% | 81.3% |
| go | 1006 | 14.1% | 1.7% | 11.3% | 72.9% |
| shell | 743 | 13.3% | 0.3% | 0.0% | 86.4% |
| javascript | 329 | 13.4% | 0.0% | 1.5% | 85.1% |
| java | 13 | 0.0% | 0.0% | 0.0% | 100.0% |

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
